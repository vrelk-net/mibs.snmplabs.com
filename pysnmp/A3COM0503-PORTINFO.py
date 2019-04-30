#
# PySNMP MIB module A3COM0503-PORTINFO (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM0503-PORTINFO
# Produced by pysmi-0.3.4 at Mon Apr 29 16:54:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
MacAddress, = mibBuilder.importSymbols("BRIDGE-MIB", "MacAddress")
a3ComVlanGroup, = mibBuilder.importSymbols("GENERIC-3COM-VLAN-MIB-1-0-7", "a3ComVlanGroup")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, NotificationType, IpAddress, Bits, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ObjectIdentity, iso, TimeTicks, Counter32, Unsigned32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "IpAddress", "Bits", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ObjectIdentity", "iso", "TimeTicks", "Counter32", "Unsigned32", "Counter64")
DisplayString, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TruthValue")
class VlanList(OctetString):
    pass

portInfoTable = MibTable((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 3), )
if mibBuilder.loadTexts: portInfoTable.setStatus('current')
portInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: portInfoEntry.setStatus('current')
portInfoEgressVlans = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 3, 1, 1), VlanList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portInfoEgressVlans.setStatus('current')
portInfoForbiddenEgressVlans = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 3, 1, 2), VlanList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portInfoForbiddenEgressVlans.setStatus('current')
portInfoUntaggedVlans = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 3, 1, 3), VlanList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portInfoUntaggedVlans.setStatus('current')
portInfoStpPortPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portInfoStpPortPriority.setStatus('current')
portInfoStpPortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portInfoStpPortEnable.setStatus('current')
portInfoPvid = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 3, 1, 6), VlanIndex().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portInfoPvid.setStatus('current')
portInfoAcceptableFrameTypes = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("admitAll", 1), ("admitOnlyVlanTagged", 2))).clone('admitAll')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portInfoAcceptableFrameTypes.setStatus('current')
portInfoIngressFiltering = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 3, 1, 8), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portInfoIngressFiltering.setStatus('current')
portInfoFdbTable = MibTable((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 4), )
if mibBuilder.loadTexts: portInfoFdbTable.setStatus('mandatory')
portInfoFdbEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 4, 1), ).setIndexNames((0, "A3COM0503-PORTINFO", "portInfoFdbIndex"), (0, "A3COM0503-PORTINFO", "portInfoFdbVlan"), (0, "A3COM0503-PORTINFO", "portInfoFdbAddress"))
if mibBuilder.loadTexts: portInfoFdbEntry.setStatus('mandatory')
portInfoFdbIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: portInfoFdbIndex.setStatus('mandatory')
portInfoFdbVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 4, 1, 2), VlanIndex())
if mibBuilder.loadTexts: portInfoFdbVlan.setStatus('mandatory')
portInfoFdbAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 4, 1, 3), MacAddress())
if mibBuilder.loadTexts: portInfoFdbAddress.setStatus('mandatory')
portInfoFdbStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 4, 1, 4), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portInfoFdbStatus.setStatus('mandatory')
mibBuilder.exportSymbols("A3COM0503-PORTINFO", portInfoFdbAddress=portInfoFdbAddress, portInfoFdbEntry=portInfoFdbEntry, portInfoPvid=portInfoPvid, VlanList=VlanList, portInfoFdbStatus=portInfoFdbStatus, portInfoStpPortEnable=portInfoStpPortEnable, portInfoTable=portInfoTable, portInfoFdbIndex=portInfoFdbIndex, portInfoUntaggedVlans=portInfoUntaggedVlans, portInfoStpPortPriority=portInfoStpPortPriority, portInfoEgressVlans=portInfoEgressVlans, portInfoForbiddenEgressVlans=portInfoForbiddenEgressVlans, portInfoFdbVlan=portInfoFdbVlan, portInfoIngressFiltering=portInfoIngressFiltering, portInfoEntry=portInfoEntry, portInfoAcceptableFrameTypes=portInfoAcceptableFrameTypes, portInfoFdbTable=portInfoFdbTable)
