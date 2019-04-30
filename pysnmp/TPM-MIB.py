#
# PySNMP MIB module TPM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:18:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
apmExceptionGroup, apmExceptionIndex, TransactionAggregationType, DataSourceOrZero, apmReportGroup, apmAppDirAppLocalIndex, RmonClientID, apmAppDirResponsivenessType, AppLocalIndex = mibBuilder.importSymbols("APM-MIB", "apmExceptionGroup", "apmExceptionIndex", "TransactionAggregationType", "DataSourceOrZero", "apmReportGroup", "apmAppDirAppLocalIndex", "RmonClientID", "apmAppDirResponsivenessType", "AppLocalIndex")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ZeroBasedCounter64, = mibBuilder.importSymbols("HCNUM-TC", "ZeroBasedCounter64")
rmon, OwnerString = mibBuilder.importSymbols("RMON-MIB", "rmon", "OwnerString")
ZeroBasedCounter32, protocolDirLocalIndex = mibBuilder.importSymbols("RMON2-MIB", "ZeroBasedCounter32", "protocolDirLocalIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ObjectIdentity, MibIdentifier, Bits, IpAddress, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, iso, Gauge32, ModuleIdentity, Counter32, NotificationType, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibIdentifier", "Bits", "IpAddress", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "iso", "Gauge32", "ModuleIdentity", "Counter32", "NotificationType", "Unsigned32")
TextualConvention, TimeStamp, RowStatus, DisplayString, StorageType = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TimeStamp", "RowStatus", "DisplayString", "StorageType")
SspmMicroSeconds, SspmClockMaxSkew, SspmClockSource = mibBuilder.importSymbols("SSPM-MIB", "SspmMicroSeconds", "SspmClockMaxSkew", "SspmClockSource")
tpmMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 16, 30))
tpmMIB.setRevisions(('2005-07-28 00:00',))
if mibBuilder.loadTexts: tpmMIB.setLastUpdated('200507280000Z')
if mibBuilder.loadTexts: tpmMIB.setOrganization('IETF RMON MIB Working Group')
tpmCapabilities = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 30, 1))
tpmReports = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 30, 2))
tpmConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 30, 3))
class TpmTransactionMetricIndex(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 65535)

