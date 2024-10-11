def generate_dict(n):
    square_dict = {x: x*x for x in range(1, n+1)}
    return square_dict

try:
    n = int(input("Enter a value for n: "))
    if n <= 0:
        raise ValueError("Please enter a positive integer for n.")

    result_dict = generate_dict(n)
    print("Generated Dictionary:", result_dict)

except ValueError as e:
    print(f"Error: {e}. Please enter a valid positive integer.")
