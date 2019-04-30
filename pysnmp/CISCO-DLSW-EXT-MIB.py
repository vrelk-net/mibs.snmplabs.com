#
# PySNMP MIB module CISCO-DLSW-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DLSW-EXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:37:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
DlciNumber, = mibBuilder.importSymbols("CISCO-FRAME-RELAY-MIB", "DlciNumber")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SAPType, = mibBuilder.importSymbols("CISCO-TC", "SAPType")
dlswTConnOperState, MacAddressNC, dlswTConnTcpConfigEntry, LFSize, dlswTConnConfigIndex, dlswIfEntry, dlswTConnConfigEntry, dlswCircuitState, TAddress, DlcType, dlswTConnOperEntry, dlswCircuitEntry = mibBuilder.importSymbols("DLSW-MIB", "dlswTConnOperState", "MacAddressNC", "dlswTConnTcpConfigEntry", "LFSize", "dlswTConnConfigIndex", "dlswIfEntry", "dlswTConnConfigEntry", "dlswCircuitState", "TAddress", "DlcType", "dlswTConnOperEntry", "dlswCircuitEntry")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Unsigned32, MibIdentifier, ModuleIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, Counter32, NotificationType, IpAddress, Integer32, TimeTicks, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibIdentifier", "ModuleIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "Counter32", "NotificationType", "IpAddress", "Integer32", "TimeTicks", "Gauge32", "Counter64")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
ciscoDlswExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 74))
ciscoDlswExtMIB.setRevisions(('1997-03-11 00:00',))
if mibBuilder.loadTexts: ciscoDlswExtMIB.setLastUpdated('9703110000Z')
if mibBuilder.loadTexts: ciscoDlswExtMIB.setOrganization('Cisco IBU Engineering Working Group')
ciscoDlswExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 74, 1))
cdeDomains = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 1))
cdeNode = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2))
cdeTConn = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3))
cdeInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 4))
cdeCircuit = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 5))
cdeFast = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 6))
cdeTrapControl = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 7))
class TDomainType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("tcp", 1), ("fst", 2), ("directHdlc", 3), ("directFrameRelay", 4), ("llc2", 5))

class Cost(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 5)

class KeepaliveInterval(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 1200)

