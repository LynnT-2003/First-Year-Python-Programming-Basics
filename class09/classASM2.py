def DoubleTriple(x):
    V = x
    doubleV = 2 * x
    tripleV = 3 * x
    return V,doubleV,tripleV

original,double,triple = DoubleTriple(int(input("Enter an integer: ")))
print("Original value = " + str(original))
print("Doubled value = " + str(double))
print("Tripled value = " + str(triple))

