#Ek list lijiye aur uske andar dictionaries me keys and values 
#likhiye jaisa ki niche dikhaya gaya hai (Sample Data) aur uske 
#baad saare unique values ko ek list me print karaye
#OUTPUT [2', '7', '9', '5', '1'] 
list1=[
        {"first":"1"}, 
        {"second": "2"}, 
        {"third": "1"}, 
        {"four": "5"}, 
        {"five":"5"}, 
        {"six":"9"},
        {"seven":"7"}
      ] 
list2=[]
for i in range(len(list1)):
    for x in list1[i]:
        if (list1[i][x]) not in list2:
            list2.append(list1[i][x])
print(list2)