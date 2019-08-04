#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: hbasriaykol

import rospy

if __name__ == '__main__':
    rospy.init_node('a_node_name')
    # This has to be unique or you can add a parameter -> anonymous = True
    rospy.loginfo("This is a node that called a_node_name.")
    rospy.sleep(1)
    rospy.loginfo("Exit now")
