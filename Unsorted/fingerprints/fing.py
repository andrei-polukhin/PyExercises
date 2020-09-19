from fingerprint import Fingerprint
from collections import Counter
from pprint import pprint


def check(origin, plagiarized):
    with open(origin, "r") as file:
        origin = file.read()

    with open(plagiarized, "r") as file:
        plagiarism = file.read()

    text_length = min(len(origin.split()), len(plagiarism.split()))

    if text_length < 60:
        raise NotImplementedError("Compare texts with at least 60 words.")

    window = max(text_length // 21, 3)
    kgram = window - 1
    base = 11 if text_length < 250 else 23 if text_length < 600 else 101
    modulo = max(round(text_length * 5, -3), 1000)

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


if __name__ == "__main__":
    print("--------THE FIRST CHECK--------")
    try:
        check(
            "./Unsorted/fingerprints/origin.txt",
            "./Unsorted/fingerprints/plagiarism.txt"
        )
        print("--------THE CHECK ON DIRECT PLAGIARISM--------")
        check(
            "./Unsorted/fingerprints/direct_source.txt",
            "./Unsorted/fingerprints/direct_plagiarized.txt"
        )
        print("--------THE CHECK ON MOSAIC PLAGIARISM--------")
        check(
            "./Unsorted/fingerprints/mosaic_source.txt",
            "./Unsorted/fingerprints/mosaic_plagiarized.txt"
        )
        print("--------THE CHECK ON CLOSE PARAPHRASING--------")
        check(
            "./Unsorted/fingerprints/paraphrase_source.txt",
            "./Unsorted/fingerprints/paraphrase_plag.txt"
        )
    except FileNotFoundError:
        check("origin.txt", "plagiarism.txt")
        print("--------THE CHECK ON DIRECT PLAGIARISM--------")
        check("direct_source.txt", "direct_plagiarized.txt")
        print("--------THE CHECK ON MOSAIC PLAGIARISM--------")
        check("mosaic_source.txt", "mosaic_plagiarized.txt")
        print("--------THE CHECK ON CLOSE PARAPHRASING--------")
        check("paraphrase_source.txt", "paraphrase_plag.txt")
