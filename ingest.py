import pandas as pd

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully")
        print(data.head())
        return data
    except Exception as e:
        print("Error loading data:", e)
        return None


if __name__ == "__main__":
    file = "customers.csv"
    load_data(file)