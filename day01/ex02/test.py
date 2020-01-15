from vector import Vector


v1 = Vector([0.0, 1.0, 2.0])
v2 = Vector.from_size(3)
v3 = Vector.from_range((10, 15))
print('Value of V1 BEFORE add SCALAR: %s\n' % format(v1.values))
v1 + 1
print('Value of V1 AFTER add SCALAR: ', v1.values)
print('Value of V2 BEFORE add SCALAR: %s\n' % format(v2.values))
v1 + v2
print('Value of V1 AFTER add VECTOR', v1.values)
print('Value of V2 AFTER add VECTOR', v2.values)

