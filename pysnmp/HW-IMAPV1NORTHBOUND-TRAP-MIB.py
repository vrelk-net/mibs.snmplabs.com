#
# PySNMP MIB module HW-IMAPV1NORTHBOUND-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HW-IMAPV1NORTHBOUND-TRAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:38:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, NotificationType, Counter64, iso, ObjectIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Gauge32, Integer32, enterprises, Counter32, MibIdentifier, Unsigned32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "Counter64", "iso", "ObjectIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Gauge32", "Integer32", "enterprises", "Counter32", "MibIdentifier", "Unsigned32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
huawei = MibIdentifier((1, 3, 6, 1, 4, 1, 2011))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2))
hwNetManagement = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 15))
hwNmAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1))
hwNmFault = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 3))
thirdNMSFaultFilter = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 3, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(14, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: thirdNMSFaultFilter.setStatus('mandatory')
hwNmNorthboundEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7))
hwNmNorthboundEventInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1))
hwNmNorthboundNEName = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNmNorthboundNEName.setStatus('mandatory')
hwNmNorthboundNEType = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNmNorthboundNEType.setStatus('mandatory')
hwNmNorthboundObjectInstance = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNmNorthboundObjectInstance.setStatus('mandatory')
hwNmNorthboundEventType = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNmNorthboundEventType.setStatus('mandatory')
hwNmNorthboundEventTime = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNmNorthboundEventTime.setStatus('mandatory')
hwNmNorthboundProbableCause = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNmNorthboundProbableCause.setStatus('mandatory')
hwNmNorthboundSeverity = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNmNorthboundSeverity.setStatus('mandatory')
hwNmNorthboundEventDetail = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNmNorthboundEventDetail.setStatus('mandatory')
hwNmNorthboundAdditionalInfo = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNmNorthboundAdditionalInfo.setStatus('mandatory')
hwNmNorthboundFaultFlag = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNmNorthboundFaultFlag.setStatus('mandatory')
hwNmNorthboundFaultFunction = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNmNorthboundFaultFunction.setStatus('mandatory')
hwNmNorthboundDeviceIP = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 12), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNmNorthboundDeviceIP.setStatus('mandatory')
hwNmNorthboundSerialNo = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNmNorthboundSerialNo.setStatus('mandatory')
hwNmNorthboundProbableRepair = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNmNorthboundProbableRepair.setStatus('mandatory')
hwNmNorthboundResourceIDs = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 15), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNmNorthboundResourceIDs.setStatus('mandatory')
hwNmNorthboundsAdditionalVB1 = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 16), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNmNorthboundsAdditionalVB1.setStatus('mandatory')
hwNmNorthboundsAdditionalVB2 = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 17), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNmNorthboundsAdditionalVB2.setStatus('mandatory')
hwNmNorthboundsAdditionalVB3 = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 18), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNmNorthboundsAdditionalVB3.setStatus('mandatory')
hwNmNorthboundsAdditionalVB4 = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 19), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNmNorthboundsAdditionalVB4.setStatus('mandatory')
hwNmNorthboundsAdditionalVB5 = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 20), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNmNorthboundsAdditionalVB5.setStatus('mandatory')
hwNmNorthboundsAdditionalVB6 = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 21), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNmNorthboundsAdditionalVB6.setStatus('mandatory')
hwNmNorthboundsAdditionalVB7 = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 22), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNmNorthboundsAdditionalVB7.setStatus('mandatory')
hwNmNorthboundsAdditionalVB8 = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 23), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNmNorthboundsAdditionalVB8.setStatus('mandatory')
hwNmNorthboundEventName = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1, 24), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNmNorthboundEventName.setStatus('mandatory')
hwNmNorthboundEventKeepAliveInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 2))
hwNmNorthboundEventSynchronization = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 7))
hwNmNorthboundEventSynchronizationStart = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 7, 1))
hwNmNorthboundEventSynchronizationQueryResult = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 7, 2))
hwNmNorthboundEventSynchronizationEnd = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 7, 3))
hwNmNorthboundEventSynchronizationEndStatus = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 7, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normalEnd", 1), ("stopped", 2), ("error", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNmNorthboundEventSynchronizationEndStatus.setStatus('mandatory')
hwNmNorthboundEventSynchronizationEndStatusDetail = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 7, 3, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwNmNorthboundEventSynchronizationEndStatusDetail.setStatus('mandatory')
hwNmNorthboundEventSynchronizationCommandStart = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 7, 4), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwNmNorthboundEventSynchronizationCommandStart.setStatus('mandatory')
hwNmNorthboundEventSynchronizationCommandStop = MibScalar((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 7, 5), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwNmNorthboundEventSynchronizationCommandStop.setStatus('mandatory')
hwNmNorthboundEventNotify = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1) + (0,1)).setObjects(("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundNEName"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundNEType"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundObjectInstance"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventType"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventTime"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundProbableCause"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundSeverity"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventDetail"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundAdditionalInfo"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundFaultFlag"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundFaultFunction"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundDeviceIP"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundSerialNo"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundProbableRepair"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundResourceIDs"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB1"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB2"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB3"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB4"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB5"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB6"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB7"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB8"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventName"))
hwNmNorthboundEventKeepAlive = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 2) + (0,2))
hwNmNorthboundEventNotifyCritical = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1) + (0,3)).setObjects(("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundNEName"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundNEType"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundObjectInstance"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventType"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventTime"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundProbableCause"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundSeverity"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventDetail"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundAdditionalInfo"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundFaultFlag"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundFaultFunction"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundDeviceIP"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundSerialNo"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundProbableRepair"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundResourceIDs"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB1"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB2"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB3"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB4"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB5"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB6"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB7"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB8"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventName"))
hwNmNorthboundEventNotifyMajor = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1) + (0,4)).setObjects(("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundNEName"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundNEType"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundObjectInstance"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventType"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventTime"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundProbableCause"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundSeverity"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventDetail"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundAdditionalInfo"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundFaultFlag"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundFaultFunction"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundDeviceIP"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundSerialNo"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundProbableRepair"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundResourceIDs"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB1"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB2"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB3"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB4"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB5"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB6"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB7"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB8"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventName"))
hwNmNorthboundEventNotifyMinor = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1) + (0,5)).setObjects(("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundNEName"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundNEType"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundObjectInstance"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventType"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventTime"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundProbableCause"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundSeverity"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventDetail"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundAdditionalInfo"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundFaultFlag"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundFaultFunction"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundDeviceIP"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundSerialNo"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundProbableRepair"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundResourceIDs"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB1"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB2"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB3"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB4"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB5"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB6"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB7"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB8"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventName"))
hwNmNorthboundEventNotifyWarning = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1) + (0,6)).setObjects(("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundNEName"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundNEType"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundObjectInstance"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventType"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventTime"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundProbableCause"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundSeverity"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventDetail"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundAdditionalInfo"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundFaultFlag"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundFaultFunction"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundDeviceIP"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundSerialNo"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundProbableRepair"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundResourceIDs"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB1"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB2"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB3"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB4"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB5"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB6"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB7"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB8"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventName"))
hwNmNorthboundEventNotifyIndefinitely = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1) + (0,7)).setObjects(("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundNEName"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundNEType"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundObjectInstance"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventType"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventTime"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundProbableCause"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundSeverity"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventDetail"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundAdditionalInfo"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundFaultFlag"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundFaultFunction"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundDeviceIP"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundSerialNo"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundProbableRepair"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundResourceIDs"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB1"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB2"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB3"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB4"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB5"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB6"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB7"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB8"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventName"))
hwNmNorthboundEventNotifyUnknownSeverity = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 1) + (0,8)).setObjects(("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundNEName"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundNEType"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundObjectInstance"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventType"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventTime"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundProbableCause"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundSeverity"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventDetail"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundAdditionalInfo"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundFaultFlag"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundFaultFunction"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundDeviceIP"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundSerialNo"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundProbableRepair"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundResourceIDs"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB1"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB2"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB3"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB4"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB5"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB6"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB7"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB8"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventName"))
hwNmNorthboundEventSynchronizationStartNotify = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 7, 1) + (0,9))
hwNmNorthboundEventSynchronizationQueryResultNotify = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 7, 2) + (0,10)).setObjects(("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundNEName"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundNEType"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundObjectInstance"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventType"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventTime"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundProbableCause"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundSeverity"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventDetail"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundAdditionalInfo"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundFaultFlag"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundFaultFunction"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundDeviceIP"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundSerialNo"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundProbableRepair"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundResourceIDs"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB1"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB2"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB3"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB4"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB5"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB6"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB7"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundsAdditionalVB8"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventName"))
hwNmNorthboundEventSynchronizationEndNotify = NotificationType((1, 3, 6, 1, 4, 1, 2011, 2, 15, 1, 7, 7, 3) + (0,11)).setObjects(("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventSynchronizationEndStatus"), ("HW-IMAPV1NORTHBOUND-TRAP-MIB", "hwNmNorthboundEventSynchronizationEndStatusDetail"))
mibBuilder.exportSymbols("HW-IMAPV1NORTHBOUND-TRAP-MIB", hwNmNorthboundEventNotifyUnknownSeverity=hwNmNorthboundEventNotifyUnknownSeverity, hwNmNorthboundProbableCause=hwNmNorthboundProbableCause, hwNmNorthboundEventSynchronizationQueryResultNotify=hwNmNorthboundEventSynchronizationQueryResultNotify, hwNmNorthboundsAdditionalVB7=hwNmNorthboundsAdditionalVB7, hwNmNorthboundEventNotifyCritical=hwNmNorthboundEventNotifyCritical, hwNmNorthboundsAdditionalVB6=hwNmNorthboundsAdditionalVB6, hwNmNorthboundAdditionalInfo=hwNmNorthboundAdditionalInfo, hwNmNorthboundNEType=hwNmNorthboundNEType, hwNmNorthboundDeviceIP=hwNmNorthboundDeviceIP, hwNmNorthboundsAdditionalVB3=hwNmNorthboundsAdditionalVB3, hwNmNorthboundEvent=hwNmNorthboundEvent, hwNmNorthboundsAdditionalVB8=hwNmNorthboundsAdditionalVB8, hwNmNorthboundEventKeepAliveInfo=hwNmNorthboundEventKeepAliveInfo, hwNmNorthboundEventSynchronization=hwNmNorthboundEventSynchronization, hwNmNorthboundEventSynchronizationEnd=hwNmNorthboundEventSynchronizationEnd, hwNmNorthboundEventNotify=hwNmNorthboundEventNotify, hwNmNorthboundFaultFlag=hwNmNorthboundFaultFlag, hwNetManagement=hwNetManagement, hwNmNorthboundNEName=hwNmNorthboundNEName, hwNmNorthboundEventSynchronizationStart=hwNmNorthboundEventSynchronizationStart, hwNmNorthboundObjectInstance=hwNmNorthboundObjectInstance, hwNmNorthboundEventSynchronizationEndStatus=hwNmNorthboundEventSynchronizationEndStatus, hwNmNorthboundSerialNo=hwNmNorthboundSerialNo, hwNmNorthboundResourceIDs=hwNmNorthboundResourceIDs, hwNmNorthboundEventSynchronizationCommandStop=hwNmNorthboundEventSynchronizationCommandStop, hwNmNorthboundEventInfo=hwNmNorthboundEventInfo, hwNmNorthboundEventSynchronizationEndStatusDetail=hwNmNorthboundEventSynchronizationEndStatusDetail, hwNmNorthboundsAdditionalVB4=hwNmNorthboundsAdditionalVB4, hwNmNorthboundEventTime=hwNmNorthboundEventTime, hwNmNorthboundEventKeepAlive=hwNmNorthboundEventKeepAlive, hwNmNorthboundProbableRepair=hwNmNorthboundProbableRepair, hwNmNorthboundEventType=hwNmNorthboundEventType, hwNmNorthboundSeverity=hwNmNorthboundSeverity, hwNmNorthboundEventNotifyWarning=hwNmNorthboundEventNotifyWarning, huawei=huawei, hwNmNorthboundsAdditionalVB2=hwNmNorthboundsAdditionalVB2, hwNmNorthboundsAdditionalVB5=hwNmNorthboundsAdditionalVB5, hwNmNorthboundEventNotifyMajor=hwNmNorthboundEventNotifyMajor, hwNmNorthboundEventSynchronizationCommandStart=hwNmNorthboundEventSynchronizationCommandStart, hwNmNorthboundEventNotifyMinor=hwNmNorthboundEventNotifyMinor, hwNmNorthboundEventSynchronizationEndNotify=hwNmNorthboundEventSynchronizationEndNotify, hwNmNorthboundEventSynchronizationQueryResult=hwNmNorthboundEventSynchronizationQueryResult, hwNmAgent=hwNmAgent, thirdNMSFaultFilter=thirdNMSFaultFilter, hwNmFault=hwNmFault, hwNmNorthboundEventName=hwNmNorthboundEventName, hwNmNorthboundEventNotifyIndefinitely=hwNmNorthboundEventNotifyIndefinitely, hwNmNorthboundEventSynchronizationStartNotify=hwNmNorthboundEventSynchronizationStartNotify, hwNmNorthboundsAdditionalVB1=hwNmNorthboundsAdditionalVB1, products=products, hwNmNorthboundEventDetail=hwNmNorthboundEventDetail, hwNmNorthboundFaultFunction=hwNmNorthboundFaultFunction)
