from readerwriterlock import rwlock

class Bus(object):
    def __init__(self):
        self.message = 0
        self.lock = rwlock.RWLockWriteD()

    def write(self,message):
        wlock = self.lock.gen_wlock()
        if wlock.acquire(blocking=True, timeout=0.5):
            try:
                self.message = message
            finally:
                wlock.release()

    def read(self):
        rlock = self.lock.gen_rlock()
        if rlock.acquire(blocking=True, timeout=0.5):
            try:
                message = self.message
                return message
            finally:
                rlock.release()