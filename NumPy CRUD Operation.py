#!/usr/bin/env python
# coding: utf-8

# In[50]:


import numpy
import numpy as np
numpy.version


# # CRUD Operation

# In[1]:





# # C - Create

# In[2]:


# np.array()
arr = np.array([[1,2,3],[4,5,6]])


# In[3]:


arr = np.array({1,2,3})


# In[4]:


arr


# In[5]:


arr.ndim


# In[6]:


# np.zeros()
arr = np.zeros([10,3,4])

# 1D
# 2D


# In[7]:


arr


# In[8]:


# np.ones()
arr = np.ones([10,9])


# In[9]:


arr


# In[10]:


# np.empty()
arr = np.empty([4,4])


# In[11]:


arr


# In[12]:


# np.full()

arr = np.full([3,4,4],5)


# In[13]:


arr


# In[14]:


# np.eye() -> Identity Matrix
# No. of Rows = No. of Columns = 9
arr = np.eye(4)


# In[15]:


arr


# In[16]:


# np.diag()

arr = np.diag([10,20,30,40,50,60,70,80,90,100])


# In[17]:


arr


# In[18]:


# np.linspace()

# 10,100,10
# 10 40 45 ,78,40
# 10, 20, 30, 40, 50, 60, 70, 80, 90, 100

arr = np.linspace(1,10, 20)


# In[19]:


arr


# In[20]:


# np.random()

arr = np.random.randint(15,25, size=(2,3))


# In[21]:


arr


# In[22]:


# np.arange()

arr = np.arange(1,12,2)


# In[23]:


arr


# # U -> Update

# In[24]:


arr1 = np.array([1,2,3,4,5])
arr2  = np.array([[1,2,3,4],[5,6,7,8],[1,3,5,7]])
arr3  = np.array([
                  [
                   [1,2,3],
                   [4,5,6]
                  ],
                  [
                     [7,8,9],
                     [11,12,12]
                  ]
                  ])


# In[25]:


arr


# In[57]:


arr1[-1] 
arr1[4]  


# In[58]:


arr2[2,2]


# In[27]:


arr3


# In[28]:


arr3[0,1,1] = 23


# In[29]:


arr3


# In[30]:


# Slicing


# In[31]:


arr2


# In[32]:


arr2[1:2]


# In[33]:


arr3


# In[34]:


arr3[0,1,0:2]
arr3[0,1][0:2]

# Error
# Might be yes


# In[35]:


# Quiz

# Create a matrix 3x4, 10 to 500 + elements should be evenly distributed

arr = np.linspace(10,500,18)

# element (12) % n-dimesion == 0


# In[36]:


arr.reshape(3,3,2)

# 3D
# Error


# In[37]:


# reshape


# In[38]:


arr = np.array(12)
arr


# In[39]:


# Create a 7X9 matrix where all the elements are random


arr = np.random.rand(63).reshape(7,9)


# In[40]:


arr


# In[41]:


arr2


# In[42]:


arr2d = np.array([[1, 2, 3], [4, 5, 6]])  # 2D array
arr2dd = np.array([[7, 8, 9], [10, 11, 12]])  # 2D array


# In[61]:


arr2d


# In[62]:


arr2dd


# In[63]:


# Append along axis 1 (columns)
result = np.append(arr2d, arr2dd, axis=1)
print(result)


# In[64]:


np.append([arr2d],[arr2dd], axis=0)


# In[65]:


arrop  = np.array([[1,2,3,4],[5,6,7,8],[1,3,5,7]])
arrpo  = np.array([[1,2,3,4],[5,6,7,8],[1,3,5,7]])


# In[66]:


arrop * arrpo
# 2 Types - Cross & Dot Multiplication


# # R -> Read

# In[67]:


arr1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


# In[68]:


# Read a specific element
element = arr1[1, 2]  # Access the element at row 1, column 2
print("Element at row 1, column 2:", element)


# In[69]:


# Read a specific row
row = arr1[1, :]  
print("Row 1:", row)


# In[70]:


# Read a specific column
column = arr1[:, 2]  
print("Column 2:", column)


# In[71]:


# Read a subarray
subarray = arr1[0:2, 1:3]  
print("Subarray (first two rows, last two columns):")
print(subarray)


# # D -> Delete

# In[82]:


arr1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


# In[83]:


# Flatten the array to 1D
flat_arr1 = arr1.flatten()


# In[84]:


flat_arr1 


# In[85]:


# Delete the element at index 4 (which is the value 5 in the original array)
flat_arr1 = np.delete(flat_arr1, 4)


# In[86]:


flat_arr1


# In[87]:


reshaped_arr1 = flat_arr1.reshape(2, 4)  # Example: reshape into (2, 4)
print("Array after deleting element at index 4 and reshaping to (2, 4):")
print(reshaped_arr1)

