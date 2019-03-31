'''
演示多线程
'''

import  threading
import  time

threadLock = threading.Lock()
threads = []

class myThread(threading.Thread):

    def __init__(self,_threadID,_name,_delay):
        threading.Thread.__init__(self)
        self.threadID =_threadID
        self.name=_name
        self.delay = _delay

    def run(self):
        print('%s线程启动' %(self.name))
        # 获取锁，用于线程同步
        threadLock.acquire()
        self.print_time(self.name, self.delay, 3)
        # 释放锁，开启下一个线程
        threadLock.release()

    def print_time(self,threadName, delay, counter):
        while counter:
            time.sleep(delay)
            print("%s: %s" % (threadName, time.ctime(time.time())))
            counter -= 1
# 创建新线程
thread1=myThread(1, "Thread-1", 1)
thread2=myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()
print ("退出主线程")