import numpy as np
print("output result0")
result0 = np.where([[True,False],[True,True]],[[1,2],[3,4]],[[5,6],[7,8]])
print(result0)

print("output result1")
result1 = np.where([[True,True],[True,True]],[[1,2],[3,4]],[[5,6],[7,8]])
print(result1)

print("output result2")
result2 = np.where([[False,False],[True,True]],[[1,2],[3,4]],[[5,6],[7,8]])
print(result2)

print("output result3")
result3 = np.where([[False,True],[True,True]],[[1,2],[3,4]],[[5,6],[7,8]])
print(result3)

print("output result4")
result4 = np.where([[False,True],[False,False]],[[1,2],[3,4]],[[5,6],[7,8]])
print(result4)