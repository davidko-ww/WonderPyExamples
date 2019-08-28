import sys
import WonderPy.core.wwMain


class MyClass(object):

    def on_sensors(self, robot):
        print('({}, {}, {}) ({}, {}, {})'.format(
            robot.sensors.attitude.roll, 
            robot.sensors.attitude.pitch,
            robot.sensors.attitude.slope,
            robot.sensors.attitude.roll_type,
            robot.sensors.attitude.pitch_type,
            robot.sensors.attitude.slope_type))

if __name__ == "__main__":
    WonderPy.core.wwMain.start(MyClass())
