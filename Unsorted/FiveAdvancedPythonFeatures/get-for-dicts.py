"""
Usually when we ask a dict in Python for a key, which does not exist,
it throws KeyError. This problem was successfully solved with .get()
method.
"""
example_dict = {
    "Andrew": "Polukhin",
    "John": "Cordel",
    "Emily": "McTerras"
}

# -- Conventional approach
print(example_dict["John"])  # the key exists
print(example_dict["Mary"])  # KeyError arises!

# -- With .get() method
print(example_dict.get("Emily"))  # nothing new with an existing key
print(example_dict.get("Jack"))  # -- a non-existent key -> None
