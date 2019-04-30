#
# PySNMP MIB module HH3C-RMON-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-RMON-EXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:16:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
hh3crmonExtend, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3crmonExtend")
OwnerString, = mibBuilder.importSymbols("IF-MIB", "OwnerString")
EntryStatus, = mibBuilder.importSymbols("RMON-MIB", "EntryStatus")
trapDestEntry, trapDestIndex = mibBuilder.importSymbols("RMON2-MIB", "trapDestEntry", "trapDestIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, ModuleIdentity, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32, MibIdentifier, Gauge32, ObjectIdentity, iso, Bits, TimeTicks, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ModuleIdentity", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32", "MibIdentifier", "Gauge32", "ObjectIdentity", "iso", "Bits", "TimeTicks", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hh3cperformance = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 8, 4, 4))
hh3cperformance.setRevisions(('2003-03-15 00:00',))
if mibBuilder.loadTexts: hh3cperformance.setLastUpdated('200303150000Z')
if mibBuilder.loadTexts: hh3cperformance.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
hh3cprialarmTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1), )
if mibBuilder.loadTexts: hh3cprialarmTable.setStatus('current')
hh3cprialarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1), ).setIndexNames((0, "HH3C-RMON-EXT-MIB", "hh3cprialarmIndex"))
if mibBuilder.loadTexts: hh3cprialarmEntry.setStatus('current')
hh3cprialarmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cprialarmIndex.setStatus('current')
hh3cprialarmInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cprialarmInterval.setStatus('current')
hh3cprialarmVariable = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cprialarmVariable.setStatus('current')
hh3cprialarmSympol = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cprialarmSympol.setStatus('current')
hh3cprialarmSampleType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("absoluteValue", 1), ("deltaValue", 2), ("speedValue", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cprialarmSampleType.setStatus('current')
hh3cprialarmValue = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cprialarmValue.setStatus('current')
hh3cprialarmStartupAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("risingAlarm", 1), ("fallingAlarm", 2), ("risingOrFallingAlarm", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cprialarmStartupAlarm.setStatus('current')
hh3cprialarmRisingThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cprialarmRisingThreshold.setStatus('current')
hh3cprialarmFallingThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cprialarmFallingThreshold.setStatus('current')
hh3cprialarmRisingEventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cprialarmRisingEventIndex.setStatus('current')
hh3cprialarmFallingEventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cprialarmFallingEventIndex.setStatus('current')
hh3cprialarmStatCycle = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 12), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cprialarmStatCycle.setStatus('current')
hh3cprialarmStatType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("forever", 1), ("during", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cprialarmStatType.setStatus('current')
hh3cprialarmOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 14), OwnerString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cprialarmOwner.setStatus('current')
hh3cprialarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 15), EntryStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cprialarmStatus.setStatus('current')
hh3crmonEnableTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 4, 5), )
if mibBuilder.loadTexts: hh3crmonEnableTable.setStatus('current')
hh3crmonEnableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 4, 5, 1), ).setIndexNames((0, "HH3C-RMON-EXT-MIB", "hh3crmonEnableIfIndex"))
if mibBuilder.loadTexts: hh3crmonEnableEntry.setStatus('current')
hh3crmonEnableIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 4, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3crmonEnableIfIndex.setStatus('current')
hh3crmonEnableStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 4, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3crmonEnableStatus.setStatus('current')
hh3cTrapDestTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 4, 6), )
if mibBuilder.loadTexts: hh3cTrapDestTable.setStatus('current')
hh3cTrapDestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 4, 6, 1), )
trapDestEntry.registerAugmentions(("HH3C-RMON-EXT-MIB", "hh3cTrapDestEntry"))
hh3cTrapDestEntry.setIndexNames(*trapDestEntry.getIndexNames())
if mibBuilder.loadTexts: hh3cTrapDestEntry.setStatus('current')
hh3cTrapDestVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 4, 6, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("snmpv1", 1), ("snmpv2", 2), ("snmpv3andauthen", 3), ("snmpv3andnoauthen", 4), ("snmpv3andpriv", 5))).clone('snmpv1')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cTrapDestVersion.setStatus('current')
hh3crmonExtendEventsV2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 25506, 8, 4, 0))
if mibBuilder.loadTexts: hh3crmonExtendEventsV2.setStatus('current')
hh3cpririsingAlarm = NotificationType((1, 3, 6, 1, 4, 1, 25506, 8, 4, 0, 1)).setObjects(("HH3C-RMON-EXT-MIB", "hh3cprialarmIndex"), ("HH3C-RMON-EXT-MIB", "hh3cprialarmSympol"), ("HH3C-RMON-EXT-MIB", "hh3cprialarmSampleType"), ("HH3C-RMON-EXT-MIB", "hh3cprialarmValue"), ("HH3C-RMON-EXT-MIB", "hh3cprialarmRisingThreshold"))
if mibBuilder.loadTexts: hh3cpririsingAlarm.setStatus('current')
hh3cprifallingAlarm = NotificationType((1, 3, 6, 1, 4, 1, 25506, 8, 4, 0, 2)).setObjects(("HH3C-RMON-EXT-MIB", "hh3cprialarmIndex"), ("HH3C-RMON-EXT-MIB", "hh3cprialarmSympol"), ("HH3C-RMON-EXT-MIB", "hh3cprialarmSampleType"), ("HH3C-RMON-EXT-MIB", "hh3cprialarmValue"), ("HH3C-RMON-EXT-MIB", "hh3cprialarmFallingThreshold"))
if mibBuilder.loadTexts: hh3cprifallingAlarm.setStatus('current')
mibBuilder.exportSymbols("HH3C-RMON-EXT-MIB", hh3cprialarmSampleType=hh3cprialarmSampleType, hh3cprialarmEntry=hh3cprialarmEntry, hh3crmonEnableTable=hh3crmonEnableTable, hh3cTrapDestTable=hh3cTrapDestTable, hh3cTrapDestVersion=hh3cTrapDestVersion, hh3crmonEnableIfIndex=hh3crmonEnableIfIndex, hh3cprialarmStartupAlarm=hh3cprialarmStartupAlarm, hh3cprialarmOwner=hh3cprialarmOwner, hh3cprialarmValue=hh3cprialarmValue, hh3cprialarmInterval=hh3cprialarmInterval, hh3crmonEnableStatus=hh3crmonEnableStatus, hh3cprialarmStatCycle=hh3cprialarmStatCycle, hh3cprifallingAlarm=hh3cprifallingAlarm, PYSNMP_MODULE_ID=hh3cperformance, hh3cprialarmIndex=hh3cprialarmIndex, hh3cprialarmSympol=hh3cprialarmSympol, hh3cprialarmTable=hh3cprialarmTable, hh3cprialarmRisingEventIndex=hh3cprialarmRisingEventIndex, hh3cTrapDestEntry=hh3cTrapDestEntry, hh3crmonExtendEventsV2=hh3crmonExtendEventsV2, hh3cprialarmFallingThreshold=hh3cprialarmFallingThreshold, hh3cprialarmFallingEventIndex=hh3cprialarmFallingEventIndex, hh3cprialarmStatType=hh3cprialarmStatType, hh3cprialarmVariable=hh3cprialarmVariable, hh3cpririsingAlarm=hh3cpririsingAlarm, hh3cprialarmRisingThreshold=hh3cprialarmRisingThreshold, hh3crmonEnableEntry=hh3crmonEnableEntry, hh3cperformance=hh3cperformance, hh3cprialarmStatus=hh3cprialarmStatus)
