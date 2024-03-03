# Libraries required
import numpy as np
import matplotlib.pyplot as plt


    # Exercise 1: Histogram of uniform random numbers in [0, 1]

# Sample uniform random numbers on [0, 1]
muestra_uniforme = np.random.uniform(0, 1, 100000) # 100000 is the sample size
print(muestra_uniforme)

# Sample histogram
plt.figure('Exercise 1')
plt.hist(muestra_uniforme, bins=50, density=True, alpha=0.6, color='royalblue', edgecolor='black', label='empirical values')
plt.axhline(1, color="orangered", linewidth=2, label='theoric value')
plt.title('Histogram of uniform random numbers on [0, 1]', fontweight="bold")
plt.legend(loc = 'lower left')
plt.xlabel('X', fontstyle='italic')
plt.ylabel('Normalized Frequency', fontstyle='italic')
plt.grid(True)
plt.show()


    # Exercise 2: Histogram of the transformed sample with exponential distribution

# Arrangement of numbers to represent our theoretical values of the cdf
x_aux = np.arange(0, 10, 0.1) 

# Probability density function pdf_x (Exponential)
def pdf_Exp(x, theta):
    pdf_x = 1 / theta * np.exp(- x / theta)
    return pdf_x

# Inverse function of the cdf_x (Exponential)
def cdf_Inverse_Exp(f, theta):
    cdf_x_inv = - theta * np.log(1.0 - f)
    return cdf_x_inv

# Sample transformed from the inverse cdf_x (Exponential)
theta = 2
muestra_exp = cdf_Inverse_Exp(muestra_uniforme, theta)
print(max(muestra_exp))

# Calculate theoretical values from the pdf (Exponential)
pdf_exp = pdf_Exp(x_aux, theta)  

# Histogram of the transformed sample
plt.figure('Exercise 2')
plt.hist(muestra_exp, bins=50, density=True, alpha=0.6, color='crimson', edgecolor='black', label='empirical values')
plt.plot(x_aux, pdf_exp, color = 'b', label='theoric value')   # Add the theoretical line
plt.title('Exponential Distribution of a sample with pdf_X(x;θ=2)', fontweight="bold")
plt.legend(loc = 'upper right')
plt.xlabel('X', fontstyle='italic')
plt.ylabel('Probability density (pdf)', fontstyle='italic')
plt.grid(True)
plt.show()


    # Exercise 3: Histogram of the sample transformed with Rayleigh distribution
    
# Probability density function pdf_x (Rayleigh)
def pdf_Rayleigh(x,sigma):
    pdf_x = x / (sigma ** 2) * np.exp(- (x ** 2) / 2 * (sigma ** 2))
    return pdf_x

# Inverse function of the cdf_x (Rayleigh)
def cdf_Inverse_Rayleigh(f, sigma):
    cdf_x_inv = np.sqrt(-2 * (sigma ** 2) * np.log(1.0-f))
    return cdf_x_inv

# Sample transformed from the inverse cdf_x (Rayleigh)
sigma = 1
muestra_rayleigh = cdf_Inverse_Rayleigh(muestra_uniforme, sigma) 

# Calculate theoretical values from the pdf (Rayleigh)
pdf_exp = pdf_Rayleigh(x_aux, sigma)  

# Histogram of the transformed sample
plt.figure('Exercise 3')
plt.hist(muestra_rayleigh, bins=50, density=True, alpha=0.6, color='limegreen', edgecolor='black', label='empirical values')
plt.plot(x_aux, pdf_exp, color = 'b', label='theoric value')   # Add the theoretical line
plt.title('Rayleigh distribution of a sample with pdf_X(x;σ=1)', fontweight="bold")
plt.legend(loc = 'upper right')
plt.xlabel('X', fontstyle='italic')
plt.ylabel('Probability density (pdf)', fontstyle='italic')
plt.grid(True)
plt.show()