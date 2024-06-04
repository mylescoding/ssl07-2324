import math
import torch
from botorch.models import SingleTaskGP, ModelListGP
from gpytorch.mlls.exact_marginal_log_likelihood import ExactMarginalLogLikelihood
from botorch import fit_gpytorch_model
from botorch.acquisition.monte_carlo import qExpectedImprovement
from botorch.optim import optimize_acqf
import random

import warnings

class Vertex:
    def __init__(self, name, car_num, busy, speed, leng, source, dest):
        self.name = name  # Returns number of cars on path
        self.car_num = car_num  # Returns number of cars on path
        self.busy = busy  # Returns 1 if busy, 0 if free
        self.speed = speed  # Constant showing speed of cars in m/s
        self.leng = leng  # Constant showing length of path in meters
        self.source = source
        self.dest = dest

    def __str__(self):
        return f"{self.name}"


# Generation Vertices do not have source or dest attributes.
# 0 is given instead as a place holder

Cars_Passed = 0  # Number of Cars that have exited system
Time = float(0.0)  # Current Time



# generation vertices
#indiv roads
K = Vertex("Katipunan", 0, 0, 17, 406, 0, 0)  # Generation Vertex at LaVista
Gonza = Vertex("Gonza", 0, 0, 9, 300,  0, 0)  # Generation Vertex at Gonzales
TDrive = Vertex( "TDrive",0, 0, 14, 230, 0, 0)  # Generation Vertex at Thornton Drive
K2S = Vertex("K2S", 0, 0, 17, 178, 0 , 0)  # Road between Katip-Gonza_TDrive and Katip-FDRosa-URd, Northbound
K2N = Vertex("K2N", 0, 0, 17, 170, 0, 0)  # Same as above, but southbound
FDRosa = Vertex("FDRosa", 0, 0, 9, 243, 0,0)  # Generation Vertex at FDRosa
K3 = Vertex("K3", 0, 0, 17, 309, 0,0)  # Generation at Aurora Katipunan
URd = Vertex("URd", 0, 0, 14, 140, 0,0)  # Combination of all four mini roads in the direction of Ateneo
Uturn = Vertex("Uturn", 0, 0, 14, 10, 0,0)

#routes
K_Gonza = Vertex("K_Gonza",0, 0, 9, 7, K, Gonza)  # Katip to Katip2
K_K2S = Vertex("K_K2S",0, 0, 17, 7, K, K2S)  # Katipu LaVista to Katipunan-FDRosa-URd Intersec
K_TDrive = Vertex("K_TDrive",0, 0, 14, 7, K, TDrive)  # Katip to Thornton
K_Uturn = Vertex("K_Uturn",0, 0, 9, 7, K, Uturn)  # Katip uturn to self

Gonza_K = Vertex("Gonza_K",0, 0, 5, 7, Gonza, K)  # Gonzales to Katip
Gonza_TDrive = Vertex("Gonza_TDrive",0, 0, 5, 7, Gonza, TDrive)  # Gonzales to Thornton Drive
Gonza_K2S = Vertex("Gonza_K2S",0, 0, 5, 7, Gonza, K2S)  # Gonzales to Katipunan-FDRosa-URd Intersec

TDrive_K = Vertex("TDrive_K",0, 0, 14, 7, TDrive, K)  # Thornton to Katip LaVista
TDrive_Gonza = Vertex("TDrive_Gonza",0, 0, 9, 7, TDrive, Gonza)  # TDrive to Gonza
TDrive_K2S = Vertex("TDrive_K2S",0, 0, 14, 7, TDrive, K2S)  # TDrive to Katipunan-FDRosa-URd Intersec

K2N_K = Vertex("K2N_K",0, 0, 17, 7, K2N, K)  # Road from Katip2 to Katip1
K2N_TDrive = Vertex("K2N_TDrive",0, 0, 14, 7, K2N, TDrive)  # Katip2 to Tdrive
K2S_URd = Vertex("K2S_URd",0, 0, 14, 7, K2S, URd)  # Katip2 to University Road
K2S_K2N = Vertex("K2S_K2N",0, 0, 9, 7, K2N, Uturn)  # Katip2 Uturn
K2N_K2S = Vertex("K2N_K2S",0, 0, 9, 7, K2N, Uturn)  # Katip2 Uturn
K2S_K3 = Vertex("K2S_K3",0, 0, 17, 7, K2S, K3)  # Katip2 to Katip3(Aurora)
K2S_FDRosa = Vertex("K2S_FDRosa",0, 0, 14, 7, K2S, FDRosa)  # Katip2 to FDRosa

