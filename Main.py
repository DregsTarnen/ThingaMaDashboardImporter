#!/usr/bin/python2.7.8
# Main body for the Observer project

import Request
import Data

apir = Request.APIrequest()
var = Data.DataVar()

class Main:



    def writeDeviceData(self):
        for i in range(len(var.type)):
            devdata = apir.requestDevices(var.type[i])
            apir.parseDeviceData(devdata)
        apir.writeDeviceTimeSerieData()


    def writePortData(self):
        for i in range(len(var.deviceids)):
            portdata = apir.requestPorts(var.deviceids[i])
            apir.parsePortData(portdata)
        apir.writePortTimeSerieData()

    def writeSensorData(self):
        for i in range(len(var.roomsensorid)):
            sensordata = apir.requestSensors(var.roomsensorid[i])
            apir.parseSensorData(sensordata)
        apir.convertTempToFahrenheit()
        apir.writeSensorTimeSerieData()

    def clearVariables(self):
        var.deviceids = []
        var.devices = []
        var.portdeviceid = []
        var.devicestatus = []
        var.portlabels = []
        var.opstatus = []
        var.adminstatus = []
        var.totalerrordelta = []
        var.sensorvalue = []
        var.sensorlimit = []
        var.sensorname = []
        var.sensordeviceid = []
        var.sensorids = []





    def __init__(self):
        apir.clearDBdata()
        self.writeDeviceData()
        self.writePortData()
        self.writeSensorData()
        self.clearVariables()


x = Main()