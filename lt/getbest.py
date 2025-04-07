#!/usr/bin/env python3

import sys

def getCols(f):
    ''' Identify the columns that contain the marks and student numbers '''
    headings = f.readline().strip().split(",")
    i=1
    for head in headings:
        if head == "Student Number": 
            num_col=i
            
        elif head == "Mark" : 
            mark_col = i
        i=i+1     ##iterate i in loop
   
        
    return (num_col, mark_col)

def findTop(f,num_col, mark_col):
    ''' finds the top student in the class '''
    best = best_idx =  0
    for line in f:
        data = line.strip().split(",")
        num = (data[num_col-1])     ##data holder for current line student number
        mark = int(data[mark_col-1])
        if mark > best:
            best=mark
            best_idx=num ##set best_idx equal to current student number
    return best_idx, best

f = open(sys.argv[1])
_num_col, _mark_col = getCols(f)   ##Variable names start with underscores for clarity
best_idx, best = findTop(f,_num_col,_mark_col)
print("The top student was student %s with %d"%(best_idx,best))
