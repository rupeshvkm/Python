#dictionary:
a=['abc', 67, 34]
a={'name':'abc', 'empid':67, 'age':34}
# print (a)
#key--> should be of immutable data type
#unique keys 
# print (a['name'])
#mutable
#insert:
# a['key']='value'
# print (a)

#update:
# a['age']=78
# print (a)

#delete:
# del a
# del a['empid']
# print (a)
# print (a.pop('age'))
# print (a)
# a.popitem()
# print (a)
# a.clear()
# print (a)

# help(dict)
# a={'key1':{'key2':'value2', 'key3':'value3'}, 'key4':'value4'}
# print (a['key1']['key3'])

# for i in a:
# 	print (a[i])


# a={'emp1':{'name':'rup','salary':2000},'emp2':{'name':'raj','salary':29000},'emp3':{'name':'raj','salary':28000}}
# flag=a['emp1']['salary'];
# for i in a:
# 	if(a[i]['salary']>flag):
# 		flag=a[i]['salary']
# print (flag)

#set:
# a={23,45,89,12,'abc', 'hi', (5,6),89}
#values in a set should be of immutable data type
# #mutable
# print (a)
# help(set)
#insert:
# a.add(5)
# print (a)

