#Ek code likhiye jo dictionary ki 3 highest value print karaye.
#OUTPUT ['e','b','c']
# my_dict = {
#     'a':50, 
#     'b':58,
#     'c': 56,
#     'd':40,
#     'e':100, 
#     'f':20
#     } 
# a=[]
# for i in my_dict:
#     for j in my_dict:
#         if (my_dict[i]>my_dict[j]):
#             my_dict[i],my_dict[j]=my_dict[j],my_dict[i]
# # print(my_dict)
# for x in my_dict:
#     a.append(x)
# print(a)

# for i in my_dict:
#     a=max(my_dict)
# print(a)


# a_dictionary = {"a": 1, "b": 2, "c": 3}
# all_values = a_dictionary. values()
# max_value = max(all_values) 
# # all_values is a list.
# print(max_value)


my_dict = {
    'a':50, 
    'b':58,
    'c': 56,
    'd':40,
    'e':100, 
    'f':20
    }
a=[]
i=0
while i <3:
    max_key = max(my_dict, key=my_dict.get)
    # print(max_key)
    a.append(max_key)
    my_dict.pop(max_key)
    i+=1
print(a)
