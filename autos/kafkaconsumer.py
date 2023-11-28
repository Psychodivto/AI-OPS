from confluent_kafka import Consumer, KafkaException, KafkaError

class KafkaConsumer:
    def __init__(self, bootstrap_servers, group_id):
        self.bootstrap_servers = bootstrap_servers
        self.group_id = group_id
        self.consumer = Consumer({
            'bootstrap.servers': self.bootstrap_servers,
            'group.id': self.group_id,
            'auto.offset.reset': 'earliest'
        })

    def subscribe(self, topics):
        self.consumer.subscribe(topics)

    def consume(self):
        while True:
            msg = self.consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
                    break
            print('Received message: {}'.format(msg.value().decode('utf-8')))

    def close(self):
        self.consumer.close()


consumer = KafkaConsumer('localhost:9092', group_id='test', topics=['test'])