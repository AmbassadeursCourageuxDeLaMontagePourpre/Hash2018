
"""
Permet d'écrire le tableau des distributions
dans un fichier de sortie
"""
def write_distributions(distributions, filename):
  f = open(filename+'.out', 'w')
  for dis in distributions:
    line = str(len(dis)) + ' '
    for d in dis:
      line += str(d) + ' '
    f.write(line+'\n')
  f.close()
