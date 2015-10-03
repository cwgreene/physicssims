import numpy
import argparse
import sys

def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("-N", type=float, default=100)
    parser.add_argument("--dt", type=float, default=.01)
    parser.add_argument("--sim-time", type=int, default=1000)
    options = parser.parse_args(args)
    # 1d gas
    # random velocities and positions
    N = options.N
    x = numpy.random.uniform(size=N)
    p = numpy.random.normal(size=N)
    dt = options.dt
    collisions = 0
    sim_time = options.sim_time
    force = 0
    for i in range(sim_time):
        # Move!
        x = x+p*dt
        # count collisions, and accumulate force
        collisions += numpy.sum(x>1) + numpy.sum(x<0)
        force += abs(sum(2*p[x<0]/dt))
        force += abs(sum(2*p[x>1]/dt))
        # reflect!
        p[x>1] = -p[x>1]
        p[x<0] = -p[x<0]
        x[x>1] = 1 - (x[x>1] - 1)
        x[x<0] = -x[x<0]
    print "Out of bounds:", sum(x>1) + sum(x<0)
    kinetic_energy = sum(p**2)/2
    print "Kinetic energy:", sum(p**2)/(2)
    print "Collisions per unit time:", collisions/(dt*sim_time)
    avg_force = force/(sim_time)/2
    print "Average force:", avg_force
    print "ratio:",avg_force/kinetic_energy
main(sys.argv[1:])
