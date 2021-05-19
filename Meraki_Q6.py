#Ek program likhiye jo dictionary me se duplicate keys hata de.
#OUTPUT {“ball”:”red”,”bat”:4,”wickets”:8}

dic={
    "ball":"red”",
    "bat":4,
    "wickets":8,
    "ball":"green",
    "bat":3
    } 
# dic1={}
# # # dic1.update(dic)
# # # print(dic1)
# for i in dic:
#     if i in dic1:
#         # dic.pop(i)
#         dic1[i] = dic[i]
#         dic1.update(dic)
# print(dic)

result={}
for key,value in dic.items():
    if value not in result.values():
        result[key]=value
print(result)