FDRosa_K2N = Vertex("FDRosa_K2N",0, 0, 9, 7, FDRosa, K2N)  # FDRosa to K2
FDRosa_URd = Vertex("FDRosa_URd",0, 0, 9, 7, FDRosa, URd)  # FDRosa to University Road
FDRosa_K3 = Vertex("FDRosa_K3",0, 0, 9, 7, FDRosa, K3)  # FDRosa to K3

URd_K3 = Vertex("URd_K3",0, 0, 14, 7, URd, K3)  # University Road to K3 Southbound
URd_K2N = Vertex("URd_K2N",0, 0, 14, 7, URd, K2N) # University Road to K2 Northbound

K3_K2N = Vertex("K3_K2N",0, 0, 17, 7, K3, K2N)  # K3 to K2 Northbound
K3_URd = Vertex("K3_URd",0, 0, 14, 7, K3, URd)  # K3 to University Road

Roads = [K_Gonza, K_K2S, K_TDrive, K_Uturn, Gonza_K, Gonza_TDrive, Gonza_K2S,
         TDrive_K, TDrive_Gonza, TDrive_K2S, FDRosa_K2N, FDRosa_URd, FDRosa_K3,
         K2N_K, K2N_TDrive, K2S_URd, K2N_K2S, K2S_K2N, K2S_K3, K2S_FDRosa, K3_K2N, K3_URd, URd_K3, URd_K2N]  # list of the roads

Entrance_Nodes = [K, Gonza, TDrive, K3, FDRosa, URd]
Exit_Nodes = [FDRosa, K, K3, URd, TDrive, Gonza]


def Set_Busy(Vertex):
    if Vertex.busy == 0:
        Vertex.busy = 1
    else:
        pass


def Set_Stall(Vertex):
    if Vertex.busy == 1:
        Vertex.busy = 0
    else:
        pass


def Evaluate_Busy(Green_Time):
    Restore_Original_State()
    global Cars_Passed
    Cars_Passed = 0
    y = 0   
    for i in range(len(Roads)):  # go through all the lanes
        if Roads[i].busy == 1:  # if the selected road is busy meaning there is a presence of car/s
            y = torch.ceil(Green_Time / (Roads[i].leng / Roads[i].speed))[-1]# Number of Cars that can pass through in green time
            if y > Roads[i].car_num:
                y = Roads[i].car_num
            Roads[i].car_num = Roads[i].car_num - y  # Remove from road
            Cars_Passed = Cars_Passed + y
        #print(f"Road {Roads[i].name} has {Roads[i].car_num} cars")
    global Time
    #print(f"Time: {Time} ")
    #print(f"Green_Time: {Green_Time} ")
    #Time = Time + Green_Time


def Phase_1():
    # Katip-B.Gon-Thornton
    Set_Busy(K_K2S)
    Set_Busy(K2N_K)
    Set_Busy(K2N_TDrive)

    # Katip-Univ-F.dela
    Set_Busy(K2S_K3)
    Set_Busy(K3_K2N)
    Set_Busy(K3_URd)


def Phase_2():
    # Katip-B.Gon-Thornton
    Set_Busy(Gonza_K)
    Set_Busy(Gonza_K2S)

    # Katip-Univ-F.dela
    Set_Busy(URd_K3)
    Set_Busy(FDRosa_K2N)
    Set_Busy(FDRosa_K3)
    Set_Busy(FDRosa_URd)


def Phase_3():
    # Katip-B.Gon-Thornton
    Set_Busy(K_Uturn)
    Set_Busy(TDrive_K2S)
    Set_Busy(TDrive_K)
    #Set_Busy(K2N_TDrive)

    # Katip-Univ-F.dela
    Set_Busy(URd_K3)
    Set_Busy(URd_K2N)


