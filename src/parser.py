"""
This module contains the parser for the Apache log analyzer.
"""

from pyspark.sql import DataFrame
from pyspark.sql.functions import regexp_extract
import config

def parse_raw_logs(raw_logs: DataFrame) -> DataFrame:
    """
    Parse the raw logs into a structured DataFrame.

    Args:
        raw_logs: DataFrame containing the raw logs
    
    Returns:
        DataFrame containing the parsed logs
    """
    parsed_logs = raw_logs.select(
        regexp_extract('value', config.TIMESTAMP_PATTERN, 1).alias('timestamp'),
        regexp_extract('value', config.LOG_LEVEL_PATTERN, 1).alias('log_level'),
        regexp_extract('value', config.MESSAGE_PATTERN, 1).alias('message'),
    )

    return parsed_logs


def show_sample_logs(df: DataFrame, num_rows: int = 10, title: str = "Sample Logs") -> None:
    """
    Show a sample of the parsed logs.

    Args:
        df: DataFrame containing the parsed logs
        num_rows: Number of rows to show
        title: Title of the sample logs
    
    Returns:
        None
    """
    print(f"\n{'='*60}")
    print(f"  {title}")
    print('='*60)
    df.show(num_rows, truncate=False)