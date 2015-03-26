#!/usr/bin/env python
# 
# File Name : ptbtokenizer.py
#
# Description : Do the PTB Tokenization and remove punctuations.
#
# Usage :
#
# Creation Date : 29-12-2014
# Last Modified : Feb  25  2015
# Author : Hao Fang and Tsung-Yi Lin

import os
import sys
import subprocess
import tempfile
import itertools

STANFORD_CORENLP_3_4_1_JAR = 'stanford-corenlp-3.4.1.jar'
#print STANFORD_CORENLP_3_4_1_JAR

PUNCTUATIONS = ["''", "'", "``", "`", "-LRB-", "-RRB-", "-LCB-", "-RCB-", \
        ".", "?", "!", ",", ":", "-", "--", "...", ";"] 

class PTBTokenizer:
    """Python wrapper of Stanford PTBTokenizer"""

    def tokenize(self, captionsfile):
        cmd = ['java', '-cp', STANFORD_CORENLP_3_4_1_JAR, \
                'edu.stanford.nlp.process.PTBTokenizer', \
                '-preserveLines', '-lowerCase']

        # ======================================================
        # tokenize sentence
        # ======================================================
        cmd.append(captionsfile)
        path_to_jar_dirname=os.path.dirname(os.path.abspath(__file__))
        with open('intermediate', 'w') as f:
          subprocess.call(cmd, stdout=f)
        lines = open("intermediate").readlines()
        lines = [x.replace("\n","") for x in lines]
        os.remove("intermediate")

        # ======================================================
        # create dictionary for tokenized captions
        # ======================================================
        handle = open("%s-tokenized" % (captionsfile), "w")
        for line in lines:
            tokenized_caption = ' '.join([w for w in line.rstrip().split(' ') \
                    if w not in PUNCTUATIONS])
            handle.write(tokenized_caption+"\n")
        handle.close()

if __name__ == "__main__":
  t = PTBTokenizer()
  t.tokenize(sys.argv[1])
