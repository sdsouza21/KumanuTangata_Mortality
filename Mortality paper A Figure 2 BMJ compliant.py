# -*- coding: utf-8 -*-
"""
Created on Wed May 21 07:29:00 2025

@author: quarriek
"""

# -*- coding: utf-8 -*-
"""
BMJ-style forest plot of YLL differences between players and the general population with values displayed to the right of the error bars
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image
import io

# BMJ-style settings
plt.style.use('bmh')
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.serif': ['Calibri'],
    'font.size': 12,
    'axes.titlesize': 12,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 11,
    'legend.fontsize': 9,
    'figure.dpi': 600,
    'figure.figsize': (7, 5),
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.linewidth': 0.5,
    'grid.alpha': 0.3,
    'axes.facecolor': 'white',
    'figure.facecolor': 'white'
})

# Data
primary_data = {
    'Cause_of_death': ['Neurodegenerative', 'Cardiovascular', 'Cancer',
                       'Suicide', 'Alcohol/SUD-related', 'Metabolic',
                       'Respiratory', 'Digestive', 'Other or unknown'],
    'YLL_diff': [-38, 78, 113, 42, 25, 91, 161, 4, 210],
    'YLL_diff_lower_cl': [-57, 19, 55, 29, 19, 77, 144, -12, 165],
    'YLL_diff_UCL': [-19, 123, 163, 55, 32, 105, 178, 26, 246]
}

df = pd.DataFrame(primary_data)

# Calculate error bars
lower_error = df['YLL_diff'] - df['YLL_diff_lower_cl']
upper_error = df['YLL_diff_UCL'] - df['YLL_diff']
errors = [lower_error, upper_error]

# Flip main values (for display orientation)
df['YLL_diff'] = df['YLL_diff'] * -1

# Plot
fig, ax = plt.subplots(figsize=(7.5, 5))  # Slightly wider to accommodate text
fig.subplots_adjust(right=0.75)

# Error bars
ax.errorbar(df['YLL_diff'],
            np.arange(len(df)),
            xerr=errors,
            fmt='o',
            color='black',
            ecolor='black',
            capsize=3,
            capthick=1,
            elinewidth=1,
            markersize=6)

# Reference line
ax.axvline(x=0, color='gray', linestyle='--', linewidth=0.8, alpha=0.7)

# Configure axes
ax.set_yticks(np.arange(len(df)))
ax.set_yticklabels(df['Cause_of_death'], fontsize=11)
ax.set_xlabel('Difference in years of life lost per 1000 individuals', labelpad=12)
ax.set_xlim(-300, 300)
ax.invert_yaxis()
ax.grid(True, axis='y', linestyle=':', linewidth=0.7, alpha=0.3)
ax.grid(False, axis='x')

# Add YLL annotations to right
for i, (yll, low, high) in enumerate(zip(df['YLL_diff']*-1, df['YLL_diff_lower_cl'], df['YLL_diff_UCL'])):
    label = f"{-yll:.0f} ({-high:.0f} to {-low:.0f})"
    ax.text(300, i, label, va='center', ha='right', fontsize=9)

# Annotations for direction
transform = ax.get_xaxis_transform()
ax.annotate('Higher premature mortality for players',
            xy=(0, -0.05), xytext=(30, -1),
            textcoords='data', transform=transform,
            ha='left', va='center', fontsize=9,
            clip_on=False)

ax.annotate('Lower premature mortality for players',
            xy=(0, -0.05), xytext=(-20, -1),
            textcoords='data', transform=transform,
            ha='right', va='center', fontsize=9,
            clip_on=False)

plt.tight_layout()

# Save as TIFF
buf = io.BytesIO()
plt.savefig(buf, format='tiff', dpi=600, bbox_inches='tight')
buf.seek(0)
img = Image.open(buf)
final_tiff = "Mortality_paper_figure_2.tiff"
img.save(final_tiff, compression="tiff_lzw")
buf.close()

print(f"TIFF saved as: {final_tiff}")
plt.show()
plt.close()