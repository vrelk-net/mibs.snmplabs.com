#
# PySNMP MIB module COM21-HCXALM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/COM21-HCXALM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:10:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
com21Hcx, com21 = mibBuilder.importSymbols("COM21-HCX-MIB", "com21Hcx", "com21")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, MibIdentifier, NotificationType, iso, ModuleIdentity, Bits, TimeTicks, Counter32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "MibIdentifier", "NotificationType", "iso", "ModuleIdentity", "Bits", "TimeTicks", "Counter32", "Unsigned32")
MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString")
com21HcxAlm = ModuleIdentity((1, 3, 6, 1, 4, 1, 1141, 2, 11))
if mibBuilder.loadTexts: com21HcxAlm.setLastUpdated('9701080000Z')
if mibBuilder.loadTexts: com21HcxAlm.setOrganization('Com21, Inc.')
com21HcxCurrAlmGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1141, 2, 15))
com21HcxEventLogGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1141, 2, 16))
com21HcxAlmSeverityGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1141, 2, 17))
class EpochTime(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class AlarmSeverity(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("clear", 1), ("warning", 2), ("minor", 3), ("major", 4), ("critical", 5))

com21HcxCurrAlmTable = MibTable((1, 3, 6, 1, 4, 1, 1141, 2, 15, 1), )
if mibBuilder.loadTexts: com21HcxCurrAlmTable.setStatus('current')
com21HcxAlmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1141, 2, 15, 1, 1), ).setIndexNames((0, "COM21-HCXALM-MIB", "hcxAlmTrapId"), (0, "COM21-HCXALM-MIB", "hcxAlmShelfId"), (0, "COM21-HCXALM-MIB", "hcxAlmSlotId"), (0, "COM21-HCXALM-MIB", "hcxAlmPortId"))
if mibBuilder.loadTexts: com21HcxAlmEntry.setStatus('current')
hcxAlmTrapId = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 15, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxAlmTrapId.setStatus('current')
hcxAlmSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 15, 1, 1, 2), AlarmSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxAlmSeverity.setStatus('current')
hcxAlmTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 15, 1, 1, 3), EpochTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxAlmTime.setStatus('current')
hcxAlmShelfId = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 15, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxAlmShelfId.setStatus('current')
hcxAlmSlotId = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 15, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxAlmSlotId.setStatus('current')
hcxAlmPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 15, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxAlmPortId.setStatus('current')
hcxAlmMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 15, 1, 1, 7), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxAlmMacAddr.setStatus('current')
hcxAlmDataAValid = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 15, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxAlmDataAValid.setStatus('current')
hcxAlmDataA = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 15, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxAlmDataA.setStatus('current')
hcxAlmDataBValid = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 15, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxAlmDataBValid.setStatus('current')
hcxAlmDataB = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 15, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxAlmDataB.setStatus('current')
hcxAlmStrDataValid = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 15, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxAlmStrDataValid.setStatus('current')
hcxAlmStrData = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 15, 1, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxAlmStrData.setStatus('current')
com21HcxEventLogTable = MibTable((1, 3, 6, 1, 4, 1, 1141, 2, 16, 1), )
if mibBuilder.loadTexts: com21HcxEventLogTable.setStatus('current')
com21HcxEventLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1141, 2, 16, 1, 1), ).setIndexNames((0, "COM21-HCXALM-MIB", "hcxEventLogId"))
if mibBuilder.loadTexts: com21HcxEventLogEntry.setStatus('current')
hcxEventLogId = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 16, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxEventLogId.setStatus('current')
hcxEventLogSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 16, 1, 1, 2), AlarmSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxEventLogSeverity.setStatus('current')
hcxEventLogTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 16, 1, 1, 3), EpochTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxEventLogTime.setStatus('current')
hcxEventLogShelfId = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 16, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxEventLogShelfId.setStatus('current')
hcxEventLogSlotId = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 16, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxEventLogSlotId.setStatus('current')
hcxEventLogPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 16, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxEventLogPortId.setStatus('current')
hcxEventLogMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 16, 1, 1, 7), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxEventLogMacAddr.setStatus('current')
hcxEventLogTrapId = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 16, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxEventLogTrapId.setStatus('current')
hcxEventLogDataAValid = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 16, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxEventLogDataAValid.setStatus('current')
hcxEventLogDataA = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 16, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxEventLogDataA.setStatus('current')
hcxEventLogDataBValid = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 16, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxEventLogDataBValid.setStatus('current')
hcxEventLogDataB = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 16, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxEventLogDataB.setStatus('current')
hcxEventStrDataValid = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 16, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxEventStrDataValid.setStatus('current')
hcxEventStrData = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 16, 1, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxEventStrData.setStatus('current')
com21HcxAlmSeverityTable = MibTable((1, 3, 6, 1, 4, 1, 1141, 2, 17, 1), )
if mibBuilder.loadTexts: com21HcxAlmSeverityTable.setStatus('current')
com21HcxAlmSeverityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1141, 2, 17, 1, 1), ).setIndexNames((0, "COM21-HCXALM-MIB", "hcxAlmSevTrapId"))
if mibBuilder.loadTexts: com21HcxAlmSeverityEntry.setStatus('current')
hcxAlmSevTrapId = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 17, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcxAlmSevTrapId.setStatus('current')
hcxSetAlmSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 1141, 2, 17, 1, 1, 2), AlarmSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hcxSetAlmSeverity.setStatus('current')
mibBuilder.exportSymbols("COM21-HCXALM-MIB", com21HcxEventLogGroup=com21HcxEventLogGroup, hcxEventLogShelfId=hcxEventLogShelfId, com21HcxAlmEntry=com21HcxAlmEntry, hcxAlmDataB=hcxAlmDataB, com21HcxEventLogEntry=com21HcxEventLogEntry, hcxEventLogTrapId=hcxEventLogTrapId, hcxAlmTrapId=hcxAlmTrapId, hcxAlmSeverity=hcxAlmSeverity, EpochTime=EpochTime, hcxAlmSlotId=hcxAlmSlotId, com21HcxEventLogTable=com21HcxEventLogTable, hcxEventLogPortId=hcxEventLogPortId, com21HcxAlmSeverityTable=com21HcxAlmSeverityTable, com21HcxAlmSeverityGroup=com21HcxAlmSeverityGroup, AlarmSeverity=AlarmSeverity, hcxEventLogMacAddr=hcxEventLogMacAddr, hcxEventLogDataA=hcxEventLogDataA, hcxAlmStrData=hcxAlmStrData, hcxAlmDataA=hcxAlmDataA, com21HcxCurrAlmGroup=com21HcxCurrAlmGroup, hcxEventLogSlotId=hcxEventLogSlotId, hcxAlmSevTrapId=hcxAlmSevTrapId, hcxEventLogDataAValid=hcxEventLogDataAValid, hcxEventLogSeverity=hcxEventLogSeverity, hcxEventLogTime=hcxEventLogTime, com21HcxCurrAlmTable=com21HcxCurrAlmTable, hcxAlmDataBValid=hcxAlmDataBValid, hcxEventLogId=hcxEventLogId, hcxAlmStrDataValid=hcxAlmStrDataValid, hcxAlmMacAddr=hcxAlmMacAddr, hcxAlmShelfId=hcxAlmShelfId, hcxEventLogDataBValid=hcxEventLogDataBValid, hcxAlmPortId=hcxAlmPortId, com21HcxAlmSeverityEntry=com21HcxAlmSeverityEntry, com21HcxAlm=com21HcxAlm, hcxEventLogDataB=hcxEventLogDataB, hcxEventStrData=hcxEventStrData, hcxEventStrDataValid=hcxEventStrDataValid, hcxAlmDataAValid=hcxAlmDataAValid, PYSNMP_MODULE_ID=com21HcxAlm, hcxSetAlmSeverity=hcxSetAlmSeverity, hcxAlmTime=hcxAlmTime)
