from vector import Vector


v1 = Vector([1.0, 2.0, 3.0])
v2 = Vector.from_size(3)
v3 = Vector.from_range((10, 13))
print('Value of V1 BEFORE mult SCALAR:', v1, '\n')
v1 * 2
print('Value of V1 AFTER mult SCALAR:', v1)
print('Value of V2 BEFORE mult SCALAR:', v2, '\n')
v1 * v2
print('Value of V1 AFTER mult VECTOR', v1)
print('Value of V2 AFTER mult VECTOR', v2)
