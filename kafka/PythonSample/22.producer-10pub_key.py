################################################################
# 초당 1회 10회 send
################################################################

import json
import sys
from kafka import KafkaProducer
import configparser
from time import sleep

config  = configparser.ConfigParser()  ## 클래스 객체 생성
config.read('./config.ini', encoding='utf-8')


def producer(topic_name='edu-topic01-a', keyName='key1'):
    bootstrap_servers=config["KAFKAINFO"]["bootstrap_servers"]
    sasl_plain_username=config["KAFKAINFO"]["sasl_plain_username"]
    sasl_plain_password=config["KAFKAINFO"]["sasl_plain_password"]
    topic_name=topic_name
    """
    ex) topic_name : edu-topic01
    """


    print(f"KafkaProducer...")
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                            security_protocol="SASL_PLAINTEXT",
                            sasl_mechanism='SCRAM-SHA-512',
                            ssl_check_hostname=True,
                            sasl_plain_username=sasl_plain_username,
                            sasl_plain_password=sasl_plain_password,
                            key_serializer=str.encode
                            # value_serializer=lambda v: json.dumps(v).encode('utf-8')
                            )

    # 10000건을 1초에 한번씩 발송해보자.
    print(f"topicName[{topic_name}] keyName[{keyName}] Producing...")
    for i in range(10):
        print(i)
        sleep(1)
        producer.send(topic=topic_name, value=b'{"eventName":"a","num":%d,"title":"a", "writeId":"", "writeName": "", "writeDate":"" }' % i, key=keyName)

    # 테스트를 끝내려면 Ctrl + C 로 중지
        
if __name__ == '__main__':
    # key를 아규먼트 로 입력 받는다.
    producer(sys.argv[1], sys.argv[2])
    # producer()

