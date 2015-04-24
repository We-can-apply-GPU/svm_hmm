#!/usr/bin/env python
# -*- coding: utf-8 -*-
FBANKS = 69
import numpy as np
def charto48(c):
    a = 0
    chrmap = open('data/48_idx_chr.map','r')
    for line in chrmap:
        s = line.split()
        for line in s:
            if s[0] == c:
                a = int(s[1])
                break
    return a

def read_examples(filename):
    ark = open('data/fbank/' + filename + '.ark','r')
    lab = open('data/label/' + filename + '.lab','r')
    datum = []
    curPos = 0
    seqDic = {}

    for line in ark:
        s = line.rstrip().split(' ')
        for line in lab:
            l = line.rstrip().split(',')
            if s[0] == l[0]:        #map label to train data
                for i in range(1,len(s)):
                    s[i] = float(s[i])
                seqs = s[0].rstrip().split('_')
                s[0] = seqs[0] + seqs[1]
                s.append(l[1])
                datum.append(s)
                #curPos += 1
                break

    with open("example/inFile",'w') as fout:
        idCnt = 0
        #until now , datum is the list of [ID  FBANKfeature phone]
        prevId = ""
        for i in range(len(datum)):
            curId = datum[i][0] 
            if(curId != prevId):
                prevId = curId
                idCnt +=1
            fout.write(str(charto48(datum[i][-1])))
            fout.write(" qid:{} ".format(idCnt))
            for j in range(FBANKS):
                fout.write("{}:{} ".format(j+1,datum[i][j+1]))
            fout.write('\n')
if __name__     == "__main__":
    #print(read_examples("trainToy"))
    read_examples("trainToy")
