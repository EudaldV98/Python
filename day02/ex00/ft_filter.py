def ft_filter(function_to_apply, list_of_inputs):
    if not callable(function_to_apply):
        print(function_to_apply, 'is not a function.')
        return
    try:
        new_lst = []
        for i in list_of_inputs:
            if function_to_apply(i):
                new_lst.append(i)
        return (new_lst)
    except TypeError:
        print(list_of_inputs, 'is not iterable.')

def filter_vowels(lst):
	vowels = ['a', 'e', 'i', 'o', 'u']
	if lst in vowels:
		return True
	else:
		return False
	

alphabet = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

result = ft_filter(filter_vowels, alphabet)
for i in result:
    print(i)