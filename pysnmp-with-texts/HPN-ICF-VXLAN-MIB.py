#
# PySNMP MIB module HPN-ICF-VXLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-VXLAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:42:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, ObjectIdentity, Bits, Unsigned32, Counter64, Gauge32, MibIdentifier, TimeTicks, iso, ModuleIdentity, Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "Bits", "Unsigned32", "Counter64", "Gauge32", "MibIdentifier", "TimeTicks", "iso", "ModuleIdentity", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType")
MacAddress, TextualConvention, DisplayString, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString", "RowStatus", "TruthValue")
hpnicfVxlan = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150))
hpnicfVxlan.setRevisions(('2013-11-21 09:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpnicfVxlan.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: hpnicfVxlan.setLastUpdated('201311210900Z')
if mibBuilder.loadTexts: hpnicfVxlan.setOrganization('')
if mibBuilder.loadTexts: hpnicfVxlan.setContactInfo('')
if mibBuilder.loadTexts: hpnicfVxlan.setDescription('The overlay MIB.')
hpnicfVxlanObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1))
hpnicfVxlanScalarGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 1))
hpnicfVxlanLocalMacNotify = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfVxlanLocalMacNotify.setStatus('current')
if mibBuilder.loadTexts: hpnicfVxlanLocalMacNotify.setDescription('Local MAC(Media Access Control) address report capability.')
hpnicfVxlanRemoteMacLearn = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 1, 2), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfVxlanRemoteMacLearn.setStatus('current')
if mibBuilder.loadTexts: hpnicfVxlanRemoteMacLearn.setDescription('Remote MAC address self-learning capability.')
hpnicfVxlanNextVxlanID = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVxlanNextVxlanID.setStatus('current')
if mibBuilder.loadTexts: hpnicfVxlanNextVxlanID.setDescription('Next available VXLAN ID(identifier), in the range of 0x0 to 0xFFFFFF. The invalid value 0xFFFFFFFF indicates that no ID can be set.')
hpnicfVxlanConfigured = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVxlanConfigured.setStatus('current')
if mibBuilder.loadTexts: hpnicfVxlanConfigured.setDescription('Number of currently configured VXLANs.')
hpnicfVxlanTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 2), )
if mibBuilder.loadTexts: hpnicfVxlanTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfVxlanTable.setDescription('A table for VXLAN parameters.')
hpnicfVxlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 2, 1), ).setIndexNames((0, "HPN-ICF-VXLAN-MIB", "hpnicfVxlanID"))
if mibBuilder.loadTexts: hpnicfVxlanEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfVxlanEntry.setDescription('Each entry represents the parameters of a VXLAN.')
hpnicfVxlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hpnicfVxlanID.setStatus('current')
if mibBuilder.loadTexts: hpnicfVxlanID.setDescription('The VXLAN ID.')
hpnicfVxlanAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 2, 1, 2), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVxlanAddrType.setStatus('current')
if mibBuilder.loadTexts: hpnicfVxlanAddrType.setDescription('The type of multicast group address.')
hpnicfVxlanGroupAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 2, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVxlanGroupAddr.setStatus('current')
if mibBuilder.loadTexts: hpnicfVxlanGroupAddr.setDescription('Group destination address.')
hpnicfVxlanSourceAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 2, 1, 4), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVxlanSourceAddr.setStatus('current')
if mibBuilder.loadTexts: hpnicfVxlanSourceAddr.setDescription('Group source address.')
hpnicfVxlanVsiIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 2, 1, 5), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVxlanVsiIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfVxlanVsiIndex.setDescription('VSI index. A unique index for the conceptual row identifying a VSI in the hpnicfVsiTable.')
hpnicfVxlanRemoteMacCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 2, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVxlanRemoteMacCount.setStatus('current')
if mibBuilder.loadTexts: hpnicfVxlanRemoteMacCount.setDescription('Remote MAC address count of this VXLAN.')
hpnicfVxlanRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 2, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVxlanRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfVxlanRowStatus.setDescription('Operation status of this table entry. When a row in this table is in active state, no objects in that row can be modified by the agent except hpnicfVxlanGroupAddr, hpnicfVxlanSourceAddr.')
hpnicfVxlanTunnelTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 3), )
if mibBuilder.loadTexts: hpnicfVxlanTunnelTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfVxlanTunnelTable.setDescription('A table for VXLAN tunnel parameters.')
hpnicfVxlanTunnelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 3, 1), ).setIndexNames((0, "HPN-ICF-VXLAN-MIB", "hpnicfVxlanID"), (0, "HPN-ICF-VXLAN-MIB", "hpnicfVxlanTunnelID"))
if mibBuilder.loadTexts: hpnicfVxlanTunnelEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfVxlanTunnelEntry.setDescription('Each entry represents the parameters of a VXLAN tunnel.')
hpnicfVxlanTunnelID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hpnicfVxlanTunnelID.setStatus('current')
if mibBuilder.loadTexts: hpnicfVxlanTunnelID.setDescription('A unique index for tunnel.')
hpnicfVxlanTunnelRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVxlanTunnelRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfVxlanTunnelRowStatus.setDescription('Operation status of this table entry.')
hpnicfVxlanTunnelOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 3, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVxlanTunnelOctets.setStatus('current')
if mibBuilder.loadTexts: hpnicfVxlanTunnelOctets.setDescription('The number of octets that have been forwarded over the tunnel. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times.')
hpnicfVxlanTunnelPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 3, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVxlanTunnelPackets.setStatus('current')
if mibBuilder.loadTexts: hpnicfVxlanTunnelPackets.setDescription('The number of packets that have been forwarded over the tunnel. Discontinuities in the value of this counter can occur at re-initialization of the management system and at other times.')
hpnicfVxlanTunnelBoundTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 4), )
if mibBuilder.loadTexts: hpnicfVxlanTunnelBoundTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfVxlanTunnelBoundTable.setDescription('A table for the number of VXLANs to which the tunnel is bound.')
hpnicfVxlanTunnelBoundEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 4, 1), ).setIndexNames((0, "HPN-ICF-VXLAN-MIB", "hpnicfVxlanTunnelID"))
if mibBuilder.loadTexts: hpnicfVxlanTunnelBoundEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfVxlanTunnelBoundEntry.setDescription('An entry represents the number of VXLANs to which a tunnel is bound.')
hpnicfVxlanTunnelBoundVxlanNum = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 4, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVxlanTunnelBoundVxlanNum.setStatus('current')
if mibBuilder.loadTexts: hpnicfVxlanTunnelBoundVxlanNum.setDescription('The number of VXLANs to which this tunnel is bound.')
hpnicfVxlanMacTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 5), )
if mibBuilder.loadTexts: hpnicfVxlanMacTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfVxlanMacTable.setDescription('A table for VXLAN remote MAC addresses.')
hpnicfVxlanMacEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 5, 1), ).setIndexNames((0, "HPN-ICF-VXLAN-MIB", "hpnicfVxlanVsiIndex"), (0, "HPN-ICF-VXLAN-MIB", "hpnicfVxlanMacAddr"))
if mibBuilder.loadTexts: hpnicfVxlanMacEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfVxlanMacEntry.setDescription('A VXLAN remote MAC address.')
hpnicfVxlanMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 5, 1, 1), MacAddress())
if mibBuilder.loadTexts: hpnicfVxlanMacAddr.setStatus('current')
if mibBuilder.loadTexts: hpnicfVxlanMacAddr.setDescription('MAC address.')
hpnicfVxlanMacTunnelID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 5, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVxlanMacTunnelID.setStatus('current')
if mibBuilder.loadTexts: hpnicfVxlanMacTunnelID.setDescription('A unique index for tunnel.')
hpnicfVxlanMacType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("selfLearned", 1), ("staticConfigured", 2), ("protocolLearned", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVxlanMacType.setStatus('current')
if mibBuilder.loadTexts: hpnicfVxlanMacType.setDescription('The type of an MAC address.')
hpnicfVxlanStaticMacTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 6), )
if mibBuilder.loadTexts: hpnicfVxlanStaticMacTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfVxlanStaticMacTable.setDescription('A table for VXLAN static remote MAC addresses.')
hpnicfVxlanStaticMacEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 6, 1), ).setIndexNames((0, "HPN-ICF-VXLAN-MIB", "hpnicfVxlanVsiIndex"), (0, "HPN-ICF-VXLAN-MIB", "hpnicfVxlanStaticMacAddr"))
if mibBuilder.loadTexts: hpnicfVxlanStaticMacEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfVxlanStaticMacEntry.setDescription('A VXLAN static MAC address.')
hpnicfVxlanStaticMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 6, 1, 1), MacAddress())
if mibBuilder.loadTexts: hpnicfVxlanStaticMacAddr.setStatus('current')
if mibBuilder.loadTexts: hpnicfVxlanStaticMacAddr.setDescription('Static MAC address.')
hpnicfVxlanStaticMacTunnelID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 6, 1, 2), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVxlanStaticMacTunnelID.setStatus('current')
if mibBuilder.loadTexts: hpnicfVxlanStaticMacTunnelID.setDescription('A unique index for tunnel.')
hpnicfVxlanStaticMacRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 150, 1, 6, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVxlanStaticMacRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfVxlanStaticMacRowStatus.setDescription('Operation status of this table entry. When a row in this table is in active state, no objects in that row can be modified by the agent.')
mibBuilder.exportSymbols("HPN-ICF-VXLAN-MIB", hpnicfVxlanLocalMacNotify=hpnicfVxlanLocalMacNotify, hpnicfVxlanStaticMacAddr=hpnicfVxlanStaticMacAddr, hpnicfVxlanScalarGroup=hpnicfVxlanScalarGroup, hpnicfVxlanTable=hpnicfVxlanTable, hpnicfVxlanMacAddr=hpnicfVxlanMacAddr, PYSNMP_MODULE_ID=hpnicfVxlan, hpnicfVxlanEntry=hpnicfVxlanEntry, hpnicfVxlanRemoteMacCount=hpnicfVxlanRemoteMacCount, hpnicfVxlanMacEntry=hpnicfVxlanMacEntry, hpnicfVxlanNextVxlanID=hpnicfVxlanNextVxlanID, hpnicfVxlanSourceAddr=hpnicfVxlanSourceAddr, hpnicfVxlanMacTable=hpnicfVxlanMacTable, hpnicfVxlanStaticMacTunnelID=hpnicfVxlanStaticMacTunnelID, hpnicfVxlanStaticMacTable=hpnicfVxlanStaticMacTable, hpnicfVxlanConfigured=hpnicfVxlanConfigured, hpnicfVxlanID=hpnicfVxlanID, hpnicfVxlanAddrType=hpnicfVxlanAddrType, hpnicfVxlanRowStatus=hpnicfVxlanRowStatus, hpnicfVxlanTunnelRowStatus=hpnicfVxlanTunnelRowStatus, hpnicfVxlanTunnelTable=hpnicfVxlanTunnelTable, hpnicfVxlan=hpnicfVxlan, hpnicfVxlanTunnelBoundTable=hpnicfVxlanTunnelBoundTable, hpnicfVxlanTunnelOctets=hpnicfVxlanTunnelOctets, hpnicfVxlanTunnelEntry=hpnicfVxlanTunnelEntry, hpnicfVxlanMacType=hpnicfVxlanMacType, hpnicfVxlanTunnelBoundEntry=hpnicfVxlanTunnelBoundEntry, hpnicfVxlanStaticMacEntry=hpnicfVxlanStaticMacEntry, hpnicfVxlanMacTunnelID=hpnicfVxlanMacTunnelID, hpnicfVxlanStaticMacRowStatus=hpnicfVxlanStaticMacRowStatus, hpnicfVxlanObjects=hpnicfVxlanObjects, hpnicfVxlanVsiIndex=hpnicfVxlanVsiIndex, hpnicfVxlanTunnelID=hpnicfVxlanTunnelID, hpnicfVxlanTunnelBoundVxlanNum=hpnicfVxlanTunnelBoundVxlanNum, hpnicfVxlanRemoteMacLearn=hpnicfVxlanRemoteMacLearn, hpnicfVxlanTunnelPackets=hpnicfVxlanTunnelPackets, hpnicfVxlanGroupAddr=hpnicfVxlanGroupAddr)