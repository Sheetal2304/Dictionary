#Ek dictionary ki value ke sabhi items ko count 
#kijiye jo ki ek list me hai. 
#OUTPUT  total count:5
dict1 =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']}
count=0
for i in dict1:
    for j in dict1[i]:
        count+=1  
print("Total count","=",count)