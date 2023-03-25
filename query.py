# Import Statements
import time

import json

import nltk 
from nltk.tokenize import word_tokenize
from nltk.metrics.distance import jaccard_distance
from nltk.util import ngrams
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('words')
from nltk.corpus import words
from nltk.tokenize import MWETokenizer
from wildcard import wildcardProcessing
 
start_time = time.time()
# Text file the query
file = open('query.txt')
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
# array = []
# for i in range(line):
# 	array.append(file.readline())
 
# print(array)
 

# Taking care of Punctuations
punc = '''!()-[]{};:'"\, <>./?@#$%^&_~'''
for ele in read:
	if ele in punc:
		read = read.replace(ele, " ")
		
# print(read)
 
# Making case insensitive
read=read.lower()				
# print(read)

# print(read)

# tokenizer = MWETokenizer([('*')])
# # Tokenization 
# for i in range(1):
# 	# this will convert
# 	# the word into tokens
# 	text_tokens = tokenizer.tokenize(word_tokenize(read))

# print(text_tokens)

text_tokens = read.split(' ')

# Wildcard characters

wildcards = []

# Checking for permute term
for tok in text_tokens:
	if '*' in tok:
		wildcards.extend(wildcardProcessing(tok))
		text_tokens.remove(tok)

# for wc in wildcards:
#     if wc not in text_tokens:
#         text_tokens.append(wc)


# Spell Correction
correct_words = words.words()

correct_tokens = []

changed_words = {}

for word in text_tokens:
    temp = [(jaccard_distance(set(ngrams(word, 2)),
                              set(ngrams(w, 2))),w)
            for w in correct_words if w[0]==word[0]]
    correct_word = sorted(temp, key = lambda val:val[0])[0][1]
    correct_tokens.append(correct_word)
    if(word != correct_word):
    	changed_words[word] = correct_word
    

# Taking care of stop words

tokens_without_sw = [
	word for word in correct_tokens if not word in stopwords.words()]
 
# print(tokens_without_sw)


# For Performming Stemming (Porter)
# ps = PorterStemmer()

# tokens_final = []

# for tok in tokens_without_sw:
# 	tok_lem = ps.stem(tok)
# 	if tok_lem not in tokens_final:
# 		tokens_final.append(tok_lem)
 

tokens_final = tokens_without_sw

 
# file1 = open('token_try.txt','w')
# for tok in tokens_final:
#     file1.write(tok +" ")
# file1.close()
 


# Dictionary for storing the line numbers of tokens (Inverted Tavle Index)
 
# dict = {}
 
# for i in range(line):
# 	check = array[i].lower()
# 	for item in tokens_final:
 
# 		if item in check:
# 			if item not in dict:
# 				dict[item] = []
 
# 			if item in dict:
# 				if ((i+1) not in dict[item]):
# 				    dict[item].append(i+1)

# print(dict)			
 
# file1 = open('dict.txt','w')
# for tok in dict:
#     file1.write(tok +"\n\n")
# file1.close()
# print(dict)
 
# Printing ITI
# for i in dict:
# 	print (i)
 
 
 
# json  = json.dumps(dict)
 
# f = open("query.json", 'w')
# f.write(json)
# f.close()


# Loading all Json files
f = open('start.json')
start = json.load(f)
f.close()
 
f = open('end.json')
end = json.load(f)
f.close()
 
f = open('dict.json')
data = json.load(f)
f.close()
 
f = open('document.json')
doc = json.load(f)
f.close()

 
# print(start)
# print(end)
# print(data)


# Function to find paragraph containing all tokens
# def common_numbers(d):
#     # Find the set of common numbers for all keys
#     common_set = set(d[next(iter(d))])
#     for lst in d.values():
#         common_set &= set(lst)

#     # Convert the set of common numbers to a list of lists
#     common_list = [list(x) for x in common_set]
#     return common_list


def common_para(search):
	res = search[list(search.keys())[0]]
	for key in search:
		res = list(set(res).intersection(set(search[key])))

	return res


# Function to check which document the line belongs
def check_doc(line_no):
	for d in doc:
		if line_no>=doc[d][0] and line_no<=doc[d][1]:
			return d

list_tokens = []

# Wild Card handling
for wc in wildcards:
    temp = []
    temp.extend(tokens_final)
    temp.append(wc)
    list_tokens.append(temp)

tot_search = []
# Searching the line for the search token keywords
for lis in list_tokens:
	search = {}
	
	for item in lis:
		if item in data:
			for idx in data[item]:
				for i in range(len(start)):
					if(idx>=start[i] and idx<=end[i]):
						if item in search:
							search[item].append((start[i], end[i]))
						else:
							search[item] = [(start[i], end[i])]
						# print(item + "  :  " + str(start[i]) + " -> " + str(end[i]))
		if(search):
			tot_search.append(search)

	
# print(search)

tot_common_list =[]
flag = 0
for search in tot_search:
	if len(search)!=0:
		common_list = common_para(search)
		flag = 1
		if(len(common_list)!=0):
			tot_common_list.extend(common_list)
			

print('\n\n')

res_count = 1

if flag:
	for lis in tot_common_list:
		with open(r"final-final.txt", errors="ignore") as fp:
			x = fp.readlines()[lis[0]:lis[1]]
			if(lis[0] == lis[1]) :
				continue
			print("RESULT " + str(res_count))
			print("\n")

			print("Document Name : " + str(check_doc(lis[0])))

			print("\n")
			print(''.join(x))
			print("\n\n--------------------------------------------------------------------------")
			res_count += 1

if (res_count == 1):
	print("\n\nNO OUTPUT FOR SAME PARAGRAPH\n\n")

end_time = time.time()

print("Time Taken : " + str(end_time-start_time))

print("\nTokens :")
print(tokens_final)
print("\nWildcards :")
print(wildcards)
# print(search)
# print(common_list)

if(len(changed_words) != 0):
    print("\nDid You Mean?")
    for key in changed_words:
        print(key + "  ->  " + changed_words[key])