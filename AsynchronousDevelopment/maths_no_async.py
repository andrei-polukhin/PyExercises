import time


def calculate_number(number):
    answer = [x**2 for x in range(1, number+1)]
    return answer


def main():
    before = time.time()
    numbers = [1, 3, 6, 10, 16, 21, 420, 500, 3200, 12900, 11008]
    for number in numbers:
        print(calculate_number(number))
    print(f"The time spent for maths without async is {time.time()-before}s")


if __name__ == "__main__":
    main()
