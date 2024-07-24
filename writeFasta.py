from Bio import SeqIO
import pandas as pd

#write fasta from a df. Presumes that df has atleast two columns: name (with header information) and seq (with the sequence).
def writeFA(df,outname):
    with open (outname,'w') as f:
        for r in range(0,df.shape[0]):
            f.write('>'+df.loc[r,'name']+'\n')
            f.write(df.loc[r,'seq']+'\n')