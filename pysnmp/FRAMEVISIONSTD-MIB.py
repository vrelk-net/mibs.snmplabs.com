#
# PySNMP MIB module FRAMEVISIONSTD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FRAMEVISIONSTD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:02:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Counter32, IpAddress, enterprises, Bits, ModuleIdentity, NotificationType, Integer32, ObjectIdentity, iso, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "IpAddress", "enterprises", "Bits", "ModuleIdentity", "NotificationType", "Integer32", "ObjectIdentity", "iso", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class FribDLCI(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483646)

class Counter32(Counter32):
    pass

framevisionstd = MibIdentifier((1, 3, 6, 1, 4, 1, 181, 100, 1))
fribStd = MibIdentifier((1, 3, 6, 1, 4, 1, 181, 100, 1, 1))
fribCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 181, 100, 1, 2))
fribPortMon = MibIdentifier((1, 3, 6, 1, 4, 1, 181, 100, 1, 3))
fribVcMon = MibIdentifier((1, 3, 6, 1, 4, 1, 181, 100, 1, 4))
fribFrlm = MibIdentifier((1, 3, 6, 1, 4, 1, 181, 100, 1, 5))
fribMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 181, 100, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("version1", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribMibVersion.setStatus('mandatory')
fribMibLastChange = MibScalar((1, 3, 6, 1, 4, 1, 181, 100, 1, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribMibLastChange.setStatus('mandatory')
fribCfgTable = MibTable((1, 3, 6, 1, 4, 1, 181, 100, 1, 2, 1), )
if mibBuilder.loadTexts: fribCfgTable.setStatus('mandatory')
fribCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 181, 100, 1, 2, 1, 1), ).setIndexNames((0, "FRAMEVISIONSTD-MIB", "fribCfgIfIndex"))
if mibBuilder.loadTexts: fribCfgEntry.setStatus('mandatory')
fribCfgIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribCfgIfIndex.setStatus('mandatory')
fribCfgLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 2, 1, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribCfgLastChange.setStatus('mandatory')
fribCfgFrameType = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("frameTypeNlpid", 1), ("frameTypeEther", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fribCfgFrameType.setStatus('mandatory')
fribCfgAddrOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("twoOctets", 1), ("fourOctets", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fribCfgAddrOctets.setStatus('mandatory')
fribCfgFcsBitLength = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("frib16BitFcs", 1), ("frib32BitFcs", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fribCfgFcsBitLength.setStatus('mandatory')
fribCfgTimeInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 2, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fribCfgTimeInterval.setStatus('mandatory')
fribCfgMaxVCs = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 2, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribCfgMaxVCs.setStatus('mandatory')
fribCfgNumberVCs = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 2, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribCfgNumberVCs.setStatus('mandatory')
fribCfgVcAddDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 2, 1, 1, 9), FribDLCI()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fribCfgVcAddDLCI.setStatus('mandatory')
fribCfgVcDelDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 2, 1, 1, 10), FribDLCI()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fribCfgVcDelDLCI.setStatus('mandatory')
fribCfgVcListTable = MibTable((1, 3, 6, 1, 4, 1, 181, 100, 1, 2, 2), )
if mibBuilder.loadTexts: fribCfgVcListTable.setStatus('mandatory')
fribCfgVcListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 181, 100, 1, 2, 2, 1), ).setIndexNames((0, "FRAMEVISIONSTD-MIB", "fribCfgVcListIfIndex"), (0, "FRAMEVISIONSTD-MIB", "fribCfgVcListDLCI"))
if mibBuilder.loadTexts: fribCfgVcListEntry.setStatus('mandatory')
fribCfgVcListIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribCfgVcListIfIndex.setStatus('mandatory')
fribCfgVcListDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 2, 2, 1, 2), FribDLCI()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribCfgVcListDLCI.setStatus('mandatory')
fribCfgVcListCIR = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 2, 2, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fribCfgVcListCIR.setStatus('mandatory')
fribCfgVcListEIR = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 2, 2, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fribCfgVcListEIR.setStatus('mandatory')
fribCfgVcListCreationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 2, 2, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribCfgVcListCreationTime.setStatus('mandatory')
fribPortMonDuration = MibScalar((1, 3, 6, 1, 4, 1, 181, 100, 1, 3, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribPortMonDuration.setStatus('mandatory')
fribPortMonClearData = MibScalar((1, 3, 6, 1, 4, 1, 181, 100, 1, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("clearDataIdle", 1), ("clearDataStart", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fribPortMonClearData.setStatus('mandatory')
fribPortMonTable = MibTable((1, 3, 6, 1, 4, 1, 181, 100, 1, 3, 3), )
if mibBuilder.loadTexts: fribPortMonTable.setStatus('mandatory')
fribPortMonEntry = MibTableRow((1, 3, 6, 1, 4, 1, 181, 100, 1, 3, 3, 1), ).setIndexNames((0, "FRAMEVISIONSTD-MIB", "fribPortMonIfIndex"))
if mibBuilder.loadTexts: fribPortMonEntry.setStatus('mandatory')
fribPortMonIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 3, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribPortMonIfIndex.setStatus('mandatory')
fribPortMonAvailTime = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 3, 3, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribPortMonAvailTime.setStatus('mandatory')
fribPortMonTxFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 3, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribPortMonTxFrames.setStatus('mandatory')
fribPortMonRxFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 3, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribPortMonRxFrames.setStatus('mandatory')
fribPortMonTxOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 3, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribPortMonTxOctets.setStatus('mandatory')
fribPortMonRxOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 3, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribPortMonRxOctets.setStatus('mandatory')
fribPortMonIpMgmtTxFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 3, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribPortMonIpMgmtTxFrames.setStatus('mandatory')
fribPortMonIpMgmtRxFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 3, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribPortMonIpMgmtRxFrames.setStatus('mandatory')
fribPortMonIpMgmtTxOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 3, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribPortMonIpMgmtTxOctets.setStatus('mandatory')
fribPortMonIpMgmtRxOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 3, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribPortMonIpMgmtRxOctets.setStatus('mandatory')
fribPortMonRxInvalidHdrs = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 3, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribPortMonRxInvalidHdrs.setStatus('mandatory')
fribPortMonRxHdlcErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 3, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribPortMonRxHdlcErrors.setStatus('mandatory')
fribVcStatDuration = MibScalar((1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribVcStatDuration.setStatus('mandatory')
fribVcStatClearData = MibScalar((1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("clearDataIdle", 1), ("clearDataStart", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fribVcStatClearData.setStatus('mandatory')
fribVcStatTable = MibTable((1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 3), )
if mibBuilder.loadTexts: fribVcStatTable.setStatus('mandatory')
fribVcStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 3, 1), ).setIndexNames((0, "FRAMEVISIONSTD-MIB", "fribVcStatIfIndex"), (0, "FRAMEVISIONSTD-MIB", "fribVcStatDLCI"))
if mibBuilder.loadTexts: fribVcStatEntry.setStatus('mandatory')
fribVcStatIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribVcStatIfIndex.setStatus('mandatory')
fribVcStatDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribVcStatDLCI.setStatus('mandatory')
fribVcStatTxFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribVcStatTxFrames.setStatus('mandatory')
fribVcStatRxFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribVcStatRxFrames.setStatus('mandatory')
fribVcStatTxOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribVcStatTxOctets.setStatus('mandatory')
fribVcStatRxOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribVcStatRxOctets.setStatus('mandatory')
fribVcStatTxDEs = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribVcStatTxDEs.setStatus('mandatory')
fribVcStatRxDEs = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribVcStatRxDEs.setStatus('mandatory')
fribVcStatTxFECNs = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribVcStatTxFECNs.setStatus('mandatory')
fribVcStatRxFECNs = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribVcStatRxFECNs.setStatus('mandatory')
fribVcStatTxBECNs = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribVcStatTxBECNs.setStatus('mandatory')
fribVcStatRxBECNs = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribVcStatRxBECNs.setStatus('mandatory')
fribVcUtilDuration = MibScalar((1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribVcUtilDuration.setStatus('mandatory')
fribVcUtilClearData = MibScalar((1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("clearDataIdle", 1), ("clearDataStart", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fribVcUtilClearData.setStatus('mandatory')
fribVcUtilTable = MibTable((1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 6), )
if mibBuilder.loadTexts: fribVcUtilTable.setStatus('mandatory')
fribVcUtilEntry = MibTableRow((1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 6, 1), ).setIndexNames((0, "FRAMEVISIONSTD-MIB", "fribVcUtilIfIndex"), (0, "FRAMEVISIONSTD-MIB", "fribVcUtilDLCI"))
if mibBuilder.loadTexts: fribVcUtilEntry.setStatus('mandatory')
fribVcUtilIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribVcUtilIfIndex.setStatus('mandatory')
fribVcUtilDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 6, 1, 2), FribDLCI()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribVcUtilDLCI.setStatus('mandatory')
fribVcUtilCirExceededTx = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 6, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribVcUtilCirExceededTx.setStatus('mandatory')
fribVcUtilCirOctetsExceededTx = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 6, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribVcUtilCirOctetsExceededTx.setStatus('mandatory')
fribVcUtilEirExceededTx = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 6, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribVcUtilEirExceededTx.setStatus('mandatory')
fribVcUtilEirOctetsExceededTx = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 4, 6, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribVcUtilEirOctetsExceededTx.setStatus('mandatory')
fribFrlmCfgTable = MibTable((1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 1), )
if mibBuilder.loadTexts: fribFrlmCfgTable.setStatus('mandatory')
fribFrlmCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 1, 1), ).setIndexNames((0, "FRAMEVISIONSTD-MIB", "fribFrlmCfgIfIndex"))
if mibBuilder.loadTexts: fribFrlmCfgEntry.setStatus('mandatory')
fribFrlmCfgIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribFrlmCfgIfIndex.setStatus('mandatory')
fribFrlmCfgLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 1, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribFrlmCfgLastChange.setStatus('mandatory')
fribFrlmCfgProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("lmi", 2), ("ansiT1617D", 3), ("ccittQ933A", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fribFrlmCfgProtocol.setStatus('mandatory')
fribFrlmCfgSpoofing = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("spoofingEnabled", 1), ("spoofingDisabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fribFrlmCfgSpoofing.setStatus('mandatory')
fribFrlmCfgT391 = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fribFrlmCfgT391.setStatus('mandatory')
fribFrlmCfgN392 = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fribFrlmCfgN392.setStatus('mandatory')
fribFrlmCfgN393 = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fribFrlmCfgN393.setStatus('mandatory')
fribFrlmCfgSpoofingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("spoofingInactive", 1), ("spoofingActive", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribFrlmCfgSpoofingStatus.setStatus('mandatory')
fribFrlmPortDuration = MibScalar((1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribFrlmPortDuration.setStatus('mandatory')
fribFrlmPortClearData = MibScalar((1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("clearDataIdle", 1), ("clearDataStart", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fribFrlmPortClearData.setStatus('mandatory')
fribFrlmPortTable = MibTable((1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 4), )
if mibBuilder.loadTexts: fribFrlmPortTable.setStatus('mandatory')
fribFrlmPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 4, 1), ).setIndexNames((0, "FRAMEVISIONSTD-MIB", "fribFrlmPortIfIndex"))
if mibBuilder.loadTexts: fribFrlmPortEntry.setStatus('mandatory')
fribFrlmPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribFrlmPortIfIndex.setStatus('mandatory')
fribFrlmPortSendSeqNumTx = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 4, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribFrlmPortSendSeqNumTx.setStatus('mandatory')
fribFrlmPortSendSeqNumRx = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribFrlmPortSendSeqNumRx.setStatus('mandatory')
fribFrlmPortReceiveSeqNumTx = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribFrlmPortReceiveSeqNumTx.setStatus('mandatory')
fribFrlmPortReceiveSeqNumRx = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribFrlmPortReceiveSeqNumRx.setStatus('mandatory')
fribFrlmPortStatusRsp = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribFrlmPortStatusRsp.setStatus('mandatory')
fribFrlmPortStatusRspMissed = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 4, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribFrlmPortStatusRspMissed.setStatus('mandatory')
fribFrlmPortStatusRspSpoofed = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 4, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribFrlmPortStatusRspSpoofed.setStatus('mandatory')
fribFrlmPortStatusFullRsp = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 4, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribFrlmPortStatusFullRsp.setStatus('mandatory')
fribFrlmPortStatusFullRspMissed = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 4, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribFrlmPortStatusFullRspMissed.setStatus('mandatory')
fribFrlmPortStatusFullRspSpoofed = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 4, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribFrlmPortStatusFullRspSpoofed.setStatus('mandatory')
fribFrlmStatusDuration = MibScalar((1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribFrlmStatusDuration.setStatus('mandatory')
fribFrlmStatusClearData = MibScalar((1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("clearDataIdle", 1), ("clearDataStart", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fribFrlmStatusClearData.setStatus('mandatory')
fribFrlmStatusTable = MibTable((1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 7), )
if mibBuilder.loadTexts: fribFrlmStatusTable.setStatus('mandatory')
fribFrlmStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 7, 1), ).setIndexNames((0, "FRAMEVISIONSTD-MIB", "fribVcUtilIfIndex"), (0, "FRAMEVISIONSTD-MIB", "fribVcUtilDLCI"))
if mibBuilder.loadTexts: fribFrlmStatusEntry.setStatus('mandatory')
fribFrlmStatusIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 7, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribFrlmStatusIfIndex.setStatus('mandatory')
fribFrlmStatusDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 7, 1, 2), FribDLCI()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribFrlmStatusDLCI.setStatus('mandatory')
fribFrlmStatusStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("frlmStatusNew", 1), ("frlmStatusDelete", 2), ("frlmStatusActive", 3), ("frlmStatusInactive", 4), ("frlmStatusSpoofed", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribFrlmStatusStatus.setStatus('mandatory')
fribFrlmStatusDownEvents = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 7, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribFrlmStatusDownEvents.setStatus('mandatory')
fribFrlmStatusActiveSecs = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 7, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribFrlmStatusActiveSecs.setStatus('mandatory')
fribFrlmStatusTotalSecs = MibTableColumn((1, 3, 6, 1, 4, 1, 181, 100, 1, 5, 7, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fribFrlmStatusTotalSecs.setStatus('mandatory')
mibBuilder.exportSymbols("FRAMEVISIONSTD-MIB", fribPortMonEntry=fribPortMonEntry, fribFrlmPortIfIndex=fribFrlmPortIfIndex, fribPortMonIpMgmtRxOctets=fribPortMonIpMgmtRxOctets, fribFrlmStatusActiveSecs=fribFrlmStatusActiveSecs, fribVcUtilEirExceededTx=fribVcUtilEirExceededTx, fribVcUtilTable=fribVcUtilTable, fribVcStatRxBECNs=fribVcStatRxBECNs, FribDLCI=FribDLCI, fribMibVersion=fribMibVersion, fribFrlmCfgSpoofing=fribFrlmCfgSpoofing, fribPortMonIfIndex=fribPortMonIfIndex, fribVcUtilEntry=fribVcUtilEntry, fribFrlmStatusEntry=fribFrlmStatusEntry, fribPortMonTable=fribPortMonTable, fribCfgEntry=fribCfgEntry, fribVcUtilCirExceededTx=fribVcUtilCirExceededTx, fribVcUtilDLCI=fribVcUtilDLCI, fribFrlmPortStatusFullRspSpoofed=fribFrlmPortStatusFullRspSpoofed, fribFrlmStatusIfIndex=fribFrlmStatusIfIndex, fribCfgNumberVCs=fribCfgNumberVCs, fribFrlmCfgN392=fribFrlmCfgN392, fribFrlmCfgEntry=fribFrlmCfgEntry, fribVcStatDLCI=fribVcStatDLCI, Counter32=Counter32, fribFrlmCfgSpoofingStatus=fribFrlmCfgSpoofingStatus, fribCfgLastChange=fribCfgLastChange, fribVcUtilClearData=fribVcUtilClearData, fribPortMonRxFrames=fribPortMonRxFrames, fribStd=fribStd, fribCfgFcsBitLength=fribCfgFcsBitLength, fribFrlmPortReceiveSeqNumTx=fribFrlmPortReceiveSeqNumTx, fribFrlmStatusStatus=fribFrlmStatusStatus, fribVcUtilDuration=fribVcUtilDuration, fribPortMonClearData=fribPortMonClearData, fribFrlmPortStatusRspMissed=fribFrlmPortStatusRspMissed, fribVcStatIfIndex=fribVcStatIfIndex, fribFrlmPortStatusFullRspMissed=fribFrlmPortStatusFullRspMissed, fribVcStatRxFECNs=fribVcStatRxFECNs, fribCfgVcAddDLCI=fribCfgVcAddDLCI, fribFrlmCfgN393=fribFrlmCfgN393, fribCfgVcListEIR=fribCfgVcListEIR, fribVcStatTxBECNs=fribVcStatTxBECNs, fribFrlmPortClearData=fribFrlmPortClearData, fribFrlmPortDuration=fribFrlmPortDuration, fribCfgVcDelDLCI=fribCfgVcDelDLCI, fribFrlmCfgLastChange=fribFrlmCfgLastChange, fribVcStatTxFrames=fribVcStatTxFrames, fribPortMonTxFrames=fribPortMonTxFrames, fribPortMonAvailTime=fribPortMonAvailTime, fribCfgFrameType=fribCfgFrameType, fribFrlmPortStatusRsp=fribFrlmPortStatusRsp, fribCfgVcListCreationTime=fribCfgVcListCreationTime, fribCfgTimeInterval=fribCfgTimeInterval, fribCfgMaxVCs=fribCfgMaxVCs, fribPortMonRxOctets=fribPortMonRxOctets, fribFrlmStatusClearData=fribFrlmStatusClearData, fribVcStatDuration=fribVcStatDuration, fribCfgIfIndex=fribCfgIfIndex, fribFrlmCfgTable=fribFrlmCfgTable, fribFrlmCfgProtocol=fribFrlmCfgProtocol, fribCfgVcListCIR=fribCfgVcListCIR, fribFrlmPortStatusRspSpoofed=fribFrlmPortStatusRspSpoofed, fribVcStatTxDEs=fribVcStatTxDEs, fribPortMonDuration=fribPortMonDuration, fribFrlmPortTable=fribFrlmPortTable, fribCfg=fribCfg, fribFrlmCfgT391=fribFrlmCfgT391, fribPortMonRxHdlcErrors=fribPortMonRxHdlcErrors, fribFrlmPortSendSeqNumRx=fribFrlmPortSendSeqNumRx, fribFrlmStatusDLCI=fribFrlmStatusDLCI, fribCfgTable=fribCfgTable, fribFrlmStatusDownEvents=fribFrlmStatusDownEvents, fribVcMon=fribVcMon, fribCfgVcListEntry=fribCfgVcListEntry, fribCfgVcListTable=fribCfgVcListTable, framevisionstd=framevisionstd, fribPortMonRxInvalidHdrs=fribPortMonRxInvalidHdrs, fribFrlmPortEntry=fribFrlmPortEntry, fribVcStatTxOctets=fribVcStatTxOctets, fribMibLastChange=fribMibLastChange, fribPortMonIpMgmtTxOctets=fribPortMonIpMgmtTxOctets, fribVcUtilIfIndex=fribVcUtilIfIndex, fribVcStatRxDEs=fribVcStatRxDEs, fribVcStatRxFrames=fribVcStatRxFrames, fribFrlmPortReceiveSeqNumRx=fribFrlmPortReceiveSeqNumRx, fribVcUtilEirOctetsExceededTx=fribVcUtilEirOctetsExceededTx, fribFrlmPortStatusFullRsp=fribFrlmPortStatusFullRsp, fribCfgAddrOctets=fribCfgAddrOctets, fribFrlmStatusTotalSecs=fribFrlmStatusTotalSecs, fribFrlmStatusDuration=fribFrlmStatusDuration, fribVcUtilCirOctetsExceededTx=fribVcUtilCirOctetsExceededTx, fribPortMonIpMgmtTxFrames=fribPortMonIpMgmtTxFrames, fribPortMonIpMgmtRxFrames=fribPortMonIpMgmtRxFrames, fribFrlmCfgIfIndex=fribFrlmCfgIfIndex, fribVcStatRxOctets=fribVcStatRxOctets, fribPortMon=fribPortMon, fribFrlm=fribFrlm, fribVcStatEntry=fribVcStatEntry, fribFrlmPortSendSeqNumTx=fribFrlmPortSendSeqNumTx, fribFrlmStatusTable=fribFrlmStatusTable, fribVcStatClearData=fribVcStatClearData, fribCfgVcListIfIndex=fribCfgVcListIfIndex, fribCfgVcListDLCI=fribCfgVcListDLCI, fribVcStatTxFECNs=fribVcStatTxFECNs, fribPortMonTxOctets=fribPortMonTxOctets, fribVcStatTable=fribVcStatTable)
