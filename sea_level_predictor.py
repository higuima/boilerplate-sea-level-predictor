import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('freeCodeCamp/boilerplate-sea-level-predictor/epa-sea-level.csv')
    y = df['CSIRO Adjusted Sea Level']
    x = df['Year']

    # Create scatter plot
    plt.scatter(x=x,y=y, label='sea level')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(x=x,y=y)
    range_2050 = pd.Series([int(i) for i in range(1880, 2051)])
    plt.plot(range_2050, intercept + slope*range_2050, 'r', label='fisrt line')

    # Create second line of best fit
    most_recent_year = df[df['Year']>=2000]
    slope_2, intercept_2, r_value, p_value, std_err = linregress(x=most_recent_year['Year'],y=most_recent_year['CSIRO Adjusted Sea Level'])
    range_2000_2050 = pd.Series([int(i) for i in range(2000, 2051)])
    # most_recent_year.append(range_2000_2050, ignore_index=True)
    plt.plot(range_2000_2050, intercept_2 + slope_2*range_2000_2050, 'g', label='second line')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()