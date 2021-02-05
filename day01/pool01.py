# from multiprocessing import Pool
# import time
#
# def fun(msg):
#     print("msg: %s" %msg)
#     time.sleep(2)

# if __name__ == "__main__":
#     pool = Pool(3)
#     for i in range(5):
#         msg = "hello %s" %i
#         pool.apply_async(fun, args=(msg, ))
#     pool.close()
#     pool.join()

# if __name__ == '__main__':
#     pool = Pool(3)
#     for i in range(5):
#         msg = "hello %s" %i
#         pool.apply(fun, args=(msg, ))
#     pool.close()
#     pool.join()

