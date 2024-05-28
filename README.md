# ssl07-2324
# SmartLight: A Decentralized MPC-based Multi-intersection Traffic Signal Optimization Algorithm

## SIMULATION GUIDE:

To make simulation run with TraCI, make sure to include TraCI-integrated Python Code in the same directory as the SUMO Configuration files.
Then run python file in terminal.
For integrations with BoTorch, make sure to have conda environment.


## VERY RELEVANT FILES:

1. sf_centralized.py
2. sf_decentralized.py
3. collect_hourly_simulated_demand.py
4. performance_indicators.py

These files are already added into SUMO Configuration files due to dependencies.


## GIT GUIDE

An issue with the multiple code revisions ay keeping track of the changes, which is very hard to do kung magssend lang nang magssend ng updated codes.

The repository is reorganized na so that the changes we make with the codes are reflected din in a single source. 

Steps:
0. Have Git installed
1. Clone the Repository
    Once repository is cloned, open the directory on your IDE.
2. Whenever you make changes to the files in the repo do the following:
    git add .
    git commit -m "insert message here, describe the changes you are making"
    git push


This time around we'll be working with the main branch lang. Creating branches would be tricky as all of us are learning Git pa lang. To address this, if major major changes are going to be made with the code, duplicate the file and place it in the proper folder in the repository, then push whatever change you need on the file. 

## Change Log
May 28, 2024; 11:09pm - created a new branch called "ctm". Please commit changes to CTM codes in this branch first and ask another person to check, before committing to the main branch. ~ Myles
