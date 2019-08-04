#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: hbasriaykol

import rospy
from std_msgs.msg import String


def create_publisher():
    """
     This function is a publisher node.
    """
    pub = rospy.Publisher("/a_topic_name", String, queue_size=10)
    # publisher(topic_name, msgs_type, queue_size)
    rate = rospy.Rate(2)

    while not rospy.is_shutdown():
        msg = String()
        msg.data = "Hi, this is a publisher."
        pub.publish(msg)
        rate.sleep()


if __name__ == '__main__':
    rospy.init_node('a_node_name_2')
    create_publisher()
    rospy.loginfo("Node was stopped.")
