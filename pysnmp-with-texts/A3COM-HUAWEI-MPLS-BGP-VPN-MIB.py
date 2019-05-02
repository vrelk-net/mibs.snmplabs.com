#
# PySNMP MIB module A3COM-HUAWEI-MPLS-BGP-VPN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-MPLS-BGP-VPN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:06:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
hwMpls, huaweiMgmt = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "hwMpls", "huaweiMgmt")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, TimeTicks, experimental, iso, Bits, MibIdentifier, Integer32, Counter32, NotificationType, Unsigned32, Counter64, ObjectIdentity, IpAddress, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "experimental", "iso", "Bits", "MibIdentifier", "Integer32", "Counter32", "NotificationType", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TimeStamp, DisplayString, StorageType, TextualConvention, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "StorageType", "TextualConvention", "TruthValue", "RowStatus")
hwMplsVpn = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3))
hwMplsVpn.setRevisions(('2001-07-20 12:00', '2001-07-17 12:00', '2001-07-10 12:00', '2001-06-19 12:00', '2001-05-30 12:00', '2000-09-30 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hwMplsVpn.setRevisionsDescriptions(('Re-published as PPVPN working group draft. No changes between this version and last; just name change.', "Removed mplsVpnVrfRouteTargetImport/Export from route target table, and modified indexing to better reflect N <> R distribution policy. Also added new object called mplsVpnVrfRouteTargetType which denotes import/export policy for the specified route target. Added mplsVpnInterfaceConfRowStatus which allows for an interface to be associated with a VPN through SNMP configuration. Added VrfName to index of VrfInterfaceConfEntry which allows interfaces to be associated with the appropriate VRF. Modified description of mplsVpnVrfConfMaxPossibleRoutes and mplsVpnVrfConfMaxRoutes to allow for undetermined value. Removed 'both' enumerated value in mplsVpnVrfBgpNbrRole. Updated example to reflect these changes.", 'Renamed mplsNumVrfSecViolationThreshExceeded to mplsNumVrfSecIllegalLabelThreshExceeded, and removed mplsVpnInterfaceConfIndex from varbind. Changed MplsVpnId TC from SnmpAdminString to OCTET STRING. Added mplsVpnVrfSecIllegalLabelRcvThresh to mplsVpnVrfSecEntry. Changed duplicate mplsVpnVrfRouteTargetImport in mplsVpnVrfRouteTargetEntry INDEX to mplsVpnVrfRouteTargetExport.', 'Fixed several compile errors.', 'Updated most of document and MIB to reflect comments from WG.', 'Initial draft version.',))
if mibBuilder.loadTexts: hwMplsVpn.setLastUpdated('200107201200Z')
if mibBuilder.loadTexts: hwMplsVpn.setOrganization('IETF Layer-3 Virtual Private Networks Working Group.')
if mibBuilder.loadTexts: hwMplsVpn.setContactInfo(' Thomas D. Nadeau tnadeau@cisco.com Luyuan Fang luyuanfang@att.com Stephen Brannon Fabio M. Chiussi fabio@bell-labs.com Joseph Dube jdube@avici.com Martin Tatham martin.tatham@bt.com Harmen Van Der Linde hvdl@att.com Comments and discussion to ppvpn@ietf.org')
if mibBuilder.loadTexts: hwMplsVpn.setDescription('This MIB contains managed object definitions for the Multiprotocol Label Switching (MPLS)/Border Gateway Protocol (BGP) Virtual Private Networks (VPNs) as defined in : Rosen, E., Viswanathan, A., and R. Callon, Multiprotocol Label Switching Architecture, Internet Draft <draft-ietf-mpls-arch-06.txt>, August 1999.')
class MplsVpnId(TextualConvention, OctetString):
    reference = "RFC 2685 [VPN-RFC2685] Fox B., et al, 'Virtual Private Networks Identifier', September 1999."
    description = 'An identifier that is assigned to each MPLS/BGP VPN and is used to uniquely identify it. This is assigned by the system operator or NMS and SHOULD be unique throughout the MPLS domain. If this is the case, then this identifier can then be used at any LSR within a specific MPLS domain to identify this MPLS/BGP VPN. It may also be possible to preserve the uniqueness of this identifier across MPLS domain boundaries, in which case this identifier can then be used to uniquely identify MPLS/BGP VPNs on a more global basis.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 31)

class MplsVpnRouteDistinguisher(TextualConvention, OctetString):
    description = 'Syntax for a route distinguisher and route target.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

mplsVpnObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1))
mplsVpnScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 1))
mplsVpnConf = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2))
mplsVpnRoute = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 3))
mplsVpnConfiguredVrfs = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsVpnConfiguredVrfs.setStatus('current')
if mibBuilder.loadTexts: mplsVpnConfiguredVrfs.setDescription('The number of VRFs which are configured on this node.')
mplsVpnActiveVrfs = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsVpnActiveVrfs.setStatus('current')
if mibBuilder.loadTexts: mplsVpnActiveVrfs.setDescription('The number of VRFs which are active on this node. That is, those whose operStatus = Up (1).')
mplsVpnInterfaceConfTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 1), )
if mibBuilder.loadTexts: mplsVpnInterfaceConfTable.setStatus('current')
if mibBuilder.loadTexts: mplsVpnInterfaceConfTable.setDescription('This table specifies per-interface MPLS capability and associated information.')
mplsVpnInterfaceConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-MPLS-BGP-VPN-MIB", "mplsVpnVrfName"), (0, "A3COM-HUAWEI-MPLS-BGP-VPN-MIB", "mplsVpnInterfaceConfIndex"))
if mibBuilder.loadTexts: mplsVpnInterfaceConfEntry.setStatus('current')
if mibBuilder.loadTexts: mplsVpnInterfaceConfEntry.setDescription('An entry in this table is created by an LSR for every interface capable of supporting MPLS/BGP VPN. Each entry in this table is meant to correspond to an entry in the Interfaces Table.')
mplsVpnInterfaceConfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsVpnInterfaceConfIndex.setReference('RFC 2233 - The Interfaces Group MIB using SMIv2, McCloghrie, K., and F. Kastenholtz, Nov. 1997')
if mibBuilder.loadTexts: mplsVpnInterfaceConfIndex.setStatus('current')
if mibBuilder.loadTexts: mplsVpnInterfaceConfIndex.setDescription('This is a unique index for an entry in the MplsVPNInterfaceConfTable.')
mplsVpnInterfaceLabelEdgeType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("providerEdge", 1), ("customerEdge", 2))).clone('providerEdge')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsVpnInterfaceLabelEdgeType.setStatus('current')
if mibBuilder.loadTexts: mplsVpnInterfaceLabelEdgeType.setDescription('Either the providerEdge(1) (PE) or customerEdge(2) (CE) bit MUST be set.')
mplsVpnInterfaceVpnClassification = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("carrierOfCarrier", 1), ("enterprise", 2), ("interProvider", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsVpnInterfaceVpnClassification.setStatus('current')
if mibBuilder.loadTexts: mplsVpnInterfaceVpnClassification.setDescription("Denotes whether this link participates in a carrier-of-carrier's, enterprise, or inter-provider scenario.")
mplsVpnInterfaceIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 1, 1, 4), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsVpnInterfaceIpAddress.setStatus('current')
if mibBuilder.loadTexts: mplsVpnInterfaceIpAddress.setDescription('The IP address of this interface.')
mplsVpnInterfaceIpAddressMask = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 1, 1, 5), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsVpnInterfaceIpAddressMask.setStatus('current')
if mibBuilder.loadTexts: mplsVpnInterfaceIpAddressMask.setDescription('The IP address mask of this interface.')
mplsVpnInterfaceConfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsVpnInterfaceConfRowStatus.setStatus('current')
if mibBuilder.loadTexts: mplsVpnInterfaceConfRowStatus.setDescription('The row status for this entry. This value is used to create a row in this table, signifying that the specified interface is to be associated with the specified interface. If this operation suceeds, the interface will have been associated, otherwise the agent would not allow the association. If the agent only allows read-only operations on this table, it will create entries in this table as they are created.')
mplsVpnVrfConfTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 2), )
if mibBuilder.loadTexts: mplsVpnVrfConfTable.setStatus('current')
if mibBuilder.loadTexts: mplsVpnVrfConfTable.setDescription('This table specifies per-interface MPLS/BGP VPN VRF Table capability and associated information. Entries in this table define VRF routing instances associated with MPLS/VPN interfaces. Note that multiple interfaces can belong to the same VRF instance. The collection of all VRF instances comprises an actual VPN.')
mplsVpnVrfConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 2, 1), ).setIndexNames((0, "A3COM-HUAWEI-MPLS-BGP-VPN-MIB", "mplsVpnVrfName"))
if mibBuilder.loadTexts: mplsVpnVrfConfEntry.setStatus('current')
if mibBuilder.loadTexts: mplsVpnVrfConfEntry.setDescription('An entry in this table is created by an LSR for every VRF capable of supporting MPLS/BGP VPN. The indexing provides an ordering of VRFs per-VPN interface.')
mplsVpnVrfName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 2, 1, 1), MplsVpnId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsVpnVrfName.setReference('RFC 2685 [VPN-RFC2685] Fox B., et al, `Virtual Private Networks Identifier`, September 1999.')
if mibBuilder.loadTexts: mplsVpnVrfName.setStatus('current')
if mibBuilder.loadTexts: mplsVpnVrfName.setDescription('The human-readable name of this VPN. This MAY be equivalent to the RFC2685 VPN-ID.')
mplsVpnVrfRouteDistinguisher = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 2, 1, 2), MplsVpnRouteDistinguisher()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsVpnVrfRouteDistinguisher.setStatus('current')
if mibBuilder.loadTexts: mplsVpnVrfRouteDistinguisher.setDescription('The route distinguisher for this VRF.')
mplsVpnVrfNetPrefixType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("rip", 2), ("ospf", 3), ("isis", 4), ("bgp", 5), ("static", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsVpnVrfNetPrefixType.setStatus('current')
if mibBuilder.loadTexts: mplsVpnVrfNetPrefixType.setDescription('Denotes the type network prefix in use for the PE-CE connections. ')
mplsVpnVrfNetPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 2, 1, 4), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsVpnVrfNetPrefix.setStatus('current')
if mibBuilder.loadTexts: mplsVpnVrfNetPrefix.setDescription('Denotes the network prefix for the PE-CE connections.')
mplsVpnVrfIpRouteRedistributeConn = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 2, 1, 5), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsVpnVrfIpRouteRedistributeConn.setStatus('current')
if mibBuilder.loadTexts: mplsVpnVrfIpRouteRedistributeConn.setDescription('Denotes the redistribution of directly connected networks into the VRF BGP table.')
mplsVpnVrfIpRouteRedistributeStatic = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 2, 1, 6), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsVpnVrfIpRouteRedistributeStatic.setStatus('current')
if mibBuilder.loadTexts: mplsVpnVrfIpRouteRedistributeStatic.setDescription('Denotes the redistribution of static routes into the VRF BGP table.')
mplsVpnVrfIpRouteRedistributeRip = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 2, 1, 7), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsVpnVrfIpRouteRedistributeRip.setStatus('current')
if mibBuilder.loadTexts: mplsVpnVrfIpRouteRedistributeRip.setDescription('Denotes the redistribution of rip routes into the VRF BGP table.')
mplsVpnVrfConfHighRouteThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 2, 1, 8), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsVpnVrfConfHighRouteThreshold.setStatus('current')
if mibBuilder.loadTexts: mplsVpnVrfConfHighRouteThreshold.setDescription('Denotes high-level water marker for the number of routes which this VRF may hold.')
mplsVpnVrfConfIsWarnOnly = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 2, 1, 9), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsVpnVrfConfIsWarnOnly.setStatus('current')
if mibBuilder.loadTexts: mplsVpnVrfConfIsWarnOnly.setDescription("Denotes the action when the amount of VPN's routes exceed the mplsVpnVrfConfHighRouteThreshold.")
mplsVpnVrfConfMaxRoutes = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 2, 1, 10), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsVpnVrfConfMaxRoutes.setStatus('current')
if mibBuilder.loadTexts: mplsVpnVrfConfMaxRoutes.setDescription('Denotes maximum number of routes which this VRF is configured to hold. This value MUST be less than or equal to mplsVrfMaxPossibleRoutes unless it is set to 0.')
mplsVpnVrfConfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 2, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsVpnVrfConfRowStatus.setStatus('current')
if mibBuilder.loadTexts: mplsVpnVrfConfRowStatus.setDescription('This variable is used to create, modify, and/or delete a row in this table.')
mplsVpnVrfRouteTargetTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 3), )
if mibBuilder.loadTexts: mplsVpnVrfRouteTargetTable.setStatus('current')
if mibBuilder.loadTexts: mplsVpnVrfRouteTargetTable.setDescription('This table specifies per-VRF route target association. Each entry identifies a connectivity policy supported as part of a VPN.')
mplsVpnVrfRouteTargetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 3, 1), ).setIndexNames((0, "A3COM-HUAWEI-MPLS-BGP-VPN-MIB", "mplsVpnVrfName"), (0, "A3COM-HUAWEI-MPLS-BGP-VPN-MIB", "mplsVpnVrfRouteTarget"), (0, "A3COM-HUAWEI-MPLS-BGP-VPN-MIB", "mplsVpnVrfRouteTargetType"))
if mibBuilder.loadTexts: mplsVpnVrfRouteTargetEntry.setStatus('current')
if mibBuilder.loadTexts: mplsVpnVrfRouteTargetEntry.setDescription(' An entry in this table is created by an LSR for each route target configured for a VRF supporting a MPLS/BGP VPN instance. The indexing provides an ordering per-VRF instance.')
mplsVpnVrfRouteTarget = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 3, 1, 1), MplsVpnRouteDistinguisher()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsVpnVrfRouteTarget.setStatus('current')
if mibBuilder.loadTexts: mplsVpnVrfRouteTarget.setDescription('The route target distribution policy.')
mplsVpnVrfRouteTargetType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("import", 1), ("export", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsVpnVrfRouteTargetType.setStatus('current')
if mibBuilder.loadTexts: mplsVpnVrfRouteTargetType.setDescription('The route target export distribution type.')
mplsVpnVrfRouteTargetRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 3, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsVpnVrfRouteTargetRowStatus.setStatus('current')
if mibBuilder.loadTexts: mplsVpnVrfRouteTargetRowStatus.setDescription('Row status for this entry.')
mplsVpnVrfBgpNbrAddrTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 4), )
if mibBuilder.loadTexts: mplsVpnVrfBgpNbrAddrTable.setStatus('current')
if mibBuilder.loadTexts: mplsVpnVrfBgpNbrAddrTable.setDescription('This table specifies per-interface MPLS/BGP neighbor addresses for both PEs and CEs.')
mplsVpnVrfBgpNbrAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 4, 1), ).setIndexNames((0, "A3COM-HUAWEI-MPLS-BGP-VPN-MIB", "mplsVpnVrfName"), (0, "A3COM-HUAWEI-MPLS-BGP-VPN-MIB", "mplsVpnVrfBgpNbrAddr"))
if mibBuilder.loadTexts: mplsVpnVrfBgpNbrAddrEntry.setStatus('current')
if mibBuilder.loadTexts: mplsVpnVrfBgpNbrAddrEntry.setDescription('An entry in this table is created by an LSR for every VRF capable of supporting MPLS/BGP VPN. The indexing provides an ordering of VRFs per-VPN interface.')
mplsVpnVrfBgpNbrAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 4, 1, 1), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsVpnVrfBgpNbrAddr.setStatus('current')
if mibBuilder.loadTexts: mplsVpnVrfBgpNbrAddr.setDescription('Denotes the BGP neighbor address.')
mplsVpnVrfBgpNbrRole = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ce", 1), ("pe", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsVpnVrfBgpNbrRole.setStatus('current')
if mibBuilder.loadTexts: mplsVpnVrfBgpNbrRole.setDescription('Denotes the role played by this BGP neighbor with respect to this VRF.')
mplsVpnVrfBgpNbrType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 4, 1, 3), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsVpnVrfBgpNbrType.setStatus('current')
if mibBuilder.loadTexts: mplsVpnVrfBgpNbrType.setDescription('Denotes the address family of the PE address.')
mplsVpnVrfBgpNbrAsNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 4, 1, 4), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsVpnVrfBgpNbrAsNumber.setStatus('current')
if mibBuilder.loadTexts: mplsVpnVrfBgpNbrAsNumber.setDescription("The Automonous System that the BGP's neighbour in.")
mplsVpnVrfBgpNbrAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mplsVpnVrfBgpNbrSetUp", 1), ("mplsVpnVrfBgpNbrSetDown", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsVpnVrfBgpNbrAdminStatus.setStatus('current')
if mibBuilder.loadTexts: mplsVpnVrfBgpNbrAdminStatus.setDescription('The action set by SNMP client.')
mplsVpnVrfBgpNbrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 2, 4, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsVpnVrfBgpNbrRowStatus.setStatus('current')
if mibBuilder.loadTexts: mplsVpnVrfBgpNbrRowStatus.setDescription('This variable is used to create, modify, and/or delete a row in this table.')
mplsVpnVrfRouteTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 3, 1), )
if mibBuilder.loadTexts: mplsVpnVrfRouteTable.setReference('1. RFC 1213 Section 6.6, The IP Group. 2. RFC 2096 ')
if mibBuilder.loadTexts: mplsVpnVrfRouteTable.setStatus('current')
if mibBuilder.loadTexts: mplsVpnVrfRouteTable.setDescription('This table specifies per-interface MPLS/BGP VPN VRF Table routing information. Entries in this table define VRF routing entries associated with the specified MPLS/VPN interfaces. Note that this table contains both BGP and IGP routes, as both may appear in the same VRF.')
mplsVpnVrfRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 3, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-MPLS-BGP-VPN-MIB", "mplsVpnVrfName"), (0, "A3COM-HUAWEI-MPLS-BGP-VPN-MIB", "mplsVpnVrfRouteDest"), (0, "A3COM-HUAWEI-MPLS-BGP-VPN-MIB", "mplsVpnVrfRouteMask"), (0, "A3COM-HUAWEI-MPLS-BGP-VPN-MIB", "mplsVpnVrfRouteNextHop"))
if mibBuilder.loadTexts: mplsVpnVrfRouteEntry.setStatus('current')
if mibBuilder.loadTexts: mplsVpnVrfRouteEntry.setDescription('An entry in this table is created by an LSR for every route present configured (either dynamically or statically) within the context of a specific VRF capable of supporting MPLS/BGP VPN. The indexing provides an ordering of VRFs per-VPN interface.')
mplsVpnVrfRouteDest = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 3, 1, 1, 1), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsVpnVrfRouteDest.setStatus('current')
if mibBuilder.loadTexts: mplsVpnVrfRouteDest.setDescription('The destination IP address of this route. This object may not take a Multicast (Class D) address value.')
mplsVpnVrfRouteMask = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 3, 1, 1, 2), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsVpnVrfRouteMask.setStatus('current')
if mibBuilder.loadTexts: mplsVpnVrfRouteMask.setDescription('Indicate the mask to be logical-ANDed with the destination address before being compared to the value in the mplsVpnVrfRouteDest field. For those systems that do not support arbitrary subnet masks, an agent constructs the value of the mplsVpnVrfRouteMask by reference to the IP Address Class. Any assignment (implicit or otherwise) of an instance of this object to a value x must be rejected if the bit-wise logical-AND of x with the value of the corresponding instance of the mplsVpnVrfRouteDest object is not equal to mplsVpnVrfRouteDest.')
mplsVpnVrfRouteNextHop = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 3, 1, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsVpnVrfRouteNextHop.setStatus('current')
if mibBuilder.loadTexts: mplsVpnVrfRouteNextHop.setDescription('On remote routes, the address of the next system en route; Otherwise, 0.0.0.0. .')
mplsVpnVrfRouteIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 3, 1, 1, 4), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsVpnVrfRouteIfIndex.setStatus('current')
if mibBuilder.loadTexts: mplsVpnVrfRouteIfIndex.setDescription('The ifIndex value that identifies the local interface through which the next hop of this route should be reached.')
mplsVpnVrfRouteProto = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))).clone(namedValues=NamedValues(("other", 1), ("local", 2), ("netmgmt", 3), ("icmp", 4), ("egp", 5), ("ggp", 6), ("hello", 7), ("rip", 8), ("isIs", 9), ("esIs", 10), ("ciscoIgrp", 11), ("bbnSpfIgp", 12), ("ospf", 13), ("bgp", 14), ("idpr", 15), ("ciscoEigrp", 16)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsVpnVrfRouteProto.setStatus('current')
if mibBuilder.loadTexts: mplsVpnVrfRouteProto.setDescription('The routing mechanism via which this route was learned. Inclusion of values for gateway rout- ing protocols is not intended to imply that hosts should support those protocols.')
mplsVpnVrfRouteRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 12, 3, 1, 3, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mplsVpnVrfRouteRowStatus.setStatus('current')
if mibBuilder.loadTexts: mplsVpnVrfRouteRowStatus.setDescription('Row status for this table. It is used according to row installation and removal conventions.')
mibBuilder.exportSymbols("A3COM-HUAWEI-MPLS-BGP-VPN-MIB", mplsVpnActiveVrfs=mplsVpnActiveVrfs, MplsVpnId=MplsVpnId, mplsVpnInterfaceConfRowStatus=mplsVpnInterfaceConfRowStatus, mplsVpnVrfNetPrefixType=mplsVpnVrfNetPrefixType, mplsVpnVrfBgpNbrRowStatus=mplsVpnVrfBgpNbrRowStatus, mplsVpnVrfRouteIfIndex=mplsVpnVrfRouteIfIndex, hwMplsVpn=hwMplsVpn, MplsVpnRouteDistinguisher=MplsVpnRouteDistinguisher, mplsVpnVrfRouteDistinguisher=mplsVpnVrfRouteDistinguisher, mplsVpnVrfRouteProto=mplsVpnVrfRouteProto, PYSNMP_MODULE_ID=hwMplsVpn, mplsVpnVrfBgpNbrAddr=mplsVpnVrfBgpNbrAddr, mplsVpnVrfRouteNextHop=mplsVpnVrfRouteNextHop, mplsVpnInterfaceVpnClassification=mplsVpnInterfaceVpnClassification, mplsVpnConfiguredVrfs=mplsVpnConfiguredVrfs, mplsVpnVrfBgpNbrAddrEntry=mplsVpnVrfBgpNbrAddrEntry, mplsVpnConf=mplsVpnConf, mplsVpnRoute=mplsVpnRoute, mplsVpnInterfaceIpAddress=mplsVpnInterfaceIpAddress, mplsVpnVrfRouteTarget=mplsVpnVrfRouteTarget, mplsVpnVrfRouteTargetType=mplsVpnVrfRouteTargetType, mplsVpnVrfBgpNbrType=mplsVpnVrfBgpNbrType, mplsVpnVrfRouteDest=mplsVpnVrfRouteDest, mplsVpnVrfName=mplsVpnVrfName, mplsVpnVrfConfTable=mplsVpnVrfConfTable, mplsVpnVrfBgpNbrAsNumber=mplsVpnVrfBgpNbrAsNumber, mplsVpnScalars=mplsVpnScalars, mplsVpnInterfaceLabelEdgeType=mplsVpnInterfaceLabelEdgeType, mplsVpnVrfConfMaxRoutes=mplsVpnVrfConfMaxRoutes, mplsVpnVrfRouteTargetEntry=mplsVpnVrfRouteTargetEntry, mplsVpnVrfNetPrefix=mplsVpnVrfNetPrefix, mplsVpnObjects=mplsVpnObjects, mplsVpnVrfRouteEntry=mplsVpnVrfRouteEntry, mplsVpnVrfBgpNbrAddrTable=mplsVpnVrfBgpNbrAddrTable, mplsVpnVrfConfIsWarnOnly=mplsVpnVrfConfIsWarnOnly, mplsVpnVrfConfHighRouteThreshold=mplsVpnVrfConfHighRouteThreshold, mplsVpnVrfIpRouteRedistributeStatic=mplsVpnVrfIpRouteRedistributeStatic, mplsVpnVrfIpRouteRedistributeConn=mplsVpnVrfIpRouteRedistributeConn, mplsVpnVrfBgpNbrRole=mplsVpnVrfBgpNbrRole, mplsVpnVrfRouteRowStatus=mplsVpnVrfRouteRowStatus, mplsVpnVrfConfRowStatus=mplsVpnVrfConfRowStatus, mplsVpnVrfRouteTargetRowStatus=mplsVpnVrfRouteTargetRowStatus, mplsVpnVrfConfEntry=mplsVpnVrfConfEntry, mplsVpnVrfRouteMask=mplsVpnVrfRouteMask, mplsVpnVrfBgpNbrAdminStatus=mplsVpnVrfBgpNbrAdminStatus, mplsVpnVrfRouteTable=mplsVpnVrfRouteTable, mplsVpnInterfaceConfEntry=mplsVpnInterfaceConfEntry, mplsVpnInterfaceConfTable=mplsVpnInterfaceConfTable, mplsVpnVrfIpRouteRedistributeRip=mplsVpnVrfIpRouteRedistributeRip, mplsVpnVrfRouteTargetTable=mplsVpnVrfRouteTargetTable, mplsVpnInterfaceIpAddressMask=mplsVpnInterfaceIpAddressMask, mplsVpnInterfaceConfIndex=mplsVpnInterfaceConfIndex)