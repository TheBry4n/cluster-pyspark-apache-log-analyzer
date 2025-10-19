"""
Apache Log Analyzer - Main script
Educational project to learn PySpark and Big Data
"""

from pyspark.sql import SparkSession
import parser
import cleaner
import analyzer
import config

def main():
    # Initialize Spark session

    spark = SparkSession.builder \
        .appName("Apache Log Analyzer") \
        .master("local[*]") 
    
    for key, value in config.SPARK_CONFIGS.items():
        spark = spark.config(key, value)
    
    spark = spark.getOrCreate()
    spark.sparkContext.setLogLevel(config.SPARK_LOG_LEVEL)

    print("\n Apache Log Analyzer - Starting...")

    # Load log file into DataFrame
    print(f"\n Loading log file from: {config.LOG_FILE_PATH}")
    raw_logs = spark.read.text(config.LOG_FILE_PATH)

    # Parse the raw logs
    print("\n Parsing the raw logs...")
    parsed_logs = parser.parse_raw_logs(raw_logs)
    parser.show_sample_logs(parsed_logs, num_rows=10, title="Sample Parsed Logs")

    # Clean the logs
    print("\n Cleaning the logs...")
    dirty_data = cleaner.indentify_dirty_logs(parsed_logs)
    dirty_count = dirty_data.count()
    print(f"\n Found {dirty_count} dirty logs")

    if dirty_count > 0:
        parser.show_sample_logs(dirty_data, num_rows=10, title="Sample Dirty Logs")
        print("\n Removing the dirty logs...")
        clean_data = cleaner.remove_dirty_logs(parsed_logs)
        print("\n Formatting the timestamp...")
        final_clean_data = cleaner.convert_timestamp(clean_data)
    else:
        print("\n Formatting the timestamp...")
        final_clean_data = cleaner.convert_timestamp(parsed_logs)

    # Print the cleaning statistics
    print("\n Printing the cleaning statistics...")
    total_rows = parsed_logs.count()
    clean_rows = final_clean_data.count()
    cleaner.print_cleaning_stats(total_rows, clean_rows, dirty_count)

    # Verify no null values
    print("\n Verifying no null values...")
    cleaner.verify_no_null_values(final_clean_data)

    parser.show_sample_logs(final_clean_data, num_rows=10, title="Sample Final Clean Data")

    # Analyze the logs
    print("\n Analyzing the logs...")

    # Count by log level
    print("\n Counting by log level...")
    log_level_counts = analyzer.count_by_log_level(final_clean_data)
    log_level_counts.show()

    # Top error messages
    print("\n Getting the top error messages...")
    top_error_messages = analyzer.top_error_messages(final_clean_data)
    top_error_messages.show()

    # Print the summary
    analyzer.print_summary(final_clean_data)

    # Stop the Spark session
    print("\n Analysis complete. Stopping Spark session...")
    spark.stop()

if __name__ == "__main__":
    main()