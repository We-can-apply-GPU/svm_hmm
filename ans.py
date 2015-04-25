#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
def numTo48Char(num):
    a = 'Z'
    chrmap = open('data/48_idx_chr.map','r')
    for line in chrmap:
        s = line.split()
        for line in s:
            if int(s[1]) == int(num):
                a = s[2]
                break
    return a

def mapResult(fileName):
    tags = open(fileName,'r').read().splitlines()
    testRec = open('testRecord','r').read().splitlines()
    total = []
    curPos = 0
    for line in testRec:
        s = line.split(',')
        ID = s[0]
        numSeqs = int(s[1])
        seqs = ID + ","
        ansPrev = ""
        for i in range(numSeqs):
            ansPrev += numTo48Char(tags[curPos])
            curPos += 1
        ans  = answer(ansPrev)
        seqs += (ans)
        total.append(seqs)
    return total

def answer(y):
    answer = ""
    start = False
    pre = 'K'
    for char in y:
        now = char
        if( not (start)):
            if now == 'K': #sil
                continue
            else:
                start = True
        if(start):
            if(now != pre):
                answer += now
                pre = now
    return answer

if __name__ == "__main__":
    #Usage : ./ans.py outputFile predictFile
    ans = mapResult(sys.argv[2])
    with open("output/" + sys.argv[1],'w') as output:
        output.write("id,phone_sequence")
        for line in ans:
            output.write(line + '\n')
