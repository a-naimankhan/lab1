x = 1 #integer
y = 1.5 #float
z = 1j #complex:d

print(type(x))
print(type(y))
print(type(z))


converted_x=float(x)
converted_y=int(y)
#converted_z=int(z) it isn't possible to convert the "complex number".

print(converted_x , "type is:" , type(converted_x))
print(converted_y , "type is:" , type(converted_y))
#print(type(converted_z)) int() argument must be a string, a bytes-like object or a real number, not 'complex'