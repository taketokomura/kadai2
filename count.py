#!/usr/bin/env python3 
import rospy 
import rosparam 
from std_msgs.msg import String 

rospy.init_node('count') # ノード名「count」に設定 
pub = rospy.Publisher('count_up', String, queue_size=1) # パブリッシャ「count_up」を作成 
text = rospy.get_param("~content", "default")
rate = rospy.Rate(10) # 10Hzで実行

while not rospy.is_shutdown():
    str = "send: %s" % text 
    rospy.loginfo(str) 
    pub.publish(str) 
    rate.sleep()
