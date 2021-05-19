#Ek program likhiye jisse ki agar di hui key pehle se 
# dictionary me exist karti ho toh “exists “ print kare 
# aur agar nahi karti ho toh “not exists” print kare.
'''If input is “name” then output will be “exist”'''
'''If input is “class” then output will be “not exists”.'''

dict1={"name":"Raju", "marks":56}
user=input("enter the word")
# for x in dict1:
if user in dict1:
    print("exists")
else:
    print("not exists")