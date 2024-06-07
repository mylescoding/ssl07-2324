import xml.etree.ElementTree as ET

# Load and parse the XML file
tree = ET.parse('tripinfo.xml')
root = tree.getroot()

tree2 = ET.parse('summary_out.xml')
root2 = tree2.getroot()


def extract_tripinfo(attribute_name, flag = 0):
    values = []
    for tripinfo in root.findall('tripinfo'):
        value = tripinfo.get(attribute_name)
        if value is not None:
            values.append(float(value))
        if value is not None and flag == 1:
            timestep = tripinfo.get('depart')
            if float(timestep) >= 14400.00:
                return sum(values)/len(values)
            
    return sum(values)/len(values)

def extract_summary(attribute_name, flag = 0):
    values = []
    for step in root2.findall('step'):
        value = step.get(attribute_name)
        if value is not None:
            values.append(float(value))
        if value is not None and flag == 1:
            timestep = step.get('time')
            if float(timestep) == 14400.00:
                return sum(values)/14400
    return sum(values)/14400


def serviced_4hr(attribute_name):
    for step in root2.findall('step'):
        value = step.get('arrived')
        if value is not None:
            timestep = step.get('time')
            if float(timestep) == 14400.00:
                return value


            



attribute_qt = 'halting'
average_qt_whole = extract_summary(attribute_qt,  0)
print(f"(WHOLE) Average queue length (veh): " + str(average_qt_whole/24))

average_qt_4hr = extract_summary(attribute_qt,  1)
print(f"(4 HR) Average queue length (veh) - 4 hour: " + str(average_qt_4hr/24))

attribute_wt = 'waitingTime'
average_wt_whole = extract_tripinfo(attribute_wt, 0)
print(f"(WHOLE) Average time in queue (s): " + str(average_wt_whole))

average_wt_4hr = extract_tripinfo(attribute_wt, 1)
print(f"(4 HR) Average time in queue (s): " + str(average_wt_4hr))

attribute_vfr = 'running'
average_vfr_whole = extract_summary(attribute_vfr, 0)
print(f"(WHOLE) Average vehicular flow rate (veh/hr): " + str (average_vfr_whole))

average_vfr_4hr = extract_summary(attribute_vfr, 1)
print(f"(4 HR) Average vehicular flow rate (veh/hr): " + str (average_vfr_4hr))

attribute_serviced = 'time'
cars_serviced = serviced_4hr(attribute_serviced)
print(f"Cars serviced in 4 hours is:  " + str (cars_serviced))





