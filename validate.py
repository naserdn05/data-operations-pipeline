import pandas as pd
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def validate_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Validate DataFrame: check nulls, duplicates, and data types.
    """
    if data is None or data.empty:
        logger.error("No data to validate")
        return None

    try:
        logger.info("=== Starting Data Validation ===")
        
        # Check missing values
        missing = data.isnull().sum()
        missing_pct = (missing / len(data) * 100).round(2)
        logger.info(f"Missing values:\n{missing[missing > 0]}")
        logger.info(f"Missing percentage:\n{missing_pct[missing_pct > 0]}")

        # Check duplicates
        duplicates = data.duplicated().sum()
        logger.info(f"Duplicate rows found: {duplicates}")
        if duplicates > 0:
            data = data.drop_duplicates()
            logger.info("Duplicates removed")

        # Check data types
        logger.info(f"Data types:\n{data.dtypes}")
        
        # Basic stats
        logger.info(f"Dataset shape after validation: {data.shape}")
        logger.info(f"Validation completed at: {datetime.now().isoformat()}")
        
        return data

    except Exception as e:
        logger.error(f"Validation error: {e}")
        return None

if __name__ == "__main__":
    import pandas as pd
    df = pd.read_csv("customers.csv")
    validate_data(df)
