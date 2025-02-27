import threading
class DiningPhilosophers:
    def __init__(self):
        self.locks = [threading.Lock() for _ in range(5)]
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        first_fork, second_fork = sorted([philosopher, (philosopher + 1) % 5])
        with self.locks[first_fork]:
            with self.locks[second_fork]:
                pickLeftFork()
                pickRightFork()
                eat()
                putLeftFork()
                putRightFork()
#Runtime Complexity: O(1)
#Space Complexity: O(1)