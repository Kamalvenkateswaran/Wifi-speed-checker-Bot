from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from InternetSpeedTwitterBot import InternetSpeedTwitterBot



internet_speed = InternetSpeedTwitterBot()

PROMISED_UP=50
PROMISED_DOWN=100


internet_speed.get_speed()


if internet_speed.down <PROMISED_DOWN or internet_speed.up<PROMISED_UP:
    internet_speed.twitter()

