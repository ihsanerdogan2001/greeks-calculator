import numpy as np
from scipy.stats import norm

class BlackScholesGreeks:
    def __init__(self, S, K, T, r, sigma, option_type="call"):
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        self.option_type = option_type.lower()
        self.d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
        self.d2 = self.d1 - sigma * np.sqrt(T)

    def delta(self):
        if self.option_type == "call":
            return norm.cdf(self.d1)
        elif self.option_type == "put":
            return norm.cdf(self.d1) - 1

    def gamma(self):
        return norm.pdf(self.d1) / (self.S * self.sigma * np.sqrt(self.T))

    def vega(self):
        return self.S * norm.pdf(self.d1) * np.sqrt(self.T) / 100

    def theta(self):
        if self.option_type == "call":
            return (-self.S * norm.pdf(self.d1) * self.sigma / (2 * np.sqrt(self.T))
                    - self.r * self.K * np.exp(-self.r * self.T) * norm.cdf(self.d2)) / 365
        elif self.option_type == "put":
            return (-self.S * norm.pdf(self.d1) * self.sigma / (2 * np.sqrt(self.T))
                    + self.r * self.K * np.exp(-self.r * self.T) * norm.cdf(-self.d2)) / 365

    def rho(self):
        if self.option_type == "call":
            return self.K * self.T * np.exp(-self.r * self.T) * norm.cdf(self.d2) / 100
        elif self.option_type == "put":
            return -self.K * self.T * np.exp(-self.r * self.T) * norm.cdf(-self.d2) / 100
