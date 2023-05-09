import numpy as np

# implement the function gaussian_analysis

def gaussian_analysis(loc, scale, lower_bound, upper_bound):

    if not isinstance(loc, (int, float)) or not isinstance(scale, (int, float)) or not isinstance(lower_bound, (int, float)) or not isinstance(upper_bound, (int, float)):
        raise ValueError("loc, scale, upper_bound and lower_bound must be integers or floats.")

    if lower_bound >= upper_bound:
        raise ValueError("lower_bound must be smaller than upper_bound.")
        
    samples = np.random.normal(loc, scale, 100)
    
    filtered_samples = samples[(samples >= lower_bound) & (samples <= upper_bound)]
    
    mean = np.mean(filtered_samples)
    std = np.std(filtered_samples)
    
    return mean, std


if __name__ == "__main__":
    result = gaussian_analysis(0, 1, -1, 1)
    print(result)
