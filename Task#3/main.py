from threading import Lock
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass

@dataclass
class A:
    val : int


def function(arg, lock, a):
    for _ in range(arg):
        lock.acquire()
        a.val += 1
        lock.release()


def main():
    lock = Lock()
    a = A(0)
    arg = 1000000
    with ThreadPoolExecutor() as executor:
        for _ in range(5):
            executor.submit(function, arg, lock, a)

    print("----------------------", a.val)


main()