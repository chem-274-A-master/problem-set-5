"""
Monte Carlo Simulation package
"""

import os
import random
import math
import numpy as np
from copy import deepcopy


def calculate_LJ(r_ij):
    """
    The LJ interaction energy between two particles.

    Computes the pairwise Lennard Jones interaction energy based on the separation distance in reduced units.

    Parameters
    ----------
    r_ij : float
        The distance between the particles in reduced units.

    Returns
    -------
    pairwise_energy : float
        The pairwise Lennard Jones interaction energy in reduced units.

    """

    r6_term = math.pow(1 / r_ij, 6)
    r12_term = math.pow(r6_term, 2)

    pairwise_energy = 4 * (r12_term - r6_term)

    return pairwise_energy


def generate_random_coordinates(num_atoms, density):
    """
    Generate random coordinates in a box.

    Parameters
    ----------
    num_atoms : int
        The number of atoms to place
    density : float
        The target system density

    Returns
    -------
    coordinates : list
        The generated coordinates
    box_length : float
        The box length for the number of atoms and desired density.
    """

    box_length = math.pow(num_atoms / density, (1 / 3))
    coordinates = []

    for i in range(num_atoms):
        x_val = random.uniform(0, box_length)
        y_val = random.uniform(0, box_length)
        z_val = random.uniform(0, box_length)
        coordinates.append([x_val, y_val, z_val])

    return coordinates, box_length


def calculate_distance(coord1, coord2, box_length=None):
    """
    Calculate the distance between two 3D coordinates.

    Parameters
    ----------
    coord1, coord2: list
        The atomic coordinates

    Returns
    -------
    distance: float
        The distance between the two points.
    """

    distance = 0
    for i in range(3):
        dim_dist = (coord1[i] - coord2[i])

        if box_length:
            dim_dist = dim_dist - box_length * round(dim_dist / box_length)

        dim_dist = dim_dist**2
        distance += dim_dist

    distance = math.sqrt(distance)
    return distance


def calculate_tail_correction(num_particles, box_length, cutoff):
    """
    Calculate the long range tail correction
    """

    const1 = (8 * math.pi * num_particles**2) / (3 * box_length**3)
    const2 = (1 / 3) * (1 / cutoff)**9 - (1 / cutoff)**3

    return const1 * const2


def calculate_total_energy(coordinates, box_length, cutoff):
    """
    Calculate the total Lennard Jones energy of a system of particles.

    Parameters
    ----------
    coordinates : list
        Nested list containing particle coordinates.

    Returns
    -------
    total_energy : float
        The total pairwise Lennard Jones energy of the system of particles.
    """

    total_energy = 0

    num_atoms = len(coordinates)

    for i in range(num_atoms):
        for j in range(i + 1, num_atoms):

            #print(f'Comparings atom number {i} with atom number {j}')

            dist_ij = calculate_distance(coordinates[i],
                                         coordinates[j],
                                         box_length=box_length)

            if dist_ij < cutoff:
                interaction_energy = calculate_LJ(dist_ij)
                total_energy += interaction_energy

    return total_energy


def read_xyz(filepath):
    """
    Reads coordinates from an xyz file.

    Parameters
    ----------
    filepath : str
       The path to the xyz file to be processed.

    Returns
    -------
    atomic_coordinates : list
        A two dimensional list containing atomic coordinates
    """

    with open(filepath) as f:
        box_length = float(f.readline().split()[0])
        num_atoms = float(f.readline())
        coordinates = f.readlines()

    atomic_coordinates = []

    for atom in coordinates:
        split_atoms = atom.split()

        float_coords = []

        # We split this way to get rid of the atom label.
        for coord in split_atoms[1:]:
            float_coords.append(float(coord))

        atomic_coordinates.append(float_coords)

    return atomic_coordinates, box_length


def accept_or_reject(delta_e, beta):
    """
    Accept or reject based on change in energy and temperature.
    """

    if delta_e <= 0:
        accept = True
    else:
        random_number = random.random()
        p_acc = math.exp(-beta * delta_e)

        if random_number < p_acc:
            accept = True
        else:
            accept = False

    return accept


