#
# PySNMP MIB module ZXR10-SWITCHQOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZXR10-SWITCHQOS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:42:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, NotificationType, iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Unsigned32, MibIdentifier, enterprises, Counter64, Integer32, Counter32, Gauge32, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "NotificationType", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Unsigned32", "MibIdentifier", "enterprises", "Counter64", "Integer32", "Counter32", "Gauge32", "ObjectIdentity", "TimeTicks")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
zte = MibIdentifier((1, 3, 6, 1, 4, 1, 3902))
zxr10 = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3))
zxr10switch = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 102))
zxr10swqos = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3))
class DisplayString(OctetString):
    pass

class TrafficDropPriority(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("low", 0), ("medium", 1), ("high", 2))

class TrafficColorMode(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("blind", 0), ("aware", 1))

class TrafficForward(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("forwardRed", 1))

class TrafficDrop(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("dropYellow", 1))

class TrafficMirrorAction(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("cpu", 1), ("interface", 2))

class RedirectFlag(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("cpu", 1), ("interface", 2), ("next-hop", 3), ("next-hop-ipv6", 4))

class Packettype(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("all", 0), ("red", 1), ("yellow", 2), ("green", 3))

class Statisticstype(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("packet", 0), ("byte", 1))

class GreenOnlyType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("green-only", 1))

