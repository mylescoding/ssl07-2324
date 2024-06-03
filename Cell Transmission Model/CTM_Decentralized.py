import math

curr_phase = "Phase 0"
the_dict = {}


class Cell:
    def __init__(self, lane, length, max_speed, car_num, busy, tick):
        self.lane = lane
        self.busy = busy
        self.car_num = car_num
        self.arr = []
        self.cells = []
        self.delay = 0
        name = lane.split("-")
        shortname_dictionary = {
            " Lane 0": "L0_",
            " Lane 1": "L1_",
            " Lane 2": "L2_",
            " Lane 3": "L3_",
            " Lane 4": "L4_",
            "Upper Katipunan SB ": "K1_SB_",
            "Middle Katipunan SB ": "K2_SB_",
            "B. Gonzales Road ": "Bgon_",
            "F. dela Rosa Road ": "FdRosa_",
            "Middle Katipunan NB upper ": "K2_NB_R4_",
            "Middle Katipunan NB lower ": "K2_NB_R5R6_",
            "Lower Katipunan NB ": "K3_NB_",
            "Thornton Drive ": "TDrive_",
            " Lower": "lower_L0_",
            " Upper": "upper_L0_",
            " extension": "L0_",
            "University Road upper ": "URd_upper_",
            "University Road lower ": "URd_lower_",
            " Exit": "out_L0_"
        }
        road_lane_name = shortname_dictionary[name[0]] + shortname_dictionary[name[1]]

        for n in range(math.floor(length / (max_speed / tick))):
            self.arr.append((road_lane_name + "C" + str(n), 0, 0))
            self.cells.append(road_lane_name + "C" + str(n))
        self.arr_len = len(self.arr)


K1_SB_0 = Cell("Upper Katipunan SB - Lane 0", 400, 16.67, 0, 0, 1)
K1_SB_1 = Cell("Upper Katipunan SB - Lane 1", 400, 16.67, 0, 0, 1)
K1_SB_2 = Cell("Upper Katipunan SB - Lane 2", 400, 16.67, 0, 0, 1)
K1_SB_3 = Cell("Upper Katipunan SB - Lane 3", 400, 16.67, 0, 0, 1)
K1_SB_4 = Cell("Upper Katipunan SB - Lane 4", 400, 16.67, 0, 0, 1)

BGon_0 = Cell("B. Gonzales Road - Lane 0", 291, 8.33, 0, 0, 1)
BGon_1 = Cell("B. Gonzales Road - Lane 1", 291, 8.33, 0, 0, 1)

TDrive_lower = Cell("Thornton Drive - Lower", 56, 13.89, 0, 0, 1)
TDrive_upper = Cell("Thornton Drive - Upper", 36.72, 13.89, 0, 0, 1)
TDrive_extension = Cell("Thornton Drive - extension", 188.45, 13.89, 0, 0, 1)

K2_SB_0 = Cell("Middle Katipunan SB - Lane 0", 178.37, 16.67, 0, 0, 1)
K2_SB_1 = Cell("Middle Katipunan SB - Lane 1", 178.37, 16.67, 0, 0, 1)
K2_SB_2 = Cell("Middle Katipunan SB - Lane 2", 178.37, 16.67, 0, 0, 1)
K2_SB_3 = Cell("Middle Katipunan SB - Lane 3", 178.37, 16.67, 0, 0, 1)
K2_SB_4 = Cell("Middle Katipunan SB - Lane 4", 178.37, 16.67, 0, 0, 1)

K2_NB_R4_0 = Cell("Middle Katipunan NB upper - Lane 0", 33.4, 16.67, 0, 0, 1)
K2_NB_R4_1 = Cell("Middle Katipunan NB upper - Lane 1", 33.4, 16.67, 0, 0, 1)
K2_NB_R4_2 = Cell("Middle Katipunan NB upper - Lane 2", 33.4, 16.67, 0, 0, 1)
K2_NB_R4_3 = Cell("Middle Katipunan NB upper - Lane 3", 33.4, 16.67, 0, 0, 1)

