#
# PySNMP MIB module H3C-FCOE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-FCOE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:09:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
fcmInstanceIndex, = mibBuilder.importSymbols("FC-MGMT-MIB", "fcmInstanceIndex")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, ObjectIdentity, Unsigned32, IpAddress, ModuleIdentity, NotificationType, iso, Counter32, Counter64, TimeTicks, Integer32, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "Unsigned32", "IpAddress", "ModuleIdentity", "NotificationType", "iso", "Counter32", "Counter64", "TimeTicks", "Integer32", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TimeStamp, RowStatus, DisplayString, TextualConvention, TruthValue, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "RowStatus", "DisplayString", "TextualConvention", "TruthValue", "MacAddress")
T11FabricIndex, = mibBuilder.importSymbols("T11-TC-MIB", "T11FabricIndex")
h3cFCoE = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 120))
h3cFCoE.setRevisions(('2012-03-28 00:00',))
if mibBuilder.loadTexts: h3cFCoE.setLastUpdated('201203280000Z')
if mibBuilder.loadTexts: h3cFCoE.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
h3cFCoEObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1))
h3cFCoEConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1))
h3cFCoEFIPSnoopingObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 2))
class H3cFCoEVfcBindType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("interfaceIndex", 1), ("macAddress", 2))

h3cFCoECfgTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 1), )
if mibBuilder.loadTexts: h3cFCoECfgTable.setStatus('current')
h3cFCoECfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 1, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"))
if mibBuilder.loadTexts: h3cFCoECfgEntry.setStatus('current')
h3cFCoECfgFcmap = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3).clone(hexValue="0EFC00")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cFCoECfgFcmap.setStatus('current')
h3cFCoECfgDynamicVfcCreation = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cFCoECfgDynamicVfcCreation.setStatus('current')
h3cFCoECfgDefaultFCFPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(128)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cFCoECfgDefaultFCFPriority.setStatus('current')
h3cFCoECfgDATov = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 60)).clone(5)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cFCoECfgDATov.setStatus('current')
h3cFCoECfgAddressingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("fpma", 1), ("spma", 2), ("fpmaAndSpma", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cFCoECfgAddressingMode.setStatus('current')
h3cFCoEVLANTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 2), )
if mibBuilder.loadTexts: h3cFCoEVLANTable.setStatus('current')
h3cFCoEVLANEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 2, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "H3C-FCOE-MIB", "h3cFCoEVLANIndex"), (0, "H3C-FCOE-MIB", "h3cFCoEFabricIndex"))
if mibBuilder.loadTexts: h3cFCoEVLANEntry.setStatus('current')
h3cFCoEVLANIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 2, 1, 1), VlanIndex())
if mibBuilder.loadTexts: h3cFCoEVLANIndex.setStatus('current')
h3cFCoEFabricIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 2, 1, 2), T11FabricIndex())
if mibBuilder.loadTexts: h3cFCoEFabricIndex.setStatus('current')
h3cFCoEVLANOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFCoEVLANOperState.setStatus('current')
h3cFCoEVLANRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cFCoEVLANRowStatus.setStatus('current')
h3cFCoEStaticVfcTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 3), )
if mibBuilder.loadTexts: h3cFCoEStaticVfcTable.setStatus('current')
h3cFCoEStaticVfcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 3, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "H3C-FCOE-MIB", "h3cFCoEStaticVfcIndex"))
if mibBuilder.loadTexts: h3cFCoEStaticVfcEntry.setStatus('current')
h3cFCoEStaticVfcIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: h3cFCoEStaticVfcIndex.setStatus('current')
h3cFCoEStaticVfcFCFPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(128)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cFCoEStaticVfcFCFPriority.setStatus('current')
h3cFCoEStaticVfcBindType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 3, 1, 3), H3cFCoEVfcBindType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cFCoEStaticVfcBindType.setStatus('current')
h3cFCoEStaticVfcBindIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 3, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cFCoEStaticVfcBindIfIndex.setStatus('current')
h3cFCoEStaticVfcBindMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 3, 1, 5), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cFCoEStaticVfcBindMACAddress.setStatus('current')
h3cFCoEStaticVfcIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 3, 1, 6), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFCoEStaticVfcIfIndex.setStatus('current')
h3cFCoEStaticVfcCreationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 3, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFCoEStaticVfcCreationTime.setStatus('current')
h3cFCoEStaticVfcFailureCause = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 3, 1, 8), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cFCoEStaticVfcFailureCause.setStatus('current')
h3cFCoEStaticVfcRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 3, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cFCoEStaticVfcRowStatus.setStatus('current')
mibBuilder.exportSymbols("H3C-FCOE-MIB", h3cFCoEStaticVfcRowStatus=h3cFCoEStaticVfcRowStatus, h3cFCoEFabricIndex=h3cFCoEFabricIndex, h3cFCoEStaticVfcIfIndex=h3cFCoEStaticVfcIfIndex, h3cFCoECfgEntry=h3cFCoECfgEntry, h3cFCoECfgFcmap=h3cFCoECfgFcmap, h3cFCoECfgDynamicVfcCreation=h3cFCoECfgDynamicVfcCreation, h3cFCoEStaticVfcCreationTime=h3cFCoEStaticVfcCreationTime, h3cFCoEStaticVfcFailureCause=h3cFCoEStaticVfcFailureCause, h3cFCoEVLANRowStatus=h3cFCoEVLANRowStatus, h3cFCoEVLANTable=h3cFCoEVLANTable, h3cFCoECfgDefaultFCFPriority=h3cFCoECfgDefaultFCFPriority, h3cFCoEStaticVfcEntry=h3cFCoEStaticVfcEntry, h3cFCoECfgDATov=h3cFCoECfgDATov, h3cFCoEConfig=h3cFCoEConfig, h3cFCoEStaticVfcFCFPriority=h3cFCoEStaticVfcFCFPriority, h3cFCoEVLANOperState=h3cFCoEVLANOperState, PYSNMP_MODULE_ID=h3cFCoE, h3cFCoEStaticVfcIndex=h3cFCoEStaticVfcIndex, h3cFCoECfgAddressingMode=h3cFCoECfgAddressingMode, h3cFCoEVLANEntry=h3cFCoEVLANEntry, h3cFCoECfgTable=h3cFCoECfgTable, h3cFCoEObjects=h3cFCoEObjects, h3cFCoEStaticVfcBindIfIndex=h3cFCoEStaticVfcBindIfIndex, h3cFCoEVLANIndex=h3cFCoEVLANIndex, H3cFCoEVfcBindType=H3cFCoEVfcBindType, h3cFCoEFIPSnoopingObjects=h3cFCoEFIPSnoopingObjects, h3cFCoEStaticVfcBindMACAddress=h3cFCoEStaticVfcBindMACAddress, h3cFCoEStaticVfcTable=h3cFCoEStaticVfcTable, h3cFCoE=h3cFCoE, h3cFCoEStaticVfcBindType=h3cFCoEStaticVfcBindType)
