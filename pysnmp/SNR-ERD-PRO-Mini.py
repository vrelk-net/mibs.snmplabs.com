#
# PySNMP MIB module SNR-ERD-PRO-Mini (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SNR-ERD-PRO-Mini
# Produced by pysmi-0.3.4 at Mon Apr 29 21:00:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits, Unsigned32, MibIdentifier, ObjectIdentity, Counter32, iso, TimeTicks, Counter64, enterprises, IpAddress, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits", "Unsigned32", "MibIdentifier", "ObjectIdentity", "Counter32", "iso", "TimeTicks", "Counter64", "enterprises", "IpAddress", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
snr = ModuleIdentity((1, 3, 6, 1, 4, 1, 40418))
snr.setRevisions(('2015-04-29 12:00',))
if mibBuilder.loadTexts: snr.setLastUpdated('201504291200Z')
if mibBuilder.loadTexts: snr.setOrganization('NAG ')
snr_erd = MibIdentifier((1, 3, 6, 1, 4, 1, 40418, 2)).setLabel("snr-erd")
snr_erd_pro_mini = MibIdentifier((1, 3, 6, 1, 4, 1, 40418, 2, 5)).setLabel("snr-erd-pro-mini")
measurements = MibIdentifier((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1))
sensesstate = MibIdentifier((1, 3, 6, 1, 4, 1, 40418, 2, 5, 2))
management = MibIdentifier((1, 3, 6, 1, 4, 1, 40418, 2, 5, 3))
counters = MibIdentifier((1, 3, 6, 1, 4, 1, 40418, 2, 5, 8))
options = MibIdentifier((1, 3, 6, 1, 4, 1, 40418, 2, 5, 10))
snrSensors = MibIdentifier((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1))
temperatureSensors = MibIdentifier((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 1))
powerSensors = MibIdentifier((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 2))
alarmSensCnts = MibIdentifier((1, 3, 6, 1, 4, 1, 40418, 2, 5, 8, 2))
erdproMiniTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 40418, 2, 5, 0))
voltageSensor = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageSensor.setStatus('current')
serialS1 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialS1.setStatus('current')
serialS2 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 11), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialS2.setStatus('current')
serialS3 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 12), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialS3.setStatus('current')
serialS4 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 13), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialS4.setStatus('current')
serialS5 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 14), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialS5.setStatus('current')
serialS6 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 15), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialS6.setStatus('current')
serialS7 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 16), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialS7.setStatus('current')
serialS8 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 17), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialS8.setStatus('current')
serialS9 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 18), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialS9.setStatus('current')
serialS10 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 19), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialS10.setStatus('current')
temperatureS1 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureS1.setStatus('current')
temperatureS2 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureS2.setStatus('current')
temperatureS3 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureS3.setStatus('current')
temperatureS4 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureS4.setStatus('current')
temperatureS5 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureS5.setStatus('current')
temperatureS6 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureS6.setStatus('current')
temperatureS7 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureS7.setStatus('current')
temperatureS8 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureS8.setStatus('current')
temperatureS9 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureS9.setStatus('current')
temperatureS10 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureS10.setStatus('current')
voltageS1 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageS1.setStatus('current')
currentS1 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentS1.setStatus('current')
voltageS2 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageS2.setStatus('current')
currentS2 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentS2.setStatus('current')
voltageS3 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 2, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageS3.setStatus('current')
currentS3 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 2, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentS3.setStatus('current')
voltageS4 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 2, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageS4.setStatus('current')
currentS4 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 2, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentS4.setStatus('current')
voltageS5 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 2, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageS5.setStatus('current')
currentS5 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 2, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentS5.setStatus('current')
voltageS6 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 2, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageS6.setStatus('current')
currentS6 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 2, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentS6.setStatus('current')
voltageS7 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 2, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageS7.setStatus('current')
currentS7 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 2, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentS7.setStatus('current')
voltageS8 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 2, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageS8.setStatus('current')
currentS8 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 2, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentS8.setStatus('current')
voltageS9 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 2, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageS9.setStatus('current')
currentS9 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 2, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentS9.setStatus('current')
voltageS10 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 2, 28), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageS10.setStatus('current')
currentS10 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 1, 1, 2, 29), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentS10.setStatus('current')
alarmSensor1 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("high", 1), ("low", 0)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmSensor1.setStatus('current')
alarmSensor2 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("high", 1), ("low", 0)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmSensor2.setStatus('current')
uSensor = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("no", 1), ("yes", 0)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: uSensor.setStatus('current')
smart1State = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 0), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smart1State.setStatus('current')
smart2State = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 0), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smart2State.setStatus('current')
smart1ResetTime = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 3, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smart1ResetTime.setStatus('current')
smart2ResetTime = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 3, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smart2ResetTime.setStatus('current')
alarmSensor1cnt = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 8, 2, 1), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmSensor1cnt.setStatus('current')
alarmSensor2cnt = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 8, 2, 2), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmSensor2cnt.setStatus('current')
dataType = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 5, 10, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("integer", 0), ("float", 1), ("ufloat", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dataType.setStatus('current')
aSense1Alarm = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 5, 0, 1))
if mibBuilder.loadTexts: aSense1Alarm.setStatus('current')
aSense1Release = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 5, 0, 2))
if mibBuilder.loadTexts: aSense1Release.setStatus('current')
aSense2Alarm = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 5, 0, 3))
if mibBuilder.loadTexts: aSense2Alarm.setStatus('current')
aSense2Release = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 5, 0, 4))
if mibBuilder.loadTexts: aSense2Release.setStatus('current')
uSenseAlarm = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 5, 0, 9))
if mibBuilder.loadTexts: uSenseAlarm.setStatus('current')
uSenseRelease = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 5, 0, 10))
if mibBuilder.loadTexts: uSenseRelease.setStatus('current')
smart1ThermoOn = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 5, 0, 13))
if mibBuilder.loadTexts: smart1ThermoOn.setStatus('current')
smart1ThermoOff = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 5, 0, 14))
if mibBuilder.loadTexts: smart1ThermoOff.setStatus('current')
smart2ThermoOn = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 5, 0, 15))
if mibBuilder.loadTexts: smart2ThermoOn.setStatus('current')
smart2ThermoOff = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 5, 0, 16))
if mibBuilder.loadTexts: smart2ThermoOff.setStatus('current')
tempSensorAlarm = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 5, 0, 29))
if mibBuilder.loadTexts: tempSensorAlarm.setStatus('current')
tempSensorRelease = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 5, 0, 30))
if mibBuilder.loadTexts: tempSensorRelease.setStatus('current')
voltSensorAlarm = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 5, 0, 31))
if mibBuilder.loadTexts: voltSensorAlarm.setStatus('current')
voltSensorRelease = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 5, 0, 32))
if mibBuilder.loadTexts: voltSensorRelease.setStatus('current')
task1Done = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 5, 0, 36))
if mibBuilder.loadTexts: task1Done.setStatus('current')
task2Done = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 5, 0, 37))
if mibBuilder.loadTexts: task2Done.setStatus('current')
task3Done = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 5, 0, 38))
if mibBuilder.loadTexts: task3Done.setStatus('current')
task4Done = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 5, 0, 39))
if mibBuilder.loadTexts: task4Done.setStatus('current')
pingLost = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 5, 0, 45))
if mibBuilder.loadTexts: pingLost.setStatus('current')
batteryChargeLow = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 5, 0, 47))
if mibBuilder.loadTexts: batteryChargeLow.setStatus('current')
erdProMiniTrapGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 40418, 2, 5, 99)).setObjects(("SNR-ERD-PRO-Mini", "aSense1Alarm"), ("SNR-ERD-PRO-Mini", "aSense1Release"), ("SNR-ERD-PRO-Mini", "aSense2Alarm"), ("SNR-ERD-PRO-Mini", "aSense2Release"), ("SNR-ERD-PRO-Mini", "uSenseAlarm"), ("SNR-ERD-PRO-Mini", "uSenseRelease"), ("SNR-ERD-PRO-Mini", "smart1ThermoOn"), ("SNR-ERD-PRO-Mini", "smart1ThermoOff"), ("SNR-ERD-PRO-Mini", "smart2ThermoOn"), ("SNR-ERD-PRO-Mini", "smart2ThermoOff"), ("SNR-ERD-PRO-Mini", "tempSensorAlarm"), ("SNR-ERD-PRO-Mini", "tempSensorRelease"), ("SNR-ERD-PRO-Mini", "voltSensorAlarm"), ("SNR-ERD-PRO-Mini", "voltSensorRelease"), ("SNR-ERD-PRO-Mini", "task1Done"), ("SNR-ERD-PRO-Mini", "task2Done"), ("SNR-ERD-PRO-Mini", "task3Done"), ("SNR-ERD-PRO-Mini", "task4Done"), ("SNR-ERD-PRO-Mini", "pingLost"), ("SNR-ERD-PRO-Mini", "batteryChargeLow"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    erdProMiniTrapGroup = erdProMiniTrapGroup.setStatus('current')
mibBuilder.exportSymbols("SNR-ERD-PRO-Mini", temperatureS2=temperatureS2, voltageS10=voltageS10, snr=snr, temperatureS8=temperatureS8, smart2ThermoOff=smart2ThermoOff, options=options, temperatureS6=temperatureS6, serialS5=serialS5, pingLost=pingLost, smart1ThermoOff=smart1ThermoOff, alarmSensor1=alarmSensor1, temperatureS9=temperatureS9, currentS2=currentS2, currentS6=currentS6, currentS9=currentS9, serialS6=serialS6, temperatureS4=temperatureS4, currentS10=currentS10, sensesstate=sensesstate, task2Done=task2Done, aSense1Alarm=aSense1Alarm, smart1ThermoOn=smart1ThermoOn, voltageS6=voltageS6, serialS1=serialS1, smart1ResetTime=smart1ResetTime, voltageS9=voltageS9, aSense2Release=aSense2Release, alarmSensor2cnt=alarmSensor2cnt, temperatureS1=temperatureS1, uSensor=uSensor, alarmSensor2=alarmSensor2, currentS3=currentS3, voltSensorRelease=voltSensorRelease, batteryChargeLow=batteryChargeLow, voltageS1=voltageS1, smart2State=smart2State, voltageSensor=voltageSensor, serialS2=serialS2, powerSensors=powerSensors, task1Done=task1Done, tempSensorRelease=tempSensorRelease, erdProMiniTrapGroup=erdProMiniTrapGroup, measurements=measurements, smart2ResetTime=smart2ResetTime, tempSensorAlarm=tempSensorAlarm, voltageS2=voltageS2, serialS8=serialS8, currentS1=currentS1, task4Done=task4Done, snrSensors=snrSensors, voltageS5=voltageS5, temperatureS3=temperatureS3, currentS8=currentS8, counters=counters, voltageS8=voltageS8, serialS10=serialS10, temperatureSensors=temperatureSensors, management=management, snr_erd_pro_mini=snr_erd_pro_mini, alarmSensor1cnt=alarmSensor1cnt, PYSNMP_MODULE_ID=snr, snr_erd=snr_erd, aSense2Alarm=aSense2Alarm, serialS4=serialS4, smart2ThermoOn=smart2ThermoOn, alarmSensCnts=alarmSensCnts, voltSensorAlarm=voltSensorAlarm, currentS7=currentS7, voltageS4=voltageS4, serialS3=serialS3, temperatureS7=temperatureS7, temperatureS10=temperatureS10, serialS7=serialS7, currentS5=currentS5, smart1State=smart1State, currentS4=currentS4, aSense1Release=aSense1Release, uSenseRelease=uSenseRelease, voltageS7=voltageS7, temperatureS5=temperatureS5, voltageS3=voltageS3, task3Done=task3Done, uSenseAlarm=uSenseAlarm, erdproMiniTraps=erdproMiniTraps, dataType=dataType, serialS9=serialS9)