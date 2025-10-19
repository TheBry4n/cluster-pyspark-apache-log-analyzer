# Apache Log Analyzer with PySpark

A batch processing project for analyzing Apache server logs using PySpark DataFrames. Built as a learning project for Big Data technologies.

## Overview

This project parses Apache log files, cleans the data, and performs basic analytics using PySpark. It demonstrates fundamental Big Data concepts including data cleaning, transformation, and analysis.

## Features

- Parse Apache log files with regex patterns
- Data cleaning (remove null/empty values)
- Timestamp formatting (convert to dd/mm/yyyy and time)
- Log level analysis (errors, notices, etc.)
- Top error frequency analysis
- Modular code structure

## Project Structure

```
pyspark-apache-log-analysis-2/
├── data/
│   └── apache_test.log          # Sample Apache log file (2000 lines)
├── src/
│   ├── config.py                # Configuration (paths, patterns, formats)
│   ├── parser.py                # Log parsing functions
│   ├── cleaner.py               # Data cleaning functions
│   ├── analyzer.py              # Analysis functions
│   └── main.py                  # Main script (orchestrates everything)
├── requirements.txt             # Python dependencies
├── .gitignore                   # Git ignore rules
└── README.md                    # This file
```

## Requirements

- Python 3.13+
- PySpark 4.0.1
- Pandas 2.3.3
- Matplotlib 3.10.7 (for visualizations)

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd pyspark-apache-log-analysis-2
```

2. Create and activate virtual environment:
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows PowerShell
# or
source venv/bin/activate      # Linux/Mac
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the main script from the `src` directory:

```bash
cd src
python main.py
```

## Output

The script will display:
- Sample parsed logs
- Data cleaning statistics (clean vs dirty rows)
- Null value verification
- Log counts by level (error, notice, etc.)
- Top 10 most frequent errors
- Summary statistics

## Sample Log Format

```
[Sun Dec 04 04:47:44 2005] [notice] workerEnv.init() ok /etc/httpd/conf/workers2.properties
[Sun Dec 04 04:47:44 2005] [error] mod_jk child workerEnv in error state 6
```

Parsed into:
- `date`: 04/12/2005
- `time`: 04:47:44
- `log_level`: notice/error
- `message`: Log message text

## Code Modules

### `config.py`
Contains all configuration constants including file paths, regex patterns, and timestamp formats.

### `parser.py`
Functions to parse raw log files and extract structured data using regex.

### `cleaner.py`
Data cleaning functions:
- Identify dirty data (null/empty values)
- Remove invalid rows
- Format timestamps
- Verify data quality

### `analyzer.py`
Analysis functions:
- Count logs by level
- Find top errors
- Generate summary statistics

### `main.py`
Main orchestrator that:
1. Initializes Spark session
2. Loads log file
3. Parses logs
4. Cleans data
5. Performs analysis
6. Displays results

## Learning Concepts

This project demonstrates:
- PySpark DataFrame operations
- Regex pattern matching
- Data cleaning workflows
- Timestamp manipulation
- Aggregations and grouping
- User-defined functions (UDF)
- Modular code architecture

## License

Educational project - free to use and modify.

