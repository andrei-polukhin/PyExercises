from fingerprint import Fingerprint
from collections import Counter
from pprint import pprint

with open("./Unsorted/fingerprints/origin.txt", "r") as file:
    origin = file.read()

with open("./Unsorted/fingerprints/plagiarism.txt", "r") as file:
    plagiarism = file.read()

text_length = min(len(origin.split()), len(plagiarism.split()))

if text_length < 60:
    raise NotImplementedError("Compare texts with at least 60 words.")

kgram = max(text_length // 21, 3)
window = kgram - 1
base = 11 if text_length < 250 else 23 if text_length < 600 else 101
modulo = max(round(text_length * 10, -3), 1000)

fprint = Fingerprint(kgram_len=kgram, window_len=window, base=base, modulo=modulo)

first = fprint.generate(str=origin)
second = fprint.generate(str=plagiarism)

similar = [
    x
    for x in first
    if x in second
]

similar_grams = Counter([
    element[0]
    for element in first
    for sec in second
    if sec[0] == element[0]
])

print("Identical substring hashes:")
pprint(similar)
print("\nIdentical grams:")
pprint(similar_grams)
