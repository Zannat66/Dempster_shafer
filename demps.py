# Dempster-Shafer theory implementation

print("Welcome - Evidential Reasoning using Dempster-Shafer")
print("Intrinsic Quality\n")

w1 = float(input("Enter Accuracy weight: "))
w2 = float(input("Enter Reputation weight: "))

print("\nProbability mass calculation----")

print("\nEnter Degree of beliefs for Accuracy (w1): use float values of percentage")
b11 = float(input("Enter (B1,1): "))
b21 = float(input("Enter (B2,1): "))
b31 = float(input("Enter (B3,1): "))

print("\nEnter Degree of beliefs for Reputation (w2): use float values of percentage")
b12 = float(input("Enter (B1,2): "))
b22 = float(input("Enter (B2,2): "))
b32 = float(input("Enter (B3,2): "))

print("\nResults-------------------")
print("Probability mass for Accuracy (w1): ")
print("(m1,1) = " + str(w1*b11))
print("(m2,1) = " + str(w1*b21))
print("(m3,1) = " + str(w1*b31))
m11bar = 1 - w1
m11bar2 = (w1 * (1 - (b11 + b21 + b31)))
mh1 = m11bar + m11bar2
print("Remaining Probability mass : " + str(mh1))
print("m(1,1)bar = " + str(m11bar))
print("m(1,1)bar2 = " + str(m11bar2))

print("\nProbability mass for Reputation (w2): ")
print("(m1,2) = " + str(w2*b12))
print("(m2,2) = " + str(w2*b22))
print("(m3,2) = " + str(w2*b32))
m12bar = 1 - w2
m12bar2 = (w2 * (1 - (b12 + b22 + b32)))
mh2 = m12bar + m12bar2
print("Remaining Probability mass : " + str(mh2))
print("m(1,2)bar = " + str(m12bar))
print("m(1,2)bar2 = " + str(m12bar2))