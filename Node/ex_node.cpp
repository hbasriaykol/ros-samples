#include <ros/ros.h>

int main(int argc, char **argv)

{
	ros::init(argc, argv, "a_node_name"); //#This has to be unique or you can add a parameter ->  ros::init_options::AnonymousName
	ros::NodeHandle nh;
	ROS_INFO("This is a node that called a_node_name");
	ros::Duration(1).sleep();
	ROS_INFO("Exit now");
}
