#
# PySNMP MIB module Nortel-Magellan-Passport-VirtualMediaMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-Magellan-Passport-VirtualMediaMIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:19:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
RowStatus, Integer32, DisplayString, InterfaceIndex, StorageType, Unsigned32 = mibBuilder.importSymbols("Nortel-Magellan-Passport-StandardTextualConventionsMIB", "RowStatus", "Integer32", "DisplayString", "InterfaceIndex", "StorageType", "Unsigned32")
Link, = mibBuilder.importSymbols("Nortel-Magellan-Passport-TextualConventionsMIB", "Link")
passportMIBs, components = mibBuilder.importSymbols("Nortel-Magellan-Passport-UsefulDefinitionsMIB", "passportMIBs", "components")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, TimeTicks, Gauge32, Integer32, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, NotificationType, IpAddress, Counter32, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "Gauge32", "Integer32", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "NotificationType", "IpAddress", "Counter32", "Bits", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
virtualMediaMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 135))
vm = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133))
vmRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 1), )
if mibBuilder.loadTexts: vmRowStatusTable.setStatus('mandatory')
vmRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 1, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-VirtualMediaMIB", "vmIndex"))
if mibBuilder.loadTexts: vmRowStatusEntry.setStatus('mandatory')
vmRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vmRowStatus.setStatus('mandatory')
vmComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmComponentName.setStatus('mandatory')
vmStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmStorageType.setStatus('mandatory')
vmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)))
if mibBuilder.loadTexts: vmIndex.setStatus('mandatory')
vmIf = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2))
vmIfRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 1), )
if mibBuilder.loadTexts: vmIfRowStatusTable.setStatus('mandatory')
vmIfRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 1, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-VirtualMediaMIB", "vmIndex"), (0, "Nortel-Magellan-Passport-VirtualMediaMIB", "vmIfIndex"))
if mibBuilder.loadTexts: vmIfRowStatusEntry.setStatus('mandatory')
vmIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vmIfRowStatus.setStatus('mandatory')
vmIfComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmIfComponentName.setStatus('mandatory')
vmIfStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmIfStorageType.setStatus('mandatory')
vmIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)))
if mibBuilder.loadTexts: vmIfIndex.setStatus('mandatory')
vmIfMpTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 10), )
if mibBuilder.loadTexts: vmIfMpTable.setStatus('mandatory')
vmIfMpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 10, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-VirtualMediaMIB", "vmIndex"), (0, "Nortel-Magellan-Passport-VirtualMediaMIB", "vmIfIndex"))
if mibBuilder.loadTexts: vmIfMpEntry.setStatus('mandatory')
vmIfLinkToProtocolPort = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 10, 1, 1), Link()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vmIfLinkToProtocolPort.setStatus('mandatory')
vmIfCidDataTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 11), )
if mibBuilder.loadTexts: vmIfCidDataTable.setStatus('mandatory')
vmIfCidDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 11, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-VirtualMediaMIB", "vmIndex"), (0, "Nortel-Magellan-Passport-VirtualMediaMIB", "vmIfIndex"))
if mibBuilder.loadTexts: vmIfCidDataEntry.setStatus('mandatory')
vmIfCustomerIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 11, 1, 1), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8191), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vmIfCustomerIdentifier.setStatus('mandatory')
vmIfIfEntryTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 12), )
if mibBuilder.loadTexts: vmIfIfEntryTable.setStatus('mandatory')
vmIfIfEntryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 12, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-VirtualMediaMIB", "vmIndex"), (0, "Nortel-Magellan-Passport-VirtualMediaMIB", "vmIfIndex"))
if mibBuilder.loadTexts: vmIfIfEntryEntry.setStatus('mandatory')
vmIfIfAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 12, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3))).clone('up')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vmIfIfAdminStatus.setStatus('mandatory')
vmIfIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 12, 1, 2), InterfaceIndex().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmIfIfIndex.setStatus('mandatory')
vmIfOperStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 13), )
if mibBuilder.loadTexts: vmIfOperStatusTable.setStatus('mandatory')
vmIfOperStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 13, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-VirtualMediaMIB", "vmIndex"), (0, "Nortel-Magellan-Passport-VirtualMediaMIB", "vmIfIndex"))
if mibBuilder.loadTexts: vmIfOperStatusEntry.setStatus('mandatory')
vmIfSnmpOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 13, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3))).clone('up')).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmIfSnmpOperStatus.setStatus('mandatory')
vmIfStateTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 14), )
if mibBuilder.loadTexts: vmIfStateTable.setStatus('mandatory')
vmIfStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 14, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-VirtualMediaMIB", "vmIndex"), (0, "Nortel-Magellan-Passport-VirtualMediaMIB", "vmIfIndex"))
if mibBuilder.loadTexts: vmIfStateEntry.setStatus('mandatory')
vmIfAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 14, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("locked", 0), ("unlocked", 1), ("shuttingDown", 2))).clone('unlocked')).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmIfAdminState.setStatus('mandatory')
vmIfOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 14, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmIfOperationalState.setStatus('mandatory')
vmIfUsageState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 14, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("idle", 0), ("active", 1), ("busy", 2))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmIfUsageState.setStatus('mandatory')
vmIfProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 15), )
if mibBuilder.loadTexts: vmIfProvTable.setStatus('mandatory')
vmIfProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 15, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-VirtualMediaMIB", "vmIndex"), (0, "Nortel-Magellan-Passport-VirtualMediaMIB", "vmIfIndex"))
if mibBuilder.loadTexts: vmIfProvEntry.setStatus('mandatory')
vmIfMode = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 133, 2, 15, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("alwaysUpInterface", 0), ("interVrConnection", 1))).clone('alwaysUpInterface')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vmIfMode.setStatus('mandatory')
virtualMediaGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 135, 1))
virtualMediaGroupBE = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 135, 1, 5))
virtualMediaGroupBE01 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 135, 1, 5, 2))
virtualMediaGroupBE01A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 135, 1, 5, 2, 2))
virtualMediaCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 135, 3))
virtualMediaCapabilitiesBE = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 135, 3, 5))
virtualMediaCapabilitiesBE01 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 135, 3, 5, 2))
virtualMediaCapabilitiesBE01A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 135, 3, 5, 2, 2))
mibBuilder.exportSymbols("Nortel-Magellan-Passport-VirtualMediaMIB", vmComponentName=vmComponentName, vmIfRowStatus=vmIfRowStatus, vmIfIndex=vmIfIndex, vm=vm, virtualMediaCapabilitiesBE01=virtualMediaCapabilitiesBE01, vmIfIfIndex=vmIfIfIndex, vmIfOperStatusTable=vmIfOperStatusTable, virtualMediaCapabilitiesBE=virtualMediaCapabilitiesBE, virtualMediaMIB=virtualMediaMIB, vmIfMpTable=vmIfMpTable, vmIfComponentName=vmIfComponentName, virtualMediaCapabilitiesBE01A=virtualMediaCapabilitiesBE01A, vmIfUsageState=vmIfUsageState, vmIfMode=vmIfMode, vmIfAdminState=vmIfAdminState, vmIfProvTable=vmIfProvTable, vmIfCidDataTable=vmIfCidDataTable, virtualMediaGroupBE01A=virtualMediaGroupBE01A, virtualMediaGroupBE=virtualMediaGroupBE, vmIfCustomerIdentifier=vmIfCustomerIdentifier, vmRowStatus=vmRowStatus, virtualMediaGroup=virtualMediaGroup, vmIfRowStatusTable=vmIfRowStatusTable, vmIfIfAdminStatus=vmIfIfAdminStatus, virtualMediaGroupBE01=virtualMediaGroupBE01, vmIfStateEntry=vmIfStateEntry, vmIfProvEntry=vmIfProvEntry, virtualMediaCapabilities=virtualMediaCapabilities, vmRowStatusTable=vmRowStatusTable, vmIfRowStatusEntry=vmIfRowStatusEntry, vmIfIfEntryTable=vmIfIfEntryTable, vmIfStorageType=vmIfStorageType, vmIfOperStatusEntry=vmIfOperStatusEntry, vmIfOperationalState=vmIfOperationalState, vmStorageType=vmStorageType, vmIfLinkToProtocolPort=vmIfLinkToProtocolPort, vmIfMpEntry=vmIfMpEntry, vmIfCidDataEntry=vmIfCidDataEntry, vmIfSnmpOperStatus=vmIfSnmpOperStatus, vmIndex=vmIndex, vmIf=vmIf, vmRowStatusEntry=vmRowStatusEntry, vmIfStateTable=vmIfStateTable, vmIfIfEntryEntry=vmIfIfEntryEntry)
