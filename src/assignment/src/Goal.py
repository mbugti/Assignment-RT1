#!/usr/bin/env python
import rospy
import actionlib
from geometry_msgs.msg  import Twist, , Point, Quaternion
from nav_msgs.msg import Odometry
from math import pow,atan2,sqrt

class turtlebot():
    """
    Documentation of class
    
    More details
    """
    
    def __init__(self):        
        """
	    Initializes the node
	    Publish to a topic "/cmd_vel"
	    Subscribe to a topic "/odom" and calls a "callback" function
	    """
        
        rospy.init_node('turtlebot_controller', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber('/odom', Odometry, self.callback)
        self.pose = Pose()
        self.rate = rospy.Rate(10)

 
    def callback(self, data):       
        """
	    After being called by the subscriber 
	    Returns:
	           Implement the recieved pose values
	    """

        self.pose = data
        self.pose.x = round(self.position.x, 4)
        self.pose.y = round(self.position.y, 4)

    def get_distance(self, goal_x, goal_y):
        distance = sqrt(pow((goal_x - self.pose.x), 2) + pow((goal_y - self.pose.y), 2))
        return distance

    def move2goal(self):
        """"
	    This functions behaves as a Proportional controller
	    Set the linear velocity in X-axis and y-axis
	    Publish a message
	    Return:
	          Stop the robot after the movement is over
	    """

        goal_pose = Odometry()
        goal_pose.x = input("Set x goal:")
        goal_pose.y = input("Set y goal:")
        distance_tolerance = input("Set your tolerance:")
        vel_msg = Twist()


        while sqrt(pow((goal_pose.x - self.pose.x), 2) + pow((goal_pose.y - self.pose.y), 2)) >= distance_tolerance:

\
            vel_msg.linear.x = 1.5 * sqrt(pow((goal_pose.x - self.pose.x), 2) + pow((goal_pose.y - self.pose.y), 2))
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0


            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
   
            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()


        vel_msg.linear.x = 0
        vel_msg.angular.z =0
        self.velocity_publisher.publish(vel_msg)

        rospy.spin()

if __name__ == '__main__':
    try:
        x = turtlebot()
        x.move2goal()

    except rospy.ROSInterruptException: pass

