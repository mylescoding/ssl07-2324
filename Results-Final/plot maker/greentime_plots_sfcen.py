import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates

# Define the green times for each phase
phase1_times = [float(x) for x in ['120.00', '145.00', '146.00', '144.00', '132.00', '124.00', '138.00', '149.00', '119.00', '90.00', '114.00', '158.00', '99.00', '140.00', '98.00', '151.00', '112.00', '94.00', '105.00', '151.00', '132.00', '126.00', '145.00', '135.00', '131.00', '143.00', '141.00', '114.00', '121.00', '142.00', '148.00', '156.00', '111.00', '140.00', '109.00', '87.00', '118.00', '157.00', '122.00', '159.00', '118.00', '134.00', '116.00', '130.00', '100.00', '100.00', '133.00', '157.00', '89.00', '129.00', '124.00', '134.00', '96.00', '136.00', '26.00', '26.00', '26.00', '26.00', '26.00']]
phase2_times = [float(x) for x in ['26.00', '61.00', '65.00', '52.00', '38.00', '64.00', '49.00', '36.00', '34.00', '65.00', '62.00', '52.00', '36.00', '54.00', '47.00', '39.00', '55.00', '60.00', '31.00', '54.00', '41.00', '34.00', '50.00', '34.00', '55.00', '35.00', '60.00', '39.00', '55.00', '34.00', '44.00', '41.00', '42.00', '41.00', '44.00', '36.00', '40.00', '30.00', '52.00', '40.00', '35.00', '44.00', '39.00', '51.00', '42.00', '33.00', '38.00', '52.00', '38.00', '34.00', '35.00', '62.00', '54.00', '36.00', '71.00', '71.00', '71.00', '71.00', '71.00']]
phase3_times = [float(x) for x in ['26.00', '47.00', '41.00', '26.00', '33.00', '31.00', '38.00', '38.00', '26.00', '26.00', '42.00', '53.00', '26.00', '40.00', '26.00', '60.00', '26.00', '42.00', '46.00', '44.00', '47.00', '26.00', '37.00', '35.00', '32.00', '34.00', '54.00', '44.00', '29.00', '30.00', '32.00', '51.00', '52.00', '39.00', '52.00', '33.00', '53.00', '32.00', '47.00', '38.00', '54.00', '52.00', '50.00', '26.00', '26.00', '26.00', '26.00', '53.00', '26.00', '26.00', '26.00', '31.00', '44.00', '26.00', '26.00', '26.00', '26.00', '26.00', '26.00']]
phase4_times = [float(x) for x in ['26.00', '41.00', '20.00', '26.00', '26.00', '16.00', '34.00', '24.00', '22.00', '32.00', '51.00', '51.00', '26.00', '31.00', '20.00', '18.00', '29.00', '37.00', '58.00', '18.00', '25.00', '26.00', '43.00', '26.00', '37.00', '42.00', '21.00', '24.00', '41.00', '48.00', '39.00', '22.00', '21.00', '53.00', '55.00', '59.00', '49.00', '26.00', '40.00', '26.00', '19.00', '39.00', '26.00', '26.00', '26.00', '26.00', '26.00', '29.00', '26.00', '26.00', '26.00', '42.00', '59.00', '26.00', '26.00', '26.00', '26.00', '26.00', '26.00']]

print(len(phase1_times))
print(len(phase2_times))
print(len(phase3_times))
print(len(phase4_times))

# Generate time intervals from 6:00 AM to 10:00 AM, distributed over 52 points
start_time = datetime.datetime.strptime("06:00", "%H:%M")
time_intervals = [start_time + datetime.timedelta(minutes=4.8 * i) for i in range(len(phase1_times))]

# Plotting
plt.figure(figsize=(12, 5))
plt.plot(time_intervals, phase1_times, marker='o', label='Phase 1', color = 'green')
plt.plot(time_intervals, phase2_times, marker='s', label='Phase 2', color = 'goldenrod')
plt.plot(time_intervals, phase3_times, marker='^', label='Phase 3', color = 'red')
plt.plot(time_intervals, phase4_times, marker='d', label='Phase 4', color = 'blue')
plt.title("SF Centralized - Phase Green Times from 6 AM to 10 AM")
plt.xlabel("Time")
plt.ylabel("Green Time (s)")

# Setting x-axis ticks to 15-minute intervals
minutes = mdates.MinuteLocator(interval=30)
time_format = mdates.DateFormatter('%H:%M')
plt.gca().xaxis.set_major_locator(minutes)
plt.gca().xaxis.set_major_formatter(time_format)

# Setting x-axis limits
end_time = start_time + datetime.timedelta(hours=4)
plt.xlim([start_time, end_time])

plt.grid(True)

# Add the legend
plt.legend()

plt.tight_layout()
plt.show()