import json

f = open('dict.json')
data = json.load(f)
f.close()

def rotate(str, n):
    return str[n:] + str[:n]

dict = {}

keys = data.keys()
for key in sorted(keys):
    dkey = key + "$"
    for i in range(len(dkey),0,-1):
        out = rotate(dkey,i)
        dict[out] = key


permute_dict = json.dumps(dict)
 
f = open("permute.json", 'w')
f.write(permute_dict)
f.close()