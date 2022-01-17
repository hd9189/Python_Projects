#problem: find most common in an array/list, and give the number of the most frequent

from collections import Counter

def most_frequent_item_count(collection):

    return Counter(collection).mostcommon(1)[0][1] if collection else 0

#if collection else 0 gives the "if" the oppotunity to check whether or not there are any data, if not give 0

