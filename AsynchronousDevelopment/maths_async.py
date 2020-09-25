import asyncio
import time


async def calculate_number(number):
    answer = [x**2 for x in range(1, number+1)]
    return answer


async def get_numbers(*numbers):
    tasks = []
    for number in numbers:
        tasks.append(calculate_number(number))
    return await asyncio.gather(*tasks)


def main():
    before = time.time()
    loop = asyncio.get_event_loop()
    numbers = [
      1, 3, 6, 10, 16, 21, 420, 500, 3200, 12900, 11008
    ]
    results = loop.run_until_complete(get_numbers(*numbers))
    for result in results:
        print(result)
    loop.close()
    print(f"The time spent on maths with async is {time.time()-before}s")


if __name__ == "__main__":
    main()
