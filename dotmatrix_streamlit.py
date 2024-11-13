import streamlit as st
from Bio import SeqIO
import numpy as np
import matplotlib.pyplot as plt 

def dotmatrix(f1,f2,w):
#コロナの配列
    record1 = next(SeqIO.parse(f1,"fasta"))
#SARSの配列
    record2 = next(SeqIO.parse(f2,"fasta"))
       
    #w = 10
    seq1 = record1.seq 
    seq2 = record2.seq
    

#hash作成
    hash = {}
    sub1 = seq1
    sub2 = seq2
    x = 102

#行列の各点[y,x]について
    for x in range(len(seq1)-w+1):
        sub1 = seq1[x:x+w]
        if sub1 not in hash:
             hash[sub1] = []
        hash[sub1].append(x)

#win = 10
    len1 = len(seq1) - w + 1
    len2 = len(seq2) - w + 1

    width = 500
    height = 500

    image = np.zeros((height,width))

   
    for y in range(len2):
           sub2 = seq2[y:y+w]
           py = int(y/len2 * height)
           if sub2 in hash:
               for x in hash[sub2]:
                px = int(x/len1 * width)
                image[py,px] = 1


    plt.imshow(image,extent=(1,len1,len2,1),cmap="Grays")
    #plt.show()
    st.pyplot(plt)


st.title("Dot matrix")
file1 = st.sidebar.file_uploader("Sequence file 1:")
file2 = st.sidebar.file_uploader("sequence file 2:")
w = st.sidebar.slider("Window size:", 4,100,10)

from io import StringIO
if file1 and file2:
    with StringIO(file1.getvalue().decode("utf-8")) as f1,\
        StringIO(file2.getvalue().decode("utf-8")) as f2:
        dotmatrix(f1,f2,w)
