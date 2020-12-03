from threading import Lock
from concurrent.futures import ThreadPoolExecutor


class ThreadSafeCounter:
    def __init__(self):
        self._value = 0
        self._lock = Lock()
    

    def locked_update(self, number_of_increments):
        for _ in range(number_of_increments):
            with self._lock:
                self._value += 1
    

    def __str__(self):
        return str(self._value)


def main():
    counter = ThreadSafeCounter()
    number_of_increments = 1000000
    with ThreadPoolExecutor() as executor:
        for _ in range(5):
            executor.submit(counter.locked_update, number_of_increments)

    print("----------------------", counter)


main()