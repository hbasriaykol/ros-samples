#include<ros/ros.h>
#include<std_msgs/String.h>

void callback_function(const std_msgs::String& msg) 
{
	ROS_INFO(msg.data.c_str());
}

int main(int argc, char **argv)
{
	ros::init(argc, argv, "a_node_name_3");
	ros::NodeHandle nh;

	ros::Subscriber sub = nh.subscribe("/a_topic_name", 1000, callback_function);
	ros::spin();
}
