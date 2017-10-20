# i=0
# while(i<10):
#     i+=1
#     msg='hello world' + str(i)
#     #msg2= msg + str(i)
#     print msg
#     print "send msg: %s" % msg
#     
# from random import randint
# max_size =10
# data1 =[x for x in range(max_size)]
# print data1
# data2 =[randint(0,max_size) for _ in range(max_size)]
# print data2





for i in range(20000):
    message = "Hello World!"
    message= message+str(i)
#     #channel.basic_publish(exchange='',routing_key='task_queue',body=message,properties=pika.BasicProperties(delivery_mode = 2,))
    print(" [x] Sent %r" % message)