from concurrent.futures import (
    ThreadPoolExecutor,
    wait
)

class Counter:
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count = self.count + 1

def count_up(counter):
    for _ in range(1000000):
        counter.increment()

counter = Counter()
threads = 2
with ThreadPoolExecutor() as e:
    futures = [e.submit(count_up, counter)
                for _ in range(threads)]
    done, not_done = wait(futures)

print(f'counter.count={counter.count}')