K2_NB_R5R6_0 = Cell("Middle Katipunan NB lower - Lane 0", 137.78, 16.67, 0, 0, 1)
K2_NB_R5R6_1 = Cell("Middle Katipunan NB lower - Lane 1", 137.78, 16.67, 0, 0, 1)
K2_NB_R5R6_2 = Cell("Middle Katipunan NB lower - Lane 2", 137.78, 16.67, 0, 0, 1)

FdRosa_0 = Cell("F. dela Rosa Road - Lane 0", 233.12, 8.33, 0, 0, 1)
FdRosa_1 = Cell("F. dela Rosa Road - Lane 1", 233.12, 8.33, 0, 0, 1)

URd_upper_out = Cell("University Road upper - Exit", 277, 13.89, 0, 0, 1)
URd_lower_out = Cell("University Road lower - Exit", 156.24, 13.89, 0, 0, 1)

K3_NB_0 = Cell("Lower Katipunan NB - Lane 0", 309.12, 16.67, 0, 0, 1)
K3_NB_1 = Cell("Lower Katipunan NB - Lane 1", 309.12, 16.67, 0, 0, 1)
K3_NB_2 = Cell("Lower Katipunan NB - Lane 2", 309.12, 16.67, 0, 0, 1)

Phase_1_kbt = [K1_SB_0, K1_SB_1, K1_SB_2, K1_SB_3, K2_NB_R4_0, K2_NB_R4_1, K2_NB_R4_2, K2_NB_R4_3]
Phase_1_kuf = [K2_SB_0, K2_SB_1, K2_SB_2, K2_SB_3, K2_SB_4, K3_NB_0, K3_NB_1, K3_NB_2]

Phase_2_kbt = [BGon_0, BGon_1]
Phase_2_kuf = [URd_lower_out, FdRosa_0, FdRosa_1]

Phase_3_kbt = [K1_SB_4, TDrive_lower]
Phase_3_kuf = [URd_upper_out]

Phase_4_kbt = [K1_SB_0, K1_SB_1, K1_SB_2, K1_SB_3, K1_SB_4]
Phase_4_kuf = [K2_SB_0, K2_SB_1, K2_SB_2, K2_SB_3, K2_SB_4]

network = [K1_SB_0, K1_SB_1, K1_SB_2, K1_SB_3, K1_SB_4, BGon_0, BGon_1, TDrive_lower, TDrive_upper, TDrive_extension,
           K2_SB_0, K2_SB_1, K2_SB_2, K2_SB_3, K2_SB_4, K2_NB_R4_0, K2_NB_R4_1, K2_NB_R4_2, K2_NB_R4_3, K2_NB_R5R6_0,
           K2_NB_R5R6_1, K2_NB_R5R6_2, FdRosa_0, FdRosa_1, URd_upper_out, URd_lower_out, K3_NB_0, K3_NB_1, K3_NB_2]

array = []


def read_input():
    current_phase = curr_phase
    traci_cell_dict = the_dict

    for cell_group in network:
        for cell in cell_group.arr:
            index = cell_group.arr.index(cell)
            listed_tuple = list(cell)
            listed_tuple[1] = traci_cell_dict[listed_tuple[0]][0]
            listed_tuple[2] = round(traci_cell_dict[listed_tuple[0]][1], 2)
            cell_group.arr[index] = tuple(listed_tuple)
        array.append(cell_group.arr)
    # return current_phase, array
    return traci_cell_dict

# phase, get_array = read_input()
# print(phase)
# print(get_array)


def evaluate_delay(cell):
    traci_cell_dict = read_input()
    delay_time = 0
    sum = 0
    for cells in cell.cells:
#        if traci_cell_dict[cells][1] > 95:
#            delay_time += 1
        sum += traci_cell_dict[cells][1]
        delay_time = math.floor(sum / 100)
    cell.delay = delay_time


