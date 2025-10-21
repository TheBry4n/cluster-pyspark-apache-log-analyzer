"""
This module contains the configuration for the Apache log analyzer.
"""

import os

# Path
if os.path.exists("/opt/spark-data"):
    LOG_FILE_PATH = "/opt/spark-data/apache_test.log"
    OUTPUT_DIR = "/opt/spark-output"
else:
    LOG_FILE_PATH = "data/apache_test.log"
    OUTPUT_DIR = "output"

# Regex patterns for parsing
TIMESTAMP_PATTERN = r'\[(.*?)\]'
LOG_LEVEL_PATTERN = r'\]\s\[(.*?)\]'
MESSAGE_PATTERN = r'\]\s\[.*?\]\s(.*)'

# Timestamp format
TIMESTAMP_FORMAT_INPUT = 'E MMM dd HH:mm:ss yyyy'
DATE_FORMAT_OUTPUT = 'dd/MM/yyyy'
TIME_FORMAT_OUTPUT = 'HH:mm:ss'

# Spark log level
SPARK_LOG_LEVEL = "ERROR"

# Spark Configuration
SPARK_CONFIGS = {
    "spark.sql.legacy.timeParserPolicy": "LEGACY"
}