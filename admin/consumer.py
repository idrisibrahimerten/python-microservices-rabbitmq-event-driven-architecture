import pika 

params = pika.URLParameters('amqps://argrorjt:rcopNCLgiFnsHCr6oMnmceIPwTXlFcMn@beaver.rmq.cloudamqp.com/argrorjt')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Adminden gelen mesaj')
    print(body)

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Başla bakalım.')

channel.start_consuming()

channel.close()

