import json
 
sum = 0
count = 0
 
# maxi = 0   #-->not using due to outliners
 
# Calculating the average character in a line
with open('final-final.txt', errors="ignore") as f:
    for line in f:
        length = len(line.strip())
 
        # maxi = max(maxi, length)
        if(length > 10):
            sum += length
            count += 1
 
avg = sum/count
 
# print(maxi)
 
 
 
####          Either use lists or dicts        ####
 
# Making paragraphs marker using lists
start = [0]
end = []
count = 0
 
# marking the the starting and wending line of paragraphs
with open('final-final.txt', errors="ignore") as f:
    for line in f:
        length = len(line.strip())
        # print(str(line.strip()[-1])
        count += 1
        if(length <(avg) and len(line.strip())!=0 and line.strip()[-1] == '.'):
            end.append(count)
            start.append(count+1)
 
start.pop()
 
 
#Printing paragraph lists - start & end
 
# for i in range(len(start)):
#     print(str(start[i])+ " " + str(end[i]))
 
 
 
 
# Making paragraphs marker using dict
 
# para = {0 : [0]}
# count = 0
# count_para = 0
 
# with open('AU127-1.txt') as f:
#     for line in f:
#         length = len(line.strip())
#         count += 1
#         if(length <(avg*2/3) and line.strip()[-1] == '.'):
#             para[count_para].append(count)
#             count_para += 1
#             para[count_para] = [count+1]
 
 
# para.pop(count_para)
 
 
#Printing paragraph dict
# print(para)
 
##########                                    #########
 
 
json_start  = json.dumps(start)
json_end = json.dumps(end)
 
f = open("start.json", 'w')
f.write(json_start)
f.close()
 
f = open("end.json", 'w')
f.write(json_end)
f.close()