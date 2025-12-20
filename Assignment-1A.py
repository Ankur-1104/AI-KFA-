# Assignment-1A
# Gradient Descent for Best Fit Line 

print("Program to find the equation of best fit line using Gradient Descent")

# Input section
x_values = []
y_values = []

try:
    n = int(input("Enter number of data points: "))
    for i in range(n):
        x, y = map(int, input(f"Enter data point {i+1} (x,y): ").split(','))
        x_values.append(x)
        y_values.append(y)
except ValueError:
    print("Error! Please use format: x,y (e.g., 1,2)")
    exit()

# Parameters
learning_rate = 0.01
target = 0.001
max_iterations = 1000
N = len(x_values)

# Initial guess
m = 0
b = 0
iteration = 0

# Gradient Descent Loop
while iteration < max_iterations:
    # Predictions and errors
    y_pred = [(m * x_values[i] + b) for i in range(N)]
    errors = [(y_pred[i] - y_values[i]) for i in range(N)]

    # Cost function
    cost = (1 / (2 * N)) * sum(error ** 2 for error in errors)

    if cost <= target:
        break

    # Gradients
    dm = (1 / N) * sum(errors[i] * x_values[i] for i in range(N))
    db = (1 / N) * sum(errors)

    # Update parameters
    m = m - learning_rate * dm
    b = b - learning_rate * db

    iteration += 1

# Output
print("\nBest Fit Line Equation:")
print(f"y = {m:.3f}x + {b:.3f}")
print(f"Final cost = {cost:.6f}")

