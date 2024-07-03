immutable_var = (0, 2, 'Бубас', False)
print('Immutable tuple:', immutable_var)
#immutable_var[1] = 'Кукусик'
#print(immutable_var) - PyCharm выдаёт ошибку, так как переменной immutable_var присвоен кортеж - неизменяемый объект, то изменить его нельзя
#print(type(immutable_var)) <class 'tuple'>
mutable_list = [0, 2, 'Бубас', True]
print('Mutable list:', mutable_list)
mutable_list[0] = 'Пупырка'
print('Mutable list modified:', mutable_list)
mutable_list.append(False)
print('Mutable list modified:', mutable_list)
mutable_list.extend('apple')
print('Mutable list modified:', mutable_list)
mutable_list.remove('a')
print('Mutable list modified:', mutable_list)
