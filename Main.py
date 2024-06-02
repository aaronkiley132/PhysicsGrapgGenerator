import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

#-------------------------------------------------------------------
# Data
#-------------------------------------------------------------------

#main data
x_data = np.array([343, 338, 333, 328, 323, 318, 313, 308, 298])
y_data = np.array([0.5, 0.57, 0.68, 0.81, 0.95, 1.08, 1.22, 1.43, 1.87])

#error bars
x_error_bars = np.array([2, 2, 2, 2, 2, 2, 2, 2, 2])
y_error_bars = np.array([0.10, 0.11, 0.06, 0.06, 0.09, 0.11, 0.16, 0.21, 0.13])

#shallow
shallow_x = np.array([343, 298])
shallow_y = np.array([0.425, 1.75])

#steep
steep_x = np.array([343, 298])
steep_y = np.array([0.40, 1.80])


#-------------------------------------------------------------------
#Functions
#-------------------------------------------------------------------

# Defines a quadratic function to model the data
def linear_func(x, a, b):
    return a * x + b


#-------------------------------------------------------------------
#Main Program
#-------------------------------------------------------------------

# Fit the data using curve_fit
params, covariance = curve_fit(linear_func, x_data, y_data)
a, b = params
steep_params, steep_covariance = curve_fit(linear_func, steep_x, steep_y)
a_steep, b_steep = steep_params
shallow_params, shallow_covariance = curve_fit(linear_func, shallow_x, shallow_y)
a_shallow, b_shallow = shallow_params

# Print the resulting function
print(f"The line of best fit is: y = {a:.4f}x + {b:.4f}")
print(f"The steep line of best fit is: y = {a_steep:.4f}x + {b_steep:.4f}")
print(f"The shallow line of best fit is: y = {a_shallow:.4f}x + {b_shallow:.4f}")

# Plot the data and the fit
plt.errorbar(x_data, y_data, yerr=y_error_bars, xerr=x_error_bars, fmt='o')
plt.scatter(x_data, y_data)
x_fit = np.linspace(min(x_data), max(x_data), 100)
steep_fit = np.linspace(min(steep_x), max(steep_x), 100)
shallow_fit = np.linspace(min(shallow_x), max(shallow_x), 100)
plt.plot(x_fit, linear_func(x_fit, *params), color='blue', label=f"Best : y = {a:.4f}x + {b:.4f}")
plt.plot(steep_fit, linear_func(steep_fit, *steep_params), color='orange', label=f"Steep : y = {a_steep:.4f}x + {b_steep:.4f}")
plt.plot(shallow_fit, linear_func(shallow_fit, *shallow_params), color='grey', label=f"Shallow : y = {a_shallow:.4f}x + {b_shallow:.4f}")
plt.xlabel('Temperature °K', fontsize=16)
plt.ylabel('ln(viscosity) / Pas', fontsize=16)
plt.title("ln(Viscosity) - Temperature", fontsize=18)
plt.legend(prop={'size': 14})
plt.show()
