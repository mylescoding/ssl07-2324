import matplotlib.pyplot as plt
import datetime


values_fixedtime = [16592.0, 16804.0, 19736.0, 16928.0, 21740.0, 19004.0, 22344.0, 19356.0, 23264.0, 20988.0, 23188.0, 21240.0, 18668.0, 16916.0, 17128.0, 17136.0]
values_sf_cen = [15508.0, 17824.0, 16532.0, 19624.0, 21252.0, 20324.0, 20664.0, 18264.0, 21728.0, 20300.0, 24364.0, 21208.0, 18224.0, 18216.0, 18732.0, 17484.0]
values_sf_dec= [15216.0, 18380.0, 16732.0, 18708.0, 21048.0, 21132.0, 19756.0, 22028.0, 20252.0, 21060.0, 22404.0, 21084.0, 21276.0, 16988.0, 16772.0, 17168.0]
values_ctm_cen= [15880.0, 18740.0, 17748.0, 18488.0, 19780.0, 21368.0, 20272.0, 21112.0, 21776.0, 21804.0, 21972.0, 21880.0, 18540.0, 17676.0, 17132.0, 16704.0]
values_ctm_dec=[16184.0, 18268.0, 17720.0, 18576.0, 19776.0, 20528.0, 19708.0, 20476.0, 22364.0, 22228.0, 21988.0, 21708.0, 19576.0, 18276.0, 16152.0, 17620.0]
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

plt.title("Average Vehicular Flow Rate from 6 AM to 10 AM (15 minute-window)")
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
