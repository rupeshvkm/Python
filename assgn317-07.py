c=6.2
d='game'
print(type(c))
print(type(float(c)))
if(type(d) is (type(c))):
	print('int number')
elif(type(d) is (type(float(c)))):
	print('float number')
else:
	print('invalid number')	