# Generates a list of words, saves it into a file

# import nltk
# nltk.download("words")  # used for downloading the words corpus from nltk (needed to run only once per machine)

import numpy as np
from nltk.corpus import words


def generate(file: str, count: int):
    words_array = np.array(
        list(filter(lambda word: len(word) >= 3, words.words("en-basic")))
    )  # create numpy array of words of 3 or more characters

    print(words_array[:20])
    print(f"Length of words_array: {len(words_array)}")

    words_array_subset = np.random.choice(
        words_array, size=count
    )  # extract count-many words randomly from words_array with uniform distribution

    print(words_array_subset)
    print(f"Length of words_array_subset: {len(words_array_subset)}")

    print("Saving generated words to file")
    np.savetxt(file, words_array_subset, fmt="%s", newline=" ", encoding="utf-8")
    print("Done")
