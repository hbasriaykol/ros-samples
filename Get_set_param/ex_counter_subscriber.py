#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: hbasriaykol

import rospy
from std_msgs.msg import Int64
from std_srvs.srv import SetBool


class NumberCounter:
    """
    This class gets numbers as subscriber
    and sums this numbers then publish the result.
    """
    def __init__(self):
        """
        Creates a publisher, a subscriber and a services.
        """
        self.counter = 0
        self.sub = rospy.Subscriber("/number", Int64, self.callback_function)
        self.pub = rospy.Publisher("/a_new_topic", Int64, queue_size=10)
        self.reset_service = rospy.Service("/reset_counter", SetBool,
                                           self.callback_function_2)

    def callback_function(self, msg):
        """
        This function is a callback function which sums the numbers.
        """
        self.counter += msg.data
        new_msg = Int64()
        new_msg.data = self.counter
        self.pub.publish(new_msg)

    def callback_function_2(self, req):
        """
        This function is a callback function which resets the counter
        """
        if req.data:
            self.counter = 0
            return True, "Counter has been successfully reset"
        return False, "Counter has not been reset"


if __name__ == '__main__':
    rospy.init_node('a_node_name_7')
    NumberCounter()
    rospy.spin()
