#
# PySNMP MIB module MPLS-TE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MPLS-TE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:04:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAddressIPv6, InetAddressIPv4 = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv6", "InetAddressIPv4")
MplsLSPID, MplsBurstSize, MplsBitRate = mibBuilder.importSymbols("MPLS-LSR-MIB", "MplsLSPID", "MplsBurstSize", "MplsBitRate")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter64, experimental, Unsigned32, Counter32, Integer32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, TimeTicks, NotificationType, ObjectIdentity, Gauge32, IpAddress, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "experimental", "Unsigned32", "Counter32", "Integer32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "TimeTicks", "NotificationType", "ObjectIdentity", "Gauge32", "IpAddress", "MibIdentifier")
DisplayString, RowStatus, StorageType, RowPointer, TimeStamp, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "StorageType", "RowPointer", "TimeStamp", "TextualConvention", "TruthValue")
mplsTeMIB = ModuleIdentity((1, 3, 6, 1, 3, 95))
mplsTeMIB.setRevisions(('2000-11-21 12:00', '2000-07-14 12:00', '2000-05-26 12:00', '2000-03-03 12:00', '1999-07-16 12:00',))
if mibBuilder.loadTexts: mplsTeMIB.setLastUpdated('200011211200Z')
if mibBuilder.loadTexts: mplsTeMIB.setOrganization('Multiprotocol Label Switching (MPLS) Working Group')
class MplsTunnelIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 65535)

