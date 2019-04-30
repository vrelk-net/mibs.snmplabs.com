#
# PySNMP MIB module DES-1226G-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DES-1226G-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:23:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Counter32, NotificationType, ObjectIdentity, Bits, TimeTicks, mib_2, ModuleIdentity, Unsigned32, MibIdentifier, Gauge32, IpAddress, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Counter32", "NotificationType", "ObjectIdentity", "Bits", "TimeTicks", "mib-2", "ModuleIdentity", "Unsigned32", "MibIdentifier", "Gauge32", "IpAddress", "Counter64")
DisplayString, PhysAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "PhysAddress", "TextualConvention")
d_link = MibIdentifier((1, 3, 6, 1, 4, 1, 171)).setLabel("d-link")
dlink_products = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10)).setLabel("dlink-products")
dlink_FESmartSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 75)).setLabel("dlink-FESmartSwitch")
des_1226G = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 75, 1)).setLabel("des-1226G")
class OwnerString(DisplayString):
    pass

class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class PortList(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class RowStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6))

companyCommGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 1))
companyMiscGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 3))
companyConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 11))
companyTVlanGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 13))
companyPortTrunkGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 14))
companyQoSGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 15))
companyStaticGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 21))
commSetTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 1, 1), )
if mibBuilder.loadTexts: commSetTable.setStatus('mandatory')
commSetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 1, 1, 1), ).setIndexNames((0, "DES-1226G-MIB", "commSetIndex"))
if mibBuilder.loadTexts: commSetEntry.setStatus('mandatory')
commSetIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: commSetIndex.setStatus('mandatory')
commSetName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commSetName.setStatus('mandatory')
commSetStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 1, 1, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commSetStatus.setStatus('mandatory')
commGetTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 1, 2), )
if mibBuilder.loadTexts: commGetTable.setStatus('mandatory')
commGetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 1, 2, 1), ).setIndexNames((0, "DES-1226G-MIB", "commGetIndex"))
if mibBuilder.loadTexts: commGetEntry.setStatus('mandatory')
commGetIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: commGetIndex.setStatus('mandatory')
commGetName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commGetName.setStatus('mandatory')
commGetStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 1, 2, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commGetStatus.setStatus('mandatory')
commTrapTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 1, 3), )
if mibBuilder.loadTexts: commTrapTable.setStatus('mandatory')
commTrapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 1, 3, 1), ).setIndexNames((0, "DES-1226G-MIB", "commTrapIndex"))
if mibBuilder.loadTexts: commTrapEntry.setStatus('mandatory')
commTrapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: commTrapIndex.setStatus('mandatory')
commTrapName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 1, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commTrapName.setStatus('mandatory')
commTrapIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 1, 3, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commTrapIpAddress.setStatus('mandatory')
commTrapSNMPBootup = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commTrapSNMPBootup.setStatus('mandatory')
commTrapSNMPTPLinkUpDown = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commTrapSNMPTPLinkUpDown.setStatus('mandatory')
commTrapSNMPFiberLinkUpDown = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commTrapSNMPFiberLinkUpDown.setStatus('mandatory')
commTrapStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 1, 3, 1, 13), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commTrapStatus.setStatus('mandatory')
miscReset = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("reset", 1), ("noop", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: miscReset.setStatus('mandatory')
configVerSwPrimary = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 11, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: configVerSwPrimary.setStatus('mandatory')
configVerHwChipSet = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 11, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: configVerHwChipSet.setStatus('mandatory')
configPortTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 11, 6), )
if mibBuilder.loadTexts: configPortTable.setStatus('mandatory')
configPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 11, 6, 1), ).setIndexNames((0, "DES-1226G-MIB", "configPort"))
if mibBuilder.loadTexts: configPortEntry.setStatus('mandatory')
configPort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 11, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: configPort.setStatus('mandatory')
configPortSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 11, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("disable", 1), ("auto", 2), ("rate10M-Half", 3), ("rate10M-Full", 4), ("rate100M-Half", 5), ("rate100M-Full", 6), ("rate1G-Full", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configPortSpeed.setStatus('mandatory')
configPortOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 11, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("down", 1), ("rate10M-Half", 2), ("rate10M-Full", 3), ("rate100M-Half", 4), ("rate100M-Full", 5), ("rate1G-Half", 6), ("rate1G-Full", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: configPortOperStatus.setStatus('mandatory')
configPortFlowControl = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 11, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configPortFlowControl.setStatus('mandatory')
configPortFlowControlOper = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 11, 6, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: configPortFlowControlOper.setStatus('mandatory')
configPortPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 11, 6, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("qlevel0", 0), ("qlevel1", 1), ("qlevel2", 2), ("qlevel3", 3), ("qlevel4", 4), ("qlevel5", 5), ("qlevel6", 6), ("qlevel7", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configPortPriority.setStatus('mandatory')
configMirrorTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 11, 8), )
if mibBuilder.loadTexts: configMirrorTable.setStatus('mandatory')
configMirrorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 11, 8, 1), ).setIndexNames((0, "DES-1226G-MIB", "configMirrorId"))
if mibBuilder.loadTexts: configMirrorEntry.setStatus('mandatory')
configMirrorId = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 11, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: configMirrorId.setStatus('mandatory')
configMirrorMode = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 11, 8, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("disabled", 0), ("rx", 1), ("tx", 2), ("both", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configMirrorMode.setStatus('mandatory')
configMirrorMon = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 11, 8, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configMirrorMon.setStatus('mandatory')
configMirrorSrc = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 11, 8, 1, 4), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configMirrorSrc.setStatus('mandatory')
configMirrorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 11, 8, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configMirrorStatus.setStatus('mandatory')
configSNMPEnable = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 11, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configSNMPEnable.setStatus('mandatory')
configIpAssignmentMode = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 11, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("manual", 1), ("dhcp", 2), ("other", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configIpAssignmentMode.setStatus('mandatory')
configPhysAddress = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 11, 13), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: configPhysAddress.setStatus('mandatory')
configPasswordAdmin = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 11, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: configPasswordAdmin.setStatus('mandatory')
configIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 11, 16), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configIpAddress.setStatus('mandatory')
configNetMask = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 11, 17), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configNetMask.setStatus('mandatory')
configGateway = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 11, 18), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configGateway.setStatus('mandatory')
configSave = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 11, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("save", 1), ("noop", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configSave.setStatus('mandatory')
configRestoreDefaults = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 11, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("restore", 1), ("noop", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configRestoreDefaults.setStatus('mandatory')
tvlanTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 13, 1), )
if mibBuilder.loadTexts: tvlanTable.setStatus('mandatory')
tvlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 13, 1, 1), ).setIndexNames((0, "DES-1226G-MIB", "tvlanId"))
if mibBuilder.loadTexts: tvlanEntry.setStatus('mandatory')
tvlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 13, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tvlanId.setStatus('mandatory')
tvlanMember = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 13, 1, 1, 3), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tvlanMember.setStatus('mandatory')
tvlanUntaggedPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 13, 1, 1, 4), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tvlanUntaggedPorts.setStatus('mandatory')
tvlanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 13, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3, 4, 5, 6))).clone(namedValues=NamedValues(("active", 1), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tvlanStatus.setStatus('mandatory')
tvlanPortTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 13, 2), )
if mibBuilder.loadTexts: tvlanPortTable.setStatus('mandatory')
tvlanPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 13, 2, 1), ).setIndexNames((0, "DES-1226G-MIB", "tvlanPortPortId"))
if mibBuilder.loadTexts: tvlanPortEntry.setStatus('mandatory')
tvlanPortPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 13, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tvlanPortPortId.setStatus('mandatory')
tvlanPortVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 13, 2, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tvlanPortVlanId.setStatus('mandatory')
portTrunkTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 14, 1), )
if mibBuilder.loadTexts: portTrunkTable.setStatus('mandatory')
portTrunkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 14, 1, 1), ).setIndexNames((0, "DES-1226G-MIB", "portTrunkId"), (0, "DES-1226G-MIB", "portTrunkMember"))
if mibBuilder.loadTexts: portTrunkEntry.setStatus('mandatory')
portTrunkId = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 14, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portTrunkId.setStatus('mandatory')
portTrunkMember = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 14, 1, 1, 2), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portTrunkMember.setStatus('mandatory')
portTrunkMemberValue = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 14, 1, 1, 3), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portTrunkMemberValue.setStatus('mandatory')
portTrunkEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 14, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portTrunkEnable.setStatus('mandatory')
qos8021pTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 15, 2), )
if mibBuilder.loadTexts: qos8021pTable.setStatus('mandatory')
qos8021pEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 15, 2, 1), ).setIndexNames((0, "DES-1226G-MIB", "qos8021pPriority"))
if mibBuilder.loadTexts: qos8021pEntry.setStatus('mandatory')
qos8021pPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 15, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qos8021pPriority.setStatus('mandatory')
qos8021pQueueLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 15, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("high", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qos8021pQueueLevel.setStatus('mandatory')
staticOnOff = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 21, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: staticOnOff.setStatus('mandatory')
staticAutoLearning = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 21, 2), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: staticAutoLearning.setStatus('mandatory')
staticTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 21, 3), )
if mibBuilder.loadTexts: staticTable.setStatus('mandatory')
staticEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 21, 3, 1), ).setIndexNames((0, "DES-1226G-MIB", "staticId"))
if mibBuilder.loadTexts: staticEntry.setStatus('mandatory')
staticId = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 21, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: staticId.setStatus('mandatory')
staticMac = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 21, 3, 1, 2), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: staticMac.setStatus('mandatory')
staticPort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 21, 3, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: staticPort.setStatus('mandatory')
staticVID = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 21, 3, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: staticVID.setStatus('mandatory')
staticStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 75, 1, 21, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 4, 6))).clone(namedValues=NamedValues(("active", 1), ("createAndGo", 4), ("destroy", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: staticStatus.setStatus('mandatory')
swFiberInsert = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 75, 1) + (0,1))
swFiberRemove = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 75, 1) + (0,2))
mibBuilder.exportSymbols("DES-1226G-MIB", staticEntry=staticEntry, configIpAddress=configIpAddress, qos8021pPriority=qos8021pPriority, commGetStatus=commGetStatus, commTrapIpAddress=commTrapIpAddress, companyCommGroup=companyCommGroup, tvlanStatus=tvlanStatus, des_1226G=des_1226G, commTrapSNMPBootup=commTrapSNMPBootup, configIpAssignmentMode=configIpAssignmentMode, commTrapStatus=commTrapStatus, tvlanId=tvlanId, staticVID=staticVID, portTrunkTable=portTrunkTable, companyMiscGroup=companyMiscGroup, RowStatus=RowStatus, configMirrorMode=configMirrorMode, configMirrorSrc=configMirrorSrc, configMirrorMon=configMirrorMon, staticMac=staticMac, swFiberRemove=swFiberRemove, d_link=d_link, qos8021pEntry=qos8021pEntry, tvlanTable=tvlanTable, tvlanMember=tvlanMember, qos8021pTable=qos8021pTable, commTrapEntry=commTrapEntry, configPasswordAdmin=configPasswordAdmin, portTrunkId=portTrunkId, qos8021pQueueLevel=qos8021pQueueLevel, companyPortTrunkGroup=companyPortTrunkGroup, portTrunkEnable=portTrunkEnable, commSetEntry=commSetEntry, configSave=configSave, commTrapSNMPFiberLinkUpDown=commTrapSNMPFiberLinkUpDown, commSetStatus=commSetStatus, commTrapIndex=commTrapIndex, commGetEntry=commGetEntry, swFiberInsert=swFiberInsert, configGateway=configGateway, configNetMask=configNetMask, PortList=PortList, commSetIndex=commSetIndex, portTrunkEntry=portTrunkEntry, companyQoSGroup=companyQoSGroup, staticId=staticId, tvlanUntaggedPorts=tvlanUntaggedPorts, tvlanPortTable=tvlanPortTable, companyTVlanGroup=companyTVlanGroup, commTrapName=commTrapName, companyConfigGroup=companyConfigGroup, portTrunkMember=portTrunkMember, commSetTable=commSetTable, commGetName=commGetName, commGetIndex=commGetIndex, configPort=configPort, configPortTable=configPortTable, commGetTable=commGetTable, staticAutoLearning=staticAutoLearning, configSNMPEnable=configSNMPEnable, tvlanEntry=tvlanEntry, configPortPriority=configPortPriority, configPhysAddress=configPhysAddress, tvlanPortEntry=tvlanPortEntry, configPortSpeed=configPortSpeed, companyStaticGroup=companyStaticGroup, configPortFlowControl=configPortFlowControl, configPortOperStatus=configPortOperStatus, miscReset=miscReset, OwnerString=OwnerString, configPortEntry=configPortEntry, commTrapTable=commTrapTable, configVerSwPrimary=configVerSwPrimary, configMirrorId=configMirrorId, configMirrorStatus=configMirrorStatus, dlink_FESmartSwitch=dlink_FESmartSwitch, configVerHwChipSet=configVerHwChipSet, MacAddress=MacAddress, staticTable=staticTable, staticStatus=staticStatus, configMirrorTable=configMirrorTable, configPortFlowControlOper=configPortFlowControlOper, staticPort=staticPort, commTrapSNMPTPLinkUpDown=commTrapSNMPTPLinkUpDown, commSetName=commSetName, tvlanPortVlanId=tvlanPortVlanId, dlink_products=dlink_products, staticOnOff=staticOnOff, configRestoreDefaults=configRestoreDefaults, tvlanPortPortId=tvlanPortPortId, portTrunkMemberValue=portTrunkMemberValue, configMirrorEntry=configMirrorEntry)