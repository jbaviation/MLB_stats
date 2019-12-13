import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import mplcursors as mpl

import pdb


# Plots
#---------------------------------------------------------
# Plot1
data = pd.read_csv('MLB_Team_Batting.csv')   # Read csv into dataframe

fig1, ax1 = plt.subplots(figsize=(18,9))
cols_to_plot = [['BA',1],['HR',1],['SO',1],['BB',1],['R',0.5],['OBP',0.5]]

# Plot each column in cols_to_plot with [0] being the column name and [1] being the weight
for col in cols_to_plot:
   ax1.plot(data['Year'],data[col[0]]/data[col[0]].max(), label=col[0], linewidth=col[1])

ax1.set_title('History of MLB Batting (Normalized to Max)')    # plot title
ax1.set_xlabel('Year')
ax1.set_xlim(data.Year.min(), data.Year.max())  # set axis limits to first and last years
ax1.axes.get_yaxis().set_visible(False)   # remove yaxis label

# Create legend and move off of the plot
ax1.legend(loc=(0.9,0))
ax1.grid(b=True, which='major', linestyle='-')              # grid for major ticks
ax1.minorticks_on()                                         # turn on minor ticks
ax1.grid(b=True, which='minor', linestyle='-', alpha=0.2)   # grid for minor ticks



# Plot2
data = pd.read_csv('MLB_Team_Pitching.csv')

fig2, ax2 = plt.subplots(figsize=(18,9))
cols_to_plot = [['WHIP',1],['ERA',1],['SV',1],['CG',0.5],['SHO',0.5]]

# Plot each column in cols_to_plot with [0] being the column name and [1] being the weight
for col in cols_to_plot:
   ax2.plot(data['Year'],data[col[0]]/data[col[0]].max(), label=col[0], linewidth=col[1])

ax2.set_title('History of MLB Pitching (Normalized to Max)')    # plot title
ax2.set_xlabel('Year')
ax2.set_xlim(data.Year.min(), data.Year.max())  # set axis limits to first and last years
ax2.axes.get_yaxis().set_visible(False)   # remove yaxis label

# Create legend and move off of the plot
ax2.legend(loc=(0.9,0))
ax2.grid(b=True, which='major', linestyle='-')              # grid for major ticks
ax2.minorticks_on()                                         # turn on minor ticks
ax2.grid(b=True, which='minor', linestyle='-', alpha=0.2)   # grid for minor ticks

# Connect to hover capability and show only variable name
mpl.cursor(hover=True).connect('add', lambda sel: sel.annotation.set_text(sel.artist.get_label()))

fig1.savefig('mlb_history_hitting.png')
fig2.savefig('mlb_history_pitching.png')
plt.show()
