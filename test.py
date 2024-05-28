import math
def hypotenusa(a,b):
    c = math.sqrt(a**2+b**2)
    return round(c,2) 
a = int(input("geef een zijde van een rechthoekige driehoek"))
b = int(input("Geef de tweede zijde van een rechthoekige driehoek"))

print(hypotenusa(a,b))
