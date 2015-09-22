import numpy

def main():
    # 1d gas
    # random velocities and positions
    N = 1000
    x = numpy.random.uniform(size=N)
    p = numpy.random.normal(size=N)
    dt = .001
    collisions = 0
    sim_time = 1000
    force = 0
    for i in range(sim_time):
        # Move!
        x = x+p*dt
        # count collisions, and accumulate force
        collisions += sum(x>1) + sum(x<0)
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
main()
