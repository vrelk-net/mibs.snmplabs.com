#
# PySNMP MIB module HUAWEI-ISOLATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-ISOLATE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:45:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter64, Unsigned32, ObjectIdentity, Bits, iso, ModuleIdentity, IpAddress, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Gauge32, Counter32, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Unsigned32", "ObjectIdentity", "Bits", "iso", "ModuleIdentity", "IpAddress", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Gauge32", "Counter32", "MibIdentifier", "Integer32")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
hwIsolateMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 247))
hwIsolateMIB.setRevisions(('2014-03-12 15:28', '2010-08-11 16:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hwIsolateMIB.setRevisionsDescriptions(('V2.00, modify node.', 'V1.00, initial version.',))
if mibBuilder.loadTexts: hwIsolateMIB.setLastUpdated('201403121528Z')
if mibBuilder.loadTexts: hwIsolateMIB.setOrganization('Huawei Technologies Co.,Ltd.')
if mibBuilder.loadTexts: hwIsolateMIB.setContactInfo("Huawei Industrial Base Bantian, Longgang Shenzhen 518129 People's Republic of China Website: http://www.huawei.com Email: support@huawei.com")
if mibBuilder.loadTexts: hwIsolateMIB.setDescription('This file is an extension of ISOLATE-MIB.')
hwIsolateObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 247, 1))
hwIsolateTable = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 247, 1, 2))
hwPortIsolateMode = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 247, 1, 2, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwPortIsolateMode.setStatus('current')
if mibBuilder.loadTexts: hwPortIsolateMode.setDescription('Global Isolation Mode. If the HwPortIsolateMode is 1, mode is layer2. If the HwPortIsolateMode is 2, mode is all. By default, mode is layer2.')
hwPortIsolateTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 247, 1, 2, 2), )
if mibBuilder.loadTexts: hwPortIsolateTable.setStatus('current')
if mibBuilder.loadTexts: hwPortIsolateTable.setDescription('Port-isolation table.')
hwPortIsolateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 247, 1, 2, 2, 1), ).setIndexNames((0, "HUAWEI-ISOLATE-MIB", "hwPortIsolateIfIndex"), (0, "HUAWEI-ISOLATE-MIB", "hwPortIsolateGroupId"))
if mibBuilder.loadTexts: hwPortIsolateEntry.setStatus('current')
if mibBuilder.loadTexts: hwPortIsolateEntry.setDescription('Entries of the Port-isolation table.')
hwPortIsolateGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 247, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64)))
if mibBuilder.loadTexts: hwPortIsolateGroupId.setStatus('current')
if mibBuilder.loadTexts: hwPortIsolateGroupId.setDescription('Port-isolation GroupId.')
hwPortIsolateIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 247, 1, 2, 2, 1, 2), InterfaceIndex())
if mibBuilder.loadTexts: hwPortIsolateIfIndex.setStatus('current')
if mibBuilder.loadTexts: hwPortIsolateIfIndex.setDescription('Port IfIndex.')
hwPortIsolateRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 247, 1, 2, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwPortIsolateRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwPortIsolateRowStatus.setDescription('Operation status.')
hwAmIsolateTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 247, 1, 2, 3), )
if mibBuilder.loadTexts: hwAmIsolateTable.setStatus('current')
if mibBuilder.loadTexts: hwAmIsolateTable.setDescription('Am-isolation table.')
hwAmIsolateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 247, 1, 2, 3, 1), ).setIndexNames((0, "HUAWEI-ISOLATE-MIB", "hwAmIsolateSrcIfIndex"), (0, "HUAWEI-ISOLATE-MIB", "hwAmIsolateDstIfIndex"))
if mibBuilder.loadTexts: hwAmIsolateEntry.setStatus('current')
if mibBuilder.loadTexts: hwAmIsolateEntry.setDescription('Entries of the Am-isolation table.')
hwAmIsolateSrcIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 247, 1, 2, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hwAmIsolateSrcIfIndex.setStatus('current')
if mibBuilder.loadTexts: hwAmIsolateSrcIfIndex.setDescription('Source port IfIndex.')
hwAmIsolateDstIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 247, 1, 2, 3, 1, 2), InterfaceIndex())
if mibBuilder.loadTexts: hwAmIsolateDstIfIndex.setStatus('current')
if mibBuilder.loadTexts: hwAmIsolateDstIfIndex.setDescription('Destination port IfIndex.')
hwAmIsolateRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 247, 1, 2, 3, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwAmIsolateRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwAmIsolateRowStatus.setDescription('Operation status.')
hwIsolateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 247, 1, 2, 4)).setObjects(("HUAWEI-ISOLATE-MIB", "hwPortIsolateMode"), ("HUAWEI-ISOLATE-MIB", "hwPortIsolateRowStatus"), ("HUAWEI-ISOLATE-MIB", "hwAmIsolateRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwIsolateGroup = hwIsolateGroup.setStatus('current')
if mibBuilder.loadTexts: hwIsolateGroup.setDescription('This group is mandatory for agents which implement the Isolation.')
hwIsolateComformance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 247, 3)).setObjects(("HUAWEI-ISOLATE-MIB", "hwIsolateGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwIsolateComformance = hwIsolateComformance.setStatus('current')
if mibBuilder.loadTexts: hwIsolateComformance.setDescription('Isolate comformance.')
mibBuilder.exportSymbols("HUAWEI-ISOLATE-MIB", hwAmIsolateEntry=hwAmIsolateEntry, hwAmIsolateSrcIfIndex=hwAmIsolateSrcIfIndex, hwAmIsolateRowStatus=hwAmIsolateRowStatus, hwIsolateObjects=hwIsolateObjects, hwPortIsolateTable=hwPortIsolateTable, hwPortIsolateGroupId=hwPortIsolateGroupId, hwIsolateMIB=hwIsolateMIB, hwAmIsolateDstIfIndex=hwAmIsolateDstIfIndex, hwIsolateGroup=hwIsolateGroup, PYSNMP_MODULE_ID=hwIsolateMIB, hwAmIsolateTable=hwAmIsolateTable, hwIsolateTable=hwIsolateTable, hwPortIsolateEntry=hwPortIsolateEntry, hwPortIsolateIfIndex=hwPortIsolateIfIndex, hwPortIsolateRowStatus=hwPortIsolateRowStatus, hwPortIsolateMode=hwPortIsolateMode, hwIsolateComformance=hwIsolateComformance)