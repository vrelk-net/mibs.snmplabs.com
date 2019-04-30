#
# PySNMP MIB module XYLAN-DS1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XYLAN-DS1-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:38:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Gauge32, iso, TimeTicks, Counter64, NotificationType, ModuleIdentity, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Gauge32", "iso", "TimeTicks", "Counter64", "NotificationType", "ModuleIdentity", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
xylanPportArch, = mibBuilder.importSymbols("XYLAN-BASE-MIB", "xylanPportArch")
dsx1Port = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 11, 1))
dsx1PortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 1), )
if mibBuilder.loadTexts: dsx1PortConfigTable.setStatus('mandatory')
dsx1PortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 1, 1), ).setIndexNames((0, "XYLAN-DS1-MIB", "dsx1PortConfigSlotIndex"), (0, "XYLAN-DS1-MIB", "dsx1PortConfigPortIndex"))
if mibBuilder.loadTexts: dsx1PortConfigEntry.setStatus('mandatory')
dsx1PortConfigSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1PortConfigSlotIndex.setStatus('mandatory')
dsx1PortConfigPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1PortConfigPortIndex.setStatus('mandatory')
dsx1PortConfigIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("t1", 1), ("e1", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1PortConfigIfType.setStatus('mandatory')
dsx1PortFdlRole = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("network", 1), ("user", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1PortFdlRole.setStatus('mandatory')
dsx1PortNfasAlign = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1PortNfasAlign.setStatus('mandatory')
dsx1PortConfigYelAlarmDetectEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dsx1PortConfigYelAlarmDetectEnable.setStatus('mandatory')
dsx1PortStatsTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2), )
if mibBuilder.loadTexts: dsx1PortStatsTable.setStatus('mandatory')
dsx1PortStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1), ).setIndexNames((0, "XYLAN-DS1-MIB", "dsx1PortStatsSlotIndex"), (0, "XYLAN-DS1-MIB", "dsx1PortStatsPortIndex"))
if mibBuilder.loadTexts: dsx1PortStatsEntry.setStatus('mandatory')
dsx1PortStatsSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1PortStatsSlotIndex.setStatus('mandatory')
dsx1PortStatsPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1PortStatsPortIndex.setStatus('mandatory')
dsx1PortStatsLossOfSignal = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1PortStatsLossOfSignal.setStatus('mandatory')
dsx1PortStatsOutOfFrame = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1PortStatsOutOfFrame.setStatus('mandatory')
dsx1PortStatsRedAlarmEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1PortStatsRedAlarmEvent.setStatus('mandatory')
dsx1PortStatsYellowAlarmEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1PortStatsYellowAlarmEvent.setStatus('mandatory')
dsx1PortStatsSquelchAlarmEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1PortStatsSquelchAlarmEvent.setStatus('mandatory')
dsx1PortStatsBipolarVioEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1PortStatsBipolarVioEvent.setStatus('mandatory')
dsx1PortStatsAISEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1PortStatsAISEvent.setStatus('mandatory')
dsx1PortStatsCrcErrorEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1PortStatsCrcErrorEvent.setStatus('mandatory')
dsx1PortStatsOutOfSubMultiFrame = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1PortStatsOutOfSubMultiFrame.setStatus('mandatory')
dsx1PortStatsOutOfTs16MultiFrame = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1PortStatsOutOfTs16MultiFrame.setStatus('mandatory')
dsx1PortStatsRemFrameAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1PortStatsRemFrameAlarm.setStatus('mandatory')
dsx1PortStatsRemMultiFrameAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1PortStatsRemMultiFrameAlarm.setStatus('mandatory')
dsx1PortStatsFarEndBlkError = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1PortStatsFarEndBlkError.setStatus('mandatory')
dsx1PortStatsFramingBitError = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 1, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dsx1PortStatsFramingBitError.setStatus('mandatory')
mibBuilder.exportSymbols("XYLAN-DS1-MIB", dsx1PortStatsSlotIndex=dsx1PortStatsSlotIndex, dsx1PortStatsPortIndex=dsx1PortStatsPortIndex, dsx1PortStatsSquelchAlarmEvent=dsx1PortStatsSquelchAlarmEvent, dsx1PortStatsRemFrameAlarm=dsx1PortStatsRemFrameAlarm, dsx1PortConfigIfType=dsx1PortConfigIfType, dsx1PortStatsLossOfSignal=dsx1PortStatsLossOfSignal, dsx1PortStatsOutOfFrame=dsx1PortStatsOutOfFrame, dsx1PortStatsRedAlarmEvent=dsx1PortStatsRedAlarmEvent, dsx1PortConfigTable=dsx1PortConfigTable, dsx1PortConfigYelAlarmDetectEnable=dsx1PortConfigYelAlarmDetectEnable, dsx1PortConfigPortIndex=dsx1PortConfigPortIndex, dsx1PortConfigEntry=dsx1PortConfigEntry, dsx1Port=dsx1Port, dsx1PortStatsRemMultiFrameAlarm=dsx1PortStatsRemMultiFrameAlarm, dsx1PortFdlRole=dsx1PortFdlRole, dsx1PortStatsFramingBitError=dsx1PortStatsFramingBitError, dsx1PortNfasAlign=dsx1PortNfasAlign, dsx1PortStatsTable=dsx1PortStatsTable, dsx1PortStatsYellowAlarmEvent=dsx1PortStatsYellowAlarmEvent, dsx1PortStatsOutOfSubMultiFrame=dsx1PortStatsOutOfSubMultiFrame, dsx1PortStatsFarEndBlkError=dsx1PortStatsFarEndBlkError, dsx1PortStatsOutOfTs16MultiFrame=dsx1PortStatsOutOfTs16MultiFrame, dsx1PortStatsAISEvent=dsx1PortStatsAISEvent, dsx1PortStatsEntry=dsx1PortStatsEntry, dsx1PortStatsCrcErrorEvent=dsx1PortStatsCrcErrorEvent, dsx1PortStatsBipolarVioEvent=dsx1PortStatsBipolarVioEvent, dsx1PortConfigSlotIndex=dsx1PortConfigSlotIndex)