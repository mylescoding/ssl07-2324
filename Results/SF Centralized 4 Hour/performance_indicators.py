import xml.etree.ElementTree as ET

# Load and parse the XML file
tree = ET.parse('tripinfo_out.xml')
root = tree.getroot()

tree2 = ET.parse('summary_out.xml')
root2 = tree2.getroot()


def extract_tripinfo(attribute_name):
    values = []
    for tripinfo in root.findall('tripinfo'):
        value = tripinfo.get(attribute_name)
        if value is not None:
            values.append(float(value))
    return sum(values)/len(values)

def extract_summary(attribute_name):
    values = []
    for step in root2.findall('step'):
        value = step.get(attribute_name)
        if value is not None:
            values.append(float(value))
    return sum(values)/14400
    #return sum(values)/50400


attribute_qt = 'halting'
average_qt = extract_summary(attribute_qt)
print(f"Average queue length (veh): " + str(average_qt))

attribute_wt = 'waitingTime'
average_wt = extract_tripinfo(attribute_wt)

print(f"Average time in queue (s): " + str(average_wt))

attribute_vfr = 'running'
average_vfr = extract_summary(attribute_vfr)
print(f"Average vehicular flow rate (veh/hr): " + str (average_vfr))





