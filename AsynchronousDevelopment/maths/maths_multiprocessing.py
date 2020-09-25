import time
from concurrent.futures import ProcessPoolExecutor


def calculate_number(number):
    answer = [x**2 for x in range(1, number+1)]
    return answer


def main():
    before = time.time()
    numbers = [500, 3200, 12900, 31008]
    processes = []
    with ProcessPoolExecutor(max_workers=len(numbers)) as pool:
        for number in numbers:
            process = pool.submit(calculate_number, number=number)
            processes.append(process)
    for task in processes:
        print(task.result())
    print(f"Four processes join time: {time.time() - before} secs.")


if __name__ == "__main__":
    main()
