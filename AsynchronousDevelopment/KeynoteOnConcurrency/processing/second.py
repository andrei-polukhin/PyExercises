import urllib.request
from multiprocessing.pool import ThreadPool as Pool


sites = [
    'https://www.yahoo.com/',
    'http://www.cnn.com',
    'http://www.python.org',
    'http://www.jython.org',
    'http://www.pypy.org',
    'http://www.perl.org',
    'http://www.cisco.com',
    'http://www.facebook.com',
    'http://www.twitter.com',
]

def sitesize(url):  # pylint: disable=missing-function-docstring
    with urllib.request.urlopen(url) as u:
        page = u.read()
        return url, len(page)


pool = Pool(4)

for result in pool.map(sitesize, sites):
    print(result)
