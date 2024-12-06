print("-------Varianza-----")

print("Dame los 5 numeros")
n=float(input(" "))
n2=float(input(" "))
n3=float(input(" "))
n4=float(input(" "))
n5=float(input(" "))

sum=n+n2+n3+n4+n5
pro=(n+n2+n3+n4+n5)/5

var=(sum*(n**2-pro**2))/5
var2=var**2

print("La Varianza es: ",var2)