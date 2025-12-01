## 
# SigPt-EKF-SoC-Estimator/socestimator.py
# Copyright Enxu Liu 2025
# MIT License
# Reads one pin of anything and will estimate the state of charge of a battery using an Extended Kalman Filter.
##
import RPi.GPIO as GPIO
import time
import math

# define the pin you wan to read for voltage here
voltage_pin = 9  # example pin number

GPIO.setmode(GPIO.BOARD)  # BOARD pin-numbering scheme
GPIO.setup(voltage_pin, GPIO.IN)  # voltage pin set as input

