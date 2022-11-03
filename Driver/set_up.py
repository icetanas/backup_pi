import odrive
from odrive.enums import *

odrv0 = odrive.find_any()
print(odrv0)
odrv0.axis1.motor.config.current_lim = 6
odrv0.axis1.controller.config.vel_limit = 14
odrv0.axis1.motor.config.calibration_current = 1
odrv0.axis1.motor.config.pole_pairs = 15
odrv0.axis1.motor.config.torque_constant = 0.27566667
odrv0.axis1.motor.config.motor_type=MOTOR_TYPE_HIGH_CURRENT

odrv0.axis1.encoder.config.mode = ENCODER_MODE_HALL
odrv0.axis1.encoder.config.cpr = 90
odrv0.axis1.encoder.config.calib_scan_distance = 150
odrv0.axis1.encoder.config.bandwidth = 100
odrv0.axis1.controller.config.pos_gain = 1
odrv0.axis1.controller.config.vel_gain = 0.02 * odrv0.axis1.motor.config.torque_constant * odrv0.axis1.encoder.config.cpr
odrv0.axis1.controller.config.vel_integrator_gain = 0.1 * odrv0.axis1.motor.config.torque_constant * odrv0.axis1.encoder.config.cpr
odrv0.axis1.controller.config.vel_limit = 10
odrv0.axis1.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE
odrv0.axis1.controller.config.control_mode = CONTROL_MODE_VELOCITY_CONTROL