# !/usr/bin/env python

import os
import sys
import optparse

# we need to import some python modules from the $SUMO_HOME/tools directory
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

from sumolib import checkBinary  # Checks for the binary in environ vars
import traci


def get_options():
    opt_parser = optparse.OptionParser()
    opt_parser.add_option("--nogui", action="store_true",
                          default=False, help="run the commandline version of sumo")
    options, args = opt_parser.parse_args()
    return options


def getLaneParams():
    cells = traci.lanearea.getIDList()
    cell_dict = dict()
    for cell in cells:
        # print(cell)
        cell_vehicles = traci.lanearea.getLastStepVehicleNumber(cell)
        # print(cell_vehicles)
        occupancy = traci.lanearea.getLastStepOccupancy(cell)
        # print(occupancy)
        # if cell_vehicles != 0:
        cell_dict[cell] = (cell_vehicles, occupancy)
        # cell_list.append((cell, (cell_vehicles, occupancy)))

    if len(cell_dict) > 0:
        # print(cell_dict)
        return cell_dict


# TraCI control loop
def run():
    step = 0
    ctr_kbt = 0
    ctr_kuf = 0
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()  # move one second in simulation
        if (step % 5 == 0):
            print("time step:" + str(step))
            # print(str(traci.trafficlight.getPhase("kuf")) + " : " + str(traci.trafficlight.getPhaseDuration("kuf")))
            #if (traci.trafficlight.getPhase("kuf") in [0, 3, 6, 9]):
            #kuf_phase = traci.trafficlight.getPhase("kuf")
            kbt_phase_name = traci.trafficlight.getPhaseName("kbt")
            kuf_phase_name = traci.trafficlight.getPhaseName("kuf")

            time_remaining_kbt = traci.trafficlight.getNextSwitch("kbt") - traci.simulation.getTime()
            time_remaining_kuf = traci.trafficlight.getNextSwitch("kuf") - traci.simulation.getTime()

            print("KBT NextSwitch:" + str(time_remaining_kbt))
            print("KUF NextSwitch:" + str(time_remaining_kuf))
            #if (kuf_phase != old_kuf_phase):
            global curr_phase
            global the_dict
            curr_phase = kuf_phase_name.split(" - ")
            the_dict = getLaneParams()
            #print("---------------------------------------------------")
            #print("The current phase with light color: " + str(kuf_phase_name))
            #print("The current phase only: " + str(curr_phase[0]))
            #print("dict w/ lane name, veh count and occupancy:")
            #print(str(the_dict))
            print("---------------------------------------------------")

            phase1kbtdelay = 0
            phase2kbtdelay = 0
            phase3kbtdelay = 0
            phase4kbtdelay = 0
            phase1kufdelay = 0
            phase2kufdelay = 0
            phase3kufdelay = 0
            phase4kufdelay = 0

            for phases in Phase_1_kbt:
                evaluate_delay(phases)
                phase1kbtdelay += phases.delay
                
            for phases in Phase_2_kbt:
                evaluate_delay(phases)
                phase2kbtdelay += phases.delay

            for phases in Phase_3_kbt:
                evaluate_delay(phases)
                phase3kbtdelay += phases.delay

            for phases in Phase_4_kbt:
                evaluate_delay(phases)
                phase4kbtdelay += phases.delay
                
            for phases in Phase_1_kuf:
                evaluate_delay(phases)
                phase1kufdelay += phases.delay
                
            for phases in Phase_2_kuf:
                evaluate_delay(phases)
                phase2kufdelay += phases.delay

            for phases in Phase_3_kuf:
                evaluate_delay(phases)
                phase3kufdelay += phases.delay

            for phases in Phase_4_kuf:
                evaluate_delay(phases)
                phase4kufdelay += phases.delay

            print("kbt phase 1 = " + str(phase1kbtdelay) +"\nphase 2 = " + str(phase2kbtdelay) +"\nphase 3 = " + str(phase3kbtdelay) +"\nphase 4 = " + str(phase4kbtdelay) )
            print("kuf phase 1 = " + str(phase1kufdelay) +"\nphase 2 = " + str(phase2kufdelay) +"\nphase 3 = " + str(phase3kufdelay) +"\nphase 4 = " + str(phase4kufdelay) )

            #print("===================================================")
            #print(phase1delay, phase2delay, phase3delay, phase4delay)
            # this tracks green changes in KUF
            
            current_phase_kbt = traci.trafficlight.getPhase("kbt")
            current_phase_kuf = traci.trafficlight.getPhase("kuf")
            next_phase_kbt = (current_phase_kbt + 1)
            next_phase_kuf = (current_phase_kuf + 1)
            print(f"kbt current phase: {current_phase_kbt}")
            print(f"kuf current phase: {current_phase_kuf}")
            print(f"kbt ctr = {ctr_kbt}     kuf ctr = {ctr_kuf}")
            print("===================================================")
            
            # KBT
            if current_phase_kbt == 0:
                phase_x_kbt = phase1kbtdelay
                phase_y_kbt = phase2kbtdelay
            elif current_phase_kbt == 3:
                phase_x_kbt = phase2kbtdelay
                phase_y_kbt = phase3kbtdelay
            elif current_phase_kbt == 6:
                phase_x_kbt = phase3kbtdelay
                phase_y_kbt = phase4kbtdelay
            elif current_phase_kbt == 9:
                phase_x_kbt = phase4kbtdelay
                phase_y_kbt = phase1kbtdelay
                
            if next_phase_kbt == 12:
                next_phase_kbt = 0

            if phase_x_kbt<phase_y_kbt and current_phase_kbt in [0,3,6,9]:
                traci.trafficlight.setPhase("kbt", next_phase_kbt)
            elif current_phase_kbt in [0,3,6,9] and time_remaining_kbt <= 5 and ctr_kbt % 4 != 0:
                traci.trafficlight.setPhaseDuration ("kbt", 10)
                ctr_kbt += 1
            elif ctr_kbt % 4 == 0 and ctr_kbt != 0:
                traci.trafficlight.setPhase("kbt", next_phase_kbt)
                
            # KUF
            if current_phase_kuf == 0:
                phase_x_kuf = phase1kufdelay
                phase_y_kuf = phase2kufdelay
            elif current_phase_kuf == 3:
                phase_x_kuf = phase2kufdelay
                phase_y_kuf = phase3kufdelay
            elif current_phase_kuf == 6:
                phase_x_kuf = phase3kufdelay
                phase_y_kuf = phase4kufdelay
            elif current_phase_kuf == 9:
                phase_x_kuf = phase4kufdelay
                phase_y_kuf = phase1kufdelay
                
            if next_phase_kuf == 12:
                next_phase_kuf = 0

            if phase_x_kuf<phase_y_kuf and current_phase_kuf in [0,3,6,9]:
                traci.trafficlight.setPhase("kuf", next_phase_kuf)
            elif current_phase_kuf in [0,3,6,9] and time_remaining_kuf <= 5 and ctr_kuf % 4 != 0:
                traci.trafficlight.setPhaseDuration ("kuf", 10)
                ctr_kuf += 1
            elif ctr_kuf % 4 == 0 and ctr_kuf != 0:
                traci.trafficlight.setPhase("kuf", next_phase_kuf)
                
        step += 1


    # traci.close()
    # sys.stdout.flush()


if __name__ == "__main__":
    options = get_options()

    # check binary
    if options.nogui:
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')

    # traci starts sumo as a subprocess and then this script connects and runs
    traci.start([sumoBinary, "-c", "osm.sumocfg",
                 "--tripinfo-output", "tripinfo.xml"])
    # getLaneParams()

    run()

