#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
import math
 
def joint2_controller():
    pub1 = rospy.Publisher('/rrbot/joint1_position_controller/command', Float64, queue_size=10)
    pub2 = rospy.Publisher('/rrbot/joint2_position_controller/command', Float64, queue_size=10)
    rospy.init_node('rrbot_joint_controller', anonymous=False)
    rate = rospy.Rate(50) # 50hz
    count_i = 0.0
    while not rospy.is_shutdown():
        count_i += 1.0
        position1 = (1.0*math.pi/4.0)*math.sin(count_i/90.0)*math.sin(count_i/90.0)
        position2 = (math.pi/4.0)-(1.0*math.pi/4.0)*math.cos(count_i/40.0)*math.cos(count_i/40.0)
        # rospy.loginfo(position1)
        pub1.publish(position1)
        # rospy.loginfo(position2)
        pub2.publish(position2)

        rate.sleep()
 
if __name__ == '__main__':
    try:
        joint2_controller()
    except rospy.ROSInterruptException:
        pass