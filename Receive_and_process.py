import subprocess
from kafka import KafkaProducer
import json

# Assuming the TML binary is named 'tml_processor'
maadsdocker/seneca-iot-tml-kafka-amd64 = '/path/to/tml_processor'

# TML Command to receive data
TML_RECEIVE_CMD = [maadsdocker/seneca-iot-tml-kafka-amd64, 'receive']

# Kafka configuration
KAFKA_SERVER = 'kafka:9092'  # Assuming Kafka service is named 'kafka'
KAFKA_TOPIC = 'topic_name'   # Replace with your Kafka topic

# Function to process TML data
def process_tml_data(raw_data):
    # Add your data processing logic here
    processed_data = raw_data.upper()
    return processed_data

# Main function
def main():
    # Execute TML receive command
    raw_data = subprocess.check_output(TML_RECEIVE_CMD, text=True).strip()

    # Process TML data
    processed_data = process_tml_data(raw_data)

    # Initialize Kafka producer
    producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

    # Send processed data to Kafka topic
    producer.send(KAFKA_TOPIC, value=json.dumps(processed_data).encode('utf-8'))
    producer.flush()

if __name__ == "__main__":
    main()
