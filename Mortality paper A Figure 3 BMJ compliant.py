# -*- coding: utf-8 -*-
"""
BMJ-formatted visualization with corrected x-axis label handling
"""

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import io

# BMJ-style settings
mpl.rcParams['font.family'] = 'Calibri'
mpl.rcParams['font.size'] = 12
mpl.rcParams["axes.spines.right"] = False
mpl.rcParams["axes.spines.top"] = False
mpl.rcParams["axes.linewidth"] = 0.5
mpl.rcParams['xtick.major.pad'] = 2
mpl.rcParams['ytick.major.pad'] = 2

# Load data
df1 = pd.read_excel(r'C:\Users\quarriek\OneDrive - New Zealand Rugby\Kumanu Tangata\Mortality paper\HRs stratified by age 1.xlsx')
df = pd.DataFrame(df1.to_dict('list'))

# Create subplots with adjusted bottom margin
fig, axes = plt.subplots(nrows=5, ncols=2, figsize=(7.08, 9.84),
                        gridspec_kw={'bottom': 0.07, 'top': 0.95},  # Increased bottom margin
                        sharex=True)
axes = axes.flatten()

# Plotting parameters
plot_params = {
    'capsize': 2,
    'linewidth': 0.5,
    'markersize': 4,
    'markeredgewidth': 0.5
}

for i, (ax, condition) in enumerate(zip(axes, df['Condition'].unique())):
    data = df[df['Condition'] == condition]
    
    # Plot with error bars
    ax.errorbar(
        data['Age at death'], 
        data['Hazard ratio'], 
        yerr=[data['Hazard ratio'] - data['Lower 95% CL'], 
              data['Upper 95% CL'] - data['Hazard ratio']],
        fmt='o', 
        color='black',
        ecolor='black',
        markerfacecolor='black',
        **plot_params
    )
    
    # Reference lines
    ax.axhline(1, color='grey', linestyle='--', linewidth=0.5, alpha=0.7)
    ax.axhline(0.5, color='grey', linestyle=':', linewidth=0.3, alpha=0.4)
    ax.axhline(2.0, color='grey', linestyle=':', linewidth=0.3, alpha=0.4)
    
    # Axis formatting
    ax.set_yscale('log')
    ax.set_ylim(0.1, 5)
    ax.set_yticks([0.1, 0.5, 1.0, 2.0, 5])
    ax.set_yticklabels(['0.1', '0.5', '1.0', '2.0', '5.0'], fontsize=9)
    # Minor ticks
    ax.yaxis.set_minor_locator(mpl.ticker.LogLocator(subs=np.arange(0.1, 1, 0.1)))
    ax.tick_params(axis='both', which='major', width=0.5, length=3)
    ax.tick_params(axis='both', which='minor', width=0.2, length=1)
    
    # Only show x-axis labels on bottom row
    if i >= len(axes) - 2:  # Last row (for 5x2 grid)
        ax.set_xticks(data['Age at death'])
        ax.set_xticklabels(
            data['Age at death'],
            fontsize=9,
            rotation=45,
            rotation_mode='anchor',
            ha='right'
        )
        for label in ax.get_xticklabels():
            label.set_position((-0.2, -0.03))
    else:
        ax.set_xticks([])
        ax.set_xlabel('')
    
    # Title
    ax.text(0.5, 1.02, condition, transform=ax.transAxes,
            ha='center', va='bottom', fontsize=10)

# Y-axis label
label_ax = fig.add_axes([0.04, 0.4, 0.01, 0.2])
label_ax.axis('off')
label_ax.text(-2.5, 0.55, 'Hazard ratio', ha='center', va='center', fontsize=10)
label_ax.text(-2.5, 0.45, '(95% CI)', ha='center', va='center', fontsize=10)

# X-axis label
fig.text(0.5, 0.002, 'Age at death', ha='center', fontsize=10)  # Lowered position

# Remove unused axes
for ax in axes[len(df['Condition'].unique()):]:
    fig.delaxes(ax)

# Adjust layout
plt.tight_layout(rect=[0.08, 0.2, 0.98, 0.98])

# Save with padding
buffer = io.BytesIO()
plt.savefig(buffer, format='tiff', dpi=600,
           bbox_extra_artists=[label_ax],
           bbox_inches='tight',
           pad_inches=0.5)
buffer.seek(0)
img = Image.open(buffer)
img.save('Mortality_paper_figure_3.tiff', compression='tiff_lzw')
buffer.close()
plt.show()

plt.close()