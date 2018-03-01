"""
Fonction qui permet de parser
l'entrée et renvoie la data
"""

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
    self.distance = abs(end_x - start_x) + abs(end_y - start_y)

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
    i += 1
    l = line.split()
    data['rides'].append(Ride(i, int(l[0]), int(l[1]), int(l[2]), int(l[3]), int(l[4]), int(l[5])))
  return data


  
