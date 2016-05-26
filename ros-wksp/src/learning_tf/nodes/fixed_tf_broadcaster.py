#!/usr/bin/env python

import roslib
roslib.load_manifest('learning_tf')
import rospy
import tf
import math

# Making a new frame
if __name__ == '__main__':
	# Making a broadcasting node
	rospy.init_node('my_tf_broadcaster')
	br = tf.TransformBroadcaster()

	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		#create a new transform from turtle1 to carrot 1
		#carrot1 is 2 metres offset from turtle1
		# in place
		# br.sendTransform(
		# 	(0.0, 2.0, 0.0),
		# 	(0.0, 0.0, 0.0, 1.0),
		# 	rospy.Time.now(),
		# 	"carrot1",
		# 	"turtle1"
		# )
		
		# not in place
		t = rospy.Time.now().to_sec() * math.pi
		br.sendTransform(
        	(2.0 * math.sin(t), 2.0 * math.cos(t), 0.0), 
        	(0.0, 0.0, 0.0, 1.0), 
        	rospy.Time.now(), 
        	"carrot1", 
        	"turtle1")
		
		rate.sleep()