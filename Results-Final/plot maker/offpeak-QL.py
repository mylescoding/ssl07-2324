import matplotlib.pyplot as plt
import datetime


values_fixedtime = [4.7686574074074075, 5.568981481481482, 4.994212962962963, 5.532175925925926, 5.023981481481481, 5.458055555555556, 5.025601851851852, 5.44587962962963, 6.641666666666667, 7.440787037037037, 7.098981481481482, 7.4195370370370375, 7.231805555555556, 7.6943981481481485, 7.57337962962963, 8.693472222222223]

values_sf_cen = [3.878240740740741, 4.971481481481482, 4.4937499999999995, 4.957268518518519, 5.333055555555556, 5.470324074074075, 4.680046296296296, 4.801388888888889, 8.048287037037037, 7.206898148148149, 7.583657407407408, 8.172638888888889, 8.083657407407408, 7.022361111111111, 7.145231481481481, 7.210092592592592]

values_sf_dec= [5.8187500000000005, 6.144259259259258, 7.115231481481481, 7.279305555555556, 7.164166666666667, 7.025601851851852, 6.025509259259259, 6.175, 8.98111111111111, 12.874953703703703, 13.203657407407407, 10.664861111111112, 10.237222222222222, 9.615509259259259, 9.318935185185184, 12.312222222222223]
values_ctm_cen= [3.7631944444444443, 3.936851851851852, 4.004444444444444, 4.095416666666667, 4.058425925925926, 3.8688888888888893, 4.170648148148148, 4.095833333333333, 5.326064814814814, 5.805555555555556, 6.476388888888889, 6.889120370370371, 7.534027777777777, 7.684768518518518, 7.301898148148148, 7.172453703703703]
values_ctm_dec= [4.86212962962963, 6.590601851851852, 6.705324074074074, 8.502268518518518, 10.648148148148147, 12.736203703703703, 14.655185185185184, 15.578842592592594, 19.84939814814815, 22.90513888888889, 21.90185185185185, 21.62523148148148, 23.498148148148147, 25.054259259259258, 26.24384259259259, 25.956435185185185]

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

plt.title("Average Queue Lengths from 11 AM to 3 PM (15 minute-window)")
plt.xlabel("Time")
plt.ylabel("Average Queue Length (veh)")
plt.xticks(time_intervals, [t.strftime("%H:%M") for t in time_intervals], rotation=45)


# Setting x-axis limits
end_time = start_time + datetime.timedelta(hours=4)
plt.xlim([start_time, end_time])
plt.legend()

plt.grid(True)
plt.tight_layout()
plt.show()