class InetAddressIPv6(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2x:2x:2x:2x:2x:2x:2x:2x%4d'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(16, 16), ValueSizeConstraint(20, 20), )
zxr10AclQosPriorityMarkTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 1), )
if mibBuilder.loadTexts: zxr10AclQosPriorityMarkTable.setStatus('current')
zxr10AclQosPriorityMarkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 1, 1), ).setIndexNames((0, "ZXR10-SWITCHQOS-MIB", "zxr10AclQosPriorityMarkAclNo"), (0, "ZXR10-SWITCHQOS-MIB", "zxr10AclQosPriorityMarkRuleId"))
if mibBuilder.loadTexts: zxr10AclQosPriorityMarkEntry.setStatus('current')
zxr10AclQosPriorityMarkAclNo = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10AclQosPriorityMarkAclNo.setStatus('current')
zxr10AclQosPriorityMarkRuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10AclQosPriorityMarkRuleId.setStatus('current')
zxr10AclQosPriorityMarkAclName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10AclQosPriorityMarkAclName.setStatus('current')
zxr10AclQosPriorityMarkDscpValue = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 1, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosPriorityMarkDscpValue.setStatus('current')
zxr10AclQosPriorityMarkCosValue = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 1, 1, 5), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosPriorityMarkCosValue.setStatus('current')
zxr10AclQosPriorityMarkLocalPrecedence = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 1, 1, 6), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosPriorityMarkLocalPrecedence.setStatus('current')
zxr10AclQosPriorityMarkDropPrecedence = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 1, 1, 7), TrafficDropPriority()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosPriorityMarkDropPrecedence.setStatus('current')
zxr10AclQosPriorityMarkOuterVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 1, 1, 8), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosPriorityMarkOuterVlanId.setStatus('current')
zxr10AclQosPriorityMarkPrecedenceValue = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 1, 1, 9), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosPriorityMarkPrecedenceValue.setStatus('current')
zxr10AclQosPriorityMarkRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 1, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosPriorityMarkRowStatus.setStatus('current')
zxr10AclQosTrafficLimitTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 2), )
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitTable.setStatus('current')
zxr10AclQosTrafficLimitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 2, 1), ).setIndexNames((0, "ZXR10-SWITCHQOS-MIB", "zxr10AclQosTrafficLimitAclNo"), (0, "ZXR10-SWITCHQOS-MIB", "zxr10AclQosTrafficLimitRuleId"))
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitEntry.setStatus('current')
zxr10AclQosTrafficLimitAclNo = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitAclNo.setStatus('current')
zxr10AclQosTrafficLimitRuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitRuleId.setStatus('current')
zxr10AclQosTrafficLimitAclName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitAclName.setStatus('current')
zxr10AclQosTrafficLimitCir = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 2, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitCir.setStatus('current')
zxr10AclQosTrafficLimitCbs = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 2, 1, 5), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitCbs.setStatus('current')
zxr10AclQosTrafficLimitEbs = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 2, 1, 6), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitEbs.setStatus('current')
zxr10AclQosTrafficLimitPir = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 2, 1, 7), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitPir.setStatus('current')
zxr10AclQosTrafficLimitPbs = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 2, 1, 8), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitPbs.setStatus('current')
zxr10AclQosTrafficLimitMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 2, 1, 9), TrafficColorMode()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitMode.setStatus('current')
zxr10AclQosTrafficLimitRedDscpValue = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 2, 1, 10), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitRedDscpValue.setStatus('current')
zxr10AclQosTrafficLimitYelDscpValue = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 2, 1, 11), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitYelDscpValue.setStatus('current')
zxr10AclQosTrafficLimitRedDp = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 2, 1, 12), TrafficDropPriority()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitRedDp.setStatus('current')
zxr10AclQosTrafficLimitYelDp = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 2, 1, 13), TrafficDropPriority()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitYelDp.setStatus('current')
zxr10AclQosTrafficLimitForwadRed = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 2, 1, 14), TrafficForward()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitForwadRed.setStatus('current')
zxr10AclQosTrafficLimitDropYellow = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 2, 1, 15), TrafficDrop()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitDropYellow.setStatus('current')
zxr10AclQosTrafficLimitRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 2, 1, 16), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosTrafficLimitRowStatus.setStatus('current')
zxr10AclQosTrafficMirrorTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 3), )
if mibBuilder.loadTexts: zxr10AclQosTrafficMirrorTable.setStatus('current')
zxr10AclQosTrafficMirrorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 3, 1), ).setIndexNames((0, "ZXR10-SWITCHQOS-MIB", "zxr10AclQosTrafficMirrorAclNo"), (0, "ZXR10-SWITCHQOS-MIB", "zxr10AclQosTrafficMirrorRuleId"))
if mibBuilder.loadTexts: zxr10AclQosTrafficMirrorEntry.setStatus('current')
zxr10AclQosTrafficMirrorAclNo = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10AclQosTrafficMirrorAclNo.setStatus('current')
zxr10AclQosTrafficMirrorRuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10AclQosTrafficMirrorRuleId.setStatus('current')
zxr10AclQosTrafficMirrorAclName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10AclQosTrafficMirrorAclName.setStatus('current')
zxr10AclQosTrafficMirrorAction = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 3, 1, 4), TrafficMirrorAction()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosTrafficMirrorAction.setStatus('current')
zxr10AclQosTrafficMirrorIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 3, 1, 5), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosTrafficMirrorIfName.setStatus('current')
zxr10AclQosTrafficMirrorRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 3, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosTrafficMirrorRowStatus.setStatus('current')
zxr10AclQosRedirectTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4), )
if mibBuilder.loadTexts: zxr10AclQosRedirectTable.setStatus('current')
zxr10AclQosRedirectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1), ).setIndexNames((0, "ZXR10-SWITCHQOS-MIB", "zxr10AclQosRedirectAclNo"), (0, "ZXR10-SWITCHQOS-MIB", "zxr10AclQosRedirectRuleId"))
if mibBuilder.loadTexts: zxr10AclQosRedirectEntry.setStatus('current')
zxr10AclQosRedirectAclNo = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10AclQosRedirectAclNo.setStatus('current')
zxr10AclQosRedirectRuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10AclQosRedirectRuleId.setStatus('current')
zxr10AclQosRedirectAclName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10AclQosRedirectAclName.setStatus('current')
zxr10AclQosRedirectFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 4), RedirectFlag()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosRedirectFlag.setStatus('current')
zxr10AclQosRedirectGPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 5), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosRedirectGPort.setStatus('current')
zxr10AclQosRedirectIpAddr1 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 6), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosRedirectIpAddr1.setStatus('current')
zxr10AclQosRedirectIpPri1 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 7), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosRedirectIpPri1.setStatus('current')
zxr10AclQosRedirectIpAddr2 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 8), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosRedirectIpAddr2.setStatus('current')
zxr10AclQosRedirectIpPri2 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 9), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosRedirectIpPri2.setStatus('current')
zxr10AclQosRedirectIpAddr3 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 10), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosRedirectIpAddr3.setStatus('current')
zxr10AclQosRedirectIpPri3 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 11), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosRedirectIpPri3.setStatus('current')
zxr10AclQosRedirectIpAddr4 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 12), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosRedirectIpAddr4.setStatus('current')
zxr10AclQosRedirectIpPri4 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 13), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosRedirectIpPri4.setStatus('current')
zxr10AclQosRedirectIpAddr5 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 14), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosRedirectIpAddr5.setStatus('current')
zxr10AclQosRedirectIpPri5 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 15), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosRedirectIpPri5.setStatus('current')
zxr10AclQosRedirectIpAddr6 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 16), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosRedirectIpAddr6.setStatus('current')
zxr10AclQosRedirectIpPri6 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 17), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosRedirectIpPri6.setStatus('current')
zxr10AclQosRedirectIpAddr7 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 18), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosRedirectIpAddr7.setStatus('current')
zxr10AclQosRedirectIpPri7 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 19), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosRedirectIpPri7.setStatus('current')
zxr10AclQosRedirectIpAddr8 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 20), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosRedirectIpAddr8.setStatus('current')
zxr10AclQosRedirectIpPri8 = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 21), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosRedirectIpPri8.setStatus('current')
zxr10AclQosRedirectIPv6Addr = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 22), InetAddressIPv6()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosRedirectIPv6Addr.setStatus('current')
zxr10AclQosRedirectGreenOnly = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 23), GreenOnlyType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosRedirectGreenOnly.setStatus('current')
zxr10AclQosRedirectRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 4, 1, 24), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosRedirectRowStatus.setStatus('current')
zxr10AclQosTrafficStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 5), )
if mibBuilder.loadTexts: zxr10AclQosTrafficStatisticsTable.setStatus('current')
zxr10AclQosTrafficStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 5, 1), ).setIndexNames((0, "ZXR10-SWITCHQOS-MIB", "zxr10AclQosTrafficStatisticsAclNo"), (0, "ZXR10-SWITCHQOS-MIB", "zxr10AclQosTrafficStatisticsRuleId"))
if mibBuilder.loadTexts: zxr10AclQosTrafficStatisticsEntry.setStatus('current')
zxr10AclQosTrafficStatisticsAclNo = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10AclQosTrafficStatisticsAclNo.setStatus('current')
zxr10AclQosTrafficStatisticsRuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 5, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10AclQosTrafficStatisticsRuleId.setStatus('current')
zxr10AclQosTrafficStatisticsAclName = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 5, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxr10AclQosTrafficStatisticsAclName.setStatus('current')
zxr10AclQosTrafficStatisticsPkttype = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 5, 1, 4), Packettype()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosTrafficStatisticsPkttype.setStatus('current')
zxr10AclQosTrafficStatisticsStatype = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 5, 1, 5), Statisticstype()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosTrafficStatisticsStatype.setStatus('current')
zxr10AclQosTrafficStatisticsRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 3, 102, 3, 5, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zxr10AclQosTrafficStatisticsRowStatus.setStatus('current')
mibBuilder.exportSymbols("ZXR10-SWITCHQOS-MIB", zxr10AclQosTrafficLimitEbs=zxr10AclQosTrafficLimitEbs, zxr10AclQosPriorityMarkDscpValue=zxr10AclQosPriorityMarkDscpValue, zxr10AclQosRedirectIpPri3=zxr10AclQosRedirectIpPri3, zxr10AclQosTrafficMirrorAction=zxr10AclQosTrafficMirrorAction, zxr10AclQosRedirectIpAddr5=zxr10AclQosRedirectIpAddr5, zxr10AclQosTrafficStatisticsTable=zxr10AclQosTrafficStatisticsTable, zxr10AclQosPriorityMarkLocalPrecedence=zxr10AclQosPriorityMarkLocalPrecedence, zxr10AclQosRedirectIpAddr7=zxr10AclQosRedirectIpAddr7, zxr10AclQosTrafficLimitCir=zxr10AclQosTrafficLimitCir, zxr10AclQosPriorityMarkDropPrecedence=zxr10AclQosPriorityMarkDropPrecedence, zxr10AclQosTrafficLimitAclNo=zxr10AclQosTrafficLimitAclNo, zxr10AclQosRedirectRuleId=zxr10AclQosRedirectRuleId, zxr10AclQosTrafficStatisticsRuleId=zxr10AclQosTrafficStatisticsRuleId, zxr10AclQosRedirectFlag=zxr10AclQosRedirectFlag, GreenOnlyType=GreenOnlyType, zxr10AclQosRedirectIpAddr4=zxr10AclQosRedirectIpAddr4, zxr10AclQosPriorityMarkRowStatus=zxr10AclQosPriorityMarkRowStatus, zxr10AclQosTrafficMirrorRowStatus=zxr10AclQosTrafficMirrorRowStatus, zxr10AclQosPriorityMarkEntry=zxr10AclQosPriorityMarkEntry, TrafficMirrorAction=TrafficMirrorAction, zxr10AclQosTrafficLimitYelDp=zxr10AclQosTrafficLimitYelDp, InetAddressIPv6=InetAddressIPv6, zxr10AclQosTrafficLimitRedDp=zxr10AclQosTrafficLimitRedDp, zxr10AclQosRedirectAclName=zxr10AclQosRedirectAclName, zxr10AclQosRedirectIpPri6=zxr10AclQosRedirectIpPri6, zxr10AclQosRedirectRowStatus=zxr10AclQosRedirectRowStatus, TrafficDrop=TrafficDrop, TrafficForward=TrafficForward, zxr10AclQosRedirectIpAddr6=zxr10AclQosRedirectIpAddr6, TrafficColorMode=TrafficColorMode, zxr10AclQosTrafficLimitEntry=zxr10AclQosTrafficLimitEntry, zxr10AclQosTrafficLimitCbs=zxr10AclQosTrafficLimitCbs, zxr10AclQosTrafficLimitRuleId=zxr10AclQosTrafficLimitRuleId, zxr10AclQosTrafficStatisticsEntry=zxr10AclQosTrafficStatisticsEntry, zxr10AclQosTrafficLimitYelDscpValue=zxr10AclQosTrafficLimitYelDscpValue, zxr10AclQosRedirectIpAddr2=zxr10AclQosRedirectIpAddr2, zxr10AclQosTrafficStatisticsAclName=zxr10AclQosTrafficStatisticsAclName, zxr10AclQosPriorityMarkRuleId=zxr10AclQosPriorityMarkRuleId, zxr10switch=zxr10switch, zxr10AclQosTrafficLimitMode=zxr10AclQosTrafficLimitMode, zxr10swqos=zxr10swqos, zxr10AclQosPriorityMarkAclName=zxr10AclQosPriorityMarkAclName, zxr10AclQosRedirectIPv6Addr=zxr10AclQosRedirectIPv6Addr, zxr10AclQosTrafficLimitTable=zxr10AclQosTrafficLimitTable, zxr10AclQosTrafficLimitPir=zxr10AclQosTrafficLimitPir, zxr10AclQosRedirectIpPri7=zxr10AclQosRedirectIpPri7, zxr10AclQosPriorityMarkCosValue=zxr10AclQosPriorityMarkCosValue, zxr10AclQosRedirectTable=zxr10AclQosRedirectTable, zxr10AclQosTrafficStatisticsStatype=zxr10AclQosTrafficStatisticsStatype, zxr10AclQosRedirectIpPri8=zxr10AclQosRedirectIpPri8, zxr10AclQosTrafficLimitForwadRed=zxr10AclQosTrafficLimitForwadRed, DisplayString=DisplayString, zxr10AclQosTrafficMirrorTable=zxr10AclQosTrafficMirrorTable, zxr10AclQosRedirectIpPri2=zxr10AclQosRedirectIpPri2, zxr10AclQosRedirectAclNo=zxr10AclQosRedirectAclNo, zxr10AclQosTrafficStatisticsAclNo=zxr10AclQosTrafficStatisticsAclNo, zxr10AclQosTrafficMirrorRuleId=zxr10AclQosTrafficMirrorRuleId, zxr10AclQosTrafficStatisticsRowStatus=zxr10AclQosTrafficStatisticsRowStatus, zxr10=zxr10, zte=zte, zxr10AclQosPriorityMarkAclNo=zxr10AclQosPriorityMarkAclNo, zxr10AclQosRedirectIpAddr3=zxr10AclQosRedirectIpAddr3, zxr10AclQosTrafficLimitRedDscpValue=zxr10AclQosTrafficLimitRedDscpValue, zxr10AclQosTrafficLimitAclName=zxr10AclQosTrafficLimitAclName, zxr10AclQosRedirectIpPri1=zxr10AclQosRedirectIpPri1, RedirectFlag=RedirectFlag, zxr10AclQosTrafficMirrorAclNo=zxr10AclQosTrafficMirrorAclNo, zxr10AclQosPriorityMarkTable=zxr10AclQosPriorityMarkTable, zxr10AclQosPriorityMarkPrecedenceValue=zxr10AclQosPriorityMarkPrecedenceValue, Packettype=Packettype, TrafficDropPriority=TrafficDropPriority, zxr10AclQosRedirectIpAddr1=zxr10AclQosRedirectIpAddr1, zxr10AclQosRedirectGreenOnly=zxr10AclQosRedirectGreenOnly, zxr10AclQosRedirectEntry=zxr10AclQosRedirectEntry, zxr10AclQosPriorityMarkOuterVlanId=zxr10AclQosPriorityMarkOuterVlanId, zxr10AclQosTrafficLimitRowStatus=zxr10AclQosTrafficLimitRowStatus, zxr10AclQosTrafficLimitPbs=zxr10AclQosTrafficLimitPbs, zxr10AclQosTrafficMirrorIfName=zxr10AclQosTrafficMirrorIfName, zxr10AclQosTrafficLimitDropYellow=zxr10AclQosTrafficLimitDropYellow, zxr10AclQosRedirectIpPri5=zxr10AclQosRedirectIpPri5, zxr10AclQosTrafficMirrorEntry=zxr10AclQosTrafficMirrorEntry, zxr10AclQosTrafficStatisticsPkttype=zxr10AclQosTrafficStatisticsPkttype, zxr10AclQosRedirectIpAddr8=zxr10AclQosRedirectIpAddr8, zxr10AclQosRedirectGPort=zxr10AclQosRedirectGPort, Statisticstype=Statisticstype, zxr10AclQosRedirectIpPri4=zxr10AclQosRedirectIpPri4, zxr10AclQosTrafficMirrorAclName=zxr10AclQosTrafficMirrorAclName)
