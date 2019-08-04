#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: hbasriaykol

import rospy
from rospy_tutorials.srv import AddTwoInts


def handle_add_two_ints(req):
    """
    This function is a callback function which adds two numbers.

    Returns sum of two numbers.
    """
    result = req.a + req.b
    rospy.loginfo(str(req.a) + " + " + str(req.b) + " = " + str(result))
    return result


def service_server():
    """
    The function responds to requests.
    """
    service = rospy.Service("/a_service_name", AddTwoInts, handle_add_two_ints)
    rospy.loginfo("Service server has been started")


if __name__ == '__main__':
    rospy.init_node("a_node_name_4")
    service_server()
    rospy.spin()
