from threading import Lock

class Foo:
    def __init__(self):
        self.firstjobDone = Lock()
        self.secondjobDone = Lock()
        self.firstjobDone.acquire()
        self.secondjobDone.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()

        self.firstjobDone.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        
        with self.firstjobDone:
            printSecond()

            self.secondjobDone.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        
        with self.secondjobDone:
            printThird()
