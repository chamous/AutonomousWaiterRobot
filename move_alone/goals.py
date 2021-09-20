import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point, Twist
from math import atan2, sqrt
x = 0
y = 0
theta = 0.0
def newOdom(msg):
        global x
        global y
        global theta
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y

        q = (msg.pose.pose.orientation.x,
              msg.pose.pose.orientation.y,
              msg.pose.pose.orientation.z,
              msg.pose.pose.orientation.w)
        euler = euler_from_quaternion(q)
        theta = euler[2]
rospy.init_node("RobotController")
rospy.Subscriber("/odom", Odometry, newOdom)
pub = rospy.Publisher("cmd_vel", Twist, queue_size = 1)
speed = Twist()
r = rospy.Rate(5)

goal = Point()
goal.x = input("Set your x goal:")
goal.y = input("Set your y goal:")
distance= sqrt(pow(goal.x-x,2) + pow(goal.y-y, 2))

inc_x = goal.x-x
inc_y = goal.y-y
angle_to_goal = atan2(inc_y, inc_x)
while abs(angle_to_goal - theta) > 0.1 :
    scale=1.5
    dir=(angle_to_goal-theta) /abs( angle_to_goal-theta)
    angSpeed= min(0.5, abs( angle_to_goal-theta) / scale)
    speed.angular.z = dir*angSpeed
    speed.linear.x = 0
    pub.publish(speed)
    r.sleep()


    speed.angular.z = 0
while distance >= 0.0:
    distance=sqrt(pow(goal.x-x,2) + pow(goal.y-y, 2))
    rospy.loginfo(distance)
    speed.linear.x = 0.5
    speed.angular.z = 0
    pub.publish(speed)
    r.sleep()
    speed.linear.x = 0.0
    speed.angular.z =0.0
    pub.publish(speed)