#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: hbasriaykol

import rospy
from std_msgs.msg import String


def callback_function(msg):
    ''' This function is callback function that received a message.'''
    rospy.loginfo(msg)


def create_subscriber():
    ''' This function creates a subscriber. '''
    sub = rospy.Subscriber("/a_topic_name", String, callback_function)


if __name__ == '__main__':
    rospy.init_node('a_node_name_3')
    rospy.spin()
