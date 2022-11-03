import odrive
from odrive.enums import *
from odrive.utils import start_liveplotter
import time

#import matplotlib.pyplot as plt
import numpy as np
try:
    odrv0 = odrive.find_any()
    print("Connected")
except:
    print("shit the bed")
vel = 0.15
P_left = 5
I_left = 60

P_right = 5
I_right = 60

seconds = 8

odrv0.axis0.controller.config.vel_gain = P_left
odrv0.axis1.controller.config.vel_gain = P_right

odrv0.axis0.controller.config.vel_integrator_gain = I_left
odrv0.axis1.controller.config.vel_integrator_gain = I_right


odrv0.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
odrv0.axis0.controller.input_vel=-vel
odrv0.axis1.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
odrv0.axis1.controller.input_vel=vel

vel_data = []
vel_left = []
vel_right = []


for i in range(seconds*4):
    vel_left.append(-odrv0.axis0.encoder.vel_estimate)
    vel_right.append(odrv0.axis1.encoder.vel_estimate)
    if len(vel_left)%4 == 0:
        print(sum(vel_left)/len(vel_left))
        print(sum(vel_right)/len(vel_right))
        print("=========================")
    time.sleep(0.25)

odrv0.axis0.controller.input_vel=0
odrv0.axis0.requested_state = AXIS_STATE_IDLE
odrv0.axis1.controller.input_vel=0
odrv0.axis1.requested_state = AXIS_STATE_IDLE


print(vel_left)
print(vel_right)

#plt.plot(xpoints, np.array(vel_left), color = 'g')
#plt.plot(xpoints, np.array(vel_right), color='r')
#plt.show()
quit()


	
