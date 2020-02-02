#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
import math
 
def joint2_controller():
    pub = rospy.Publisher('/rrbot/joint2_position_controller/command', Float64, queue_size=10)
    rospy.init_node('joint2_controller', anonymous=False)
    rate = rospy.Rate(10) # 10hz
    count_i = 0.0
    while not rospy.is_shutdown():
        count_i += 1.0
        position = (math.pi/4)+(1*math.pi/4)*math.sin(count_i/20.0)*math.sin(count_i/20.0)
        # rospy.loginfo(position)
        pub.publish(position)
        rate.sleep()
 
if __name__ == '__main__':
    try:
        joint2_controller()
    except rospy.ROSInterruptException:
        pass