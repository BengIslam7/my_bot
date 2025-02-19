#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import os

class Control(Node):
    def __init__(self):
        super().__init__("control_node") # Node name
        self.get_logger().info("Control Node")
        # Include the motor control pins
        self.subscription = self.create_subscription(Twist,'/cmd_vel',self.control_callback,10)
    def control_callback(self, msg):
        
        self.get_logger().info(f"Received Twist message: linear=({msg.linear.x}, {msg.linear.y}, {msg.linear.z}), "
                           f"angular=({msg.angular.x}, {msg.angular.y}, {msg.angular.z})")

        if(msg.angular.z==1.0 and msg.linear.x==0.5):
            self.get_logger().info("FORWARD : RIGHT DIAGONAL")
        elif(msg.angular.z==-1.0 and msg.linear.x==0.5):
            self.get_logger().info("FORWARD : LEFT DIAGONAL")
        elif(msg.linear.x==0.5):
            self.get_logger().info("FORWARD")
            os.system("sudo python3 forward.py")
        elif(msg.angular.z==1.0 and msg.linear.x==-0.5):
            self.get_logger().info("BACKWARD : RIGHT DIAGONAL")
        elif(msg.angular.z==-1.0 and msg.linear.x==-0.5):
            self.get_logger().info("BACKWARD : LEFT DIAGONAL")
        elif(msg.linear.x==-0.5):
            self.get_logger().info("BACKWARD")
            os.system("sudo python3 forward.py")            
        elif(msg.angular.z==1.0):
            self.get_logger().info("LEFT")
            os.system("sudo python3 forward.py")
        elif(msg.angular.z==-1.0):
            self.get_logger().info("RIGHT")
            os.system("sudo python3 forward.py")
        else:
            self.get_logger().info("STOP")
        
            

def main (args=None):
    rclpy.init(args=args)
    #Node
    node = Control()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__" :
    main()