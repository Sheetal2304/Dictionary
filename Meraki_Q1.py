# Ek program likhiye jisse ki niche di hui dictionaries ek hi 
#dictionary me aa jaaye jaise ki niche Expected result me diya 
# gaya hain or jisski bhi keys same hai unki values add ho jai.dic1={1:10, 2:20}
'''output{1: 10, 2: 60, 3: 30,  5: 50, 6: 60}''' 
dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
sum = 0
dic = {}
for x in dic1:
    num = x
    if x in dic2 :
        sum = sum + dic1[x] + dic2[x] 
        dic1[x] = sum
        dic2.pop(x)
dic1.update(dic2)
dic1.update((dic3))
print(dic1)



    
