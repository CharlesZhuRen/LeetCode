import threading

class SimpleLock:
    def __init__(self):
        self._lock = threading.Lock()

    def acquire(self):
        """获取锁"""
        self._lock.acquire()

    def release(self):
        """释放锁"""
        self._lock.release()

# 示例使用SimpleLock
lock = SimpleLock()

def critical_section():
    print("Critical section start")
    # 模拟临界区代码
    print("Critical section end")

def thread_function():
    lock.acquire()
    try:
        critical_section()
    finally:
        lock.release()

# 创建线程并使用锁
thread1 = threading.Thread(target=thread_function)
thread2 = threading.Thread(target=thread_function)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

