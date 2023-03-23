# Import Statements
import json

from nltk.tokenize import word_tokenize
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
nltk.download('stopwords')

# Text file containing all pdfs
file = open('final-final.txt', errors="ignore")
read = file.read()
file.seek(0)
read
 
# Calc No of line
line = 1
for word in read:
	if word == '\n':
		line += 1
# print("Number of lines in file is: ", line)
 
#list to store each line as an element of list
array = []
for i in range(line):
	array.append(file.readline())
 
print(array)
print("ARRAY DONE")
 

# Taking care of Punctuations
punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
for ele in read:
	if ele in punc:
		read = read.replace(ele, " ")
		
# print(read)
 
# Making case insensitive
read=read.lower()				
print(read)
print("READ DONE")
 

print("LOADING DONE")


# Tokenization 
for i in range(1):
	# this will convert
	# the word into tokens
	text_tokens = word_tokenize(read)
 
 
print(text_tokens)
print("TOKENIZATION DONE")

# Taking care of stop words

# tokens_without_sw = [
# 	word for word in text_tokens if not word in stopwords.words()]
tokens_without_sw = []

for word in text_tokens:
	if not word in stopwords.words():
		tokens_without_sw.append(word)
		print(word)


# tokens_without_sw = text_tokens
 
print(tokens_without_sw)
print("TOKEN DONE")
 
# For Performming Stemming (Porter)
# ps = PorterStemmer()
# tokens_final = []

# for tok in tokens_without_sw:
# 	tok_lem = ps.stem(tok)
# 	if tok_lem not in tokens_final:
# 		tokens_final.append(tok_lem)

# print("Stemming Done!")

tokens_final = tokens_without_sw
 
# file1 = open('token_try.txt','w')
 
# for tok in tokens_without_sw:
#     file1.write(tok +" ")
 
# file1.close()
 

# Dictionary for storing the line numbers of tokens (Inverted Tavle Index)
 
dict = {}
 
for i in range(line):
	print("Working" + str(i))
	check = array[i].lower()
	for item in tokens_final:
 
		if item in check:
			if item not in dict:
				dict[item] = []
 
			if item in dict:
				if ((i+1) not in dict[item]):
				    dict[item].append(i+1)
				
 
# file1 = open('dict.txt','w')
 
# for tok in dict:
#     file1.write(tok +"\n\n")
 
# file1.close()
 
print(dict)
 
 

json_dict = json.dumps(dict)
 
f = open("dict.json", 'w')
f.write(json_dict)
f.close()