def Phase_4():
    # Katip-B.Gon-Thornton
    Set_Busy(K_Uturn)
    Set_Busy(K_K2S)
    Set_Busy(K_TDrive)

    # Katip-Univ-F.dela
    Set_Busy(K2S_URd)
    Set_Busy(K2S_K2N)
    Set_Busy(K2S_K3)


def Unassert():
    for i in range(len(Roads)):
        Set_Stall(Roads[i])



for_helper_phase = "phase 4 - kuf-green"
for_helper_dictionary = {'katip_t_nb_0_count': 0, 'katip_t_nb_1_count': 0, 'katip_t_nb_2_count': 0, 'katip_t_nb_3_count': 0, 'katip_t_sb_0_count': 0, 'katip_t_sb_1_count': 0, 'katip_t_sb_2_count': 0, 'katip_t_sb_3_count': 0, 'katip_t_sb_4_count': 0, 'thornton-drive-lower-out_0_count': 0, 'thornton-drive-in_0_count': 0, 'katip_m_u_nb_0_count': 0, 'katip_m_u_nb_1_count': 0, 'katip_m_u_nb_2_count': 0, 'katip_m_u_nb_3_count': 0, 'katip_m_l_nb_0_count': 0, 'katip_m_l_nb_1_count': 0, 'katip_m_l_nb_2_count': 0, 'b.gonzales-road_0_count': 0, 'b.gonzales-road_1_count': 0, 'katip_m_sb_0_count': 0, 'katip_m_sb_1_count': 0, 'katip_m_sb_2_count': 0, 'katip_m_sb_3_count': 0, 'katip_m_sb_4_count': 0, 'univ-road-upper-out_0_count': 0, 'univ-road-upper-in_0_count': 0, 'univ-road-lower-out_0_count': 0, 'univ-road-lower-in_0_count': 0, 'f.dela-rosa-road_1_count': 0, 'f.dela-rosa-road_0_count': 0, 'katip_b_sb_0_count': 0, 'katip_b_sb_1_count': 0, 'katip_b_sb_2_count': 0, 'katip_b_sb_3_count': 0, 'katip_b_sb_4_count': 0, 'katip_b_nb_0_count': 100, 'katip_b_nb_1_count': 100, 'katip_b_nb_2_count': 100}

past_phases = [0,0,0,0]
def helper_function(phase,diksyonaryo):
    global past_phases
    phase = phase.partition(" - ")[0]
    #Mid Katipunan to Top Katipunan
    K2N_K.car_num  = diksyonaryo["katip_m_u_nb_1_count"]
    K2N_K.car_num += diksyonaryo["katip_m_u_nb_2_count"]
    K2N_K.car_num += diksyonaryo["katip_m_u_nb_3_count"]
    K2N_K.car_num += diksyonaryo["katip_m_l_nb_1_count"]
    K2N_K.car_num += diksyonaryo["katip_m_l_nb_2_count"]
    K2N_K.car_num += int(diksyonaryo["katip_m_u_nb_0_count"]/2)
    K2N_K.car_num += int(diksyonaryo["katip_m_l_nb_0_count"]/2)
    # Mid Katipunan to Thornton
    K2N_TDrive.car_num += int(diksyonaryo["katip_m_u_nb_0_count"]/2)
    K2N_TDrive.car_num += int(diksyonaryo["katip_m_l_nb_0_count"]/2)
    
    #IMPROVE: Lane 0 is just being divided to Thornton and Top Katipunan Equally
    
    #Top Katipunan to Mid Katipunan
    K_K2S.car_num = diksyonaryo["katip_t_sb_0_count"]
    K_K2S.car_num += diksyonaryo["katip_t_sb_1_count"]
    K_K2S.car_num += diksyonaryo["katip_t_sb_2_count"]
    K_K2S.car_num += diksyonaryo["katip_t_sb_3_count"]
    # Top Katipunan U-turn
    K_Uturn.car_num  = int(diksyonaryo["katip_t_sb_4_count"] * 0.75)
    K_TDrive.car_num = int(diksyonaryo["katip_t_sb_4_count"] * 0.25)
    
    #IMPROVE DISTRIBUTION
    
    # Thornton Drive (Divide divide)
    divide_thornton = int(diksyonaryo["thornton-drive-lower-out_0_count"] / 2)
    mod = diksyonaryo["thornton-drive-lower-out_0_count"] % 2
    TDrive_K.car_num = divide_thornton
    TDrive_K2S.car_num = divide_thornton
    random_number = random.randint(1, 2)
    if random_number == 1:
        TDrive_K.car_num += mod
    else:
        TDrive_K2S.car_num  += mod

    #B.Gonzales to Mid Katipunan
    Gonza_K2S.car_num = diksyonaryo["b.gonzales-road_0_count"]