class TpmMetricDefID(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

tpmClockResolution = MibScalar((1, 3, 6, 1, 2, 1, 16, 30, 1, 1), SspmMicroSeconds()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmClockResolution.setStatus('current')
tpmClockMaxSkew = MibScalar((1, 3, 6, 1, 2, 1, 16, 30, 1, 2), SspmClockMaxSkew()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmClockMaxSkew.setStatus('current')
tpmClockSource = MibScalar((1, 3, 6, 1, 2, 1, 16, 30, 1, 3), SspmClockSource()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmClockSource.setStatus('current')
tpmTransMetricDirLastChange = MibScalar((1, 3, 6, 1, 2, 1, 16, 30, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmTransMetricDirLastChange.setStatus('current')
tpmTransMetricDirTable = MibTable((1, 3, 6, 1, 2, 1, 16, 30, 1, 5), )
if mibBuilder.loadTexts: tpmTransMetricDirTable.setStatus('current')
tpmTransMetricDirEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 30, 1, 5, 1), ).setIndexNames((0, "TPM-MIB", "tpmTransMetricAppLocalIndex"), (0, "TPM-MIB", "tpmTransMetricIndex"))
if mibBuilder.loadTexts: tpmTransMetricDirEntry.setStatus('current')
tpmTransMetricAppLocalIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 1, 5, 1, 1), AppLocalIndex())
if mibBuilder.loadTexts: tpmTransMetricAppLocalIndex.setStatus('current')
tpmTransMetricIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 1, 5, 1, 2), TpmTransactionMetricIndex())
if mibBuilder.loadTexts: tpmTransMetricIndex.setStatus('current')
tpmTransMetricProtocolIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 1, 5, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmTransMetricProtocolIndex.setStatus('current')
tpmTransMetricMetricIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 1, 5, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmTransMetricMetricIndex.setStatus('current')
tpmTransMetricDirConfig = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 1, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("supportedOff", 2), ("supportedOn", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpmTransMetricDirConfig.setStatus('current')
tpmMetricDefTable = MibTable((1, 3, 6, 1, 2, 1, 16, 30, 1, 6), )
if mibBuilder.loadTexts: tpmMetricDefTable.setStatus('current')
tpmMetricDefEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 30, 1, 6, 1), ).setIndexNames((0, "TPM-MIB", "tpmMetricDefinitionID"))
if mibBuilder.loadTexts: tpmMetricDefEntry.setStatus('current')
tpmMetricDefinitionID = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 1, 6, 1, 1), TpmMetricDefID())
if mibBuilder.loadTexts: tpmMetricDefinitionID.setStatus('current')
tpmMetricDefType = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 1, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("connectMetric", 2), ("delayMetric", 3), ("lossMetric", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmMetricDefType.setStatus('current')
tpmMetricDefDirType = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 1, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("oneWay", 1), ("twoWay", 2), ("multiWay", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmMetricDefDirType.setStatus('current')
tpmMetricDefName = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 1, 6, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmMetricDefName.setStatus('current')
tpmMetricDefReference = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 1, 6, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmMetricDefReference.setStatus('current')
tpmMetricDefGlobalID = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 1, 6, 1, 6), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmMetricDefGlobalID.setStatus('current')
tpmAggrReportCntrlTable = MibTable((1, 3, 6, 1, 2, 1, 16, 30, 2, 1), )
if mibBuilder.loadTexts: tpmAggrReportCntrlTable.setStatus('current')
tpmAggrReportCntrlEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 30, 2, 1, 1), ).setIndexNames((0, "TPM-MIB", "tpmAggrReportCntrlIndex"))
if mibBuilder.loadTexts: tpmAggrReportCntrlEntry.setStatus('current')
tpmAggrReportCntrlIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: tpmAggrReportCntrlIndex.setStatus('current')
tpmAggrReportCntrlApmCntrlIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpmAggrReportCntrlApmCntrlIndex.setStatus('current')
tpmAggrReportCntrlDataSource = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 1, 1, 3), DataSourceOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpmAggrReportCntrlDataSource.setStatus('current')
tpmAggrReportCntrlAggrType = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 1, 1, 4), TransactionAggregationType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpmAggrReportCntrlAggrType.setStatus('current')
tpmAggrReportCntrlInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 1, 1, 5), Unsigned32().clone(3600)).setUnits('Seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpmAggrReportCntrlInterval.setStatus('current')
tpmAggrReportCntrlReqSize = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 1, 1, 6), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpmAggrReportCntrlReqSize.setStatus('current')
tpmAggrReportCntrlGrantedSize = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmAggrReportCntrlGrantedSize.setStatus('current')
tpmAggrReportCntrlReqReports = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpmAggrReportCntrlReqReports.setStatus('current')
tpmAggrReportCntrlGrantedReports = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 1, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmAggrReportCntrlGrantedReports.setStatus('current')
tpmAggrReportCntrlStartTime = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 1, 1, 10), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmAggrReportCntrlStartTime.setStatus('current')
tpmAggrReportCntrlReportNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 1, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmAggrReportCntrlReportNumber.setStatus('current')
tpmAggrReportCntrlInsertsDenied = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmAggrReportCntrlInsertsDenied.setStatus('current')
tpmAggrReportCntrlDroppedFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmAggrReportCntrlDroppedFrames.setStatus('current')
tpmAggrReportCntrlOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 1, 1, 14), OwnerString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpmAggrReportCntrlOwner.setStatus('current')
tpmAggrReportCntrlStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 1, 1, 15), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpmAggrReportCntrlStorageType.setStatus('current')
tpmAggrReportCntrlStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 1, 1, 16), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tpmAggrReportCntrlStatus.setStatus('current')
tpmAggrReportTable = MibTable((1, 3, 6, 1, 2, 1, 16, 30, 2, 2), )
if mibBuilder.loadTexts: tpmAggrReportTable.setStatus('current')
tpmAggrReportEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1), ).setIndexNames((0, "TPM-MIB", "tpmAggrReportCntrlIndex"), (0, "TPM-MIB", "tpmAggrReportIndex"), (0, "TPM-MIB", "tpmAggrReportAppLocalIndex"), (0, "TPM-MIB", "tpmAggrReportTransMetricIndex"), (0, "RMON2-MIB", "protocolDirLocalIndex"), (0, "TPM-MIB", "tpmAggrReportServerAddress"), (0, "TPM-MIB", "tpmAggrReportApmNameClientID"))
if mibBuilder.loadTexts: tpmAggrReportEntry.setStatus('current')
tpmAggrReportIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: tpmAggrReportIndex.setStatus('current')
tpmAggrReportAppLocalIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1, 2), AppLocalIndex())
if mibBuilder.loadTexts: tpmAggrReportAppLocalIndex.setStatus('current')
tpmAggrReportTransMetricIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1, 3), TpmTransactionMetricIndex())
if mibBuilder.loadTexts: tpmAggrReportTransMetricIndex.setStatus('current')
tpmAggrReportServerAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 108)))
if mibBuilder.loadTexts: tpmAggrReportServerAddress.setStatus('current')
tpmAggrReportApmNameClientID = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1, 5), RmonClientID())
if mibBuilder.loadTexts: tpmAggrReportApmNameClientID.setStatus('current')
tpmAggrReportStatN = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1, 6), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmAggrReportStatN.setStatus('current')
tpmAggrReportOverflowStatN = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1, 7), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmAggrReportOverflowStatN.setStatus('current')
tpmAggrReportHCStatN = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1, 8), ZeroBasedCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmAggrReportHCStatN.setStatus('current')
tpmAggrReportStatSumX = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1, 9), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmAggrReportStatSumX.setStatus('current')
tpmAggrReportOverflowStatSumX = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1, 10), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmAggrReportOverflowStatSumX.setStatus('current')
tpmAggrReportHCStatSumX = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1, 11), ZeroBasedCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmAggrReportHCStatSumX.setStatus('current')
tpmAggrReportStatMaximum = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1, 12), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmAggrReportStatMaximum.setStatus('current')
tpmAggrReportStatMinimum = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1, 13), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmAggrReportStatMinimum.setStatus('current')
tpmAggrReportStatSumSq = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1, 14), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmAggrReportStatSumSq.setStatus('current')
tpmAggrReportOverflowStatSumSq = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1, 15), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmAggrReportOverflowStatSumSq.setStatus('current')
tpmAggrReportHCStatSumSq = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1, 16), ZeroBasedCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmAggrReportHCStatSumSq.setStatus('current')
tpmAggrReportStatSumIX = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1, 17), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmAggrReportStatSumIX.setStatus('current')
tpmAggrReportOverflowStatSumIX = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1, 18), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmAggrReportOverflowStatSumIX.setStatus('current')
tpmAggrReportHCStatSumIX = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1, 19), ZeroBasedCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmAggrReportHCStatSumIX.setStatus('current')
tpmAggrReportStatSumIXSq = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1, 20), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmAggrReportStatSumIXSq.setStatus('current')
tpmAggrReportOverflowStatSumIXSq = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1, 21), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmAggrReportOverflowStatSumIXSq.setStatus('current')
tpmAggrReportHCStatSumIXSq = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 2, 1, 22), ZeroBasedCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmAggrReportHCStatSumIXSq.setStatus('current')
tpmCurReportTable = MibTable((1, 3, 6, 1, 2, 1, 16, 30, 2, 3), )
if mibBuilder.loadTexts: tpmCurReportTable.setStatus('current')
tpmCurReportEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 30, 2, 3, 1), ).setIndexNames((0, "TPM-MIB", "tpmAggrReportCntrlIndex"), (0, "TPM-MIB", "tpmCurReportAppLocalIndex"), (0, "TPM-MIB", "tpmCurReportTransMetricIndex"), (0, "RMON2-MIB", "protocolDirLocalIndex"), (0, "TPM-MIB", "tpmCurReportServerAddress"), (0, "TPM-MIB", "tpmCurReportApmNameClientID"), (0, "TPM-MIB", "tpmCurReportApmTransactionID"))
if mibBuilder.loadTexts: tpmCurReportEntry.setStatus('current')
tpmCurReportAppLocalIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 3, 1, 1), AppLocalIndex())
if mibBuilder.loadTexts: tpmCurReportAppLocalIndex.setStatus('current')
tpmCurReportTransMetricIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 3, 1, 2), TpmTransactionMetricIndex())
if mibBuilder.loadTexts: tpmCurReportTransMetricIndex.setStatus('current')
tpmCurReportServerAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 3, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 108)))
if mibBuilder.loadTexts: tpmCurReportServerAddress.setStatus('current')
tpmCurReportApmNameClientID = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 3, 1, 4), RmonClientID())
if mibBuilder.loadTexts: tpmCurReportApmNameClientID.setStatus('current')
tpmCurReportApmTransactionID = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 3, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)))
if mibBuilder.loadTexts: tpmCurReportApmTransactionID.setStatus('current')
tpmCurReportMetricValue = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 3, 1, 6), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmCurReportMetricValue.setStatus('current')
tpmCurReportCompletion = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("current", 1), ("completed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmCurReportCompletion.setStatus('current')
tpmCurReportSize = MibScalar((1, 3, 6, 1, 2, 1, 16, 30, 2, 4), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpmCurReportSize.setStatus('current')
tpmExcpReportTable = MibTable((1, 3, 6, 1, 2, 1, 16, 30, 2, 5), )
if mibBuilder.loadTexts: tpmExcpReportTable.setStatus('current')
tpmExcpReportEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 30, 2, 5, 1), ).setIndexNames((0, "APM-MIB", "apmAppDirAppLocalIndex"), (0, "APM-MIB", "apmAppDirResponsivenessType"), (0, "APM-MIB", "apmExceptionIndex"), (0, "TPM-MIB", "tpmExcpReportTransMetricIndex"))
if mibBuilder.loadTexts: tpmExcpReportEntry.setStatus('current')
tpmExcpReportTransMetricIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 5, 1, 1), TpmTransactionMetricIndex())
if mibBuilder.loadTexts: tpmExcpReportTransMetricIndex.setStatus('current')
tpmExcpReportStatN = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 5, 1, 2), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmExcpReportStatN.setStatus('current')
tpmExcpReportOverflowStatN = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 5, 1, 3), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmExcpReportOverflowStatN.setStatus('current')
tpmExcpReportHCStatN = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 5, 1, 4), ZeroBasedCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmExcpReportHCStatN.setStatus('current')
tpmExcpReportStatSumX = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 5, 1, 5), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmExcpReportStatSumX.setStatus('current')
tpmExcpReportOverflowStatSumX = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 5, 1, 6), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmExcpReportOverflowStatSumX.setStatus('current')
tpmExcpReportHCStatSumX = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 5, 1, 7), ZeroBasedCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmExcpReportHCStatSumX.setStatus('current')
tpmExcpReportStatMaximum = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 5, 1, 8), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmExcpReportStatMaximum.setStatus('current')
tpmExcpReportStatMinimum = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 5, 1, 9), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmExcpReportStatMinimum.setStatus('current')
tpmExcpReportStatSumSq = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 5, 1, 10), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmExcpReportStatSumSq.setStatus('current')
tpmExcpReportOverflowStatSumSq = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 5, 1, 11), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmExcpReportOverflowStatSumSq.setStatus('current')
tpmExcpReportHCStatSumSq = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 5, 1, 12), ZeroBasedCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmExcpReportHCStatSumSq.setStatus('current')
tpmExcpReportStatSumIX = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 5, 1, 13), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmExcpReportStatSumIX.setStatus('current')
tpmExcpReportOverflowStatSumIX = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 5, 1, 14), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmExcpReportOverflowStatSumIX.setStatus('current')
tpmExcpReportHCStatSumIX = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 5, 1, 15), ZeroBasedCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmExcpReportHCStatSumIX.setStatus('current')
tpmExcpReportStatSumIXSq = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 5, 1, 16), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmExcpReportStatSumIXSq.setStatus('current')
tpmExcpReportOverflowStatSumIXSq = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 5, 1, 17), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmExcpReportOverflowStatSumIXSq.setStatus('current')
tpmExcpReportHCStatSumIXSq = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 30, 2, 5, 1, 18), ZeroBasedCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpmExcpReportHCStatSumIXSq.setStatus('current')
tpmMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 30, 3, 1))
tpmGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 30, 3, 2))
tpmMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 16, 30, 3, 1, 1)).setObjects(("TPM-MIB", "tpmCapabilitiesGroup"), ("TPM-MIB", "tpmAggregateReportsGroup"), ("TPM-MIB", "tpmCurrentReportsGroup"), ("TPM-MIB", "tpmExceptionReportsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tpmMIBCompliance = tpmMIBCompliance.setStatus('current')
tpmCurrentReportsCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 16, 30, 3, 1, 2)).setObjects(("TPM-MIB", "tpmCapabilitiesGroup"), ("TPM-MIB", "tpmAggregateReportsGroup"), ("TPM-MIB", "tpmCurrentReportsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tpmCurrentReportsCompliance = tpmCurrentReportsCompliance.setStatus('current')
tpmExceptionReportsCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 16, 30, 3, 1, 3)).setObjects(("TPM-MIB", "tpmCapabilitiesGroup"), ("TPM-MIB", "tpmAggregateReportsGroup"), ("TPM-MIB", "tpmExceptionReportsGroup"), ("APM-MIB", "apmReportGroup"), ("APM-MIB", "apmExceptionGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tpmExceptionReportsCompliance = tpmExceptionReportsCompliance.setStatus('current')
tpmCapabilitiesGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 16, 30, 3, 2, 1)).setObjects(("TPM-MIB", "tpmClockResolution"), ("TPM-MIB", "tpmClockMaxSkew"), ("TPM-MIB", "tpmClockSource"), ("TPM-MIB", "tpmTransMetricDirLastChange"), ("TPM-MIB", "tpmTransMetricProtocolIndex"), ("TPM-MIB", "tpmTransMetricMetricIndex"), ("TPM-MIB", "tpmTransMetricDirConfig"), ("TPM-MIB", "tpmMetricDefType"), ("TPM-MIB", "tpmMetricDefDirType"), ("TPM-MIB", "tpmMetricDefName"), ("TPM-MIB", "tpmMetricDefReference"), ("TPM-MIB", "tpmMetricDefGlobalID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tpmCapabilitiesGroup = tpmCapabilitiesGroup.setStatus('current')
tpmAggregateReportsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 16, 30, 3, 2, 2)).setObjects(("TPM-MIB", "tpmAggrReportCntrlApmCntrlIndex"), ("TPM-MIB", "tpmAggrReportCntrlDataSource"), ("TPM-MIB", "tpmAggrReportCntrlAggrType"), ("TPM-MIB", "tpmAggrReportCntrlInterval"), ("TPM-MIB", "tpmAggrReportCntrlReqSize"), ("TPM-MIB", "tpmAggrReportCntrlGrantedSize"), ("TPM-MIB", "tpmAggrReportCntrlReqReports"), ("TPM-MIB", "tpmAggrReportCntrlGrantedReports"), ("TPM-MIB", "tpmAggrReportCntrlStartTime"), ("TPM-MIB", "tpmAggrReportCntrlReportNumber"), ("TPM-MIB", "tpmAggrReportCntrlInsertsDenied"), ("TPM-MIB", "tpmAggrReportCntrlDroppedFrames"), ("TPM-MIB", "tpmAggrReportCntrlOwner"), ("TPM-MIB", "tpmAggrReportCntrlStorageType"), ("TPM-MIB", "tpmAggrReportCntrlStatus"), ("TPM-MIB", "tpmAggrReportStatN"), ("TPM-MIB", "tpmAggrReportOverflowStatN"), ("TPM-MIB", "tpmAggrReportHCStatN"), ("TPM-MIB", "tpmAggrReportStatSumX"), ("TPM-MIB", "tpmAggrReportOverflowStatSumX"), ("TPM-MIB", "tpmAggrReportHCStatSumX"), ("TPM-MIB", "tpmAggrReportStatMaximum"), ("TPM-MIB", "tpmAggrReportStatMinimum"), ("TPM-MIB", "tpmAggrReportStatSumSq"), ("TPM-MIB", "tpmAggrReportOverflowStatSumSq"), ("TPM-MIB", "tpmAggrReportHCStatSumSq"), ("TPM-MIB", "tpmAggrReportStatSumIX"), ("TPM-MIB", "tpmAggrReportOverflowStatSumIX"), ("TPM-MIB", "tpmAggrReportHCStatSumIX"), ("TPM-MIB", "tpmAggrReportStatSumIXSq"), ("TPM-MIB", "tpmAggrReportOverflowStatSumIXSq"), ("TPM-MIB", "tpmAggrReportHCStatSumIXSq"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tpmAggregateReportsGroup = tpmAggregateReportsGroup.setStatus('current')
tpmCurrentReportsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 16, 30, 3, 2, 3)).setObjects(("TPM-MIB", "tpmCurReportMetricValue"), ("TPM-MIB", "tpmCurReportCompletion"), ("TPM-MIB", "tpmCurReportSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tpmCurrentReportsGroup = tpmCurrentReportsGroup.setStatus('current')
tpmExceptionReportsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 16, 30, 3, 2, 4)).setObjects(("TPM-MIB", "tpmExcpReportStatN"), ("TPM-MIB", "tpmExcpReportOverflowStatN"), ("TPM-MIB", "tpmExcpReportHCStatN"), ("TPM-MIB", "tpmExcpReportStatSumX"), ("TPM-MIB", "tpmExcpReportOverflowStatSumX"), ("TPM-MIB", "tpmExcpReportHCStatSumX"), ("TPM-MIB", "tpmExcpReportStatMaximum"), ("TPM-MIB", "tpmExcpReportStatMinimum"), ("TPM-MIB", "tpmExcpReportStatSumSq"), ("TPM-MIB", "tpmExcpReportOverflowStatSumSq"), ("TPM-MIB", "tpmExcpReportHCStatSumSq"), ("TPM-MIB", "tpmExcpReportStatSumIX"), ("TPM-MIB", "tpmExcpReportOverflowStatSumIX"), ("TPM-MIB", "tpmExcpReportHCStatSumIX"), ("TPM-MIB", "tpmExcpReportStatSumIXSq"), ("TPM-MIB", "tpmExcpReportOverflowStatSumIXSq"), ("TPM-MIB", "tpmExcpReportHCStatSumIXSq"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tpmExceptionReportsGroup = tpmExceptionReportsGroup.setStatus('current')
mibBuilder.exportSymbols("TPM-MIB", tpmTransMetricDirLastChange=tpmTransMetricDirLastChange, tpmAggrReportStatSumX=tpmAggrReportStatSumX, tpmAggrReportCntrlEntry=tpmAggrReportCntrlEntry, tpmTransMetricIndex=tpmTransMetricIndex, tpmCurReportApmTransactionID=tpmCurReportApmTransactionID, tpmAggrReportStatSumSq=tpmAggrReportStatSumSq, tpmMetricDefTable=tpmMetricDefTable, tpmExcpReportStatSumIXSq=tpmExcpReportStatSumIXSq, tpmAggrReportCntrlStatus=tpmAggrReportCntrlStatus, tpmCurReportAppLocalIndex=tpmCurReportAppLocalIndex, tpmAggrReportCntrlTable=tpmAggrReportCntrlTable, tpmAggrReportCntrlApmCntrlIndex=tpmAggrReportCntrlApmCntrlIndex, tpmCurReportServerAddress=tpmCurReportServerAddress, tpmAggrReportCntrlReqSize=tpmAggrReportCntrlReqSize, tpmCurReportMetricValue=tpmCurReportMetricValue, tpmAggrReportCntrlReportNumber=tpmAggrReportCntrlReportNumber, tpmAggrReportHCStatSumIX=tpmAggrReportHCStatSumIX, tpmClockSource=tpmClockSource, tpmAggrReportStatMaximum=tpmAggrReportStatMaximum, tpmExcpReportOverflowStatSumX=tpmExcpReportOverflowStatSumX, tpmExcpReportHCStatN=tpmExcpReportHCStatN, tpmMetricDefName=tpmMetricDefName, tpmExceptionReportsGroup=tpmExceptionReportsGroup, tpmMetricDefDirType=tpmMetricDefDirType, tpmCurrentReportsCompliance=tpmCurrentReportsCompliance, tpmTransMetricProtocolIndex=tpmTransMetricProtocolIndex, tpmExcpReportHCStatSumX=tpmExcpReportHCStatSumX, tpmAggregateReportsGroup=tpmAggregateReportsGroup, tpmGroups=tpmGroups, tpmAggrReportCntrlAggrType=tpmAggrReportCntrlAggrType, tpmAggrReportTable=tpmAggrReportTable, tpmAggrReportOverflowStatSumIXSq=tpmAggrReportOverflowStatSumIXSq, TpmTransactionMetricIndex=TpmTransactionMetricIndex, tpmTransMetricDirConfig=tpmTransMetricDirConfig, TpmMetricDefID=TpmMetricDefID, tpmExcpReportStatSumSq=tpmExcpReportStatSumSq, tpmExcpReportTransMetricIndex=tpmExcpReportTransMetricIndex, tpmAggrReportHCStatN=tpmAggrReportHCStatN, tpmAggrReportStatN=tpmAggrReportStatN, tpmAggrReportCntrlInterval=tpmAggrReportCntrlInterval, tpmTransMetricMetricIndex=tpmTransMetricMetricIndex, tpmExcpReportStatMaximum=tpmExcpReportStatMaximum, tpmAggrReportCntrlReqReports=tpmAggrReportCntrlReqReports, tpmClockMaxSkew=tpmClockMaxSkew, tpmExcpReportHCStatSumIX=tpmExcpReportHCStatSumIX, tpmAggrReportHCStatSumX=tpmAggrReportHCStatSumX, tpmExcpReportOverflowStatSumIX=tpmExcpReportOverflowStatSumIX, tpmCurReportEntry=tpmCurReportEntry, tpmAggrReportOverflowStatSumIX=tpmAggrReportOverflowStatSumIX, tpmExceptionReportsCompliance=tpmExceptionReportsCompliance, tpmExcpReportStatN=tpmExcpReportStatN, tpmMIBCompliances=tpmMIBCompliances, PYSNMP_MODULE_ID=tpmMIB, tpmCapabilities=tpmCapabilities, tpmAggrReportCntrlInsertsDenied=tpmAggrReportCntrlInsertsDenied, tpmTransMetricDirTable=tpmTransMetricDirTable, tpmCurReportTransMetricIndex=tpmCurReportTransMetricIndex, tpmAggrReportCntrlDataSource=tpmAggrReportCntrlDataSource, tpmTransMetricAppLocalIndex=tpmTransMetricAppLocalIndex, tpmCurReportTable=tpmCurReportTable, tpmExcpReportOverflowStatN=tpmExcpReportOverflowStatN, tpmAggrReportCntrlOwner=tpmAggrReportCntrlOwner, tpmMetricDefGlobalID=tpmMetricDefGlobalID, tpmExcpReportStatSumX=tpmExcpReportStatSumX, tpmAggrReportStatMinimum=tpmAggrReportStatMinimum, tpmExcpReportHCStatSumIXSq=tpmExcpReportHCStatSumIXSq, tpmAggrReportCntrlDroppedFrames=tpmAggrReportCntrlDroppedFrames, tpmAggrReportIndex=tpmAggrReportIndex, tpmMIB=tpmMIB, tpmCurReportCompletion=tpmCurReportCompletion, tpmAggrReportOverflowStatSumSq=tpmAggrReportOverflowStatSumSq, tpmReports=tpmReports, tpmAggrReportEntry=tpmAggrReportEntry, tpmClockResolution=tpmClockResolution, tpmAggrReportOverflowStatN=tpmAggrReportOverflowStatN, tpmCapabilitiesGroup=tpmCapabilitiesGroup, tpmCurReportApmNameClientID=tpmCurReportApmNameClientID, tpmConformance=tpmConformance, tpmCurReportSize=tpmCurReportSize, tpmMetricDefReference=tpmMetricDefReference, tpmExcpReportOverflowStatSumIXSq=tpmExcpReportOverflowStatSumIXSq, tpmAggrReportHCStatSumIXSq=tpmAggrReportHCStatSumIXSq, tpmAggrReportCntrlIndex=tpmAggrReportCntrlIndex, tpmMetricDefEntry=tpmMetricDefEntry, tpmExcpReportStatMinimum=tpmExcpReportStatMinimum, tpmAggrReportTransMetricIndex=tpmAggrReportTransMetricIndex, tpmAggrReportStatSumIX=tpmAggrReportStatSumIX, tpmCurrentReportsGroup=tpmCurrentReportsGroup, tpmExcpReportEntry=tpmExcpReportEntry, tpmExcpReportOverflowStatSumSq=tpmExcpReportOverflowStatSumSq, tpmAggrReportServerAddress=tpmAggrReportServerAddress, tpmExcpReportTable=tpmExcpReportTable, tpmAggrReportCntrlGrantedReports=tpmAggrReportCntrlGrantedReports, tpmMetricDefType=tpmMetricDefType, tpmAggrReportHCStatSumSq=tpmAggrReportHCStatSumSq, tpmMIBCompliance=tpmMIBCompliance, tpmTransMetricDirEntry=tpmTransMetricDirEntry, tpmAggrReportOverflowStatSumX=tpmAggrReportOverflowStatSumX, tpmExcpReportHCStatSumSq=tpmExcpReportHCStatSumSq, tpmAggrReportApmNameClientID=tpmAggrReportApmNameClientID, tpmAggrReportAppLocalIndex=tpmAggrReportAppLocalIndex, tpmAggrReportCntrlGrantedSize=tpmAggrReportCntrlGrantedSize, tpmExcpReportStatSumIX=tpmExcpReportStatSumIX, tpmAggrReportStatSumIXSq=tpmAggrReportStatSumIXSq, tpmAggrReportCntrlStartTime=tpmAggrReportCntrlStartTime, tpmMetricDefinitionID=tpmMetricDefinitionID, tpmAggrReportCntrlStorageType=tpmAggrReportCntrlStorageType)
