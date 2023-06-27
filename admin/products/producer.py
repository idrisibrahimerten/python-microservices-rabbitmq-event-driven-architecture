# amqps://argrorjt:rcopNCLgiFnsHCr6oMnmceIPwTXlFcMn@beaver.rmq.cloudamqp.com/argrorjt

import pika, json

params = pika.URLParameters('amqps://argrorjt:rcopNCLgiFnsHCr6oMnmceIPwTXlFcMn@beaver.rmq.cloudamqp.com/argrorjt')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)