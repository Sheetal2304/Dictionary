#Ek program likhiye jo:- Ek dictionary me 1
#se 15 tak saare numbers ki keys banaye aur 
#unke square unn keys ki values ho.
#OUTPUT {1: 1, 2: 4, 3: 9, 4: 16, 5: 25,
#6: 36,7: 49, 8: 64, 9: 81, 10: 100,
#11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
square={}
i=1
while i<=15:
    square[i]=i*i
    i+=1
print(square)
