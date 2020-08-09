import time
from multiprocessing import Process


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

## Processes

# process = Process(target=complex_calculation)
# process2 = Process(target=ask_user)
# process.start()
# process2.start()

# start = time.time()

# process.join()
# process2.join()
# """Boom! We want to access the same terminal twice and get EOFError!"""


# We should use multithreading - if there is waiting
# and multiprocesses - if we need to do sth simultaneously
# NOTE: the code below works for quadcore processors (like mine)
process = Process(target=complex_calculation)
process2 = Process(target=complex_calculation)
process3 = Process(target=complex_calculation)
process4 = Process(target=complex_calculation)

process.start()
process2.start()
process3.start()
process4.start()

start = time.time()

process.join()
process2.join()
process3.join()
process4.join()

print(f"Four processes join time: {time.time() - start}")
