import pandas as pd
import logging
import os
from datetime import datetime

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def load_data(file_path: str) -> pd.DataFrame:
    """
    Load data from CSV or JSON file into a DataFrame.
    Supports: .csv, .json, .parquet
    """
    if not os.path.exists(file_path):
        logger.error(f"File not found: {file_path}")
        return None

    try:
        ext = os.path.splitext(file_path)[1].lower()
        
        if ext == '.csv':
            data = pd.read_csv(file_path)
        elif ext == '.json':
            data = pd.read_json(file_path)
        elif ext == '.parquet':
            data = pd.read_parquet(file_path)
        else:
            logger.error(f"Unsupported file type: {ext}")
            return None

        logger.info(f"Data loaded successfully from {file_path}")
        logger.info(f"Shape: {data.shape[0]} rows, {data.shape[1]} columns")
        logger.info(f"Columns: {list(data.columns)}")
        logger.info(f"Ingestion timestamp: {datetime.now().isoformat()}")
        
        return data

    except Exception as e:
        logger.error(f"Error loading data: {e}")
        return None

if __name__ == "__main__":
    file = "customers.csv"
    df = load_data(file)
