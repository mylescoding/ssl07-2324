import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates

# Define the green times for each phase
phase1_times = [120.00, 139.00, 76.00, 76.00, 76.00, 76.00, 76.00, 76.00, 143.00, 76.00, 131.00, 76.00, 76.00, 96.00, 112.00, 98.00, 76.00, 92.00, 115.00, 122.00, 92.00, 76.00, 76.00, 76.00, 76.00, 76.00, 76.00, 92.00, 76.00, 118.00, 76.00, 91.00, 76.00, 110.00, 121.00, 76.00, 76.00, 127.00, 105.00, 76.00, 94.00, 76.00, 109.00, 76.00, 104.00, 100.00, 76.00, 76.00, 76.00, 76.00]
phase2_times = [16.00, 66.00, 66.00, 66.00, 16.00, 66.00, 17.00, 66.00, 66.00, 66.00, 66.00, 66.00, 66.00, 66.00, 66.00, 66.00, 26.00, 66.00, 45.00, 66.00, 66.00, 66.00, 66.00, 66.00, 53.00, 66.00, 41.00, 16.00, 66.00, 66.00, 65.00, 66.00, 66.00, 17.00, 16.00, 66.00, 66.00, 66.00, 18.00, 21.00, 66.00, 66.00, 66.00, 66.00, 66.00, 53.00, 66.00, 24.00, 36.00, 55.00]
phase3_times = [16.00, 19.00, 38.00, 35.00, 18.00, 37.00, 66.00, 66.00, 66.00, 66.00, 66.00, 66.00, 22.00, 35.00, 66.00, 66.00, 58.00, 29.00, 66.00, 66.00, 66.00, 66.00, 66.00, 52.00, 44.00, 66.00, 41.00, 66.00, 35.00, 66.00, 66.00, 63.00, 39.00, 21.00, 36.00, 66.00, 65.00, 29.00, 66.00, 66.00, 66.00, 34.00, 66.00, 54.00, 52.00, 50.00, 33.00, 16.00, 16.00, 61.00]
phase4_times = [81.00, 19.00, 81.00, 32.00, 81.00, 20.00, 80.00, 48.00, 81.00, 81.00, 81.00, 81.00, 81.00, 81.00, 81.00, 43.00, 60.00, 81.00, 32.00, 81.00, 35.00, 19.00, 56.00, 81.00, 81.00, 16.00, 60.00, 54.00, 68.00, 53.00, 81.00, 81.00, 52.00, 31.00, 81.00, 25.00, 60.00, 64.00, 78.00, 79.00, 81.00, 59.00, 81.00, 60.00, 65.00, 81.00, 68.00, 30.00, 17.00, 20.00]
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
plt.plot(time_intervals, phase2_times, marker='s', label='Phase 2', color = 'yellow')
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