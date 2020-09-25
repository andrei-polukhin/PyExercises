import time


def calculate_number(number):
    answer = [x**2 for x in range(1, number+1)]
    return answer


def main():
    before = time.time()
    numbers = [500, 3200, 12900, 31008]
    for number in numbers:
        print(calculate_number(number))
    print(f"The time spent on maths without async is {time.time()-before} secs.")


if __name__ == "__main__":
    main()
