# model.py

# --------------------------------------------------------------
# 📌 Importing Required Libraries
# --------------------------------------------------------------
import pandas as pd
# Linear Regression is a parametric model that fits a straight line (or plane)
# to predict a continuous target variable.
from sklearn.linear_model import LinearRegression

# Decision Tree Regressor is a non-parametric model that splits data into rules.
from sklearn.tree import DecisionTreeRegressor

# Random Forest is an ensemble model (multiple trees combined)
# to reduce overfitting and improve accuracy.
from sklearn.ensemble import RandomForestRegressor

# XGBoost is a powerful Gradient Boosting algorithm that builds trees sequentially
# and corrects the errors of previous trees.
import xgboost as xgb
# train_test_split divides the dataset into training (learn) and testing (evaluate) sets.
from sklearn.model_selection import train_test_split

# Evaluation metrics for regression:
# MAE = Mean Absolute Error → average absolute difference.
# MSE = Mean Squared Error → penalizes big errors.
# R² Score → explains how much variance is captured by the model.
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# --------------------------------------------------------------
# 📌 1. FUNCTION: Split Data
# --------------------------------------------------------------
def split_data(X, y, test_size=0.2, random_state=42):
    """
    Splits features (X) and target (y) into training and testing sets.
    
    - test_size=0.2 → 20% goes to testing, 80% used for training.
    - random_state ensures reproducibility (same split every run).
    """
    return train_test_split(X, y, test_size=test_size, random_state=random_state)


# --------------------------------------------------------------
# 📌 2. FUNCTION: Train All Models
# --------------------------------------------------------------
def train_models(X_train, y_train):
    """
    Trains four regression models safely and efficiently.
    Fixes XGBoost + pandas bug and adds good default hyperparameters
    for the insurance claim severity / premium prediction task.
    
    Args:
        X_train (pd.DataFrame or np.array): Features
        y_train (pd.Series or np.array): Target (e.g., TotalClaims where claim > 0)
    
    Returns:
        tuple: (lr, dt, rf, xgb) trained models
    """
    
    # ===================================================================
    # 1. Safety conversion – this is the key fix for the XGBoost bug
    # ===================================================================
    if isinstance(X_train, pd.DataFrame):
        # Drop any remaining object/category columns (should be none after proper encoding)
        X_train_clean = X_train.select_dtypes(include=['int64', 'float64', 'int32', 'float32'])
        
        # Fill any NaN that might have slipped through (common in insurance data)
        X_train_clean = X_train_clean.fillna(0)
        
        # XGBoost loves float32
        X_train_xgb = X_train_clean.astype('float32')
        X_train_other = X_train_clean  # sklearn models are fine with float64
    else:
        X_train_other = X_train
        X_train_xgb = X_train.astype('float32')

    # ===================================================================
    # 2. Model initialisation with sensible defaults for insurance data
    # ===================================================================
    lr_model = LinearRegression()

    dt_model = DecisionTreeRegressor(
        max_depth=10,
        min_samples_leaf=5,
        random_state=42
    )

    rfr_model = RandomForestRegressor(
        n_estimators=300,
        max_depth=15,
        min_samples_leaf=2,
        n_jobs=-1,
        random_state=42
    )

    xgb_model = xgb.XGBRegressor(
        n_estimators=500,
        learning_rate=0.05,
        max_depth=7,
        subsample=0.8,
        colsample_bytree=0.8,
        reg_alpha=0.1,           # L1 regularisation
        reg_lambda=1.0,          # L2 regularisation
        random_state=42,
        n_jobs=-1,
        tree_method='hist',       # fast & memory-efficient
        enable_categorical=False  # we already encoded everything
    )

    # ===================================================================
    # 3. Train models
    # ===================================================================
    print("Training Linear Regression...")
    lr_model.fit(X_train_other, y_train)

    print("Training Decision Tree...")
    dt_model.fit(X_train_other, y_train)

    print("Training Random Forest...")
    rfr_model.fit(X_train_other, y_train)

    print("Training XGBoost... (this may take 10–30 seconds)")
    xgb_model.fit(X_train_xgb, y_train)   # ← this line will now work perfectly

    print("All 4 models trained successfully!")

    return lr_model, dt_model, rfr_model, xgb_model


# --------------------------------------------------------------
# 📌 3. FUNCTION: Evaluate a Single Model
# --------------------------------------------------------------
def evaluate_model(model, X_test, y_test):
    """
    Predicts on test set and computes:
    - MAE  → average absolute error
    - MSE  → average squared error
    - R²   → goodness of fit (1 = perfect)
    """

    # Make predictions using the trained model
    y_pred = model.predict(X_test)

    # Calculate regression evaluation metrics
    mae = mean_absolute_error(y_test, y_pred)   # Lower = better
    mse = mean_squared_error(y_test, y_pred)    # Lower = better
    r2 = r2_score(y_test, y_pred)               # Higher = better (max = 1)

    return mae, mse, r2, y_pred


# --------------------------------------------------------------
# 📌 4. FUNCTION: Plot Model Comparison
# --------------------------------------------------------------
def plot_metrics(models, mae_scores, mse_scores, r2_scores):
    """
    Visualizes model performance using bar charts.
    Helps compare:
    - MAE accuracy
    - MSE error
    - R² fit score
    """

    import matplotlib.pyplot as plt

    # ---------- Plot MAE ----------
    plt.figure(figsize=(6, 4))
    plt.bar(models, mae_scores, color='skyblue')
    plt.xlabel('Models')
    plt.ylabel('Mean Absolute Error (MAE)')
    plt.title('Comparison of MAE Scores')
    plt.xticks(rotation=45)
    plt.show()

    # ---------- Plot MSE ----------
    plt.figure(figsize=(6, 4))
    plt.bar(models, mse_scores, color='lightgreen')
    plt.xlabel('Models')
    plt.ylabel('Mean Squared Error (MSE)')
    plt.title('Comparison of MSE Scores')
    plt.xticks(rotation=45)
    plt.show()

    # ---------- Plot R² ----------
    plt.figure(figsize=(6, 4))
    plt.bar(models, r2_scores, color='salmon')
    plt.xlabel('Models')
    plt.ylabel('R-squared Score')
    plt.title('Comparison of R-squared Scores')
    plt.xticks(rotation=45)
    plt.show()
