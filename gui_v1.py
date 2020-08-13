import tkinter as tk
import translation as tr
from tkinter import messagebox


window = tk.Tk()  


window.geometry("800x500")
window.title("Translython")
window.configure(bg = '#A188A0')
window.resizable(False, False)


#----Create menubar-----

menubar = tk.Menu(window)
window.config(menu = menubar)


#-----Functions used for menu defined here------

def explain():
  messagebox.showinfo('Translython', 'Translython takes a DNA or RNA string input and returns all protein sequences derived from all possible reading frames.\nFor more information, please consult:\nhttps://www.genome.gov/genetics-glossary/Open-Reading-Frame')
  

helpMenu = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Help", menu = helpMenu,font = ("Times New Roman", 12))
helpMenu.add_command(label = "How Translython works",font = ("Times New Roman", 12), command = explain)

#-----Functions----

def protein_generator():
  
  sequence = str(entry_field1.get())
  sequence = sequence.replace('\n','')
  
  for nucleotide in sequence:
    if nucleotide != 'A' and nucleotide != 'C' and nucleotide != 'G' and nucleotide != 'T' and nucleotide != 'U':
      return 'Invalid sequence'
      break
      
  if 'U' in sequence:
    g = tr.rna2dna(sequence)
    return tr.dna2protein(g)
  else:
    return tr.dna2protein(sequence)
   
def protein_display():
  protein = protein_generator()

#-----Create text field------

  prot_display = tk.Text(master = window, height = 30, width = 70, font = ("Times New Roman",15))
  prot_display.place(relx = 0.42, rely = 0.4, relwidth = 0.4, relheight = 0.4)
  
  prot_display.insert(tk.END, protein)

#-----Labels-------

title = tk.Label(text = "Translate DNA or RNA sequences into protein", bg = '#A188A0', font = ("Times New Roman", 20))
title.place(relx = 0.05, rely = 0.1)
 

label1 = tk.Label(text = "Insert your sequence", font = ("Times New Roman", 20), bg = '#A188A0')
label1.place(relx = 0.05, rely = 0.25)

label2 = tk.Label(text = "Possible proteins", font = ("Times New Roman", 20), bg = '#A188A0')
label2.place(relx = 0.05, rely = 0.55)

#-----Button--------

button1 = tk.Button(text = "Translate", bg = "#FEEA11", command = protein_display, font =("Times New Roman", 15, 'bold'))

button1.place(relx = 0.4, rely = 0.9, relwidth = 0.2, relheight = 0.1)

#-----Entry field-------

entry_field1 = tk.Entry(font = ("Times New Roman", 15))
entry_field1.place(relx = 0.42, rely = 0.235, relwidth = 0.4, relheight = 0.1)

window.mainloop()




