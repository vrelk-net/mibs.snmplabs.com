#
# PySNMP MIB module HMTRACKING-SNMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HMTRACKING-SNMP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:20:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
hmConfiguration, = mibBuilder.importSymbols("HMPRIV-MGMT-SNMP-MIB", "hmConfiguration")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, ObjectIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, MibIdentifier, TimeTicks, IpAddress, Gauge32, Counter64, Bits, ModuleIdentity, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ObjectIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "MibIdentifier", "TimeTicks", "IpAddress", "Gauge32", "Counter64", "Bits", "ModuleIdentity", "iso", "NotificationType")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
hmTracking = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 14, 15))
hmTracking.setRevisions(('2007-09-13 12:00',))
if mibBuilder.loadTexts: hmTracking.setLastUpdated('200709131200Z')
if mibBuilder.loadTexts: hmTracking.setOrganization('Hirschmann Automation and Control GmbH')
hmTrackingGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 14, 15, 1))
hmTrackingTable = MibTable((1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 1), )
if mibBuilder.loadTexts: hmTrackingTable.setStatus('current')
hmTrackingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 1, 1), ).setIndexNames((0, "HMTRACKING-SNMP-MIB", "hmTrackId"))
if mibBuilder.loadTexts: hmTrackingEntry.setStatus('current')
hmTrackId = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmTrackId.setStatus('current')
hmTrackRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 1, 1, 2), RowStatus().clone('notReady')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmTrackRowStatus.setStatus('current')
hmTrackType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("undefined", 1), ("interface", 2), ("ping", 3), ("logical", 4))).clone('undefined')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmTrackType.setStatus('current')
hmTrackState = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2))).clone('up')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmTrackState.setStatus('current')
hmTrackNumberOfChanges = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmTrackNumberOfChanges.setStatus('current')
hmTrackTimeSinceLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 1, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmTrackTimeSinceLastChange.setStatus('current')
hmTrackIfNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 1, 1, 7), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmTrackIfNumber.setStatus('current')
hmTrackIfLinkUpDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmTrackIfLinkUpDelay.setStatus('current')
hmTrackIfLinkDownDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmTrackIfLinkDownDelay.setStatus('current')
hmTrackPingIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 1, 1, 10), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmTrackPingIpAddress.setStatus('current')
hmTrackPingInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(1)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmTrackPingInterval.setStatus('current')
hmTrackPingMiss = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmTrackPingMiss.setStatus('current')
hmTrackPingSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmTrackPingSuccess.setStatus('current')
hmTrackPingTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 10000)).clone(100)).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmTrackPingTimeout.setStatus('current')
hmTrackPingTTL = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(128)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmTrackPingTTL.setStatus('current')
hmTrackPingBestRouteIfNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 1, 1, 16), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmTrackPingBestRouteIfNumber.setStatus('current')
hmTrackLogicalOperator = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("and", 1), ("or", 2))).clone('or')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmTrackLogicalOperator.setStatus('current')
hmTrackSendStateChangeTrap = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmTrackSendStateChangeTrap.setStatus('current')
hmTrackingApplicationTable = MibTable((1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 2), )
if mibBuilder.loadTexts: hmTrackingApplicationTable.setStatus('current')
hmTrackingApplicationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 2, 1), ).setIndexNames((0, "HMTRACKING-SNMP-MIB", "hmTrackId"), (0, "HMTRACKING-SNMP-MIB", "hmTrackAppId"))
if mibBuilder.loadTexts: hmTrackingApplicationEntry.setStatus('current')
hmTrackAppId = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 2, 1, 2), Integer32())
if mibBuilder.loadTexts: hmTrackAppId.setStatus('current')
hmTrackAppName = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmTrackAppName.setStatus('current')
hmTrackLogicalInstanceTable = MibTable((1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 3), )
if mibBuilder.loadTexts: hmTrackLogicalInstanceTable.setStatus('current')
hmTrackLogicalInstanceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 3, 1), ).setIndexNames((0, "HMTRACKING-SNMP-MIB", "hmTrackId"), (0, "HMTRACKING-SNMP-MIB", "hmTrackLogicalInstanceId"))
if mibBuilder.loadTexts: hmTrackLogicalInstanceEntry.setStatus('current')
hmTrackLogicalInstanceId = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 3, 1, 2), Integer32())
if mibBuilder.loadTexts: hmTrackLogicalInstanceId.setStatus('current')
hmTrackLogicInstRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 3, 1, 3), RowStatus().clone('notReady')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hmTrackLogicInstRowStatus.setStatus('current')
hmTrackEvent = ObjectIdentity((1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 0))
if mibBuilder.loadTexts: hmTrackEvent.setStatus('current')
hmTrackStatusChangeEvent = NotificationType((1, 3, 6, 1, 4, 1, 248, 14, 15, 1, 0, 1)).setObjects(("HMTRACKING-SNMP-MIB", "hmTrackId"), ("HMTRACKING-SNMP-MIB", "hmTrackRowStatus"), ("HMTRACKING-SNMP-MIB", "hmTrackState"))
if mibBuilder.loadTexts: hmTrackStatusChangeEvent.setStatus('current')
mibBuilder.exportSymbols("HMTRACKING-SNMP-MIB", hmTrackingGroup=hmTrackingGroup, hmTrackId=hmTrackId, hmTrackType=hmTrackType, hmTrackLogicalInstanceTable=hmTrackLogicalInstanceTable, hmTrackAppId=hmTrackAppId, hmTrackIfLinkDownDelay=hmTrackIfLinkDownDelay, hmTrackPingTTL=hmTrackPingTTL, hmTrackAppName=hmTrackAppName, hmTrackIfNumber=hmTrackIfNumber, hmTrackRowStatus=hmTrackRowStatus, hmTrackingEntry=hmTrackingEntry, hmTrackNumberOfChanges=hmTrackNumberOfChanges, hmTrackTimeSinceLastChange=hmTrackTimeSinceLastChange, hmTrackPingInterval=hmTrackPingInterval, hmTrackPingTimeout=hmTrackPingTimeout, hmTracking=hmTracking, hmTrackLogicalOperator=hmTrackLogicalOperator, hmTrackPingMiss=hmTrackPingMiss, hmTrackingApplicationTable=hmTrackingApplicationTable, hmTrackLogicalInstanceEntry=hmTrackLogicalInstanceEntry, hmTrackStatusChangeEvent=hmTrackStatusChangeEvent, hmTrackIfLinkUpDelay=hmTrackIfLinkUpDelay, hmTrackState=hmTrackState, hmTrackLogicalInstanceId=hmTrackLogicalInstanceId, hmTrackEvent=hmTrackEvent, hmTrackPingSuccess=hmTrackPingSuccess, hmTrackSendStateChangeTrap=hmTrackSendStateChangeTrap, hmTrackLogicInstRowStatus=hmTrackLogicInstRowStatus, hmTrackPingBestRouteIfNumber=hmTrackPingBestRouteIfNumber, hmTrackPingIpAddress=hmTrackPingIpAddress, hmTrackingApplicationEntry=hmTrackingApplicationEntry, hmTrackingTable=hmTrackingTable, PYSNMP_MODULE_ID=hmTracking)
