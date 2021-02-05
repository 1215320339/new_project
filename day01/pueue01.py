from multiprocessing import Process, Queue
import time, os

class Production(Process):

    def __init__(self, name, q, prices=[]):
        super().__init__()
        self.name = name
        self.prices = prices
        self.q = q

    def run(self):
        for item in self.prices:
            time.sleep(1.5)
            print("%d---%s生产:%f" %(os.getpid(), self.name, item))
            self.q.put(item)

class Consumer(Process):

    def __init__(self, name, q):
        super().__init__()
        self.name = name
        self.q = q

    def run(self):
        while True:
            try:
                result = self.q.get(timeout=3)
                print("%d---%s消费：%f" %(os.getpid(), self.name, result))
            except:
                break
if __name__ == '__main__':
    q = Queue()
    prices1 = [1.2, 3.45, 5.66, 0]
    prices2 = [1, 2, 3, 4, 5, 6]
    q1 = Production("lilei", q, prices1)
    q3 = Production("tom", q, prices2)
    q2 = Consumer("hanmeimei", q)
    q1.start()
    q3.start()
    q2.start()
    q1.join()
    q2.join()
    q3.join()