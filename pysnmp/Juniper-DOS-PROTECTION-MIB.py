#
# PySNMP MIB module Juniper-DOS-PROTECTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-DOS-PROTECTION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:51:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
JuniEnable, = mibBuilder.importSymbols("Juniper-TC", "JuniEnable")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Integer32, Unsigned32, TimeTicks, Bits, iso, ObjectIdentity, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, ModuleIdentity, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Unsigned32", "TimeTicks", "Bits", "iso", "ObjectIdentity", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "ModuleIdentity", "NotificationType", "Counter32")
RowStatus, TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "TextualConvention", "DisplayString")
juniDosProtectionMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80))
juniDosProtectionMIB.setRevisions(('2008-05-06 00:00', '2006-07-01 00:00', '2006-08-18 04:00', '2006-08-17 19:26', '2006-01-01 05:00',))
if mibBuilder.loadTexts: juniDosProtectionMIB.setLastUpdated('200805060000Z')
if mibBuilder.loadTexts: juniDosProtectionMIB.setOrganization('Juniper Networks, Inc.')
class JuniDosProtectionProtocolType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73))
    namedValues = NamedValues(("pppEchoRequest", 0), ("ppEchoReply", 1), ("pppEchoReplyFast", 2), ("pppControl", 3), ("atmControl", 4), ("atmOam", 5), ("atmDynamicIf", 6), ("atmInverseArp", 7), ("frameRelayControl", 8), ("frameRelayArp", 9), ("pppoeControl", 10), ("pppoePppConfig", 11), ("ethernetArpMiss", 12), ("ethernetArp", 13), ("ethernetFcBasedArp", 14), ("ethernetLacp", 15), ("ethernetOam", 16), ("ethernetDynamicIf", 17), ("ethernetPppTerminate", 18), ("slepSlarp", 19), ("slepSlarpReplyFast", 20), ("mplsTtlOnReceive", 21), ("mplsTtlOnTransmit", 22), ("mplsMtuExceeded", 23), ("itmL2tpControl", 24), ("flisInPayload", 25), ("flisInPayloadUpdateTable", 26), ("dhcpExternal", 27), ("ipOsi", 28), ("ipTtlExpired", 29), ("ipOptionsOther", 30), ("ipOptionsRouterAlert", 31), ("ipMulticastBroadcastOther", 32), ("ipMulticastDhcpSc", 33), ("ipMulticastControlSc", 34), ("ipMulticastControlIc", 35), ("ipMulticastVrrp", 36), ("ipMulticastCacheMiss", 37), ("ipMulticastCacheMissAutoReply", 38), ("ipMulticastWrongIf", 39), ("ipLocalDhcpSc", 40), ("ipLocalDhcpIc", 41), ("ipLocalIcmpEcho", 42), ("ipLocalIcmpOther", 43), ("ipLocalLDP", 44), ("ipLocalBgp", 45), ("ipLocalOspf", 46), ("ipLocalRsvp", 47), ("ipLocalPim", 48), ("ipLocalCops", 49), ("ipLocalL2tpControlSc", 50), ("ipLocalL2tpControlIc", 51), ("ipLocalOther", 52), ("ipLocalDemuxMiss", 53), ("ipRouteToSrpEthernet", 54), ("ipRouteNoRoute", 55), ("ipNormalPathMtu", 56), ("ipNeighborDiscovery", 57), ("ipNeighborDiscoveryMiss", 58), ("ipSearchError", 59), ("ipMld", 60), ("ipLocalPimAssert", 61), ("ipLocalBfd", 62), ("ipFastBfd", 63), ("ipLocalFastBfd", 64), ("ipIke", 65), ("ipReassembly", 66), ("ipLocalIcmpFragment", 67), ("ipLocalFragment", 68), ("ipAppClassifierHttpRedirect", 69), ("ipMulticastDhcpIc", 70), ("dhcpTesterIc", 71), ("atmDynamicIfPppData", 72), ("ipLocalLspPing", 73))

class JuniDosProtectionPriorityType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("hiGreenFcIc", 0), ("hiYellowFcIc", 1), ("loGreenFcIc", 2), ("loYellowFcIc", 3), ("hiGreenFcSc", 4), ("hiYellowFcSc", 5), ("loGreenFcSc", 6), ("loYellowFcSc", 7))