####B. Gonzales Divide2x
    divide_gonza = int(diksyonaryo["b.gonzales-road_1_count"] / 2)
    mod = diksyonaryo["b.gonzales-road_1_count"] % 2
    TDrive_K.car_num = divide_gonza
    TDrive_K2S.car_num = divide_gonza
    random_number = random.randint(1, 7)
    if random_number == 1:
        # B.Gonzales to Top Katipunan
        Gonza_K2S.car_num += mod
    else:
        # B.Gonzales to Thornton Drive
        Gonza_TDrive.car_num += mod
    # From Mid Katipunan to Bottom Katipunan
    K2S_K3.car_num  = diksyonaryo["katip_m_sb_0_count"]
    K2S_K3.car_num += diksyonaryo["katip_m_sb_1_count"]
    K2S_K3.car_num += diksyonaryo["katip_m_sb_2_count"]
    # From Mid Katipunan to University Drive
    K2S_URd.car_num = diksyonaryo["katip_m_sb_3_count"]
    # From Mid Katipunan U-turn
    K2S_K2N.car_num = diksyonaryo["katip_m_sb_4_count"]#
########University Road Upper Out Divide2x
    divide_urduo = int(diksyonaryo["univ-road-upper-out_0_count"] / 2)
    mod = diksyonaryo["univ-road-upper-out_0_count"] % 2
    URd_K2N.car_num = divide_urduo
    URd_K3.car_num = divide_urduo
    random_number = random.randint(1, 2)
    if random_number == 1:
        # University Road Upper Out to Mid Katipunan
        URd_K2N.car_num += mod
    else:
        # University Road Upper Out to Bottom Katipunan
        URd_K3.car_num  += mod
    # University Road Lower Out
    URd_K3.car_num += diksyonaryo["univ-road-lower-out_0_count"]
    # F.delaRosa to Mid Katip
    FDRosa_K2N.car_num = diksyonaryo["f.dela-rosa-road_1_count"]
