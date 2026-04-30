import pika
import json
from decouple import config

def publier_message(message: dict):
    try:
        rabbitmq_host = config('RABBITMQ_HOST', default='localhost')
        
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbitmq_host)
        )
        channel = connection.channel()

        channel.queue_declare(queue='reservations_queue', durable=True)

        channel.basic_publish(
            exchange='',
            routing_key='reservations_queue',
            body=json.dumps(message),
            properties=pika.BasicProperties(delivery_mode=2)
        )

        connection.close()
        print(f"[RabbitMQ] ✅ Message publié : {message}")

    except Exception as e:
        print(f"[RabbitMQ] ❌ Erreur : {e}")