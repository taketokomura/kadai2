#!/usr/bin/env python3 
import rospy 
from std_msgs.msg import String 
def cb(message): 
    rospy.loginfo("recieved %s", message.data) 
    now = rospy.Time.now() 
    rospy.loginfo("now: %f", now.to_sec()) 
    rospy.loginfo("five: %f", now.to_sec()*5)

if __name__ == '__main__': 
    rospy.init_node('twice') 
    sub = rospy.Subscriber('count_up', String, cb) 
    rospy.spin()
