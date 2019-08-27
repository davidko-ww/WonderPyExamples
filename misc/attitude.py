import sys
import WonderPy.core.wwMain


class MyClass(object):

    def on_sensors(self, robot):
        print('({}, {})'.format(robot.sensors.attitude.roll, robot.sensors.attitude.pitch))

if __name__ == "__main__":
    WonderPy.core.wwMain.start(MyClass())
