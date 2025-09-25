import math

def discriminant(a,b,c):
	return b**2 - 4*a*c

     

def quadratic_roots(a, b, c):
    d = discriminant(a, b, c)

    if d > 0:
        print("Рівняння має два корені")
        x1 = (-b - math.sqrt(d)) / (2*a)
        x2 = (-b + math.sqrt(d)) / (2*a)
        print("x1 =", x1)
        print("x2 =", x2)
        return x1, x2
    elif d == 0:
        print("Рівняння має один корінь")
        x = -b / (2*a)
        print("x =", x)
        return x,
    else:
        print("Рівняння не має дійсних коренів")
        return None


a, b, c = 3, -18, 27
roots = quadratic_roots(a, b, c)
