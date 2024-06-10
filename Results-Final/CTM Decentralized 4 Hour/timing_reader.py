import xml.etree.ElementTree as ET

# Load and parse the XML file
tree = ET.parse('kbt_timing.xml')
root = tree.getroot()
roott = root.find('tlLogic')





def extract_tripinfo():
    values = []
    p1 =[]
    p2 =[]
    p3 =[]
    p4 =[]
    for tripinfo in roott.findall('phase'):
        duration = tripinfo.get('duration')
        name = tripinfo.get('name')
        phase_num = name.split(' - ')[0]
        green=name.split(' - ')[2]
        if green == 'green':
            if phase_num == 'phase 1':
                p1.append(duration)
            if phase_num == 'phase 2':
                p2.append(duration)
            if phase_num == 'phase 3':
                p3.append(duration)
            if phase_num == 'phase 4':
                p4.append(duration)
    print("PHASE 1 with length of " + str(len(p1)))
    print(p1)
    print("PHASE 2 with length of " + str(len(p2)))
    print(p2)
    print("PHASE 3 with length of " + str(len(p3)))
    print(p3)
    print("PHASE 4 with length of " + str(len(p4)))
    print(p4)
            
            
        
        

            
extract_tripinfo()