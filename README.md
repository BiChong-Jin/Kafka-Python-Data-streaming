# Kafka-Python-Data-streaming


## About This Project

A real-time stock data streaming project built using Python, kafka and AWS.


![名称未設定ファイル drawio (2)](https://github.com/user-attachments/assets/bd033244-8a0e-4df2-b636-385cdf55f638)


For making this project:
- Python for data processing and kafka server connections.
- Kafka for real-time data streaming.
- AWS EC2 VM for hosting kafka producer and client server.
- S3 for data storage.
- Amazon Athena for some data managements.




## How to start a kafka server on a linux machine

- Download the source code.
  
  wget https://downloads.apache.org/kafka/3.5.2/kafka_2.12-3.5.2.tgz

  tar -xvf kafka_2.12-3.5.2.tgz
- Make sure have java installed, and then start zoo-keeper

  bin/zookeeper-server-start.sh config/zookeeper.properties
- Start kafka server
  
  export KAFKA_HEAP_OPTS="-Xmx256M -Xms128M"
  
  cd kafka_2.12-3.3.1
  
  bin/kafka-server-start.sh config/server.properties

- Create topics

  cd kafka_2.12-3.3.1
  
  bin/kafka-topics.sh --create --topic KafkaTest --bootstrap-server (your ip address) --replication-factor 1 --partitions 1

- Start Producer

  bin/kafka-console-producer.sh --topic KafkaTest --bootstrap-server (your ip address)

- Start Consumer

  bin/kafka-console-consumer.sh --topic KafkaTest --bootstrap-server (your ip address)


  


