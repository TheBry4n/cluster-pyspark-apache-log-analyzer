# Apache Log Analyzer with PySpark

A batch processing project for analyzing Apache server logs using PySpark DataFrames. Built as a learning project for Big Data technologies.

## 🚀 Quick Start

```bash
# Clone the repository
git clone <your-repo-url>
cd pyspark-apache-log-analysis-2

# Start Spark cluster with Docker
docker compose up -d

# Run the analysis
docker exec spark-app python3 main.py

# Access Spark Web UI at http://localhost:8080
```

## Overview

This project parses Apache log files, cleans the data, and performs basic analytics using PySpark. It demonstrates fundamental Big Data concepts including data cleaning, transformation, and analysis.

The project can run in two modes:
- **Docker mode** (recommended): Full distributed Spark cluster with 1 master and 2 workers
- **Local mode**: Standalone Spark on your local machine

## Features

- 🔍 Parse Apache log files with regex patterns
- 🧹 Data cleaning (remove null/empty values)
- 📅 Timestamp formatting (convert to dd/mm/yyyy and time)
- 📊 Log level analysis (errors, notices, etc.)
- 🔝 Top error frequency analysis
- 📦 Modular code structure
- 🐳 Docker support with multi-node Spark cluster
- 🌐 Web UI monitoring for Spark master and workers

## Project Structure

```
pyspark-apache-log-analysis-2/
├── data/
│   └── apache_test.log          # Sample Apache log file (2000 lines)
├── output/                      # Output directory for results
├── src/
│   ├── config.py                # Configuration (paths, patterns, formats)
│   ├── parser.py                # Log parsing functions
│   ├── cleaner.py               # Data cleaning functions
│   ├── analyzer.py              # Analysis functions
│   └── main.py                  # Main script (orchestrates everything)
├── docker-compose.yaml          # Docker Compose configuration
├── Dockerfile                   # Docker image configuration
├── .env                         # Environment variables for Docker
├── requirements.txt             # Python dependencies
├── .gitignore                   # Git ignore rules
└── README.md                    # This file
```

## Requirements

### Option 1: Docker (Recommended)
- Docker Desktop or Docker Engine
- Docker Compose v2.0+

### Option 2: Local Installation
- Python 3.10+
- PySpark 4.0.1
- Pandas 2.3.3
- Matplotlib 3.10.7 (for visualizations)

## Installation & Usage

### 🐳 Option 1: Using Docker (Recommended)

This is the easiest way to run the project with a full Spark cluster (1 master + 2 workers).

#### 1. Clone the repository
```bash
git clone <your-repo-url>
cd pyspark-apache-log-analysis-2
```

#### 2. Start the Spark cluster with Docker Compose
```bash
docker compose up -d
```

This command will:
- Pull the Apache Spark image
- Build the custom application image
- Start 1 Spark Master node
- Start 2 Spark Worker nodes
- Start the application container

#### 3. Run the log analysis
```bash
docker exec spark-app python3 main.py
```

#### 4. Access Spark Web UIs

Monitor your Spark cluster through the web interfaces:

- **Spark Master UI**: http://localhost:8080
  - View cluster status, workers, and running applications
  
- **Worker 1 UI**: http://localhost:8081
  - Monitor the first worker node
  
- **Worker 2 UI**: http://localhost:8082
  - Monitor the second worker node

#### 5. Useful Docker Commands

```bash
# View logs of a specific container
docker logs spark-master
docker logs spark-app -f  # Follow logs in real-time

# Stop the cluster
docker compose down

# Rebuild and restart the cluster
docker compose up -d --build

# View running containers
docker ps

# Access container shell for debugging
docker exec -it spark-app bash

# Check container resource usage
docker stats
```

#### Docker Cluster Architecture

The setup creates a distributed Spark environment:

```
┌─────────────────┐
│  spark-master   │  (Port 8080: Web UI, 7077: RPC)
│   1 Master Node │
└────────┬────────┘
         │
    ┌────┴────┐
    │         │
┌───▼──┐  ┌───▼──┐
│worker│  │worker│  (Ports 8081, 8082: Web UIs)
│  1   │  │  2   │
└──────┘  └──────┘
    │         │
    └────┬────┘
         │
    ┌────▼────┐
    │spark-app│  (Your application)
    └─────────┘
```

Each worker has:
- 1 CPU core
- 1GB RAM

### 💻 Option 2: Local Installation

#### 1. Clone the repository
```bash
git clone <your-repo-url>
cd pyspark-apache-log-analysis-2
```

#### 2. Create and activate virtual environment
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows PowerShell
# or
source venv/bin/activate      # Linux/Mac
```

#### 3. Install dependencies
```bash
pip install -r requirements.txt
```

#### 4. Run the analysis
```bash
cd src
python main.py
```

> **Note**: Local mode runs Spark in standalone mode on your machine without a distributed cluster.

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
- Distributed computing with Spark clusters
- Docker containerization
- Docker Compose orchestration

## Docker Configuration

### Environment Variables (.env)

```env
SPARK_MASTER_PORT=7077
SPARK_MASTER_URL=spark://spark-master:7077
```

### Docker Compose Services

The `docker-compose.yaml` defines 4 services:

1. **spark-master**: Spark master node (coordinator)
   - Image: `apache/spark:latest`
   - Ports: 8080 (Web UI), 7077 (RPC)
   
2. **spark-worker-1**: First worker node
   - Image: `apache/spark:latest`
   - Port: 8081 (Web UI)
   - Resources: 1 core, 1GB RAM
   
3. **spark-worker-2**: Second worker node
   - Image: `apache/spark:latest`
   - Port: 8082 (Web UI)
   - Resources: 1 core, 1GB RAM
   
4. **spark-app**: Application container
   - Built from `Dockerfile`
   - Includes Python dependencies and source code
   - Connects to master at `spark://spark-master:7077`

### Volume Mounts

All containers share these directories:
- `./data` → `/opt/spark-data` (input data)
- `./output` → `/opt/spark-output` (analysis results)
- `./src` → `/opt/spark-app` (source code - live reload)

### Networking

All services communicate through the `spark-network` bridge network, allowing containers to reference each other by service name (e.g., `spark-master:7077`).

## Troubleshooting

### Docker Issues

**Problem**: Image not found
```bash
# Solution: Pull the image manually
docker pull apache/spark:latest
```

**Problem**: Containers not starting
```bash
# Check logs
docker logs spark-master
docker logs spark-worker-1

# Restart the cluster
docker compose down
docker compose up -d
```

**Problem**: Port already in use
```bash
# Check what's using the port
netstat -ano | findstr :8080  # Windows
lsof -i :8080                  # Linux/Mac

# Or change ports in docker-compose.yaml
```

### Application Issues

**Problem**: File not found
- Make sure your log file is in the `./data` directory
- Verify volume mounts: `docker inspect spark-app`

**Problem**: Workers not connecting
- Check master logs: `docker logs spark-master`
- Verify network: `docker network inspect pyspark-apache-log-analysis-2_spark-network`

## Performance Tuning

To adjust worker resources, edit `docker-compose.yaml`:

```yaml
environment:
  - SPARK_WORKER_MEMORY=2G  # Increase memory
  - SPARK_WORKER_CORES=2    # Increase CPU cores
```

To add more workers, duplicate a worker service with a unique name and port.

## License

Educational project - free to use and modify.

