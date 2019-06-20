import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import mplcursors as mpl


# Plots
#---------------------------------------------------------
# Plot1
data = pd.read_csv('MLB_Team_Batting.csv')   # Read csv into dataframe
#data.Year = pd.to_datetime(data.Year, format='%Y')  # Convert year into datetime

fig1, ax1 = plt.subplots(figsize=(18,9))
ax1.plot(data.Year,data.BA/np.max(data.BA))
ax1.plot(data.Year,data.HR/np.max(data.HR))
ax1.plot(data.Year,data.SO/np.max(data.SO))
ax1.plot(data.Year,data.BB/np.max(data.BB))
ax1.plot(data.Year,data.R/np.max(data.R))
ax1.plot(data.Year,data.H/np.max(data.H),linewidth=0.5)
ax1.plot(data.Year,data.OBP/np.max(data.OBP),linewidth=0.5)
ax1.plot(data.Year,data.SLG/np.max(data.SLG),linewidth=0.5)

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
#data.Year = pd.to_datetime(data.Year, format='%Y')

fig2, ax2 = plt.subplots(figsize=(18,9))
ax2.plot(data.Year,data.CG/np.max(data.CG))
ax2.plot(data.Year,data.SHO/np.max(data.SHO))
ax2.plot(data.Year,data.SV/np.max(data.SV))
ax2.plot(data.Year,data.WP/np.max(data.WP))
ax2.plot(data.Year,data.WHIP/np.max(data.WHIP))

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
#plt.show()
