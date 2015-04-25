#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sortLab():
    ark = open('data/fbank/train.ark','r')
    lab = open('data/label/train.lab','r')
    with open ('data/label/newLab.lab','w') as newLab:
        datum = []
        curPos = 0
        seqDic = {}
        for line in ark:
            s = line.rstrip().split(" ")
            seqDic[s[0]] = ""
        ark.close()
        for lines in lab:
            l = lines.rstrip().split(",")
            seqDic[l[0]] = l[1]
        #print(seqDic)
        ark = open('data/fbank/train.ark','r')
        for line in ark:
            s = line.rstrip().split(" ")
            print(seqDic[s[0]])
            newLab.write(str(s[0]) + ',' + seqDic[s[0]] + '\n')
        
        

sortLab()
