import matplotlib.pyplot as plt
import numpy as np
from src.data_analysis import DataAnalysis
from src.confidence_interval import ConfidenceInterval
import scipy.stats as st

class Plotter:

    def __init__(self, X):
        self.X = X

    def plot_hist(self):
        fig, ax = plt.subplots(1,1)
        ax.hist(x=self.X, bins=10, histtype='step', linewidth=3.5, density=False)
        ax.tick_params(axis='both', which='major', labelsize=15)
        ax.axvline(self.X.mean(), color='k', linestyle='dashed', linewidth=2)
        ax.set_xlabel("X", size=20)
        ax.set_ylabel("P(X = x)", size=20)
        plt.title("Histogram", size=20)
        plt.show()

    def plot_cdf(self, dx=1e-5):
        data_analysis = DataAnalysis(self.X)
        xs = self.__get_bins__(dx)
        fig, ax = plt.subplots(1,1)
        ax.plot(xs,data_analysis.cdf_range(xs), label='Fe')
        ax.plot(xs, st.norm.cdf(xs, loc=self.X.mean(), scale=self.X.std()), label='F')
        ax.axvline(self.X.mean(), color='k', linestyle='dashed', linewidth=2)
        ax.tick_params(axis='both', which='major', labelsize=15)
        ax.set_xlabel("X", size=20)
        ax.set_ylabel("P(X <= x)", size=20)
        plt.title("Histogram", size=20)
        ax.legend()
        plt.show()
    
    def __get_bins__(self, dx):
        mean = self.X.mean()
        std = self.X.std()
        a = mean - 3 * std
        b = mean + 3 * std
        n = round((b - a)/dx)
        xs = np.linspace(a, b, n)
        return xs

    def plot_pdf(self, dx):
        data_analysis = DataAnalysis(self.X)
        mean = self.X.mean()
        std = self.X.std()
        a = mean - 3 * std
        b = mean + 3 * std
        xs, fe = data_analysis.pdf_range(a, b, dx)
        fig, ax = plt.subplots(1,1)
        ax.plot(xs,fe,label='Fe')
        ax.plot(xs, st.norm.pdf(xs, loc=mean, scale=std), label='F')
        ax.axvline(self.X.mean(), color='k', linestyle='dashed', linewidth=2)
        ax.tick_params(axis='both', which='major', labelsize=15)
        ax.set_xlabel("X", size=20)
        ax.set_ylabel("P(X <= x)", size=20)
        plt.title("Histogram", size=20)
        ax.legend()
        plt.show()

    def plot_ci(self, alpha):
        ci = ConfidenceInterval(self.X, alpha)
        mean = ci.mean
        lower = ci.calculate_lower_bound()
        upper = ci.calculate_upper_bound()

        fig, ax = plt.subplots(1,1)
        ax.plot(1, mean, marker='o', markersize=10)
        ax.vlines(x=1, ymin=lower, ymax=upper, linewidth=2)
        ax.hlines(y=lower, xmin=1 - 0.1, xmax=1 + 0.1, linewidth=2)
        ax.hlines(y=upper, xmin=1 - 0.1, xmax=1 + 0.1, linewidth=2)
        ax.set_xticks([1])
        ax.set_xticklabels([""])
        ax.tick_params(axis='both', which='major', labelsize=15)

        ax.set_xlim(0,2)
        ax.set_ylabel("X", size=20)
        plt.title("Confidence Interval", size=20)
        plt.show()
        