#
# PySNMP MIB module CISCO-IETF-PW-ATM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IETF-PW-ATM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:43:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
AtmVpIdentifier, AtmVcIdentifier = mibBuilder.importSymbols("ATM-TC-MIB", "AtmVpIdentifier", "AtmVcIdentifier")
cpwVcIndex, = mibBuilder.importSymbols("CISCO-IETF-PW-MIB", "cpwVcIndex")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter32, MibIdentifier, Unsigned32, ModuleIdentity, IpAddress, NotificationType, TimeTicks, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, ObjectIdentity, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibIdentifier", "Unsigned32", "ModuleIdentity", "IpAddress", "NotificationType", "TimeTicks", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "ObjectIdentity", "Counter64", "Integer32")
TruthValue, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "DisplayString", "TextualConvention")
cpwVcAtmMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 9000))
cpwVcAtmMIB.setRevisions(('2005-04-19 12:00', '2003-02-16 12:00',))
if mibBuilder.loadTexts: cpwVcAtmMIB.setLastUpdated('200504191200Z')
if mibBuilder.loadTexts: cpwVcAtmMIB.setOrganization('Cisco Systems, Inc')
cpwVcAtmNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 9000, 0))
cpwVcAtmObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 9000, 1))
cpwVcAtmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 9000, 2))
cpwVcAtmTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 1), )
if mibBuilder.loadTexts: cpwVcAtmTable.setStatus('current')
cpwVcAtmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 1, 1), ).setIndexNames((0, "CISCO-IETF-PW-MIB", "cpwVcIndex"))
if mibBuilder.loadTexts: cpwVcAtmEntry.setStatus('current')
cpwAtmIf = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpwAtmIf.setStatus('current')
cpwAtmVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 1, 1, 2), AtmVpIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpwAtmVpi.setStatus('current')
cpwAtmVci = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 1, 1, 3), AtmVcIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpwAtmVci.setStatus('current')
cpwAtmClpQosMapping = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 1, 1, 4), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpwAtmClpQosMapping.setStatus('current')
cpwAtmRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpwAtmRowStatus.setStatus('current')
cpwAtmOamCellSupported = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 1, 1, 6), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpwAtmOamCellSupported.setStatus('current')
cpwAtmQosScalingFactor = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 1, 1, 7), Integer32().clone(100)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpwAtmQosScalingFactor.setStatus('current')
cpwAtmCellPacking = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 1, 1, 8), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpwAtmCellPacking.setStatus('current')
cpwAtmMncp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 1, 1, 9), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpwAtmMncp.setStatus('current')
cpwAtmPeerMncp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpwAtmPeerMncp.setStatus('current')
cpwAtmEncap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("mpls", 1), ("l2tpv3", 2), ("unknown", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpwAtmEncap.setStatus('current')
cpwAtmMcptTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 1, 1, 12), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cpwAtmMcptTimeout.setStatus('current')
cpwVcAtmPerfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 2), )
if mibBuilder.loadTexts: cpwVcAtmPerfTable.setStatus('current')
cpwVcAtmPerfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 2, 1), )
cpwVcAtmEntry.registerAugmentions(("CISCO-IETF-PW-ATM-MIB", "cpwVcAtmPerfEntry"))
cpwVcAtmPerfEntry.setIndexNames(*cpwVcAtmEntry.getIndexNames())
if mibBuilder.loadTexts: cpwVcAtmPerfEntry.setStatus('current')
cpwAtmCellsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpwAtmCellsReceived.setStatus('current')
cpwAtmCellsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpwAtmCellsSent.setStatus('current')
cpwAtmCellsRejected = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpwAtmCellsRejected.setStatus('current')
cpwAtmCellsTagged = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpwAtmCellsTagged.setStatus('current')
cpwAtmHCCellsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpwAtmHCCellsReceived.setStatus('current')
cpwAtmHCCellsRejected = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpwAtmHCCellsRejected.setStatus('current')
cpwAtmHCCellsTagged = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 2, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpwAtmHCCellsTagged.setStatus('current')
cpwAtmAvgCellsPacked = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpwAtmAvgCellsPacked.setStatus('current')
cpwAtmPktsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpwAtmPktsReceived.setStatus('current')
cpwAtmPktsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpwAtmPktsSent.setStatus('current')
cpwAtmPktsRejected = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 9000, 1, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpwAtmPktsRejected.setStatus('current')
cpwVcAtmGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 9000, 2, 1))
cpwVcAtmCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 9000, 2, 2))
cpwVcAtmModuleCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 9000, 2, 2, 1)).setObjects(("CISCO-IETF-PW-ATM-MIB", "cpwVcAtmGroup"), ("CISCO-IETF-PW-ATM-MIB", "cpwAtmPerfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpwVcAtmModuleCompliance = cpwVcAtmModuleCompliance.setStatus('current')
cpwVcAtmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 9000, 2, 1, 1)).setObjects(("CISCO-IETF-PW-ATM-MIB", "cpwAtmIf"), ("CISCO-IETF-PW-ATM-MIB", "cpwAtmVpi"), ("CISCO-IETF-PW-ATM-MIB", "cpwAtmVci"), ("CISCO-IETF-PW-ATM-MIB", "cpwAtmRowStatus"), ("CISCO-IETF-PW-ATM-MIB", "cpwAtmClpQosMapping"), ("CISCO-IETF-PW-ATM-MIB", "cpwAtmOamCellSupported"), ("CISCO-IETF-PW-ATM-MIB", "cpwAtmQosScalingFactor"), ("CISCO-IETF-PW-ATM-MIB", "cpwAtmCellPacking"), ("CISCO-IETF-PW-ATM-MIB", "cpwAtmMncp"), ("CISCO-IETF-PW-ATM-MIB", "cpwAtmPeerMncp"), ("CISCO-IETF-PW-ATM-MIB", "cpwAtmEncap"), ("CISCO-IETF-PW-ATM-MIB", "cpwAtmMcptTimeout"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpwVcAtmGroup = cpwVcAtmGroup.setStatus('current')
cpwAtmPerfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 9000, 2, 1, 2)).setObjects(("CISCO-IETF-PW-ATM-MIB", "cpwAtmCellsReceived"), ("CISCO-IETF-PW-ATM-MIB", "cpwAtmCellsSent"), ("CISCO-IETF-PW-ATM-MIB", "cpwAtmCellsRejected"), ("CISCO-IETF-PW-ATM-MIB", "cpwAtmCellsTagged"), ("CISCO-IETF-PW-ATM-MIB", "cpwAtmHCCellsReceived"), ("CISCO-IETF-PW-ATM-MIB", "cpwAtmHCCellsRejected"), ("CISCO-IETF-PW-ATM-MIB", "cpwAtmHCCellsTagged"), ("CISCO-IETF-PW-ATM-MIB", "cpwAtmPktsReceived"), ("CISCO-IETF-PW-ATM-MIB", "cpwAtmPktsSent"), ("CISCO-IETF-PW-ATM-MIB", "cpwAtmPktsRejected"), ("CISCO-IETF-PW-ATM-MIB", "cpwAtmAvgCellsPacked"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpwAtmPerfGroup = cpwAtmPerfGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-IETF-PW-ATM-MIB", cpwAtmVci=cpwAtmVci, cpwAtmAvgCellsPacked=cpwAtmAvgCellsPacked, cpwVcAtmGroup=cpwVcAtmGroup, cpwVcAtmObjects=cpwVcAtmObjects, cpwAtmRowStatus=cpwAtmRowStatus, cpwAtmPktsReceived=cpwAtmPktsReceived, cpwAtmVpi=cpwAtmVpi, cpwAtmCellsTagged=cpwAtmCellsTagged, cpwVcAtmNotifications=cpwVcAtmNotifications, cpwAtmCellsRejected=cpwAtmCellsRejected, cpwAtmPktsSent=cpwAtmPktsSent, cpwVcAtmCompliances=cpwVcAtmCompliances, cpwAtmQosScalingFactor=cpwAtmQosScalingFactor, cpwAtmCellsReceived=cpwAtmCellsReceived, cpwAtmCellsSent=cpwAtmCellsSent, cpwVcAtmMIB=cpwVcAtmMIB, cpwVcAtmPerfTable=cpwVcAtmPerfTable, cpwAtmMcptTimeout=cpwAtmMcptTimeout, cpwAtmHCCellsRejected=cpwAtmHCCellsRejected, cpwAtmPeerMncp=cpwAtmPeerMncp, cpwAtmHCCellsReceived=cpwAtmHCCellsReceived, cpwVcAtmGroups=cpwVcAtmGroups, cpwVcAtmModuleCompliance=cpwVcAtmModuleCompliance, cpwAtmPerfGroup=cpwAtmPerfGroup, cpwAtmHCCellsTagged=cpwAtmHCCellsTagged, cpwAtmIf=cpwAtmIf, cpwAtmPktsRejected=cpwAtmPktsRejected, cpwAtmOamCellSupported=cpwAtmOamCellSupported, cpwAtmClpQosMapping=cpwAtmClpQosMapping, cpwVcAtmTable=cpwVcAtmTable, PYSNMP_MODULE_ID=cpwVcAtmMIB, cpwAtmEncap=cpwAtmEncap, cpwVcAtmConformance=cpwVcAtmConformance, cpwAtmCellPacking=cpwAtmCellPacking, cpwVcAtmEntry=cpwVcAtmEntry, cpwVcAtmPerfEntry=cpwVcAtmPerfEntry, cpwAtmMncp=cpwAtmMncp)