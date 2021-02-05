from multiprocessing import Pool
import os, time, random


class Test:

    def lee(self):
        print("进程号：%s" %os.getpid())
        start = time.time()
        time.sleep(random.random() * 10)
        end = time.time()
        print("用时：%f" %(end-start))

    def marlon(self):
        print("进程号：%s" %os.getpid())
        start = time.time()
        time.sleep(random.random() * 20)
        end = time.time()
        print("用时：%f" %(end-start))

    def allen(self):
        print("进程号：%s" %os.getpid())
        start = time.time()
        time.sleep(random.random() * 30)
        end = time.time()
        print("用时：%f" %(end-start))

if __name__ == '__main__':
    test = Test()
    fun_list = [test.lee, test.allen, test.marlon]
    pool = Pool(2)
    for item in fun_list:
        pool.apply_async(item)

    pool.close()
    pool.join()
