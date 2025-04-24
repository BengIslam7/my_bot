#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import JointState
import os

class Control(Node):
    def __init__(self):
        super().__init__("control_node") # Node name
        self.get_logger().info("Control Node")
        self.subscription = self.create_subscription(JointState,'/joint_states',self.control_callback,10)
    def control_callback(self, msg):
        self.get_logger().info(f"Received JointState message: names of joints=({msg.name}) velocity=({msg.velocity})")
        right_wheel_vel=round(msg.velocity[2])
        r_right_wheel_vel=round(msg.velocity[3])
        left_wheel_vel=round(msg.velocity[0])
        r_left_wheel_vel=round(msg.velocity[1])
        print("passed value for right wheel : "+str(right_wheel_vel))
        print("passed value for right wheel : "+str(left_wheel_vel))
        os.system("sudo python3 /home/pfe/work/src/my_bot/move.py "+str(left_wheel_vel)+" "+str(right_wheel_vel))

def main (args=None):
    rclpy.init(args=args)
    #Node
    node = Control()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__" :
    main()