#Do lists lekar ek dictionary banaiye jisme pehli 
# list ke elements keys ho aur dusri list ke 
# elements unn keys ki values ho.

list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,]
a={}
for x in range (len(list1)):
    a[list1[x]]=list2[x]
print(a)


