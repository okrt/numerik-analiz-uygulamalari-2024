def lagrange_interpolation(x_values, y_values, x):
    result = 0.0
    for i in range(len(x_values)):
        term = y_values[i]
        for j in range(len(x_values)):
            if j != i:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term
    return result

x_values = [1, 2, 3, 4]
y_values = [1, 4, 9, 16]
x = 2.5
interpolated_y = lagrange_interpolation(x_values, y_values, x)
print(f"Interpolasyon sonucu x={x} {interpolated_y}")
