import pandas as pd
from kafka import KafkaConsumer, KafkaProducer
from time import sleep
from json import dumps
import json

producer = KafkaProducer(bootstrap_servers=['34.224.39.87:9092'], 
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

producer.send("KafkaTest", value={"Greeting" : "Jin"})

df = pd.read_csv("StockData/StockData.csv")

while True:
    dict_stock = df.sample(1).to_dict(orient="records")[0]
    producer.send("KafkaTest", value = dict_stock)
    sleep(1)