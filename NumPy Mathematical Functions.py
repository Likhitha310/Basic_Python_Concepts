#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


arr1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
arr2 = np.array([[10,9,8,7,6],[5,4,3,2,1]])


# In[3]:


arr1


# In[4]:


arr2


# # Mathematical Functions & Stats

# # * Addition -> Add two matrices or add an element to a matix

# In[5]:


# Adding two matrics
arr1 + arr2


# In[6]:


# Adding an element
arr1 + 20


# In[7]:


arr3 = np.array([[1],[2]])
arr3


# In[8]:


arr3.shape


# In[9]:


arr1 + arr3


# In[ ]:


arr1


# # * Substraction

# In[ ]:


arr1


# In[ ]:


arr2


# In[ ]:


arr1 - arr2


# In[ ]:


arr1 - 100


# # * Division

# In[15]:


arr1


# In[16]:


arr2


# In[17]:


arr1 / arr2


# In[18]:


arr1/arr1


# In[19]:


arr1 / 4


# # * Exponential

# In[20]:


arr1


# In[21]:


arr2


# In[22]:


arr1 ** arr2


# In[23]:


arr1 ** 2


# # * Multiplication - Cross & Dot

# In[24]:


arr1
# 2 X 5


# In[25]:


arr2

# 2 x 5


# In[26]:


# Cross Product
arr1 * arr2


# In[27]:


# Dot Product


# In[28]:


arr3 = np.array([[1,2],[3,4],[5,6],[7,8],[9,10]])


# In[29]:


arr3.ndim


# In[30]:


arr3.shape


# In[31]:


# np.dot(arr1,arr3)
np.dot(arr3,arr1)

# np.matmul(arr1, arr3)
np.matmul(arr1, arr3)


# In[32]:


np.dot(arr1,arr3)


# # Determinant

# In[33]:


# Square matrix -> No. of rows = No. of columns
# Square matrix -> No. of rows & No. of columns = Same

detarray = np.array([[-4,-10],[0,5]])


# In[38]:


# np.linalg.det(arr)

np.linalg.det(detarray)


# In[39]:


detarray3 = np.array([[-4,-10,-6],[0,5,7], [-9, 6, 0]])


# In[40]:


np.linalg.det(detarray3)


# # * Inverse of a matrix

# In[41]:


arrinv = np.array([[1,2],[3,4]])


# In[42]:


arrinv


# In[44]:


arrinv
deter = np.linalg.det(arrinv)


# In[45]:


newdet = 1/deter


# In[46]:


newdet


# In[47]:


# Inverse of the matrix

np.linalg.inv(arrinv)


# In[48]:


arrinv.transpose()


# # * Reciprocal

# In[50]:


arreci = np.array([[10,20],[30,40]], dtype='float')


# In[51]:


arreci


# In[52]:


# np.reciprocal(array_name)
# 1/element
np.reciprocal(arreci)


# # Statistics

# In[53]:


statarr = np.array([[20, 50, -40],[9, 10, -1],[7, 26, 34]])


# In[54]:


statarr


# # * max()

# In[55]:


np.max(statarr)


# In[56]:


np.max(statarr, axis=0)
# [20, 50, 34]


# In[57]:


np.max(statarr, axis=1)


# # * min()

# In[58]:


statarr


# In[59]:


np.min(statarr)


# In[60]:


np.min(statarr, axis=0)


# In[61]:


np.min(statarr, axis=1)


# # * Sum

# In[63]:


statarr


# In[64]:


np.sum(statarr)


# In[65]:


np.sum(statarr, axis=0)
[36, 86, -7]


# In[66]:


np.sum(statarr, axis=1)
[30, 18, 67]


# # * argmax()

# In[67]:


statarr


# In[68]:


np.argmax(statarr)


# In[69]:


np.argmin(statarr)


# In[70]:


statarr[2,1] = 100
statarr[1,1] = -100


# In[71]:


np.argmax(statarr,axis=1)
# [1, 0, 1]


# In[72]:


np.argmax(statarr,axis=0)


# # * argmin()

# In[73]:


np.argmin(statarr)


# In[74]:


np.argmin(statarr,axis=1)


# In[75]:


np.argmin(statarr,axis=0)


# # * around()

# In[76]:


arr = np.array([3.501, 0.98])


# In[77]:


np.around(arr,decimals=3)
# [0,0]
# [0,1]
# [1,1]
# [3.501, 1.000]
# [3.501, 0.98]
# [3.500, 1.000]


# # * floor & ceil

# In[78]:


a = np.array([-1.7, -4.2, 4.6, -0.87])


# In[79]:


np.floor(a)
# [-2, -5, 4, -1]


# In[80]:


np.ceil(a)
# [-1, -4, 5, 0]


# # * Copy & View

# In[81]:


arr


# In[82]:


# Copy

x = arr.copy()
x


# In[83]:


x[0] = 10


# In[84]:


x


# In[85]:


arr


# In[86]:


# View

y = arr.view()


# In[87]:


y[0] = 10


# In[88]:


y


# In[89]:


arr


# # * Iteration

# In[90]:


arr


# In[91]:


for i in arr:
  print(i)


# In[92]:


for i in np.nditer(arr1[1]):
  print(i)


# In[93]:


arr1


# In[94]:


for i in range(10):
  print("Hey")


# In[95]:


print("Hey")
print("Hey")
print("Hey")
print("Hey")
print("Hey")
print("Hey")
print("Hey")
print("Hey")
print("Hey")
print("Hey")

