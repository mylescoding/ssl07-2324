import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates

# Define the green times for each phase
phase1_times = [float(x) for x in ['120.00', '81.00', '81.00', '81.00', '16.00', '81.00', '81.00', '81.00', '81.00', '109.00', '81.00', '16.00', '103.00', '81.00', '81.00', '81.00', '16.00', '81.00', '81.00', '81.00', '81.00', '81.00', '81.00', '99.00', '81.00', '81.00', '81.00', '99.00', '121.00', '81.00', '81.00', '101.00', '81.00', '127.00', '81.00', '97.00', '16.00', '81.00', '81.00', '130.00', '98.00', '16.00', '131.00', '81.00', '81.00', '81.00', '101.00', '16.00', '81.00', '81.00', '81.00', '81.00', '81.00', '133.00', '81.00', '106.00', '81.00', '110.00', '81.00', '81.00', '45.00']]
phase2_times = [float(x) for x in ['16.00', '66.00', '66.00', '66.00', '16.00', '39.00', '25.00', '66.00', '16.00', '41.00', '40.00', '16.00', '66.00', '66.00', '66.00', '41.00', '16.00', '57.00', '66.00', '54.00', '63.00', '43.00', '66.00', '66.00', '66.00', '66.00', '66.00', '55.00', '57.00', '58.00', '66.00', '66.00', '66.00', '51.00', '66.00', '40.00', '16.00', '66.00', '66.00', '66.00', '18.00', '24.00', '66.00', '66.00', '66.00', '66.00', '66.00', '16.00', '53.00', '66.00', '20.00', '66.00', '66.00', '66.00', '16.00', '35.00', '40.00', '66.00', '66.00', '37.00', '16.00']]
phase3_times = [float(x) for x in ['16.00', '16.00', '16.00', '16.00', '16.00', '16.00', '16.00', '16.00', '16.00', '16.00', '16.00', '16.00', '16.00', '16.00', '16.00', '16.00', '16.00', '16.00', '16.00', '16.00', '16.00', '16.00', '16.00', '16.00', '16.00', '16.00', '16.00', '16.00', '16.00', '16.00', '16.00', '66.00', '16.00', '16.00', '16.00', '16.00', '16.00', '16.00', '16.00', '66.00', '16.00', '16.00', '29.00', '16.00', '16.00', '16.00', '16.00', '16.00', '16.00', '16.00', '16.00', '16.00', '16.00', '16.00', '16.00', '16.00', '16.00', '16.00', '16.00', '16.00', '16.00']]
phase4_times = [float(x) for x in ['81.00', '51.00', '81.00', '41.00', '81.00', '81.00', '63.00', '16.00', '23.00', '56.00', '74.00', '81.00', '57.00', '63.00', '81.00', '64.00', '81.00', '81.00', '55.00', '40.00', '51.00', '26.00', '81.00', '42.00', '81.00', '81.00', '22.00', '78.00', '71.00', '81.00', '21.00', '81.00', '33.00', '81.00', '44.00', '55.00', '81.00', '70.00', '38.00', '81.00', '81.00', '53.00', '81.00', '81.00', '81.00', '64.00', '46.00', '81.00', '81.00', '48.00', '44.00', '81.00', '61.00', '32.00', '81.00', '64.00', '78.00', '81.00', '81.00', '16.00', '16.00']]

print(len(phase1_times))
print(len(phase2_times))
print(len(phase3_times))
print(len(phase4_times))

# Generate time intervals from 6:00 AM to 10:00 AM, distributed over 52 points
start_time = datetime.datetime.strptime("06:00", "%H:%M")
time_intervals = [start_time + datetime.timedelta(minutes=4.7 * i) for i in range(len(phase1_times))]

# Plotting
plt.figure(figsize=(12, 5))
plt.plot(time_intervals, phase1_times, marker='o', label='Phase 1', color = 'green')
plt.plot(time_intervals, phase2_times, marker='s', label='Phase 2', color = 'yellow')
plt.plot(time_intervals, phase3_times, marker='^', label='Phase 3', color = 'red')
plt.plot(time_intervals, phase4_times, marker='d', label='Phase 4', color = 'blue')
plt.title("SF Decentralized - Phase Green Times from 6 AM to 10 AM (Katipunan-B. Gonzales-Thornton Drive intersection)")
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
plt.ylim([15,150])

plt.grid(True)

# Add the legend
plt.legend()

plt.tight_layout()
plt.show()