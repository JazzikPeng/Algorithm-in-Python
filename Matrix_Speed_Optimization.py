# Numpy matrix speed optimization


# Python matrix multiplicaiton optimization:
def matrix_multiplication_loop(A,B):
    m = A.shape[0]
    n = A.shape[1]
    l = B.shape[1]
    C = np.zeros([m,l])
    for i in range(m):
        for j in range(l):
            for k in range(n):
                C += A[i][k]*B[k][j]
    return C
A = np.random.random([300,12])
B = np.random.random([12,256])
get_ipython().run_line_magic('timeit', 'C = matrix_multiplication_loop(A,B)')
#1 loop, best of 3: 2.22 s per loop

'''作者：霍华德
链接：https://www.zhihu.com/question/67310504/answer/252179088
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。'''


# In[80]:


get_ipython().run_line_magic('timeit', 'C = np.dot(A,B)')
#10000 loops, best of 3: 105 µs per loop


# In[81]:


import numba
@numba.autojit
def matrix_multiplication_numba(A,B):
    return np.dot(A,B)
get_ipython().run_line_magic('timeit', 'C = matrix_multiplication_numba(A,B)')
#10000 loops, best of 3: 55 µs per loop


# In[82]:


get_ipython().run_line_magic('load_ext', 'Cython')


# In[83]:


get_ipython().run_cell_magic('cython', '', 'cdef int a = 0\nfor i in range(10):\n    a+=i\nprint(a)')


# In[84]:


import tensorflow as tf
A = tf.random_normal([3000,1280])
B = tf.random_normal([1280,2560])
C = tf.matmul(A,B)
with tf.Session() as sess:
    get_ipython().run_line_magic('timeit', 'result = sess.run(C)')
#100 loops, best of 3: 4.83 ms per loop


# In[85]:


A = np.random.random([3000,1280])
B = np.random.random([1280,2560])
get_ipython().run_line_magic('timeit', 'C = np.dot(A,B)')
#1 loop, best of 3: 582 ms per loop

