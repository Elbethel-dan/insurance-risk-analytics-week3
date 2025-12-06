import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """
    Load data from CSV, Excel, JSON, or TXT files based on file extension.
    Supported formats: .csv, .xlsx, .xls, .json, .txt
    """

    # ---- NEW: helper function inside load_data ----
    def load_txt_as_csv(path: str, delimiter: str = "|") -> pd.DataFrame:
        """
        Internal helper: Load a TXT file as if it were a CSV.
        """
        return pd.read_csv(path, sep=delimiter)
    # ------------------------------------------------

    file_ext = file_path.lower().split('.')[-1]

    try:
        if file_ext == "csv":
            return pd.read_csv(file_path)

        elif file_ext in ("xlsx", "xls"):
            return pd.read_excel(file_path)

        elif file_ext == "json":
            return pd.read_json(file_path, lines=True)

        elif file_ext == "txt":
            # Your original TXT behavior (kept exactly the same)
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.read().splitlines()
            return pd.DataFrame(lines, columns=["text"])

        else:
            raise ValueError(f"Unsupported file type: .{file_ext}")

    except Exception as e:
        raise ValueError(f"Failed to load file '{file_path}': {e}")
