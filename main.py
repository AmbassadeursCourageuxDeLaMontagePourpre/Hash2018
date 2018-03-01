import solver
import sys 

#files = ["a_example.in", "b_should_be_easy.in", "c_no_hurry.in", "d_metropolis.in", "e_high_bonus.in"]
files = ["a_example.in"]
#files = ["a_example.in"]
for f in files:
  solver.solver_heuristic('examples/'+f)

