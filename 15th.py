setA = {1, 2, 3, 4, 5}
setB = {1, 2, 3}
setC = {1, 2, 3, 6, 7}
print("setA: ", setA)
print("setB: ", setB)
print("setC: ", setC)

print("Is setB a subset of setA?: ", setB.issubset(setA))
print("Is setA a subset of setB?: ", setA.issubset(setB))
print("Is setC a subset of setA?: ", setC.issubset(setA))
