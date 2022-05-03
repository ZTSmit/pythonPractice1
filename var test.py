from math import factorial

testVarBase = 50
testVarBase2 = 55
#testVarMult = 2 #2 factorial less interesting
testVarMult = 4
testVarBool = True


testVarB2_String = str(testVarBase2)
testVar_StrToInt = int(testVarB2_String)
testVarB2_dupe = testVarB2_String
testVar_Concat = int(testVarB2_dupe + testVarB2_String)
testVarMultFactorial = factorial(testVarMult)
testVar_ConcatFloat = float((testVarB2_String+"."+testVarB2_String))

print(testVarBase)
print(testVarBase2 + testVarBase)
print(testVarB2_String)
print(testVarB2_String + str(testVarBase2))
print(testVar_StrToInt + testVarBase)
print(testVarB2_dupe)
print(testVar_Concat)
print(testVar_Concat * testVarMult)
#print(testVariable3*testVariable5)
print(testVarBase2 / testVarBase)
print((testVarBase2 / testVarBase) + testVarMult)
#print(testVariableMult!)
print(testVarBase % testVarMult)
print(str(testVarBool) + testVarB2_String)
print(testVarMultFactorial)
print(2 * testVarBase)
print(testVar_ConcatFloat*testVarMult)