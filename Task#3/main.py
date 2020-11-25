from threading import Thread, Lock


lock = Lock()
a = 0


def function(arg, thread_number):
    global a
    print(f"Thread #{thread_number}: starting")
    for _ in range(arg):
        lock.acquire()
        a += 1
        lock.release()
    print(f"Thread #{thread_number}: finishing")


def main():
    threads = []
    for val in range(5):
        thread = Thread(target=function, args=(1000000, val,))
        thread.start()
        threads.append(thread)


    [t.join() for t in threads]
    print("----------------------", a)

main()