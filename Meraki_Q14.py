#Ek program likho jo ki dictionaries ki values
#ko sort(ascending or descending) kar de.
#OUTPUT:- ASCENDING ORDER{'param':20,'anjili':30,'bijender':45,'roshini':50,'deepak':60}
#DESCENDING ORDER{'deepak':60,'roshini':50,'bijender':45,'anjili':30,'param':20}#

dic={"priya" : 1,"bijender":45,"deepak":60,"param":20,"sheetal" : 12 ,"anjili":30,"roshini":50,"shreshta":100}
#ascending order
count=0
# a={}
for y in dic:
    count+=1
# print(count)
a={}
i=0
while i<count:
    max_key = max(dic, key=dic.get)
    value=dic.values()
    max_value=max(value)
    a[max_key]=max_value
    dic.pop(max_key)
    i+=1
print(a)

#descending order
b={}
j=0
while j<count:
    min_key = min(a, key=a.get)
    values=a.values()
    min_value=min(values)   
    b[min_key]=min_value
    a.pop(min_key)
    j+=1
print(b)

