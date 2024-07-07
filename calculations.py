# Import `FEModel3D` from `PyNite`
from PyNite import FEModel3D
from matplotlib.figure import Figure


def calculate_beam(N1, N2, load):
    # Create a new finite element model
    beam = FEModel3D()

    # Add nodes (14 ft = 168 inches apart)
    beam.add_node('N1', N1, 0, 0)
    beam.add_node('N2', N2, 0, 0)

    # Define a material
    E = 29000       # Modulus of elasticity (ksi)
    G = 11200       # Shear modulus of elasticity (ksi)
    nu = 0.3        # Poisson's ratio
    rho = 2.836e-4  # Density (kci)
    beam.add_material('Steel', E, G, nu, rho)

    # Add a beam with the following properties:
    # Iy = 100 in^4, Iz = 150 in^4, J = 250 in^4, A = 20 in^2
    beam.add_member('M1', 'N1', 'N2', 'Steel', 100, 150, 250, 20)

    # Provide simple supports
    beam.def_support('N1', True, True, True, False, False, False)
    beam.def_support('N2', True, True, True, True, False, False)

    # Add a uniform load of 200 lbs/ft to the beam (from 0 in to 168 in)
    beam.add_member_dist_load('M1', 'Fy', load, load, N1, N2)

    return beam

def plot_results(array):
    fig = Figure()
    ax = fig.gca()

    #Plot beam line
    ax.plot(array[0], [0]*len(array[0]), color='k')
    ax.plot(array[0], array[1], color='red')

    return fig