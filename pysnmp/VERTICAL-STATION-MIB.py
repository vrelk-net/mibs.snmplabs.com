#
# PySNMP MIB module VERTICAL-STATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VERTICAL-STATION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:27:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, ModuleIdentity, iso, Bits, Counter64, ObjectIdentity, enterprises, Integer32, Unsigned32, IpAddress, Gauge32, NotificationType, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "ModuleIdentity", "iso", "Bits", "Counter64", "ObjectIdentity", "enterprises", "Integer32", "Unsigned32", "IpAddress", "Gauge32", "NotificationType", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
vertical = MibIdentifier((1, 3, 6, 1, 4, 1, 2338))
vStationModule = MibIdentifier((1, 3, 6, 1, 4, 1, 2338, 7))
vStationCommonGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2338, 7, 1))
vStationFirstDigitTimeout = MibScalar((1, 3, 6, 1, 4, 1, 2338, 7, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vStationFirstDigitTimeout.setStatus('mandatory')
vStationDigitTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vStationDigitTimeout.setStatus('mandatory')
vStationOffHookTimeout = MibScalar((1, 3, 6, 1, 4, 1, 2338, 7, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vStationOffHookTimeout.setStatus('mandatory')
vStationNumStationCards = MibScalar((1, 3, 6, 1, 4, 1, 2338, 7, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vStationNumStationCards.setStatus('mandatory')
vStationExternalDialDigit = MibScalar((1, 3, 6, 1, 4, 1, 2338, 7, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vStationExternalDialDigit.setStatus('mandatory')
vStationCardGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2338, 7, 2))
vStationCardTable = MibTable((1, 3, 6, 1, 4, 1, 2338, 7, 2, 1), )
if mibBuilder.loadTexts: vStationCardTable.setStatus('current')
vStationCardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2338, 7, 2, 1, 1), ).setIndexNames((0, "VERTICAL-STATION-MIB", "vStationCardSlotNumber"))
if mibBuilder.loadTexts: vStationCardEntry.setStatus('mandatory')
vStationCardSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 14))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationCardSlotNumber.setStatus('mandatory')
vStationCardType = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 4))).clone(namedValues=NamedValues(("card-type-NOT-CONFIGURED", 0), ("card-type-24-CHANNEL-STATION", 2), ("card-type-BRIDGE1", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationCardType.setStatus('mandatory')
vStationCardIOPortAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationCardIOPortAddress.setStatus('mandatory')
vStationCardState = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 255))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1), ("removed", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationCardState.setStatus('mandatory')
vStationCardErrorLED = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationCardErrorLED.setStatus('mandatory')
vStationCardReadyLED = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationCardReadyLED.setStatus('mandatory')
vStationDeviceTable = MibTable((1, 3, 6, 1, 4, 1, 2338, 7, 2, 2), )
if mibBuilder.loadTexts: vStationDeviceTable.setStatus('current')
vStationDeviceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2338, 7, 2, 2, 1), ).setIndexNames((0, "VERTICAL-STATION-MIB", "vStationDeviceSlotNumber"))
if mibBuilder.loadTexts: vStationDeviceEntry.setStatus('mandatory')
vStationDeviceSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationDeviceSlotNumber.setStatus('mandatory')
vStationDeviceDeviceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationDeviceDeviceNumber.setStatus('mandatory')
vStationDeviceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationDeviceIfIndex.setStatus('mandatory')
vStationDeviceBaseIOAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationDeviceBaseIOAddress.setStatus('mandatory')
vStationDeviceEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vStationDeviceEnabled.setStatus('mandatory')
vStationDeviceInterrupt = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationDeviceInterrupt.setStatus('mandatory')
vStationDeviceNumChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationDeviceNumChannels.setStatus('mandatory')
vStationDeviceMVIPStartingChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationDeviceMVIPStartingChannel.setStatus('mandatory')
vStationDeviceMVIPStream = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationDeviceMVIPStream.setStatus('mandatory')
vStationDeviceType = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 8))).clone(namedValues=NamedValues(("dev-undef", 0), ("dev-station", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationDeviceType.setStatus('mandatory')
vStationDeviceChangePending = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vStationDeviceChangePending.setStatus('mandatory')
vStationChannelTable = MibTable((1, 3, 6, 1, 4, 1, 2338, 7, 2, 3), )
if mibBuilder.loadTexts: vStationChannelTable.setStatus('current')
vStationChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2338, 7, 2, 3, 1), ).setIndexNames((0, "VERTICAL-STATION-MIB", "vStationChannelSlotNumber"), (0, "VERTICAL-STATION-MIB", "vStationChannelIndex"))
if mibBuilder.loadTexts: vStationChannelEntry.setStatus('mandatory')
vStationChannelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationChannelIndex.setStatus('mandatory')
vStationChannelSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationChannelSlotNumber.setStatus('mandatory')
vStationChannelDeviceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationChannelDeviceNumber.setStatus('mandatory')
vStationChannelChannelType = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("loopStart", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vStationChannelChannelType.setStatus('mandatory')
vStationChannelMWIType = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("stutter", 1), ("lamp", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vStationChannelMWIType.setStatus('mandatory')
vStationChannelOperationMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("station", 1), ("voiceMail", 2), ("pBX", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vStationChannelOperationMode.setStatus('mandatory')
vStationChannelState = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1), ("notConfigured", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vStationChannelState.setStatus('mandatory')
vStationChannelType = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("basic", 1), ("callerID", 2), ("callerID-callWaiting", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vStationChannelType.setStatus('mandatory')
vStationChannelCallState = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22))).clone(namedValues=NamedValues(("call-state-VOID", 0), ("call-state-IDLE", 1), ("call-state-DIALING", 2), ("call-state-COLLECT-FIRST-DIGIT", 3), ("call-state-COLLECT-DIGITS", 4), ("call-state-CALL-OFFERED", 5), ("call-state-PROCEEDING", 6), ("call-state-RINGING", 7), ("call-state-ALERTING", 8), ("call-state-CONNECTED", 9), ("call-state-DISCONNECTING", 10), ("call-state-FAILED", 11), ("call-state-UNAVAILABLE", 12), ("call-state-OFFHOOK", 13), ("call-state-INITIALIZE", 14), ("call-state-INITIALIZING", 15), ("call-state-DIAL-REQUEST", 16), ("call-state-HELD", 17), ("call-state-FEATURE-INVOKED", 18), ("call-state-OFFHOOK-IDLE", 19), ("call-state-OFFHOOK-ACTIVE", 20), ("call-state-OUT-OF-SERVICE", 21), ("call-state-OUTPULSING", 22)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationChannelCallState.setStatus('mandatory')
vStationChannelCalledPartyNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 3, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationChannelCalledPartyNumber.setStatus('mandatory')
vStationChannelCallingPartyNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 3, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationChannelCallingPartyNumber.setStatus('mandatory')
vStationChannelChangePending = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 2, 3, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vStationChannelChangePending.setStatus('mandatory')
vStationDigitTableGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2338, 7, 3))
vStationFirstDigitTable = MibTable((1, 3, 6, 1, 4, 1, 2338, 7, 3, 1), )
if mibBuilder.loadTexts: vStationFirstDigitTable.setStatus('current')
vStationFirstDigitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2338, 7, 3, 1, 1), ).setIndexNames((0, "VERTICAL-STATION-MIB", "vStationDigitIndex"))
if mibBuilder.loadTexts: vStationFirstDigitEntry.setStatus('mandatory')
vStationDigitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationDigitIndex.setStatus('mandatory')
vStationDigitString = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 3, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationDigitString.setStatus('mandatory')
vStationDigitCallType = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("fc-VOID", 0), ("fc-HOLD-CALL", 1), ("fc-PARK-CALL", 2), ("fc-STATION-CALL", 3), ("fc-LONG-DISTANCE-CALL", 4), ("fc-INTERNATIONAL-CALL", 5), ("fc-LOCAL-CALL", 6), ("fc-OPERATOR-CALL", 7), ("fc-RECEPTIONIST-CALL", 8), ("fc-CAMP-ON-CALL", 9)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vStationDigitCallType.setStatus('mandatory')
vStationDigitMoreDigits = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vStationDigitMoreDigits.setStatus('mandatory')
vStationDigitTimeout2 = MibScalar((1, 3, 6, 1, 4, 1, 2338, 7, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("dontTerminate", 0), ("terminate", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vStationDigitTimeout2.setStatus('mandatory')
vStationDigitStripDigits = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vStationDigitStripDigits.setStatus('mandatory')
vStationExtVoiceMailGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2338, 7, 4))
vStationATTSystem25Group = MibIdentifier((1, 3, 6, 1, 4, 1, 2338, 7, 4, 1))
vStationMWILampON = MibScalar((1, 3, 6, 1, 4, 1, 2338, 7, 4, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vStationMWILampON.setStatus('mandatory')
vStationMWILampOFF = MibScalar((1, 3, 6, 1, 4, 1, 2338, 7, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vStationMWILampOFF.setStatus('mandatory')
vStationVMCallHandleTable = MibTable((1, 3, 6, 1, 4, 1, 2338, 7, 4, 1, 3), )
if mibBuilder.loadTexts: vStationVMCallHandleTable.setStatus('current')
vStationVMCallHandleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2338, 7, 4, 1, 3, 1), ).setIndexNames((0, "VERTICAL-STATION-MIB", "vStationVMCallHandleIndex"))
if mibBuilder.loadTexts: vStationVMCallHandleEntry.setStatus('mandatory')
vStationVMCallHandleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 4, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationVMCallHandleIndex.setStatus('mandatory')
vStationVMCallHandleType = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 4, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("directExternal", 1), ("forwardExternal", 2), ("directInternal", 3), ("forwardInternal", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vStationVMCallHandleType.setStatus('mandatory')
vStationVMCallHandleOpcode = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 4, 1, 3, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vStationVMCallHandleOpcode.setStatus('mandatory')
vStationVMCallHandleSRCNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 4, 1, 3, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vStationVMCallHandleSRCNumber.setStatus('mandatory')
vStationVMCallHandleDSTNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2338, 7, 4, 1, 3, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vStationVMCallHandleDSTNumber.setStatus('mandatory')
vStationCannotPlayTone = NotificationType((1, 3, 6, 1, 4, 1, 2338) + (0,12)).setObjects(("VERTICAL-STATION-MIB", "vStationChannelSlotNumber"), ("VERTICAL-STATION-MIB", "vStationChannelDeviceNumber"), ("VERTICAL-STATION-MIB", "vStationChannelIndex"))
vStationCannotCancelTone = NotificationType((1, 3, 6, 1, 4, 1, 2338) + (0,13)).setObjects(("VERTICAL-STATION-MIB", "vStationChannelSlotNumber"), ("VERTICAL-STATION-MIB", "vStationChannelDeviceNumber"), ("VERTICAL-STATION-MIB", "vStationChannelIndex"))
vStationCannotAttachDigitCollector = NotificationType((1, 3, 6, 1, 4, 1, 2338) + (0,14)).setObjects(("VERTICAL-STATION-MIB", "vStationChannelSlotNumber"), ("VERTICAL-STATION-MIB", "vStationChannelDeviceNumber"), ("VERTICAL-STATION-MIB", "vStationChannelIndex"))
vStationCannotReleaseDigitCollector = NotificationType((1, 3, 6, 1, 4, 1, 2338) + (0,15)).setObjects(("VERTICAL-STATION-MIB", "vStationChannelSlotNumber"), ("VERTICAL-STATION-MIB", "vStationChannelDeviceNumber"), ("VERTICAL-STATION-MIB", "vStationChannelIndex"))
vStationRECONFIG_COMPLETE = NotificationType((1, 3, 6, 1, 4, 1, 2338) + (0,16)).setLabel("vStationRECONFIG-COMPLETE").setObjects(("VERTICAL-STATION-MIB", "vStationChannelSlotNumber"), ("VERTICAL-STATION-MIB", "vStationChannelDeviceNumber"))
vStationRECONFIG_ERROR = NotificationType((1, 3, 6, 1, 4, 1, 2338) + (0,17)).setLabel("vStationRECONFIG-ERROR").setObjects(("VERTICAL-STATION-MIB", "vStationChannelSlotNumber"), ("VERTICAL-STATION-MIB", "vStationChannelDeviceNumber"))
mibBuilder.exportSymbols("VERTICAL-STATION-MIB", vStationMWILampON=vStationMWILampON, vStationVMCallHandleSRCNumber=vStationVMCallHandleSRCNumber, vStationChannelChangePending=vStationChannelChangePending, vStationFirstDigitTable=vStationFirstDigitTable, vStationChannelDeviceNumber=vStationChannelDeviceNumber, vStationDigitMoreDigits=vStationDigitMoreDigits, vStationVMCallHandleEntry=vStationVMCallHandleEntry, vStationCannotAttachDigitCollector=vStationCannotAttachDigitCollector, vStationDeviceTable=vStationDeviceTable, vertical=vertical, vStationChannelCallState=vStationChannelCallState, vStationNumStationCards=vStationNumStationCards, vStationDeviceEntry=vStationDeviceEntry, vStationDeviceEnabled=vStationDeviceEnabled, vStationDeviceChangePending=vStationDeviceChangePending, vStationDigitStripDigits=vStationDigitStripDigits, vStationChannelChannelType=vStationChannelChannelType, vStationChannelMWIType=vStationChannelMWIType, vStationFirstDigitEntry=vStationFirstDigitEntry, vStationDeviceMVIPStream=vStationDeviceMVIPStream, vStationChannelTable=vStationChannelTable, vStationDeviceIfIndex=vStationDeviceIfIndex, vStationVMCallHandleType=vStationVMCallHandleType, vStationDigitIndex=vStationDigitIndex, vStationCannotReleaseDigitCollector=vStationCannotReleaseDigitCollector, vStationDeviceDeviceNumber=vStationDeviceDeviceNumber, vStationRECONFIG_ERROR=vStationRECONFIG_ERROR, vStationCardReadyLED=vStationCardReadyLED, vStationCardState=vStationCardState, vStationModule=vStationModule, vStationDigitTimeout2=vStationDigitTimeout2, vStationDeviceNumChannels=vStationDeviceNumChannels, vStationChannelCallingPartyNumber=vStationChannelCallingPartyNumber, vStationChannelSlotNumber=vStationChannelSlotNumber, vStationDeviceBaseIOAddress=vStationDeviceBaseIOAddress, vStationCardSlotNumber=vStationCardSlotNumber, vStationDeviceMVIPStartingChannel=vStationDeviceMVIPStartingChannel, vStationOffHookTimeout=vStationOffHookTimeout, vStationVMCallHandleIndex=vStationVMCallHandleIndex, vStationFirstDigitTimeout=vStationFirstDigitTimeout, vStationChannelCalledPartyNumber=vStationChannelCalledPartyNumber, vStationVMCallHandleOpcode=vStationVMCallHandleOpcode, vStationCardTable=vStationCardTable, vStationCardGroup=vStationCardGroup, vStationChannelType=vStationChannelType, vStationCannotCancelTone=vStationCannotCancelTone, vStationChannelOperationMode=vStationChannelOperationMode, vStationCardEntry=vStationCardEntry, vStationExtVoiceMailGroup=vStationExtVoiceMailGroup, vStationDeviceInterrupt=vStationDeviceInterrupt, vStationChannelEntry=vStationChannelEntry, vStationExternalDialDigit=vStationExternalDialDigit, vStationVMCallHandleTable=vStationVMCallHandleTable, vStationCannotPlayTone=vStationCannotPlayTone, vStationCardErrorLED=vStationCardErrorLED, vStationATTSystem25Group=vStationATTSystem25Group, vStationDigitTimeout=vStationDigitTimeout, vStationChannelIndex=vStationChannelIndex, vStationDigitString=vStationDigitString, vStationCommonGroup=vStationCommonGroup, vStationDeviceSlotNumber=vStationDeviceSlotNumber, vStationDeviceType=vStationDeviceType, vStationChannelState=vStationChannelState, vStationCardType=vStationCardType, vStationDigitTableGroup=vStationDigitTableGroup, vStationDigitCallType=vStationDigitCallType, vStationMWILampOFF=vStationMWILampOFF, vStationRECONFIG_COMPLETE=vStationRECONFIG_COMPLETE, vStationCardIOPortAddress=vStationCardIOPortAddress, vStationVMCallHandleDSTNumber=vStationVMCallHandleDSTNumber)
