#
# PySNMP MIB module RADLAN-MIR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-MIR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:39:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, TimeTicks, ObjectIdentity, Integer32, Counter64, Counter32, Gauge32, Unsigned32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "ObjectIdentity", "Integer32", "Counter64", "Counter32", "Gauge32", "Unsigned32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "IpAddress", "Bits")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
rlMir = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 61))
rlMir.setRevisions(('2007-01-02 00:00',))
if mibBuilder.loadTexts: rlMir.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rlMir.setOrganization('Radlan - a MARVELL company. Marvell Semiconductor, Inc.')
rlMirMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 61, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlMirMibVersion.setStatus('current')
rlMirMaxNumOfMRIsAfterReset = MibScalar((1, 3, 6, 1, 4, 1, 89, 61, 2), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMirMaxNumOfMRIsAfterReset.setStatus('current')
rlMirMaxNumOfMRIs = MibScalar((1, 3, 6, 1, 4, 1, 89, 61, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlMirMaxNumOfMRIs.setStatus('current')
rlMirCurMriNum = MibScalar((1, 3, 6, 1, 4, 1, 89, 61, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMirCurMriNum.setStatus('current')
rlMirInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 89, 61, 5), )
if mibBuilder.loadTexts: rlMirInterfaceTable.setStatus('current')
rlMirInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 61, 5, 1), ).setIndexNames((0, "RADLAN-MIR-MIB", "rlMirInterfaceIfIndex"))
if mibBuilder.loadTexts: rlMirInterfaceEntry.setStatus('current')
rlMirInterfaceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 61, 5, 1, 1), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMirInterfaceIfIndex.setStatus('current')
rlMirInterfaceMrid = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 61, 5, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlMirInterfaceMrid.setStatus('current')
rlMirVlanBaseReservedPortsTable = MibTable((1, 3, 6, 1, 4, 1, 89, 61, 6), )
if mibBuilder.loadTexts: rlMirVlanBaseReservedPortsTable.setStatus('current')
rlMirVlanBaseReservedPortsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 61, 6, 1), ).setIndexNames((0, "RADLAN-MIR-MIB", "rlMirVlanBaseReservedPortsIfIndex"))
if mibBuilder.loadTexts: rlMirVlanBaseReservedPortsEntry.setStatus('current')
rlMirVlanBaseReservedPortsIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 61, 6, 1, 1), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlMirVlanBaseReservedPortsIfIndex.setStatus('current')
rlMirVlanBaseReservedPortsStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 61, 6, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlMirVlanBaseReservedPortsStatus.setStatus('current')
rlMirVlanBaseLogicalPortsTable = MibTable((1, 3, 6, 1, 4, 1, 89, 61, 7), )
if mibBuilder.loadTexts: rlMirVlanBaseLogicalPortsTable.setStatus('current')
rlMirVlanBaseLogicalPortsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 61, 7, 1), ).setIndexNames((0, "RADLAN-MIR-MIB", "rlMirVlanBaseLogicalPortsIfIndex"))
if mibBuilder.loadTexts: rlMirVlanBaseLogicalPortsEntry.setStatus('current')
rlMirVlanBaseLogicalPortsIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 61, 7, 1, 1), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlMirVlanBaseLogicalPortsIfIndex.setStatus('current')
rlMirVlanBaseLogicalPortsReservedIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 61, 7, 1, 2), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlMirVlanBaseLogicalPortsReservedIfIndex.setStatus('current')
rlMirVlanBaseLogicalPortsVlanTag = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 61, 7, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlMirVlanBaseLogicalPortsVlanTag.setStatus('current')
rlMirVlanBaseLogicalPortsStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 61, 7, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlMirVlanBaseLogicalPortsStatus.setStatus('current')
rlMirCurMriNumRouter = MibScalar((1, 3, 6, 1, 4, 1, 89, 61, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlMirCurMriNumRouter.setStatus('current')
rlMirCurMriNumOob = MibScalar((1, 3, 6, 1, 4, 1, 89, 61, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlMirCurMriNumOob.setStatus('current')
mibBuilder.exportSymbols("RADLAN-MIR-MIB", rlMirVlanBaseLogicalPortsVlanTag=rlMirVlanBaseLogicalPortsVlanTag, rlMirMaxNumOfMRIsAfterReset=rlMirMaxNumOfMRIsAfterReset, rlMirCurMriNumRouter=rlMirCurMriNumRouter, rlMirVlanBaseLogicalPortsTable=rlMirVlanBaseLogicalPortsTable, rlMirVlanBaseLogicalPortsEntry=rlMirVlanBaseLogicalPortsEntry, rlMirMibVersion=rlMirMibVersion, rlMirInterfaceMrid=rlMirInterfaceMrid, rlMirVlanBaseLogicalPortsIfIndex=rlMirVlanBaseLogicalPortsIfIndex, rlMirVlanBaseLogicalPortsStatus=rlMirVlanBaseLogicalPortsStatus, rlMirVlanBaseReservedPortsStatus=rlMirVlanBaseReservedPortsStatus, rlMir=rlMir, rlMirInterfaceIfIndex=rlMirInterfaceIfIndex, rlMirCurMriNumOob=rlMirCurMriNumOob, rlMirInterfaceTable=rlMirInterfaceTable, PYSNMP_MODULE_ID=rlMir, rlMirInterfaceEntry=rlMirInterfaceEntry, rlMirVlanBaseLogicalPortsReservedIfIndex=rlMirVlanBaseLogicalPortsReservedIfIndex, rlMirCurMriNum=rlMirCurMriNum, rlMirVlanBaseReservedPortsTable=rlMirVlanBaseReservedPortsTable, rlMirVlanBaseReservedPortsIfIndex=rlMirVlanBaseReservedPortsIfIndex, rlMirMaxNumOfMRIs=rlMirMaxNumOfMRIs, rlMirVlanBaseReservedPortsEntry=rlMirVlanBaseReservedPortsEntry)
