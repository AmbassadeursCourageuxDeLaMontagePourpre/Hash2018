from model import * 
from helping import *

"""
Fonction qui résout le problème
de façon greedy selon le temps
"""
def solver_greedy_time(filename):
  data = get_input(filename)
  rides = data['rides']
  vehicules = data['n_vehicles']
  distributions = [[] for _ in range(vehicules)]

  new_rides = sorted(rides, key=lambda x: x.earliest_start)

  cpt = 0
  for ride in new_rides:
    if cpt == vehicules:
      cpt = 0
    distributions[cpt].append(ride.id)
    cpt+=1

  write_distributions(distributions, filename)
