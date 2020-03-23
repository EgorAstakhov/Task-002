a = str(input('Name of the geometric shape: '))
if a == "Circle" or "circle":
    b = float(input("Length r : "))
    print("S = ", b, "* pi = ", b*3.14)
elif a == "Square" or "square":
    c = float(input("Enter the side length: "))
    print("S = ", c, " * ", c, " = ", c*c)
elif a == "Triangle" or "triangle":
    e = float(input("Enter the side length a: "))
    g = float(input("Enter the side length b: "))
    r = float(input("Enter the side length c: "))
    print("S = (a+b+c) / 2 = ", (e+g+r)/2)
else:
    print("You entered something wrong!")