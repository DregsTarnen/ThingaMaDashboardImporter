# !/usr/bin/python2.7.8
# author Erik R Fritts
# data variables for Observer project

class DataVar:
    devices = []
#UNIVERSAL DEVICE TYPES MONITORED APPLICABLE TO ALL USERS############
    type = ["type=network", "type=server", "type=environment", "type=wireless", "type=power", "type=video"]
#ROOM SENSOR IDS ARE USER SPECIFIC AND UNIQUE TO EACH USE CASE########
    roomsensorid = ["33", "32", "31"]
#INDEX BY DEVICE######################
    deviceids = []
    portdeviceid = []
    sensordeviceid = []
#----------------------------->>>>>>>>>>>>>>>>>>>
    devicestatus = []
    portlabels = []
    opstatus = []
    adminstatus = []
    inerrorsdelta = []
    outerrorsdelta = []
#TOTALERRORDELTA IS DERIVED AND IS NOT AN OBSERVIUM API VALUE/ INERRORSDELTA + OUTERRORSDELTA = TOTAL#####
    totalerrordelta = []
#--------------------------->>>>>>>>>>>>>>>>>>>>
    sensorids = []
    sensorname = []
    sensorvalue = []
    sensorlimit = []
#SEE OBSERVIUM API FOR SPECIFICS/ THIS ALLOWS A GET FILTERING THE RETURNED VALUES IN YOUR PORT LIST/ THIS CASE ETHERNET ONLY######
    porttype = "&ifType=ethernetCsmacd"
#OBSERVIUM API ####################################################
    urldev = "http://172.20.16.61/api/v0/devices/"
    urlport = "http://172.20.16.61/api/v0/ports/"
    urlsens = "http://172.20.16.61/api/v0/sensors/"
#INFLUX DB WRITE AND QUERY#####################################
    urldb = "http://localhost:8086/write?db=observerdb"
    urldbdrop = "http://localhost:8086/query?db=observerdb"
    user = "api"
    pword = "suckit"
#SENSOR DATA STRINGS#########################
    sdataprefix = 'Sensors,host_id='
    siddata = ',sensor_id='
    sldata = ' sensor_limit='
    svdata = ',sensor_value='
    sndata = ',sensor_name="'
    quote = '"'
#PORT DATA STRINGS##########################
    pdataprefix = 'NetPorts,host_id='
    pldata = ',port_label='
    asdata = ',admin_status='
    osdata = ',opstatus='
    tedata = ',totalerrordelta='
    efdata = ' errorfield='
#DEVICE DATA STRINGS#######################
    ddataprefix = 'Devices,hostname='
    hidata = ',host_id='
    dsdata = ' device_status='
#OBSERVIUM GET ENDPOINTS###################
    withdevid = "?device_id="
#INFLUX DB GET PARAMS######################
    dropseries = 'q=DROP SERIES FROM /.*/'
