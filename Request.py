#!/usr/bin/python2.7.8
# class for HTTP requests for the Observer project

import urllib2
import requests
import json
import base64
import Data

var = Data.DataVar()

class APIrequest:

    def requestDevices(self, devtype):
        # type: (string) -> string
        url = var.urldev + "?" + devtype
        request = urllib2.Request(url)
        base64string = base64.encodestring('%s:%s' % (var.user, var.pword)).replace('\n', '')
        request.add_header("Authorization", "Basic %s" % base64string)
        response = urllib2.urlopen(request)
        jsonString = response.read()
        data = json.loads(jsonString)
        return data

    def requestPorts(self, devid):
        # type: (string) -> string
        url = var.urlport + var.withdevid + devid + var.porttype
        request = urllib2.Request(url)
        base64string = base64.encodestring('%s:%s' % (var.user, var.pword)).replace('\n', '')
        request.add_header("Authorization", "Basic %s" % base64string)
        response = urllib2.urlopen(request)
        jsonString = response.read()
        data = json.loads(jsonString)
        return data

    def requestSensors(self, devid):
        # type: (string) -> string
        url = var.urlsens + var.withdevid + devid
        request = urllib2.Request(url)
        base64string = base64.encodestring('%s:%s' % (var.user, var.pword)).replace('\n', '')
        request.add_header("Authorization", "Basic %s" % base64string)
        response = urllib2.urlopen(request)
        jsonString = response.read()
        data = json.loads(jsonString)
        return data

    def writeDeviceTimeSerieData(self):
        for i in range(len(var.devices)):
            url = var.urldb
            data = var.ddataprefix + var.devices[i] + var.hidata + var.deviceids[i] + var.dsdata + var.devicestatus[i]
            print data
            response = requests.post(url=url, data=data)
            print response

    def writePortTimeSerieData(self):
        for i in range(len(var.portdeviceid)):
            url = var.urldb
            data = var.pdataprefix + var.portdeviceid[i] + var.pldata + var.portlabels[i] + var.asdata + var.adminstatus[i] + var.osdata + var.opstatus[i] + var.tedata + var.totalerrordelta[i] + var.efdata + var.totalerrordelta[i]
            print data
            response = requests.post(url=url, data=data)
            print response

    def writeSensorTimeSerieData(self):
        for i in range(len(var.sensordeviceid)):
            url = var.urldb
            data = var.sdataprefix + var.sensordeviceid[i] + var.siddata + var.sensorids[i] + var.sldata + var.sensorlimit[i] + var.svdata + var.sensorvalue[i] + var.sndata + var.sensorname[i] + var.quote
            print data
            response = requests.post(url=url, data=data)
            print response

    def clearDBdata(self):
        url = var.urldbdrop
        params = var.dropseries
        response = requests.get(url=url, params=params)
        print response

    def parseDeviceData(self, devdata):
        # type: (string) -> string
        devicedata = devdata
        if devicedata["devices"]!=None:
            for i in range(len(devicedata["devices"])):
                index = devicedata["devices"].keys()
                var.deviceids.append(devicedata["devices"][index[i]]["device_id"])
                var.devices.append(devicedata["devices"][index[i]]["hostname"])
                var.devicestatus.append(devicedata["devices"][index[i]]["status"])

    def parsePortData(self, pdata):
        portdata = pdata
        if portdata["ports"]!=None:
            for i in range(len(portdata["ports"])):
                index = portdata["ports"].keys()
                var.portdeviceid.append(portdata["ports"][index[i]]["device_id"])
                var.portlabels.append(portdata["ports"][index[i]]["port_label"])
                var.adminstatus.append(portdata["ports"][index[i]]["admin_status"])
                var.opstatus.append(portdata["ports"][index[i]]["ifOperStatus"])
                var.inerrorsdelta.append(portdata["ports"][index[i]]["ifInErrors_delta"])
                var.outerrorsdelta.append(portdata["ports"][index[i]]["ifOutErrors_delta"])
                total = str(int(portdata["ports"][index[i]]["ifInErrors_delta"]) + int(portdata["ports"][index[i]]["ifOutErrors_delta"]))
                var.totalerrordelta.append(total)
                print total

    def parseSensorData(self, sdata):
        sensordata = sdata
        if sensordata["sensors"]!=None:
            for i in range(len(sensordata["sensors"])):
                index = sensordata["sensors"].keys()
                var.sensordeviceid.append(sensordata["sensors"][index[i]]["device_id"])
                var.sensorids.append(sensordata["sensors"][index[i]]["sensor_id"])
                var.sensorname.append(sensordata["sensors"][index[i]]["sensor_descr"])
                var.sensorlimit.append(sensordata["sensors"][index[i]]["sensor_limit"])
                var.sensorvalue.append(sensordata["sensors"][index[i]]["sensor_value"])


    def convertTempToFahrenheit(self):
        for i in range(len(var.sensorlimit)):
            var.sensorlimit[i] = str(9.0/5.0*float(var.sensorlimit[i])+32)
        for i in range(len(var.sensorvalue)):
            var.sensorvalue[i] = str(9.0/5.0*float(var.sensorvalue[i])+32)
