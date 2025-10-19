"""
Module for analyzing the Apache logs.
"""

from pyspark.sql import DataFrame
from pyspark.sql.functions import col, count, desc

def count_by_log_level(df: DataFrame) -> DataFrame:
    """
    Count the number of logs by log level.

    Args:
        df: DataFrame containing the logs
    Returns:
        DataFrame containing the number of logs by log level
    """

    return df.groupBy('log_level').count().orderBy(desc('count'))


def top_error_messages(df: DataFrame, limit: int = 10) -> DataFrame:
    """
    Get the top error messages.
    
    Args:
        df: DataFrame containing the logs
        limit: Number of top error messages to return
    Returns:
        DataFrame containing the top error messages
    """
    return df \
        .filter(col('log_level') == 'error') \
        .groupBy('message') \
        .count() \
        .orderBy(desc('count')) \
        .limit(limit)


def print_summary(df: DataFrame) -> None:
    """
    Print the summary of the logs.
    
    Args:
        df: DataFrame containing the logs
    Returns:
        None
    """
    total = df.count()
    errors = df.filter(col('log_level') == 'error').count()
    notices = df.filter(col('log_level') == 'notice').count()

    print("\n" + "="*60)
    print(" Summary of the Logs")
    print("="*60)
    print(f"Total logs:    {total}")
    print(f"Errors:        {errors} ({errors/total*100:.2f}%)")
    print(f"Notices:        {notices} ({notices/total*100:.2f}%)")
    print("="*60)