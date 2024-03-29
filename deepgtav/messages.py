#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import numpy as np
from numpy.lib.stride_tricks import as_strided

class Scenario:
    def __init__(self, location=None, time=None, weather=None, vehicle=None, drivingMode=None, route=None, surroundDrivingMode=None):
        self.location = location #[x,y]
        self.time = time #[hour, minute]
        self.weather = weather #string
        self.vehicle = vehicle #string
        self.drivingMode = drivingMode 
        self.route = route
        self.surroundDrivingMode = surroundDrivingMode

class Dataset:
    def __init__(self, rate=None, frame=None, vehicles=None, peds=None, trafficSigns=None, direction=None, 
                reward=None, throttle=None, brake=None, steering=None, speed=None, yaw=None, yawRate=None, drivingModeMsg=None, 
                location=None, time=None, rageMatrices=None, cameraInfo=None, eulerAngles=None, lidar=None, isCollide=None, acceleration=None):
        self.rate = rate #Hz
        self.frame = frame #[width, height]
        self.vehicles = vehicles #boolean
        self.peds = peds #boolean
        self.trafficSigns = trafficSigns #boolean
        self.direction = direction #[x,y,z]
        self.reward = reward #[id, p1, p2]
        self.throttle = throttle #boolean
        self.brake = brake #boolean
        self.steering = steering #boolean
        self.speed = speed #boolean
        self.yaw = yaw #boolean
        self.yawRate = yawRate #boolean
        self.drivingModeMsg = drivingModeMsg #boolean
        self.location = location #boolean
        self.time = time #boolean
        self.rageMatrices = rageMatrices #boolean
        self.cameraInfo = cameraInfo #boolean
        self.eulerAngles = eulerAngles #boolean
        self.lidar = lidar #boolean
        self.isCollide = isCollide #boolean
        self.acceleration = acceleration #boolean

class Start:
    def __init__(self, scenario=None, dataset=None):
        self.scenario = scenario
        self.dataset = dataset

    def to_json(self):
        _scenario = None
        _dataset = None

        if (self.scenario != None):
            _scenario = self.scenario.__dict__

        if (self.dataset != None):
            _dataset = self.dataset.__dict__     

        return json.dumps({'start':{'scenario': _scenario, 'dataset': _dataset}})

    def activate_bytes_frame(self):
        return True if self.dataset.frame != None else False, True if self.dataset.lidar != None else False

        

class Config:
    def __init__(self, scenario=None, dataset=None):
        self.scenario = scenario
        self.dataset = dataset

    def to_json(self):
        _scenario = None
        _dataset = None

        if (self.scenario != None):
            _scenario = self.scenario.__dict__

        if (self.dataset != None):
            _dataset = self.dataset.__dict__         

        return json.dumps({'config':{'scenario': _scenario, 'dataset': _dataset}})

    def activate_bytes_frame(self):
        return True if self.dataset.frame != None else False, True if self.dataset.lidar != None else False

        

class Stop:
    def to_json(self):
        return json.dumps({'stop':None}) #super dummy

class Commands:
    def __init__(self, throttle=None, brake=None, steering=None):
        self.throttle = throttle #float (0,1)
        self.brake = brake #float (0,1)
        self.steering = steering #float (-1,1)

    def to_json(self):
        return json.dumps({'commands':self.__dict__})
        
def frame2numpy(frame, frameSize):
    buff = np.fromstring(frame, dtype='uint8')
    # Scanlines are aligned to 4 bytes in Windows bitmaps
    strideWidth = int((frameSize[0] * 3 + 3) / 4) * 4
    # Return a copy because custom strides are not supported by OpenCV.
    return as_strided(buff, strides=(strideWidth, 3, 1), shape=(frameSize[1], frameSize[0], 3)).copy()



