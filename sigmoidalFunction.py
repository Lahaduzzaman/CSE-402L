# import numpy library
import numpy as np
# define inputs
x=np.array([0.2,0.4,0.7])
# weight values
w=np.array([0.4,-0.1,0.6])

print("Inputs:")
print(x)
print("Weights:")
print(w)

# transpose the weight matrix
w_t=np.transpose(w)
print("Weight matrix transposed")
print(w_t)
# assigning bias
b=-1.0
print("Bias:")
print(b)

# feedforward computaton
u=w_t*x
v=u[0]+u[1]+u[2]+b
print("Activation Potential:")
print(v)
# applying sigmoidal function
y=1/(1+np.exp(-v))
# print the output
print("Output")
print(y)
