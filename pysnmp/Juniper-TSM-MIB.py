#
# PySNMP MIB module Juniper-TSM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-TSM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:53:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
JuniIfType, = mibBuilder.importSymbols("Juniper-UNI-IF-MIB", "JuniIfType")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
iso, ModuleIdentity, Bits, Counter64, Counter32, NotificationType, ObjectIdentity, MibIdentifier, TimeTicks, IpAddress, Unsigned32, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "Bits", "Counter64", "Counter32", "NotificationType", "ObjectIdentity", "MibIdentifier", "TimeTicks", "IpAddress", "Unsigned32", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
juniTsmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72))
juniTsmMIB.setRevisions(('2005-05-23 14:37', '2005-04-27 22:57', '2003-10-23 20:45',))
if mibBuilder.loadTexts: juniTsmMIB.setLastUpdated('200505231437Z')
if mibBuilder.loadTexts: juniTsmMIB.setOrganization('Juniper Networks, Inc.')
class JuniTsmLocationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("slotPort", 1), ("slotAdapterPort", 2), ("adapterPort", 3))

class JuniTsmLocationValue(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 16)

juniTsmObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1))
juniTsmData = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1))
juniTsmLocationType = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 1), JuniTsmLocationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniTsmLocationType.setStatus('current')
juniTsmPortTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 2), )
if mibBuilder.loadTexts: juniTsmPortTable.setStatus('current')
juniTsmPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 2, 1), ).setIndexNames((0, "Juniper-TSM-MIB", "juniTsmPortLocation"))
if mibBuilder.loadTexts: juniTsmPortEntry.setStatus('current')
juniTsmPortLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 2, 1, 1), JuniTsmLocationValue())
if mibBuilder.loadTexts: juniTsmPortLocation.setStatus('current')
juniTsmPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("generalPurposeStatic", 1), ("generalPurposeDynamic", 2), ("securityStatic", 3), ("securityDynamic", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniTsmPortType.setStatus('current')
juniTsmPortHwPresent = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniTsmPortHwPresent.setStatus('current')
juniTsmPortAvailableInterfaces = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniTsmPortAvailableInterfaces.setStatus('current')
juniTsmPortProvisionedInterfaces = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 16000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: juniTsmPortProvisionedInterfaces.setStatus('current')
juniTsmAppRegistryTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 3), )
if mibBuilder.loadTexts: juniTsmAppRegistryTable.setStatus('current')
juniTsmAppRegistryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 3, 1), ).setIndexNames((0, "Juniper-TSM-MIB", "juniTsmAppRegistryIndex"))
if mibBuilder.loadTexts: juniTsmAppRegistryEntry.setStatus('current')
juniTsmAppRegistryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: juniTsmAppRegistryIndex.setStatus('current')
juniTsmAppRegistryIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 3, 1, 2), JuniIfType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniTsmAppRegistryIfType.setStatus('current')
juniTsmAppRegistryName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniTsmAppRegistryName.setStatus('current')
juniTsmAppRegistryInterfaceLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniTsmAppRegistryInterfaceLimit.setStatus('current')
juniTsmApplicationTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 4), )
if mibBuilder.loadTexts: juniTsmApplicationTable.setStatus('current')
juniTsmApplicationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 4, 1), ).setIndexNames((0, "Juniper-TSM-MIB", "juniTsmPortLocation"), (0, "Juniper-TSM-MIB", "juniTsmAppRegistryIndex"))
if mibBuilder.loadTexts: juniTsmApplicationEntry.setStatus('current')
juniTsmApplicationMaxInterfaces = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniTsmApplicationMaxInterfaces.setStatus('current')
juniTsmApplicationActiveInterfaces = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 1, 1, 4, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniTsmApplicationActiveInterfaces.setStatus('current')
juniTsmMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 4))
juniTsmMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 4, 1))
juniTsmMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 4, 2))
juniTsmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 4, 1, 1)).setObjects(("Juniper-TSM-MIB", "juniTsmGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniTsmCompliance = juniTsmCompliance.setStatus('current')
juniTsmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 72, 4, 2, 1)).setObjects(("Juniper-TSM-MIB", "juniTsmLocationType"), ("Juniper-TSM-MIB", "juniTsmPortType"), ("Juniper-TSM-MIB", "juniTsmPortHwPresent"), ("Juniper-TSM-MIB", "juniTsmPortAvailableInterfaces"), ("Juniper-TSM-MIB", "juniTsmPortProvisionedInterfaces"), ("Juniper-TSM-MIB", "juniTsmAppRegistryIfType"), ("Juniper-TSM-MIB", "juniTsmAppRegistryName"), ("Juniper-TSM-MIB", "juniTsmAppRegistryInterfaceLimit"), ("Juniper-TSM-MIB", "juniTsmApplicationMaxInterfaces"), ("Juniper-TSM-MIB", "juniTsmApplicationActiveInterfaces"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniTsmGroup = juniTsmGroup.setStatus('current')
mibBuilder.exportSymbols("Juniper-TSM-MIB", juniTsmMIBConformance=juniTsmMIBConformance, juniTsmApplicationEntry=juniTsmApplicationEntry, juniTsmPortTable=juniTsmPortTable, juniTsmMIBGroups=juniTsmMIBGroups, juniTsmCompliance=juniTsmCompliance, juniTsmData=juniTsmData, juniTsmAppRegistryName=juniTsmAppRegistryName, juniTsmApplicationActiveInterfaces=juniTsmApplicationActiveInterfaces, juniTsmLocationType=juniTsmLocationType, juniTsmPortHwPresent=juniTsmPortHwPresent, juniTsmAppRegistryEntry=juniTsmAppRegistryEntry, juniTsmMIB=juniTsmMIB, juniTsmAppRegistryIfType=juniTsmAppRegistryIfType, juniTsmPortAvailableInterfaces=juniTsmPortAvailableInterfaces, juniTsmPortLocation=juniTsmPortLocation, juniTsmObjects=juniTsmObjects, juniTsmApplicationMaxInterfaces=juniTsmApplicationMaxInterfaces, juniTsmGroup=juniTsmGroup, JuniTsmLocationValue=JuniTsmLocationValue, juniTsmPortProvisionedInterfaces=juniTsmPortProvisionedInterfaces, juniTsmPortEntry=juniTsmPortEntry, juniTsmPortType=juniTsmPortType, juniTsmAppRegistryTable=juniTsmAppRegistryTable, juniTsmAppRegistryInterfaceLimit=juniTsmAppRegistryInterfaceLimit, PYSNMP_MODULE_ID=juniTsmMIB, juniTsmMIBCompliances=juniTsmMIBCompliances, juniTsmAppRegistryIndex=juniTsmAppRegistryIndex, juniTsmApplicationTable=juniTsmApplicationTable, JuniTsmLocationType=JuniTsmLocationType)
