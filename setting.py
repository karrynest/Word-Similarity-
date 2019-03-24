#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys

ROOT_DIR=os.path.dirname(os.path.abspath(sys.argv[0]))
RESULT_DIR=os.path.join(ROOT_DIR, "result")
WORDSIM353_DIR=os.path.join(ROOT_DIR, "Mturk-771")

RESULT_PREFIXS=[
    "wordnet/path_", "wordnet/wup_", "wordnet/lch_",
    "wordnet/res_", "wordnet/lin_", "wordnet/jcn_",
    "word2vec/Wikipedia_"
    ]



