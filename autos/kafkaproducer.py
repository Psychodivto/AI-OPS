from confluent_kafka import Producer

class KafkaProducer:
    def __init__(self, bootstrap_servers):
        self.bootstrap_servers = bootstrap_servers
        self.producer = Producer({'bootstrap.servers': self.bootstrap_servers})

    def send(self, topic, message):
        self.producer.produce(topic, message)
        self.producer.flush()
        print('Message published successfully to Kafka Topic: {}'.format(topic))

    def close(self):
        self.producer.close()

# Path: AI-OPS/autos/kafkaproducer.py
# Compare this snippet from AI-OPS/autos/schema.py:

# kafka_prodiucer = KafkaProducer(bootstrap_servers='localhost:9092')

producer = KafkaProducer(bootstrap_servers='localhost:9092', group_id='test', topics=['test'])
producer.send('test', b'Hola desde django')