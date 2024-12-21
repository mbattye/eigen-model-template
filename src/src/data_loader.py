import pandas as pd

def load_data(file_path):
    """
    Load dataset from a file.
    """
    try:
        data = pd.read_csv(file_path)
        print(f"Data successfully loaded from {file_path}")
        return data
    except Exception as e:
        raise Exception(f"Error loading data: {e}")

def preprocess_data(data, variables):
    """
    Preprocess data: Extract relevant variables.
    """
    try:
        return data[variables]
    except KeyError as e:
        raise Exception(f"Variable(s) not found in dataset: {e}")
