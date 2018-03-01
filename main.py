import solver
import sys 

files = ["a_example.in", "b_should_be_easy.in", "c_no_hurry.in", "d_metropolis.in", "e_high_bonus.in"]
for f in files:
  solver.solver_greedy_time('examples/'+f)
