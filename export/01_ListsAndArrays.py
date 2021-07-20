# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Lists and Arrays in Python

# %%
import array
import numpy as np

# %% [markdown]
# ## Python List

# %%
my_list = [True, "Hello", 42.0, 420, None]

print([type(val) for val in my_list])

# %% [markdown]
# ## Python Array

# %%
my_array_range = list(range(10))
my_array = array.array('i', my_array_range)

print(my_array)

# %% [markdown]
# ### Array Dtypes
#
# |  |  |  |  |  |
# |-|-|-|-|-|
# | Type code | C Type | Python Type | Minimum size in bytes |
# | 'b' | signed char | int | 1 |
# | 'B' | unsigned char | int | 1 |
# | 'u' | wchar_t | Unicode character | 2 |
# | 'h' | signed short | int | 2 |
# | 'H' | unsigned short | int | 2 |
# | 'i' | signed int | int | 2 |
# | 'I' | unsigned int | int | 2 |
# | 'l' | signed long | int | 4 |
# | 'L' | unsigned long | int | 4 |
# | 'q' | signed long long | int | 8 |
# | 'Q' | unsigned long long | int | 8 |
# | 'f' | float | float | 4 |
# | 'd' | double | float | 8 |

# %%
my_array_range = list(range(10))
my_array = array.array('d', my_array_range)

print(my_array)

# %% [markdown]
# ## Numpy Array
# %% [markdown]
# NumPy is the fundamental package for scientific computing in Python.
# It is a Python library that provides a multidimensional array object, various derived objects, and an assortment of routines for fast operations on arrays.
#
# At the core of the NumPy package, is the ndarray object.
# This encapsulates n-dimensional arrays of homogeneous data types, with many operations being performed in compiled code for performance.

# %%
def array_info(array: np.ndarray) -> None:
    print(f"ndim: {array.ndim}")
    print(f"shape: {array.shape}")
    print(f"size: {array.size}")
    print(f"dtype: {array.dtype}")
    print(f"values:\n{array}\n")


# %%
my_np_array = np.array([1, 4, 2, 5, 3])
array_info(my_np_array)


# %%
my_np_array = np.array([3.14, 4, 2, 3])
array_info(my_np_array)


# %%
my_np_array = np.array([1, 2, 3, 4], dtype='float32')
array_info(my_np_array)

# %% [markdown]
# ## Intrinsic Arrays

# %%
my_np_array = np.zeros(shape=10, dtype=int)
array_info(my_np_array)


# %%
my_np_array = np.ones(shape=(3, 5), dtype=float)
array_info(my_np_array)


# %%
my_np_array = np.full(shape=(3, 5), fill_value=3.14)
array_info(my_np_array)


# %%
my_np_array = np.arange(start=0, stop=20, step=2)
array_info(my_np_array)


# %%
my_np_array = np.linspace(start=0, stop=1, num=5)
array_info(my_np_array)


# %%
my_np_array = np.eye(N=3)
array_info(my_np_array)


# %%
my_np_array = np.diag([1, 2, 3])
array_info(my_np_array)

# %% [markdown]
# ## Random Functions

# %%
my_np_array = np.random.randint(low=0, high=10, size=(3, 3))
array_info(my_np_array)


# %%
my_np_array = np.random.random(size=(3, 3))
array_info(my_np_array)


