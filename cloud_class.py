# -*- coding: utf-8 -*-
"""
Last updated: 4/3/24
"""

import numpy as np

class cloud:
    """
    Cloud density should be drawn in relation to the prevalance of
    different cloud varieties in the sky. Cloud volume distribution
    needs real-world data to support the mean and standard deviation used.
    """
    
    density = 1 # kgm^-3
    
    def __init__(self, max_radial_coord):
        """
        r and theta drawn from uniform distributions, creating
        clouds enclosed within the specified radius of sky.
        """
        self.volume = np.random.normal(10**9, 5*10**8) # m^3
        self.r_coord = np.random.uniform(0, max_radial_coord) # m
        self.theta_coord = np.random.uniform(0, 2*np.pi)
        
    def initial_cartesian_position(self):
        x = self.r_coord*np.cos(self.theta_coord) # m
        y = self.r_coord*np.sin(self.theta_coord) # m
        return [x,y]
    
    def mass(self):
        return cloud.density*self.volume # kg
        
def generate_initial_clouds(ring_radius):
    """
    Cloud num should be made random later
    """
    cloud_num = 5
    cloud_array = np.zeros(cloud_num, dtype="object")
    for i in range(cloud_num):
        cloud_array[i] = cloud(ring_radius)
    return cloud_array

# Test
clouds = generate_initial_clouds(10**3)
for i in clouds:
    x_init, y_init = i.initial_cartesian_position()
    print("Cloud of mass {0:.3g} kg at [{1}, {2}]".format(
        i.mass(), x_init, y_init) + "\n")
        
        