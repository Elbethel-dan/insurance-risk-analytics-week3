import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class Plotter:
    """
    Reusable Plotter module for common visualizations.
    Supports: histogram, bar chart, line plot, scatter plot, box plot, heatmap.
    """

    def __init__(self, style="whitegrid"):
        sns.set_style(style)

    def histogram(self, data, column, bins=30, title=None, xlabel=None, ylabel="Frequency"):
        plt.figure(figsize=(8, 5))
        sns.histplot(data[column], bins=bins, kde=True)
        plt.title(title or f"Histogram of {column}")
        plt.xlabel(xlabel or column)
        plt.ylabel(ylabel)
        plt.show()

    def bar_chart(self, data, x, y, title=None, xlabel=None, ylabel=None):
        plt.figure(figsize=(8, 5))
        sns.barplot(x=x, y=y, data=data)
        plt.title(title or f"Bar Chart of {y} by {x}")
        plt.xlabel(xlabel or x)
        plt.ylabel(ylabel or y)
        plt.show()

    def line_plot(self, data, x, y, title=None, xlabel=None, ylabel=None):
        plt.figure(figsize=(8, 5))
        sns.lineplot(x=x, y=y, data=data)
        plt.title(title or f"Line Plot of {y} over {x}")
        plt.xlabel(xlabel or x)
        plt.ylabel(ylabel or y)
        plt.show()

    def scatter_plot(self, data, x, y, title=None, xlabel=None, ylabel=None):
        plt.figure(figsize=(8, 5))
        sns.scatterplot(x=x, y=y, data=data)
        plt.title(title or f"Scatter Plot: {x} vs {y}")
        plt.xlabel(xlabel or x)
        plt.ylabel(ylabel or y)
        plt.show()

    def box_plot(self, data, column, by=None, title=None, xlabel=None, ylabel=None):
        plt.figure(figsize=(8, 5))
        if by:
            sns.boxplot(x=by, y=column, data=data)
            plt.title(title or f"Box Plot of {column} by {by}")
            plt.xlabel(xlabel or by)
            plt.ylabel(ylabel or column)
        else:
            sns.boxplot(y=data[column])
            plt.title(title or f"Box Plot of {column}")
            plt.ylabel(ylabel or column)
        plt.show()

    def heatmap(self, data, title="Correlation Heatmap"):
        plt.figure(figsize=(10, 6))
        corr = data.corr()
        sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
        plt.title(title)
        plt.show()

    # Additional EDA Plots
    def count_plot(self, data, column, title=None, xlabel=None, ylabel="Count", rotation=None):
        plt.figure(figsize=(14, 6))
        sns.countplot(x=column, data=data)
        plt.title(title or f"Count Plot of {column}")
        plt.xlabel(xlabel or column)
        plt.ylabel(ylabel)

        # auto-rotate long labels
        if rotation is not None:
            plt.xticks(rotation=rotation, ha='right')
        else:
            plt.xticks(rotation=45 if data[column].nunique() > 5 else 0, ha='right')

        plt.tight_layout()
        plt.show()


    def kde_plot(self, data, column, title=None, xlabel=None, ylabel="Density"):
        plt.figure(figsize=(8, 5))
        sns.kdeplot(data[column], shade=True)
        plt.title(title or f"KDE Plot of {column}")
        plt.xlabel(xlabel or column)
        plt.ylabel(ylabel)
        plt.show()

    def violin_plot(self, data, column, by=None, title=None, xlabel=None, ylabel=None):
        plt.figure(figsize=(8, 5))
        sns.violinplot(x=by, y=column, data=data) if by else sns.violinplot(y=data[column])
        plt.title(title or f"Violin Plot of {column}")
        if by:
            plt.xlabel(xlabel or by)
        plt.ylabel(ylabel or column)
        plt.show()

    def pair_plot(self, data, title="Pair Plot"):
        sns.pairplot(data)
        plt.suptitle(title, y=1.02)
        plt.show()

    def joint_plot(self, data, x, y, kind="scatter", title=None):
        plot = sns.jointplot(x=x, y=y, data=data, kind=kind)
        plot.fig.suptitle(title or f"Joint Plot of {x} vs {y}")
        plot.fig.tight_layout()
        plot.fig.subplots_adjust(top=0.95)
        plt.show()

    def swarm_plot(self, data, x, y, title=None, xlabel=None, ylabel=None):
        plt.figure(figsize=(8, 5))
        sns.swarmplot(x=x, y=y, data=data)
        plt.title(title or f"Swarm Plot of {y} by {x}")
        plt.xlabel(xlabel or x)
        plt.ylabel(ylabel or y)
        plt.show()

    def horizontal_bar_chart(self, data, y, x, title=None, xlabel=None, ylabel=None):
        plt.figure(figsize=(8, 5))
        sns.barplot(y=y, x=x, data=data)
        plt.title(title or f"Bar Chart of {x} by {y}")
        plt.xlabel(xlabel or x)
        plt.ylabel(ylabel or y)
        plt.show()
