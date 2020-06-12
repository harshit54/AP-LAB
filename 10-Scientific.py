import math

print("What Do You Want To Calculate?")
print("A - Sine")
print("B - Cosine")
print("C - Tangent")
t = input()
print("Enter Angle In Degrees: ")
ang = float(input())
pi = math.acos(-1)
if t == "A" or t == "a":
    print("sin(" + str(ang) + ") = " + str(math.sin(ang*pi/180)))

elif t == "B" or t == "b":
    print("cos(" + str(ang) + ") = " + str(math.cos(ang*pi/180)))

elif t == "C" or t == "c":
    print("tan(" + str(ang) + ") = " + str(math.tan(ang*pi/180)))