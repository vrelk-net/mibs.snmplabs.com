#
# PySNMP MIB module Nortel-MsCarrier-MscPassport-DataCollectionMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-MsCarrier-MscPassport-DataCollectionMIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:20:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
DisplayString, Integer32, RowStatus, Gauge32, Counter32, Unsigned32, StorageType = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB", "DisplayString", "Integer32", "RowStatus", "Gauge32", "Counter32", "Unsigned32", "StorageType")
AsciiString, EnterpriseDateAndTime, NonReplicated = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-TextualConventionsMIB", "AsciiString", "EnterpriseDateAndTime", "NonReplicated")
mscPassportMIBs, mscComponents = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB", "mscPassportMIBs", "mscComponents")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Counter64, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, IpAddress, iso, Gauge32, Counter32, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "IpAddress", "iso", "Gauge32", "Counter32", "Bits", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dataCollectionMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 14))
mscCol = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21))
mscColRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 1), )
if mibBuilder.loadTexts: mscColRowStatusTable.setStatus('mandatory')
mscColRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColIndex"))
if mibBuilder.loadTexts: mscColRowStatusEntry.setStatus('mandatory')
mscColRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscColRowStatus.setStatus('mandatory')
mscColComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscColComponentName.setStatus('mandatory')
mscColStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscColStorageType.setStatus('mandatory')
mscColIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("accounting", 0), ("alarm", 1), ("log", 2), ("debug", 3), ("scn", 4), ("trap", 5), ("stats", 6))))
if mibBuilder.loadTexts: mscColIndex.setStatus('mandatory')
mscColProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 10), )
if mibBuilder.loadTexts: mscColProvTable.setStatus('mandatory')
mscColProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 10, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColIndex"))
if mibBuilder.loadTexts: mscColProvEntry.setStatus('mandatory')
mscColAgentQueueSize = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 10, 1, 1), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(20, 10000), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscColAgentQueueSize.setStatus('obsolete')
mscColStatsTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 11), )
if mibBuilder.loadTexts: mscColStatsTable.setStatus('mandatory')
mscColStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 11, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColIndex"))
if mibBuilder.loadTexts: mscColStatsEntry.setStatus('mandatory')
mscColCurrentQueueSize = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 11, 1, 1), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscColCurrentQueueSize.setStatus('mandatory')
mscColRecordsRx = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 11, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscColRecordsRx.setStatus('mandatory')
mscColRecordsDiscarded = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 11, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscColRecordsDiscarded.setStatus('mandatory')
mscColTimesTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 266), )
if mibBuilder.loadTexts: mscColTimesTable.setStatus('mandatory')
mscColTimesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 266, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColIndex"), (0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColTimesValue"))
if mibBuilder.loadTexts: mscColTimesEntry.setStatus('mandatory')
mscColTimesValue = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 266, 1, 1), EnterpriseDateAndTime().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscColTimesValue.setStatus('mandatory')
mscColTimesRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 266, 1, 2), RowStatus()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: mscColTimesRowStatus.setStatus('mandatory')
mscColLastTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 275), )
if mibBuilder.loadTexts: mscColLastTable.setStatus('obsolete')
mscColLastEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 275, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColIndex"), (0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColLastValue"))
if mibBuilder.loadTexts: mscColLastEntry.setStatus('obsolete')
mscColLastValue = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 275, 1, 1), EnterpriseDateAndTime().subtype(subtypeSpec=ValueSizeConstraint(19, 19)).setFixedLength(19)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscColLastValue.setStatus('obsolete')
mscColPeakTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 279), )
if mibBuilder.loadTexts: mscColPeakTable.setStatus('mandatory')
mscColPeakEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 279, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColIndex"), (0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColPeakValue"))
if mibBuilder.loadTexts: mscColPeakEntry.setStatus('mandatory')
mscColPeakValue = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 279, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscColPeakValue.setStatus('mandatory')
mscColPeakRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 279, 1, 2), RowStatus()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: mscColPeakRowStatus.setStatus('mandatory')
mscColSp = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2))
mscColSpRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 1), )
if mibBuilder.loadTexts: mscColSpRowStatusTable.setStatus('mandatory')
mscColSpRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColIndex"), (0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColSpIndex"))
if mibBuilder.loadTexts: mscColSpRowStatusEntry.setStatus('mandatory')
mscColSpRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscColSpRowStatus.setStatus('mandatory')
mscColSpComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscColSpComponentName.setStatus('mandatory')
mscColSpStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscColSpStorageType.setStatus('mandatory')
mscColSpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: mscColSpIndex.setStatus('mandatory')
mscColSpProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 10), )
if mibBuilder.loadTexts: mscColSpProvTable.setStatus('mandatory')
mscColSpProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 10, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColIndex"), (0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColSpIndex"))
if mibBuilder.loadTexts: mscColSpProvEntry.setStatus('mandatory')
mscColSpSpooling = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 10, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscColSpSpooling.setStatus('mandatory')
mscColSpMaximumNumberOfFiles = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 10, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 200))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscColSpMaximumNumberOfFiles.setStatus('mandatory')
mscColSpStateTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 11), )
if mibBuilder.loadTexts: mscColSpStateTable.setStatus('mandatory')
mscColSpStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 11, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColIndex"), (0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColSpIndex"))
if mibBuilder.loadTexts: mscColSpStateEntry.setStatus('mandatory')
mscColSpAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 11, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("locked", 0), ("unlocked", 1), ("shuttingDown", 2))).clone('unlocked')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscColSpAdminState.setStatus('mandatory')
mscColSpOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 11, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscColSpOperationalState.setStatus('mandatory')
mscColSpUsageState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 11, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("idle", 0), ("active", 1), ("busy", 2))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscColSpUsageState.setStatus('mandatory')
mscColSpAvailabilityStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 11, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscColSpAvailabilityStatus.setStatus('mandatory')
mscColSpProceduralStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 11, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscColSpProceduralStatus.setStatus('mandatory')
mscColSpControlStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 11, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscColSpControlStatus.setStatus('mandatory')
mscColSpAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 11, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscColSpAlarmStatus.setStatus('mandatory')
mscColSpStandbyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 11, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 15))).clone(namedValues=NamedValues(("hotStandby", 0), ("coldStandby", 1), ("providingService", 2), ("notSet", 15))).clone('notSet')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscColSpStandbyStatus.setStatus('mandatory')
mscColSpUnknownStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 11, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1))).clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscColSpUnknownStatus.setStatus('mandatory')
mscColSpOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 12), )
if mibBuilder.loadTexts: mscColSpOperTable.setStatus('mandatory')
mscColSpOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 12, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColIndex"), (0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColSpIndex"))
if mibBuilder.loadTexts: mscColSpOperEntry.setStatus('mandatory')
mscColSpSpoolingFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 12, 1, 1), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscColSpSpoolingFileName.setStatus('mandatory')
mscColSpStatsTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 13), )
if mibBuilder.loadTexts: mscColSpStatsTable.setStatus('mandatory')
mscColSpStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 13, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColIndex"), (0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColSpIndex"))
if mibBuilder.loadTexts: mscColSpStatsEntry.setStatus('mandatory')
mscColSpCurrentQueueSize = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 13, 1, 1), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscColSpCurrentQueueSize.setStatus('mandatory')
mscColSpRecordsRx = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 13, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscColSpRecordsRx.setStatus('mandatory')
mscColSpRecordsDiscarded = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 2, 13, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscColSpRecordsDiscarded.setStatus('mandatory')
mscColAg = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 3))
mscColAgRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 3, 1), )
if mibBuilder.loadTexts: mscColAgRowStatusTable.setStatus('mandatory')
mscColAgRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 3, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColIndex"), (0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColAgIndex"))
if mibBuilder.loadTexts: mscColAgRowStatusEntry.setStatus('mandatory')
mscColAgRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 3, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscColAgRowStatus.setStatus('mandatory')
mscColAgComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 3, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscColAgComponentName.setStatus('mandatory')
mscColAgStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 3, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscColAgStorageType.setStatus('mandatory')
mscColAgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)))
if mibBuilder.loadTexts: mscColAgIndex.setStatus('mandatory')
mscColAgStatsTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 3, 10), )
if mibBuilder.loadTexts: mscColAgStatsTable.setStatus('mandatory')
mscColAgStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 3, 10, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColIndex"), (0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColAgIndex"))
if mibBuilder.loadTexts: mscColAgStatsEntry.setStatus('mandatory')
mscColAgCurrentQueueSize = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 3, 10, 1, 1), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscColAgCurrentQueueSize.setStatus('mandatory')
mscColAgRecordsRx = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 3, 10, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscColAgRecordsRx.setStatus('mandatory')
mscColAgRecordsDiscarded = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 3, 10, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscColAgRecordsDiscarded.setStatus('mandatory')
mscColAgAgentStatsTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 3, 11), )
if mibBuilder.loadTexts: mscColAgAgentStatsTable.setStatus('mandatory')
mscColAgAgentStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 3, 11, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColIndex"), (0, "Nortel-MsCarrier-MscPassport-DataCollectionMIB", "mscColAgIndex"))
if mibBuilder.loadTexts: mscColAgAgentStatsEntry.setStatus('mandatory')
mscColAgRecordsNotGenerated = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 21, 3, 11, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscColAgRecordsNotGenerated.setStatus('mandatory')
dataCollectionGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 14, 1))
dataCollectionGroupCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 14, 1, 1))
dataCollectionGroupCA02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 14, 1, 1, 3))
dataCollectionGroupCA02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 14, 1, 1, 3, 2))
dataCollectionCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 14, 3))
dataCollectionCapabilitiesCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 14, 3, 1))
dataCollectionCapabilitiesCA02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 14, 3, 1, 3))
dataCollectionCapabilitiesCA02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 14, 3, 1, 3, 2))
mibBuilder.exportSymbols("Nortel-MsCarrier-MscPassport-DataCollectionMIB", mscColProvEntry=mscColProvEntry, mscColSpUsageState=mscColSpUsageState, mscColAgRowStatus=mscColAgRowStatus, mscColIndex=mscColIndex, mscColSpProvEntry=mscColSpProvEntry, mscColSpStandbyStatus=mscColSpStandbyStatus, mscColAgComponentName=mscColAgComponentName, mscColCurrentQueueSize=mscColCurrentQueueSize, mscColAgCurrentQueueSize=mscColAgCurrentQueueSize, mscColStatsEntry=mscColStatsEntry, mscColStatsTable=mscColStatsTable, mscColSpSpoolingFileName=mscColSpSpoolingFileName, mscColAgStorageType=mscColAgStorageType, mscColAgRecordsRx=mscColAgRecordsRx, mscColPeakTable=mscColPeakTable, mscColSpRecordsDiscarded=mscColSpRecordsDiscarded, mscColSpControlStatus=mscColSpControlStatus, dataCollectionGroupCA02=dataCollectionGroupCA02, dataCollectionCapabilitiesCA02A=dataCollectionCapabilitiesCA02A, mscColAgAgentStatsEntry=mscColAgAgentStatsEntry, mscColSpOperTable=mscColSpOperTable, mscColSpOperationalState=mscColSpOperationalState, mscColAgRowStatusTable=mscColAgRowStatusTable, dataCollectionMIB=dataCollectionMIB, mscColAgRowStatusEntry=mscColAgRowStatusEntry, mscColAgRecordsDiscarded=mscColAgRecordsDiscarded, mscColSpAdminState=mscColSpAdminState, mscColAgStatsTable=mscColAgStatsTable, mscColSpAlarmStatus=mscColSpAlarmStatus, mscColTimesValue=mscColTimesValue, mscColAgAgentStatsTable=mscColAgAgentStatsTable, mscColTimesRowStatus=mscColTimesRowStatus, mscColTimesTable=mscColTimesTable, mscColAgIndex=mscColAgIndex, mscColLastEntry=mscColLastEntry, mscColPeakValue=mscColPeakValue, dataCollectionGroupCA=dataCollectionGroupCA, mscColSpSpooling=mscColSpSpooling, dataCollectionCapabilitiesCA02=dataCollectionCapabilitiesCA02, mscColSpMaximumNumberOfFiles=mscColSpMaximumNumberOfFiles, mscColSpProvTable=mscColSpProvTable, mscColSpAvailabilityStatus=mscColSpAvailabilityStatus, mscColSpCurrentQueueSize=mscColSpCurrentQueueSize, mscColSpStorageType=mscColSpStorageType, dataCollectionGroupCA02A=dataCollectionGroupCA02A, mscColAg=mscColAg, mscColSpUnknownStatus=mscColSpUnknownStatus, mscColAgStatsEntry=mscColAgStatsEntry, dataCollectionGroup=dataCollectionGroup, mscCol=mscCol, mscColSpOperEntry=mscColSpOperEntry, mscColSpRowStatusEntry=mscColSpRowStatusEntry, mscColSpStateEntry=mscColSpStateEntry, mscColAgRecordsNotGenerated=mscColAgRecordsNotGenerated, mscColSpStateTable=mscColSpStateTable, mscColSpRecordsRx=mscColSpRecordsRx, mscColSpRowStatusTable=mscColSpRowStatusTable, mscColSpComponentName=mscColSpComponentName, mscColSpProceduralStatus=mscColSpProceduralStatus, mscColRowStatusTable=mscColRowStatusTable, mscColPeakEntry=mscColPeakEntry, mscColLastValue=mscColLastValue, mscColRowStatusEntry=mscColRowStatusEntry, mscColAgentQueueSize=mscColAgentQueueSize, mscColLastTable=mscColLastTable, mscColRowStatus=mscColRowStatus, mscColTimesEntry=mscColTimesEntry, mscColSp=mscColSp, mscColPeakRowStatus=mscColPeakRowStatus, mscColStorageType=mscColStorageType, dataCollectionCapabilitiesCA=dataCollectionCapabilitiesCA, mscColSpRowStatus=mscColSpRowStatus, mscColComponentName=mscColComponentName, mscColSpIndex=mscColSpIndex, mscColRecordsRx=mscColRecordsRx, mscColSpStatsTable=mscColSpStatsTable, mscColProvTable=mscColProvTable, mscColSpStatsEntry=mscColSpStatsEntry, dataCollectionCapabilities=dataCollectionCapabilities, mscColRecordsDiscarded=mscColRecordsDiscarded)