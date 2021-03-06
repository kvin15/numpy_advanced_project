# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

def get_total_deliveries_played(s_batsman):
    i_deliveries_played = len(ipl_matches_array[ipl_matches_array[:,13]==s_batsman])
    return i_deliveries_played
