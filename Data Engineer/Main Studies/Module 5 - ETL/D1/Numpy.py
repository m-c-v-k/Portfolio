#! python3

# Importing necesssary libraries
import time
import numpy as np
import sys

# 1.1
dataset_digits = 8  # SCales exponentially

dataset_size = 10 ** dataset_digits

# Generate with traditional python and numpoy method
python_list = [1] * dataset_size
numpy_array = np.ones(dataset_size)

# Measure python time for multiplying eacxh value by 1024
time_start = time.time()
python_list = [x * 1024 for x in python_list]

time_py = time.time() - time_start
py_size = sys.getsizeof(python_list) / 1000  # Size in mb
# print(python_list[:10]) # Data sample

# Measure numpy time for multiplying each value by 1024
time_start = time.time()
numpy_array = numpy_array * 1024

time_np = time.time() - time_start
np_size = sys.getsizeof(numpy_array) / 1000  # Size in mb
# print(numpy_array[:10]) # Data sample

print(f"Python computation time: {time_py}s")
print(f"Numpy computation time: {time_np}s")

print(f"Python list size: {py_size}mb")
print(f"Numpy array size: {np_size} mb")
