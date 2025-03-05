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
lgpio.gpio_write(h, IN1, 1)
lgpio.tx_pwm(h, ENA, 10000, 50)  # Motor A: 10kHz, 50% speed
time.sleep(5)
lgpio.tx_pwm(h, ENA, 10000, 0)  # Motor A: 10kHz, 50% speed

