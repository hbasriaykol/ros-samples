#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: hbasriaykol

import rospy
from std_msgs.msg import Int64


def create_publisher():
    """
    This function creates a publisher and determines some parameters.
    """
    pub = rospy.Publisher("/number", Int64, queue_size=10)
    rospy.set_param("/number_publish_frequency", 2)
    pub_freq = rospy.get_param("/number_publish_frequency")
    rate = rospy.Rate(pub_freq)
    
    rospy.set_param("/number_to_publish",3)
    number = rospy.get_param("/number_to_publish")
    rospy.set_param("/try_param", "what's up")
    
    while not rospy.is_shutdown():
        msg = Int64()
        msg.data = number
        pub.publish(msg)
        rate.sleep()


if __name__ == '__main__':
    rospy.init_node("a_node_name_6")
    create_publisher()
