import urllib.request

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

for url in sites:
    with urllib.request.urlopen(url) as u:
        page = u.read()
        print(url, len(page))
