# Week 5 Task 3

import numpy as np
import matplotlib.pyplot as plt

# Initialize the physical properties of the system
dt=      # In seconds.
k=1.0   #spring constant in SI units
xeq=0.0 #equilibrium position of the particle on a spring
mass=0.1 # in kg


# The following is the function responsible to compute the elastic force
def felastic(k,xeq,x):
    """
    This function computes the value of the elastic force
    Input arguments:
        k: force constant of the spring; 
        xeq: equilibrium position of the spring;
        x: position of the spring; 
    Output results:
        elastic force
    """
    
    return 


# The following is the function responsible to describe the motion of a single particle during a short timestep
def move(xpos,xvel,xforce,mass):
    """
    This function describes the motion of a single particle subject to a constant force.
    The particle's coordinates are updated according to Euler algorithm. 
    Input arguments:
        dt: timestep; 
        xpos: particle's coordinate along x; 
        xvel: x-component of particle's velocity; 
        xforce: x-component of particle's force; mass: 
        mass of particle.
    Output results:
        update x components of particle's position and velocity
    """
    xpos = xpos + dt*xvel
    xacceleration = 
    xvel = xvel + dt * xacceleration
    
    return xpos,xvel

# Initialize the configuration of the system
# We drag the particle 1m away from it's equilibrium position
# and let go with zero velocity
xpos = 1
xvel = 0
t_range =  


#numerical result
xn = []
for t in t_range:
    force = felastic(k,xeq,xpos)
    xpos,xvel = move(xpos,xvel,force,mass)
    xn.append(xpos)

#analytical result
xa = []
    
fig, ax = plt.subplots(1)
ax.plot(, xn , 'b.', label='Numerical')
ax.plot(, xa , 'r-', label='Analytical')

ax.set_ylim(-2,2)
ax.set_xlim(0,10)
ax.set_xlabel('time (s)')
ax.set_ylabel('x position (m)')
plt.title('Harmonic Motion: Numerical vs Analytic Solution')
plt.show()
