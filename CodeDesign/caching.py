"""
Caching engine which will store key values according to specified duration
"""

from datetime import datetime, timedelta


class CachingEngine:
  """Caching engine unvalidating keys after a given duration"""

  cache = {}

  def add(self, key, value, duration):
    """
    Add a new key value which will work according to specified duration
    """

    self.cache[key] = {
      'value': value,
      'expires': datetime.now() + timedelta(seconds=duration)
    }

  def get(self, key):
    """
    Retrieve a given key if it exists and did not expire
    """

    if key in self.cache and self.cache[key]['expires'] >= datetime.now():
      return self.cache[key]['value']

    return None


if __name__ == '__main__':
  """Tests"""

  import time  # pylint: disable=import-outside-toplevel
  engine = CachingEngine()

  engine.add('key', 'value', 0)
  assert engine.get('key') is None  # expired
  assert engine.get('non-existent') is None  # never existed

  engine.add('key', 'value', 5)
  time.sleep(3)
  assert engine.get('key') == 'value'  # 3 < 5 -> still should exist

  engine.add('key', 'new-value', 2)
  assert engine.get('key') == 'new-value'  # got updated!

  # misused 'duration' will give TypeError
  # mutable 'key' will give TypeError
  ## no need to cover them by tests and handle them - traceback is sufficient
