def ft_map(function_to_apply, list_of_inputs):
    if not callable(function_to_apply):
        print(function_to_apply, 'is not a function.')
        return
    try:
        new_lst = []
        for i in list_of_inputs:
            new_lst.append(function_to_apply(i))
        return (new_lst)
    except TypeError:
        print(list_of_inputs, 'is not iterable.')

def addition(n):
    return n + n

numbers = (1, 2, 3, 4)
x = 'Hello'

result = ft_map(addition, numbers)
print(result)