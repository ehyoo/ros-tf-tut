#!/usr/bin/env python
# this doesn't work
import roslib
roslib.load_manifest('learning_tf')
import rospyrt", "/carrot1", now)
		except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
import math
import tf
import geometry_msgs.msg
import turtlesim.srv

if __name__ == '__main__':
	rospy.init_node('tf_turtle')
	listener = tf.TransformListener()
	rospy.wait_for_service('spawn') 
	spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
	spawner(4, 2, 0, 'robert')
	turtle_vel = rospy.Publisher('robert/cmd_vel', geometry_msgs.msg.Twist, queue_size = 1)
	
	rate = rospy.Rate(10.0) # 10hz
	listener.waitForTransform("/robert", "/carrot1", rospy.Time(), rospy.Duration(4.0))
	while not rospy.is_shutdown():
		try:
			now = rospy.Time.now() - rospy.Duration(5.0)
			listener.waitForTransform("/robert", "/carrot1", now, rospy.Duration(1.0))
			(trans, rot) = listener.lookupTransform("/robert", "/carrot1", now)
		except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
			continue

		angular = 4 * math.atan2(trans[1], trans[0])
		linear = 0.5 * math.sqrt(trans[0] ** 2  + trans[1] ** 2)
		cmd = geometry_msgs.msg.Twist()
		cmd.linear.x = linear
		cmd.angular.z = angular
		turtle_vel.publish(cmd)

		rate.sleep()