#!/usr/bin/env python
import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib
from actionlib_msgs.msg import *
from geometry_msgs.msg import Pose, Point, Quaternion
import argparse


point=[(0.0,0),(-0.5,-12), (-0.5, -15), (-0.5, -19), (-4.5,-12), (-4.5, -12), (-4.5, -12), (0, -4)]

def movebase_client(point, i):

    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    #def choi(data):
	    #print("X: "+str(point[data][0]))
	    #print("Y: "+str(point[data][1]))
	
    #data=input()
    #choi(data)
    i = point[i-1]
    goal.target_pose.pose.position.x = i[0] #input("Set your x goal:")
    goal.target_pose.pose.position.y = i[1] #input("Set your x goal:")
    goal.target_pose.pose.orientation.w = 0.5

    client.send_goal(goal)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        return client.get_result()

if __name__ == '__main__':
    try:
        ap = argparse.ArgumentParser()
        ap.add_argument("-p", "--point", type=int, required=True,
	    help="point de destination")
        args = vars(ap.parse_args())
        rospy.init_node('movebase_client_py')
        result = movebase_client(point, args['point'])
        if result:
            rospy.loginfo("Destination reached sucsufuly!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")