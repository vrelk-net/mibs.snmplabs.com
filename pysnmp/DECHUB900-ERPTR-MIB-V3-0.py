#
# PySNMP MIB module DECHUB900-ERPTR-MIB-V3-0 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DECHUB900-ERPTR-MIB-V3-0
# Produced by pysmi-0.3.4 at Mon Apr 29 18:22:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, TimeTicks, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter32, Integer32, ModuleIdentity, enterprises, iso, MibIdentifier, Counter64, Bits, NotificationType, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "TimeTicks", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter32", "Integer32", "ModuleIdentity", "enterprises", "iso", "MibIdentifier", "Counter64", "Bits", "NotificationType", "ObjectIdentity")
DisplayString, TextualConvention, PhysAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "PhysAddress")
dec = MibIdentifier((1, 3, 6, 1, 4, 1, 36))
ema = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2))
decMIBextension = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18))
decHub900 = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18, 11))
repeater = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5))
rptrVersion1 = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1))
rptrExtensions = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1))
erptrBasicPackage = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1))
erptrAddrDBPackage = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 2))
erptrDprPackage = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 3))
erptrSecurityPackage = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4))
erptrMauPackage = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 5))
erptrAddrLearnPackage = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 6))
erptrMonitorPackage = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 7))
erptrRptrInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 1))
erptrGroupInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 2))
erptrPortInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 3))
erptrAddrDBRptrInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 2, 1))
erptrAddrDBGroupInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 2, 2))
erptrAddrDBPortInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 2, 3))
erptrDprRptrInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 3, 1))
erptrDprGroupInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 3, 2))
erptrDprPortInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 3, 3))
erptrSecurityRptrInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 1))
erptrSecurityGroupInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 2))
erptrSecurityPortInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 3))
erptrMauRptrInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 5, 1))
erptrMauGroupInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 5, 2))
erptrMauPortInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 5, 3))
erptrAddrLearnRptrInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 6, 1))
erptrAddrLearnGroupInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 6, 2))
erptrAddrLearnPortInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 6, 3))
erptrMonitorRptrInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 7, 1))
erptrMonitorGroupInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 7, 2))
erptrMonitorPortInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 7, 3))
erptrAutoPartitionAlg = MibScalar((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("standard", 1), ("enhanced", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: erptrAutoPartitionAlg.setStatus('mandatory')
erptrAutoPartitionReconnectAlg = MibScalar((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("standard", 1), ("txOnly", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: erptrAutoPartitionReconnectAlg.setStatus('mandatory')
erptrJamBits = MibScalar((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("jb96", 1), ("jb128", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: erptrJamBits.setStatus('mandatory')
erptrHealthTextChanges = MibScalar((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrHealthTextChanges.setStatus('mandatory')
erptrTotalPortEvents = MibScalar((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrTotalPortEvents.setStatus('mandatory')
erptrTotalRptrErrors = MibScalar((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrTotalRptrErrors.setStatus('mandatory')
erptrJabberProtectionAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: erptrJabberProtectionAdminStatus.setStatus('mandatory')
erptrTotalPorts = MibScalar((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrTotalPorts.setStatus('mandatory')
erptrPMDCarrierCardType = MibScalar((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unknown", 1), ("type10Base", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrPMDCarrierCardType.setStatus('mandatory')
erptrGroupTable = MibTable((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 2, 1), )
if mibBuilder.loadTexts: erptrGroupTable.setStatus('mandatory')
erptrGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 2, 1, 1), ).setIndexNames((0, "DECHUB900-ERPTR-MIB-V3-0", "erptrGroupIndex"))
if mibBuilder.loadTexts: erptrGroupEntry.setStatus('mandatory')
erptrGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrGroupIndex.setStatus('mandatory')
erptrGroupTransmitCollisions = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrGroupTransmitCollisions.setStatus('mandatory')
erptrGroupReset = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noReset", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: erptrGroupReset.setStatus('mandatory')
erptrGroupLanTotalOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrGroupLanTotalOctets.setStatus('mandatory')
erptrPortTable = MibTable((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 3, 1), )
if mibBuilder.loadTexts: erptrPortTable.setStatus('mandatory')
erptrPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 3, 1, 1), ).setIndexNames((0, "DECHUB900-ERPTR-MIB-V3-0", "erptrPortGroupIndex"), (0, "DECHUB900-ERPTR-MIB-V3-0", "erptrPortIndex"))
if mibBuilder.loadTexts: erptrPortEntry.setStatus('mandatory')
erptrPortGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrPortGroupIndex.setStatus('mandatory')
erptrPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrPortIndex.setStatus('mandatory')
erptrPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 3, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: erptrPortName.setStatus('mandatory')
erptrPortPartitions = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrPortPartitions.setStatus('mandatory')
erptrPortPartitionReason = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("unknown", 1), ("notPartitioned", 2), ("managementPartitioned", 3), ("excessiveCollision", 4), ("excessiveCollisionAndMgmtPart", 5), ("consecutiveCollisions", 6), ("consecutiveCollisionsAndMgmtPart", 7), ("jabber", 8), ("jabberAndMgmtPart", 9), ("noCarrierLoopback", 10), ("noCarrierLoopbackandMgmtPart", 11), ("transmitCarrierDropout", 12), ("transmitCarrierDropoutAndMgmtPart", 13), ("forcedReconnection", 14)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrPortPartitionReason.setStatus('mandatory')
erptrPortMAUType = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("unknown", 1), ("typeAUI", 2), ("type10Base5", 3), ("typeFoirl", 4), ("type10Base2", 5), ("type10BaseT", 6), ("type10BaseFP", 7), ("type10BaseFB", 8), ("type10BaseFL", 9), ("typeTelco10BaseT", 10), ("typeBackplaneThinwire", 11), ("typeRAUI", 12)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrPortMAUType.setStatus('mandatory')
erptrPortSQETestError = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 1, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("sqeTestDetected", 2), ("sqeTestNotDetected", 3), ("sqeTestMasked", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrPortSQETestError.setStatus('mandatory')
erptrAddrDBTableCapacity = MibScalar((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrAddrDBTableCapacity.setStatus('mandatory')
erptrAddrDBPortAddrTable = MibTable((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 2, 3, 1), )
if mibBuilder.loadTexts: erptrAddrDBPortAddrTable.setStatus('mandatory')
erptrAddrDBPortAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 2, 3, 1, 1), ).setIndexNames((0, "DECHUB900-ERPTR-MIB-V3-0", "erptrAddrDBPortPhyAddr"))
if mibBuilder.loadTexts: erptrAddrDBPortAddrEntry.setStatus('mandatory')
erptrAddrDBPortPhyAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 2, 3, 1, 1, 1), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrAddrDBPortPhyAddr.setStatus('mandatory')
erptrAddrDBPortGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 2, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrAddrDBPortGroupIndex.setStatus('mandatory')
erptrAddrDBPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 2, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrAddrDBPortIndex.setStatus('mandatory')
erptrDprTotalStateChanges = MibScalar((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrDprTotalStateChanges.setStatus('mandatory')
erptrDprLinkTable = MibTable((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 3, 3, 1), )
if mibBuilder.loadTexts: erptrDprLinkTable.setStatus('mandatory')
erptrDprLinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 3, 3, 1, 1), ).setIndexNames((0, "DECHUB900-ERPTR-MIB-V3-0", "erptrDprLinkGroupIndex"), (0, "DECHUB900-ERPTR-MIB-V3-0", "erptrDprLinkPortIndex"))
if mibBuilder.loadTexts: erptrDprLinkEntry.setStatus('mandatory')
erptrDprLinkGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 3, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrDprLinkGroupIndex.setStatus('mandatory')
erptrDprLinkPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 3, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrDprLinkPortIndex.setStatus('mandatory')
erptrDprLinkType = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 3, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("redundantMaster", 1), ("redundantResponder", 2))).clone('redundantResponder')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: erptrDprLinkType.setStatus('mandatory')
erptrDprLinkToggle = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 3, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noToggle", 1), ("toggle", 2))).clone('noToggle')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: erptrDprLinkToggle.setStatus('mandatory')
erptrDprLinkOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 3, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("redundancyNotOperational", 1), ("masterPrimaryActive", 2), ("masterPrimaryStandby", 3), ("masterPrimaryLinkFailure", 4), ("responderOk", 5), ("responderLinkFailure", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrDprLinkOperStatus.setStatus('mandatory')
erptrDprSecondaryGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 3, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: erptrDprSecondaryGroupIndex.setStatus('mandatory')
erptrDprSecondaryPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 3, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: erptrDprSecondaryPortIndex.setStatus('mandatory')
erptrDprSecondaryOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 3, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("redundancyNotOperational", 1), ("masterSecondaryActive", 2), ("masterSecondaryStandby", 3), ("masterSecondaryLinkFailure", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrDprSecondaryOperStatus.setStatus('mandatory')
erptrDprLinkName = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 3, 3, 1, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: erptrDprLinkName.setStatus('mandatory')
erptrDprLinkStateChanges = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 3, 3, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrDprLinkStateChanges.setStatus('mandatory')
erptrDprLinkEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 3, 3, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("valid", 1), ("createRequest", 2), ("underCreation", 3), ("invalid", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: erptrDprLinkEntryStatus.setStatus('mandatory')
erptrSecurityRptrSecurityViolations = MibScalar((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrSecurityRptrSecurityViolations.setStatus('mandatory')
erptrSecurityRptrLogTable = MibTable((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 1, 2), )
if mibBuilder.loadTexts: erptrSecurityRptrLogTable.setStatus('mandatory')
erptrSecurityRptrLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 1, 2, 1), ).setIndexNames((0, "DECHUB900-ERPTR-MIB-V3-0", "erptrSecurityRptrLogIndex"))
if mibBuilder.loadTexts: erptrSecurityRptrLogEntry.setStatus('mandatory')
erptrSecurityRptrLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrSecurityRptrLogIndex.setStatus('mandatory')
erptrSecurityRptrLogGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrSecurityRptrLogGroupIndex.setStatus('mandatory')
erptrSecurityRptrLogPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrSecurityRptrLogPortIndex.setStatus('mandatory')
erptrSecurityRptrLogTime = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 1, 2, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrSecurityRptrLogTime.setStatus('mandatory')
erptrSecurityRptrLogPhysAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 1, 2, 1, 5), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrSecurityRptrLogPhysAddress.setStatus('mandatory')
erptrSecurityRptrLogCapacity = MibScalar((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrSecurityRptrLogCapacity.setStatus('mandatory')
erptrSecurityPortCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 3, 1), )
if mibBuilder.loadTexts: erptrSecurityPortCtrlTable.setStatus('mandatory')
erptrSecurityPortCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 3, 1, 1), ).setIndexNames((0, "DECHUB900-ERPTR-MIB-V3-0", "erptrSecurityPortCtrlGroupIndex"), (0, "DECHUB900-ERPTR-MIB-V3-0", "erptrSecurityPortCtrlPortIndex"))
if mibBuilder.loadTexts: erptrSecurityPortCtrlEntry.setStatus('mandatory')
erptrSecurityPortCtrlGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrSecurityPortCtrlGroupIndex.setStatus('mandatory')
erptrSecurityPortCtrlPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrSecurityPortCtrlPortIndex.setStatus('mandatory')
erptrSecurityPortCtrlEavesdropMode = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: erptrSecurityPortCtrlEavesdropMode.setStatus('mandatory')
erptrSecurityPortCtrlIntrusionMode = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("disabled", 1), ("notifyOnly", 2), ("jamUnauthPackets", 3), ("disablePort", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: erptrSecurityPortCtrlIntrusionMode.setStatus('mandatory')
erptrSecurityPortCtrlOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("securityOperational", 1), ("securityNotOperational", 2), ("violationPortDisabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrSecurityPortCtrlOperStatus.setStatus('mandatory')
erptrSecurityPortCtrlViolations = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 3, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrSecurityPortCtrlViolations.setStatus('mandatory')
erptrSecurityPortAddrTable = MibTable((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 3, 2), )
if mibBuilder.loadTexts: erptrSecurityPortAddrTable.setStatus('mandatory')
erptrSecurityPortAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 3, 2, 1), ).setIndexNames((0, "DECHUB900-ERPTR-MIB-V3-0", "erptrSecurityPortAddrGroupIndex"), (0, "DECHUB900-ERPTR-MIB-V3-0", "erptrSecurityPortAddrPortIndex"), (0, "DECHUB900-ERPTR-MIB-V3-0", "erptrSecurityPortAddrPhysAddress"))
if mibBuilder.loadTexts: erptrSecurityPortAddrEntry.setStatus('mandatory')
erptrSecurityPortAddrGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: erptrSecurityPortAddrGroupIndex.setStatus('mandatory')
erptrSecurityPortAddrPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: erptrSecurityPortAddrPortIndex.setStatus('mandatory')
erptrSecurityPortAddrPhysAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 3, 2, 1, 3), PhysAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: erptrSecurityPortAddrPhysAddress.setStatus('mandatory')
erptrSecurityPortAddrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 4, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("valid", 1), ("createRequest", 2), ("underCreation", 3), ("invalid", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: erptrSecurityPortAddrStatus.setStatus('mandatory')
erptrMauTotalMediaUnavailable = MibScalar((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 5, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrMauTotalMediaUnavailable.setStatus('mandatory')
erptrMauTable = MibTable((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 5, 3, 1), )
if mibBuilder.loadTexts: erptrMauTable.setStatus('mandatory')
erptrMauEntry = MibTableRow((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 5, 3, 1, 1), ).setIndexNames((0, "DECHUB900-ERPTR-MIB-V3-0", "erptrMauGroupIndex"), (0, "DECHUB900-ERPTR-MIB-V3-0", "erptrMauPortIndex"), (0, "DECHUB900-ERPTR-MIB-V3-0", "erptrMauIndex"))
if mibBuilder.loadTexts: erptrMauEntry.setStatus('mandatory')
erptrMauGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 5, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrMauGroupIndex.setStatus('mandatory')
erptrMauPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 5, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrMauPortIndex.setStatus('mandatory')
erptrMauIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 5, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrMauIndex.setStatus('mandatory')
erptrMauLinkTestAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 5, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: erptrMauLinkTestAdminStatus.setStatus('mandatory')
erptrMauMediaPolarityStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 5, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("polarityNotReversed", 1), ("polarityReversed", 2), ("polarityCorrected", 3), ("unknown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrMauMediaPolarityStatus.setStatus('mandatory')
erptrMauMediaAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 5, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("unknown", 2), ("available", 3), ("notAvailable", 4), ("remoteFault", 5), ("invalidSignal", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrMauMediaAvailable.setStatus('mandatory')
erptrMauMediaAvailableChanges = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 5, 3, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrMauMediaAvailableChanges.setStatus('mandatory')
erptrMauMaxLinkLength = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 5, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("standard", 1), ("extended", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: erptrMauMaxLinkLength.setStatus('mandatory')
erptrAddrLearnPortCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 6, 3, 1), )
if mibBuilder.loadTexts: erptrAddrLearnPortCtrlTable.setStatus('mandatory')
erptrAddrLearnPortCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 6, 3, 1, 1), ).setIndexNames((0, "DECHUB900-ERPTR-MIB-V3-0", "erptrAddrLearnPortCtrlGroupIndex"), (0, "DECHUB900-ERPTR-MIB-V3-0", "erptrAddrLearnPortCtrlPortIndex"))
if mibBuilder.loadTexts: erptrAddrLearnPortCtrlEntry.setStatus('mandatory')
erptrAddrLearnPortCtrlGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 6, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrAddrLearnPortCtrlGroupIndex.setStatus('mandatory')
erptrAddrLearnPortCtrlPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 6, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrAddrLearnPortCtrlPortIndex.setStatus('mandatory')
erptrAddrLearnPortCtrlCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 6, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrAddrLearnPortCtrlCapacity.setStatus('mandatory')
erptrAddrLearnPortCtrlAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 6, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("enableLearning", 2), ("disableLearning", 3), ("clearLearnedAddresses", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: erptrAddrLearnPortCtrlAdminStatus.setStatus('mandatory')
erptrAddrLearnPortCtrlOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 6, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("learningEnabledAndActive", 1), ("learningEnabledAndStopped", 2), ("learningDisabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrAddrLearnPortCtrlOperStatus.setStatus('mandatory')
erptrAddrLearnPortAddressTable = MibTable((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 6, 3, 2), )
if mibBuilder.loadTexts: erptrAddrLearnPortAddressTable.setStatus('mandatory')
erptrAddrLearnPortAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 6, 3, 2, 1), ).setIndexNames((0, "DECHUB900-ERPTR-MIB-V3-0", "erptrAddrLearnPortAddressGroupIndex"), (0, "DECHUB900-ERPTR-MIB-V3-0", "erptrAddrLearnPortAddressPortIndex"), (0, "DECHUB900-ERPTR-MIB-V3-0", "erptrAddrLearnPortAddressIndex"))
if mibBuilder.loadTexts: erptrAddrLearnPortAddressEntry.setStatus('mandatory')
erptrAddrLearnPortAddressGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 6, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrAddrLearnPortAddressGroupIndex.setStatus('mandatory')
erptrAddrLearnPortAddressPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 6, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrAddrLearnPortAddressPortIndex.setStatus('mandatory')
erptrAddrLearnPortAddressIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 6, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrAddrLearnPortAddressIndex.setStatus('mandatory')
erptrAddrLearnPortAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 6, 3, 2, 1, 4), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrAddrLearnPortAddress.setStatus('mandatory')
erptrMonitorPortTable = MibTable((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 7, 3, 1), )
if mibBuilder.loadTexts: erptrMonitorPortTable.setStatus('mandatory')
erptrMonitorPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 7, 3, 1, 1), ).setIndexNames((0, "DECHUB900-ERPTR-MIB-V3-0", "erptrMonitorPortGroupIndex"), (0, "DECHUB900-ERPTR-MIB-V3-0", "erptrMonitorPortIndex"))
if mibBuilder.loadTexts: erptrMonitorPortEntry.setStatus('mandatory')
erptrMonitorPortGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 7, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrMonitorPortGroupIndex.setStatus('mandatory')
erptrMonitorPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 7, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrMonitorPortIndex.setStatus('mandatory')
erptrMonitorPortMulticastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 7, 3, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrMonitorPortMulticastFrames.setStatus('mandatory')
erptrMonitorPortBroadcastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 5, 1, 1, 7, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: erptrMonitorPortBroadcastFrames.setStatus('mandatory')
mibBuilder.exportSymbols("DECHUB900-ERPTR-MIB-V3-0", erptrPortInfo=erptrPortInfo, erptrAddrLearnGroupInfo=erptrAddrLearnGroupInfo, erptrRptrInfo=erptrRptrInfo, erptrGroupInfo=erptrGroupInfo, erptrGroupIndex=erptrGroupIndex, erptrAutoPartitionReconnectAlg=erptrAutoPartitionReconnectAlg, rptrVersion1=rptrVersion1, erptrMauMediaAvailable=erptrMauMediaAvailable, erptrAutoPartitionAlg=erptrAutoPartitionAlg, erptrSecurityPortCtrlEavesdropMode=erptrSecurityPortCtrlEavesdropMode, erptrAddrLearnPortAddressGroupIndex=erptrAddrLearnPortAddressGroupIndex, repeater=repeater, erptrDprLinkName=erptrDprLinkName, erptrSecurityPortAddrPortIndex=erptrSecurityPortAddrPortIndex, erptrGroupTransmitCollisions=erptrGroupTransmitCollisions, erptrTotalRptrErrors=erptrTotalRptrErrors, dec=dec, erptrPMDCarrierCardType=erptrPMDCarrierCardType, erptrDprSecondaryGroupIndex=erptrDprSecondaryGroupIndex, erptrMauIndex=erptrMauIndex, erptrJabberProtectionAdminStatus=erptrJabberProtectionAdminStatus, rptrExtensions=rptrExtensions, erptrHealthTextChanges=erptrHealthTextChanges, erptrAddrDBTableCapacity=erptrAddrDBTableCapacity, erptrSecurityGroupInfo=erptrSecurityGroupInfo, erptrMauMediaPolarityStatus=erptrMauMediaPolarityStatus, erptrMonitorPortTable=erptrMonitorPortTable, erptrSecurityPortAddrPhysAddress=erptrSecurityPortAddrPhysAddress, erptrSecurityRptrLogCapacity=erptrSecurityRptrLogCapacity, erptrAddrDBRptrInfo=erptrAddrDBRptrInfo, erptrMauPortInfo=erptrMauPortInfo, erptrPortPartitionReason=erptrPortPartitionReason, erptrGroupTable=erptrGroupTable, erptrSecurityPortCtrlOperStatus=erptrSecurityPortCtrlOperStatus, erptrGroupEntry=erptrGroupEntry, erptrAddrLearnRptrInfo=erptrAddrLearnRptrInfo, erptrAddrDBPortPhyAddr=erptrAddrDBPortPhyAddr, erptrSecurityPortAddrTable=erptrSecurityPortAddrTable, erptrPortEntry=erptrPortEntry, erptrMonitorPackage=erptrMonitorPackage, erptrPortTable=erptrPortTable, erptrAddrLearnPortCtrlEntry=erptrAddrLearnPortCtrlEntry, erptrMauMediaAvailableChanges=erptrMauMediaAvailableChanges, erptrDprLinkOperStatus=erptrDprLinkOperStatus, erptrAddrDBPackage=erptrAddrDBPackage, erptrJamBits=erptrJamBits, erptrMonitorPortEntry=erptrMonitorPortEntry, erptrSecurityRptrLogGroupIndex=erptrSecurityRptrLogGroupIndex, erptrDprLinkToggle=erptrDprLinkToggle, erptrAddrLearnPortAddressIndex=erptrAddrLearnPortAddressIndex, erptrSecurityRptrInfo=erptrSecurityRptrInfo, erptrDprGroupInfo=erptrDprGroupInfo, erptrMauGroupIndex=erptrMauGroupIndex, erptrDprPackage=erptrDprPackage, erptrAddrDBPortGroupIndex=erptrAddrDBPortGroupIndex, erptrAddrLearnPortCtrlGroupIndex=erptrAddrLearnPortCtrlGroupIndex, erptrMauTotalMediaUnavailable=erptrMauTotalMediaUnavailable, erptrSecurityPortAddrGroupIndex=erptrSecurityPortAddrGroupIndex, erptrAddrLearnPortAddressEntry=erptrAddrLearnPortAddressEntry, erptrSecurityRptrLogPortIndex=erptrSecurityRptrLogPortIndex, erptrMonitorPortIndex=erptrMonitorPortIndex, erptrDprSecondaryPortIndex=erptrDprSecondaryPortIndex, erptrBasicPackage=erptrBasicPackage, erptrMauPackage=erptrMauPackage, erptrMonitorPortInfo=erptrMonitorPortInfo, erptrAddrLearnPortInfo=erptrAddrLearnPortInfo, erptrMauTable=erptrMauTable, erptrMonitorRptrInfo=erptrMonitorRptrInfo, erptrPortSQETestError=erptrPortSQETestError, erptrPortIndex=erptrPortIndex, erptrSecurityPortInfo=erptrSecurityPortInfo, erptrAddrLearnPortAddressTable=erptrAddrLearnPortAddressTable, erptrPortPartitions=erptrPortPartitions, erptrAddrLearnPortCtrlAdminStatus=erptrAddrLearnPortCtrlAdminStatus, decHub900=decHub900, erptrAddrLearnPackage=erptrAddrLearnPackage, erptrMonitorPortMulticastFrames=erptrMonitorPortMulticastFrames, ema=ema, erptrAddrDBPortAddrTable=erptrAddrDBPortAddrTable, erptrMauRptrInfo=erptrMauRptrInfo, erptrSecurityPortCtrlGroupIndex=erptrSecurityPortCtrlGroupIndex, erptrSecurityPortCtrlEntry=erptrSecurityPortCtrlEntry, erptrSecurityPackage=erptrSecurityPackage, erptrDprTotalStateChanges=erptrDprTotalStateChanges, erptrAddrDBGroupInfo=erptrAddrDBGroupInfo, erptrPortGroupIndex=erptrPortGroupIndex, erptrMauMaxLinkLength=erptrMauMaxLinkLength, erptrAddrDBPortInfo=erptrAddrDBPortInfo, erptrMauGroupInfo=erptrMauGroupInfo, erptrSecurityRptrSecurityViolations=erptrSecurityRptrSecurityViolations, erptrSecurityPortCtrlViolations=erptrSecurityPortCtrlViolations, erptrGroupReset=erptrGroupReset, erptrSecurityRptrLogTime=erptrSecurityRptrLogTime, erptrAddrLearnPortCtrlOperStatus=erptrAddrLearnPortCtrlOperStatus, erptrTotalPortEvents=erptrTotalPortEvents, erptrAddrLearnPortCtrlTable=erptrAddrLearnPortCtrlTable, erptrDprLinkType=erptrDprLinkType, erptrDprLinkPortIndex=erptrDprLinkPortIndex, erptrSecurityRptrLogTable=erptrSecurityRptrLogTable, erptrSecurityPortAddrStatus=erptrSecurityPortAddrStatus, erptrDprLinkEntry=erptrDprLinkEntry, erptrAddrLearnPortCtrlPortIndex=erptrAddrLearnPortCtrlPortIndex, erptrAddrDBPortIndex=erptrAddrDBPortIndex, decMIBextension=decMIBextension, erptrSecurityPortCtrlPortIndex=erptrSecurityPortCtrlPortIndex, erptrMauEntry=erptrMauEntry, erptrSecurityRptrLogIndex=erptrSecurityRptrLogIndex, erptrMonitorGroupInfo=erptrMonitorGroupInfo, erptrDprLinkGroupIndex=erptrDprLinkGroupIndex, erptrMonitorPortBroadcastFrames=erptrMonitorPortBroadcastFrames, erptrPortMAUType=erptrPortMAUType, erptrDprRptrInfo=erptrDprRptrInfo, erptrAddrLearnPortAddress=erptrAddrLearnPortAddress, erptrAddrDBPortAddrEntry=erptrAddrDBPortAddrEntry, erptrMonitorPortGroupIndex=erptrMonitorPortGroupIndex, erptrDprLinkTable=erptrDprLinkTable, erptrSecurityPortCtrlIntrusionMode=erptrSecurityPortCtrlIntrusionMode, erptrGroupLanTotalOctets=erptrGroupLanTotalOctets, erptrDprLinkStateChanges=erptrDprLinkStateChanges, erptrMauLinkTestAdminStatus=erptrMauLinkTestAdminStatus, erptrSecurityRptrLogEntry=erptrSecurityRptrLogEntry, erptrSecurityRptrLogPhysAddress=erptrSecurityRptrLogPhysAddress, erptrDprPortInfo=erptrDprPortInfo, erptrSecurityPortAddrEntry=erptrSecurityPortAddrEntry, erptrAddrLearnPortCtrlCapacity=erptrAddrLearnPortCtrlCapacity, erptrTotalPorts=erptrTotalPorts, erptrPortName=erptrPortName, erptrDprLinkEntryStatus=erptrDprLinkEntryStatus, erptrSecurityPortCtrlTable=erptrSecurityPortCtrlTable, erptrDprSecondaryOperStatus=erptrDprSecondaryOperStatus, erptrMauPortIndex=erptrMauPortIndex, erptrAddrLearnPortAddressPortIndex=erptrAddrLearnPortAddressPortIndex)