def calculate_pair_energy(coordinates, i_particle, box_length, cutoff):
    """
    Calculate the interaction energy of a particle with its environment (all other particles in the system)


    Parameters
    ----------
    coordinates : list
        The coordinates for all the particles in the system.

    i_particle : int
        The particle index for which to calculate the energy.

    box_length : float
        The length of the simulation box.

    cutoff : float
        The simulation cutoff. Beyond this distance, interactions are not calculated

    Returns
    -------
    e_total : float
        The pairwise interaction energy of the i-th particle with all other particles in the system.

    """

    e_total = 0

    i_position = coordinates[i_particle]

    num_atoms = len(coordinates)

    for j_particle in range(num_atoms):
        if i_particle != j_particle:
            j_position = coordinates[j_particle]
            rij = calculate_distance(i_position, j_position, box_length)

            if rij < cutoff:
                e_pair = calculate_LJ(rij)
                e_total += e_pair

    return e_total


def run_simulation(coordinates,
                   box_length,
                   cutoff,
                   reduced_temperature,
                   num_steps,
                   max_displacement=0.1,
                   freq=1000):
    """
    Run a Monte Carlo simulation with the specified parameters.
    """
    # Reporting information
    steps = []
    energies = []
    all_coordinates = []

    # Calculated quantities
    beta = 1 / reduced_temperature
    num_particles = len(coordinates)

    # Calculated based on simulation inputs
    total_energy = calculate_total_energy(coordinates, box_length, cutoff)
    total_energy += calculate_tail_correction(num_particles, box_length,
                                              cutoff)

    for step in range(num_steps):

        # 1. Randomly pick one of num_particles particles
        random_particle = random.randrange(num_particles)

        # 2. Calculate the interaction energy of the selected particle with the system. Store this value.
        current_energy = calculate_pair_energy(coordinates, random_particle,
                                               box_length, cutoff)

        # 3. Generate a random x, y, z displacement range (-max_displacement, max_displacement) - uniform distribution
        x_rand = random.uniform(-max_displacement, max_displacement)
        y_rand = random.uniform(-max_displacement, max_displacement)
        z_rand = random.uniform(-max_displacement, max_displacement)

        # 4. Modify the coordinate of selected particle by generated displacements.
        coordinates[random_particle][0] += x_rand
        coordinates[random_particle][1] += y_rand
        coordinates[random_particle][2] += z_rand

        # 5. Calculate the new interaction energy of moved particle, store this value.
        proposed_energy = calculate_pair_energy(coordinates, random_particle,
                                                box_length, cutoff)

        # 6. Calculate energy change and decide if we accept the move.
        delta_energy = proposed_energy - current_energy

        accept = accept_or_reject(delta_energy, beta)

        # 7. If accept, keep movement. If not revert to old position.
        if accept:
            total_energy += delta_energy
        else:
            # Move is not accepted, roll back coordinates
            coordinates[random_particle][0] -= x_rand
            coordinates[random_particle][1] -= y_rand
            coordinates[random_particle][2] -= z_rand

        # 8. Print the energy and store the coordinates at certain intervals
        if step % freq == 0:
            print(step, total_energy / num_particles)
            steps.append(step)
            energies.append(total_energy / num_particles)
            all_coordinates.append(coordinates)

    return coordinates


if __name__ == "__main__":

    # Set simulation parameters
    reduced_temperature = 0.9
    num_steps = 1000
    max_displacement = 0.1
    cutoff = 3
    freq = 100

    # Read initial coordinates
    atomic_coordinates_, box_length_ = generate_random_coordinates(500, 0.009)

    atomic_coordinates_ = np.array(atomic_coordinates_)

    # Run the simulation
    final_coordinates_ = run_simulation(deepcopy(atomic_coordinates_),
                                        box_length_,
                                        cutoff,
                                        reduced_temperature,
                                        num_steps,
                                        freq=freq)
