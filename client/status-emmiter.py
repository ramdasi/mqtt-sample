import pika
import random
import time
import datetime
import json

connection = pika.BlockingConnection(
    pika.URLParameters(
        "amqps://bqwvgzdd:w0STgD6LNKmO-0RaqYHQfZ9mQufuV_nl@puffin.rmq2.cloudamqp.com:5671/bqwvgzdd"
    )
)
channel = connection.channel()

channel = connection.channel()
channel.queue_declare(queue="sensor")
while 1:
    randomStat = {
        "status": str(random.randrange(1, 7)),
        "detectionTime": datetime.datetime.now().isoformat(),
    }
    channel.basic_publish(
        exchange="", routing_key="sensor", body=json.dumps(randomStat)
    )
    print("sent: ", json.dumps(randomStat))
    time.sleep(1)
# if(channel.is_open):
connection.close()
