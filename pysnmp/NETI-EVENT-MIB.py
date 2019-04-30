#
# PySNMP MIB module NETI-EVENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NETI-EVENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:09:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
netiGeneric, = mibBuilder.importSymbols("NETI-COMMON-MIB", "netiGeneric")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Gauge32, TimeTicks, IpAddress, Unsigned32, ModuleIdentity, iso, Bits, MibIdentifier, Counter32, Counter64, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "TimeTicks", "IpAddress", "Unsigned32", "ModuleIdentity", "iso", "Bits", "MibIdentifier", "Counter32", "Counter64", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DateAndTime, TruthValue, TextualConvention, DisplayString, RowPointer = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TruthValue", "TextualConvention", "DisplayString", "RowPointer")
netiEventMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2928, 2, 1))
netiEventMIB.setRevisions(('2011-05-03 10:00', '2009-07-09 16:00', '2007-03-06 00:00', '2004-09-10 00:00', '2003-11-25 00:00',))
if mibBuilder.loadTexts: netiEventMIB.setLastUpdated('201105031000Z')
if mibBuilder.loadTexts: netiEventMIB.setOrganization('Net Insight AB')
eventObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1))
eventNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 2, 1, 2))
eventConformanceGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 2, 1, 3))
class EventType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("created", 1), ("modified", 2), ("deleted", 3))

class AlarmType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("unknown", 0), ("communication", 1), ("qualityOfService", 2), ("processingError", 3), ("equipment", 4), ("environmental", 5))

class AlarmSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 0), ("indeterminate", 1), ("critical", 2), ("major", 3), ("minor", 4), ("warning", 5), ("cleared", 6))

class AlarmCause(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69))
    namedValues = NamedValues(("unknown", 0), ("adapterError", 1), ("applicationSubsystemFailure", 2), ("bandwidthReduced", 3), ("callEstablishmentError", 4), ("communicationsProtocolError", 5), ("communicationsSubsystemFailure", 6), ("configurationOrCustomizationError", 7), ("congestion", 8), ("corruptData", 9), ("cpuCyclesLimitExceeded", 10), ("datasetOrModemError", 11), ("degradedSignal", 12), ("dTEDCEInterfaceError", 13), ("enclosureDoorOpen", 14), ("equipmentMalfunction", 15), ("excessiveVibration", 16), ("fileError", 17), ("fireDetected", 18), ("floodDetected", 19), ("framingError", 20), ("heatingOrVentilationOrCoolingSystemProblem", 21), ("humidityUnacceptable", 22), ("inputOutputDeviceError", 23), ("inputDeviceError", 24), ("lANError", 25), ("leakDetected", 26), ("localNodeTransmissionError", 27), ("lossOfFrame", 28), ("lossOfSignal", 29), ("materialSupplyExhausted", 30), ("multiplexerProblem", 31), ("outOfMemory", 32), ("outputDeviceError", 33), ("performanceDegraded", 34), ("powerProblem", 35), ("pressureUnacceptable", 36), ("processorProblem", 37), ("pumpFailure", 38), ("queueSizeExceeded", 39), ("receiveFailure", 40), ("receiverFailure", 41), ("remoteNodeTransmissionError", 42), ("resourceAtOrNearingCapacity", 43), ("responseTimeExcessive", 44), ("retransmissionRateExcessive", 45), ("softwareError", 46), ("softwareProgramAbnormallyTerminated", 47), ("softwareProgramError", 48), ("storageCapacityProblem", 49), ("temperatureUnacceptable", 50), ("thresholdCrossed", 51), ("timingProblem", 52), ("toxicLeakDetected", 53), ("transmitFailure", 54), ("transmitterFailure", 55), ("underlyingResourceUnavailable", 56), ("versionMismatch", 57), ("phyLossOfSignal", 58), ("phyLossOfFrame", 59), ("phyAlarmIndicationSignal", 60), ("phyRemoteDefectIndication", 61), ("phySignalFailure", 62), ("phySignalDegraded", 63), ("testmodeEntered", 64), ("serviceUnavailable", 65), ("alarmIndicationSignal", 66), ("remoteDefectIndication", 67), ("replaceableUnitMissing", 68), ("replaceableUnitProblem", 69))

