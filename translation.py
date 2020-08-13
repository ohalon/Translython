import re

def complement(seq):
  
  comp = []
  for nucleotide in seq:
    if nucleotide == 'A':
      comp.append('T')
    elif nucleotide == 'C':
      comp.append('G')
    elif nucleotide == 'T':
      comp.append('A')
    elif nucleotide == 'G':
      comp.append('C')
  
  comp.reverse()
  comp = ''.join(comp)
  return(comp)

def dna2rna(dna):
  
  rna = []
  for nucleotide in dna:
    if nucleotide == 'T':
      rna.append('U')
    else:
      rna.append(nucleotide)
  
  rna = ''.join(rna)      
  return(rna)
  
def rna2dna(rna):

  dna = []
  for nucleotide in rna:
    if nucleotide == 'U':
      dna.append('T')
    else:
      dna.append(nucleotide)
          
  dna = ''.join(dna)
  return(dna)

def rna2protein(seq): 

  #Create codon dictionary
  
  d = {
	'F' : ['UUU', 'UUC'],
	'L' : ['UUA', 'UUG','CUU', 'CUC', 'CUA', 'CUG'],
	'S' : ['UCU', 'UCC', 'UCA', 'UCG','AGU' , 'AGC'],
	'Y' : ['UAU', 'UAC'],
	'X' : ['UAA' ,'UAG', 'UGA'], #stop codons
	'C' : ['UGU', 'UGC'],
	'W' : ['UGG'],
	'P' : ['CCU', 'CCC', 'CCA', 'CCG'],
	'H' : ['CAU', 'CAC'],
	'Q' : ['CAA', 'CAG'],
	'R' : ['CGU', 'CGC', 'CGA', 'CGG','AGA', 'AGG'],
	'I' : ['AUU', 'AUC', 'AUA'],
	'M' : ['AUG'], #start codon
	'T' : ['ACU', 'ACC', 'ACA', 'ACG'],
	'N' : ['AAU', 'AAC'],
	'K' : ['AAA', 'AAG'],
	'V' : ['GUU', 'GUC', 'GUA', 'GUG'],
	'A' : ['GCU', 'GCC', 'GCA', 'GCG'],
	'D' : ['GAU', 'GAC'],
	'E' : ['GAA', 'GAG'],
	'G' : ['GGU', 'GGC', 'GGA', 'GGG']
	}
 
  seq = re.findall('...', seq)	
  protein = []
  
  for i in range(len(seq)):
    for key, value in d.items():
      for val in value:
        if seq[i] == val:
          protein.append(key)
  
  protein = ''.join(protein[:-1])
  return protein
  
def dna2protein(seq):
   
   rna =  dna2rna(seq)
   rna_reverse = dna2rna(complement(seq))
   protein = []
            
   # Define reading frames
   rfs = [rna, rna_reverse, rna[1:], rna[2:], rna_reverse[1:], rna_reverse[2:]]
   for frame in rfs:
     protein.append(rna2protein(frame))
   
   all_orfs = [] # open reading frames go in here
     
   for sequence in protein:
     for i in range(0, len(sequence)):
       if sequence[i] == 'M':
         orf = 'M'
         for j in range((i + 1), len(sequence)):
           if sequence[j] != 'X':
             orf = orf + sequence[j]
           else:
             all_orfs.append(orf)
             break
       else:
         continue         
   
   all_orfs = list(set(all_orfs)) # remove duplicates 
   all_orfs = '\n'.join(all_orfs)
   return all_orfs               
         
       
     
        
       
        
    
    