class MplsTunnelInstanceIndex(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class MplsLsrId(TextualConvention, Unsigned32):
    status = 'current'

class MplsPathIndex(TextualConvention, Unsigned32):
    status = 'current'

class MplsPathIndexOrZero(TextualConvention, Unsigned32):
    status = 'current'

mplsTeScalars = MibIdentifier((1, 3, 6, 1, 3, 95, 1))
mplsTeObjects = MibIdentifier((1, 3, 6, 1, 3, 95, 2))
mplsTeNotifications = MibIdentifier((1, 3, 6, 1, 3, 95, 3))
mplsTeNotifyPrefix = MibIdentifier((1, 3, 6, 1, 3, 95, 3, 0))
mplsTeConformance = MibIdentifier((1, 3, 6, 1, 3, 95, 4))
mplsTunnelConfigured = MibScalar((1, 3, 6, 1, 3, 95, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelConfigured.setStatus('current')
mplsTunnelActive = MibScalar((1, 3, 6, 1, 3, 95, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelActive.setStatus('current')
mplsTunnelTEDistProto = MibScalar((1, 3, 6, 1, 3, 95, 1, 3), Bits().clone(namedValues=NamedValues(("other", 0), ("ospf", 1), ("isis", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelTEDistProto.setStatus('current')
mplsTunnelMaxHops = MibScalar((1, 3, 6, 1, 3, 95, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelMaxHops.setStatus('current')
mplsTunnelIndexNext = MibScalar((1, 3, 6, 1, 3, 95, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelIndexNext.setStatus('current')
mplsTunnelTable = MibTable((1, 3, 6, 1, 3, 95, 2, 2), )
if mibBuilder.loadTexts: mplsTunnelTable.setStatus('current')
mplsTunnelEntry = MibTableRow((1, 3, 6, 1, 3, 95, 2, 2, 1), ).setIndexNames((0, "MPLS-TE-MIB", "mplsTunnelIndex"), (0, "MPLS-TE-MIB", "mplsTunnelInstance"), (0, "MPLS-TE-MIB", "mplsTunnelIngressLSRId"), (0, "MPLS-TE-MIB", "mplsTunnelEgressLSRId"))
if mibBuilder.loadTexts: mplsTunnelEntry.setStatus('current')
mplsTunnelIndex = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 2, 1, 1), MplsTunnelIndex())
if mibBuilder.loadTexts: mplsTunnelIndex.setStatus('current')
mplsTunnelInstance = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 2, 1, 2), MplsTunnelInstanceIndex())
if mibBuilder.loadTexts: mplsTunnelInstance.setStatus('current')
mplsTunnelIngressLSRId = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 2, 1, 3), MplsLsrId())
if mibBuilder.loadTexts: mplsTunnelIngressLSRId.setStatus('current')
mplsTunnelEgressLSRId = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 2, 1, 4), MplsLsrId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelEgressLSRId.setStatus('current')
mplsTunnelName = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 2, 1, 5), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelName.setStatus('current')
mplsTunnelDescr = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 2, 1, 6), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelDescr.setStatus('current')
mplsTunnelIsIf = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 2, 1, 7), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelIsIf.setStatus('current')
mplsTunnelIfIndex = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 2, 1, 8), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelIfIndex.setStatus('current')
mplsTunnelXCPointer = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 2, 1, 9), RowPointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelXCPointer.setStatus('current')
mplsTunnelSignallingProto = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("rsvp", 2), ("crldp", 3), ("other", 4))).clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelSignallingProto.setStatus('current')
mplsTunnelSetupPrio = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelSetupPrio.setStatus('current')
mplsTunnelHoldingPrio = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 2, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelHoldingPrio.setStatus('current')
mplsTunnelSessionAttributes = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 2, 1, 13), Bits().clone(namedValues=NamedValues(("fastReroute", 0), ("mergingPermitted", 1), ("isPersistent", 2), ("isPinned", 3), ("isComputed", 4), ("recordRoute", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelSessionAttributes.setStatus('current')
mplsTunnelOwner = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("admin", 1), ("rsvp", 2), ("crldp", 3), ("policyAgent", 4), ("other", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelOwner.setStatus('current')
mplsTunnelLocalProtectInUse = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 2, 1, 15), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelLocalProtectInUse.setStatus('current')
mplsTunnelResourcePointer = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 2, 1, 16), RowPointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelResourcePointer.setStatus('current')
mplsTunnelInstancePriority = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 2, 1, 17), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelInstancePriority.setStatus('current')
mplsTunnelHopTableIndex = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 2, 1, 18), MplsPathIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelHopTableIndex.setStatus('current')
mplsTunnelARHopTableIndex = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 2, 1, 19), MplsPathIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelARHopTableIndex.setStatus('current')
mplsTunnelCHopTableIndex = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 2, 1, 20), MplsPathIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelCHopTableIndex.setStatus('current')
mplsTunnelPrimaryInstance = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 2, 1, 21), MplsTunnelInstanceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelPrimaryInstance.setStatus('current')
mplsTunnelPrimaryTimeUp = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 2, 1, 22), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelPrimaryTimeUp.setStatus('current')
mplsTunnelPathChanges = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 2, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelPathChanges.setStatus('current')
mplsTunnelLastPathChange = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 2, 1, 24), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelLastPathChange.setStatus('current')
mplsTunnelCreationTime = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 2, 1, 25), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelCreationTime.setStatus('current')
mplsTunnelStateTransitions = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 2, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelStateTransitions.setStatus('current')
mplsTunnelIncludeAnyAffinity = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 2, 1, 27), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelIncludeAnyAffinity.setStatus('current')
mplsTunnelIncludeAllAffinity = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 2, 1, 28), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelIncludeAllAffinity.setStatus('current')
mplsTunnelExcludeAllAffinity = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 2, 1, 29), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelExcludeAllAffinity.setStatus('current')
mplsTunnelPathInUse = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 2, 1, 30), MplsPathIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelPathInUse.setStatus('current')
mplsTunnelRole = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 2, 1, 31), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("head", 1), ("transit", 2), ("tail", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelRole.setStatus('current')
mplsTunnelTotalUpTime = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 2, 1, 32), TimeTicks()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelTotalUpTime.setStatus('current')
mplsTunnelInstanceUpTime = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 2, 1, 33), TimeTicks()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelInstanceUpTime.setStatus('current')
mplsTunnelAdminStatus = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 2, 1, 34), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelAdminStatus.setStatus('current')
mplsTunnelOperStatus = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 2, 1, 35), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3), ("unknown", 4), ("dormant", 5), ("notPresent", 6), ("lowerLayerDown", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelOperStatus.setStatus('current')
mplsTunnelRowStatus = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 2, 1, 36), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelRowStatus.setStatus('current')
mplsTunnelStorageType = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 2, 1, 37), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelStorageType.setStatus('current')
mplsTunnelHopListIndexNext = MibScalar((1, 3, 6, 1, 3, 95, 2, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelHopListIndexNext.setStatus('current')
mplsTunnelHopTable = MibTable((1, 3, 6, 1, 3, 95, 2, 4), )
if mibBuilder.loadTexts: mplsTunnelHopTable.setStatus('current')
mplsTunnelHopEntry = MibTableRow((1, 3, 6, 1, 3, 95, 2, 4, 1), ).setIndexNames((0, "MPLS-TE-MIB", "mplsTunnelHopListIndex"), (0, "MPLS-TE-MIB", "mplsPathOptionIndex"), (0, "MPLS-TE-MIB", "mplsTunnelHopIndex"))
if mibBuilder.loadTexts: mplsTunnelHopEntry.setStatus('current')
mplsTunnelHopListIndex = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 4, 1, 1), MplsPathIndex())
if mibBuilder.loadTexts: mplsTunnelHopListIndex.setStatus('current')
mplsPathOptionIndex = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 4, 1, 2), MplsPathIndex())
if mibBuilder.loadTexts: mplsPathOptionIndex.setStatus('current')
mplsTunnelHopIndex = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 4, 1, 3), MplsPathIndex())
if mibBuilder.loadTexts: mplsTunnelHopIndex.setStatus('current')
mplsTunnelHopAddrType = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ipV4", 1), ("ipV6", 2), ("asNumber", 3), ("lspid", 4))).clone('ipV4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelHopAddrType.setStatus('current')
mplsTunnelHopIpv4Addr = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 4, 1, 5), InetAddressIPv4()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelHopIpv4Addr.setStatus('current')
mplsTunnelHopIpv4PrefixLen = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 4, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelHopIpv4PrefixLen.setStatus('current')
mplsTunnelHopIpv6Addr = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 4, 1, 7), InetAddressIPv6()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelHopIpv6Addr.setStatus('current')
mplsTunnelHopIpv6PrefixLen = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 4, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelHopIpv6PrefixLen.setStatus('current')
mplsTunnelHopAsNumber = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 4, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelHopAsNumber.setStatus('current')
mplsTunnelHopLspId = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 4, 1, 10), MplsLSPID()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelHopLspId.setStatus('current')
mplsTunnelHopType = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 4, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("strict", 1), ("loose", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelHopType.setStatus('current')
mplsTunnelHopRowStatus = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 4, 1, 12), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelHopRowStatus.setStatus('current')
mplsTunnelHopStorageType = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 4, 1, 13), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelHopStorageType.setStatus('current')
mplsTunnelResourceIndexNext = MibScalar((1, 3, 6, 1, 3, 95, 2, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelResourceIndexNext.setStatus('current')
mplsTunnelResourceTable = MibTable((1, 3, 6, 1, 3, 95, 2, 6), )
if mibBuilder.loadTexts: mplsTunnelResourceTable.setStatus('current')
mplsTunnelResourceEntry = MibTableRow((1, 3, 6, 1, 3, 95, 2, 6, 1), ).setIndexNames((0, "MPLS-TE-MIB", "mplsTunnelResourceIndex"))
if mibBuilder.loadTexts: mplsTunnelResourceEntry.setStatus('current')
mplsTunnelResourceIndex = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 6, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: mplsTunnelResourceIndex.setStatus('current')
mplsTunnelResourceMaxRate = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 6, 1, 2), MplsBitRate()).setUnits('bits per second').setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelResourceMaxRate.setStatus('current')
mplsTunnelResourceMeanRate = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 6, 1, 3), MplsBitRate()).setUnits('bits per second').setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelResourceMeanRate.setStatus('current')
mplsTunnelResourceMaxBurstSize = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 6, 1, 4), MplsBurstSize()).setUnits('bytes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelResourceMaxBurstSize.setStatus('current')
mplsTunnelResourceRowStatus = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 6, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelResourceRowStatus.setStatus('current')
mplsTunnelResourceStorageType = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 6, 1, 6), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsTunnelResourceStorageType.setStatus('current')
mplsTunnelARHopTable = MibTable((1, 3, 6, 1, 3, 95, 2, 7), )
if mibBuilder.loadTexts: mplsTunnelARHopTable.setStatus('current')
mplsTunnelARHopEntry = MibTableRow((1, 3, 6, 1, 3, 95, 2, 7, 1), ).setIndexNames((0, "MPLS-TE-MIB", "mplsTunnelARHopListIndex"), (0, "MPLS-TE-MIB", "mplsTunnelARHopIndex"))
if mibBuilder.loadTexts: mplsTunnelARHopEntry.setStatus('current')
mplsTunnelARHopListIndex = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 7, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: mplsTunnelARHopListIndex.setStatus('current')
mplsTunnelARHopIndex = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 7, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: mplsTunnelARHopIndex.setStatus('current')
mplsTunnelARHopAddrType = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ipV4", 1), ("ipV6", 2), ("asNumber", 3))).clone('ipV4')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelARHopAddrType.setStatus('current')
mplsTunnelARHopIpv4Addr = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 7, 1, 4), InetAddressIPv4()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelARHopIpv4Addr.setStatus('current')
mplsTunnelARHopIpv4PrefixLen = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 7, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelARHopIpv4PrefixLen.setStatus('current')
mplsTunnelARHopIpv6Addr = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 7, 1, 6), InetAddressIPv6()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelARHopIpv6Addr.setStatus('current')
mplsTunnelARHopIpv6PrefixLen = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 7, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelARHopIpv6PrefixLen.setStatus('current')
mplsTunnelARHopAsNumber = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 7, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelARHopAsNumber.setStatus('current')
mplsTunnelARHopType = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 7, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("strict", 1), ("loose", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelARHopType.setStatus('current')
mplsTunnelCHopTable = MibTable((1, 3, 6, 1, 3, 95, 2, 8), )
if mibBuilder.loadTexts: mplsTunnelCHopTable.setStatus('current')
mplsTunnelCHopEntry = MibTableRow((1, 3, 6, 1, 3, 95, 2, 8, 1), ).setIndexNames((0, "MPLS-TE-MIB", "mplsTunnelCHopListIndex"), (0, "MPLS-TE-MIB", "mplsTunnelCHopIndex"))
if mibBuilder.loadTexts: mplsTunnelCHopEntry.setStatus('current')
mplsTunnelCHopListIndex = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 8, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: mplsTunnelCHopListIndex.setStatus('current')
mplsTunnelCHopIndex = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 8, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: mplsTunnelCHopIndex.setStatus('current')
mplsTunnelCHopAddrType = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ipV4", 1), ("ipV6", 2), ("asNumber", 3))).clone('ipV4')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelCHopAddrType.setStatus('current')
mplsTunnelCHopIpv4Addr = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 8, 1, 4), InetAddressIPv4()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelCHopIpv4Addr.setStatus('current')
mplsTunnelCHopIpv4PrefixLen = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 8, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelCHopIpv4PrefixLen.setStatus('current')
mplsTunnelCHopIpv6Addr = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 8, 1, 6), InetAddressIPv6()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelCHopIpv6Addr.setStatus('current')
mplsTunnelCHopIpv6PrefixLen = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 8, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelCHopIpv6PrefixLen.setStatus('current')
mplsTunnelCHopAsNumber = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 8, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelCHopAsNumber.setStatus('current')
mplsTunnelCHopType = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 8, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("strict", 1), ("loose", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelCHopType.setStatus('current')
mplsTunnelPerfTable = MibTable((1, 3, 6, 1, 3, 95, 2, 9), )
if mibBuilder.loadTexts: mplsTunnelPerfTable.setStatus('current')
mplsTunnelPerfEntry = MibTableRow((1, 3, 6, 1, 3, 95, 2, 9, 1), )
mplsTunnelEntry.registerAugmentions(("MPLS-TE-MIB", "mplsTunnelPerfEntry"))
mplsTunnelPerfEntry.setIndexNames(*mplsTunnelEntry.getIndexNames())
if mibBuilder.loadTexts: mplsTunnelPerfEntry.setStatus('current')
mplsTunnelPerfPackets = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 9, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelPerfPackets.setStatus('current')
mplsTunnelPerfHCPackets = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 9, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelPerfHCPackets.setStatus('current')
mplsTunnelPerfErrors = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 9, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelPerfErrors.setStatus('current')
mplsTunnelPerfBytes = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 9, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelPerfBytes.setStatus('current')
mplsTunnelPerfHCBytes = MibTableColumn((1, 3, 6, 1, 3, 95, 2, 9, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelPerfHCBytes.setStatus('current')
mplsTunnelTrapEnable = MibScalar((1, 3, 6, 1, 3, 95, 2, 10), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mplsTunnelTrapEnable.setStatus('current')
mplsTunnelUp = NotificationType((1, 3, 6, 1, 3, 95, 3, 0, 1)).setObjects(("MPLS-TE-MIB", "mplsTunnelAdminStatus"), ("MPLS-TE-MIB", "mplsTunnelOperStatus"))
if mibBuilder.loadTexts: mplsTunnelUp.setStatus('current')
mplsTunnelDown = NotificationType((1, 3, 6, 1, 3, 95, 3, 0, 2)).setObjects(("MPLS-TE-MIB", "mplsTunnelAdminStatus"), ("MPLS-TE-MIB", "mplsTunnelOperStatus"))
if mibBuilder.loadTexts: mplsTunnelDown.setStatus('current')
mplsTunnelRerouted = NotificationType((1, 3, 6, 1, 3, 95, 3, 0, 3)).setObjects(("MPLS-TE-MIB", "mplsTunnelAdminStatus"), ("MPLS-TE-MIB", "mplsTunnelOperStatus"))
if mibBuilder.loadTexts: mplsTunnelRerouted.setStatus('current')
mplsTeGroups = MibIdentifier((1, 3, 6, 1, 3, 95, 4, 1))
mplsTeCompliances = MibIdentifier((1, 3, 6, 1, 3, 95, 4, 2))
mplsTeModuleCompliance = ModuleCompliance((1, 3, 6, 1, 3, 95, 4, 2, 1)).setObjects(("MPLS-TE-MIB", "mplsTunnelGroup"), ("MPLS-TE-MIB", "mplsTunnelScalarGroup"), ("MPLS-TE-MIB", "mplsTunnelManualGroup"), ("MPLS-TE-MIB", "mplsTunnelSignaledGroup"), ("MPLS-TE-MIB", "mplsTunnelIsNotIntfcGroup"), ("MPLS-TE-MIB", "mplsTunnelIsIntfcGroup"), ("MPLS-TE-MIB", "mplsTunnelOptionalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsTeModuleCompliance = mplsTeModuleCompliance.setStatus('current')
mplsTunnelGroup = ObjectGroup((1, 3, 6, 1, 3, 95, 4, 1, 1)).setObjects(("MPLS-TE-MIB", "mplsTunnelIndexNext"), ("MPLS-TE-MIB", "mplsTunnelName"), ("MPLS-TE-MIB", "mplsTunnelDescr"), ("MPLS-TE-MIB", "mplsTunnelOwner"), ("MPLS-TE-MIB", "mplsTunnelXCPointer"), ("MPLS-TE-MIB", "mplsTunnelIfIndex"), ("MPLS-TE-MIB", "mplsTunnelHopTableIndex"), ("MPLS-TE-MIB", "mplsTunnelARHopTableIndex"), ("MPLS-TE-MIB", "mplsTunnelCHopTableIndex"), ("MPLS-TE-MIB", "mplsTunnelAdminStatus"), ("MPLS-TE-MIB", "mplsTunnelOperStatus"), ("MPLS-TE-MIB", "mplsTunnelRowStatus"), ("MPLS-TE-MIB", "mplsTunnelTrapEnable"), ("MPLS-TE-MIB", "mplsTunnelStorageType"), ("MPLS-TE-MIB", "mplsTunnelConfigured"), ("MPLS-TE-MIB", "mplsTunnelActive"), ("MPLS-TE-MIB", "mplsTunnelPrimaryInstance"), ("MPLS-TE-MIB", "mplsTunnelPrimaryTimeUp"), ("MPLS-TE-MIB", "mplsTunnelPathChanges"), ("MPLS-TE-MIB", "mplsTunnelLastPathChange"), ("MPLS-TE-MIB", "mplsTunnelCreationTime"), ("MPLS-TE-MIB", "mplsTunnelStateTransitions"), ("MPLS-TE-MIB", "mplsTunnelEgressLSRId"), ("MPLS-TE-MIB", "mplsTunnelIncludeAnyAffinity"), ("MPLS-TE-MIB", "mplsTunnelIncludeAllAffinity"), ("MPLS-TE-MIB", "mplsTunnelExcludeAllAffinity"), ("MPLS-TE-MIB", "mplsTunnelPerfPackets"), ("MPLS-TE-MIB", "mplsTunnelPerfHCPackets"), ("MPLS-TE-MIB", "mplsTunnelPerfErrors"), ("MPLS-TE-MIB", "mplsTunnelPerfBytes"), ("MPLS-TE-MIB", "mplsTunnelPerfHCBytes"), ("MPLS-TE-MIB", "mplsTunnelResourcePointer"), ("MPLS-TE-MIB", "mplsTunnelInstancePriority"), ("MPLS-TE-MIB", "mplsTunnelPathInUse"), ("MPLS-TE-MIB", "mplsTunnelRole"), ("MPLS-TE-MIB", "mplsTunnelTotalUpTime"), ("MPLS-TE-MIB", "mplsTunnelInstanceUpTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsTunnelGroup = mplsTunnelGroup.setStatus('current')
mplsTunnelManualGroup = ObjectGroup((1, 3, 6, 1, 3, 95, 4, 1, 2)).setObjects(("MPLS-TE-MIB", "mplsTunnelSignallingProto"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsTunnelManualGroup = mplsTunnelManualGroup.setStatus('current')
mplsTunnelSignaledGroup = ObjectGroup((1, 3, 6, 1, 3, 95, 4, 1, 3)).setObjects(("MPLS-TE-MIB", "mplsTunnelSetupPrio"), ("MPLS-TE-MIB", "mplsTunnelHoldingPrio"), ("MPLS-TE-MIB", "mplsTunnelSignallingProto"), ("MPLS-TE-MIB", "mplsTunnelLocalProtectInUse"), ("MPLS-TE-MIB", "mplsTunnelSessionAttributes"), ("MPLS-TE-MIB", "mplsTunnelHopListIndexNext"), ("MPLS-TE-MIB", "mplsTunnelHopAddrType"), ("MPLS-TE-MIB", "mplsTunnelHopIpv4Addr"), ("MPLS-TE-MIB", "mplsTunnelHopIpv4PrefixLen"), ("MPLS-TE-MIB", "mplsTunnelHopIpv6Addr"), ("MPLS-TE-MIB", "mplsTunnelHopIpv6PrefixLen"), ("MPLS-TE-MIB", "mplsTunnelHopAsNumber"), ("MPLS-TE-MIB", "mplsTunnelHopLspId"), ("MPLS-TE-MIB", "mplsTunnelHopType"), ("MPLS-TE-MIB", "mplsTunnelHopRowStatus"), ("MPLS-TE-MIB", "mplsTunnelHopStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsTunnelSignaledGroup = mplsTunnelSignaledGroup.setStatus('current')
mplsTunnelScalarGroup = ObjectGroup((1, 3, 6, 1, 3, 95, 4, 1, 4)).setObjects(("MPLS-TE-MIB", "mplsTunnelConfigured"), ("MPLS-TE-MIB", "mplsTunnelActive"), ("MPLS-TE-MIB", "mplsTunnelTEDistProto"), ("MPLS-TE-MIB", "mplsTunnelMaxHops"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsTunnelScalarGroup = mplsTunnelScalarGroup.setStatus('current')
mplsTunnelIsIntfcGroup = ObjectGroup((1, 3, 6, 1, 3, 95, 4, 1, 5)).setObjects(("MPLS-TE-MIB", "mplsTunnelIsIf"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsTunnelIsIntfcGroup = mplsTunnelIsIntfcGroup.setStatus('current')
mplsTunnelIsNotIntfcGroup = ObjectGroup((1, 3, 6, 1, 3, 95, 4, 1, 6)).setObjects(("MPLS-TE-MIB", "mplsTunnelIsIf"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsTunnelIsNotIntfcGroup = mplsTunnelIsNotIntfcGroup.setStatus('current')
mplsTunnelOptionalGroup = ObjectGroup((1, 3, 6, 1, 3, 95, 4, 1, 7)).setObjects(("MPLS-TE-MIB", "mplsTunnelResourceIndexNext"), ("MPLS-TE-MIB", "mplsTunnelResourceMaxRate"), ("MPLS-TE-MIB", "mplsTunnelResourceMeanRate"), ("MPLS-TE-MIB", "mplsTunnelResourceMaxBurstSize"), ("MPLS-TE-MIB", "mplsTunnelResourceRowStatus"), ("MPLS-TE-MIB", "mplsTunnelResourceStorageType"), ("MPLS-TE-MIB", "mplsTunnelARHopAddrType"), ("MPLS-TE-MIB", "mplsTunnelARHopIpv4Addr"), ("MPLS-TE-MIB", "mplsTunnelARHopIpv4PrefixLen"), ("MPLS-TE-MIB", "mplsTunnelARHopIpv6Addr"), ("MPLS-TE-MIB", "mplsTunnelARHopIpv6PrefixLen"), ("MPLS-TE-MIB", "mplsTunnelARHopAsNumber"), ("MPLS-TE-MIB", "mplsTunnelARHopType"), ("MPLS-TE-MIB", "mplsTunnelCHopAddrType"), ("MPLS-TE-MIB", "mplsTunnelCHopIpv4Addr"), ("MPLS-TE-MIB", "mplsTunnelCHopIpv4PrefixLen"), ("MPLS-TE-MIB", "mplsTunnelCHopIpv6Addr"), ("MPLS-TE-MIB", "mplsTunnelCHopIpv6PrefixLen"), ("MPLS-TE-MIB", "mplsTunnelCHopAsNumber"), ("MPLS-TE-MIB", "mplsTunnelCHopType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsTunnelOptionalGroup = mplsTunnelOptionalGroup.setStatus('current')
mplsTeNotificationGroup = NotificationGroup((1, 3, 6, 1, 3, 95, 4, 1, 8)).setObjects(("MPLS-TE-MIB", "mplsTunnelUp"), ("MPLS-TE-MIB", "mplsTunnelDown"), ("MPLS-TE-MIB", "mplsTunnelRerouted"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsTeNotificationGroup = mplsTeNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("MPLS-TE-MIB", mplsTunnelLocalProtectInUse=mplsTunnelLocalProtectInUse, mplsTunnelCHopTableIndex=mplsTunnelCHopTableIndex, mplsTunnelResourcePointer=mplsTunnelResourcePointer, mplsTunnelStorageType=mplsTunnelStorageType, mplsTunnelHopIpv4Addr=mplsTunnelHopIpv4Addr, mplsTunnelIsIf=mplsTunnelIsIf, mplsTunnelPerfHCBytes=mplsTunnelPerfHCBytes, mplsTeGroups=mplsTeGroups, mplsTunnelHopListIndex=mplsTunnelHopListIndex, mplsTunnelPrimaryTimeUp=mplsTunnelPrimaryTimeUp, mplsTunnelName=mplsTunnelName, mplsTunnelScalarGroup=mplsTunnelScalarGroup, mplsTunnelConfigured=mplsTunnelConfigured, mplsTunnelResourceMaxRate=mplsTunnelResourceMaxRate, MplsLsrId=MplsLsrId, mplsTunnelExcludeAllAffinity=mplsTunnelExcludeAllAffinity, mplsTunnelTable=mplsTunnelTable, mplsTunnelResourceEntry=mplsTunnelResourceEntry, mplsTunnelUp=mplsTunnelUp, MplsTunnelIndex=MplsTunnelIndex, mplsTunnelGroup=mplsTunnelGroup, mplsTunnelCHopType=mplsTunnelCHopType, mplsTunnelHopIpv6PrefixLen=mplsTunnelHopIpv6PrefixLen, mplsTunnelHopType=mplsTunnelHopType, mplsTunnelHopLspId=mplsTunnelHopLspId, PYSNMP_MODULE_ID=mplsTeMIB, mplsTunnelIsNotIntfcGroup=mplsTunnelIsNotIntfcGroup, mplsTunnelInstanceUpTime=mplsTunnelInstanceUpTime, mplsTunnelPathChanges=mplsTunnelPathChanges, mplsTunnelResourceTable=mplsTunnelResourceTable, mplsTunnelActive=mplsTunnelActive, mplsTunnelOptionalGroup=mplsTunnelOptionalGroup, mplsTunnelHopIpv6Addr=mplsTunnelHopIpv6Addr, mplsTeConformance=mplsTeConformance, mplsTunnelAdminStatus=mplsTunnelAdminStatus, mplsTunnelDescr=mplsTunnelDescr, mplsTunnelIndex=mplsTunnelIndex, mplsTunnelDown=mplsTunnelDown, mplsTunnelSignaledGroup=mplsTunnelSignaledGroup, mplsTunnelHopTable=mplsTunnelHopTable, mplsTunnelXCPointer=mplsTunnelXCPointer, MplsPathIndex=MplsPathIndex, mplsTunnelSetupPrio=mplsTunnelSetupPrio, mplsTunnelResourceIndex=mplsTunnelResourceIndex, mplsTunnelLastPathChange=mplsTunnelLastPathChange, mplsTunnelCHopAsNumber=mplsTunnelCHopAsNumber, mplsTunnelPerfBytes=mplsTunnelPerfBytes, mplsTunnelHopStorageType=mplsTunnelHopStorageType, mplsTunnelARHopTable=mplsTunnelARHopTable, mplsTunnelARHopIpv4Addr=mplsTunnelARHopIpv4Addr, mplsTunnelHopListIndexNext=mplsTunnelHopListIndexNext, mplsTunnelCreationTime=mplsTunnelCreationTime, mplsTunnelRerouted=mplsTunnelRerouted, mplsTunnelEgressLSRId=mplsTunnelEgressLSRId, MplsPathIndexOrZero=MplsPathIndexOrZero, mplsTunnelARHopIndex=mplsTunnelARHopIndex, mplsTunnelPerfEntry=mplsTunnelPerfEntry, mplsTeObjects=mplsTeObjects, mplsTeScalars=mplsTeScalars, mplsTunnelPerfPackets=mplsTunnelPerfPackets, mplsTunnelARHopIpv6PrefixLen=mplsTunnelARHopIpv6PrefixLen, mplsTunnelCHopAddrType=mplsTunnelCHopAddrType, MplsTunnelInstanceIndex=MplsTunnelInstanceIndex, mplsTunnelMaxHops=mplsTunnelMaxHops, mplsTunnelHopAddrType=mplsTunnelHopAddrType, mplsPathOptionIndex=mplsPathOptionIndex, mplsTunnelPathInUse=mplsTunnelPathInUse, mplsTunnelInstancePriority=mplsTunnelInstancePriority, mplsTunnelCHopIpv4Addr=mplsTunnelCHopIpv4Addr, mplsTunnelARHopListIndex=mplsTunnelARHopListIndex, mplsTeNotifyPrefix=mplsTeNotifyPrefix, mplsTunnelHopIndex=mplsTunnelHopIndex, mplsTunnelTEDistProto=mplsTunnelTEDistProto, mplsTunnelARHopAsNumber=mplsTunnelARHopAsNumber, mplsTunnelRole=mplsTunnelRole, mplsTunnelHoldingPrio=mplsTunnelHoldingPrio, mplsTunnelPerfHCPackets=mplsTunnelPerfHCPackets, mplsTunnelManualGroup=mplsTunnelManualGroup, mplsTeNotificationGroup=mplsTeNotificationGroup, mplsTunnelARHopTableIndex=mplsTunnelARHopTableIndex, mplsTeModuleCompliance=mplsTeModuleCompliance, mplsTunnelResourceRowStatus=mplsTunnelResourceRowStatus, mplsTunnelResourceIndexNext=mplsTunnelResourceIndexNext, mplsTunnelHopIpv4PrefixLen=mplsTunnelHopIpv4PrefixLen, mplsTunnelCHopTable=mplsTunnelCHopTable, mplsTunnelRowStatus=mplsTunnelRowStatus, mplsTunnelCHopListIndex=mplsTunnelCHopListIndex, mplsTunnelIsIntfcGroup=mplsTunnelIsIntfcGroup, mplsTunnelHopAsNumber=mplsTunnelHopAsNumber, mplsTunnelARHopEntry=mplsTunnelARHopEntry, mplsTunnelIngressLSRId=mplsTunnelIngressLSRId, mplsTunnelOperStatus=mplsTunnelOperStatus, mplsTunnelResourceStorageType=mplsTunnelResourceStorageType, mplsTunnelPerfTable=mplsTunnelPerfTable, mplsTunnelResourceMaxBurstSize=mplsTunnelResourceMaxBurstSize, mplsTunnelEntry=mplsTunnelEntry, mplsTunnelARHopAddrType=mplsTunnelARHopAddrType, mplsTunnelTrapEnable=mplsTunnelTrapEnable, mplsTeCompliances=mplsTeCompliances, mplsTunnelCHopIndex=mplsTunnelCHopIndex, mplsTunnelARHopIpv4PrefixLen=mplsTunnelARHopIpv4PrefixLen, mplsTunnelSignallingProto=mplsTunnelSignallingProto, mplsTunnelIfIndex=mplsTunnelIfIndex, mplsTunnelHopTableIndex=mplsTunnelHopTableIndex, mplsTunnelIndexNext=mplsTunnelIndexNext, mplsTunnelCHopIpv6PrefixLen=mplsTunnelCHopIpv6PrefixLen, mplsTunnelInstance=mplsTunnelInstance, mplsTunnelARHopIpv6Addr=mplsTunnelARHopIpv6Addr, mplsTunnelIncludeAllAffinity=mplsTunnelIncludeAllAffinity, mplsTunnelPerfErrors=mplsTunnelPerfErrors, mplsTunnelHopRowStatus=mplsTunnelHopRowStatus, mplsTeMIB=mplsTeMIB, mplsTunnelOwner=mplsTunnelOwner, mplsTunnelIncludeAnyAffinity=mplsTunnelIncludeAnyAffinity, mplsTunnelHopEntry=mplsTunnelHopEntry, mplsTunnelARHopType=mplsTunnelARHopType, mplsTunnelCHopIpv6Addr=mplsTunnelCHopIpv6Addr, mplsTunnelResourceMeanRate=mplsTunnelResourceMeanRate, mplsTunnelTotalUpTime=mplsTunnelTotalUpTime, mplsTunnelSessionAttributes=mplsTunnelSessionAttributes, mplsTunnelCHopEntry=mplsTunnelCHopEntry, mplsTunnelPrimaryInstance=mplsTunnelPrimaryInstance, mplsTunnelCHopIpv4PrefixLen=mplsTunnelCHopIpv4PrefixLen, mplsTunnelStateTransitions=mplsTunnelStateTransitions, mplsTeNotifications=mplsTeNotifications)
