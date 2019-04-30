#
# PySNMP MIB module JNX-PPPOE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JNX-PPPOE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:47:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
jnxPppoeMibRoot, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxPppoeMibRoot")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ModuleIdentity, Integer32, IpAddress, NotificationType, Counter64, iso, ObjectIdentity, Counter32, TimeTicks, Bits, MibIdentifier, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ModuleIdentity", "Integer32", "IpAddress", "NotificationType", "Counter64", "iso", "ObjectIdentity", "Counter32", "TimeTicks", "Bits", "MibIdentifier", "Gauge32")
TextualConvention, RowStatus, MacAddress, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "MacAddress", "TruthValue", "DisplayString")
jnxPPPoEMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1))
jnxPPPoEMIB.setRevisions(('2013-06-13 00:00', '2010-07-22 09:42',))
if mibBuilder.loadTexts: jnxPPPoEMIB.setLastUpdated('201007220942Z')
if mibBuilder.loadTexts: jnxPPPoEMIB.setOrganization('Juniper Networks, Inc.')
class JnxPPPoEServiceNameAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("drop", 0), ("terminate", 1))

jnxPPPoEObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1))
jnxPPPoEIfLayer = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1))
jnxPPPoESubIfLayer = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 2))
jnxPPPoESummary = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 3))
jnxPPPoEServices = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 4))
jnxPPPoENextIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 1), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoENextIfIndex.setStatus('current')
jnxPPPoEIfTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 2), )
if mibBuilder.loadTexts: jnxPPPoEIfTable.setStatus('current')
jnxPPPoEIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 2, 1), ).setIndexNames((0, "JNX-PPPOE-MIB", "jnxPPPoEIfIfIndex"))
if mibBuilder.loadTexts: jnxPPPoEIfEntry.setStatus('current')
jnxPPPoEIfIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: jnxPPPoEIfIfIndex.setStatus('current')
jnxPPPoEIfMaxNumSessions = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65335))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEIfMaxNumSessions.setStatus('current')
jnxPPPoEIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 2, 1, 3), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEIfRowStatus.setStatus('current')
jnxPPPoEIfLowerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 2, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEIfLowerIfIndex.setStatus('current')
jnxPPPoEIfAcName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEIfAcName.setStatus('current')
jnxPPPoEIfDupProtect = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEIfDupProtect.setStatus('current')
jnxPPPoEIfPADIFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEIfPADIFlag.setStatus('current')
jnxPPPoEIfAutoconfig = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEIfAutoconfig.setStatus('current')
jnxPPPoEIfServiceNameTable = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 2, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEIfServiceNameTable.setStatus('current')
jnxPPPoEIfPadrRemoteCircuitIdCapture = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEIfPadrRemoteCircuitIdCapture.setStatus('current')
jnxPPPoEIfMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 1), ValueRangeConstraint(2, 2), ValueRangeConstraint(66, 65535), )).clone(1494)).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEIfMtu.setStatus('current')
jnxPPPoEIfLockoutMin = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 2, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEIfLockoutMin.setStatus('current')
jnxPPPoEIfLockoutMax = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 2, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEIfLockoutMax.setStatus('current')
jnxPPPoEIfDynamicProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 2, 1, 14), DisplayString().clone(' ')).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEIfDynamicProfile.setStatus('current')
jnxPPPoEIfStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 3), )
if mibBuilder.loadTexts: jnxPPPoEIfStatsTable.setStatus('current')
jnxPPPoEIfStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 3, 1), ).setIndexNames((0, "JNX-PPPOE-MIB", "jnxPPPoEIfIfIndex"))
if mibBuilder.loadTexts: jnxPPPoEIfStatsEntry.setStatus('current')
jnxPPPoEIfStatsRxPADI = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEIfStatsRxPADI.setStatus('current')
jnxPPPoEIfStatsTxPADO = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEIfStatsTxPADO.setStatus('current')
jnxPPPoEIfStatsRxPADR = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEIfStatsRxPADR.setStatus('current')
jnxPPPoEIfStatsTxPADS = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEIfStatsTxPADS.setStatus('current')
jnxPPPoEIfStatsRxPADT = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEIfStatsRxPADT.setStatus('current')
jnxPPPoEIfStatsTxPADT = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEIfStatsTxPADT.setStatus('current')
jnxPPPoEIfStatsRxInvVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEIfStatsRxInvVersion.setStatus('current')
jnxPPPoEIfStatsRxInvCode = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEIfStatsRxInvCode.setStatus('current')
jnxPPPoEIfStatsRxInvTags = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEIfStatsRxInvTags.setStatus('current')
jnxPPPoEIfStatsRxInvSession = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEIfStatsRxInvSession.setStatus('obsolete')
jnxPPPoEIfStatsRxInvTypes = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEIfStatsRxInvTypes.setStatus('current')
jnxPPPoEIfStatsRxInvPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEIfStatsRxInvPackets.setStatus('current')
jnxPPPoEIfStatsRxInsufficientResources = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEIfStatsRxInsufficientResources.setStatus('current')
jnxPPPoEIfStatsTxPADM = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEIfStatsTxPADM.setStatus('current')
jnxPPPoEIfStatsTxPADN = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEIfStatsTxPADN.setStatus('current')
jnxPPPoEIfStatsRxInvTagLength = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 3, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEIfStatsRxInvTagLength.setStatus('current')
jnxPPPoEIfStatsRxInvLength = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 3, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEIfStatsRxInvLength.setStatus('current')
jnxPPPoEIfStatsRxInvPadISession = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 3, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEIfStatsRxInvPadISession.setStatus('current')
jnxPPPoEIfStatsRxInvPadRSession = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 3, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEIfStatsRxInvPadRSession.setStatus('current')
jnxPPPoEIfLockoutTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 4), )
if mibBuilder.loadTexts: jnxPPPoEIfLockoutTable.setStatus('current')
jnxPPPoEIfLockoutEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 4, 1), ).setIndexNames((0, "JNX-PPPOE-MIB", "jnxPPPoEIfIfIndex"), (0, "JNX-PPPOE-MIB", "jnxPPPoEIfLockoutClientAddress"))
if mibBuilder.loadTexts: jnxPPPoEIfLockoutEntry.setStatus('current')
jnxPPPoEIfLockoutClientAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 4, 1, 1), MacAddress())
if mibBuilder.loadTexts: jnxPPPoEIfLockoutClientAddress.setStatus('current')
jnxPPPoEIfLockoutTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEIfLockoutTime.setStatus('current')
jnxPPPoEIfLockoutElapsedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEIfLockoutElapsedTime.setStatus('current')
jnxPPPoEIfLockoutNextTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEIfLockoutNextTime.setStatus('current')
jnxPPPoESubIfNextIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 2, 1), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoESubIfNextIfIndex.setStatus('current')
jnxPPPoESubIfTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 2, 2), )
if mibBuilder.loadTexts: jnxPPPoESubIfTable.setStatus('current')
jnxPPPoESubIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 2, 2, 1), ).setIndexNames((0, "JNX-PPPOE-MIB", "jnxPPPoESubIfIndex"))
if mibBuilder.loadTexts: jnxPPPoESubIfEntry.setStatus('current')
jnxPPPoESubIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 2, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: jnxPPPoESubIfIndex.setStatus('current')
jnxPPPoESubIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 2, 2, 1, 2), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoESubIfRowStatus.setStatus('current')
jnxPPPoESubIfLowerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 2, 2, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoESubIfLowerIfIndex.setStatus('current')
jnxPPPoESubIfId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647)).clone(-1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoESubIfId.setStatus('current')
jnxPPPoESubIfSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoESubIfSessionId.setStatus('current')
jnxPPPoESubIfMotm = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 2, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoESubIfMotm.setStatus('current')
jnxPPPoESubIfUrl = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 2, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoESubIfUrl.setStatus('current')
jnxPppoeSubIfQueueStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 2, 3), )
if mibBuilder.loadTexts: jnxPppoeSubIfQueueStatsTable.setStatus('current')
jnxPppoeSubIfPerQueueStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 2, 3, 1), ).setIndexNames((0, "JNX-PPPOE-MIB", "jnxPPPoESubIfIndex"), (0, "JNX-PPPOE-MIB", "jnxPppoeSubIfQueueIndex"))
if mibBuilder.loadTexts: jnxPppoeSubIfPerQueueStatsEntry.setStatus('current')
jnxPppoeSubIfQueueIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: jnxPppoeSubIfQueueIndex.setStatus('current')
jnxPppoeSubIfQueueStatsPacketSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 2, 3, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPppoeSubIfQueueStatsPacketSent.setStatus('current')
jnxPppoeSubIfQueueStatsBytesSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 2, 3, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPppoeSubIfQueueStatsBytesSent.setStatus('current')
jnxPppoeSubIfQueueStatsPacketDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 2, 3, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPppoeSubIfQueueStatsPacketDropped.setStatus('current')
jnxPppoeSubIfQueueStatsBytesDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 2, 3, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPppoeSubIfQueueStatsBytesDropped.setStatus('current')
jnxPppoeSubIfQueueStatsActualBitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 2, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPppoeSubIfQueueStatsActualBitRate.setStatus('current')
jnxPppoeSubIfQueueStatsActualDroppedBitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 2, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPppoeSubIfQueueStatsActualDroppedBitRate.setStatus('current')
jnxPPPoEServiceNameTableTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 4, 1), )
if mibBuilder.loadTexts: jnxPPPoEServiceNameTableTable.setStatus('current')
jnxPPPoEServiceNameTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 4, 1, 1), ).setIndexNames((0, "JNX-PPPOE-MIB", "jnxPPPoEServiceNameTableName"))
if mibBuilder.loadTexts: jnxPPPoEServiceNameTableEntry.setStatus('current')
jnxPPPoEServiceNameTableName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 4, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: jnxPPPoEServiceNameTableName.setStatus('current')
jnxPPPoEServiceNameTableRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 4, 1, 1, 2), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEServiceNameTableRowStatus.setStatus('current')
jnxPPPoEServiceNameTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 4, 2), )
if mibBuilder.loadTexts: jnxPPPoEServiceNameTable.setStatus('current')
jnxPPPoEServiceNameEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 4, 2, 1), ).setIndexNames((0, "JNX-PPPOE-MIB", "jnxPPPoEServiceNameTableName"), (0, "JNX-PPPOE-MIB", "jnxPPPoEServiceName"))
if mibBuilder.loadTexts: jnxPPPoEServiceNameEntry.setStatus('current')
jnxPPPoEServiceName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 4, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64)))
if mibBuilder.loadTexts: jnxPPPoEServiceName.setStatus('current')
jnxPPPoEServiceNameAction = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 4, 2, 1, 2), JnxPPPoEServiceNameAction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEServiceNameAction.setStatus('current')
jnxPPPoEServiceNameDynamicProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 4, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEServiceNameDynamicProfile.setStatus('current')
jnxPPPoEServiceNameRoutingInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 4, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEServiceNameRoutingInstance.setStatus('current')
jnxPPPoEServiceNameMaxSessions = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 4, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEServiceNameMaxSessions.setStatus('current')
jnxPPPoEServiceNameRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 4, 2, 1, 6), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEServiceNameRowStatus.setStatus('current')
jnxPPPoEServiceNameAciAriTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 4, 3), )
if mibBuilder.loadTexts: jnxPPPoEServiceNameAciAriTable.setStatus('current')
jnxPPPoEServiceNameAciAriEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 4, 3, 1), ).setIndexNames((0, "JNX-PPPOE-MIB", "jnxPPPoEServiceNameTableName"), (0, "JNX-PPPOE-MIB", "jnxPPPoEServiceName"), (0, "JNX-PPPOE-MIB", "jnxPPPoEServiceNameAgentCircuitId"), (0, "JNX-PPPOE-MIB", "jnxPPPoEServiceNameAgentRemoteId"))
if mibBuilder.loadTexts: jnxPPPoEServiceNameAciAriEntry.setStatus('current')
jnxPPPoEServiceNameAgentCircuitId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 4, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64)))
if mibBuilder.loadTexts: jnxPPPoEServiceNameAgentCircuitId.setStatus('current')
jnxPPPoEServiceNameAgentRemoteId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 4, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64)))
if mibBuilder.loadTexts: jnxPPPoEServiceNameAgentRemoteId.setStatus('current')
jnxPPPoEServiceNameAciAriAction = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 4, 3, 1, 3), JnxPPPoEServiceNameAction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEServiceNameAciAriAction.setStatus('current')
jnxPPPoEServiceNameAciAriDynamicProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 4, 3, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEServiceNameAciAriDynamicProfile.setStatus('current')
jnxPPPoEServiceNameAciAriRoutingInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 4, 3, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEServiceNameAciAriRoutingInstance.setStatus('current')
jnxPPPoEServiceNameAciAriStaticInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 4, 3, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEServiceNameAciAriStaticInterface.setStatus('current')
jnxPPPoEServiceNameAciAriRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 4, 3, 1, 7), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEServiceNameAciAriRowStatus.setStatus('current')
jnxPPPoEMajorInterfaceCount = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoEMajorInterfaceCount.setStatus('current')
jnxPPPoESummaryMajorIfAdminUp = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 3, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoESummaryMajorIfAdminUp.setStatus('current')
jnxPPPoESummaryMajorIfAdminDown = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 3, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoESummaryMajorIfAdminDown.setStatus('current')
jnxPPPoESummaryMajorIfOperUp = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 3, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoESummaryMajorIfOperUp.setStatus('current')
jnxPPPoESummaryMajorIfOperDown = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 3, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoESummaryMajorIfOperDown.setStatus('current')
jnxPPPoESummaryMajorIfLowerLayerDown = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 3, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoESummaryMajorIfLowerLayerDown.setStatus('current')
jnxPPPoESummaryMajorIfNotPresent = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 3, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoESummaryMajorIfNotPresent.setStatus('current')
jnxPPPoESummarySubInterfaceCount = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 3, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoESummarySubInterfaceCount.setStatus('current')
jnxPPPoESummarySubIfAdminUp = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 3, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoESummarySubIfAdminUp.setStatus('current')
jnxPPPoESummarySubIfAdminDown = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 3, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoESummarySubIfAdminDown.setStatus('current')
jnxPPPoESummarySubIfOperUp = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 3, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoESummarySubIfOperUp.setStatus('current')
jnxPPPoESummarySubIfOperDown = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 3, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoESummarySubIfOperDown.setStatus('current')
jnxPPPoESummarySubIfLowerLayerDown = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 3, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoESummarySubIfLowerLayerDown.setStatus('current')
jnxPPPoESummarySubIfNotPresent = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 1, 3, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxPPPoESummarySubIfNotPresent.setStatus('current')
jnxPPPoEConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 4))
jnxPPPoECompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 4, 1))
jnxPPPoEGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 67, 1, 4, 2))
mibBuilder.exportSymbols("JNX-PPPOE-MIB", jnxPppoeSubIfQueueIndex=jnxPppoeSubIfQueueIndex, jnxPPPoEServiceNameTableRowStatus=jnxPPPoEServiceNameTableRowStatus, jnxPPPoESummarySubInterfaceCount=jnxPPPoESummarySubInterfaceCount, jnxPPPoEIfLockoutElapsedTime=jnxPPPoEIfLockoutElapsedTime, jnxPPPoESummaryMajorIfAdminUp=jnxPPPoESummaryMajorIfAdminUp, jnxPPPoESummaryMajorIfAdminDown=jnxPPPoESummaryMajorIfAdminDown, PYSNMP_MODULE_ID=jnxPPPoEMIB, jnxPPPoESummaryMajorIfOperUp=jnxPPPoESummaryMajorIfOperUp, jnxPPPoEServiceNameRoutingInstance=jnxPPPoEServiceNameRoutingInstance, jnxPPPoEIfAutoconfig=jnxPPPoEIfAutoconfig, jnxPPPoEServiceName=jnxPPPoEServiceName, jnxPPPoEIfStatsRxPADT=jnxPPPoEIfStatsRxPADT, jnxPPPoEIfStatsTxPADO=jnxPPPoEIfStatsTxPADO, jnxPppoeSubIfQueueStatsPacketDropped=jnxPppoeSubIfQueueStatsPacketDropped, jnxPPPoEIfStatsRxInvPackets=jnxPPPoEIfStatsRxInvPackets, jnxPppoeSubIfQueueStatsBytesDropped=jnxPppoeSubIfQueueStatsBytesDropped, jnxPppoeSubIfQueueStatsActualDroppedBitRate=jnxPppoeSubIfQueueStatsActualDroppedBitRate, jnxPPPoEServiceNameAction=jnxPPPoEServiceNameAction, jnxPPPoEIfStatsTable=jnxPPPoEIfStatsTable, jnxPPPoEIfIfIndex=jnxPPPoEIfIfIndex, jnxPPPoEIfStatsTxPADM=jnxPPPoEIfStatsTxPADM, jnxPPPoESubIfEntry=jnxPPPoESubIfEntry, jnxPPPoEIfTable=jnxPPPoEIfTable, jnxPPPoEIfLayer=jnxPPPoEIfLayer, jnxPPPoEMIB=jnxPPPoEMIB, jnxPPPoEServiceNameRowStatus=jnxPPPoEServiceNameRowStatus, jnxPPPoESubIfLayer=jnxPPPoESubIfLayer, jnxPppoeSubIfQueueStatsPacketSent=jnxPppoeSubIfQueueStatsPacketSent, jnxPPPoEIfStatsTxPADT=jnxPPPoEIfStatsTxPADT, jnxPPPoESummaryMajorIfLowerLayerDown=jnxPPPoESummaryMajorIfLowerLayerDown, jnxPPPoEServiceNameAciAriEntry=jnxPPPoEServiceNameAciAriEntry, jnxPPPoENextIfIndex=jnxPPPoENextIfIndex, jnxPPPoEIfLockoutTime=jnxPPPoEIfLockoutTime, jnxPPPoESummaryMajorIfNotPresent=jnxPPPoESummaryMajorIfNotPresent, jnxPPPoEServiceNameAciAriStaticInterface=jnxPPPoEServiceNameAciAriStaticInterface, jnxPPPoESubIfMotm=jnxPPPoESubIfMotm, jnxPPPoESummary=jnxPPPoESummary, jnxPPPoEIfStatsRxInvPadISession=jnxPPPoEIfStatsRxInvPadISession, jnxPPPoESubIfTable=jnxPPPoESubIfTable, jnxPPPoEIfStatsRxPADI=jnxPPPoEIfStatsRxPADI, jnxPPPoEIfEntry=jnxPPPoEIfEntry, jnxPPPoEIfStatsTxPADN=jnxPPPoEIfStatsTxPADN, jnxPPPoEIfLockoutTable=jnxPPPoEIfLockoutTable, jnxPPPoEIfAcName=jnxPPPoEIfAcName, jnxPPPoEIfStatsEntry=jnxPPPoEIfStatsEntry, jnxPPPoEIfLockoutMin=jnxPPPoEIfLockoutMin, jnxPPPoEServiceNameAciAriDynamicProfile=jnxPPPoEServiceNameAciAriDynamicProfile, jnxPPPoEServiceNameTableName=jnxPPPoEServiceNameTableName, jnxPPPoEIfStatsRxInvTagLength=jnxPPPoEIfStatsRxInvTagLength, jnxPPPoEIfStatsRxInvVersion=jnxPPPoEIfStatsRxInvVersion, jnxPPPoESummarySubIfNotPresent=jnxPPPoESummarySubIfNotPresent, jnxPPPoEServiceNameDynamicProfile=jnxPPPoEServiceNameDynamicProfile, jnxPPPoEObjects=jnxPPPoEObjects, jnxPPPoESubIfNextIfIndex=jnxPPPoESubIfNextIfIndex, jnxPPPoEIfStatsRxInvCode=jnxPPPoEIfStatsRxInvCode, jnxPPPoESubIfLowerIfIndex=jnxPPPoESubIfLowerIfIndex, jnxPPPoEServiceNameAciAriRowStatus=jnxPPPoEServiceNameAciAriRowStatus, jnxPPPoESummaryMajorIfOperDown=jnxPPPoESummaryMajorIfOperDown, jnxPPPoEIfLockoutClientAddress=jnxPPPoEIfLockoutClientAddress, jnxPPPoEServiceNameAciAriRoutingInstance=jnxPPPoEServiceNameAciAriRoutingInstance, jnxPPPoESummarySubIfLowerLayerDown=jnxPPPoESummarySubIfLowerLayerDown, jnxPPPoEIfPADIFlag=jnxPPPoEIfPADIFlag, jnxPPPoEIfDynamicProfile=jnxPPPoEIfDynamicProfile, jnxPPPoEServiceNameTableTable=jnxPPPoEServiceNameTableTable, jnxPPPoEIfStatsRxInvPadRSession=jnxPPPoEIfStatsRxInvPadRSession, JnxPPPoEServiceNameAction=JnxPPPoEServiceNameAction, jnxPppoeSubIfQueueStatsActualBitRate=jnxPppoeSubIfQueueStatsActualBitRate, jnxPPPoEMajorInterfaceCount=jnxPPPoEMajorInterfaceCount, jnxPPPoEIfLowerIfIndex=jnxPPPoEIfLowerIfIndex, jnxPPPoEGroups=jnxPPPoEGroups, jnxPPPoEIfRowStatus=jnxPPPoEIfRowStatus, jnxPPPoEServiceNameAciAriTable=jnxPPPoEServiceNameAciAriTable, jnxPppoeSubIfQueueStatsTable=jnxPppoeSubIfQueueStatsTable, jnxPPPoEIfPadrRemoteCircuitIdCapture=jnxPPPoEIfPadrRemoteCircuitIdCapture, jnxPPPoESummarySubIfOperUp=jnxPPPoESummarySubIfOperUp, jnxPPPoESubIfRowStatus=jnxPPPoESubIfRowStatus, jnxPPPoEConformance=jnxPPPoEConformance, jnxPPPoEIfMaxNumSessions=jnxPPPoEIfMaxNumSessions, jnxPppoeSubIfQueueStatsBytesSent=jnxPppoeSubIfQueueStatsBytesSent, jnxPPPoECompliances=jnxPPPoECompliances, jnxPPPoEServiceNameTable=jnxPPPoEServiceNameTable, jnxPPPoEIfStatsRxPADR=jnxPPPoEIfStatsRxPADR, jnxPPPoEServiceNameAciAriAction=jnxPPPoEServiceNameAciAriAction, jnxPPPoEServiceNameAgentCircuitId=jnxPPPoEServiceNameAgentCircuitId, jnxPPPoEIfMtu=jnxPPPoEIfMtu, jnxPPPoEServiceNameAgentRemoteId=jnxPPPoEServiceNameAgentRemoteId, jnxPPPoEIfLockoutMax=jnxPPPoEIfLockoutMax, jnxPppoeSubIfPerQueueStatsEntry=jnxPppoeSubIfPerQueueStatsEntry, jnxPPPoESummarySubIfAdminDown=jnxPPPoESummarySubIfAdminDown, jnxPPPoEIfStatsRxInvTags=jnxPPPoEIfStatsRxInvTags, jnxPPPoEIfStatsRxInvSession=jnxPPPoEIfStatsRxInvSession, jnxPPPoESubIfId=jnxPPPoESubIfId, jnxPPPoEServices=jnxPPPoEServices, jnxPPPoEIfStatsRxInvLength=jnxPPPoEIfStatsRxInvLength, jnxPPPoESubIfIndex=jnxPPPoESubIfIndex, jnxPPPoESubIfUrl=jnxPPPoESubIfUrl, jnxPPPoEIfServiceNameTable=jnxPPPoEIfServiceNameTable, jnxPPPoESummarySubIfAdminUp=jnxPPPoESummarySubIfAdminUp, jnxPPPoEIfStatsTxPADS=jnxPPPoEIfStatsTxPADS, jnxPPPoEIfDupProtect=jnxPPPoEIfDupProtect, jnxPPPoEIfLockoutNextTime=jnxPPPoEIfLockoutNextTime, jnxPPPoEServiceNameTableEntry=jnxPPPoEServiceNameTableEntry, jnxPPPoESummarySubIfOperDown=jnxPPPoESummarySubIfOperDown, jnxPPPoEIfLockoutEntry=jnxPPPoEIfLockoutEntry, jnxPPPoEServiceNameEntry=jnxPPPoEServiceNameEntry, jnxPPPoEIfStatsRxInvTypes=jnxPPPoEIfStatsRxInvTypes, jnxPPPoEIfStatsRxInsufficientResources=jnxPPPoEIfStatsRxInsufficientResources, jnxPPPoEServiceNameMaxSessions=jnxPPPoEServiceNameMaxSessions, jnxPPPoESubIfSessionId=jnxPPPoESubIfSessionId)