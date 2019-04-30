#
# PySNMP MIB module MULTIBRIDGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MULTIBRIDGE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:06:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
nncExtensions, = mibBuilder.importSymbols("NNCGNI0001-SMI", "nncExtensions")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Bits, Counter32, TimeTicks, ModuleIdentity, Gauge32, Unsigned32, IpAddress, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, Counter64, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Bits", "Counter32", "TimeTicks", "ModuleIdentity", "Gauge32", "Unsigned32", "IpAddress", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "Counter64", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nncExtMultiBridge = ModuleIdentity((1, 3, 6, 1, 4, 1, 123, 3, 43))
if mibBuilder.loadTexts: nncExtMultiBridge.setLastUpdated('9703251140Z')
if mibBuilder.loadTexts: nncExtMultiBridge.setOrganization('Newbridge Networks Corporation')
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class BridgeId(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class Timeout(Integer32):
    pass

mBrdgBase = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 43, 1))
mBrdgStp = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 43, 2))
mBrdgTp = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 43, 3))
mBrdgStatic = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 43, 4))
mBrdgConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 123, 3, 43, 5))
mBrdgBaseTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 43, 1, 1), )
if mibBuilder.loadTexts: mBrdgBaseTable.setStatus('current')
mBrdgBaseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 43, 1, 1, 1), ).setIndexNames((0, "MULTIBRIDGE-MIB", "mBrdgBaseBridgeAddress"))
if mibBuilder.loadTexts: mBrdgBaseEntry.setStatus('current')
mBrdgBaseBridgeAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 1, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBrdgBaseBridgeAddress.setStatus('current')
mBrdgBaseNumPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBrdgBaseNumPorts.setStatus('current')
mBrdgBaseType = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("transparentOnly", 2), ("sourcerouteOnly", 3), ("srt", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBrdgBaseType.setStatus('current')
mBrdgBasePortTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 43, 1, 2), )
if mibBuilder.loadTexts: mBrdgBasePortTable.setStatus('current')
mBrdgBasePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 43, 1, 2, 1), ).setIndexNames((0, "MULTIBRIDGE-MIB", "mBrdgBasePortBridgeIndex"), (0, "MULTIBRIDGE-MIB", "mBrdgBasePort"))
if mibBuilder.loadTexts: mBrdgBasePortEntry.setStatus('current')
mBrdgBasePort = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBrdgBasePort.setStatus('current')
mBrdgBasePortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBrdgBasePortIfIndex.setStatus('current')
mBrdgBasePortCircuit = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 1, 2, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBrdgBasePortCircuit.setStatus('current')
mBrdgBasePortDelayExceededDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 1, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBrdgBasePortDelayExceededDiscards.setStatus('current')
mBrdgBasePortMtuExceededDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBrdgBasePortMtuExceededDiscards.setStatus('current')
mBrdgBasePortBridgeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBrdgBasePortBridgeIndex.setStatus('current')
mBrdgStpTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 1), )
if mibBuilder.loadTexts: mBrdgStpTable.setStatus('current')
mBrdgStpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 1, 1), ).setIndexNames((0, "MULTIBRIDGE-MIB", "mBrdgStpBridgeIndex"))
if mibBuilder.loadTexts: mBrdgStpEntry.setStatus('current')
mBrdgStpProtocolSpecification = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("decLb100", 2), ("ieee8021d", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBrdgStpProtocolSpecification.setStatus('current')
mBrdgStpPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mBrdgStpPriority.setStatus('current')
mBrdgStpTimeSinceTopologyChange = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBrdgStpTimeSinceTopologyChange.setStatus('current')
mBrdgStpTopChanges = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBrdgStpTopChanges.setStatus('current')
mBrdgStpDesignatedRoot = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 1, 1, 5), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBrdgStpDesignatedRoot.setStatus('current')
mBrdgStpRootCost = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBrdgStpRootCost.setStatus('current')
mBrdgStpRootPort = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBrdgStpRootPort.setStatus('current')
mBrdgStpMaxAge = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 1, 1, 8), Timeout()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBrdgStpMaxAge.setStatus('current')
mBrdgStpHelloTime = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 1, 1, 9), Timeout()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBrdgStpHelloTime.setStatus('current')
mBrdgStpHoldTime = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBrdgStpHoldTime.setStatus('current')
mBrdgStpForwardDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 1, 1, 11), Timeout()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBrdgStpForwardDelay.setStatus('current')
mBrdgStpBridgeMaxAge = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 1, 1, 12), Timeout().subtype(subtypeSpec=ValueRangeConstraint(600, 4000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mBrdgStpBridgeMaxAge.setStatus('current')
mBrdgStpBridgeHelloTime = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 1, 1, 13), Timeout().subtype(subtypeSpec=ValueRangeConstraint(100, 1000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mBrdgStpBridgeHelloTime.setStatus('current')
mBrdgStpBridgeForwardDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 1, 1, 14), Timeout().subtype(subtypeSpec=ValueRangeConstraint(400, 3000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mBrdgStpBridgeForwardDelay.setStatus('current')
mBrdgStpEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("unavailable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mBrdgStpEnable.setStatus('current')
mBrdgStpBridgeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBrdgStpBridgeIndex.setStatus('current')
mBrdgStpPortTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 2), )
if mibBuilder.loadTexts: mBrdgStpPortTable.setStatus('current')
mBrdgStpPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 2, 1), ).setIndexNames((0, "MULTIBRIDGE-MIB", "mBrdgStpPortBridgeIndex"), (0, "MULTIBRIDGE-MIB", "mBrdgStpPort"))
if mibBuilder.loadTexts: mBrdgStpPortEntry.setStatus('current')
mBrdgStpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBrdgStpPort.setStatus('current')
mBrdgStpPortPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mBrdgStpPortPriority.setStatus('current')
mBrdgStpPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("disabled", 1), ("blocking", 2), ("listening", 3), ("learning", 4), ("forwarding", 5), ("broken", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBrdgStpPortState.setStatus('current')
mBrdgStpPortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mBrdgStpPortEnable.setStatus('current')
mBrdgStpPortPathCost = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mBrdgStpPortPathCost.setStatus('current')
mBrdgStpPortDesignatedRoot = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 2, 1, 6), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBrdgStpPortDesignatedRoot.setStatus('current')
mBrdgStpPortDesignatedCost = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBrdgStpPortDesignatedCost.setStatus('current')
mBrdgStpPortDesignatedBridge = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 2, 1, 8), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBrdgStpPortDesignatedBridge.setStatus('current')
mBrdgStpPortDesignatedPort = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 2, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBrdgStpPortDesignatedPort.setStatus('current')
mBrdgStpPortForwardTransitions = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBrdgStpPortForwardTransitions.setStatus('current')
mBrdgStpPortStatsTxBPDUCount = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 2, 1, 11), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mBrdgStpPortStatsTxBPDUCount.setStatus('current')
mBrdgStpPortStatsRxBPDUCount = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 2, 1, 12), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mBrdgStpPortStatsRxBPDUCount.setStatus('current')
mBrdgStpPortBridgeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 2, 2, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBrdgStpPortBridgeIndex.setStatus('current')
mBrdgTpTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 43, 3, 1), )
if mibBuilder.loadTexts: mBrdgTpTable.setStatus('current')
mBrdgTpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 43, 3, 1, 1), ).setIndexNames((0, "MULTIBRIDGE-MIB", "mBrdgTpBridgeIndex"))
if mibBuilder.loadTexts: mBrdgTpEntry.setStatus('current')
mBrdgTpLearnedEntryDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 3, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBrdgTpLearnedEntryDiscards.setStatus('current')
mBrdgTpAgingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 1000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mBrdgTpAgingTime.setStatus('current')
mBrdgTpLearningEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mBrdgTpLearningEnable.setStatus('current')
mBrdgTpFdbNumLearnedEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 3, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mBrdgTpFdbNumLearnedEntries.setStatus('current')
mBrdgTpFdbNumEntries = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 3, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mBrdgTpFdbNumEntries.setStatus('current')
mBrdgTpBridgeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBrdgTpBridgeIndex.setStatus('current')
mBrdgTpFdbTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 43, 3, 2), )
if mibBuilder.loadTexts: mBrdgTpFdbTable.setStatus('current')
mBrdgTpFdbEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 43, 3, 2, 1), ).setIndexNames((0, "MULTIBRIDGE-MIB", "mBrdgTpFdbBridgeIndex"), (0, "MULTIBRIDGE-MIB", "mBrdgTpFdbAddress"))
if mibBuilder.loadTexts: mBrdgTpFdbEntry.setStatus('current')
mBrdgTpFdbAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 3, 2, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBrdgTpFdbAddress.setStatus('current')
mBrdgTpFdbPort = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 3, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBrdgTpFdbPort.setStatus('current')
mBrdgTpFdbStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2), ("learned", 3), ("self", 4), ("mgmt", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBrdgTpFdbStatus.setStatus('current')
mBrdgTpFdbBridgeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBrdgTpFdbBridgeIndex.setStatus('current')
mBrdgTpPortTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 43, 3, 3), )
if mibBuilder.loadTexts: mBrdgTpPortTable.setStatus('current')
mBrdgTpPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 43, 3, 3, 1), ).setIndexNames((0, "MULTIBRIDGE-MIB", "mBrdgTpPortBridgeIndex"), (0, "MULTIBRIDGE-MIB", "mBrdgTpPort"))
if mibBuilder.loadTexts: mBrdgTpPortEntry.setStatus('current')
mBrdgTpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBrdgTpPort.setStatus('current')
mBrdgTpPortMaxInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 3, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBrdgTpPortMaxInfo.setStatus('current')
mBrdgTpPortInFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 3, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBrdgTpPortInFrames.setStatus('current')
mBrdgTpPortOutFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 3, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBrdgTpPortOutFrames.setStatus('current')
mBrdgTpPortInDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 3, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBrdgTpPortInDiscards.setStatus('current')
mBrdgTpPortBridgeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 3, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBrdgTpPortBridgeIndex.setStatus('current')
mBrdgStaticTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 43, 4, 1), )
if mibBuilder.loadTexts: mBrdgStaticTable.setStatus('current')
mBrdgStaticEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 43, 4, 1, 1), ).setIndexNames((0, "MULTIBRIDGE-MIB", "mBrdgStaticBridgeIndex"), (0, "MULTIBRIDGE-MIB", "mBrdgStaticAddress"), (0, "MULTIBRIDGE-MIB", "mBrdgStaticReceivePort"))
if mibBuilder.loadTexts: mBrdgStaticEntry.setStatus('current')
mBrdgStaticAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 4, 1, 1, 1), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mBrdgStaticAddress.setStatus('current')
mBrdgStaticReceivePort = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 4, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mBrdgStaticReceivePort.setStatus('current')
mBrdgStaticAllowedToGoTo = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 4, 1, 1, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mBrdgStaticAllowedToGoTo.setStatus('current')
mBrdgStaticStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2), ("permanent", 3), ("deleteOnReset", 4), ("deleteOnTimeout", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mBrdgStaticStatus.setStatus('current')
mBrdgStaticBridgeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 4, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBrdgStaticBridgeIndex.setStatus('current')
mBrdgConfigTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 43, 5, 1), )
if mibBuilder.loadTexts: mBrdgConfigTable.setStatus('current')
mBrdgConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 43, 5, 1, 1), ).setIndexNames((0, "MULTIBRIDGE-MIB", "mBrdgConfigBridgeIndex"))
if mibBuilder.loadTexts: mBrdgConfigEntry.setStatus('current')
mBrdgConfigBridgeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBrdgConfigBridgeIndex.setStatus('current')
mBrdgConfigBridgeName = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 5, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mBrdgConfigBridgeName.setStatus('current')
mBrdgConfigBridgePeakRate = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 43, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mBrdgConfigBridgePeakRate.setStatus('current')
mibBuilder.exportSymbols("MULTIBRIDGE-MIB", mBrdgStpTable=mBrdgStpTable, mBrdgStpHoldTime=mBrdgStpHoldTime, mBrdgTpPortTable=mBrdgTpPortTable, mBrdgBaseEntry=mBrdgBaseEntry, mBrdgBasePortTable=mBrdgBasePortTable, mBrdgStpPortState=mBrdgStpPortState, mBrdgBaseTable=mBrdgBaseTable, mBrdgTpPortInFrames=mBrdgTpPortInFrames, mBrdgStaticEntry=mBrdgStaticEntry, mBrdgTpFdbStatus=mBrdgTpFdbStatus, mBrdgStpEnable=mBrdgStpEnable, mBrdgConfigEntry=mBrdgConfigEntry, mBrdgTpPort=mBrdgTpPort, mBrdgStaticReceivePort=mBrdgStaticReceivePort, mBrdgStpPortPathCost=mBrdgStpPortPathCost, mBrdgStpPortStatsTxBPDUCount=mBrdgStpPortStatsTxBPDUCount, Timeout=Timeout, mBrdgTpPortBridgeIndex=mBrdgTpPortBridgeIndex, mBrdgStpPortEnable=mBrdgStpPortEnable, mBrdgStpPortBridgeIndex=mBrdgStpPortBridgeIndex, mBrdgTpLearningEnable=mBrdgTpLearningEnable, mBrdgStpPortTable=mBrdgStpPortTable, mBrdgTp=mBrdgTp, mBrdgStpPortForwardTransitions=mBrdgStpPortForwardTransitions, mBrdgBasePortMtuExceededDiscards=mBrdgBasePortMtuExceededDiscards, mBrdgStpTopChanges=mBrdgStpTopChanges, mBrdgStpPriority=mBrdgStpPriority, mBrdgStpForwardDelay=mBrdgStpForwardDelay, mBrdgTpTable=mBrdgTpTable, mBrdgStatic=mBrdgStatic, mBrdgTpFdbNumEntries=mBrdgTpFdbNumEntries, mBrdgBasePortCircuit=mBrdgBasePortCircuit, BridgeId=BridgeId, mBrdgStaticTable=mBrdgStaticTable, mBrdgStpPortDesignatedCost=mBrdgStpPortDesignatedCost, nncExtMultiBridge=nncExtMultiBridge, mBrdgStaticStatus=mBrdgStaticStatus, mBrdgTpFdbPort=mBrdgTpFdbPort, mBrdgTpBridgeIndex=mBrdgTpBridgeIndex, MacAddress=MacAddress, mBrdgConfigBridgePeakRate=mBrdgConfigBridgePeakRate, mBrdgStpPortStatsRxBPDUCount=mBrdgStpPortStatsRxBPDUCount, mBrdgTpFdbEntry=mBrdgTpFdbEntry, mBrdgStpPort=mBrdgStpPort, mBrdgStpBridgeIndex=mBrdgStpBridgeIndex, mBrdgStpBridgeForwardDelay=mBrdgStpBridgeForwardDelay, mBrdgStpEntry=mBrdgStpEntry, mBrdgTpFdbAddress=mBrdgTpFdbAddress, mBrdgTpLearnedEntryDiscards=mBrdgTpLearnedEntryDiscards, mBrdgConfig=mBrdgConfig, mBrdgBaseNumPorts=mBrdgBaseNumPorts, mBrdgStpPortDesignatedBridge=mBrdgStpPortDesignatedBridge, mBrdgStp=mBrdgStp, mBrdgStpPortEntry=mBrdgStpPortEntry, mBrdgBaseType=mBrdgBaseType, mBrdgStaticBridgeIndex=mBrdgStaticBridgeIndex, mBrdgTpPortInDiscards=mBrdgTpPortInDiscards, mBrdgTpFdbBridgeIndex=mBrdgTpFdbBridgeIndex, mBrdgTpPortOutFrames=mBrdgTpPortOutFrames, mBrdgTpEntry=mBrdgTpEntry, mBrdgStpDesignatedRoot=mBrdgStpDesignatedRoot, mBrdgStpBridgeMaxAge=mBrdgStpBridgeMaxAge, mBrdgStpBridgeHelloTime=mBrdgStpBridgeHelloTime, mBrdgBaseBridgeAddress=mBrdgBaseBridgeAddress, mBrdgStpTimeSinceTopologyChange=mBrdgStpTimeSinceTopologyChange, mBrdgBasePortEntry=mBrdgBasePortEntry, mBrdgBasePortBridgeIndex=mBrdgBasePortBridgeIndex, mBrdgTpFdbTable=mBrdgTpFdbTable, mBrdgTpFdbNumLearnedEntries=mBrdgTpFdbNumLearnedEntries, mBrdgStpProtocolSpecification=mBrdgStpProtocolSpecification, mBrdgStpRootPort=mBrdgStpRootPort, mBrdgStpHelloTime=mBrdgStpHelloTime, mBrdgTpAgingTime=mBrdgTpAgingTime, mBrdgBasePort=mBrdgBasePort, mBrdgBase=mBrdgBase, mBrdgConfigTable=mBrdgConfigTable, mBrdgStpRootCost=mBrdgStpRootCost, mBrdgBasePortIfIndex=mBrdgBasePortIfIndex, mBrdgStaticAllowedToGoTo=mBrdgStaticAllowedToGoTo, mBrdgStaticAddress=mBrdgStaticAddress, mBrdgStpPortDesignatedPort=mBrdgStpPortDesignatedPort, mBrdgTpPortMaxInfo=mBrdgTpPortMaxInfo, mBrdgBasePortDelayExceededDiscards=mBrdgBasePortDelayExceededDiscards, mBrdgStpPortPriority=mBrdgStpPortPriority, mBrdgTpPortEntry=mBrdgTpPortEntry, mBrdgConfigBridgeIndex=mBrdgConfigBridgeIndex, mBrdgConfigBridgeName=mBrdgConfigBridgeName, PYSNMP_MODULE_ID=nncExtMultiBridge, mBrdgStpMaxAge=mBrdgStpMaxAge, mBrdgStpPortDesignatedRoot=mBrdgStpPortDesignatedRoot)
