"""
Fonction qui permet de parser
l'entrée et renvoie la data
"""

def distance(x1, y1, x2, y2):
  return abs(x1 - x2) + abs(y1 - y2)

class Ride:
  def __init__(self, id, start_y, start_x, end_y, end_x, earliest_start, latest_finish):
    self.id = id
    self.start_x = start_x
    self.start_y = start_y
    self.end_x = end_x
    self.end_y = end_y
    self.earliest_start = earliest_start
    self.latest_finish = latest_finish
    self.total_time = latest_finish - earliest_start
    self.distance = distance(end_x, end_y, start_x, start_y)
    self.bonus_max = self.distance + (self.latest_finish - (self.earliest_start + self.distance))

def get_input(filename):
  f = open(filename, 'r')
  data = {}
  l1 = f.readline().strip().split()
  
  data['rows'] = int(l1[0])
  data['columns'] = int(l1[1])
  data['n_vehicles'] = int(l1[2])
  data['n_rides'] = int(l1[3])
  data['bonus'] = int(l1[4])
  data['n_step'] = int(l1[5])

  data['rides'] = []
  i = 0
  for line in f:
    l = line.split()
    data['rides'].append(Ride(i, int(l[0]), int(l[1]), int(l[2]), int(l[3]), int(l[4]), int(l[5])))
    i += 1
  return data

"""
Calcul le score d'une ride (bonus et temps)
étant donné une position et un temps
"""
def ride_score(x, y, t, ride, data):
  d1 = distance(x, y, ride.start_x, ride.start_y)
  bonus = data['bonus'] if d1 + t <= ride.earliest_start else 0
  d1 = max(ride.earliest_start, d1) + ride.distance
  bonus += ride.distance if d1 <= ride.latest_finish else 0
  return d1, bonus

"""
étant donné une voiture, et sa liste de ride
on renvoie le bonus
"""
def car_score(data, car):
  """car = liste de id de ride"""
  x, y = 0, 0
  bonus = 0
  t = 0
  for ride_id in car:

    ride = data['rides'][ride_id]
    t, bonus = ride_score(x, y, t, ride, data)
    x, y = ride.end_x, ride.end_y
  return bonus

def score(solution, data):
  s = 0
  for car in solution:
    s += car_score(data, car)
  return s
