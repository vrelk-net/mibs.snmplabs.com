#
# PySNMP MIB module SNR-ERD-4 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SNR-ERD-4
# Produced by pysmi-0.3.4 at Wed May  1 15:08:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, Gauge32, IpAddress, Counter64, Bits, Integer32, TimeTicks, NotificationType, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, MibIdentifier, ObjectIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Gauge32", "IpAddress", "Counter64", "Bits", "Integer32", "TimeTicks", "NotificationType", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "MibIdentifier", "ObjectIdentity", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
snr = ModuleIdentity((1, 3, 6, 1, 4, 1, 40418))
snr.setRevisions(('2015-04-29 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: snr.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: snr.setLastUpdated('201504291200Z')
if mibBuilder.loadTexts: snr.setOrganization('NAG ')
if mibBuilder.loadTexts: snr.setContactInfo('erd@nag.ru')
if mibBuilder.loadTexts: snr.setDescription('The MIB module for SNR-ERD')
snr_erd = MibIdentifier((1, 3, 6, 1, 4, 1, 40418, 2)).setLabel("snr-erd")
snr_erd_4 = MibIdentifier((1, 3, 6, 1, 4, 1, 40418, 2, 6)).setLabel("snr-erd-4")
measurements = MibIdentifier((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1))
sensesstate = MibIdentifier((1, 3, 6, 1, 4, 1, 40418, 2, 6, 2))
management = MibIdentifier((1, 3, 6, 1, 4, 1, 40418, 2, 6, 3))
counters = MibIdentifier((1, 3, 6, 1, 4, 1, 40418, 2, 6, 8))
options = MibIdentifier((1, 3, 6, 1, 4, 1, 40418, 2, 6, 10))
snrSensors = MibIdentifier((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1))
temperatureSensors = MibIdentifier((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 1))
powerSensors = MibIdentifier((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 2))
alarmSensCnts = MibIdentifier((1, 3, 6, 1, 4, 1, 40418, 2, 6, 8, 2))
erd4Traps = MibIdentifier((1, 3, 6, 1, 4, 1, 40418, 2, 6, 0))
voltageSensor = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageSensor.setStatus('current')
if mibBuilder.loadTexts: voltageSensor.setDescription('qwerty')
serialS1 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialS1.setStatus('current')
if mibBuilder.loadTexts: serialS1.setDescription('qwerty')
serialS2 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 11), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialS2.setStatus('current')
if mibBuilder.loadTexts: serialS2.setDescription('qwerty')
serialS3 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 12), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialS3.setStatus('current')
if mibBuilder.loadTexts: serialS3.setDescription('qwerty')
serialS4 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 13), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialS4.setStatus('current')
if mibBuilder.loadTexts: serialS4.setDescription('qwerty')
serialS5 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 14), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialS5.setStatus('current')
if mibBuilder.loadTexts: serialS5.setDescription('qwerty')
serialS6 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 15), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialS6.setStatus('current')
if mibBuilder.loadTexts: serialS6.setDescription('qwerty')
serialS7 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 16), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialS7.setStatus('current')
if mibBuilder.loadTexts: serialS7.setDescription('qwerty')
serialS8 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 17), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialS8.setStatus('current')
if mibBuilder.loadTexts: serialS8.setDescription('qwerty')
serialS9 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 18), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialS9.setStatus('current')
if mibBuilder.loadTexts: serialS9.setDescription('qwerty')
serialS10 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 19), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialS10.setStatus('current')
if mibBuilder.loadTexts: serialS10.setDescription('qwerty')
temperatureS1 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureS1.setStatus('current')
if mibBuilder.loadTexts: temperatureS1.setDescription('qwerty')
temperatureS2 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureS2.setStatus('current')
if mibBuilder.loadTexts: temperatureS2.setDescription('qwerty')
temperatureS3 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureS3.setStatus('current')
if mibBuilder.loadTexts: temperatureS3.setDescription('qwerty')
temperatureS4 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureS4.setStatus('current')
if mibBuilder.loadTexts: temperatureS4.setDescription('qwerty')
temperatureS5 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureS5.setStatus('current')
if mibBuilder.loadTexts: temperatureS5.setDescription('qwerty')
temperatureS6 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureS6.setStatus('current')
if mibBuilder.loadTexts: temperatureS6.setDescription('qwerty')
temperatureS7 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureS7.setStatus('current')
if mibBuilder.loadTexts: temperatureS7.setDescription('qwerty')
temperatureS8 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureS8.setStatus('current')
if mibBuilder.loadTexts: temperatureS8.setDescription('qwerty')
temperatureS9 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureS9.setStatus('current')
if mibBuilder.loadTexts: temperatureS9.setDescription('qwerty')
temperatureS10 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureS10.setStatus('current')
if mibBuilder.loadTexts: temperatureS10.setDescription('qwerty')
voltageS1 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageS1.setStatus('current')
if mibBuilder.loadTexts: voltageS1.setDescription('qwerty')
currentS1 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentS1.setStatus('current')
if mibBuilder.loadTexts: currentS1.setDescription('qwerty')
voltageS2 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageS2.setStatus('current')
if mibBuilder.loadTexts: voltageS2.setDescription('qwerty')
currentS2 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentS2.setStatus('current')
if mibBuilder.loadTexts: currentS2.setDescription('qwerty')
voltageS3 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 2, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageS3.setStatus('current')
if mibBuilder.loadTexts: voltageS3.setDescription('qwerty')
currentS3 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 2, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentS3.setStatus('current')
if mibBuilder.loadTexts: currentS3.setDescription('qwerty')
voltageS4 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 2, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageS4.setStatus('current')
if mibBuilder.loadTexts: voltageS4.setDescription('qwerty')
currentS4 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 2, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentS4.setStatus('current')
if mibBuilder.loadTexts: currentS4.setDescription('qwerty')
voltageS5 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 2, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageS5.setStatus('current')
if mibBuilder.loadTexts: voltageS5.setDescription('qwerty')
currentS5 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 2, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentS5.setStatus('current')
if mibBuilder.loadTexts: currentS5.setDescription('qwerty')
voltageS6 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 2, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageS6.setStatus('current')
if mibBuilder.loadTexts: voltageS6.setDescription('qwerty')
currentS6 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 2, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentS6.setStatus('current')
if mibBuilder.loadTexts: currentS6.setDescription('qwerty')
voltageS7 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 2, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageS7.setStatus('current')
if mibBuilder.loadTexts: voltageS7.setDescription('qwerty')
currentS7 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 2, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentS7.setStatus('current')
if mibBuilder.loadTexts: currentS7.setDescription('qwerty')
voltageS8 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 2, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageS8.setStatus('current')
if mibBuilder.loadTexts: voltageS8.setDescription('qwerty')
currentS8 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 2, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentS8.setStatus('current')
if mibBuilder.loadTexts: currentS8.setDescription('qwerty')
voltageS9 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 2, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageS9.setStatus('current')
if mibBuilder.loadTexts: voltageS9.setDescription('qwerty')
currentS9 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 2, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentS9.setStatus('current')
if mibBuilder.loadTexts: currentS9.setDescription('qwerty')
voltageS10 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 2, 28), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageS10.setStatus('current')
if mibBuilder.loadTexts: voltageS10.setDescription('qwerty')
currentS10 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 1, 1, 2, 29), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: currentS10.setStatus('current')
if mibBuilder.loadTexts: currentS10.setDescription('qwerty')
alarmSensor1 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0, 2))).clone(namedValues=NamedValues(("high", 1), ("low", 0), ("off", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmSensor1.setStatus('current')
if mibBuilder.loadTexts: alarmSensor1.setDescription('qwerty')
alarmSensor2 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0, 2))).clone(namedValues=NamedValues(("high", 1), ("low", 0), ("off", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmSensor2.setStatus('current')
if mibBuilder.loadTexts: alarmSensor2.setDescription('qwerty')
alarmSensor3 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0, 2))).clone(namedValues=NamedValues(("high", 1), ("low", 0), ("off", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmSensor3.setStatus('current')
if mibBuilder.loadTexts: alarmSensor3.setDescription('qwerty')
alarmSensor4 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0, 2))).clone(namedValues=NamedValues(("high", 1), ("low", 0), ("off", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmSensor4.setStatus('current')
if mibBuilder.loadTexts: alarmSensor4.setDescription('qwerty')
alarmSensor5 = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0, 2))).clone(namedValues=NamedValues(("high", 1), ("low", 0), ("off", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmSensor5.setStatus('current')
if mibBuilder.loadTexts: alarmSensor5.setDescription('qwerty')
uSensor = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("no", 1), ("yes", 0)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: uSensor.setStatus('current')
if mibBuilder.loadTexts: uSensor.setDescription('qwerty')
releState = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 0), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: releState.setStatus('current')
if mibBuilder.loadTexts: releState.setDescription('qwerty')
smart1State = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 0), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smart1State.setStatus('current')
if mibBuilder.loadTexts: smart1State.setDescription('qwerty')
smart2State = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 0), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smart2State.setStatus('current')
if mibBuilder.loadTexts: smart2State.setDescription('qwerty')
smart3State = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 0), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smart3State.setStatus('current')
if mibBuilder.loadTexts: smart3State.setDescription('qwerty')
smart4State = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 3, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 0), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smart4State.setStatus('current')
if mibBuilder.loadTexts: smart4State.setDescription('qwerty')
smart5State = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 3, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 0), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smart5State.setStatus('current')
if mibBuilder.loadTexts: smart5State.setDescription('qwerty')
releResetTime = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 3, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: releResetTime.setStatus('current')
if mibBuilder.loadTexts: releResetTime.setDescription('qwerty')
smart1ResetTime = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 3, 12), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smart1ResetTime.setStatus('current')
if mibBuilder.loadTexts: smart1ResetTime.setDescription('qwerty')
smart2ResetTime = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 3, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smart2ResetTime.setStatus('current')
if mibBuilder.loadTexts: smart2ResetTime.setDescription('qwerty')
smart3ResetTime = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 3, 14), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smart3ResetTime.setStatus('current')
if mibBuilder.loadTexts: smart3ResetTime.setDescription('qwerty')
smart4ResetTime = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 3, 15), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smart4ResetTime.setStatus('current')
if mibBuilder.loadTexts: smart4ResetTime.setDescription('qwerty')
smart5ResetTime = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 3, 16), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smart5ResetTime.setStatus('current')
if mibBuilder.loadTexts: smart5ResetTime.setDescription('qwerty')
alarmSensor1cnt = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 8, 2, 1), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmSensor1cnt.setStatus('current')
if mibBuilder.loadTexts: alarmSensor1cnt.setDescription('qwerty')
alarmSensor2cnt = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 8, 2, 2), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmSensor2cnt.setStatus('current')
if mibBuilder.loadTexts: alarmSensor2cnt.setDescription('qwerty')
alarmSensor3cnt = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 8, 2, 3), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmSensor3cnt.setStatus('current')
if mibBuilder.loadTexts: alarmSensor3cnt.setDescription('qwerty')
alarmSensor4cnt = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 8, 2, 4), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmSensor4cnt.setStatus('current')
if mibBuilder.loadTexts: alarmSensor4cnt.setDescription('qwerty')
alarmSensor5cnt = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 8, 2, 5), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmSensor5cnt.setStatus('current')
if mibBuilder.loadTexts: alarmSensor5cnt.setDescription('qwerty')
dataType = MibScalar((1, 3, 6, 1, 4, 1, 40418, 2, 6, 10, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("integer", 0), ("float", 1), ("ufloat", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dataType.setStatus('current')
if mibBuilder.loadTexts: dataType.setDescription('qwerty')
aSense1Alarm = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 1))
if mibBuilder.loadTexts: aSense1Alarm.setStatus('current')
if mibBuilder.loadTexts: aSense1Alarm.setDescription('Check the text of message')
aSense1Release = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 2))
if mibBuilder.loadTexts: aSense1Release.setStatus('current')
if mibBuilder.loadTexts: aSense1Release.setDescription('Check the text of message')
aSense2Alarm = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 3))
if mibBuilder.loadTexts: aSense2Alarm.setStatus('current')
if mibBuilder.loadTexts: aSense2Alarm.setDescription('Check the text of message')
aSense2Release = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 4))
if mibBuilder.loadTexts: aSense2Release.setStatus('current')
if mibBuilder.loadTexts: aSense2Release.setDescription('Check the text of message')
aSense3Alarm = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 5))
if mibBuilder.loadTexts: aSense3Alarm.setStatus('current')
if mibBuilder.loadTexts: aSense3Alarm.setDescription('Check the text of message')
aSense3Release = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 6))
if mibBuilder.loadTexts: aSense3Release.setStatus('current')
if mibBuilder.loadTexts: aSense3Release.setDescription('Check the text of message')
aSense4Alarm = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 7))
if mibBuilder.loadTexts: aSense4Alarm.setStatus('current')
if mibBuilder.loadTexts: aSense4Alarm.setDescription('Check the text of message')
aSense4Release = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 8))
if mibBuilder.loadTexts: aSense4Release.setStatus('current')
if mibBuilder.loadTexts: aSense4Release.setDescription('Check the text of message')
aSense5Alarm = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 9))
if mibBuilder.loadTexts: aSense5Alarm.setStatus('current')
if mibBuilder.loadTexts: aSense5Alarm.setDescription('Check the text of message')
aSense5Release = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 10))
if mibBuilder.loadTexts: aSense5Release.setStatus('current')
if mibBuilder.loadTexts: aSense5Release.setDescription('Check the text of message')
uSenseAlarm = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 11))
if mibBuilder.loadTexts: uSenseAlarm.setStatus('current')
if mibBuilder.loadTexts: uSenseAlarm.setDescription('Check the text of message')
uSenseRelease = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 12))
if mibBuilder.loadTexts: uSenseRelease.setStatus('current')
if mibBuilder.loadTexts: uSenseRelease.setDescription('Check the text of message')
reloutThermoOn = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 13))
if mibBuilder.loadTexts: reloutThermoOn.setStatus('current')
if mibBuilder.loadTexts: reloutThermoOn.setDescription('Check the text of message')
reloutThermoOff = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 14))
if mibBuilder.loadTexts: reloutThermoOff.setStatus('current')
if mibBuilder.loadTexts: reloutThermoOff.setDescription('Check the text of message')
smart1ThermoOn = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 15))
if mibBuilder.loadTexts: smart1ThermoOn.setStatus('current')
if mibBuilder.loadTexts: smart1ThermoOn.setDescription('Check the text of message')
smart1ThermoOff = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 16))
if mibBuilder.loadTexts: smart1ThermoOff.setStatus('current')
if mibBuilder.loadTexts: smart1ThermoOff.setDescription('Check the text of message')
smart2ThermoOn = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 17))
if mibBuilder.loadTexts: smart2ThermoOn.setStatus('current')
if mibBuilder.loadTexts: smart2ThermoOn.setDescription('Check the text of message')
smart2ThermoOff = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 18))
if mibBuilder.loadTexts: smart2ThermoOff.setStatus('current')
if mibBuilder.loadTexts: smart2ThermoOff.setDescription('Check the text of message')
smart3ThermoOn = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 19))
if mibBuilder.loadTexts: smart3ThermoOn.setStatus('current')
if mibBuilder.loadTexts: smart3ThermoOn.setDescription('Check the text of message')
smart3ThermoOff = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 20))
if mibBuilder.loadTexts: smart3ThermoOff.setStatus('current')
if mibBuilder.loadTexts: smart3ThermoOff.setDescription('Check the text of message')
smart4ThermoOn = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 21))
if mibBuilder.loadTexts: smart4ThermoOn.setStatus('current')
if mibBuilder.loadTexts: smart4ThermoOn.setDescription('Check the text of message')
smart4ThermoOff = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 22))
if mibBuilder.loadTexts: smart4ThermoOff.setStatus('current')
if mibBuilder.loadTexts: smart4ThermoOff.setDescription('Check the text of message')
smart5ThermoOn = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 23))
if mibBuilder.loadTexts: smart5ThermoOn.setStatus('current')
if mibBuilder.loadTexts: smart5ThermoOn.setDescription('Check the text of message')
smart5ThermoOff = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 24))
if mibBuilder.loadTexts: smart5ThermoOff.setStatus('current')
if mibBuilder.loadTexts: smart5ThermoOff.setDescription('Check the text of message')
tempSensorAlarm = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 29))
if mibBuilder.loadTexts: tempSensorAlarm.setStatus('current')
if mibBuilder.loadTexts: tempSensorAlarm.setDescription('Check the text of message')
tempSensorRelease = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 30))
if mibBuilder.loadTexts: tempSensorRelease.setStatus('current')
if mibBuilder.loadTexts: tempSensorRelease.setDescription('Check the text of message')
voltSensorAlarm = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 31))
if mibBuilder.loadTexts: voltSensorAlarm.setStatus('current')
if mibBuilder.loadTexts: voltSensorAlarm.setDescription('Check the text of message')
voltSensorRelease = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 32))
if mibBuilder.loadTexts: voltSensorRelease.setStatus('current')
if mibBuilder.loadTexts: voltSensorRelease.setDescription('Check the text of message')
task1Done = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 36))
if mibBuilder.loadTexts: task1Done.setStatus('current')
if mibBuilder.loadTexts: task1Done.setDescription('Check the text of message')
task2Done = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 37))
if mibBuilder.loadTexts: task2Done.setStatus('current')
if mibBuilder.loadTexts: task2Done.setDescription('Check the text of message')
task3Done = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 38))
if mibBuilder.loadTexts: task3Done.setStatus('current')
if mibBuilder.loadTexts: task3Done.setDescription('Check the text of message')
task4Done = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 39))
if mibBuilder.loadTexts: task4Done.setStatus('current')
if mibBuilder.loadTexts: task4Done.setDescription('Check the text of message')
pingLost = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 45))
if mibBuilder.loadTexts: pingLost.setStatus('current')
if mibBuilder.loadTexts: pingLost.setDescription('Check the text of message')
batteryChargeLow = NotificationType((1, 3, 6, 1, 4, 1, 40418, 2, 6, 0, 47))
if mibBuilder.loadTexts: batteryChargeLow.setStatus('current')
if mibBuilder.loadTexts: batteryChargeLow.setDescription('Check the text of message')
erd4Group = NotificationGroup((1, 3, 6, 1, 4, 1, 40418, 2, 6, 99)).setObjects(("SNR-ERD-4", "aSense1Alarm"), ("SNR-ERD-4", "aSense1Release"), ("SNR-ERD-4", "aSense2Alarm"), ("SNR-ERD-4", "aSense2Release"), ("SNR-ERD-4", "aSense3Alarm"), ("SNR-ERD-4", "aSense3Release"), ("SNR-ERD-4", "aSense4Alarm"), ("SNR-ERD-4", "aSense4Release"), ("SNR-ERD-4", "aSense5Alarm"), ("SNR-ERD-4", "aSense5Release"), ("SNR-ERD-4", "uSenseAlarm"), ("SNR-ERD-4", "uSenseRelease"), ("SNR-ERD-4", "reloutThermoOn"), ("SNR-ERD-4", "reloutThermoOff"), ("SNR-ERD-4", "smart1ThermoOn"), ("SNR-ERD-4", "smart1ThermoOff"), ("SNR-ERD-4", "smart2ThermoOn"), ("SNR-ERD-4", "smart2ThermoOff"), ("SNR-ERD-4", "smart3ThermoOn"), ("SNR-ERD-4", "smart3ThermoOff"), ("SNR-ERD-4", "smart4ThermoOn"), ("SNR-ERD-4", "smart4ThermoOff"), ("SNR-ERD-4", "smart5ThermoOn"), ("SNR-ERD-4", "smart5ThermoOff"), ("SNR-ERD-4", "tempSensorAlarm"), ("SNR-ERD-4", "tempSensorRelease"), ("SNR-ERD-4", "voltSensorAlarm"), ("SNR-ERD-4", "voltSensorRelease"), ("SNR-ERD-4", "task1Done"), ("SNR-ERD-4", "task2Done"), ("SNR-ERD-4", "task3Done"), ("SNR-ERD-4", "task4Done"), ("SNR-ERD-4", "pingLost"), ("SNR-ERD-4", "batteryChargeLow"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    erd4Group = erd4Group.setStatus('current')
if mibBuilder.loadTexts: erd4Group.setDescription(' ')
mibBuilder.exportSymbols("SNR-ERD-4", currentS3=currentS3, snr=snr, voltageS3=voltageS3, temperatureS8=temperatureS8, alarmSensor1cnt=alarmSensor1cnt, temperatureS6=temperatureS6, aSense1Alarm=aSense1Alarm, sensesstate=sensesstate, serialS4=serialS4, temperatureS2=temperatureS2, alarmSensor1=alarmSensor1, powerSensors=powerSensors, smart1ThermoOn=smart1ThermoOn, tempSensorRelease=tempSensorRelease, currentS2=currentS2, releResetTime=releResetTime, voltageS9=voltageS9, aSense5Alarm=aSense5Alarm, smart4ResetTime=smart4ResetTime, smart2ResetTime=smart2ResetTime, currentS1=currentS1, voltageS7=voltageS7, currentS4=currentS4, serialS7=serialS7, releState=releState, dataType=dataType, smart1ThermoOff=smart1ThermoOff, aSense4Alarm=aSense4Alarm, voltageS1=voltageS1, alarmSensor3=alarmSensor3, erd4Traps=erd4Traps, uSensor=uSensor, smart4State=smart4State, temperatureS9=temperatureS9, serialS3=serialS3, voltSensorAlarm=voltSensorAlarm, temperatureSensors=temperatureSensors, pingLost=pingLost, currentS5=currentS5, options=options, serialS2=serialS2, smart4ThermoOn=smart4ThermoOn, counters=counters, serialS5=serialS5, smart5State=smart5State, voltageS8=voltageS8, aSense2Alarm=aSense2Alarm, temperatureS5=temperatureS5, currentS7=currentS7, snr_erd=snr_erd, management=management, alarmSensor4=alarmSensor4, voltageSensor=voltageSensor, smart5ThermoOff=smart5ThermoOff, aSense4Release=aSense4Release, aSense1Release=aSense1Release, uSenseAlarm=uSenseAlarm, aSense3Release=aSense3Release, smart1State=smart1State, serialS1=serialS1, serialS10=serialS10, smart4ThermoOff=smart4ThermoOff, serialS8=serialS8, reloutThermoOn=reloutThermoOn, reloutThermoOff=reloutThermoOff, aSense5Release=aSense5Release, batteryChargeLow=batteryChargeLow, voltageS5=voltageS5, alarmSensor5=alarmSensor5, task1Done=task1Done, alarmSensCnts=alarmSensCnts, smart5ResetTime=smart5ResetTime, alarmSensor2=alarmSensor2, measurements=measurements, voltageS6=voltageS6, temperatureS3=temperatureS3, serialS9=serialS9, smart2ThermoOn=smart2ThermoOn, task2Done=task2Done, aSense3Alarm=aSense3Alarm, smart3ThermoOn=smart3ThermoOn, currentS10=currentS10, smart3ThermoOff=smart3ThermoOff, smart5ThermoOn=smart5ThermoOn, serialS6=serialS6, aSense2Release=aSense2Release, voltageS10=voltageS10, temperatureS10=temperatureS10, alarmSensor5cnt=alarmSensor5cnt, voltageS4=voltageS4, snr_erd_4=snr_erd_4, temperatureS1=temperatureS1, temperatureS4=temperatureS4, PYSNMP_MODULE_ID=snr, alarmSensor2cnt=alarmSensor2cnt, snrSensors=snrSensors, temperatureS7=temperatureS7, voltSensorRelease=voltSensorRelease, smart1ResetTime=smart1ResetTime, smart3ResetTime=smart3ResetTime, alarmSensor4cnt=alarmSensor4cnt, tempSensorAlarm=tempSensorAlarm, smart3State=smart3State, currentS6=currentS6, task4Done=task4Done, erd4Group=erd4Group, smart2ThermoOff=smart2ThermoOff, voltageS2=voltageS2, smart2State=smart2State, alarmSensor3cnt=alarmSensor3cnt, uSenseRelease=uSenseRelease, currentS9=currentS9, task3Done=task3Done, currentS8=currentS8)