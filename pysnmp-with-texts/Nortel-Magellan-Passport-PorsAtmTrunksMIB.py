#
# PySNMP MIB module Nortel-Magellan-Passport-PorsAtmTrunksMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-Magellan-Passport-PorsAtmTrunksMIB
# Produced by pysmi-0.3.4 at Wed May  1 14:28:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
trkPa, trkPaIndex = mibBuilder.importSymbols("Nortel-Magellan-Passport-PorsTrunksMIB", "trkPa", "trkPaIndex")
DisplayString, RowStatus, StorageType = mibBuilder.importSymbols("Nortel-Magellan-Passport-StandardTextualConventionsMIB", "DisplayString", "RowStatus", "StorageType")
Link, NonReplicated = mibBuilder.importSymbols("Nortel-Magellan-Passport-TextualConventionsMIB", "Link", "NonReplicated")
trkIndex, = mibBuilder.importSymbols("Nortel-Magellan-Passport-TrunksMIB", "trkIndex")
passportMIBs, = mibBuilder.importSymbols("Nortel-Magellan-Passport-UsefulDefinitionsMIB", "passportMIBs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Bits, Gauge32, Counter64, Unsigned32, TimeTicks, Counter32, Integer32, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Bits", "Gauge32", "Counter64", "Unsigned32", "TimeTicks", "Counter32", "Integer32", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
porsAtmTrunksMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 137))
trkPaAtm = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 3))
trkPaAtmRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 3, 1), )
if mibBuilder.loadTexts: trkPaAtmRowStatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: trkPaAtmRowStatusTable.setDescription('This entry controls the addition and deletion of trkPaAtm components.')
trkPaAtmRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 3, 1, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"), (0, "Nortel-Magellan-Passport-PorsTrunksMIB", "trkPaIndex"), (0, "Nortel-Magellan-Passport-PorsAtmTrunksMIB", "trkPaAtmIndex"))
if mibBuilder.loadTexts: trkPaAtmRowStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: trkPaAtmRowStatusEntry.setDescription('A single entry in the table represents a single trkPaAtm component.')
trkPaAtmRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 3, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trkPaAtmRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: trkPaAtmRowStatus.setDescription('This variable is used as the basis for SNMP naming of trkPaAtm components. These components can be added and deleted.')
trkPaAtmComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 3, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkPaAtmComponentName.setStatus('mandatory')
if mibBuilder.loadTexts: trkPaAtmComponentName.setDescription("This variable provides the component's string name for use with the ASCII Console Interface")
trkPaAtmStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 3, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trkPaAtmStorageType.setStatus('mandatory')
if mibBuilder.loadTexts: trkPaAtmStorageType.setDescription('This variable represents the storage type value for the trkPaAtm tables.')
trkPaAtmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 3, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: trkPaAtmIndex.setStatus('mandatory')
if mibBuilder.loadTexts: trkPaAtmIndex.setDescription('This variable represents the index for the trkPaAtm tables.')
trkPaAtmProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 3, 10), )
if mibBuilder.loadTexts: trkPaAtmProvTable.setStatus('mandatory')
if mibBuilder.loadTexts: trkPaAtmProvTable.setDescription('This group of attributes provides the parameters used by the AtmAccess component for specifying access to an ATM interface.')
trkPaAtmProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 3, 10, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-TrunksMIB", "trkIndex"), (0, "Nortel-Magellan-Passport-PorsTrunksMIB", "trkPaIndex"), (0, "Nortel-Magellan-Passport-PorsAtmTrunksMIB", "trkPaAtmIndex"))
if mibBuilder.loadTexts: trkPaAtmProvEntry.setStatus('mandatory')
if mibBuilder.loadTexts: trkPaAtmProvEntry.setDescription('An entry in the trkPaAtmProvTable.')
trkPaAtmAtmConnection = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 3, 10, 1, 1), Link()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trkPaAtmAtmConnection.setStatus('mandatory')
if mibBuilder.loadTexts: trkPaAtmAtmConnection.setDescription('This attribute specifies the component name of the ATM Virtual Circuit that the AtmAccess component will use. The format of the component name is AtmIf/n Vcc/x.y Nep')
trkPaAtmMode = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 60, 4, 3, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("multiplexing", 0), ("mapping", 1))).clone('multiplexing')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trkPaAtmMode.setStatus('mandatory')
if mibBuilder.loadTexts: trkPaAtmMode.setDescription("This attribute specifies the operating mode of the PathAdmin. When set to multiplexing the PathAdmin to multiplex voice calls to the given atmConnection using single cell per voice packet transport. All other calls will be multiplexed using AAL5 over the Trunk's VCC. When set to mapping the PathAdmin will allocate a VCC per LCh/n. In mapping mode the atmConnection should not be set. The VCC chosen for a given connection can be seen in the LCh localConnection attribute.")
porsAtmTrunksGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 137, 1))
porsAtmTrunksGroupBE = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 137, 1, 5))
porsAtmTrunksGroupBE01 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 137, 1, 5, 2))
porsAtmTrunksGroupBE01A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 137, 1, 5, 2, 2))
porsAtmTrunksCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 137, 3))
porsAtmTrunksCapabilitiesBE = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 137, 3, 5))
porsAtmTrunksCapabilitiesBE01 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 137, 3, 5, 2))
porsAtmTrunksCapabilitiesBE01A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 137, 3, 5, 2, 2))
mibBuilder.exportSymbols("Nortel-Magellan-Passport-PorsAtmTrunksMIB", trkPaAtmComponentName=trkPaAtmComponentName, trkPaAtmMode=trkPaAtmMode, porsAtmTrunksCapabilitiesBE01A=porsAtmTrunksCapabilitiesBE01A, porsAtmTrunksGroupBE=porsAtmTrunksGroupBE, porsAtmTrunksGroupBE01=porsAtmTrunksGroupBE01, trkPaAtm=trkPaAtm, trkPaAtmStorageType=trkPaAtmStorageType, porsAtmTrunksGroupBE01A=porsAtmTrunksGroupBE01A, trkPaAtmRowStatusEntry=trkPaAtmRowStatusEntry, trkPaAtmIndex=trkPaAtmIndex, trkPaAtmAtmConnection=trkPaAtmAtmConnection, porsAtmTrunksCapabilitiesBE01=porsAtmTrunksCapabilitiesBE01, trkPaAtmRowStatus=trkPaAtmRowStatus, trkPaAtmProvTable=trkPaAtmProvTable, trkPaAtmProvEntry=trkPaAtmProvEntry, porsAtmTrunksGroup=porsAtmTrunksGroup, trkPaAtmRowStatusTable=trkPaAtmRowStatusTable, porsAtmTrunksMIB=porsAtmTrunksMIB, porsAtmTrunksCapabilitiesBE=porsAtmTrunksCapabilitiesBE, porsAtmTrunksCapabilities=porsAtmTrunksCapabilities)