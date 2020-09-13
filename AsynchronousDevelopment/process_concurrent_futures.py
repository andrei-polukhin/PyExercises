import time
from concurrent.futures import ProcessPoolExecutor


####### SINGLE THREAD
def ask_user():
    start = time.time()
    user_input = input("Enter your name: ")
    greet = f"Hello, {user_input}"
    print(greet)
    print("ask_user: ", time.time() - start)


def complex_calculation():
    print("Started calculating...")
    start = time.time()
    [x**2 for x in range(20000000)]
    print("complex_calculation: ", time.time() - start)


start = time.time()
ask_user()
complex_calculation()
print("Single thread total time: ", time.time() - start, "\n\n")

# We should use multithreading - if there is waiting
# and multiprocesses - if we need to do sth simultaneously
# NOTE: the code below works for quadcore processors (like mine)
start = time.time()

with ProcessPoolExecutor(max_workers=4) as pool:
    pool.submit(complex_calculation)
    pool.submit(complex_calculation)
    pool.submit(complex_calculation)
    pool.submit(complex_calculation)

print(f"Four processes join time: {time.time() - start}")
