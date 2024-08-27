#!/usr/bin/env python
# coding: utf-8

# # More with NumPy

# In[ ]:


import numpy as np


# # 1. Stacking (hstack, vstack, dstack)

# In[11]:


arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
result = np.hstack((arr1, arr2))
print(result)  


# In[12]:


arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
result = np.vstack((arr1, arr2))
print(result)  


# In[13]:


arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])
result = np.dstack((arr1, arr2))
print(result)


# # 2. Splitting

# In[14]:


arr = np.array([1, 2, 3, 4, 5, 6])
result = np.split(arr, 3)
print(result)  


# In[15]:


arr = np.array([[1, 2, 3], [4, 5, 6]])
result = np.hsplit(arr, 3)
print(result) 


# In[16]:


arr = np.array([[1, 2, 3], [4, 5, 6]])
result = np.vsplit(arr, 2)
print(result)  


# # 3. Slicing

# In[17]:


arr = np.array([1, 2, 3, 4, 5, 6])
result = arr[1:4]
print(result) 


# # 4. Searching

# In[18]:


arr = np.array([1, 2, 3, 4, 5, 6])
result = np.where(arr > 3)
print(result)  


# In[19]:


arr = np.array([1, 2, 3, 4, 5])
result = np.searchsorted(arr, 3)
print(result)  


# # 5. Sorting

# In[20]:


arr = np.array([3, 1, 2, 5, 4])
result = np.sort(arr)
print(result)  


# In[21]:


arr = np.array([3, 1, 2, 5, 4])
result = np.argsort(arr)
print(result)  


# # 6. All/Any

# In[22]:


arr = np.array([True, True, False])
result = np.all(arr)
print(result) 


# In[23]:


arr = np.array([True, True, False])
result = np.all(arr)
print(result)  


# # 7. Resize

# In[24]:


arr = np.array([1, 2, 3, 4, 5, 6])
result = np.resize(arr, (2, 3))
print(result) 


# # 8. Delete

# In[25]:


arr = np.array([1, 2, 3, 4, 5])
result = np.delete(arr, 2)
print(result) 


# # 9. LCM (Least Common Multiple)

# In[26]:


arr = np.array([4, 6, 8])
result = np.lcm.reduce(arr)
print(result) 


# # 10. GCD (Greatest Common Divisor)

# In[27]:


arr = np.array([12, 15, 21])
result = np.gcd.reduce(arr)
print(result)  


# # 11. Solving Linear Equations

# In[28]:


A = np.array([[1, 2], [3, 4]])
b = np.array([5, 6])
x = np.linalg.solve(A, b)
print(x)  


# # 12. Solving Quadratic Equations

# In[29]:


coeff = [1, -7, 12]  
roots = np.roots(coeff)
print(roots)  


# # 13. Dot Product (vdot)

# In[30]:


arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
result = np.vdot(arr1, arr2)
print(result) 


# # 14. Mean

# In[31]:


arr = np.array([1, 2, 3, 4, 5])
result = np.mean(arr)
print(result)  


# # 15. Weighted Mean

# In[32]:


arr = np.array([1, 2, 3, 4])
weights = np.array([0.1, 0.2, 0.3, 0.4])
result = np.average(arr, weights=weights)
print(result) 


# # 16. Square Root

# In[33]:


arr = np.array([1, 4, 9, 16])
result = np.sqrt(arr)
print(result)  


# # 17. Shape Manipulation

# In[34]:


arr = np.array([1, 2, 3, 4, 5, 6])
result = arr.reshape((2, 3))
print(result)  


# In[35]:


arr = np.array([[1, 2, 3], [4, 5, 6]])
result = np.transpose(arr)
print(result)  


# In[36]:


arr = np.array([1, 2, 3])
result = np.expand_dims(arr, axis=0)
print(result)  


# In[37]:


arr = np.array([[[1, 2, 3]]])
result = np.squeeze(arr)
print(result)  


# # 18.Array Generation

# In[39]:


result = np.arange(0, 10, 2)
print(result)  


# In[40]:


result = np.linspace(0, 1, 5)
print(result)  


# In[41]:


x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
xv, yv = np.meshgrid(x, y)
print(xv)  
print(yv)  


# # 19.Copying and Broadcasting

# In[42]:


arr = np.array([1, 2, 3])
arr_copy = arr.copy()
arr_copy[0] = 10
print(arr)      
print(arr_copy) 


# In[43]:


arr1 = np.array([1, 2, 3])
arr2 = np.array([[4], [5], [6]])
result = arr1 + arr2
print(result)  


# # 20.Memory Layout

# In[44]:


arr = np.array([[1, 2, 3], [4, 5, 6]])
result = np.ravel(arr)
print(result)  


# In[45]:


arr = np.array([[1, 2, 3], [4, 5, 6]])
result = arr.flatten()
print(result)  


# # 21.Indexing Techniques

# In[46]:


arr = np.array([10, 20, 30, 40, 50])
indices = np.array([1, 3])
result = arr[indices]
print(result)  


# In[47]:


arr = np.array([1, 2, 3, 4, 5])
mask = arr > 3
result = arr[mask]
print(result)  


# # 22.Advanced Functions

# In[48]:


arr = np.array([1, 2, 2, 3, 3, 3])
result = np.unique(arr)
print(result)  


# In[49]:


arr = np.array([1, 2, 3])
result = np.tile(arr, 2)
print(result) 


# In[50]:


arr = np.array([1, 2, 3])
result = np.repeat(arr, 2)
print(result)  


# In[51]:


arr = np.array([1, 2, 3, 4, 5])
result = np.clip(arr, 2, 4)
print(result)  


# # 23. String Operations

# In[52]:


arr1 = np.array(['Hello'])
arr2 = np.array(['World'])
result = np.char.add(arr1, arr2)
print(result)  


# In[53]:


arr = np.array(['Hello', 'World'])
result = np.char.lower(arr)
print(result)  


# In[ ]:




