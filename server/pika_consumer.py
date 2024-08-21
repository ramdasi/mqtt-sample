import pika
import json
import datetime
import traceback
from mongo_handler import save_to_mongo
global channel
def status_consumer(ch, method, properties, body):
    try:
        print(f"Received Data:  {body}")
        body = json.loads(body.decode("utf8").replace("'", '"'))
        body["createdAt"] = datetime.datetime.now()
        body["updatedAt"] = datetime.datetime.now()
        body["detectionTime"] = datetime.datetime.fromisoformat(body["detectionTime"])
        save_to_mongo(body, "sensorStatuses")
        ch.basic_ack(method.delivery_tag)
    except Exception as e:
        print(f"Invalid Data:  {body} {e}")
        save_to_mongo(
            {
                "data": str(body),
                "exception": e,
                "createdAt": datetime.datetime.now(),
                "updatedAt": datetime.datetime.now(),
            },
            "invalidStatuses",
        )
        ch.basic_ack(method.delivery_tag)

def start_consumer():
    global channel
    connection = pika.BlockingConnection(
        pika.URLParameters(
            "amqps://bqwvgzdd:w0STgD6LNKmO-0RaqYHQfZ9mQufuV_nl@puffin.rmq2.cloudamqp.com:5671/bqwvgzdd"
        )
    )
    channel = connection.channel()
    channel.queue_declare(queue="sensor")
    channel.basic_consume(
        queue="sensor", auto_ack=False, on_message_callback=status_consumer
    )
    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()

    
def stop_consumer():
    global channel
    channel.stop_consuming()
    channel.close()