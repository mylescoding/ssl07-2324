import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# Given data
times = [(6.0, 6.25), (6.25, 6.5), (6.5, 6.75), (6.75, 7.0), (7.0, 7.25), (7.25, 7.5), (7.5, 7.75), 
         (7.75, 8.0), (8.0, 8.25), (8.25, 8.5), (8.5, 8.75), (8.75, 9.0), (9.0, 9.25), 
         (9.25, 9.5), (9.5, 9.75), (9.75, 10.0), (10.0, 10.25)]

# values = [9.77273148148148, 16.19949074074074, 20.019583333333333, 8.411851851851852, 
#           15.573842592592593, 23.834305555555556, 25.424537037037037, 15.251944444444446, 
#           20.34537037037037, 27.98597222222222, 30.425555555555558, 21.717175925925925, 
#           17.53796296296296, 17.38736111111111, 16.798657407407408, 10.907175925925927, 
#           6.5675]

#queue times
#values = [74.84367816091954, 119.94657811146405, 137.5760190419518, 605.3837209302326, 122.48347425057648, 143.98245125348188, 169.45500705218618, 344.20588235294116, 134.23692935475643, 186.07895431740164, 205.49388549193998, 234.85302325581395, 121.31625275070732, 108.37349397590361, 142.7244019138756, 878.6390532544378, 882.8571428571429]
#vfr
values =[510.8988888888889, 694.31, 836.1733333333333, 258.1177777777778, 709.4233333333333, 944.87, 1031.1655555555556, 497.6377777777778, 847.6922222222222, 1079.2655555555555, 1144.8044444444445, 724.7766666666666, 693.9744444444444, 715.7877777777778, 681.8933333333333, 317.8833333333333, 184.09555555555556]

# Convert times to datetime objects
start_range = datetime.strptime('06:00', '%H:%M')
end_range = datetime.strptime('10:15', '%H:%M')
time_labels = []
for start, end in times:
    time_labels.append(start_range + timedelta(hours=start))
    


# Plotting
plt.figure(figsize=(10, 6))
plt.plot(time_labels, values, marker='o')

# Formatting the x-axis to show time
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
plt.gca().xaxis.set_major_locator(mdates.MinuteLocator(interval=15))



plt.xlabel('Time')
plt.ylabel('Average Vehicular Flow Rate (veh/hr)')
plt.title('Average Vehicular Flow Rate in the Simulation - 15 minute intervals ')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()