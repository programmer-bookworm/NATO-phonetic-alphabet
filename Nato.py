import pandas
import csv
f=open("nato_phonetic_alphabet.csv","r")
data=pandas.read_csv(f)
phonetic={row.letter:row.code for (index,row) in data.iterrows()}
print(phonetic)

word=input("enter word").upper()
o_list=[phonetic[i] for i in word]
print(o_list)