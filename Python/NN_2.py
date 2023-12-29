input = [1, 2, 3, 2.5]
weight = [[0.2, 0.8, -0.5, 1], [0.5, -0.91, 0.26, -0.5], [-0.26, -0.27, 0.17, 0.87]]
bias = [2, 3, 0.5]

output = []

for i in range(0, len(weight)):
    output_layer = 0
    for j in range(0, len(input)):
        output_layer += input[j] * weight[i][j]
    output_layer += bias[i]
    output.append(output_layer)

print(output)
