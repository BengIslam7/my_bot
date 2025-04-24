import lgpio
import argparse
import time
ENA = 18
ENB=4
IN3=5
IN4=6
IN1 = 27
IN2 = 22
parser = argparse.ArgumentParser(description="Control robot movement with wheel velocities.")
parser.add_argument("left_velocity", type=int,help="Velocity for the left wheel.")
parser.add_argument("right_velocity", type=int,help="Velocity for the right wheel.")
args = parser.parse_args()
print(f"Left wheel velocity: {args.left_velocity}")
print(f"Right wheel velocity: {args.right_velocity}")
# Configuration
FAN = 18 
FREQ = 10000
h = lgpio.gpiochip_open(0)
lgpio.gpio_claim_output(h,ENA)
lgpio.gpio_claim_output(h,ENB)
lgpio.gpio_claim_output(h,IN1)
lgpio.gpio_claim_output(h,IN2)
lgpio.gpio_claim_output(h,IN3)
lgpio.gpio_claim_output(h,IN4)
lgpio.gpio_write(h, ENA, 1)
lgpio.gpio_write(h, ENB, 1)
if (args.left_velocity >= 0 and args.right_velocity >= 0):
    lgpio.gpio_write(h, IN1, 1)
    lgpio.tx_pwm(h, ENA, 10000, args.right_velocity)
    lgpio.gpio_write(h, IN3, 1)
    lgpio.tx_pwm(h, ENB, 10000, args.left_velocity)
elif (args.left_velocity < 0 and args.right_velocity >= 0):
    lgpio.gpio_write(h, IN1, 1)
    lgpio.tx_pwm(h, ENA, 10000, args.right_velocity)
    lgpio.gpio_write(h, IN4, 1)
    lgpio.tx_pwm(h, ENB, 10000, args.left_velocity)
elif (args.left_velocity >= 0 and args.right_velocity < 0):
    lgpio.gpio_write(h, IN2, 1)
    lgpio.tx_pwm(h, ENA, 10000, args.right_velocity)
    lgpio.gpio_write(h, IN3, 1)
    lgpio.tx_pwm(h, ENB, 10000, args.left_velocity)
else:
    lgpio.gpio_write(h, IN2, 1)
    lgpio.tx_pwm(h, ENA, 10000, args.right_velocity)
    lgpio.gpio_write(h, IN4, 1)
    lgpio.tx_pwm(h, ENB, 10000, args.left_velocity)


