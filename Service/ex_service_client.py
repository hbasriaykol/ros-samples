#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: hbasriaykol

import rospy
from rospy_tutorials.srv import AddTwoInts


def service_client():
    """
    This function sends a request to add two numbers.
    """
    try:
        client = rospy.ServiceProxy("/a_service_name", AddTwoInts)
        rospy.loginfo(client(2, 6))
        rospy.sleep(1)
    except rospy.ServiceException as e:
        rospy.logwarn("Service failed: " + str(e))


if __name__ == '__main__':
    rospy.init_node("a_node_name_5")
    rospy.wait_for_service("/a_service_name")
    service_client()
