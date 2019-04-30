#
# PySNMP MIB module HH3C-FCOE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-FCOE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:14:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
fcmInstanceIndex, = mibBuilder.importSymbols("FC-MGMT-MIB", "fcmInstanceIndex")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
InterfaceIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Counter32, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, TimeTicks, Unsigned32, iso, Integer32, Gauge32, ModuleIdentity, ObjectIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "TimeTicks", "Unsigned32", "iso", "Integer32", "Gauge32", "ModuleIdentity", "ObjectIdentity", "IpAddress")
TextualConvention, RowStatus, DisplayString, TruthValue, TimeStamp, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString", "TruthValue", "TimeStamp", "MacAddress")
T11FabricIndex, = mibBuilder.importSymbols("T11-TC-MIB", "T11FabricIndex")
hh3cFCoE = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 120))
hh3cFCoE.setRevisions(('2012-03-28 00:00',))
if mibBuilder.loadTexts: hh3cFCoE.setLastUpdated('201203280000Z')
if mibBuilder.loadTexts: hh3cFCoE.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
hh3cFCoEObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 120, 1))
hh3cFCoEConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1))
class Hh3cFCoEVfcBindType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("interfaceIndex", 1), ("macAddress", 2))

hh3cFCoECfgTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 1), )
if mibBuilder.loadTexts: hh3cFCoECfgTable.setStatus('current')
hh3cFCoECfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 1, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"))
if mibBuilder.loadTexts: hh3cFCoECfgEntry.setStatus('current')
hh3cFCoECfgFcmap = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3).clone(hexValue="0EFC00")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cFCoECfgFcmap.setStatus('current')
hh3cFCoECfgDynamicVfcCreation = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cFCoECfgDynamicVfcCreation.setStatus('current')
hh3cFCoECfgDefaultFCFPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(128)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cFCoECfgDefaultFCFPriority.setStatus('current')
hh3cFCoECfgDATov = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 600)).clone(5)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cFCoECfgDATov.setStatus('current')
hh3cFCoECfgAddressingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("fpma", 1), ("spma", 2), ("fpmaAndSpma", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cFCoECfgAddressingMode.setStatus('current')
hh3cFCoEVLANTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 2), )
if mibBuilder.loadTexts: hh3cFCoEVLANTable.setStatus('current')
hh3cFCoEVLANEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 2, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "HH3C-FCOE-MIB", "hh3cFCoEVLANIndex"), (0, "HH3C-FCOE-MIB", "hh3cFCoEFabricIndex"))
if mibBuilder.loadTexts: hh3cFCoEVLANEntry.setStatus('current')
hh3cFCoEVLANIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 2, 1, 1), VlanIndex())
if mibBuilder.loadTexts: hh3cFCoEVLANIndex.setStatus('current')
hh3cFCoEFabricIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 2, 1, 2), T11FabricIndex())
if mibBuilder.loadTexts: hh3cFCoEFabricIndex.setStatus('current')
hh3cFCoEVLANOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFCoEVLANOperState.setStatus('current')
hh3cFCoEVLANRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cFCoEVLANRowStatus.setStatus('current')
hh3cFCoEStaticVfcTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 3), )
if mibBuilder.loadTexts: hh3cFCoEStaticVfcTable.setStatus('current')
hh3cFCoEStaticVfcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 3, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "HH3C-FCOE-MIB", "hh3cFCoEStaticVfcIndex"))
if mibBuilder.loadTexts: hh3cFCoEStaticVfcEntry.setStatus('current')
hh3cFCoEStaticVfcIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: hh3cFCoEStaticVfcIndex.setStatus('current')
hh3cFCoEStaticVfcFCFPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(128)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cFCoEStaticVfcFCFPriority.setStatus('current')
hh3cFCoEStaticVfcBindType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 3, 1, 3), Hh3cFCoEVfcBindType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cFCoEStaticVfcBindType.setStatus('current')
hh3cFCoEStaticVfcBindIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 3, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cFCoEStaticVfcBindIfIndex.setStatus('current')
hh3cFCoEStaticVfcBindMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 3, 1, 5), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cFCoEStaticVfcBindMACAddress.setStatus('current')
hh3cFCoEStaticVfcIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 3, 1, 6), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFCoEStaticVfcIfIndex.setStatus('current')
hh3cFCoEStaticVfcCreationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 3, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFCoEStaticVfcCreationTime.setStatus('current')
hh3cFCoEStaticVfcFailureCause = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 3, 1, 8), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFCoEStaticVfcFailureCause.setStatus('current')
hh3cFCoEStaticVfcRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 3, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cFCoEStaticVfcRowStatus.setStatus('current')
hh3cFCoEFIPSnoopingTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 4), )
if mibBuilder.loadTexts: hh3cFCoEFIPSnoopingTable.setStatus('current')
hh3cFCoEFIPSnoopingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 4, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "HH3C-FCOE-MIB", "hh3cFCoEFIPSnoopingVLANIndex"))
if mibBuilder.loadTexts: hh3cFCoEFIPSnoopingEntry.setStatus('current')
hh3cFCoEFIPSnoopingVLANIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 4, 1, 1), VlanIndex())
if mibBuilder.loadTexts: hh3cFCoEFIPSnoopingVLANIndex.setStatus('current')
hh3cFCoEFIPSnoopingEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 4, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cFCoEFIPSnoopingEnable.setStatus('current')
hh3cFCoEFIPSnoopingFcmap = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 4, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3).clone(hexValue="0EFC00")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cFCoEFIPSnoopingFcmap.setStatus('current')
mibBuilder.exportSymbols("HH3C-FCOE-MIB", hh3cFCoEVLANOperState=hh3cFCoEVLANOperState, hh3cFCoEStaticVfcRowStatus=hh3cFCoEStaticVfcRowStatus, hh3cFCoEStaticVfcIndex=hh3cFCoEStaticVfcIndex, hh3cFCoEVLANRowStatus=hh3cFCoEVLANRowStatus, hh3cFCoEConfig=hh3cFCoEConfig, hh3cFCoEVLANTable=hh3cFCoEVLANTable, hh3cFCoEObjects=hh3cFCoEObjects, hh3cFCoEVLANIndex=hh3cFCoEVLANIndex, hh3cFCoEFIPSnoopingVLANIndex=hh3cFCoEFIPSnoopingVLANIndex, hh3cFCoEStaticVfcBindIfIndex=hh3cFCoEStaticVfcBindIfIndex, Hh3cFCoEVfcBindType=Hh3cFCoEVfcBindType, hh3cFCoECfgFcmap=hh3cFCoECfgFcmap, hh3cFCoEStaticVfcFailureCause=hh3cFCoEStaticVfcFailureCause, hh3cFCoECfgAddressingMode=hh3cFCoECfgAddressingMode, hh3cFCoECfgEntry=hh3cFCoECfgEntry, hh3cFCoEStaticVfcTable=hh3cFCoEStaticVfcTable, hh3cFCoEStaticVfcIfIndex=hh3cFCoEStaticVfcIfIndex, hh3cFCoEVLANEntry=hh3cFCoEVLANEntry, hh3cFCoEStaticVfcBindMACAddress=hh3cFCoEStaticVfcBindMACAddress, PYSNMP_MODULE_ID=hh3cFCoE, hh3cFCoE=hh3cFCoE, hh3cFCoECfgDefaultFCFPriority=hh3cFCoECfgDefaultFCFPriority, hh3cFCoEStaticVfcCreationTime=hh3cFCoEStaticVfcCreationTime, hh3cFCoEFIPSnoopingEntry=hh3cFCoEFIPSnoopingEntry, hh3cFCoEStaticVfcFCFPriority=hh3cFCoEStaticVfcFCFPriority, hh3cFCoEStaticVfcBindType=hh3cFCoEStaticVfcBindType, hh3cFCoEFIPSnoopingEnable=hh3cFCoEFIPSnoopingEnable, hh3cFCoECfgDynamicVfcCreation=hh3cFCoECfgDynamicVfcCreation, hh3cFCoEStaticVfcEntry=hh3cFCoEStaticVfcEntry, hh3cFCoEFIPSnoopingFcmap=hh3cFCoEFIPSnoopingFcmap, hh3cFCoECfgTable=hh3cFCoECfgTable, hh3cFCoECfgDATov=hh3cFCoECfgDATov, hh3cFCoEFIPSnoopingTable=hh3cFCoEFIPSnoopingTable, hh3cFCoEFabricIndex=hh3cFCoEFabricIndex)