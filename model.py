"""
Fonction qui permet de parser
l'entrée et renvoie la data
"""

class Ride:
  def __init__(self, start_x, start_y, end_x, end_y, earliest_start, latest_finish):
    self.start_x = start_x
    self.start_y = start_y
    self.end_x = end_x
    self.end_y = end_y
    self.earliest_start = earliest_start
    self.latest_finish = latest_finish

def get_input(filename):
  f = open(filename, 'r')
  data = {}
  data['rows'] = int(f.readline().strip())
  data['columns'] = int(f.readline().strip())
  data['n_vehicles'] = int(f.readline().strip())
  data['n_rides'] = int(f.readline().strip())
  data['bonus'] = int(f.readline().strip())
  data['n_step'] = int(f.readline().strip())

  data['rides'] = []
  for line in f:
    l = line.split()
    for i in l:
    

  
  return data
  
