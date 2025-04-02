def arctan_approximation(x):
    if x < 0 or x > 1:
        return "Error!"

    approximation = 0
    error_bound = float('inf')
    i = 0
    while (error_bound > 0.0001):
        approximation += ((-1)**i)*(x**(2*i+1))/(2*i+1)
        error_bound = (x**(2*(i+1)))/(2*(i+1))
        i+=1
    return (approximation, i, error_bound)

test_values = [-1, 0, 0.25, 0.5, 0.75, 1]
for values in test_values:
    result = arctan_approximation(values)
    print(f"arctan_approximation({values}) = {result}")