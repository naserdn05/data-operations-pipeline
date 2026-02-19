import pandas as pd

def validate_data(file_path):
    try:
        data = pd.read_csv(file_path)

        print("Checking missing values...")
        print(data.isnull().sum())

        print("\nChecking duplicate rows...")
        duplicates = data.duplicated().sum()
        print("Duplicate rows:", duplicates)

        if duplicates > 0:
            data = data.drop_duplicates()
            print("Duplicates removed")

        print("\nData validation completed")
        return data

    except Exception as e:
        print("Validation error:", e)
        return None


if __name__ == "__main__":
    file = "customers.csv"
    validate_data(file)