class TCPQueueMax(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(25, 2000)

cdeFSTDomain = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 1, 1))
cdeDirectHdlcDomain = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 1, 2))
cdeDirectFrameRelayDomain = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 1, 3))
cdeLlc2Domain = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 1, 4))
cdeNodeTAddr = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 1), TAddress().clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdeNodeTAddr.setStatus('current')
cdeNodeGroup = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdeNodeGroup.setStatus('current')
cdeNodeBorder = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdeNodeBorder.setStatus('current')
cdeNodeCost = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 4), Cost().clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdeNodeCost.setStatus('current')
cdeNodeKeepaliveInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 5), KeepaliveInterval().clone(30)).setUnits('Seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdeNodeKeepaliveInterval.setStatus('current')
cdeNodePassiveConnect = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 6), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdeNodePassiveConnect.setStatus('current')
cdeNodeBiuSegment = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 7), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdeNodeBiuSegment.setStatus('current')
cdeNodeInitPacingWindow = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2000)).clone(20)).setUnits('packets').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdeNodeInitPacingWindow.setStatus('current')
cdeNodeMaxPacingWindow = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2000)).clone(50)).setUnits('packets').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdeNodeMaxPacingWindow.setStatus('current')
cdeNodePromiscuous = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 10), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdeNodePromiscuous.setStatus('current')
cdeNodePromPeerDefaultsCost = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 11), Cost().clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdeNodePromPeerDefaultsCost.setStatus('current')
cdeNodePromPeerDefaultsDestMac = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 12), MacAddressNC().clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdeNodePromPeerDefaultsDestMac.setStatus('current')
cdeNodePromPeerDefaultsKeepaliveInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 13), KeepaliveInterval().clone(30)).setUnits('Seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdeNodePromPeerDefaultsKeepaliveInterval.setStatus('current')
cdeNodePromPeerDefaultsLFSize = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 14), LFSize().clone('lfs17749')).setUnits('bytes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdeNodePromPeerDefaultsLFSize.setStatus('current')
cdeNodePromPeerDefaultsTCPQueueMax = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 15), TCPQueueMax().clone(200)).setUnits('packets').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdeNodePromPeerDefaultsTCPQueueMax.setStatus('current')
cdeNodePeerOnDemandDefaultsCost = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 16), Cost().clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdeNodePeerOnDemandDefaultsCost.setStatus('current')
cdeNodePeerOnDemandDefaultsFst = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 17), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdeNodePeerOnDemandDefaultsFst.setStatus('current')
cdeNodePeerOnDemandDefaultsInactivityInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1440)).clone(10)).setUnits('Minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdeNodePeerOnDemandDefaultsInactivityInterval.setStatus('current')
cdeNodePeerOnDemandDefaultsKeepaliveInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 19), KeepaliveInterval().clone(30)).setUnits('Seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdeNodePeerOnDemandDefaultsKeepaliveInterval.setStatus('current')
cdeNodePeerOnDemandDefaultsLFSize = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 20), LFSize().clone('lfs17749')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdeNodePeerOnDemandDefaultsLFSize.setStatus('current')
cdeNodePeerOnDemandDefaultsPriority = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 21), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdeNodePeerOnDemandDefaultsPriority.setStatus('current')
cdeNodePeerOnDemandDefaultsTCPQueueMax = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 2, 22), TCPQueueMax().clone(200)).setUnits('packets').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdeNodePeerOnDemandDefaultsTCPQueueMax.setStatus('current')
cdeTConnConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1), )
if mibBuilder.loadTexts: cdeTConnConfigTable.setStatus('current')
cdeTConnConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1), )
dlswTConnConfigEntry.registerAugmentions(("CISCO-DLSW-EXT-MIB", "cdeTConnConfigEntry"))
cdeTConnConfigEntry.setIndexNames(*dlswTConnConfigEntry.getIndexNames())
if mibBuilder.loadTexts: cdeTConnConfigEntry.setStatus('current')
cdeTConnConfigTDomainType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1, 1), TDomainType().clone('tcp')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdeTConnConfigTDomainType.setStatus('current')
cdeTConnConfigLocalAck = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1, 2), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdeTConnConfigLocalAck.setStatus('current')
cdeTConnConfigCost = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1, 3), Cost().clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdeTConnConfigCost.setStatus('current')
cdeTConnConfigLFSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1, 4), LFSize().clone('lfs17749')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdeTConnConfigLFSize.setStatus('current')
cdeTConnConfigKeepaliveInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1, 5), KeepaliveInterval().clone(30)).setUnits('Seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdeTConnConfigKeepaliveInterval.setStatus('current')
cdeTConnConfigBackup = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1, 6), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdeTConnConfigBackup.setStatus('current')
cdeTConnConfigBackupTAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1, 7), TAddress().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdeTConnConfigBackupTAddr.setStatus('current')
cdeTConnConfigBackupLinger = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1, 8), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdeTConnConfigBackupLinger.setStatus('current')
cdeTConnConfigBackupLingerInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1440))).setUnits('Minutes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdeTConnConfigBackupLingerInterval.setStatus('current')
cdeTConnConfigPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1, 10), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdeTConnConfigPriority.setStatus('current')
cdeTConnConfigDestMac = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1, 11), MacAddressNC().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdeTConnConfigDestMac.setStatus('current')
cdeTConnConfigDynamic = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1, 12), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdeTConnConfigDynamic.setStatus('current')
cdeTConnConfigDynamicNoLlc = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 300)).clone(5)).setUnits('Minutes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdeTConnConfigDynamicNoLlc.setStatus('current')
cdeTConnConfigDynamicInactivityInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 300))).setUnits('Minutes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdeTConnConfigDynamicInactivityInterval.setStatus('current')
cdeTConnOperTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 2), )
if mibBuilder.loadTexts: cdeTConnOperTable.setStatus('current')
cdeTConnOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 2, 1), )
dlswTConnOperEntry.registerAugmentions(("CISCO-DLSW-EXT-MIB", "cdeTConnOperEntry"))
cdeTConnOperEntry.setIndexNames(*dlswTConnOperEntry.getIndexNames())
if mibBuilder.loadTexts: cdeTConnOperEntry.setStatus('current')
cdeTConnOperPartnerCost = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 2, 1, 1), Cost().clone(3)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdeTConnOperPartnerCost.setStatus('current')
cdeTConnOperPartnerPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 2, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdeTConnOperPartnerPriority.setStatus('current')
cdeTConnOperPartnerBorderPeer = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdeTConnOperPartnerBorderPeer.setStatus('current')
cdeTConnOperPartnerGroupNum = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdeTConnOperPartnerGroupNum.setStatus('current')
cdeTConnOperTDomainType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 2, 1, 5), TDomainType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdeTConnOperTDomainType.setStatus('current')
cdeTConnSpecific = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 3))
cdeTConnTcp = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 3, 1))
cdeTConnDirect = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 3, 2))
cdeTConnTcpConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 3, 1, 1), )
if mibBuilder.loadTexts: cdeTConnTcpConfigTable.setStatus('current')
cdeTConnTcpConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 3, 1, 1, 1), )
dlswTConnTcpConfigEntry.registerAugmentions(("CISCO-DLSW-EXT-MIB", "cdeTConnTcpConfigEntry"))
cdeTConnTcpConfigEntry.setIndexNames(*dlswTConnTcpConfigEntry.getIndexNames())
if mibBuilder.loadTexts: cdeTConnTcpConfigEntry.setStatus('current')
cdeTConnTcpConfigQueueMax = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 3, 1, 1, 1, 1), TCPQueueMax().clone(200)).setUnits('packets').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdeTConnTcpConfigQueueMax.setStatus('current')
cdeTConnDirectConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 3, 2, 1), )
if mibBuilder.loadTexts: cdeTConnDirectConfigTable.setStatus('current')
cdeTConnDirectConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 3, 2, 1, 1), ).setIndexNames((0, "DLSW-MIB", "dlswTConnConfigIndex"))
if mibBuilder.loadTexts: cdeTConnDirectConfigEntry.setStatus('current')
cdeTConnDirectConfigIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 3, 2, 1, 1, 1), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdeTConnDirectConfigIfIndex.setStatus('current')
cdeTConnDirectConfigMediaEncap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 3, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("directHdlc", 1), ("directFrameRelay", 2), ("llc2", 3))).clone('directHdlc')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdeTConnDirectConfigMediaEncap.setStatus('current')
cdeTConnDirectConfigFrameRelayDlci = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 3, 3, 2, 1, 1, 3), DlciNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdeTConnDirectConfigFrameRelayDlci.setStatus('current')
cdeIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 4, 1), )
if mibBuilder.loadTexts: cdeIfTable.setStatus('current')
cdeIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 4, 1, 1), )
dlswIfEntry.registerAugmentions(("CISCO-DLSW-EXT-MIB", "cdeIfEntry"))
cdeIfEntry.setIndexNames(*dlswIfEntry.getIndexNames())
if mibBuilder.loadTexts: cdeIfEntry.setStatus('current')
cdeIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 4, 1, 1, 1), DlcType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdeIfType.setStatus('current')
cdeCircuitTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 5, 1), )
if mibBuilder.loadTexts: cdeCircuitTable.setStatus('current')
cdeCircuitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 5, 1, 1), )
dlswCircuitEntry.registerAugmentions(("CISCO-DLSW-EXT-MIB", "cdeCircuitEntry"))
cdeCircuitEntry.setIndexNames(*dlswCircuitEntry.getIndexNames())
if mibBuilder.loadTexts: cdeCircuitEntry.setStatus('current')
cdeCircuitS1Name = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 5, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 17))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdeCircuitS1Name.setStatus('current')
cdeCircuitS2Name = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 5, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 17))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdeCircuitS2Name.setStatus('current')
cdeCircuitS1IdBlock = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 5, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdeCircuitS1IdBlock.setStatus('current')
cdeCircuitS1IdNum = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 5, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdeCircuitS1IdNum.setStatus('current')
cdeFastTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 6, 1), )
if mibBuilder.loadTexts: cdeFastTable.setStatus('current')
cdeFastEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 6, 1, 1), ).setIndexNames((0, "CISCO-DLSW-EXT-MIB", "cdeFastS1Mac"), (0, "CISCO-DLSW-EXT-MIB", "cdeFastS1Sap"), (0, "CISCO-DLSW-EXT-MIB", "cdeFastS2Mac"), (0, "CISCO-DLSW-EXT-MIB", "cdeFastS2Sap"))
if mibBuilder.loadTexts: cdeFastEntry.setStatus('current')
cdeFastS1Mac = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 6, 1, 1, 1), MacAddressNC())
if mibBuilder.loadTexts: cdeFastS1Mac.setStatus('current')
cdeFastS1Sap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 6, 1, 1, 2), SAPType())
if mibBuilder.loadTexts: cdeFastS1Sap.setStatus('current')
cdeFastS2Mac = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 6, 1, 1, 3), MacAddressNC())
if mibBuilder.loadTexts: cdeFastS2Mac.setStatus('current')
cdeFastS2Sap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 6, 1, 1, 4), SAPType())
if mibBuilder.loadTexts: cdeFastS2Sap.setStatus('current')
cdeFastS1IfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 6, 1, 1, 5), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdeFastS1IfIndex.setStatus('current')
cdeFastS1RouteInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 6, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdeFastS1RouteInfo.setStatus('current')
cdeFastS1CacheId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 6, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdeFastS1CacheId.setStatus('current')
cdeFastS2TDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 6, 1, 1, 8), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdeFastS2TDomain.setStatus('current')
cdeFastS2TAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 6, 1, 1, 9), TAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdeFastS2TAddress.setStatus('current')
cdeFastS2CacheId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 6, 1, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdeFastS2CacheId.setStatus('current')
cdeFastOrigin = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 6, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("s1", 1), ("s2", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdeFastOrigin.setStatus('current')
cdeFastTimeToLive = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 6, 1, 1, 12), TimeTicks()).setUnits('hundredths of a second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cdeFastTimeToLive.setStatus('current')
cdeTrapCntlTConn = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 7, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdeTrapCntlTConn.setStatus('current')
cdeTrapCntlCircuit = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 74, 1, 7, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdeTrapCntlCircuit.setStatus('current')
cdeTrapsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 74, 2))
cdeTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 74, 2, 0))
cdeTrapTConnUpDown = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 74, 2, 0, 1)).setObjects(("DLSW-MIB", "dlswTConnOperState"))
if mibBuilder.loadTexts: cdeTrapTConnUpDown.setStatus('current')
cdeTrapCircuitUpDown = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 74, 2, 0, 2)).setObjects(("DLSW-MIB", "dlswCircuitState"))
if mibBuilder.loadTexts: cdeTrapCircuitUpDown.setStatus('current')
cdeMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 74, 3))
cdeMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 74, 3, 1))
cdeMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 74, 3, 2))
cdeMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 74, 3, 1, 1)).setObjects(("CISCO-DLSW-EXT-MIB", "cdeMIBNodeGroup"), ("CISCO-DLSW-EXT-MIB", "cdeMIBTConnConfigGroup"), ("CISCO-DLSW-EXT-MIB", "cdeMIBTConnOperGroup"), ("CISCO-DLSW-EXT-MIB", "cdeMIBTConnTcpConfigGroup"), ("CISCO-DLSW-EXT-MIB", "cdeMIBTConnDirectConfigGroup"), ("CISCO-DLSW-EXT-MIB", "cdeMIBInterfaceGroup"), ("CISCO-DLSW-EXT-MIB", "cdeMIBCircuitGroup"), ("CISCO-DLSW-EXT-MIB", "cdeMIBFastGroup"), ("CISCO-DLSW-EXT-MIB", "cdeTrapControlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdeMIBCompliance = cdeMIBCompliance.setStatus('current')
cdeMIBNodeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 74, 3, 2, 1)).setObjects(("CISCO-DLSW-EXT-MIB", "cdeNodeTAddr"), ("CISCO-DLSW-EXT-MIB", "cdeNodeGroup"), ("CISCO-DLSW-EXT-MIB", "cdeNodeBorder"), ("CISCO-DLSW-EXT-MIB", "cdeNodeCost"), ("CISCO-DLSW-EXT-MIB", "cdeNodeKeepaliveInterval"), ("CISCO-DLSW-EXT-MIB", "cdeNodePassiveConnect"), ("CISCO-DLSW-EXT-MIB", "cdeNodeBiuSegment"), ("CISCO-DLSW-EXT-MIB", "cdeNodeInitPacingWindow"), ("CISCO-DLSW-EXT-MIB", "cdeNodeMaxPacingWindow"), ("CISCO-DLSW-EXT-MIB", "cdeNodePromiscuous"), ("CISCO-DLSW-EXT-MIB", "cdeNodePromPeerDefaultsCost"), ("CISCO-DLSW-EXT-MIB", "cdeNodePromPeerDefaultsDestMac"), ("CISCO-DLSW-EXT-MIB", "cdeNodePromPeerDefaultsKeepaliveInterval"), ("CISCO-DLSW-EXT-MIB", "cdeNodePromPeerDefaultsLFSize"), ("CISCO-DLSW-EXT-MIB", "cdeNodePromPeerDefaultsTCPQueueMax"), ("CISCO-DLSW-EXT-MIB", "cdeNodePeerOnDemandDefaultsCost"), ("CISCO-DLSW-EXT-MIB", "cdeNodePeerOnDemandDefaultsFst"), ("CISCO-DLSW-EXT-MIB", "cdeNodePeerOnDemandDefaultsInactivityInterval"), ("CISCO-DLSW-EXT-MIB", "cdeNodePeerOnDemandDefaultsKeepaliveInterval"), ("CISCO-DLSW-EXT-MIB", "cdeNodePeerOnDemandDefaultsLFSize"), ("CISCO-DLSW-EXT-MIB", "cdeNodePeerOnDemandDefaultsPriority"), ("CISCO-DLSW-EXT-MIB", "cdeNodePeerOnDemandDefaultsTCPQueueMax"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdeMIBNodeGroup = cdeMIBNodeGroup.setStatus('current')
cdeMIBTConnConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 74, 3, 2, 2)).setObjects(("CISCO-DLSW-EXT-MIB", "cdeTConnConfigTDomainType"), ("CISCO-DLSW-EXT-MIB", "cdeTConnConfigLocalAck"), ("CISCO-DLSW-EXT-MIB", "cdeTConnConfigCost"), ("CISCO-DLSW-EXT-MIB", "cdeTConnConfigLFSize"), ("CISCO-DLSW-EXT-MIB", "cdeTConnConfigKeepaliveInterval"), ("CISCO-DLSW-EXT-MIB", "cdeTConnConfigBackup"), ("CISCO-DLSW-EXT-MIB", "cdeTConnConfigBackupTAddr"), ("CISCO-DLSW-EXT-MIB", "cdeTConnConfigBackupLinger"), ("CISCO-DLSW-EXT-MIB", "cdeTConnConfigBackupLingerInterval"), ("CISCO-DLSW-EXT-MIB", "cdeTConnConfigPriority"), ("CISCO-DLSW-EXT-MIB", "cdeTConnConfigDestMac"), ("CISCO-DLSW-EXT-MIB", "cdeTConnConfigDynamic"), ("CISCO-DLSW-EXT-MIB", "cdeTConnConfigDynamicNoLlc"), ("CISCO-DLSW-EXT-MIB", "cdeTConnConfigDynamicInactivityInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdeMIBTConnConfigGroup = cdeMIBTConnConfigGroup.setStatus('current')
cdeMIBTConnOperGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 74, 3, 2, 3)).setObjects(("CISCO-DLSW-EXT-MIB", "cdeTConnOperPartnerCost"), ("CISCO-DLSW-EXT-MIB", "cdeTConnOperPartnerPriority"), ("CISCO-DLSW-EXT-MIB", "cdeTConnOperPartnerBorderPeer"), ("CISCO-DLSW-EXT-MIB", "cdeTConnOperPartnerGroupNum"), ("CISCO-DLSW-EXT-MIB", "cdeTConnOperTDomainType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdeMIBTConnOperGroup = cdeMIBTConnOperGroup.setStatus('current')
cdeMIBTConnTcpConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 74, 3, 2, 4)).setObjects(("CISCO-DLSW-EXT-MIB", "cdeTConnTcpConfigQueueMax"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdeMIBTConnTcpConfigGroup = cdeMIBTConnTcpConfigGroup.setStatus('current')
cdeMIBTConnDirectConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 74, 3, 2, 5)).setObjects(("CISCO-DLSW-EXT-MIB", "cdeTConnDirectConfigIfIndex"), ("CISCO-DLSW-EXT-MIB", "cdeTConnDirectConfigMediaEncap"), ("CISCO-DLSW-EXT-MIB", "cdeTConnDirectConfigFrameRelayDlci"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdeMIBTConnDirectConfigGroup = cdeMIBTConnDirectConfigGroup.setStatus('current')
cdeMIBInterfaceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 74, 3, 2, 6)).setObjects(("CISCO-DLSW-EXT-MIB", "cdeIfType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdeMIBInterfaceGroup = cdeMIBInterfaceGroup.setStatus('current')
cdeMIBCircuitGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 74, 3, 2, 7)).setObjects(("CISCO-DLSW-EXT-MIB", "cdeCircuitS1Name"), ("CISCO-DLSW-EXT-MIB", "cdeCircuitS2Name"), ("CISCO-DLSW-EXT-MIB", "cdeCircuitS1IdBlock"), ("CISCO-DLSW-EXT-MIB", "cdeCircuitS1IdNum"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdeMIBCircuitGroup = cdeMIBCircuitGroup.setStatus('current')
cdeMIBFastGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 74, 3, 2, 8)).setObjects(("CISCO-DLSW-EXT-MIB", "cdeFastS1IfIndex"), ("CISCO-DLSW-EXT-MIB", "cdeFastS1RouteInfo"), ("CISCO-DLSW-EXT-MIB", "cdeFastS1CacheId"), ("CISCO-DLSW-EXT-MIB", "cdeFastS2TDomain"), ("CISCO-DLSW-EXT-MIB", "cdeFastS2TAddress"), ("CISCO-DLSW-EXT-MIB", "cdeFastS2CacheId"), ("CISCO-DLSW-EXT-MIB", "cdeFastOrigin"), ("CISCO-DLSW-EXT-MIB", "cdeFastTimeToLive"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdeMIBFastGroup = cdeMIBFastGroup.setStatus('current')
cdeTrapControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 74, 3, 2, 9)).setObjects(("CISCO-DLSW-EXT-MIB", "cdeTrapCntlTConn"), ("CISCO-DLSW-EXT-MIB", "cdeTrapCntlCircuit"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cdeTrapControlGroup = cdeTrapControlGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-DLSW-EXT-MIB", cdeTConn=cdeTConn, TCPQueueMax=TCPQueueMax, cdeNodeBiuSegment=cdeNodeBiuSegment, cdeMIBTConnTcpConfigGroup=cdeMIBTConnTcpConfigGroup, cdeNodePeerOnDemandDefaultsCost=cdeNodePeerOnDemandDefaultsCost, cdeNodeKeepaliveInterval=cdeNodeKeepaliveInterval, cdeTConnConfigEntry=cdeTConnConfigEntry, cdeTraps=cdeTraps, ciscoDlswExtMIBObjects=ciscoDlswExtMIBObjects, cdeFastS2Mac=cdeFastS2Mac, cdeMIBCircuitGroup=cdeMIBCircuitGroup, cdeNodePromPeerDefaultsDestMac=cdeNodePromPeerDefaultsDestMac, cdeDomains=cdeDomains, cdeNodeCost=cdeNodeCost, cdeTrapCntlCircuit=cdeTrapCntlCircuit, cdeFastTable=cdeFastTable, cdeFastS2CacheId=cdeFastS2CacheId, cdeMIBNodeGroup=cdeMIBNodeGroup, cdeTConnDirectConfigFrameRelayDlci=cdeTConnDirectConfigFrameRelayDlci, cdeNodePeerOnDemandDefaultsTCPQueueMax=cdeNodePeerOnDemandDefaultsTCPQueueMax, cdeTConnOperPartnerBorderPeer=cdeTConnOperPartnerBorderPeer, cdeTConnOperTable=cdeTConnOperTable, cdeFastS1RouteInfo=cdeFastS1RouteInfo, cdeNodeTAddr=cdeNodeTAddr, Cost=Cost, cdeTConnConfigCost=cdeTConnConfigCost, cdeTConnOperPartnerGroupNum=cdeTConnOperPartnerGroupNum, cdeTConnOperEntry=cdeTConnOperEntry, cdeCircuitEntry=cdeCircuitEntry, cdeTConnTcp=cdeTConnTcp, cdeFastTimeToLive=cdeFastTimeToLive, cdeTConnConfigBackupLingerInterval=cdeTConnConfigBackupLingerInterval, cdeTConnOperTDomainType=cdeTConnOperTDomainType, cdeTrapCircuitUpDown=cdeTrapCircuitUpDown, cdeIfType=cdeIfType, cdeFastS1IfIndex=cdeFastS1IfIndex, cdeNodePeerOnDemandDefaultsPriority=cdeNodePeerOnDemandDefaultsPriority, cdeTrapCntlTConn=cdeTrapCntlTConn, cdeMIBFastGroup=cdeMIBFastGroup, cdeTConnConfigDestMac=cdeTConnConfigDestMac, ciscoDlswExtMIB=ciscoDlswExtMIB, cdeFastS2Sap=cdeFastS2Sap, cdeNodeMaxPacingWindow=cdeNodeMaxPacingWindow, cdeNodePromiscuous=cdeNodePromiscuous, cdeCircuit=cdeCircuit, cdeTConnConfigLocalAck=cdeTConnConfigLocalAck, cdeTConnConfigKeepaliveInterval=cdeTConnConfigKeepaliveInterval, cdeTrapControlGroup=cdeTrapControlGroup, cdeTConnDirect=cdeTConnDirect, cdeTConnConfigBackupLinger=cdeTConnConfigBackupLinger, cdeFast=cdeFast, PYSNMP_MODULE_ID=ciscoDlswExtMIB, cdeNodeGroup=cdeNodeGroup, KeepaliveInterval=KeepaliveInterval, cdeMIBTConnConfigGroup=cdeMIBTConnConfigGroup, cdeCircuitS1IdNum=cdeCircuitS1IdNum, cdeCircuitS1Name=cdeCircuitS1Name, cdeNode=cdeNode, cdeNodePromPeerDefaultsTCPQueueMax=cdeNodePromPeerDefaultsTCPQueueMax, cdeFastS1CacheId=cdeFastS1CacheId, cdeTrapControl=cdeTrapControl, cdeTConnDirectConfigMediaEncap=cdeTConnDirectConfigMediaEncap, cdeTConnTcpConfigTable=cdeTConnTcpConfigTable, cdeMIBCompliances=cdeMIBCompliances, cdeTConnTcpConfigQueueMax=cdeTConnTcpConfigQueueMax, cdeTConnConfigLFSize=cdeTConnConfigLFSize, cdeNodeInitPacingWindow=cdeNodeInitPacingWindow, cdeTConnConfigTDomainType=cdeTConnConfigTDomainType, cdeIfTable=cdeIfTable, cdeMIBTConnOperGroup=cdeMIBTConnOperGroup, cdeCircuitS1IdBlock=cdeCircuitS1IdBlock, cdeTConnTcpConfigEntry=cdeTConnTcpConfigEntry, cdeMIBCompliance=cdeMIBCompliance, cdeMIBGroups=cdeMIBGroups, cdeFastS2TAddress=cdeFastS2TAddress, cdeTConnConfigDynamic=cdeTConnConfigDynamic, cdeLlc2Domain=cdeLlc2Domain, cdeNodePassiveConnect=cdeNodePassiveConnect, cdeFastS1Mac=cdeFastS1Mac, cdeNodePeerOnDemandDefaultsKeepaliveInterval=cdeNodePeerOnDemandDefaultsKeepaliveInterval, cdeTConnConfigTable=cdeTConnConfigTable, cdeTConnConfigDynamicNoLlc=cdeTConnConfigDynamicNoLlc, cdeTConnConfigBackupTAddr=cdeTConnConfigBackupTAddr, cdeDirectHdlcDomain=cdeDirectHdlcDomain, cdeNodePromPeerDefaultsCost=cdeNodePromPeerDefaultsCost, cdeCircuitTable=cdeCircuitTable, cdeFastS2TDomain=cdeFastS2TDomain, cdeMIBTConnDirectConfigGroup=cdeMIBTConnDirectConfigGroup, cdeMIBInterfaceGroup=cdeMIBInterfaceGroup, cdeTConnSpecific=cdeTConnSpecific, cdeMIBConformance=cdeMIBConformance, cdeTConnConfigPriority=cdeTConnConfigPriority, cdeDirectFrameRelayDomain=cdeDirectFrameRelayDomain, cdeTrapTConnUpDown=cdeTrapTConnUpDown, cdeNodePromPeerDefaultsKeepaliveInterval=cdeNodePromPeerDefaultsKeepaliveInterval, cdeIfEntry=cdeIfEntry, cdeNodePeerOnDemandDefaultsFst=cdeNodePeerOnDemandDefaultsFst, cdeCircuitS2Name=cdeCircuitS2Name, cdeFastOrigin=cdeFastOrigin, cdeTrapsPrefix=cdeTrapsPrefix, cdeNodePeerOnDemandDefaultsLFSize=cdeNodePeerOnDemandDefaultsLFSize, cdeTConnConfigDynamicInactivityInterval=cdeTConnConfigDynamicInactivityInterval, cdeTConnDirectConfigIfIndex=cdeTConnDirectConfigIfIndex, cdeFastS1Sap=cdeFastS1Sap, cdeTConnConfigBackup=cdeTConnConfigBackup, cdeInterface=cdeInterface, cdeTConnOperPartnerPriority=cdeTConnOperPartnerPriority, cdeNodePromPeerDefaultsLFSize=cdeNodePromPeerDefaultsLFSize, cdeNodePeerOnDemandDefaultsInactivityInterval=cdeNodePeerOnDemandDefaultsInactivityInterval, cdeTConnOperPartnerCost=cdeTConnOperPartnerCost, cdeFSTDomain=cdeFSTDomain, cdeTConnDirectConfigTable=cdeTConnDirectConfigTable, TDomainType=TDomainType, cdeFastEntry=cdeFastEntry, cdeTConnDirectConfigEntry=cdeTConnDirectConfigEntry, cdeNodeBorder=cdeNodeBorder)
