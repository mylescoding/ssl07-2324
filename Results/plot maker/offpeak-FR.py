import matplotlib.pyplot as plt
import datetime


values_fixedtime = [13044.0, 13184.0, 15432.0, 13320.0, 15220.0, 13168.0, 15088.0, 13476.0, 18300.0, 17252.0, 18804.0, 17560.0, 17968.0, 17232.0, 17576.0, 17564.0]
values_sf_cen = [12828.0, 14212.0, 13712.0, 13372.0, 14460.0, 15740.0, 14152.0, 14104.0, 16248.0, 18144.0, 19364.0, 16128.0, 18800.0, 17640.0, 17700.0, 15768.0]
values_sf_dec= [11136.0, 13832.0, 16224.0, 13500.0, 14912.0, 13304.0, 14968.0, 13500.0, 17264.0, 18256.0, 16504.0, 20344.0, 16788.0, 17072.0, 16972.0, 19036.0]
values_ctm_cen= [12636.0, 14292.0, 14108.0, 14592.0, 14236.0, 14104.0, 14136.0, 14076.0, 17580.0, 18268.0, 18164.0, 17664.0, 17548.0, 17664.0, 17596.0, 17348.0]
values_ctm_dec=[13116.0, 13892.0, 14124.0, 14400.0, 14512.0, 14192.0, 14348.0, 13552.0, 17888.0, 17264.0, 18764.0, 18664.0, 16756.0, 17296.0, 17916.0, 16968.0]
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