######## F.delaRosa Divide2x
    divide_frosa = int(diksyonaryo["f.dela-rosa-road_0_count"] / 2)
    mod = diksyonaryo["f.dela-rosa-road_0_count"] % 2
    FDRosa_URd.car_num = divide_frosa
    FDRosa_K3.car_num = divide_frosa
    random_number = random.randint(1, 7)
    if random_number == 1:
        # F.delaRosa to University Road
        FDRosa_URd.car_num += mod
    else:
        # F.delaRosa to Bottom Katipunan
        FDRosa_K3.car_num += mod
    #did not include these v since exit node
    #'katip_b_sb_0_count': 4, 'katip_b_sb_1_count': 3, 'katip_b_sb_2_count': 7, 'katip_b_sb_3_count': 0, 'katip_b_sb_4_count': 0,

    # Bottom Katipunan to Mid Katipunan
    K3_K2N.car_num = diksyonaryo["katip_b_nb_1_count"]
    K3_K2N.car_num += diksyonaryo["katip_b_nb_2_count"]
    K3_K2N.car_num += int(diksyonaryo["katip_b_nb_0_count"] * 0.7)
    # Bottom Katipunan to Urd
    K3_URd.car_num = int(diksyonaryo["katip_b_nb_0_count"] * 0.3)
    Unassert()  # This happens only once
    x = int(15) #This is the minimum green time
    Save_Original_State()
    if phase == "phase 1":
        Phase_1()
        print(f"THIS IS P1")
        for i in range(len(Roads)):
            if Roads[i].busy == 1: 
                print(f"Number of cars in", Roads[i].name, ":", Roads[i].car_num)
        if (past_phases[1] == 15 and past_phases[2] == 15 and past_phases[3] == 15):
            return int(160)
        if (K_K2S.car_num <= 12 and K2N_K.car_num <= 12 and K2N_TDrive.car_num <= 12 and K2S_K3.car_num <= 12 and K3_K2N.car_num <= 12 and K3_URd.car_num <= 12):
            past_phases[0] = x
            return x
        past_phases[0] = optimization_loop(3)
        return past_phases[0]
        past_phase[0] = optimization_loop(3)
    elif phase =="phase 2":
        Phase_2()
        print("THIS IS P2")
        for i in range(len(Roads)):
            if Roads[i].busy == 1: 
                print(f"Number of cars in", Roads[i].name, ":", Roads[i].car_num)
        if (past_phases[0] == 15 and past_phases[2] == 15 and past_phases[3] == 15):
            return int(70)
        if (Gonza_K.car_num <= 12) and (Gonza_K2S.car_num <= 12) and (URd_K3.car_num <= 12) and (FDRosa_K2N.car_num <= 12) and (FDRosa_K3.car_num <= 12) and (FDRosa_URd.car_num <= 12):
            past_phases[1] = x            
            return x
        past_phases[1] = optimization_loop(3)
        return past_phases[1]
    elif phase == "phase 3":
        Phase_3()
        print("THIS IS P3")
        for i in range(len(Roads)):
            if Roads[i].busy == 1: 
                print(f"Number of cars in", Roads[i].name, ":", Roads[i].car_num)
        if (past_phases[0] == 15 and past_phases[1] == 15 and past_phases[3] == 15):
            return int(75)
        if (TDrive_K2S.car_num <= 12 and TDrive_K.car_num <= 12 and URd_K3.car_num <= 12 and URd_K2N.car_num <= 12):
            past_phases[2] = x
            return x
        past_phases[2] = optimization_loop(3)
        return past_phases[2]
    elif phase == "phase 4":
        Phase_4()
        print("THIS IS P4")
        for i in range(len(Roads)):
            if Roads[i].busy == 1: 
                print(f"Number of cars in", Roads[i].name, ":", Roads[i].car_num)
        if (past_phases[0] == 15 and past_phases[1] == 15 and past_phases[2] == 15):
            return int(160)
        if (K_Uturn.car_num <= 12 and K_K2S.car_num <= 12 and K_TDrive.car_num <= 12 and K2S_URd.car_num <= 12 and K2S_K2N.car_num <= 12 and K2S_K3.car_num <= 12):
            past_phases[3] = x
            return x
        past_phases[3] = optimization_loop(3)
        return past_phases[3]
car_num_list = []

def Save_Original_State():
    for i in range(len(Roads)):
        car_num_list.append(Roads[i].car_num)
        
def Restore_Original_State():
    for i in range(len(Roads)):
        Roads[i].car_num = car_num_list[i]
    
 

def target_function(train_greentime):
    # Standardize the input data
    mu = train_greentime.mean()
    sigma = train_greentime.std()
    std_train_greentime = (train_greentime - mu) / sigma
    Evaluate_Busy(train_greentime)
    global Cars_Passed
    try:
        flow_rate = (Cars_Passed.item() / std_train_greentime) + (std_train_greentime/100)
    except:
        flow_rate = (Cars_Passed / std_train_greentime) + (std_train_greentime/100)
    #print("Total Flow Rate:" + str(flow_rate))
    Cars_Passed = 0
    return flow_rate.unsqueeze(-1)


def generate_initial_data(n):  # This function generates the base data needed
    train_greentime = torch.rand((n, 1), dtype=torch.float64)  # for bayesian optimization
    exact_obj = target_function(train_greentime)
    best_flowrate = exact_obj.max().item()
    return train_greentime, exact_obj.squeeze(-1), best_flowrate


