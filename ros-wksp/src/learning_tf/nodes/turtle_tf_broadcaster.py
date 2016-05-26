#!/usr/bin/env python
import roslib
roslib.load_manifest('learning_tf') #loads from package.xml
import rospy
import tf
import turtlesim.msg

def handle_turtle_pose(msg, turtlename):
	br = tf.TransformBroadcaster()
	br.sendTransform((msg.x, msg.y, 0), tf.transformations.quaternion_from_euler(0, 0, msg.theta),
		rospy.Time.now(),
		turtlename,
		'world')

if __name__ == '__main__':
	rospy.init_node('turtle_tf_broadcaster')
	turtlename = rospy.get_param('~turtle') # from the parameter server- either turtle1 or turtle2 
	# subscribes to 'turtle<#>/pose' 
	# then runs handle_turtle_pose  on every message
	rospy.Subscriber("/%s/pose" % turtlename, turtlesim.msg.Pose, handle_turtle_pose, turtlename)
	# subscriber( topic name, data class, callback, callback_arguments )
	rospy.spin()
