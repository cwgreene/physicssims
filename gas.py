import numpy
import argparse
import sys

def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("-N", type=float, default=100)
    parser.add_argument("--dt", type=float, default=.01)
    parser.add_argument("--left", type=float, default=0)
    parser.add_argument("--right", type=float, default=1)
    parser.add_argument("--sim-time", type=int, default=1000)
    options = parser.parse_args(args)
    # 1d gas
    # random velocities and positions
    N = options.N
    x = numpy.random.uniform(size=N)
    p = numpy.random.normal(size=N)
    bounds_left = options.left
    bounds_right = options.right
    dt = options.dt
    collisions = 0
    sim_time = options.sim_time
    force = 0
    for i in range(sim_time):
        # Move!
        x = x+p*dt
        # count collisions, and accumulate force
        collisions += numpy.sum(x>bounds_right) + numpy.sum(x<bounds_left)
        force += abs(sum(2*p[x<bounds_left]/dt))
        force += abs(sum(2*p[x>bounds_right]/dt))
        # reflect!
        p[x>bounds_right] = -p[x>bounds_right]
        p[x<bounds_left] = -p[x<bounds_left]
        x[x>bounds_right] = bounds_right - (x[x>bounds_right] - bounds_right)
        x[x<bounds_left] = bounds_left - (x[x<bounds_left] - bounds_left)
    print "Out of bounds:", sum(x<bounds_left) + sum(x>bounds_right)
    kinetic_energy = sum(p**2)/2
    print "Kinetic energy:", sum(p**2)/(2)
    print "Collisions per unit time:", collisions/(dt*sim_time)
    avg_force = force/(sim_time)/2
    print "Average force:", avg_force
    print "ratio:",avg_force/kinetic_energy
main(sys.argv[1:])
