#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os, csv, copy

from setting import *
from sim_wordnet import sim_wordnet
from sim_word2vec import sim_word2vec
from rank_spearman import rank_spearman

def main():

    benchfile=open(os.path.join(WORDSIM353_DIR, "MTURK-771.csv"), 'r')
    benchdreader=csv.reader(benchfile)

    rank_file=open(os.path.join(RESULT_DIR,"rank.csv"),'w',newline='')
    rank_writer=csv.writer(rank_file)

    wordpairs=[]

    for line in benchdreader:
        wordpairs.append((copy.deepcopy(line[0]), copy.deepcopy(line[1]), copy.deepcopy(float(line[2]))))

    # If you want to start from scratch
    sim_wordnet(wordpairs, "MTURK-771.csv")
    sim_word2vec(wordpairs, "MTURK-771.csv")

    rank_results=rank_spearman(wordpairs, "MTURK-771.csv")
    rank_writer.writerows(rank_results)

    benchfile.close()
    rank_file.close()

if __name__ == '__main__':
    main()
