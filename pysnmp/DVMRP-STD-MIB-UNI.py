#
# PySNMP MIB module DVMRP-STD-MIB-UNI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DVMRP-STD-MIB-UNI
# Produced by pysmi-0.3.4 at Mon Apr 29 18:40:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
InterfaceIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Integer32, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier, Unsigned32, ModuleIdentity, iso, IpAddress, Bits, ObjectIdentity, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier", "Unsigned32", "ModuleIdentity", "iso", "IpAddress", "Bits", "ObjectIdentity", "Gauge32", "Counter32")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
usdDvmrpExperiment, = mibBuilder.importSymbols("Unisphere-Data-Experiment", "usdDvmrpExperiment")
dvmrpStdMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1))
dvmrpStdMIB.setRevisions(('1999-10-19 12:00',))
if mibBuilder.loadTexts: dvmrpStdMIB.setLastUpdated('9910191200Z')
if mibBuilder.loadTexts: dvmrpStdMIB.setOrganization('IETF IDMR Working Group.')
dvmrpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1))
dvmrp = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1))
dvmrpScalar = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 1))
dvmrpVersionString = MibScalar((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpVersionString.setStatus('current')
dvmrpGenerationId = MibScalar((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpGenerationId.setStatus('current')
dvmrpNumRoutes = MibScalar((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNumRoutes.setStatus('current')
dvmrpReachableRoutes = MibScalar((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpReachableRoutes.setStatus('current')
dvmrpInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 2), )
if mibBuilder.loadTexts: dvmrpInterfaceTable.setStatus('current')
dvmrpInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 2, 1), ).setIndexNames((0, "DVMRP-STD-MIB-UNI", "dvmrpInterfaceIfIndex"))
if mibBuilder.loadTexts: dvmrpInterfaceEntry.setStatus('current')
dvmrpInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: dvmrpInterfaceIfIndex.setStatus('current')
dvmrpInterfaceLocalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 2, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dvmrpInterfaceLocalAddress.setStatus('current')
dvmrpInterfaceMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 31)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dvmrpInterfaceMetric.setStatus('current')
dvmrpInterfaceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dvmrpInterfaceStatus.setStatus('current')
dvmrpInterfaceRcvBadPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpInterfaceRcvBadPkts.setStatus('current')
dvmrpInterfaceRcvBadRoutes = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpInterfaceRcvBadRoutes.setStatus('current')
dvmrpInterfaceSentRoutes = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpInterfaceSentRoutes.setStatus('current')
dvmrpInterfaceInterfaceKey = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 2, 1, 8), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dvmrpInterfaceInterfaceKey.setStatus('current')
dvmrpInterfaceInterfaceKeyVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 2, 1, 9), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dvmrpInterfaceInterfaceKeyVersion.setStatus('current')
dvmrpNeighborTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 3), )
if mibBuilder.loadTexts: dvmrpNeighborTable.setStatus('current')
dvmrpNeighborEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 3, 1), ).setIndexNames((0, "DVMRP-STD-MIB-UNI", "dvmrpNeighborIfIndex"), (0, "DVMRP-STD-MIB-UNI", "dvmrpNeighborAddress"))
if mibBuilder.loadTexts: dvmrpNeighborEntry.setStatus('current')
dvmrpNeighborIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: dvmrpNeighborIfIndex.setStatus('current')
dvmrpNeighborAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 3, 1, 2), IpAddress())
if mibBuilder.loadTexts: dvmrpNeighborAddress.setStatus('current')
dvmrpNeighborUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 3, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborUpTime.setStatus('current')
dvmrpNeighborExpiryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 3, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborExpiryTime.setStatus('current')
dvmrpNeighborGenerationId = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborGenerationId.setStatus('current')
dvmrpNeighborMajorVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborMajorVersion.setStatus('current')
dvmrpNeighborMinorVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborMinorVersion.setStatus('current')
dvmrpNeighborCapabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 3, 1, 8), Bits().clone(namedValues=NamedValues(("leaf", 0), ("prune", 1), ("generationID", 2), ("mtrace", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborCapabilities.setStatus('current')
dvmrpNeighborRcvRoutes = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborRcvRoutes.setStatus('current')
dvmrpNeighborRcvBadPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborRcvBadPkts.setStatus('current')
dvmrpNeighborRcvBadRoutes = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborRcvBadRoutes.setStatus('current')
dvmrpNeighborState = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 3, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("oneway", 1), ("active", 2), ("ignoring", 3), ("down", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborState.setStatus('current')
dvmrpRouteTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 4), )
if mibBuilder.loadTexts: dvmrpRouteTable.setStatus('current')
dvmrpRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 4, 1), ).setIndexNames((0, "DVMRP-STD-MIB-UNI", "dvmrpRouteSource"), (0, "DVMRP-STD-MIB-UNI", "dvmrpRouteSourceMask"))
if mibBuilder.loadTexts: dvmrpRouteEntry.setStatus('current')
dvmrpRouteSource = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 4, 1, 1), IpAddress())
if mibBuilder.loadTexts: dvmrpRouteSource.setStatus('current')
dvmrpRouteSourceMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 4, 1, 2), IpAddress())
if mibBuilder.loadTexts: dvmrpRouteSourceMask.setStatus('current')
dvmrpRouteUpstreamNeighbor = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 4, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpRouteUpstreamNeighbor.setStatus('current')
dvmrpRouteIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 4, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpRouteIfIndex.setStatus('current')
dvmrpRouteMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpRouteMetric.setStatus('current')
dvmrpRouteExpiryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 4, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpRouteExpiryTime.setStatus('current')
dvmrpRouteUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 4, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpRouteUpTime.setStatus('current')
dvmrpRouteNextHopTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 5), )
if mibBuilder.loadTexts: dvmrpRouteNextHopTable.setStatus('current')
dvmrpRouteNextHopEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 5, 1), ).setIndexNames((0, "DVMRP-STD-MIB-UNI", "dvmrpRouteNextHopSource"), (0, "DVMRP-STD-MIB-UNI", "dvmrpRouteNextHopSourceMask"), (0, "DVMRP-STD-MIB-UNI", "dvmrpRouteNextHopIfIndex"))
if mibBuilder.loadTexts: dvmrpRouteNextHopEntry.setStatus('current')
dvmrpRouteNextHopSource = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 5, 1, 1), IpAddress())
if mibBuilder.loadTexts: dvmrpRouteNextHopSource.setStatus('current')
dvmrpRouteNextHopSourceMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 5, 1, 2), IpAddress())
if mibBuilder.loadTexts: dvmrpRouteNextHopSourceMask.setStatus('current')
dvmrpRouteNextHopIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 5, 1, 3), InterfaceIndex())
if mibBuilder.loadTexts: dvmrpRouteNextHopIfIndex.setStatus('current')
dvmrpRouteNextHopType = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("leaf", 1), ("branch", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpRouteNextHopType.setStatus('current')
dvmrpPruneTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 6), )
if mibBuilder.loadTexts: dvmrpPruneTable.setStatus('current')
dvmrpPruneEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 6, 1), ).setIndexNames((0, "DVMRP-STD-MIB-UNI", "dvmrpPruneGroup"), (0, "DVMRP-STD-MIB-UNI", "dvmrpPruneSource"), (0, "DVMRP-STD-MIB-UNI", "dvmrpPruneSourceMask"))
if mibBuilder.loadTexts: dvmrpPruneEntry.setStatus('current')
dvmrpPruneGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 6, 1, 1), IpAddress())
if mibBuilder.loadTexts: dvmrpPruneGroup.setStatus('current')
dvmrpPruneSource = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 6, 1, 2), IpAddress())
if mibBuilder.loadTexts: dvmrpPruneSource.setStatus('current')
dvmrpPruneSourceMask = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 6, 1, 3), IpAddress())
if mibBuilder.loadTexts: dvmrpPruneSourceMask.setStatus('current')
dvmrpPruneExpiryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 6, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpPruneExpiryTime.setStatus('current')
dvmrpTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 0))
dvmrpNeighborLoss = NotificationType((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 0, 1)).setObjects(("DVMRP-STD-MIB-UNI", "dvmrpInterfaceLocalAddress"), ("DVMRP-STD-MIB-UNI", "dvmrpNeighborState"))
if mibBuilder.loadTexts: dvmrpNeighborLoss.setStatus('current')
dvmrpNeighborNotPruning = NotificationType((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 1, 1, 0, 2)).setObjects(("DVMRP-STD-MIB-UNI", "dvmrpInterfaceLocalAddress"), ("DVMRP-STD-MIB-UNI", "dvmrpNeighborCapabilities"))
if mibBuilder.loadTexts: dvmrpNeighborNotPruning.setStatus('current')
dvmrpMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 2))
dvmrpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 2, 1))
dvmrpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 2, 2))
dvmrpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 2, 1, 1)).setObjects(("DVMRP-STD-MIB-UNI", "dvmrpGeneralGroup"), ("DVMRP-STD-MIB-UNI", "dvmrpInterfaceGroup"), ("DVMRP-STD-MIB-UNI", "dvmrpNeighborGroup"), ("DVMRP-STD-MIB-UNI", "dvmrpRoutingGroup"), ("DVMRP-STD-MIB-UNI", "dvmrpTreeGroup"), ("DVMRP-STD-MIB-UNI", "dvmrpSecurityGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dvmrpMIBCompliance = dvmrpMIBCompliance.setStatus('current')
dvmrpGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 2, 2, 2)).setObjects(("DVMRP-STD-MIB-UNI", "dvmrpVersionString"), ("DVMRP-STD-MIB-UNI", "dvmrpGenerationId"), ("DVMRP-STD-MIB-UNI", "dvmrpNumRoutes"), ("DVMRP-STD-MIB-UNI", "dvmrpReachableRoutes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dvmrpGeneralGroup = dvmrpGeneralGroup.setStatus('current')
dvmrpInterfaceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 2, 2, 3)).setObjects(("DVMRP-STD-MIB-UNI", "dvmrpInterfaceLocalAddress"), ("DVMRP-STD-MIB-UNI", "dvmrpInterfaceMetric"), ("DVMRP-STD-MIB-UNI", "dvmrpInterfaceStatus"), ("DVMRP-STD-MIB-UNI", "dvmrpInterfaceRcvBadPkts"), ("DVMRP-STD-MIB-UNI", "dvmrpInterfaceRcvBadRoutes"), ("DVMRP-STD-MIB-UNI", "dvmrpInterfaceSentRoutes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dvmrpInterfaceGroup = dvmrpInterfaceGroup.setStatus('current')
dvmrpNeighborGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 2, 2, 4)).setObjects(("DVMRP-STD-MIB-UNI", "dvmrpNeighborUpTime"), ("DVMRP-STD-MIB-UNI", "dvmrpNeighborExpiryTime"), ("DVMRP-STD-MIB-UNI", "dvmrpNeighborGenerationId"), ("DVMRP-STD-MIB-UNI", "dvmrpNeighborMajorVersion"), ("DVMRP-STD-MIB-UNI", "dvmrpNeighborMinorVersion"), ("DVMRP-STD-MIB-UNI", "dvmrpNeighborCapabilities"), ("DVMRP-STD-MIB-UNI", "dvmrpNeighborRcvRoutes"), ("DVMRP-STD-MIB-UNI", "dvmrpNeighborRcvBadPkts"), ("DVMRP-STD-MIB-UNI", "dvmrpNeighborRcvBadRoutes"), ("DVMRP-STD-MIB-UNI", "dvmrpNeighborState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dvmrpNeighborGroup = dvmrpNeighborGroup.setStatus('current')
dvmrpRoutingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 2, 2, 5)).setObjects(("DVMRP-STD-MIB-UNI", "dvmrpRouteUpstreamNeighbor"), ("DVMRP-STD-MIB-UNI", "dvmrpRouteIfIndex"), ("DVMRP-STD-MIB-UNI", "dvmrpRouteMetric"), ("DVMRP-STD-MIB-UNI", "dvmrpRouteExpiryTime"), ("DVMRP-STD-MIB-UNI", "dvmrpRouteUpTime"), ("DVMRP-STD-MIB-UNI", "dvmrpRouteNextHopType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dvmrpRoutingGroup = dvmrpRoutingGroup.setStatus('current')
dvmrpSecurityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 2, 2, 6)).setObjects(("DVMRP-STD-MIB-UNI", "dvmrpInterfaceInterfaceKey"), ("DVMRP-STD-MIB-UNI", "dvmrpInterfaceInterfaceKeyVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dvmrpSecurityGroup = dvmrpSecurityGroup.setStatus('current')
dvmrpTreeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 2, 2, 7)).setObjects(("DVMRP-STD-MIB-UNI", "dvmrpPruneExpiryTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dvmrpTreeGroup = dvmrpTreeGroup.setStatus('current')
dvmrpNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 4874, 3, 2, 1, 1, 2, 2, 8)).setObjects(("DVMRP-STD-MIB-UNI", "dvmrpNeighborLoss"), ("DVMRP-STD-MIB-UNI", "dvmrpNeighborNotPruning"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dvmrpNotificationGroup = dvmrpNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("DVMRP-STD-MIB-UNI", dvmrpInterfaceRcvBadRoutes=dvmrpInterfaceRcvBadRoutes, dvmrpNeighborMinorVersion=dvmrpNeighborMinorVersion, dvmrpNeighborUpTime=dvmrpNeighborUpTime, dvmrpNeighborEntry=dvmrpNeighborEntry, dvmrpReachableRoutes=dvmrpReachableRoutes, dvmrpInterfaceIfIndex=dvmrpInterfaceIfIndex, dvmrpNeighborAddress=dvmrpNeighborAddress, dvmrpPruneGroup=dvmrpPruneGroup, dvmrpPruneExpiryTime=dvmrpPruneExpiryTime, dvmrpMIBCompliances=dvmrpMIBCompliances, dvmrpRouteUpTime=dvmrpRouteUpTime, dvmrpInterfaceInterfaceKey=dvmrpInterfaceInterfaceKey, dvmrp=dvmrp, dvmrpNeighborExpiryTime=dvmrpNeighborExpiryTime, dvmrpNeighborRcvBadRoutes=dvmrpNeighborRcvBadRoutes, dvmrpInterfaceSentRoutes=dvmrpInterfaceSentRoutes, dvmrpRouteSource=dvmrpRouteSource, dvmrpRouteNextHopTable=dvmrpRouteNextHopTable, dvmrpRouteNextHopSourceMask=dvmrpRouteNextHopSourceMask, dvmrpRouteNextHopIfIndex=dvmrpRouteNextHopIfIndex, dvmrpTraps=dvmrpTraps, dvmrpNeighborNotPruning=dvmrpNeighborNotPruning, dvmrpNeighborState=dvmrpNeighborState, dvmrpRouteTable=dvmrpRouteTable, dvmrpNeighborRcvRoutes=dvmrpNeighborRcvRoutes, dvmrpScalar=dvmrpScalar, dvmrpMIBGroups=dvmrpMIBGroups, dvmrpRouteIfIndex=dvmrpRouteIfIndex, dvmrpInterfaceLocalAddress=dvmrpInterfaceLocalAddress, dvmrpNeighborCapabilities=dvmrpNeighborCapabilities, dvmrpRouteNextHopSource=dvmrpRouteNextHopSource, dvmrpRouteNextHopType=dvmrpRouteNextHopType, dvmrpInterfaceRcvBadPkts=dvmrpInterfaceRcvBadPkts, dvmrpRouteSourceMask=dvmrpRouteSourceMask, dvmrpNotificationGroup=dvmrpNotificationGroup, dvmrpInterfaceInterfaceKeyVersion=dvmrpInterfaceInterfaceKeyVersion, dvmrpSecurityGroup=dvmrpSecurityGroup, PYSNMP_MODULE_ID=dvmrpStdMIB, dvmrpRouteEntry=dvmrpRouteEntry, dvmrpNeighborTable=dvmrpNeighborTable, dvmrpRouteUpstreamNeighbor=dvmrpRouteUpstreamNeighbor, dvmrpPruneSource=dvmrpPruneSource, dvmrpGeneralGroup=dvmrpGeneralGroup, dvmrpNeighborRcvBadPkts=dvmrpNeighborRcvBadPkts, dvmrpNeighborLoss=dvmrpNeighborLoss, dvmrpStdMIB=dvmrpStdMIB, dvmrpPruneSourceMask=dvmrpPruneSourceMask, dvmrpRouteExpiryTime=dvmrpRouteExpiryTime, dvmrpNeighborMajorVersion=dvmrpNeighborMajorVersion, dvmrpRouteNextHopEntry=dvmrpRouteNextHopEntry, dvmrpInterfaceMetric=dvmrpInterfaceMetric, dvmrpNeighborGroup=dvmrpNeighborGroup, dvmrpInterfaceEntry=dvmrpInterfaceEntry, dvmrpPruneEntry=dvmrpPruneEntry, dvmrpNeighborIfIndex=dvmrpNeighborIfIndex, dvmrpInterfaceStatus=dvmrpInterfaceStatus, dvmrpPruneTable=dvmrpPruneTable, dvmrpGenerationId=dvmrpGenerationId, dvmrpMIBConformance=dvmrpMIBConformance, dvmrpInterfaceTable=dvmrpInterfaceTable, dvmrpInterfaceGroup=dvmrpInterfaceGroup, dvmrpRouteMetric=dvmrpRouteMetric, dvmrpRoutingGroup=dvmrpRoutingGroup, dvmrpVersionString=dvmrpVersionString, dvmrpMIBCompliance=dvmrpMIBCompliance, dvmrpNeighborGenerationId=dvmrpNeighborGenerationId, dvmrpNumRoutes=dvmrpNumRoutes, dvmrpTreeGroup=dvmrpTreeGroup, dvmrpMIBObjects=dvmrpMIBObjects)
