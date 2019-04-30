#
# PySNMP MIB module DKSF-52-9-X-X-1 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DKSF-52-9-X-X-1
# Produced by pysmi-0.3.4 at Mon Apr 29 18:32:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
snmpTraps, = mibBuilder.importSymbols("SNMPv2-MIB", "snmpTraps")
NotificationType, ModuleIdentity, ObjectIdentity, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Integer32, Counter32, Counter64, IpAddress, TimeTicks, Bits, iso, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Integer32", "Counter32", "Counter64", "IpAddress", "TimeTicks", "Bits", "iso", "enterprises")
TruthValue, TimeStamp, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TimeStamp", "TextualConvention", "DisplayString")
netPing2PWR220 = ModuleIdentity((1, 3, 6, 1, 4, 1, 25728, 52))
netPing2PWR220.setRevisions(('2015-08-17 00:00', '2014-11-14 00:00', '2014-08-21 00:00', '2014-04-14 00:00', '2014-02-02 00:00', '2014-01-29 00:00', '2014-01-21 00:00', '2013-04-11 00:00', '2012-05-31 00:00', '2012-04-17 00:00', '2012-03-23 00:00', '2011-09-23 00:00', '2011-03-24 00:00', '2010-10-14 00:00', '2010-09-20 00:00', '2010-05-31 00:00', '2010-04-14 00:00',))
if mibBuilder.loadTexts: netPing2PWR220.setLastUpdated('201508170000Z')
if mibBuilder.loadTexts: netPing2PWR220.setOrganization('Alentis Electronics')
lightcom = MibIdentifier((1, 3, 6, 1, 4, 1, 25728))
npTrapInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 90))
npTrapEmailTo = MibScalar((1, 3, 6, 1, 4, 1, 25728, 90, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npTrapEmailTo.setStatus('current')
npRelay = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 5500))
npRelayTable = MibTable((1, 3, 6, 1, 4, 1, 25728, 5500, 5), )
if mibBuilder.loadTexts: npRelayTable.setStatus('current')
npRelayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1), ).setIndexNames((0, "DKSF-52-9-X-X-1", "npRelayN"))
if mibBuilder.loadTexts: npRelayEntry.setStatus('current')
npRelayN = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelayN.setStatus('current')
npRelayMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("off", 0), ("on", 1), ("watchdog", 2), ("schedule", 3), ("scheduleAndWatchdog", 4), ("logic", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npRelayMode.setStatus('current')
npRelayStartReset = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npRelayStartReset.setStatus('current')
npRelayMemo = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelayMemo.setStatus('current')
npRelayFlip = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(-1))).clone(namedValues=NamedValues(("flip", -1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelayFlip.setStatus('current')
npRelayState = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelayState.setStatus('current')
npPwr = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 5800))
npPwrTable = MibTable((1, 3, 6, 1, 4, 1, 25728, 5800, 3), )
if mibBuilder.loadTexts: npPwrTable.setStatus('current')
npPwrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25728, 5800, 3, 1), ).setIndexNames((0, "DKSF-52-9-X-X-1", "npPwrChannelN"))
if mibBuilder.loadTexts: npPwrEntry.setStatus('current')
npPwrChannelN = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5800, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npPwrChannelN.setStatus('current')
npPwrStartReset = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5800, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npPwrStartReset.setStatus('current')
npPwrManualMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5800, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("off", 0), ("on", 1), ("watchdog", 2), ("schedule", 3), ("scheduleAndWatchdog", 4), ("logic", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npPwrManualMode.setStatus('current')
npPwrResetsCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5800, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npPwrResetsCounter.setStatus('current')
npPwrRepeatingResetsCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5800, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npPwrRepeatingResetsCounter.setStatus('current')
npPwrMemo = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5800, 3, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npPwrMemo.setStatus('current')
npPwrRelayFlip = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5800, 3, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(-1))).clone(namedValues=NamedValues(("flip", -1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npPwrRelayFlip.setStatus('current')
npPwrRelayState = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5800, 3, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npPwrRelayState.setStatus('current')
npThermo = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8800))
npThermoTable = MibTable((1, 3, 6, 1, 4, 1, 25728, 8800, 1), )
if mibBuilder.loadTexts: npThermoTable.setStatus('current')
npThermoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1), ).setIndexNames((0, "DKSF-52-9-X-X-1", "npThermoSensorN"))
if mibBuilder.loadTexts: npThermoEntry.setStatus('current')
npThermoSensorN = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoSensorN.setStatus('current')
npThermoValue = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-60, 280))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoValue.setStatus('current')
npThermoStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("failed", 0), ("low", 1), ("norm", 2), ("high", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoStatus.setStatus('current')
npThermoLow = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-60, 280))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoLow.setStatus('current')
npThermoHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-60, 280))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoHigh.setStatus('current')
npThermoMemo = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoMemo.setStatus('current')
npThermoTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8800, 2))
npThermoTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8800, 2, 0))
npThermoTrapSensorN = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8800, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoTrapSensorN.setStatus('current')
npThermoTrapValue = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8800, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-60, 280))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoTrapValue.setStatus('current')
npThermoTrapStatus = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8800, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("failed", 0), ("low", 1), ("norm", 2), ("high", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoTrapStatus.setStatus('current')
npThermoTrapLow = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8800, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-60, 280))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoTrapLow.setStatus('current')
npThermoTrapHigh = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8800, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-60, 280))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoTrapHigh.setStatus('current')
npThermoTrapMemo = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8800, 2, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoTrapMemo.setStatus('current')
npThermoTrap = NotificationType((1, 3, 6, 1, 4, 1, 25728, 8800, 2, 0, 1)).setObjects(("DKSF-52-9-X-X-1", "npThermoTrapSensorN"), ("DKSF-52-9-X-X-1", "npThermoTrapValue"), ("DKSF-52-9-X-X-1", "npThermoTrapStatus"), ("DKSF-52-9-X-X-1", "npThermoTrapLow"), ("DKSF-52-9-X-X-1", "npThermoTrapHigh"), ("DKSF-52-9-X-X-1", "npThermoTrapMemo"))
if mibBuilder.loadTexts: npThermoTrap.setStatus('current')
npIo = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8900))
npIoTable = MibTable((1, 3, 6, 1, 4, 1, 25728, 8900, 1), )
if mibBuilder.loadTexts: npIoTable.setStatus('current')
npIoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1), ).setIndexNames((0, "DKSF-52-9-X-X-1", "npIoLineN"))
if mibBuilder.loadTexts: npIoEntry.setStatus('current')
npIoLineN = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npIoLineN.setStatus('current')
npIoLevelIn = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npIoLevelIn.setStatus('current')
npIoLevelOut = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(-1, 0, 1))).clone(namedValues=NamedValues(("flip", -1), ("low", 0), ("high", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npIoLevelOut.setStatus('current')
npIoMemo = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npIoMemo.setStatus('current')
npIoPulseCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 9), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npIoPulseCounter.setStatus('current')
npIoSinglePulseDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 25500))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npIoSinglePulseDuration.setStatus('current')
npIoSinglePulseStart = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npIoSinglePulseStart.setStatus('current')
npIoTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8900, 2))
npIoTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8900, 2, 0))
npIoTrapLineN = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8900, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npIoTrapLineN.setStatus('current')
npIoTrapLevelIn = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8900, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npIoTrapLevelIn.setStatus('current')
npIoTrapMemo = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8900, 2, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npIoTrapMemo.setStatus('current')
npIoTrap = NotificationType((1, 3, 6, 1, 4, 1, 25728, 8900, 2, 0, 1)).setObjects(("DKSF-52-9-X-X-1", "npIoTrapLineN"), ("DKSF-52-9-X-X-1", "npIoTrapLevelIn"), ("DKSF-52-9-X-X-1", "npIoTrapMemo"))
if mibBuilder.loadTexts: npIoTrap.setStatus('current')
npRelHumidity = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8400))
npRelHumSensor = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8400, 2))
npRelHumSensorStatus = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8400, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("ok", 0), ("error", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelHumSensorStatus.setStatus('current')
npRelHumSensorValueH = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8400, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelHumSensorValueH.setStatus('current')
npRelHumSensorValueT = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8400, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-60, 200))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelHumSensorValueT.setStatus('current')
npRelHumSensorStatusH = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8400, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("sensorFailed", 0), ("belowSafeRange", 1), ("inSafeRange", 2), ("aboveSafeRange", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelHumSensorStatusH.setStatus('current')
npRelHumSafeRangeHigh = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8400, 2, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelHumSafeRangeHigh.setStatus('current')
npRelHumSafeRangeLow = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8400, 2, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelHumSafeRangeLow.setStatus('current')
npRelHumSensorValueT100 = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8400, 2, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelHumSensorValueT100.setStatus('current')
npRelHumTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8400, 9))
npRelHumTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8400, 9, 0))
npRelHumTrap = NotificationType((1, 3, 6, 1, 4, 1, 25728, 8400, 9, 0, 1)).setObjects(("DKSF-52-9-X-X-1", "npRelHumSensorStatusH"), ("DKSF-52-9-X-X-1", "npRelHumSensorValueH"), ("DKSF-52-9-X-X-1", "npRelHumSafeRangeHigh"), ("DKSF-52-9-X-X-1", "npRelHumSafeRangeLow"), ("DKSF-52-9-X-X-1", "npTrapEmailTo"))
if mibBuilder.loadTexts: npRelHumTrap.setStatus('current')
npIr = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 7900))
npIrCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 7900, 1))
npIrPlayCmd = MibScalar((1, 3, 6, 1, 4, 1, 25728, 7900, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npIrPlayCmd.setStatus('current')
npIrReset = MibScalar((1, 3, 6, 1, 4, 1, 25728, 7900, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npIrReset.setStatus('current')
npIrStatus = MibScalar((1, 3, 6, 1, 4, 1, 25728, 7900, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 255))).clone(namedValues=NamedValues(("ok", 0), ("busyCaptureWaitingButton", 1), ("busyCaptureWaitingIr", 2), ("busyPlayback", 3), ("error", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npIrStatus.setStatus('current')
npReboot = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 911))
npSoftReboot = MibScalar((1, 3, 6, 1, 4, 1, 25728, 911, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npSoftReboot.setStatus('current')
npResetStack = MibScalar((1, 3, 6, 1, 4, 1, 25728, 911, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npResetStack.setStatus('current')
npForcedReboot = MibScalar((1, 3, 6, 1, 4, 1, 25728, 911, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npForcedReboot.setStatus('current')
mibBuilder.exportSymbols("DKSF-52-9-X-X-1", npIoTrapMemo=npIoTrapMemo, PYSNMP_MODULE_ID=netPing2PWR220, npThermoTrapValue=npThermoTrapValue, npIr=npIr, npRelHumSensorStatus=npRelHumSensorStatus, npIrReset=npIrReset, npPwrEntry=npPwrEntry, npRelay=npRelay, npThermoEntry=npThermoEntry, npRelayState=npRelayState, npRelayN=npRelayN, npIrPlayCmd=npIrPlayCmd, npThermoTrapPrefix=npThermoTrapPrefix, npIoTrapLevelIn=npIoTrapLevelIn, npIoMemo=npIoMemo, npRelHumTrapPrefix=npRelHumTrapPrefix, npRelayMemo=npRelayMemo, npThermoTrap=npThermoTrap, npPwrManualMode=npPwrManualMode, netPing2PWR220=netPing2PWR220, npRelHumSafeRangeLow=npRelHumSafeRangeLow, npPwr=npPwr, npThermoTraps=npThermoTraps, npIoPulseCounter=npIoPulseCounter, npIoEntry=npIoEntry, npRelHumSensorValueT100=npRelHumSensorValueT100, npThermoTrapMemo=npThermoTrapMemo, npIrCtrl=npIrCtrl, npThermoHigh=npThermoHigh, npIoSinglePulseDuration=npIoSinglePulseDuration, npThermoStatus=npThermoStatus, npRelHumidity=npRelHumidity, npRelayTable=npRelayTable, npThermoLow=npThermoLow, npThermo=npThermo, npRelayMode=npRelayMode, npPwrResetsCounter=npPwrResetsCounter, npThermoMemo=npThermoMemo, npIoTrapPrefix=npIoTrapPrefix, npIoLineN=npIoLineN, npIo=npIo, npPwrStartReset=npPwrStartReset, npIoTrapLineN=npIoTrapLineN, npThermoTrapLow=npThermoTrapLow, npIoSinglePulseStart=npIoSinglePulseStart, npIoLevelIn=npIoLevelIn, npIoTrap=npIoTrap, npThermoTable=npThermoTable, npRelayFlip=npRelayFlip, npIoTable=npIoTable, npPwrRelayState=npPwrRelayState, npRelHumTrap=npRelHumTrap, npTrapEmailTo=npTrapEmailTo, npThermoTrapSensorN=npThermoTrapSensorN, npPwrMemo=npPwrMemo, npThermoTrapHigh=npThermoTrapHigh, npRelHumSensorValueH=npRelHumSensorValueH, npRelayEntry=npRelayEntry, npThermoValue=npThermoValue, npPwrChannelN=npPwrChannelN, npRelHumSensorValueT=npRelHumSensorValueT, npResetStack=npResetStack, npPwrRepeatingResetsCounter=npPwrRepeatingResetsCounter, lightcom=lightcom, npRelHumSensor=npRelHumSensor, npSoftReboot=npSoftReboot, npRelHumSensorStatusH=npRelHumSensorStatusH, npRelHumSafeRangeHigh=npRelHumSafeRangeHigh, npRelHumTraps=npRelHumTraps, npIoLevelOut=npIoLevelOut, npReboot=npReboot, npRelayStartReset=npRelayStartReset, npTrapInfo=npTrapInfo, npPwrTable=npPwrTable, npPwrRelayFlip=npPwrRelayFlip, npThermoSensorN=npThermoSensorN, npIrStatus=npIrStatus, npForcedReboot=npForcedReboot, npThermoTrapStatus=npThermoTrapStatus, npIoTraps=npIoTraps)