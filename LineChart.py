import re
from bokeh.plotting import figure, show
from datetime import datetime, timedelta
from collections import defaultdict

with open('soal_chart_bokeh.txt', 'r') as file:
    lines = file.readlines()

timestamps = []
bitrates = []

def parse_datetime(timestamp_str):
    try:
        return datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
    except ValueError as e:
        print(f"Error parsing timestamp: {timestamp_str} - {e}")
        return None

current_timestamp = None

for line in lines:
    line = re.sub(r'#.*', '', line)  # Menghapus komentar setelah tanda #
    
    timestamp_match = re.match(r'Timestamp: (.*)', line)
    if timestamp_match:
        current_timestamp = parse_datetime(timestamp_match.group(1))

    bitrate_match = re.search(r"\[\s*\d+\]\s+([\d\.]+)-([\d\.]+)\s+sec\s+.*\s+([\d\.]+)\s*Mbits/sec", line)
    if bitrate_match and current_timestamp:
        interval_start = float(bitrate_match.group(1))
        bitrate = float(bitrate_match.group(3))

        timestamp_with_offset = current_timestamp + timedelta(seconds=interval_start)

        rounded_timestamp = timestamp_with_offset.replace(second=0, microsecond=0)

        print(f"Found timestamp: {rounded_timestamp}, Interval Start: {interval_start}, Bitrate: {bitrate}")

        timestamps.append(rounded_timestamp)
        bitrates.append(bitrate)

hour_bitrates = defaultdict(list)
for ts, bitrate in zip(timestamps, bitrates):
    hour_key = ts.replace(minute=0, second=0, microsecond=0)
    hour_bitrates[hour_key].append(bitrate)

avg_bitrates = []
avg_hours = []

start_time = min(hour_bitrates.keys())
end_time = max(hour_bitrates.keys())

current_time = start_time
while current_time <= end_time:
    if current_time in hour_bitrates:
        avg_bitrates.append(sum(hour_bitrates[current_time]) / len(hour_bitrates[current_time]))
    else:
        avg_bitrates.append(0)
    
    hour_diff = (current_time - start_time).total_seconds() / 3600
    avg_hours.append(hour_diff)
    
    current_time += timedelta(hours=1)

print("Rentang Waktu yang Diambil (dalam jam):")
for hour, bitrate in zip(avg_hours, avg_bitrates):
    print(f"{hour} jam: {bitrate} Mbps")

p = figure(title="Testing Jaringan",
           x_axis_label='Time (hours)',
           y_axis_label='Speed (Mbps)',
           height=400, width=800)

p.line(avg_hours, avg_bitrates, legend_label="Speed (Mbps)", line_width=2, color='blue')

show(p)
