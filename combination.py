import numpy as np 

# implement your function to combine two numpy arrays 

def combination(array_one, array_two, axis = 0):
    array_one = np.squeeze(array_one)
    array_two = np.squeeze(array_two)
    if not np.can_cast(array_one.dtype, array_two.dtype):
        raise ValueError("Arrays cannot be combined due to incompatible data types.")
    
    try:
        combined = np.concatenate((array_one, array_two), axis=axis)
        return combined
    except ValueError:
        raise ValueError("Arrays cannot be combined along the specified axis.")



if __name__ == "__main__":
    print(combination(np.array([1, 2, 3]), np.array([2, 3, 4])))

