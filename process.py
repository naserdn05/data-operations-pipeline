import pandas as pd
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def process_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Transform and clean the DataFrame:
    - Normalize column names
    - Fill missing values
    - Convert data types
    - Add processing timestamp
    """
    if data is None or data.empty:
        logger.error("No data to process")
        return None

    try:
        logger.info("=== Starting Data Processing ===")
        
        # Normalize column names
        data.columns = data.columns.str.strip().str.lower().str.replace(' ', '_')
        logger.info(f"Columns normalized: {list(data.columns)}")

        # Fill missing values
        for col in data.select_dtypes(include='number').columns:
            data[col] = data[col].fillna(data[col].median())
        for col in data.select_dtypes(include='object').columns:
            data[col] = data[col].fillna('unknown')

        # Add metadata
        data['processed_at'] = datetime.now().isoformat()

        logger.info(f"Processed rows: {len(data)}")
        logger.info(f"Processing completed at: {datetime.now().isoformat()}")

        return data

    except Exception as e:
        logger.error(f"Processing error: {e}")
        return None

if __name__ == "__main__":
    df = pd.read_csv("customers.csv")
    process_data(df)