def optimize_function(init_greentime, init_flowrate, best_flowrate, bnds, npts):
    single_model = SingleTaskGP(init_greentime, init_flowrate)
    mll = ExactMarginalLogLikelihood(single_model.likelihood, single_model)
    fit_gpytorch_model(mll)
    EI = qExpectedImprovement(single_model, best_flowrate)
    candidates, _ = optimize_acqf(
        acq_function=EI,
        bounds=bnds,  # bounds
        q=npts,  # Number of points we times we want to be suggested
        num_restarts=500,  # Increase the number of restarts
        raw_samples=1024,  # Increase the number of raw samples
        options={"batch_limit": 5, "maxiter": 200}
    )
    return candidates

def optimization_loop(loops):
    print(f"inside optimization loop, will start now!")
    init_greentime, init_flowrate, best_flowrate = generate_initial_data(10)
    bnds = torch.tensor([[15.0], [120.0]], dtype=torch.float32)
    for i in range(loops):
        print(f"Number of optimization run: {i+1}")
        new_candidates = optimize_function(init_greentime, init_flowrate, best_flowrate, bnds, 1)
        new_results = target_function(new_candidates).unsqueeze(-1)

        print(f"The new best Green Time Candidate is: {new_candidates.item()}")
        init_greentime = torch.cat([init_greentime, new_candidates])
        init_flowrate = target_function(init_greentime).squeeze(-1)
        best_flowrate = init_flowrate.max().item()

        print(f"Best Flow Rate Is: {best_flowrate}")
    car_num_list= []
    return new_candidates.item()


# print("HOY ITO NA GREENTIME")
# print(helper_function(for_helper_phase,for_helper_dictionary))


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
    edge_list = traci.edge.getIDList()
    lane_list = traci.lane.getIDList()
    output_list = []
    road_list = {
        "katip_t_nb": ['R1', 'R2', 'R3'],
        "katip_t_sb": ['L1'],
        "thornton_nb": ['thornton-drive-extension-outward', 'thornton-drive-upper-out'],
        "thornton_sb": ['thornton-drive-extension-outward', 'thornton-drive-lower-out'],
        "thornton_in": ['thornton-drive-in', 'thornton-drive-extension-towards'],
        "bgon": ['b.gonzales-extension-road', 'b.gonzales-road'],
        "katip_m_nb": ['R4', 'R5', 'R6'],
        "katip_m_sb": ['L2', 'L3', 'L4', 'L5', 'L6'],
        "univrd_t_out": ['univ-road-upper-out'],
        "univrd_t_in": ['univ-road-upper-in'],
        "univrd_b_out": ['univ-road-lower-out'],
        "univrd_b_in": ['univ-road-lower-in'],
        "fdrosa": ['f.dela-rosa-extension-road', 'f.dela-rosa-road'],
        "katip_b_nb": ['R7'],
        "katip_b_sb": ['L7', 'L8', 'L9', 'L10', 'L11', 'L12']
    }
    # road_position_direction_lanenum : smaller lanes part of that lane
    lane_dict = {
        "katip_t_nb_0": ['R1_0', 'R2_0'],
        "katip_t_nb_1": ['R1_1', 'R2_1'],
        "katip_t_nb_2": ['R1_2', 'R2_2'],
        "katip_t_nb_3": ['R1_3', 'R2_3'],
        "katip_t_sb_0": ['L1_0'],
        "katip_t_sb_1": ['L1_1'],
        "katip_t_sb_2": ['L1_2'],
        "katip_t_sb_3": ['L1_3'],
        "katip_t_sb_4": ['L1_4'],
        "thornton-drive-lower-out_0": ['thornton-drive-lower-out_0'],
        "thornton-drive-in_0": ['thornton-drive-in_0'],
        "katip_m_u_nb_0": ['R4_0'],
        "katip_m_u_nb_1": ['R4_1'],
        "katip_m_u_nb_2": ['R4_2'],
        "katip_m_u_nb_3": ['R4_3'],
        "katip_m_l_nb_0": ['R5_0', 'R6_0'],
        "katip_m_l_nb_1": ['R5_1', 'R6_1'],
        "katip_m_l_nb_2": ['R5_2', 'R6_2'],
        "b.gonzales-road_0" : ['b.gonzales-road_0'],
        "b.gonzales-road_1" : ['b.gonzales-road_1'],
        "katip_m_sb_0": ['L2_0','L3_0','L4_0','L5_0','L6_0'],
        "katip_m_sb_1": ['L2_1','L3_1','L4_1','L5_1','L6_1'],
        "katip_m_sb_2": ['L2_2','L3_2','L4_2','L5_2','L6_2'],
        "katip_m_sb_3": ['L2_3','L3_3','L4_3','L5_3','L6_3'],
        "katip_m_sb_4": ['L2_4','L3_4','L4_4','L5_4','L6_4'],
        "univ-road-upper-out_0" : ['univ-road-upper-out_0'],
        "univ-road-upper-in_0" : ['univ-road-upper-in_0'],
        "univ-road-lower-out_0" : ['univ-road-lower-out_0'],
        "univ-road-lower-in_0" : ['univ-road-lower-in_0'],
        "f.dela-rosa-road_1" : ['f.dela-rosa-road_1'],
        "f.dela-rosa-road_0" : ['f.dela-rosa-road_0'],
        "katip_b_sb_0": ['L7_0','L8_0','L9_0','L10_0','L11_0','L12_0'],
        "katip_b_sb_1": ['L7_1','L8_1','L9_1','L10_1','L11_1','L12_1'],
        "katip_b_sb_2": ['L7_2','L8_2','L9_2','L10_2','L11_2','L12_2'],
        "katip_b_sb_3": ['L7_3','L8_3','L9_3','L10_3','L11_3','L12_3'],
        "katip_b_sb_4": ['L7_4','L8_4','L9_4','L10_4','L11_4','L12_4'],
        "katip_b_nb_0": ['R7_0'],
        "katip_b_nb_1": ['R7_1'],
        "katip_b_nb_2": ['R7_2']
    }
    lane_veh_count_dict = {key + "_count": 0 for key in lane_dict}
    
    for lane in lane_list:
        lane_veh_count = traci.lane.getLastStepHaltingNumber(lane)
        for key, value in lane_dict.items():
            if lane in value:
                lane_veh_count_dict[str(key + "_count")] += lane_veh_count
                break
    #print(lane_veh_count_dict)
    
    return lane_veh_count_dict


