import math
a = input()
b = input()
c = input()
a = int(a)
b = int(b)
c = int(c)
x1 = ((-b)+ math.sqrt(b*b-4*a*c))/(2*a)
x2 = ((-b)- math.sqrt(b*b-4*a*c))/(2*a)
x1 = int(x1*10)
x2 = int(x2*10)
print("%.1f" % (x1/10))
print("%.1f" % (x2/10))