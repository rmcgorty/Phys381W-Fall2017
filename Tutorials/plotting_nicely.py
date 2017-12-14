# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 11:48:36 2017

@author: rmcgorty
"""
import matplotlib
import pylab
import numpy as np

axis_color = 'k'

# Set some defaults for plotting to get nice output for publication
matplotlib.rcParams['lines.linewidth'] = 0.5
matplotlib.rcParams['lines.antialiased'] = False
matplotlib.rcParams['patch.linewidth'] = 0.5
matplotlib.rcParams['patch.antialiased'] = False
matplotlib.rcParams['font.family'] = 'sans-serif'
# figure out how to change font to Myriad before submission
matplotlib.rcParams['legend.fontsize'] = 8#12
matplotlib.rcParams['legend.handlelength'] = 1.5
matplotlib.rcParams['font.sans-serif'] = ['DejaVu Sans']
matplotlib.rcParams['font.size'] = 8#12#7
matplotlib.rcParams['axes.titlesize'] = 8#12 #7
matplotlib.rcParams['axes.labelsize'] = 8#12 #7
matplotlib.rcParams['axes.linewidth'] = 0.5
matplotlib.rcParams['xtick.labelsize'] = 8#10
matplotlib.rcParams['xtick.major.size'] = 3
matplotlib.rcParams['ytick.major.size'] = 3
matplotlib.rcParams['ytick.labelsize'] = 8#10
# with this parameter off, fonts will be editable in inkscape
matplotlib.rcParams['svg.fonttype'] = 'none'
matplotlib.rcParams['pdf.compression'] = 0
matplotlib.rcParams['pdf.fonttype'] = 42		# embed truetype fonts
matplotlib.rcParams['axes.edgecolor'] = axis_color
matplotlib.rcParams['figure.facecolor'] = 'w'
matplotlib.rcParams['xtick.color'] = axis_color
matplotlib.rcParams['ytick.color'] = axis_color

matplotlib.rcParams['figure.subplot.bottom'] = 0.15
matplotlib.rcParams['figure.subplot.left'] = 0.15

matplotlib.rcParams['savefig.dpi'] = 300
matplotlib.rcParams['mathtext.default'] = 'regular'

gray10 = '#191919'
gray20 = '#333333'
gray30 = '#4C4C4C'
gray40 = '#666666'
gray50 = '#7F7F7F'
warm_red = '#E64F2C'
blue_214 = '#7BAFDE' # Pantone DS 214-5
blue_645 = '#739ABC'    # Pantone 645
blue_653 = '#21578A'    # Pantone 653
green_556 = '#70A489'   # Pantone 556
violet = '#4B08A1'      # Pantone violet
reflex_blue = '#002395' # Pantone reflex blue
green_330 = '#005751'   # Pantone 330
yellow_117 = '#C79900'  # Pantone 116

golden_ratio = 1.618

def ticks_format(value, index):
    """
    get the value and returns the value as:
       integer: [0,99]
       1 digit float: [0.1, 0.99]
       n*10^m: otherwise
    To have all the number of the same size they are all returned as latex strings
    """
    exp = np.floor(np.log10(value))
    base = value/10**exp
    if exp == 0 or exp == 1:   
        return '${0:d}$'.format(int(value))
    if exp == -1:
        return '${0:.1f}$'.format(value)
    else:
        return '${0:d}\\times10^{{{1:d}}}$'.format(int(base), int(exp))

one_column = 3.25 #units of inches
two_columns = 5.75

marker_size = 7
marker_edge_width = 1

test_data_x = np.array([1,3,9,29,321,991,4092])
test_data_y = np.array([0.01, 0.1, 135, 1000, 10400, 20151, 24111])
test_data_yerr = test_data_y*0.1

fig, ax = pylab.subplots(figsize=(one_column, one_column/golden_ratio))
pylab.loglog(test_data_x, test_data_y, 'o', mfc=gray50, mec='k', ms=marker_size, mew=marker_edge_width) #mfc = marker face color; mec=marker edge color
xtick_positions, xtick_labels = pylab.xticks()
new_xtick_positions = np.array([0.1, 1, 5, 10, 25, 100, 400, 1000, 10000])
new_xtick_labels = ['0.1', '1.0', '5.0', '10', '25', '100', '400', '1000', '10000']
#ax.set_xticks()
pylab.xticks(new_xtick_positions, new_xtick_labels)

#These two lines remove top axis lines and tick marks
ax.spines['top'].set_visible(False)
ax.get_xaxis().tick_bottom()

#These two lines remove right axis lines and tick marks
ax.spines['right'].set_visible(False)
ax.get_yaxis().tick_left()

pylab.savefig("testing.svg", bbox_inches='tight')

'''''''''''''''''''''''
'''''''''''''''''''''''

fig, ax = pylab.subplots(figsize=(one_column, one_column/golden_ratio))
pylab.loglog(test_data_x, test_data_y, 'o', mfc=gray50, mec='k', ms=marker_size, mew=marker_edge_width) #mfc = marker face color; mec=marker edge color
sub_ticks_per_decade = [1.0, 2.0, 3.0, 6.0]
for axis in [ax.xaxis, ax.yaxis]:
        axis.set_minor_locator(matplotlib.ticker.LogLocator(subs=sub_ticks_per_decade))
        #axis.set_minor_formatter(matplotlib.ticker.FuncFormatter(ticks_format))
        axis.set_major_formatter(matplotlib.ticker.FuncFormatter(ticks_format))

'''''''''''''''''''''''
'''''''''''''''''''''''

fig, ax = pylab.subplots(figsize=(one_column, one_column/golden_ratio))
ax2_y = ax.twiny()
ax2_x = ax.twinx()
ax.plot(test_data_x, test_data_y, 'o', mfc=gray50, mec='k', ms=marker_size, mew=marker_edge_width) #mfc = marker face color; mec=marker edge color
ax.errorbar(test_data_x, test_data_y, yerr = test_data_yerr, fmt=None, ecolor='k', elinewidth=3, capthick=3, capsize=3)
ax2_y.plot(test_data_x, -0.2*test_data_y, 's', mfc=warm_red, ms=marker_size, mew=marker_edge_width)