def run():

    step = 0

    old_kuf_phase = 0
    old_kbt_phase = 0
    while traci.simulation.getMinExpectedNumber() > 0:
        
        if(traci.trafficlight.getPhase("kuf") in [0,3,6,9]):
            kuf_phase = traci.trafficlight.getPhase("kuf")
            kuf_phase_name = traci.trafficlight.getPhaseName("kuf")
        if(kuf_phase != old_kuf_phase):
            print("CURRENT PHASE AND NAME FOR KUF: " + str(kuf_phase) + " : " + str(kuf_phase_name))    

            vehicle_count_dict = getLaneParams()
            print(f"bianckkks")
            print(vehicle_count_dict)
            kuf_phase_name = traci.trafficlight.getPhaseName("kuf")
            print(f"kuf_phase_name is: " + kuf_phase_name)
            print(f"calling helper function now!")
            greentime = helper_function(kuf_phase_name,vehicle_count_dict)
            print(f"greentime returned by helper_function! green time is: " + str(greentime) + str(type(greentime)))

            traci.trafficlight.setPhaseDuration("kuf", greentime)   
            traci.trafficlight.setPhaseDuration("kbt", greentime)   
            
            print(f"Phase and Duration for KUF: " + str(traci.trafficlight.getPhaseName("kuf"))+ ", "+str(traci.trafficlight.getPhaseDuration("kuf")) )
            print(f"Phase and Duration for KBT: " + str(traci.trafficlight.getPhaseName("kbt"))+ ", "+str(traci.trafficlight.getPhaseDuration("kbt")) )

            #this tracks green changes in KUF
        old_kuf_phase = kuf_phase
        traci.simulationStep() # move one second in simulation
        

    traci.close()
    sys.stdout.flush()



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
    #getLaneParams()
    
    with warnings.catch_warnings():
        warnings.filterwarnings('ignore')
        run()