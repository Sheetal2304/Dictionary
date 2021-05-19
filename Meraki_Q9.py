#"MISSISSIPPI" iss word me har letter ki occurrency count 
#karke ek dictionary me store karaye. Jisme letter dictionary
#ki keys aur occurrency Uss dictionary ki values hongi.
#OUTPUT {M:1,I:4,S:4,P:2}
a="MISSISSIPPI"
b=[]
c=[]
i=0
while i<len(a):
    count=0
    j=0
    while j<len(a):
        if a[j]==a[i]:
            count+=1
        j+=1
    if a[i]in b:
        i+=1
        continue
    b.append(a[i])
    c.append(count)
    i+=1
x={}
for y in range (len(b)):
    x[b[y]]=c[y]
print(x)