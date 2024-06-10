import matplotlib.pyplot as plt
import datetime


values_fixedtime = [13052.0, 13188.0, 15436.0, 13328.0, 15188.0, 13076.0, 15172.0, 13328.0, 18376.0, 17124.0, 18824.0, 17424.0, 18068.0, 17136.0, 17652.0, 17384.0]

values_sf_cen = [12652.0, 14040.0, 14808.0, 14352.0, 13932.0, 13760.0, 15124.0, 14244.0, 15328.0, 20288.0, 16972.0, 17284.0, 18728.0, 18164.0, 16036.0, 17708.0]

values_sf_dec= [12588.0, 13736.0, 15324.0, 13732.0, 14276.0, 14424.0, 13852.0, 14556.0, 16880.0, 16596.0, 18272.0, 19056.0, 17712.0, 17084.0, 17856.0, 16196.0]
values_ctm_cen= [12884.0, 14360.0, 14116.0, 14588.0, 13904.0, 14012.0, 14656.0, 13808.0, 17660.0, 17768.0, 18068.0, 17972.0, 17716.0, 17452.0, 17340.0, 17972.0]
values_ctm_dec= [11784.0, 14464.0, 14240.0, 14136.0, 13356.0, 13356.0, 13880.0, 13612.0, 15900.0, 15972.0, 15552.0, 16696.0, 16040.0, 15052.0, 15716.0, 15404.0]
# Generate time intervals from 6:00 AM to 10:00 AM in 15-minute intervals
start_time = datetime.datetime.strptime("11:15", "%H:%M")
time_intervals = [start_time + datetime.timedelta(minutes=15*i) for i in range(16)]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(time_intervals, values_fixedtime, marker='o', label='Fixed Time', linewidth = 3)
plt.plot(time_intervals, values_sf_cen, marker='v', label='SF Centralized')
plt.plot(time_intervals, values_sf_dec, marker='^', label='SF Decentralized')
plt.plot(time_intervals, values_ctm_cen, marker='>', label='CTM Centralized')
plt.plot(time_intervals, values_ctm_dec, marker='<', label='CTM Decentralized')

plt.title("Average Vehicular Flow Rate from 11 AM to 3 PM (15 minute-window)")
plt.xlabel("Time")
plt.ylabel("Average Vehicular Flow Rate (veh/hr)")
plt.xticks(time_intervals, [t.strftime("%H:%M") for t in time_intervals], rotation=45)


# Setting x-axis limits
end_time = start_time + datetime.timedelta(hours=4)
plt.xlim([start_time, end_time])
plt.legend()

plt.grid(True)
plt.tight_layout()
plt.show()
