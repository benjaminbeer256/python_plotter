import numpy as np
import re
import xml.dom.minidom as dom
import argparse

class Composite:
    pass

class XScale:
    def __init__(self, plot):
        self.domain = [plot.xmin, plot.xmax]
        self.range = [plot.margins.get('left'), plot.width - plot.margins.get('right')]
    
    def get(self, value):
        return (self.range[1] / self.range[0]) * value
    
    def inverse(self, value):
        return (self.domain[1] / self.domain[0]) * value
    
class Plot:
    def __init__(self, title="Composite plot", xmin=-500, xmax=500, ymin=-1, ymax=1, xlabel="Position (bp)", ylabel="Occupancy (AU)", 
                 opacity=1, smoothing=7, bp_shift=0, combined=False, color_trace=False, show_legend=True):
        self.title = title
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.width = 460
        self.height = 300
        self.margins = {'top': 30, 'right': 170, 'bottom': 35, 'left': 40}
        self.opacity = opacity
        self.smoothing = smoothing
        self.bp_shift = bp_shift
        self.combined = combined
        self.color_trace = color_trace
        self.show_legend = show_legend