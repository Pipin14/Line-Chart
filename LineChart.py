<<<<<<< HEAD
import re
from bokeh.plotting import figure, output_notebook, show
from datetime import datetime

with open('soal_chart_bokeh.txt', 'r') as file:
    lines = file.readlines()

timestamps = []
bitrates = []

def timestamp_to_datetime(timestamp):
    return datetime.utcfromtimestamp(timestamp)

for line in lines:
    match = re.search(r"\[\s*\d+\]\s+([\d\.]+)-([\d\.]+)\s+sec\s+.*\s+([\d\.]+)\s*Mbits/sec", line)
    if match:
        start_time = float(match.group(1))
        bitrate = float(match.group(3))
        
        speed_mbps = bitrate
        
        timestamps.append(timestamp_to_datetime(start_time))
        bitrates.append(speed_mbps)

p = figure(title="TESTING JARINGAN",
           x_axis_label='DATE TIME',
           y_axis_label='Speed (Mbps)',
           height=400, width=800, 
           x_axis_type="datetime")

p.title.text_font_style = "bold"
p.xaxis.axis_label_text_font_style = "bold"
p.yaxis.axis_label_text_font_style = "bold"

p.line(timestamps, bitrates, legend_label="Speed (Mbps)", line_width=1, color='blue')

show(p)
=======
import re
from bokeh.plotting import figure, output_notebook, show
from datetime import datetime

with open('soal_chart_bokeh.txt', 'r') as file:
    lines = file.readlines()

timestamps = []
bitrates = []

def timestamp_to_datetime(timestamp):
    return datetime.utcfromtimestamp(timestamp)

for line in lines:
    match = re.search(r"\[\s*\d+\]\s+([\d\.]+)-([\d\.]+)\s+sec\s+.*\s+([\d\.]+)\s*Mbits/sec", line)
    if match:
        start_time = float(match.group(1))
        bitrate = float(match.group(3))
        
        speed_mbps = bitrate
        
        timestamps.append(timestamp_to_datetime(start_time))
        bitrates.append(speed_mbps)

p = figure(title="TESTING JARINGAN",
           x_axis_label='DATE TIME',
           y_axis_label='Speed (Mbps)',
           height=400, width=800, 
           x_axis_type="datetime")

p.title.text_font_style = "bold"
p.xaxis.axis_label_text_font_style = "bold"
p.yaxis.axis_label_text_font_style = "bold"

p.line(timestamps, bitrates, legend_label="Speed (Mbps)", line_width=1, color='blue')

show(p)
>>>>>>> c58a048253244f4434ac65a288f15ac8b36a855a
