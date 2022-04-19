import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # Read data from file
    df = pd.read_csv("./epa-sea-level.csv")

    # Create scatter plot
    colors = np.random.rand(len(df))
    fig = plt.scatter(x=df["Year"], y=df["CSIRO Adjusted Sea Level"], c=colors)

    # Create first line of best fit
    result = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    new_xValues = pd.Series(range(df["Year"].min(), 2051))
    plt.plot(new_xValues, result.slope * new_xValues + result.intercept, "r")

    # Create second line of best fit
    new_df = df[df["Year"] >= 2000]
    x2 = new_df["Year"]
    y2 = new_df["CSIRO Adjusted Sea Level"]
    new_x2Values = pd.Series(range(x2.min(), 2051))
    result2 = linregress(x2, y2)
    plt.plot(new_x2Values, result2.slope * new_x2Values + result2.intercept, "g")

    # Add labels and title
    ax = plt.gca()
    ax.set(xlabel="Year", ylabel="Sea Level (inches)", title="Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("sea_level_plot.png")
    return plt.gca()
