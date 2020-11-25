from threading import Lock
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass

@dataclass
class A:
    val : int


def function(arg):
    for _ in range(arg[0]):
        arg[1].acquire()
        arg[2].val += 1
        arg[1].release()


def main():
    lock = Lock()
    a = A(0)
    args = [ [1000000, lock, a] ] * 5
    with ThreadPoolExecutor() as executor:
        executor.map(function, args)

    print("----------------------", a.val)


main()