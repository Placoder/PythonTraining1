dict1 = {'Name': 'Tom', 'Age': 24, 'Company': 'Zensar'}
dict2 = {}
print(dict1)
print("dict1['Name']: ", dict1['Name'])
print ("dict1['Age']: ", dict1['Age'])

dict1['Age'] = 35 # update existing entry
dict1['BU'] = "CISCO" # Add new entry
print("dict1['Age']: ", dict1['Age'])
dict1.update({'Name':'Neha'})  # update existing entry

print(dict1)

del dict1['BU']  # remove entry with key 'Name'
print(dict1)
dict1.clear()      # remove all entries in dict
print(dict1)
del dict1         # delete entire dictionary
# print(dict1)

dict = {('Name'): 'Tom', 'Age': 24}
print("dict['Name']: ", dict[('Name')])

ls_dic = [{'Name':"pla",'Age':20},{'Name':"pp",'Age':30},{'Name':"tom",'Age':15}]
print(ls_dic[0])
print(ls_dic[0]['Name'])
print(ls_dic[-1])
print(ls_dic[-1]['Name'])
ls_dic.append([{'Name':"neha",'Age':35}])
print(ls_dic)