class JuniDosProtectionProtocolState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ok", 1), ("inTrouble", 2))

class JuniDosProtectionScfdsTableOverflowState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("notOverflowingOrGrouping", 1), ("grouping", 2), ("overflowing", 3))

class JuniDosProtectionProtocolPriorityType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("hiGreen", 0), ("hiYellow", 1), ("loGreen", 2), ("loYellow", 3), ("dataPath", 4))

class JuniDosProtectionProtocolCannedType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("default", 0), ("enetAccess", 1), ("atmAccess", 2), ("frame", 3), ("uplink", 4))

class JuniDosProtectionLayerId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 6, 11, 17, 19, 35, 50))
    namedValues = NamedValues(("ip", 0), ("ppp", 1), ("ethernet", 6), ("atm1483", 11), ("pppoe", 17), ("bridge1483", 19), ("vlan", 35), ("ipv6", 50))

class JuniDosProtectionControlProcessorDestination(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("ic", 0), ("sc", 1), ("dataPath", 2))

juniDosProtectionObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1))
juniDosProtectionScfdsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 1))
juniDosProtectionDpgGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2))
juniDosProtectionScfdsGlobalState = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 1, 1), JuniEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniDosProtectionScfdsGlobalState.setStatus('current')
juniDosProtectionScfdsGlobalGrouping = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 1, 2), JuniEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniDosProtectionScfdsGlobalGrouping.setStatus('current')
juniDosProtectionScfdsGlobalClearAll = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("ok", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniDosProtectionScfdsGlobalClearAll.setStatus('current')
juniDosProtectionScfdsGlobalDiscontinuityTime = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDosProtectionScfdsGlobalDiscontinuityTime.setStatus('current')
juniDosProtectionScfdsGlobalTableOverflowState = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 1, 5), JuniDosProtectionScfdsTableOverflowState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDosProtectionScfdsGlobalTableOverflowState.setStatus('current')
juniDosProtectionScfdsGlobalCurrentSuspiciousFlows = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDosProtectionScfdsGlobalCurrentSuspiciousFlows.setStatus('current')
juniDosProtectionScfdsGlobalNumberSuspiciousFlows = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDosProtectionScfdsGlobalNumberSuspiciousFlows.setStatus('current')
juniDosProtectionScfdsGlobalCurrentSuspiciousFlowGroups = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDosProtectionScfdsGlobalCurrentSuspiciousFlowGroups.setStatus('current')
juniDosProtectionScfdsGlobalNumberSuspiciousFlowGroups = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDosProtectionScfdsGlobalNumberSuspiciousFlowGroups.setStatus('current')
juniDosProtectionScfdsGlobalCurrentFalseNegativeFlows = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDosProtectionScfdsGlobalCurrentFalseNegativeFlows.setStatus('current')
juniDosProtectionScfdsGlobalNumberFalseNegativeFlows = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDosProtectionScfdsGlobalNumberFalseNegativeFlows.setStatus('current')
juniDosProtectionScfdsGlobalNumberTableOverflows = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDosProtectionScfdsGlobalNumberTableOverflows.setStatus('current')
juniDosProtectionScfdsProtocolTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 1, 13), )
if mibBuilder.loadTexts: juniDosProtectionScfdsProtocolTable.setStatus('current')
juniDosProtectionScfdsProtocolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 1, 13, 1), ).setIndexNames((0, "Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsProtocolIndex"))
if mibBuilder.loadTexts: juniDosProtectionScfdsProtocolEntry.setStatus('current')
juniDosProtectionScfdsProtocolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 1, 13, 1, 1), JuniDosProtectionProtocolType())
if mibBuilder.loadTexts: juniDosProtectionScfdsProtocolIndex.setStatus('current')
juniDosProtectionScfdsProtocolThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 1, 13, 1, 2), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(3, 65535), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniDosProtectionScfdsProtocolThreshold.setStatus('current')
juniDosProtectionScfdsProtocolLowThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 1, 13, 1, 3), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 32767), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniDosProtectionScfdsProtocolLowThreshold.setStatus('current')
juniDosProtectionScfdsProtocolBackoffTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 1, 13, 1, 4), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(10, 1000), )).clone(300)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniDosProtectionScfdsProtocolBackoffTime.setStatus('current')
juniDosProtectionScfdsProtocolState = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 1, 13, 1, 5), JuniDosProtectionProtocolState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDosProtectionScfdsProtocolState.setStatus('current')
juniDosProtectionScfdsProtocolTransitions = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 1, 13, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDosProtectionScfdsProtocolTransitions.setStatus('current')
juniDosProtectionDpgTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 1), )
if mibBuilder.loadTexts: juniDosProtectionDpgTable.setStatus('current')
juniDosProtectionDpgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 1, 1), ).setIndexNames((0, "Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgIndex"))
if mibBuilder.loadTexts: juniDosProtectionDpgEntry.setStatus('current')
juniDosProtectionDpgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: juniDosProtectionDpgIndex.setStatus('current')
juniDosProtectionDpgRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniDosProtectionDpgRowStatus.setStatus('current')
juniDosProtectionDpgCanned = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 1, 1, 3), JuniDosProtectionProtocolCannedType().clone('default')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniDosProtectionDpgCanned.setStatus('current')
juniDosProtectionDpgRevert = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no-revert", 0), ("revert", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniDosProtectionDpgRevert.setStatus('current')
juniDosProtectionDpgModified = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDosProtectionDpgModified.setStatus('current')
juniDosProtectionDpgReferences = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDosProtectionDpgReferences.setStatus('current')
juniDosProtectionDpgProtocolTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 2), )
if mibBuilder.loadTexts: juniDosProtectionDpgProtocolTable.setStatus('current')
juniDosProtectionDpgProtocolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 2, 1), ).setIndexNames((0, "Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgProtocolName"), (0, "Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgProtocolProtocol"))
if mibBuilder.loadTexts: juniDosProtectionDpgProtocolEntry.setStatus('current')
juniDosProtectionDpgProtocolName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: juniDosProtectionDpgProtocolName.setStatus('current')
juniDosProtectionDpgProtocolProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 2, 1, 2), JuniDosProtectionProtocolType())
if mibBuilder.loadTexts: juniDosProtectionDpgProtocolProtocol.setStatus('current')
juniDosProtectionDpgProtocolBurst = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(32, 65535), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniDosProtectionDpgProtocolBurst.setStatus('current')
juniDosProtectionDpgProtocolDropProbability = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 2, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(10, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniDosProtectionDpgProtocolDropProbability.setStatus('current')
juniDosProtectionDpgProtocolRate = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 2, 1, 5), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(64, 65535), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniDosProtectionDpgProtocolRate.setStatus('current')
juniDosProtectionDpgProtocolSkipPriorityRateLimiter = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 2, 1, 6), JuniEnable()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniDosProtectionDpgProtocolSkipPriorityRateLimiter.setStatus('current')
juniDosProtectionDpgProtocolWeight = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 2, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(100, 500)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniDosProtectionDpgProtocolWeight.setStatus('current')
juniDosProtectionDpgProtocolPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 2, 1, 8), JuniDosProtectionProtocolPriorityType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniDosProtectionDpgProtocolPriority.setStatus('current')
juniDosProtectionDpgProtocolModified = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 2, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDosProtectionDpgProtocolModified.setStatus('current')
juniDosProtectionDpgProtocolDestination = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 2, 1, 10), JuniDosProtectionControlProcessorDestination()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDosProtectionDpgProtocolDestination.setStatus('current')
juniDosProtectionDpgPriorityTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 3), )
if mibBuilder.loadTexts: juniDosProtectionDpgPriorityTable.setStatus('current')
juniDosProtectionDpgPriorityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 3, 1), ).setIndexNames((0, "Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgPriorityName"), (0, "Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgPriorityPriority"))
if mibBuilder.loadTexts: juniDosProtectionDpgPriorityEntry.setStatus('current')
juniDosProtectionDpgPriorityName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: juniDosProtectionDpgPriorityName.setStatus('current')
juniDosProtectionDpgPriorityPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 3, 1, 2), JuniDosProtectionPriorityType())
if mibBuilder.loadTexts: juniDosProtectionDpgPriorityPriority.setStatus('current')
juniDosProtectionDpgPriorityBurst = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 3, 1, 3), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(32, 65535), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniDosProtectionDpgPriorityBurst.setStatus('current')
juniDosProtectionDpgPriorityOverSubscriptionFactor = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 3, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(100, 1000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniDosProtectionDpgPriorityOverSubscriptionFactor.setStatus('current')
juniDosProtectionDpgPriorityRate = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 3, 1, 5), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(64, 65535), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniDosProtectionDpgPriorityRate.setStatus('current')
juniDosProtectionDpgPriorityModified = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 3, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniDosProtectionDpgPriorityModified.setStatus('current')
juniDosProtectionDpgAttachTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 4), )
if mibBuilder.loadTexts: juniDosProtectionDpgAttachTable.setStatus('current')
juniDosProtectionDpgAttachEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 4, 1), ).setIndexNames((0, "Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgAttachIndex"))
if mibBuilder.loadTexts: juniDosProtectionDpgAttachEntry.setStatus('current')
juniDosProtectionDpgAttachIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 4, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: juniDosProtectionDpgAttachIndex.setStatus('current')
juniDosProtectionDpgAttachRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 4, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniDosProtectionDpgAttachRowStatus.setStatus('current')
juniDosProtectionDpgAttachName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 4, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniDosProtectionDpgAttachName.setStatus('current')
juniDosProtectionDpgAttachConfigured = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 4, 1, 4), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniDosProtectionDpgAttachConfigured.setStatus('current')
juniDosProtectionDpgProfileTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 5), )
if mibBuilder.loadTexts: juniDosProtectionDpgProfileTable.setStatus('current')
juniDosProtectionDpgProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 5, 1), ).setIndexNames((0, "Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgProfileProfileId"), (0, "Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgProfileLayerId"))
if mibBuilder.loadTexts: juniDosProtectionDpgProfileEntry.setStatus('current')
juniDosProtectionDpgProfileProfileId = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 5, 1, 1), Unsigned32())
if mibBuilder.loadTexts: juniDosProtectionDpgProfileProfileId.setStatus('current')
juniDosProtectionDpgProfileLayerId = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 5, 1, 2), JuniDosProtectionLayerId())
if mibBuilder.loadTexts: juniDosProtectionDpgProfileLayerId.setStatus('current')
juniDosProtectionDpgProfileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 5, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniDosProtectionDpgProfileRowStatus.setStatus('current')
juniDosProtectionDpgProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 1, 2, 5, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniDosProtectionDpgProfileName.setStatus('current')
juniDosProtectionMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 4))
juniDosProtectionMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 4, 1))
juniDosProtectionMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 4, 2))
juniDosProtectionCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 4, 1, 1)).setObjects(("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDosProtectionCompliance = juniDosProtectionCompliance.setStatus('obsolete')
juniDosProtectionCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 4, 1, 2)).setObjects(("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDosProtectionCompliance2 = juniDosProtectionCompliance2.setStatus('current')
juniDosProtectionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 4, 2, 1)).setObjects(("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalState"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalGrouping"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalClearAll"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalDiscontinuityTime"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalTableOverflowState"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalCurrentSuspiciousFlows"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalNumberSuspiciousFlows"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalCurrentSuspiciousFlowGroups"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalNumberSuspiciousFlowGroups"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalCurrentFalseNegativeFlows"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalNumberFalseNegativeFlows"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalNumberTableOverflows"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsProtocolThreshold"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsProtocolLowThreshold"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsProtocolBackoffTime"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsProtocolState"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsProtocolTransitions"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDosProtectionGroup = juniDosProtectionGroup.setStatus('obsolete')
juniDosProtectionGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 80, 4, 2, 2)).setObjects(("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalState"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalGrouping"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalClearAll"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalDiscontinuityTime"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalTableOverflowState"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalCurrentSuspiciousFlows"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalNumberSuspiciousFlows"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalCurrentSuspiciousFlowGroups"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalNumberSuspiciousFlowGroups"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalCurrentFalseNegativeFlows"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalNumberFalseNegativeFlows"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsGlobalNumberTableOverflows"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsProtocolThreshold"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsProtocolLowThreshold"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsProtocolBackoffTime"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsProtocolState"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionScfdsProtocolTransitions"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgRowStatus"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgCanned"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgRevert"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgModified"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgReferences"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgProtocolBurst"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgProtocolDropProbability"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgProtocolRate"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgProtocolSkipPriorityRateLimiter"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgProtocolWeight"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgProtocolModified"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgPriorityBurst"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgPriorityOverSubscriptionFactor"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgPriorityRate"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgPriorityModified"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgAttachRowStatus"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgAttachName"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgProfileRowStatus"), ("Juniper-DOS-PROTECTION-MIB", "juniDosProtectionDpgProfileName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniDosProtectionGroup2 = juniDosProtectionGroup2.setStatus('current')
mibBuilder.exportSymbols("Juniper-DOS-PROTECTION-MIB", juniDosProtectionDpgProtocolTable=juniDosProtectionDpgProtocolTable, juniDosProtectionDpgProfileTable=juniDosProtectionDpgProfileTable, juniDosProtectionCompliance2=juniDosProtectionCompliance2, juniDosProtectionDpgProtocolDestination=juniDosProtectionDpgProtocolDestination, juniDosProtectionScfdsGlobalCurrentSuspiciousFlowGroups=juniDosProtectionScfdsGlobalCurrentSuspiciousFlowGroups, juniDosProtectionScfdsGlobalState=juniDosProtectionScfdsGlobalState, juniDosProtectionDpgProfileEntry=juniDosProtectionDpgProfileEntry, juniDosProtectionDpgProtocolDropProbability=juniDosProtectionDpgProtocolDropProbability, JuniDosProtectionProtocolState=JuniDosProtectionProtocolState, juniDosProtectionMIBGroups=juniDosProtectionMIBGroups, juniDosProtectionScfdsProtocolState=juniDosProtectionScfdsProtocolState, juniDosProtectionDpgProtocolEntry=juniDosProtectionDpgProtocolEntry, juniDosProtectionDpgProtocolWeight=juniDosProtectionDpgProtocolWeight, juniDosProtectionDpgReferences=juniDosProtectionDpgReferences, juniDosProtectionDpgProfileRowStatus=juniDosProtectionDpgProfileRowStatus, juniDosProtectionScfdsProtocolTable=juniDosProtectionScfdsProtocolTable, juniDosProtectionDpgModified=juniDosProtectionDpgModified, juniDosProtectionGroup2=juniDosProtectionGroup2, juniDosProtectionScfdsGlobalTableOverflowState=juniDosProtectionScfdsGlobalTableOverflowState, juniDosProtectionDpgProtocolModified=juniDosProtectionDpgProtocolModified, juniDosProtectionDpgProfileLayerId=juniDosProtectionDpgProfileLayerId, juniDosProtectionDpgProfileName=juniDosProtectionDpgProfileName, juniDosProtectionDpgPriorityTable=juniDosProtectionDpgPriorityTable, juniDosProtectionDpgPriorityRate=juniDosProtectionDpgPriorityRate, juniDosProtectionScfdsGlobalClearAll=juniDosProtectionScfdsGlobalClearAll, juniDosProtectionDpgAttachConfigured=juniDosProtectionDpgAttachConfigured, juniDosProtectionDpgRevert=juniDosProtectionDpgRevert, juniDosProtectionDpgProfileProfileId=juniDosProtectionDpgProfileProfileId, juniDosProtectionScfdsProtocolThreshold=juniDosProtectionScfdsProtocolThreshold, juniDosProtectionScfdsGlobalNumberSuspiciousFlows=juniDosProtectionScfdsGlobalNumberSuspiciousFlows, juniDosProtectionScfdsGlobalNumberTableOverflows=juniDosProtectionScfdsGlobalNumberTableOverflows, juniDosProtectionMIB=juniDosProtectionMIB, juniDosProtectionDpgGroup=juniDosProtectionDpgGroup, juniDosProtectionDpgPriorityPriority=juniDosProtectionDpgPriorityPriority, juniDosProtectionCompliance=juniDosProtectionCompliance, juniDosProtectionDpgProtocolSkipPriorityRateLimiter=juniDosProtectionDpgProtocolSkipPriorityRateLimiter, juniDosProtectionDpgAttachRowStatus=juniDosProtectionDpgAttachRowStatus, JuniDosProtectionProtocolType=JuniDosProtectionProtocolType, juniDosProtectionDpgProtocolPriority=juniDosProtectionDpgProtocolPriority, juniDosProtectionDpgPriorityOverSubscriptionFactor=juniDosProtectionDpgPriorityOverSubscriptionFactor, juniDosProtectionDpgProtocolBurst=juniDosProtectionDpgProtocolBurst, juniDosProtectionScfdsProtocolTransitions=juniDosProtectionScfdsProtocolTransitions, juniDosProtectionScfdsGlobalCurrentSuspiciousFlows=juniDosProtectionScfdsGlobalCurrentSuspiciousFlows, juniDosProtectionMIBCompliances=juniDosProtectionMIBCompliances, juniDosProtectionDpgProtocolName=juniDosProtectionDpgProtocolName, juniDosProtectionScfdsProtocolLowThreshold=juniDosProtectionScfdsProtocolLowThreshold, JuniDosProtectionLayerId=JuniDosProtectionLayerId, juniDosProtectionScfdsProtocolIndex=juniDosProtectionScfdsProtocolIndex, juniDosProtectionDpgRowStatus=juniDosProtectionDpgRowStatus, juniDosProtectionDpgEntry=juniDosProtectionDpgEntry, juniDosProtectionDpgProtocolRate=juniDosProtectionDpgProtocolRate, juniDosProtectionDpgAttachIndex=juniDosProtectionDpgAttachIndex, juniDosProtectionDpgCanned=juniDosProtectionDpgCanned, juniDosProtectionScfdsGlobalGrouping=juniDosProtectionScfdsGlobalGrouping, juniDosProtectionDpgProtocolProtocol=juniDosProtectionDpgProtocolProtocol, juniDosProtectionDpgAttachName=juniDosProtectionDpgAttachName, juniDosProtectionScfdsGlobalCurrentFalseNegativeFlows=juniDosProtectionScfdsGlobalCurrentFalseNegativeFlows, juniDosProtectionScfdsProtocolEntry=juniDosProtectionScfdsProtocolEntry, juniDosProtectionGroup=juniDosProtectionGroup, JuniDosProtectionControlProcessorDestination=JuniDosProtectionControlProcessorDestination, juniDosProtectionScfdsGlobalNumberFalseNegativeFlows=juniDosProtectionScfdsGlobalNumberFalseNegativeFlows, juniDosProtectionDpgTable=juniDosProtectionDpgTable, juniDosProtectionObjects=juniDosProtectionObjects, juniDosProtectionScfdsGlobalNumberSuspiciousFlowGroups=juniDosProtectionScfdsGlobalNumberSuspiciousFlowGroups, juniDosProtectionScfdsGlobalDiscontinuityTime=juniDosProtectionScfdsGlobalDiscontinuityTime, juniDosProtectionDpgPriorityName=juniDosProtectionDpgPriorityName, juniDosProtectionScfdsGroup=juniDosProtectionScfdsGroup, JuniDosProtectionPriorityType=JuniDosProtectionPriorityType, JuniDosProtectionScfdsTableOverflowState=JuniDosProtectionScfdsTableOverflowState, JuniDosProtectionProtocolPriorityType=JuniDosProtectionProtocolPriorityType, juniDosProtectionDpgIndex=juniDosProtectionDpgIndex, juniDosProtectionDpgAttachTable=juniDosProtectionDpgAttachTable, juniDosProtectionMIBConformance=juniDosProtectionMIBConformance, juniDosProtectionDpgPriorityBurst=juniDosProtectionDpgPriorityBurst, juniDosProtectionScfdsProtocolBackoffTime=juniDosProtectionScfdsProtocolBackoffTime, JuniDosProtectionProtocolCannedType=JuniDosProtectionProtocolCannedType, juniDosProtectionDpgPriorityEntry=juniDosProtectionDpgPriorityEntry, juniDosProtectionDpgAttachEntry=juniDosProtectionDpgAttachEntry, PYSNMP_MODULE_ID=juniDosProtectionMIB, juniDosProtectionDpgPriorityModified=juniDosProtectionDpgPriorityModified)
