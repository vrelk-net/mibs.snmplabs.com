#
# PySNMP MIB module CISCO-IF-MONITOR-NOTIF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IF-MONITOR-NOTIF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:44:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
MibIdentifier, Integer32, Unsigned32, Counter64, iso, ModuleIdentity, Bits, TimeTicks, IpAddress, Gauge32, NotificationType, ObjectIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Integer32", "Unsigned32", "Counter64", "iso", "ModuleIdentity", "Bits", "TimeTicks", "IpAddress", "Gauge32", "NotificationType", "ObjectIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TimeStamp", "DisplayString")
ciscoIfMonitorNotifMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 999))
ciscoIfMonitorNotifMIB.setRevisions(('2002-10-11 00:00',))
if mibBuilder.loadTexts: ciscoIfMonitorNotifMIB.setLastUpdated('200210110000Z')
if mibBuilder.loadTexts: ciscoIfMonitorNotifMIB.setOrganization('Cisco Systems, Inc.')
cIfMonNotifMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 999, 0))
cIfMonNotifMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 999, 1))
cIfMonNotifMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 999, 2))
cIfMonNotifCount = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cIfMonNotifCount.setStatus('current')
cIfMonNotifTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 2), )
if mibBuilder.loadTexts: cIfMonNotifTable.setStatus('current')
cIfMonNotifEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cIfMonNotifEntry.setStatus('current')
cIfMonNotifLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 2, 1, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cIfMonNotifLastChange.setStatus('current')
cIfMonNotifSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("red", 1), ("yellow", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cIfMonNotifSeverity.setStatus('current')
cIfMonNotifCause = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("aborts", 1), ("crc", 2), ("drops", 3), ("flaps", 4), ("frame-reject", 5), ("runts", 6), ("sabm", 7), ("frmr", 8), ("disc", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cIfMonNotifCause.setStatus('current')
cIfMonNotifValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 2, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cIfMonNotifValue.setStatus('current')
cIfMonNotifThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 2, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 100000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cIfMonNotifThreshold.setStatus('current')
cIfMonNotifInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 999, 1, 2, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(5, 600))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cIfMonNotifInterval.setStatus('current')
cIfMonNotifEvent = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 999, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("CISCO-IF-MONITOR-NOTIF-MIB", "cIfMonNotifCount"), ("CISCO-IF-MONITOR-NOTIF-MIB", "cIfMonNotifSeverity"), ("CISCO-IF-MONITOR-NOTIF-MIB", "cIfMonNotifCause"), ("CISCO-IF-MONITOR-NOTIF-MIB", "cIfMonNotifValue"), ("CISCO-IF-MONITOR-NOTIF-MIB", "cIfMonNotifThreshold"), ("CISCO-IF-MONITOR-NOTIF-MIB", "cIfMonNotifInterval"))
if mibBuilder.loadTexts: cIfMonNotifEvent.setStatus('current')
cIfMonNotifMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 1))
cIfMonNotifMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 2))
cIfMonNotifMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 1, 1)).setObjects(("CISCO-IF-MONITOR-NOTIF-MIB", "cIfMonNotifObjectGroup"), ("CISCO-IF-MONITOR-NOTIF-MIB", "cIfMonNotifEventGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIfMonNotifMIBCompliance = cIfMonNotifMIBCompliance.setStatus('current')
cIfMonNotifObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 2, 1)).setObjects(("CISCO-IF-MONITOR-NOTIF-MIB", "cIfMonNotifCount"), ("CISCO-IF-MONITOR-NOTIF-MIB", "cIfMonNotifLastChange"), ("CISCO-IF-MONITOR-NOTIF-MIB", "cIfMonNotifSeverity"), ("CISCO-IF-MONITOR-NOTIF-MIB", "cIfMonNotifCause"), ("CISCO-IF-MONITOR-NOTIF-MIB", "cIfMonNotifValue"), ("CISCO-IF-MONITOR-NOTIF-MIB", "cIfMonNotifThreshold"), ("CISCO-IF-MONITOR-NOTIF-MIB", "cIfMonNotifInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIfMonNotifObjectGroup = cIfMonNotifObjectGroup.setStatus('current')
cIfMonNotifEventGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 10, 999, 2, 2, 2)).setObjects(("CISCO-IF-MONITOR-NOTIF-MIB", "cIfMonNotifEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIfMonNotifEventGroup = cIfMonNotifEventGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-IF-MONITOR-NOTIF-MIB", cIfMonNotifThreshold=cIfMonNotifThreshold, cIfMonNotifMIBConformance=cIfMonNotifMIBConformance, cIfMonNotifEvent=cIfMonNotifEvent, cIfMonNotifMIBObjects=cIfMonNotifMIBObjects, cIfMonNotifEventGroup=cIfMonNotifEventGroup, cIfMonNotifMIBCompliance=cIfMonNotifMIBCompliance, cIfMonNotifEntry=cIfMonNotifEntry, cIfMonNotifCount=cIfMonNotifCount, cIfMonNotifTable=cIfMonNotifTable, cIfMonNotifObjectGroup=cIfMonNotifObjectGroup, cIfMonNotifLastChange=cIfMonNotifLastChange, ciscoIfMonitorNotifMIB=ciscoIfMonitorNotifMIB, cIfMonNotifMIBCompliances=cIfMonNotifMIBCompliances, cIfMonNotifMIBNotifications=cIfMonNotifMIBNotifications, cIfMonNotifInterval=cIfMonNotifInterval, cIfMonNotifMIBGroups=cIfMonNotifMIBGroups, cIfMonNotifCause=cIfMonNotifCause, PYSNMP_MODULE_ID=ciscoIfMonitorNotifMIB, cIfMonNotifSeverity=cIfMonNotifSeverity, cIfMonNotifValue=cIfMonNotifValue)
