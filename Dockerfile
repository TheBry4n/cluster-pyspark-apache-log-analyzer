FROM apache/spark:latest

USER root

# Install Python3 and pip
RUN apt-get update && apt-get install -y python3-pip

WORKDIR /opt/spark-app

# Copy the requirements.txt file and install the dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copy the source code
COPY src/ .

# Set permissions for the source code
RUN chmod -R 755 /opt/spark-app

USER spark

# Run the main script
CMD ["python3", "main.py"]