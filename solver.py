from model import * 
from helping import *
import numpy as np

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

  return distributions

"""
Fonction heuristique amélioré
cherchant toujours le plus proche
"""
def solver_heuristic(filename):
  data = get_input(filename)
  vehicules = data['n_vehicles']
  rides = data['rides']
  new_rides = sorted(rides, key=lambda x: x.earliest_start)
  distributions = [[] for _ in range(vehicules)]

  vehicules_states = [[(0, 0), 0] for _ in range(vehicules)]

  # Pour chaque ride
  for ride in new_rides:
    # On calcule pour cette ride, quelle voiture
    # donne le meilleur score en la prenant maintenant
    value_vehicules = [-1 for _ in range(vehicules)]
    for veh in range(vehicules):
      value_vehicules[veh] = ride_score(vehicules_states[veh][0][0], vehicules_states[veh][0][1], vehicules_states[veh][1], ride, data)[1]
    chosen_vehicule = np.argmax(value_vehicules) 
    distributions[chosen_vehicule].append(ride.id)

    # On met à jour l'état du véhicule
    vehicules_states[chosen_vehicule][0] = (ride.end_x, ride.end_y)
    vehicules_states[chosen_vehicule][1] = max(ride.earliest_start, vehicules_states[chosen_vehicule][1]) + ride.distance 

  write_distributions(distributions, filename)
