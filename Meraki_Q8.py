#User se 10 students ke naam aur marks lekar unhe
#ek dictionary me store karaye
#OUTPUT {
    # 'sonu':85,
    # 'Kartik':90,
    # 'Deepak':96,
    # 'Aman':76,
    # 'Somesh':60,
    # 'Umesh':85,
    # 'Amarpal':70,
    # 'Roshan':57,
    # 'Riyaz':98,
    # 'Shabid':56
    # }
a={}
for i in range(0,10):
    name=input("enter the name")
    marks=int(input("enter the marks"))
    a[name]=marks
print(a)

       