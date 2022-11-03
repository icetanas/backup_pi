import odrive
from odrive.enums import *
import time

odrv0 = odrive.find_any()
print(odrv0)

odrv0.axis1.requested_state = AXIS_STATE_IDLE

for i in range(50):
	print("Encoder Position:",odrv0.axis1.encoder.pos_estimate)
	print("Encoder Velocity:",odrv0.axis1.encoder.vel_estimate)
	time.sleep(0.5)
