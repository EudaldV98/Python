import operator


def ft_reduce(function_to_apply, list_of_inputs):
	if len(list_of_inputs) == 0:
		return (None)
	result = list_of_inputs[0]
	for i in range(1, len(list_of_inputs)):
		result = function_to_apply(result, list_of_inputs[i])
	return (result)

def addition(n):
    return n + n
numbers = [1, 2, 3, 4]
x = 'Hello'

result = ft_reduce(operator.add, numbers)
print(result)
