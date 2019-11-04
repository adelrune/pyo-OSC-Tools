from pyo_osc_tools import OSCRecord
from pyo import *

"""This example will record an osc stream"""

s = Server().boot()
folder = input("recording name ? ")
recorder = OSCRecord(folder)
recorder.start()
s.start()
s.gui(locals)