eventSequenceCounter = MibScalar((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventSequenceCounter.setStatus('current')
eventLogLastChangedTime = MibScalar((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventLogLastChangedTime.setStatus('current')
eventTable = MibTable((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 3), )
if mibBuilder.loadTexts: eventTable.setStatus('current')
eventEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 3, 1), ).setIndexNames((0, "NETI-EVENT-MIB", "eventIndex"))
if mibBuilder.loadTexts: eventEntry.setStatus('current')
eventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 3, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventIndex.setStatus('current')
eventObject = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 3, 1, 2), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventObject.setStatus('current')
eventObjectName = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventObjectName.setStatus('current')
eventAlarmType = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 3, 1, 4), AlarmType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventAlarmType.setStatus('current')
eventType = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 3, 1, 5), EventType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventType.setStatus('current')
eventCause = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 3, 1, 6), AlarmCause()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventCause.setStatus('current')
eventSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 3, 1, 7), AlarmSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventSeverity.setStatus('current')
eventText = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 3, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventText.setStatus('current')
eventCreatedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 3, 1, 9), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventCreatedTime.setStatus('current')
eventAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 4), )
if mibBuilder.loadTexts: eventAlarmTable.setStatus('current')
eventAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 4, 1), ).setIndexNames((0, "NETI-EVENT-MIB", "eventAlarmIndex"))
if mibBuilder.loadTexts: eventAlarmEntry.setStatus('current')
eventAlarmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 4, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventAlarmIndex.setStatus('current')
eventAlarmObject = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 4, 1, 2), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventAlarmObject.setStatus('current')
eventAlarmObjectName = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 4, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventAlarmObjectName.setStatus('current')
eventAlarmAlarmType = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 4, 1, 4), AlarmType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventAlarmAlarmType.setStatus('current')
eventAlarmCause = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 4, 1, 5), AlarmCause()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventAlarmCause.setStatus('current')
eventAlarmSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 4, 1, 6), AlarmSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventAlarmSeverity.setStatus('current')
eventAlarmText = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 4, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventAlarmText.setStatus('current')
eventAlarmLastChangedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 4, 1, 8), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventAlarmLastChangedTime.setStatus('current')
eventAlarmAcknowledged = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 4, 1, 9), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eventAlarmAcknowledged.setStatus('current')
eventAlarmCreatedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 4, 1, 10), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventAlarmCreatedTime.setStatus('current')
eventActiveAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 6), )
if mibBuilder.loadTexts: eventActiveAlarmTable.setStatus('current')
eventActiveAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 6, 1), ).setIndexNames((0, "NETI-EVENT-MIB", "eventActiveAlarmIndex"))
if mibBuilder.loadTexts: eventActiveAlarmEntry.setStatus('current')
eventActiveAlarmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 6, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventActiveAlarmIndex.setStatus('current')
eventActiveAlarmObject = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 6, 1, 2), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventActiveAlarmObject.setStatus('current')
eventActiveAlarmObjectName = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 6, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventActiveAlarmObjectName.setStatus('current')
eventActiveAlarmAlarmType = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 6, 1, 4), AlarmType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventActiveAlarmAlarmType.setStatus('current')
eventActiveAlarmCause = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 6, 1, 5), AlarmCause()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventActiveAlarmCause.setStatus('current')
eventActiveAlarmSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 6, 1, 6), AlarmSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventActiveAlarmSeverity.setStatus('current')
eventActiveAlarmText = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 6, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventActiveAlarmText.setStatus('current')
eventActiveAlarmLastChangedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 6, 1, 8), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventActiveAlarmLastChangedTime.setStatus('current')
eventActiveAlarmAcknowledged = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 6, 1, 9), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eventActiveAlarmAcknowledged.setStatus('current')
eventActiveAlarmCreatedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 6, 1, 10), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventActiveAlarmCreatedTime.setStatus('current')
eventAlarmCountersGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 5))
eventCriticalCounter = MibScalar((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 5, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventCriticalCounter.setStatus('current')
eventMajorCounter = MibScalar((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 5, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventMajorCounter.setStatus('current')
eventMinorCounter = MibScalar((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 5, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventMinorCounter.setStatus('current')
eventWarningCounter = MibScalar((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 5, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventWarningCounter.setStatus('current')
eventIndeterminateCounter = MibScalar((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 5, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventIndeterminateCounter.setStatus('current')
eventNotificationObjectsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 7))
eventTrapPurpose = MibScalar((1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 7, 1), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: eventTrapPurpose.setStatus('current')
eventAlarmCritical = NotificationType((1, 3, 6, 1, 4, 1, 2928, 2, 1, 2, 1)).setObjects(("NETI-EVENT-MIB", "eventIndex"), ("NETI-EVENT-MIB", "eventObject"), ("NETI-EVENT-MIB", "eventObjectName"), ("NETI-EVENT-MIB", "eventAlarmType"), ("NETI-EVENT-MIB", "eventCause"), ("NETI-EVENT-MIB", "eventSeverity"), ("NETI-EVENT-MIB", "eventText"), ("NETI-EVENT-MIB", "eventCreatedTime"), ("NETI-EVENT-MIB", "eventSequenceCounter"))
if mibBuilder.loadTexts: eventAlarmCritical.setStatus('current')
eventAlarmMajor = NotificationType((1, 3, 6, 1, 4, 1, 2928, 2, 1, 2, 2)).setObjects(("NETI-EVENT-MIB", "eventIndex"), ("NETI-EVENT-MIB", "eventObject"), ("NETI-EVENT-MIB", "eventObjectName"), ("NETI-EVENT-MIB", "eventAlarmType"), ("NETI-EVENT-MIB", "eventCause"), ("NETI-EVENT-MIB", "eventSeverity"), ("NETI-EVENT-MIB", "eventText"), ("NETI-EVENT-MIB", "eventCreatedTime"), ("NETI-EVENT-MIB", "eventSequenceCounter"))
if mibBuilder.loadTexts: eventAlarmMajor.setStatus('current')
eventAlarmMinor = NotificationType((1, 3, 6, 1, 4, 1, 2928, 2, 1, 2, 3)).setObjects(("NETI-EVENT-MIB", "eventIndex"), ("NETI-EVENT-MIB", "eventObject"), ("NETI-EVENT-MIB", "eventObjectName"), ("NETI-EVENT-MIB", "eventAlarmType"), ("NETI-EVENT-MIB", "eventCause"), ("NETI-EVENT-MIB", "eventSeverity"), ("NETI-EVENT-MIB", "eventText"), ("NETI-EVENT-MIB", "eventCreatedTime"), ("NETI-EVENT-MIB", "eventSequenceCounter"))
if mibBuilder.loadTexts: eventAlarmMinor.setStatus('current')
eventAlarmWarning = NotificationType((1, 3, 6, 1, 4, 1, 2928, 2, 1, 2, 4)).setObjects(("NETI-EVENT-MIB", "eventIndex"), ("NETI-EVENT-MIB", "eventObject"), ("NETI-EVENT-MIB", "eventObjectName"), ("NETI-EVENT-MIB", "eventAlarmType"), ("NETI-EVENT-MIB", "eventCause"), ("NETI-EVENT-MIB", "eventSeverity"), ("NETI-EVENT-MIB", "eventText"), ("NETI-EVENT-MIB", "eventCreatedTime"), ("NETI-EVENT-MIB", "eventSequenceCounter"))
if mibBuilder.loadTexts: eventAlarmWarning.setStatus('current')
eventAlarmIndeterminate = NotificationType((1, 3, 6, 1, 4, 1, 2928, 2, 1, 2, 5)).setObjects(("NETI-EVENT-MIB", "eventIndex"), ("NETI-EVENT-MIB", "eventObject"), ("NETI-EVENT-MIB", "eventObjectName"), ("NETI-EVENT-MIB", "eventAlarmType"), ("NETI-EVENT-MIB", "eventCause"), ("NETI-EVENT-MIB", "eventSeverity"), ("NETI-EVENT-MIB", "eventText"), ("NETI-EVENT-MIB", "eventCreatedTime"), ("NETI-EVENT-MIB", "eventSequenceCounter"))
if mibBuilder.loadTexts: eventAlarmIndeterminate.setStatus('current')
eventAlarmUnknown = NotificationType((1, 3, 6, 1, 4, 1, 2928, 2, 1, 2, 6)).setObjects(("NETI-EVENT-MIB", "eventIndex"), ("NETI-EVENT-MIB", "eventObject"), ("NETI-EVENT-MIB", "eventObjectName"), ("NETI-EVENT-MIB", "eventAlarmType"), ("NETI-EVENT-MIB", "eventCause"), ("NETI-EVENT-MIB", "eventSeverity"), ("NETI-EVENT-MIB", "eventText"), ("NETI-EVENT-MIB", "eventCreatedTime"), ("NETI-EVENT-MIB", "eventSequenceCounter"))
if mibBuilder.loadTexts: eventAlarmUnknown.setStatus('current')
eventAlarmClear = NotificationType((1, 3, 6, 1, 4, 1, 2928, 2, 1, 2, 7)).setObjects(("NETI-EVENT-MIB", "eventIndex"), ("NETI-EVENT-MIB", "eventObject"), ("NETI-EVENT-MIB", "eventObjectName"), ("NETI-EVENT-MIB", "eventAlarmType"), ("NETI-EVENT-MIB", "eventCause"), ("NETI-EVENT-MIB", "eventSeverity"), ("NETI-EVENT-MIB", "eventText"), ("NETI-EVENT-MIB", "eventCreatedTime"), ("NETI-EVENT-MIB", "eventSequenceCounter"))
if mibBuilder.loadTexts: eventAlarmClear.setStatus('current')
netiGenericEvent = NotificationType((1, 3, 6, 1, 4, 1, 2928, 2, 1, 2, 8)).setObjects(("NETI-EVENT-MIB", "eventObject"), ("NETI-EVENT-MIB", "eventObjectName"), ("NETI-EVENT-MIB", "eventType"), ("NETI-EVENT-MIB", "eventText"), ("NETI-EVENT-MIB", "eventCreatedTime"), ("NETI-EVENT-MIB", "eventSequenceCounter"))
if mibBuilder.loadTexts: netiGenericEvent.setStatus('current')
eventConformanceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2928, 2, 1, 3, 1)).setObjects(("NETI-EVENT-MIB", "eventSequenceCounter"), ("NETI-EVENT-MIB", "eventLogLastChangedTime"), ("NETI-EVENT-MIB", "eventIndex"), ("NETI-EVENT-MIB", "eventObject"), ("NETI-EVENT-MIB", "eventObjectName"), ("NETI-EVENT-MIB", "eventAlarmType"), ("NETI-EVENT-MIB", "eventType"), ("NETI-EVENT-MIB", "eventCause"), ("NETI-EVENT-MIB", "eventSeverity"), ("NETI-EVENT-MIB", "eventText"), ("NETI-EVENT-MIB", "eventCreatedTime"), ("NETI-EVENT-MIB", "eventAlarmIndex"), ("NETI-EVENT-MIB", "eventAlarmObject"), ("NETI-EVENT-MIB", "eventAlarmObjectName"), ("NETI-EVENT-MIB", "eventAlarmAlarmType"), ("NETI-EVENT-MIB", "eventAlarmCause"), ("NETI-EVENT-MIB", "eventAlarmSeverity"), ("NETI-EVENT-MIB", "eventAlarmText"), ("NETI-EVENT-MIB", "eventAlarmLastChangedTime"), ("NETI-EVENT-MIB", "eventAlarmAcknowledged"), ("NETI-EVENT-MIB", "eventAlarmCreatedTime"), ("NETI-EVENT-MIB", "eventActiveAlarmIndex"), ("NETI-EVENT-MIB", "eventActiveAlarmObject"), ("NETI-EVENT-MIB", "eventActiveAlarmObjectName"), ("NETI-EVENT-MIB", "eventActiveAlarmAlarmType"), ("NETI-EVENT-MIB", "eventActiveAlarmCause"), ("NETI-EVENT-MIB", "eventActiveAlarmSeverity"), ("NETI-EVENT-MIB", "eventActiveAlarmText"), ("NETI-EVENT-MIB", "eventActiveAlarmLastChangedTime"), ("NETI-EVENT-MIB", "eventActiveAlarmAcknowledged"), ("NETI-EVENT-MIB", "eventActiveAlarmCreatedTime"), ("NETI-EVENT-MIB", "eventCriticalCounter"), ("NETI-EVENT-MIB", "eventMajorCounter"), ("NETI-EVENT-MIB", "eventMinorCounter"), ("NETI-EVENT-MIB", "eventWarningCounter"), ("NETI-EVENT-MIB", "eventIndeterminateCounter"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    eventConformanceGroup = eventConformanceGroup.setStatus('current')
eventNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2928, 2, 1, 3, 2)).setObjects(("NETI-EVENT-MIB", "eventAlarmCritical"), ("NETI-EVENT-MIB", "eventAlarmMajor"), ("NETI-EVENT-MIB", "eventAlarmMinor"), ("NETI-EVENT-MIB", "eventAlarmWarning"), ("NETI-EVENT-MIB", "eventAlarmIndeterminate"), ("NETI-EVENT-MIB", "eventAlarmUnknown"), ("NETI-EVENT-MIB", "eventAlarmClear"), ("NETI-EVENT-MIB", "netiGenericEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    eventNotificationsGroup = eventNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("NETI-EVENT-MIB", eventAlarmIndeterminate=eventAlarmIndeterminate, eventActiveAlarmObjectName=eventActiveAlarmObjectName, eventCreatedTime=eventCreatedTime, PYSNMP_MODULE_ID=netiEventMIB, eventCause=eventCause, eventAlarmWarning=eventAlarmWarning, eventAlarmObject=eventAlarmObject, eventAlarmEntry=eventAlarmEntry, eventAlarmCountersGroup=eventAlarmCountersGroup, eventNotifications=eventNotifications, eventText=eventText, eventAlarmCause=eventAlarmCause, eventConformanceGroups=eventConformanceGroups, eventActiveAlarmObject=eventActiveAlarmObject, eventAlarmCreatedTime=eventAlarmCreatedTime, eventActiveAlarmCause=eventActiveAlarmCause, eventAlarmClear=eventAlarmClear, eventAlarmText=eventAlarmText, eventAlarmAlarmType=eventAlarmAlarmType, eventActiveAlarmLastChangedTime=eventActiveAlarmLastChangedTime, eventMinorCounter=eventMinorCounter, eventMajorCounter=eventMajorCounter, eventNotificationsGroup=eventNotificationsGroup, eventIndeterminateCounter=eventIndeterminateCounter, eventAlarmIndex=eventAlarmIndex, AlarmType=AlarmType, eventTable=eventTable, eventIndex=eventIndex, eventSeverity=eventSeverity, eventActiveAlarmAcknowledged=eventActiveAlarmAcknowledged, EventType=EventType, eventAlarmType=eventAlarmType, eventAlarmLastChangedTime=eventAlarmLastChangedTime, eventEntry=eventEntry, eventActiveAlarmIndex=eventActiveAlarmIndex, eventActiveAlarmText=eventActiveAlarmText, AlarmCause=AlarmCause, eventLogLastChangedTime=eventLogLastChangedTime, eventObject=eventObject, eventAlarmTable=eventAlarmTable, eventCriticalCounter=eventCriticalCounter, eventConformanceGroup=eventConformanceGroup, eventActiveAlarmAlarmType=eventActiveAlarmAlarmType, eventSequenceCounter=eventSequenceCounter, eventActiveAlarmSeverity=eventActiveAlarmSeverity, eventObjectName=eventObjectName, eventActiveAlarmTable=eventActiveAlarmTable, eventAlarmCritical=eventAlarmCritical, netiEventMIB=netiEventMIB, eventAlarmSeverity=eventAlarmSeverity, eventWarningCounter=eventWarningCounter, eventNotificationObjectsGroup=eventNotificationObjectsGroup, eventTrapPurpose=eventTrapPurpose, eventAlarmMajor=eventAlarmMajor, netiGenericEvent=netiGenericEvent, eventAlarmAcknowledged=eventAlarmAcknowledged, eventAlarmUnknown=eventAlarmUnknown, eventObjects=eventObjects, eventActiveAlarmEntry=eventActiveAlarmEntry, AlarmSeverity=AlarmSeverity, eventAlarmObjectName=eventAlarmObjectName, eventAlarmMinor=eventAlarmMinor, eventActiveAlarmCreatedTime=eventActiveAlarmCreatedTime, eventType=eventType)
