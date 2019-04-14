# x = 1
# y = 2.5
# name = 'Michael'
# is_cool = False

#Multiple Assignment
x,y,name,is_cool = (1,2.5,'Michael',False)

#print (x,y,name,is_cool)

a = x + y
#print (a)

#print (type(x))
x = str(x)
#print (type(x))

#arguments by position
#print('{2},{0},{1}'.format('a','b','c'))

#print('I\'m {name} and I\'m cool: {is_cool}'.format(name=name,is_cool=is_cool))

#F-Strings
#print(f'My name is {name}.')

fruit_tuple = ('Apple','Banana','Orange')
#fruit_tuple = tuple(('Apple','Banana','Orange'))
#print (fruit_tuple[0])

fruit_set = {'Apple','Banana','Orange'}
#print(fruit_set)
#print('Apple' in fruit_set)
fruit_set.add('Grape')
#print('Grape' in fruit_set)
fruit_set.remove('Banana')
#print('Banana' in fruit_set)
fruit_set.clear()
#del fruit_set
print(fruit_set)