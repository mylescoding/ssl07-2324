import matplotlib.pyplot as plt
import datetime


values_fixedtime = 
values_sf_cen = 
values_sf_dec= 
values_ctm_cen=
values_ctm_dec=
# Generate time intervals from 6:00 AM to 10:00 AM in 15-minute intervals
start_time = datetime.datetime.strptime("06:15", "%H:%M")
time_intervals = [start_time + datetime.timedelta(minutes=15*i) for i in range(16)]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(time_intervals, values_fixedtime, marker='o', label='Fixed Time', linewidth = 3)
plt.plot(time_intervals, values_sf_cen, marker='v', label='SF Centralized')
plt.plot(time_intervals, values_sf_dec, marker='^', label='SF Decentralized')
plt.plot(time_intervals, values_ctm_cen, marker='>', label='CTM Centralized')
plt.plot(time_intervals, values_ctm_dec, marker='<', label='CTM Decentralized')

plt.title("Average Queue Times from 6 AM to 10 AM (15 minute-window)")
plt.xlabel("Time")
plt.ylabel("Average Queue Time (s)")
plt.xticks(time_intervals, [t.strftime("%H:%M") for t in time_intervals], rotation=45)


# Setting x-axis limits
end_time = start_time + datetime.timedelta(hours=4)
plt.xlim([start_time, end_time])
plt.legend()

plt.grid(True)
plt.tight_layout()
plt.show()
