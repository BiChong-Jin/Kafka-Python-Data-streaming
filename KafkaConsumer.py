import pandas as pd
from kafka import KafkaConsumer, KafkaProducer
from time import sleep
from json import dumps
import json
from s3fs import S3FileSystem

consumer = KafkaConsumer(
    "KafkaTest",
    bootstrap_servers = ["ip address"],
    value_deserializer = lambda x: loads(x.decode("utf-8"))
)

s3 = S3FileSystem()

for index, info in enumerate(consumer):
    with s3.open("s3://kafka-python-project-jin/stock_market_{}.json".format(index), 'w') as file:
        json.dump(info.value, file)
