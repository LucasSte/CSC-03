import cv2
import os
from datetime import datetime
import olympe
from olympe.messages.ardrone3.Piloting import TakeOff, Landing
from olympe.messages.ardrone3.Piloting import moveBy
from olympe.messages.ardrone3.PilotingState import FlyingStateChanged, PositionChanged
from olympe.messages.ardrone3.PilotingSettings import MaxTilt
from olympe.messages.ardrone3.GPSSettingsState import GPSFixStateChanged

class Cloud:
    report = None
    report_path = os.getcwd() + "/sick_plants_report/" + str(datetime.now())
    img_path = os.getcwd() + "/sick_plants_img/" + str(datetime.now())
    latitude = None
    longitude = None
    altitude = None

    def __init__(self):
        print("Connecting to Cloud...")
        self.open_report()

    def save_ocurrence(self,drone,image):
        self.latitude = drone.get_state(PositionChanged)['latitude']
        self.longitude = drone.get_state(PositionChanged)['longitude']
        self.altitude = drone.get_state(PositionChanged)['altitude']
        self.add_to_report(drone,image)
        self.save_img(image)

    def add_to_report(self,drone,image):
        self.report.write("Latitude = {} \n".format(self.latitude))
        self.report.write("Longitude = {} \n".format(self.longitude))
        self.report.write("Altitude = {} \n".format(self.altitude))
        self.report.write("--------------------------------------\n")
        print ("Latitude = {}".format(self.latitude))
        print ("Longitude = {}".format(self.longitude))
        print ("Altitude = {}".format(self.altitude))
        print ("--------------------------------------")
        
    def save_img(self,image):
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        img_filename = self.img_path+str(round(self.latitude,2))+"_"+str(round(self.longitude,2))+"_"+str(round(self.altitude,2))+".png"
        cv2.imwrite(img_filename,image)
    
    def open_report(self):
        self.report = open(self.report_path+".txt","w+")

    def close_report(self):
        self.report.close()
        
