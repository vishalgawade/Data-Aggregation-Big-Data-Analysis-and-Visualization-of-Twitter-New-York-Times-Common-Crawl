#!/usr/bin/python3.6

import sys
from itertools import groupby
from operator import itemgetter


def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)


def main(separator='\t'):
    hashtable={}; # maintain dictionary <word,count> to store count of word
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)

    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
            if current_word not in hashtable:
                hashtable[current_word] = total_count;
            else:
                hashtable[current_word] += total_count;
        except ValueError:
            # count was not a number, so silently discard this item
            pass

    sortedTuple = sorted(hashtable.items(), key=itemgetter(1),reverse=True);  # sort hashtable by word occurence count
    for tuples in sortedTuple:
        print("%s%s%d" % (tuples[0], separator, tuples[1]));

if __name__ == "__main__":
    main()