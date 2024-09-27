my_dict = {'Nikolay': 1992, 'Daniil': 2020}
print(my_dict)
print(my_dict['Nikolay'])
my_dict.update({'mom': 87564794059,
                'dad': 89875636585})
print(my_dict)
del my_dict['Daniil']
print(my_dict)

my_set = {1, 2, 3, 4, 5, 1, 2, 3, 4, 'set', True, (1, 2, 3)}
list_ = [1, 2, 3, 3, 2, 1, 3]
list_ = set(list_)
print(list_)
print(list_.discard(3))
print(list_)