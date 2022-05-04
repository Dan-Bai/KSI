from collections import defaultdict
import csv
import string
from stop_words import get_stop_words    # download stop words package from https://pypi.org/project/stop-words/
import numpy as np


stop_words = get_stop_words('english')

admidic=defaultdict(list)
count=0

print("Reading NOTEEVENTS ---")

with open('NOTEEVENTS.csv', 'r') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
     for row in spamreader:
         if row[6]=='Discharge summary':
             admidic[row[2]].append(row[-1].replace('\n',' ').translate(str.maketrans('','',string.punctuation)).lower())
             count=count+1

print("Counting word occurrences ---")

u=defaultdict(int)
for i in admidic:
    for jj in admidic[i]:
        line=jj.strip('\n').split()
        for j in line:
            u[j]=u[j]+1

print("Filtering word to non-digit, more than 10 occurrence, not stop words ---")

u2=defaultdict(int)
for i in u:
        if i.isdigit()==False:
            if u[i]>10:
                if i not in stop_words:
                    u2[i]=u[i]
                    
u=[]   

file1=open('DIAGNOSES_ICD.csv','r')
ad2c=defaultdict(list)
line=file1.readline()
line=file1.readline()

print("Reading DIAGNOSES ICD ---")

while line:
    line=line.strip().split(',')

    if line[4][1:-1]!='':
        ad2c[line[2]].append("d_"+line[4][1:-1])
    
    line=file1.readline()

print("Counting medical code occurrences ---")

codeu=defaultdict(int)
for i in ad2c:
    for j in ad2c[i]:
        codeu[j]=codeu[j]+1

print("Generating combined dataset from codes and notes ---")

cthre=0
fileo=open("combined_dataset",'w', newline="\n")

IDlist=np.load('IDlist.npy',encoding='bytes').astype(str)
for i in IDlist[:10000]:
    if ad2c[i]!=[]:
        
        fileo.write('start! '+i+'\n')
        fileo.write('codes: ')
        tempc=[]
        for code in ad2c[i]:
            if codeu[code]>=cthre:
                if code[0:5] not in tempc:
                    tempc.append(code[0:5])
       
        for code in tempc:
            fileo.write(code+" ")
        fileo.write('\n')
        fileo.write('notes:\n')
        for line in admidic[i]:    
            thisline=line.strip('\n').split() 
            for j in thisline:
                if u2[j]!=0:
                    fileo.write(j+" ")
            fileo.write('\n')
        fileo.write('end!\n')
fileo.close()

