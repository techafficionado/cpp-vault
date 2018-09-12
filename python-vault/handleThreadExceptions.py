import Queue
import threading

class WorkerThread(threading.Thread):
    def __init__(self, q):
        super(WorkerThread, self).__init__()
        
        self q = q
        self.exception = None
        
    def run():
        try:
            while not self.q.empty():
                item = None
                
                try:
                    item = self.q.get(False)
                    # do your stuff
                except Queue.Empty:
                    pass
                finally:
                    if item:
                        self.q.task_done()
                        
        except Exception as e:
            self.exception = e
        
    def get_exception():
        return self.exception
        

class MyClass:
    def spawn_threads(self, q):
        self.threads = []
        
        for _ in range(NUM_THREADS):
            t = WorkerThread(q)
            self.threads.append(t)
            
            t.start()
            
    def raise_thread_exceptions():
        for t in self.threads:
            e = t.get_exception()
            
            if e:
                raise e
                
    def my_func(self):
        q = Queue.Queue()
        
        # do something and q.put()
        
        self.spawn_threads(q)
        q.join()
        
        # raise exceptions from worker threads
        self.raise_thread_exceptions()        
