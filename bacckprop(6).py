import numpy as np

x = np.array([[2, 9], [1, 5], [3, 6]], dtype=float)
x /= np.amax(x, axis=0)  # Normalize after defining x
y = np.array([[92], [86], [89]], dtype=float) / 100

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

epochs = 5000
lr = 0.1
input_neurons, hidden_neurons, output_neurons = 2, 3, 1

wh = np.random.uniform(size=(input_neurons, hidden_neurons))
bh = np.random.uniform(size=(1, hidden_neurons))
wout = np.random.uniform(size=(hidden_neurons, output_neurons))
bout = np.random.uniform(size=(1, output_neurons))

for _ in range(epochs):
    
    hidden_input = np.dot(x, wh) + bh
    hidden_output = sigmoid(hidden_input)
    output_input = np.dot(hidden_output, wout) + bout
    output = sigmoid(output_input)

    error = y - output
    output_gradient = sigmoid_derivative(output)
    hidden_error = error.dot(wout.T)
    hidden_gradient = sigmoid_derivative(hidden_output)

    wout += hidden_output.T.dot(error * output_gradient) * lr
    wh += x.T.dot(hidden_error * hidden_gradient) * lr

print("Input:\n", x)
print("Actual Output:\n", y)
print("Predicted Output:\n", output)
