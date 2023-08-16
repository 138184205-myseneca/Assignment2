from kafka import KafkaProducer
import json

# Kafka configuration
KAFKA_SERVER = 'kafka:9092'  # Assuming Kafka service is named 'kafka'
KAFKA_TOPIC = 'topic_name'   # Replace with your Kafka topic

# Sample data to send
sample_data = {
    "key": "value",
    "another_key": "another_value"
}

# Main function
def main():
    # Initialize Kafka producer
    producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

    # Send sample data to Kafka topic
    producer.send(KAFKA_TOPIC, value=json.dumps(sample_data).encode('utf-8'))
    producer.flush()

if __name__ == "__main__":
    main()
