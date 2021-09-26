counter = 0


def worker():
    'My job is to increment the counter and print the current count'
    global counter

    counter += 1
    print('The count is %d' % counter)
    print('---------------')


print('Starting up')
for i in range(10):
    worker()
print('Finishing up')
