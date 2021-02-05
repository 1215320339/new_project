from multiprocessing import Process, Queue
import random, time


class User:
    def __init__(self, name):
        self.name = name

    def buy(self, q):
        while True:
            time.sleep(1)
            number = random.randint(1, 100)
            q.put(number)
            print("%s 生产了：%d" %(self.name, number))

    def sell(self, q):
        while True:
            time.sleep(1.5)
            result = q.get()
            print("%s 消费了：%d" %(self.name, result))


if __name__ == '__main__':
    q = Queue()
    prodecer = User("张三")
    consumer = User("李四")
    t1 = Process(target=prodecer.buy, args=(q,))
    t1.start()
    t2 = Process(target=consumer.sell, args=(q, ))
    t2.start()

    t1.join()
    t2.join()