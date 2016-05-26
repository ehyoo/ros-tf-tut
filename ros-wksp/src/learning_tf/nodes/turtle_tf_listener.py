#!/usr/bin/env python

import roslib
roslib.load_manifest('learning_tf')
import rospy
import math
import tf
import geometry_msgs.msg
import turtlesim.srv

if __name__ == '__main__':
	rospy.init_node('tf_turtle')
	listener = tf.TransformListener() # receiving transformations, buffers up to 10 seconds
	
	# this block of code uses the Service to make a new turtle
	rospy.wait_for_service('spawn') 
	spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn) # of Spawn server type
	spawner(4, 2, 0, 'robert') # x, y, theta, name (for the turtle)
	turtle_vel = rospy.Publisher('robert/cmd_vel', geometry_msgs.msg.Twist, queue_size = 1)
	# using 'robert' to make a point that any name could be used
	
	rate = rospy.Rate(10.0) # 10hz
	while not rospy.is_shutdown():
		try:
			# lookupTransform(target_frame, source_frame, time) -> (position, quaternion)
			# transform target_frame to source_frame
			# position and quaternion being returned as tuples of 3 and 4 respectively
			# (trans, rot) = listener.lookupTransform('/robert', '/turtle1', rospy.Time(0)) # Time(0) being latest time
			(trans, rot) = listener.lookupTransform('/robert', '/carrot1', rospy.Time(0)) # for carrot demonstration 
		except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
			continue

		angular = 4 * math.atan2(trans[1], trans[0])
		linear = 0.5 * math.sqrt(trans[0] ** 2  + trans[1] ** 2)
		cmd = geometry_msgs.msg.Twist()
		cmd.linear.x = linear
		cmd.angular.z = angular
		turtle_vel.publish(cmd)

		rate.sleep()