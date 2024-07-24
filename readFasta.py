from Bio import SeqIO
import pandas as pd


def readFasta(fastaFile):
    specieslist ={} #dictionary to store species name+ID as key and seq as value. 
    with open(fastaFile, 'rt') as fastafile:
        for record in SeqIO.parse(fastafile,'fasta'):
            ID,header,info=str(record.id).split('|')
            name = str(header).split(';')[-1]+'|'+ID # get species name from list of taxonomy data and unique ID
            if name not in specieslist:
                specieslist[name]={}
            seq = str(record.seq)
            if seq not in specieslist[name]:
                specieslist[name][seq]=0 # add seq count for species
            specieslist[name][seq]= specieslist[name][seq]+1

fastadict = readFasta(fastaFile) #provide an input fasta file

#convert fasta dict to df

data_df = pd.DataFrame([[k1,k2,v] 
                        for k1,d in fastadict.items() 
                        for k2,v in d.items()],
                        columns =['name','seq','count'])


