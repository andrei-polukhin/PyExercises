"""https://pybay.com/site_media/slides/raymond2017-keynote/threading.html"""
import threading

counter = 0


def worker():
    'My job is to increment the counter and print the current count'
    global counter

    counter += 1
    print('The count is %d' % counter)
    print('---------------')


print('Starting up')
for i in range(10):
    threading.Thread(target=worker).start()
print('Finishing up')
# I cannot get paid for it as it does not work! We see fuzzying problem!

# Seriously said we have two options to do:
#   1. use threading.Thread.join()
#   2. use queues.Queue, task_done
#                       (you can see it in AsynchronousDevelopment directory).
#   3. use threading.local() - to use the global variable
#                           INDEPENDENTLY for each thread.
