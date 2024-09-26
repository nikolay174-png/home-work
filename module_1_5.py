#immutable_list = ([7, 'string'], True)
#print('immutable tuple: ', immutable_list)

mutable_list = ([7, 'string'], True)
print('immutable tuple: ', mutable_list)
mutable_list[0][0] = ['list']
print(mutable_list)