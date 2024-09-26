from redpanda import RedpandaClient
import random

client = RedpandaClient(bootstrap_servers='localhost:9092')

producer = client.procedur()
for _ in range(100):
    data= random.random()
    producer.send('ml-inputs', value=str(data).encode('utf-8'))

consumer = client.consumer('ml-group')
consumer.subscribe(['ml-inputs'])

for message in consumer:
    data= float(message.value.decode('utf-8'))
    if data > 0.95:
        print(f'Anomaly detectes: {data}')