import lgpio
import time
ENA = 17
ENB=4
IN3=5
IN4=6
IN1 = 27
IN2 = 22
h = lgpio.gpiochip_open(0)
lgpio.gpio_claim_output(h,ENA)
lgpio.gpio_claim_output(h,ENB)
lgpio.gpio_claim_output(h,IN1)
lgpio.gpio_claim_output(h,IN2)
lgpio.gpio_claim_output(h,IN3)
lgpio.gpio_claim_output(h,IN4)
lgpio.gpio_write(h, ENA, 1)
lgpio.gpio_write(h, ENB, 1)
lgpio.gpio_write(h, IN1, 0)
lgpio.gpio_write(h, IN2, 1)
lgpio.gpio_write(h, IN3, 0)
lgpio.gpio_write(h, IN4, 1)
time.sleep(1)
lgpio.gpio_write(h, ENA, 0)
lgpio.gpio_write(h, ENB, 0)
lgpio.gpio_write(h, IN1, 0)
lgpio.gpio_write(h, IN2, 0)
lgpio.gpio_write(h, IN3, 0)
lgpio.gpio_write(h, IN4, 0)
