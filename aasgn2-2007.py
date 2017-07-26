a={'emp1':{'name':'rup','salary':20000},'emp2':{'name':'raj','salary':21000}}
flag=a['emp1']['salary'];
for i in a:
	if(a[i]['salary']>flag):
		flag=a[i]['name']

print(flag)	


	
help