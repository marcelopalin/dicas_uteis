from concurrent.futures import ProcessPoolExecutor
import os

# https://tutorialedge.net/python/concurrency/python-threadpoolexecutor-tutorial/

def task():
    print("Executing our Task on Process {}".format(os.getpid()))

def main():
    executor = ProcessPoolExecutor(max_workers=3)
    task1 = executor.submit(task)
    task2 = executor.submit(task)

if __name__ == '__main__':
    main()