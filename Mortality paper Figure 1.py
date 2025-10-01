

# -*- coding: utf-8 -*-
"""
Created on Thu May 15 20:27:23 2025

@author: quarriek
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import rcParams
from PIL import Image
import io

# Set BMJ-style font and sizes (Arial or Helvetica preferred)
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Calibri']  # BMJ prefers sans-serif for tables and charts
rcParams['font.size'] = 9  
rcParams['axes.labelsize'] = 9  # Slightly larger for axis labels
rcParams['axes.titlesize'] = 9  # If using title
rcParams['xtick.labelsize'] = 8  # Equal size for x and y ticks
rcParams['ytick.labelsize'] = 8  # Equal size for x and y ticks
rcParams['legend.fontsize'] = 8
rcParams['figure.dpi'] = 600
rcParams['savefig.dpi'] = 600
rcParams['lines.linewidth'] = 1
rcParams['axes.linewidth'] = 0.7
rcParams['xtick.major.width'] = 0.7
rcParams['ytick.major.width'] = 0.7
rcParams['xtick.major.size'] = 3  # BMJ prefers shorter ticks
rcParams['ytick.major.size'] = 3

# Load your data
df1 = pd.read_excel(r'C:\Users\quarriek\OneDrive - New Zealand Rugby\Kumanu Tangata\Mortality paper\Primary YLL versus Cause of death contour plot data.xlsx')
data = df1.to_dict('list')

# Create figure (consider BMJ's column width requirements)
fig, ax = plt.subplots(figsize=(6.85, 6.85))  # Double column width, square

# Contour background
deaths_grid, years_lost_grid = np.meshgrid(np.linspace(0, 105, 300), np.linspace(0, 40, 300))
product_grid = deaths_grid * years_lost_grid

# Use BMJ-friendly colors
ax.contourf(deaths_grid, years_lost_grid, product_grid,
            levels=[-1, 151.9, 457.7, 10000],
            colors=['#e0f3db', '#fee8c8', '#fdbb84'],
            alpha=0.4)

ax.contour(deaths_grid, years_lost_grid, product_grid,
           levels=[151.9, 457.7],
           colors=['#238b45', '#d94701'],
           linestyles='dashed', alpha=0.7, linewidths=0.7)

# Plot data points
ax.errorbar(data['Deaths per 1000 players'], data['YLL Players'],
            xerr=[np.array(data['Deaths per 1000 players']) - np.array(data['Deaths per 1000 players LCL']),
                  np.array(data['Deaths per 1000 players UCL']) - np.array(data['Deaths per 1000 players'])],
            yerr=[np.array(data['YLL Players']) - np.array(data['YLL Players LCL']),
                  np.array(data['YLL Players UCL']) - np.array(data['YLL Players'])],
            fmt='o', color='black', label='Rugby Players', 
            markersize=5, capsize=3, capthick=0.7, elinewidth=0.7,
            markerfacecolor='black', markeredgewidth=0.5)

ax.errorbar(data['Deaths per 1000 people (General population)'], data['YLL General Pop'],
            xerr=[np.array(data['Deaths per 1000 people (General population)']) - np.array(data['Deaths per 1000 people (General population) LCL']),
                  np.array(data['Deaths per 1000 people (General population) UCL']) - np.array(data['Deaths per 1000 people (General population)'])],
            yerr=[np.array(data['YLL General Pop']) - np.array(data['YLL LCL General Pop']),
                  np.array(data['YLL UCL General Pop']) - np.array(data['YLL General Pop'])],
            fmt='s', color='#0570b0', label='General Population', 
            markersize=5, capsize=3, capthick=0.7, elinewidth=0.7,
            markerfacecolor='#0570b0', markeredgewidth=0.5)


# Axis labels with 'per death' added below y-axis label
ax.set_xlabel('Deaths per 1000 individuals', fontsize=11)
ax.set_ylabel('Years of life lost\n per death\n (mean)', rotation=0, labelpad=50, fontsize=11)
ax.yaxis.set_label_coords(-0.15, 0.45)

# Add annotations and arrows for each point
for i in range(len(data['Primary cause of death'])):
    if pd.isna(data['Primary cause of death'][i]):
        continue

    cause = data['Primary cause of death'][i].strip()
    
    if cause == "NDD":
        cause = "Neurodegenerative"
    elif cause == "CVD":
        cause = "Cardiovascular"
    
    # Position adjustments (same as before)
    label_position = (data['Deaths per 1000 people (General population)'][i] + 25,
                      data['YLL General Pop'][i] - 1)

    if cause == "Suicide":
        label_position = (data['Deaths per 1000 people (General population)'][i] + 15,
                          data['YLL General Pop'][i] - 1)
    elif cause == "Digestive":
        label_position = (data['Deaths per 1000 people (General population)'][i] + 9,
                          data['YLL General Pop'][i] - 0.5)
    elif cause == "Respiratory":
        label_position = (data['Deaths per 1000 people (General population)'][i] + 2,
                          data['YLL General Pop'][i] - 2)
    elif cause == "Metabolic":
        label_position = (data['Deaths per 1000 people (General population)'][i] + 14,
                          data['YLL General Pop'][i] + 1.5)
    elif cause == "Cardiovascular":
        label_position = (data['Deaths per 1000 people (General population)'][i] - 8,
                          data['YLL General Pop'][i] + 2)
    elif cause == "Cancer":
        label_position = (data['Deaths per 1000 people (General population)'][i] - 8,
                          data['YLL General Pop'][i] + 2)
    elif cause == "Neurodegenerative":
        label_position = (data['Deaths per 1000 people (General population)'][i] + 12,
                          data['YLL General Pop'][i] + 1)
    elif cause == "Other or unidentified":
        label_position = (data['Deaths per 1000 people (General population)'][i] + 10,
                          data['YLL General Pop'][i] + 2)

    ha = 'center' if cause in ['Cardiovascular', 'Cancer'] else 'left'
    va = 'bottom' if cause in ['Cardiovascular', 'Cancer'] else 'center'

    ax.text(label_position[0], label_position[1], cause, 
            fontsize=8, ha=ha, va=va, fontfamily='Calibri')

    ax.annotate(' ', xy=(data['Deaths per 1000 players'][i], data['YLL Players'][i]),
                xytext=label_position,
                arrowprops=dict(arrowstyle='->', lw=0.5, color='black', 
                               mutation_scale=8, shrinkA=0.2, shrinkB=3, alpha=0.7))

    ax.annotate(' ', xy=(data['Deaths per 1000 people (General population)'][i], data['YLL General Pop'][i]),
                xytext=label_position,
                arrowprops=dict(arrowstyle='->', lw=0.5, color='#0570b0', 
                               mutation_scale=8, shrinkA=0.2, shrinkB=3, alpha=0.7))

# Legend
ax.legend(loc='upper right', frameon=False, handlelength=1.5)

# Clean up axes
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlim(0, 105)
ax.set_ylim(0, 40)

# Add minor ticks
ax.xaxis.set_minor_locator(plt.MultipleLocator(10))
ax.yaxis.set_minor_locator(plt.MultipleLocator(5))

# Maintain aspect ratio
ax.set_aspect(2.625, adjustable='box')
plt.tight_layout(pad=1.5)

# Save in required formats
output_path = "Mortality paper figure 1.tiff"
plt.savefig(output_path, format='tiff', dpi=600, pil_kwargs={'compression': 'tiff_lzw'})
plt.savefig(output_path.replace('.tiff', '.pdf'), format='pdf')
plt.show()
plt.close()