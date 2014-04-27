import sys


def split_line(line):
    cols = line.split("\t")
    return cols


def get_words(cols):
    words_ids = cols[4].split(" ")
    words = [w.split("#")[0] for w in words_ids]
    return words

def get_positive(cols):
    return cols[2]


def get_negative(cols):
    return cols[3]


def get_objective(cols):
    return 1 - (float(cols[2]) + float(cols[3]))


def get_gloss(cols):
    return cols[5]


def get_scores(filepath, word):
    p_score = 0
    n_score = 0
    word = word.lower()
    f = open(filepath)
    for line in f:
        if not line.startswith("#"):
            cols = split_line(line)
            words = get_words(cols)

            if word in words:
                p_score = get_positive(cols)
                n_score = get_negative(cols)

    return p_score, n_score


