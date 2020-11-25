from multiprocessing import Pool


def function(arg):
    a = 0
    for _ in range(arg):
        a += 1
    return a


def main():
    args = [1000000, 1000000, 1000000, 1000000, 1000000]
    pool = Pool(processes=5)
    result = pool.map(function, args)
    print("----------------------", sum(result)) 
 

main()