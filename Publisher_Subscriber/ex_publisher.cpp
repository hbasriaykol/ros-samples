#include <ros/ros.h>
#include <std_msgs/String.h>

int main(int argc, char **argv)
{
	ros::init(argc, argv, "a_node_name_2");
	ros::NodeHandle nh;

	ros::Publisher pub = nh.advertise<std_msgs::String>("/a_topic_name",10);

	ros::Rate rate(3);

	while(ros::ok())
	{
		std_msgs::String msg;
		msg.data = "Hi, this is a publisher";
		pub.publish(msg);
		rate.sleep();
	}
}
