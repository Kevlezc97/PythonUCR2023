a = 3
b = 4
print(a+b)


if a > b:
    print(b)
elif a < b:
    print(a)

string_ex = "Esto es una string"

# Acceder a la cantidad de caracteres individuales
print("El primer caracter es {0} y el último {1}" .format( string_ex[0], string_ex[-1]))

# Checkear si otra string está incluida en la otra
sub_string = "string"


#MAYUS
print (string_ex.upper())
#MINUS
print (string_ex.lower())

#Reemplazar una string

print(string_ex.replace("string", "prueba"))
