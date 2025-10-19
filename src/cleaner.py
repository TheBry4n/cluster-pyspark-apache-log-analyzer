"""
This module contains the cleaner for the Apache log analyzer.
"""

from pyspark.sql import DataFrame
from pyspark.sql.functions import col, trim, to_timestamp, date_format, when, count
import config

def indentify_dirty_logs(df: DataFrame) -> DataFrame:
    """
    Identify dirty logs in the DataFrame.
    
    Args:
        df: DataFrame containing the logs
    Returns:
        DataFrame containing the dirty logs
    """
    dirty_logs = df.filter(
        col('timestamp').isNull() |
        col('log_level').isNull() |
        col('message').isNull() |
        (trim(col('timestamp')) == '') |
        (trim(col('log_level')) == '') |
        (trim(col('message')) == '') 
    )

    return dirty_logs


def remove_dirty_logs(df: DataFrame) -> DataFrame:
    """
    Remove the dirty logs from the DataFrame.
    
    Args:
        df: DataFrame containing the logs
    Returns:
        DataFrame containing the logs without dirty logs
    """
    clean_data = df.filter(
        col('timestamp').isNotNull() & 
        col('log_level').isNotNull() & 
        col('message').isNotNull() &
        (trim(col('timestamp')) != '') &
        (trim(col('log_level')) != '') &
        (trim(col('message')) != '')
    )

    return clean_data

def convert_timestamp(df: DataFrame) -> DataFrame:
    """
    Convert the timestamp to the correct format.
    
    Args:
        df: DataFrame containing the logs
    Returns:
        DataFrame containing the logs with the correct timestamp format
    """
    df_with_time = df.withColumn(
        'datetime_parsed',
        to_timestamp(col('timestamp'), config.TIMESTAMP_FORMAT_INPUT)
    )

    # Create new formatted columns
    formatted_df = df_with_time.select(
        date_format('datetime_parsed', config.DATE_FORMAT_OUTPUT).alias('date'),
        date_format('datetime_parsed', config.TIME_FORMAT_OUTPUT).alias('time'),
        col('log_level'),
        col('message'),
        col('timestamp').alias('original_timestamp')
    )

    return formatted_df

def print_cleaning_stats(total_rows: int, clean_rows: int, dirty_rows: int) -> None:
    """
    Print the cleaning statistics.
    
    Args:
        total_rows: Total number of rows
        clean_rows: Number of clean rows
        dirty_rows: Number of dirty rows
    Returns:
        None
    """
    print("\n" + "="*60)
    print(" Cleaning Statistics")
    print("="*60)
    print(f"Total rows:  {total_rows}")
    print(f"Clean rows:  {clean_rows}")
    print(f"Dirty rows:  {dirty_rows}")
    print(f"Valid percentage:      {(clean_rows/total_rows)*100:.2f}%")
    print(f"Invalid percentage:    {(dirty_rows/total_rows)*100:.2f}%")
    print("="*60)


def verify_no_null_values(df: DataFrame) -> None:
    """
    Verify that there are no null values in the DataFrame.
    
    Args:
        df: DataFrame containing the logs
    Returns:
        None
    """
    print("\n verify no null values...")
    null_counts = df.select([
        count(when(col(c).isNull(), c)).alias(c)
        for c in df.columns
    ])

    null_counts.show()