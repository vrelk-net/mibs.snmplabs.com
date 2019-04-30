#
# PySNMP MIB module DOCS-CABLE-DEVICE-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DOCS-CABLE-DEVICE-TRAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:37:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
docsDevEvId, docsDevEvLevel, docsDevSwFilename, docsDevNotification, docsDev, docsDevServerTime, docsDevSwServer, docsDevServerDhcp, docsDevEvText = mibBuilder.importSymbols("DOCS-CABLE-DEVICE-MIB", "docsDevEvId", "docsDevEvLevel", "docsDevSwFilename", "docsDevNotification", "docsDev", "docsDevServerTime", "docsDevSwServer", "docsDevServerDhcp", "docsDevEvText")
docsIfCmtsCmStatusDocsisMode, docsIfDocsisOperMode, docsIfDocsisCapability = mibBuilder.importSymbols("DOCS-IF-EXT-MIB", "docsIfCmtsCmStatusDocsisMode", "docsIfDocsisOperMode", "docsIfDocsisCapability")
docsIfCmtsCmStatusMacAddress, docsIfCmCmtsAddress = mibBuilder.importSymbols("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress", "docsIfCmCmtsAddress")
ifPhysAddress, = mibBuilder.importSymbols("IF-MIB", "ifPhysAddress")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Unsigned32, MibIdentifier, ModuleIdentity, Counter64, NotificationType, Counter32, ObjectIdentity, IpAddress, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibIdentifier", "ModuleIdentity", "Counter64", "NotificationType", "Counter32", "ObjectIdentity", "IpAddress", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
docsDevTrapMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 69, 10))
if mibBuilder.loadTexts: docsDevTrapMIB.setLastUpdated('000926000000Z')
if mibBuilder.loadTexts: docsDevTrapMIB.setOrganization('Cisco Systems, Inc.')
docsDevTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 69, 2, 1))
docsDevTrapControl = MibIdentifier((1, 3, 6, 1, 2, 1, 69, 2, 1, 1))
docsDevCmTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0))
docsDevCmtsTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 69, 2, 1, 3, 0))
docsDevCmTrapControl = MibScalar((1, 3, 6, 1, 2, 1, 69, 2, 1, 1, 1), Bits().clone(namedValues=NamedValues(("cmInitTLVUnknownTrap", 0), ("cmDynServReqFailTrap", 1), ("cmDynServRspFailTrap", 2), ("cmDynServAckFailTrap", 3), ("cmBpiInitTrap", 4), ("cmBPKMTrap", 5), ("cmDynamicSATrap", 6), ("cmDHCPFailTrap", 7), ("cmSwUpgradeInitTrap", 8), ("cmSwUpgradeFailTrap", 9), ("cmSwUpgradeSuccessTrap", 10), ("cmSwUpgradeCVCTrap", 11), ("cmTODFailTrap", 12), ("cmDCCReqFailTrap", 13), ("cmDCCRspFailTrap", 14), ("cmDCCAckFailTrap", 15)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsDevCmTrapControl.setStatus('current')
docsDevCmtsTrapControl = MibScalar((1, 3, 6, 1, 2, 1, 69, 2, 1, 1, 2), Bits().clone(namedValues=NamedValues(("cmtsInitRegReqFailTrap", 0), ("cmtsInitRegRspFailTrap", 1), ("cmtsInitRegAckFailTrap", 2), ("cmtsDynServReqFailTrap", 3), ("cmtsDynServRspFailTrap", 4), ("cmtsDynServAckFailTrap", 5), ("cmtsBpiInitTrap", 6), ("cmtsBPKMTrap", 7), ("cmtsDynamicSATrap", 8), ("cmtsDCCReqFailTrap", 9), ("cmtsDCCRspFailTrap", 10), ("cmtsDCCAckFailTrap", 11)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: docsDevCmtsTrapControl.setStatus('current')
docsDevCmInitTLVUnknownTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 1)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"), ("IF-MIB", "ifPhysAddress"), ("DOCS-IF-MIB", "docsIfCmCmtsAddress"))
if mibBuilder.loadTexts: docsDevCmInitTLVUnknownTrap.setStatus('current')
docsDevCmDynServReqFailTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 2)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"), ("IF-MIB", "ifPhysAddress"), ("DOCS-IF-MIB", "docsIfCmCmtsAddress"))
if mibBuilder.loadTexts: docsDevCmDynServReqFailTrap.setStatus('current')
docsDevCmDynServRspFailTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 3)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"), ("IF-MIB", "ifPhysAddress"), ("DOCS-IF-MIB", "docsIfCmCmtsAddress"))
if mibBuilder.loadTexts: docsDevCmDynServRspFailTrap.setStatus('current')
docsDevCmDynServAckFailTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 4)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"), ("IF-MIB", "ifPhysAddress"), ("DOCS-IF-MIB", "docsIfCmCmtsAddress"))
if mibBuilder.loadTexts: docsDevCmDynServAckFailTrap.setStatus('current')
docsDevCmBpiInitTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 5)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"), ("IF-MIB", "ifPhysAddress"), ("DOCS-IF-MIB", "docsIfCmCmtsAddress"))
if mibBuilder.loadTexts: docsDevCmBpiInitTrap.setStatus('current')
docsDevCmBPKMTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 6)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"), ("IF-MIB", "ifPhysAddress"), ("DOCS-IF-MIB", "docsIfCmCmtsAddress"))
if mibBuilder.loadTexts: docsDevCmBPKMTrap.setStatus('current')
docsDevCmDynamicSATrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 7)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"), ("IF-MIB", "ifPhysAddress"), ("DOCS-IF-MIB", "docsIfCmCmtsAddress"))
if mibBuilder.loadTexts: docsDevCmDynamicSATrap.setStatus('current')
docsDevCmDHCPFailTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 8)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"), ("IF-MIB", "ifPhysAddress"), ("DOCS-IF-MIB", "docsIfCmCmtsAddress"), ("DOCS-CABLE-DEVICE-MIB", "docsDevServerDhcp"))
if mibBuilder.loadTexts: docsDevCmDHCPFailTrap.setStatus('current')
docsDevCmSwUpgradeInitTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 9)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"), ("IF-MIB", "ifPhysAddress"), ("DOCS-IF-MIB", "docsIfCmCmtsAddress"), ("DOCS-CABLE-DEVICE-MIB", "docsDevSwFilename"), ("DOCS-CABLE-DEVICE-MIB", "docsDevSwServer"))
if mibBuilder.loadTexts: docsDevCmSwUpgradeInitTrap.setStatus('current')
docsDevCmSwUpgradeFailTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 10)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"), ("IF-MIB", "ifPhysAddress"), ("DOCS-IF-MIB", "docsIfCmCmtsAddress"), ("DOCS-CABLE-DEVICE-MIB", "docsDevSwFilename"), ("DOCS-CABLE-DEVICE-MIB", "docsDevSwServer"))
if mibBuilder.loadTexts: docsDevCmSwUpgradeFailTrap.setStatus('current')
docsDevCmSwUpgradeSuccessTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 11)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"), ("IF-MIB", "ifPhysAddress"), ("DOCS-IF-MIB", "docsIfCmCmtsAddress"), ("DOCS-CABLE-DEVICE-MIB", "docsDevSwFilename"), ("DOCS-CABLE-DEVICE-MIB", "docsDevSwServer"))
if mibBuilder.loadTexts: docsDevCmSwUpgradeSuccessTrap.setStatus('current')
docsDevCmSwUpgradeCVCFailTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 12)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"), ("IF-MIB", "ifPhysAddress"), ("DOCS-IF-MIB", "docsIfCmCmtsAddress"))
if mibBuilder.loadTexts: docsDevCmSwUpgradeCVCFailTrap.setStatus('current')
docsDevCmTODFailTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 13)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"), ("IF-MIB", "ifPhysAddress"), ("DOCS-IF-MIB", "docsIfCmCmtsAddress"), ("DOCS-CABLE-DEVICE-MIB", "docsDevServerTime"))
if mibBuilder.loadTexts: docsDevCmTODFailTrap.setStatus('current')
docsDevCmDCCReqFailTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 14)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"), ("IF-MIB", "ifPhysAddress"), ("DOCS-IF-MIB", "docsIfCmCmtsAddress"))
if mibBuilder.loadTexts: docsDevCmDCCReqFailTrap.setStatus('current')
docsDevCmDCCRspFailTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 15)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"), ("IF-MIB", "ifPhysAddress"), ("DOCS-IF-MIB", "docsIfCmCmtsAddress"))
if mibBuilder.loadTexts: docsDevCmDCCRspFailTrap.setStatus('current')
docsDevCmDCCAckFailTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 0, 16)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"), ("IF-MIB", "ifPhysAddress"), ("DOCS-IF-MIB", "docsIfCmCmtsAddress"))
if mibBuilder.loadTexts: docsDevCmDCCAckFailTrap.setStatus('current')
docsDevCmtsInitRegReqFailTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 3, 0, 1)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfCmtsCmStatusDocsisMode"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("IF-MIB", "ifPhysAddress"))
if mibBuilder.loadTexts: docsDevCmtsInitRegReqFailTrap.setStatus('current')
docsDevCmtsInitRegRspFailTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 3, 0, 2)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfCmtsCmStatusDocsisMode"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("IF-MIB", "ifPhysAddress"))
if mibBuilder.loadTexts: docsDevCmtsInitRegRspFailTrap.setStatus('current')
docsDevCmtsInitRegAckFailTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 3, 0, 3)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfCmtsCmStatusDocsisMode"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("IF-MIB", "ifPhysAddress"))
if mibBuilder.loadTexts: docsDevCmtsInitRegAckFailTrap.setStatus('current')
docsDevCmtsDynServReqFailTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 3, 0, 4)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfCmtsCmStatusDocsisMode"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("IF-MIB", "ifPhysAddress"))
if mibBuilder.loadTexts: docsDevCmtsDynServReqFailTrap.setStatus('current')
docsDevCmtsDynServRspFailTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 3, 0, 5)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfCmtsCmStatusDocsisMode"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("IF-MIB", "ifPhysAddress"))
if mibBuilder.loadTexts: docsDevCmtsDynServRspFailTrap.setStatus('current')
docsDevCmtsDynServAckFailTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 3, 0, 6)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfCmtsCmStatusDocsisMode"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("IF-MIB", "ifPhysAddress"))
if mibBuilder.loadTexts: docsDevCmtsDynServAckFailTrap.setStatus('current')
docsDevCmtsBpiInitTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 3, 0, 7)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfCmtsCmStatusDocsisMode"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("IF-MIB", "ifPhysAddress"))
if mibBuilder.loadTexts: docsDevCmtsBpiInitTrap.setStatus('current')
docsDevCmtsBPKMTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 3, 0, 8)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfCmtsCmStatusDocsisMode"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("IF-MIB", "ifPhysAddress"))
if mibBuilder.loadTexts: docsDevCmtsBPKMTrap.setStatus('current')
docsDevCmtsDynamicSATrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 3, 0, 9)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfCmtsCmStatusDocsisMode"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("IF-MIB", "ifPhysAddress"))
if mibBuilder.loadTexts: docsDevCmtsDynamicSATrap.setStatus('current')
docsDevCmtsDCCReqFailTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 3, 0, 10)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfCmtsCmStatusDocsisMode"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("IF-MIB", "ifPhysAddress"))
if mibBuilder.loadTexts: docsDevCmtsDCCReqFailTrap.setStatus('current')
docsDevCmtsDCCRspFailTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 3, 0, 11)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfCmtsCmStatusDocsisMode"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("IF-MIB", "ifPhysAddress"))
if mibBuilder.loadTexts: docsDevCmtsDCCRspFailTrap.setStatus('current')
docsDevCmtsDCCAckFailTrap = NotificationType((1, 3, 6, 1, 2, 1, 69, 2, 1, 3, 0, 12)).setObjects(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"), ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"), ("DOCS-IF-EXT-MIB", "docsIfCmtsCmStatusDocsisMode"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"), ("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("IF-MIB", "ifPhysAddress"))
if mibBuilder.loadTexts: docsDevCmtsDCCAckFailTrap.setStatus('current')
docsDevTrapConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 69, 2, 1, 2))
docsDevTrapGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 1))
docsDevTrapCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 2))
docsDevCmTrapCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 2, 1)).setObjects(("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmTrapControlGroup"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsDevCmTrapCompliance = docsDevCmTrapCompliance.setStatus('current')
docsDevCmTrapControlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 1, 1)).setObjects(("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmTrapControl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsDevCmTrapControlGroup = docsDevCmTrapControlGroup.setStatus('current')
docsDevCmNotificationGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 1, 2)).setObjects(("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmInitTLVUnknownTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmDynServReqFailTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmDynServRspFailTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmDynServAckFailTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmBpiInitTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmBPKMTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmDynamicSATrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmDHCPFailTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmSwUpgradeInitTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmSwUpgradeFailTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmSwUpgradeSuccessTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmSwUpgradeCVCFailTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmTODFailTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmDCCReqFailTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmDCCRspFailTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmDCCAckFailTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsDevCmNotificationGroup = docsDevCmNotificationGroup.setStatus('current')
docsDevCmtsTrapCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 2, 2)).setObjects(("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmtsTrapControlGroup"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmtsNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsDevCmtsTrapCompliance = docsDevCmtsTrapCompliance.setStatus('current')
docsDevCmtsTrapControlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 1, 3)).setObjects(("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmtsTrapControl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsDevCmtsTrapControlGroup = docsDevCmtsTrapControlGroup.setStatus('current')
docsDevCmtsNotificationGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 69, 2, 1, 2, 1, 4)).setObjects(("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmtsInitRegReqFailTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmtsInitRegRspFailTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmtsInitRegAckFailTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmtsDynServReqFailTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmtsDynServRspFailTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmtsDynServAckFailTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmtsBpiInitTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmtsBPKMTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmtsDynamicSATrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmtsDCCReqFailTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmtsDCCRspFailTrap"), ("DOCS-CABLE-DEVICE-TRAP-MIB", "docsDevCmtsDCCAckFailTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsDevCmtsNotificationGroup = docsDevCmtsNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("DOCS-CABLE-DEVICE-TRAP-MIB", docsDevCmBpiInitTrap=docsDevCmBpiInitTrap, docsDevCmDHCPFailTrap=docsDevCmDHCPFailTrap, docsDevCmTODFailTrap=docsDevCmTODFailTrap, docsDevCmtsNotificationGroup=docsDevCmtsNotificationGroup, docsDevCmDCCAckFailTrap=docsDevCmDCCAckFailTrap, docsDevCmInitTLVUnknownTrap=docsDevCmInitTLVUnknownTrap, docsDevCmtsInitRegAckFailTrap=docsDevCmtsInitRegAckFailTrap, docsDevTrapCompliances=docsDevTrapCompliances, docsDevCmTrapControlGroup=docsDevCmTrapControlGroup, docsDevCmSwUpgradeInitTrap=docsDevCmSwUpgradeInitTrap, docsDevCmtsBPKMTrap=docsDevCmtsBPKMTrap, docsDevCmtsDynServRspFailTrap=docsDevCmtsDynServRspFailTrap, docsDevTrapGroups=docsDevTrapGroups, docsDevCmDCCRspFailTrap=docsDevCmDCCRspFailTrap, docsDevTrapConformance=docsDevTrapConformance, docsDevCmtsInitRegRspFailTrap=docsDevCmtsInitRegRspFailTrap, docsDevCmDynServAckFailTrap=docsDevCmDynServAckFailTrap, docsDevCmtsTraps=docsDevCmtsTraps, docsDevCmtsDynamicSATrap=docsDevCmtsDynamicSATrap, docsDevCmNotificationGroup=docsDevCmNotificationGroup, docsDevCmtsBpiInitTrap=docsDevCmtsBpiInitTrap, docsDevCmTrapCompliance=docsDevCmTrapCompliance, docsDevTraps=docsDevTraps, docsDevCmtsInitRegReqFailTrap=docsDevCmtsInitRegReqFailTrap, docsDevCmTraps=docsDevCmTraps, PYSNMP_MODULE_ID=docsDevTrapMIB, docsDevCmtsDCCRspFailTrap=docsDevCmtsDCCRspFailTrap, docsDevTrapControl=docsDevTrapControl, docsDevCmTrapControl=docsDevCmTrapControl, docsDevCmDynamicSATrap=docsDevCmDynamicSATrap, docsDevCmtsDCCReqFailTrap=docsDevCmtsDCCReqFailTrap, docsDevCmSwUpgradeSuccessTrap=docsDevCmSwUpgradeSuccessTrap, docsDevCmtsTrapControlGroup=docsDevCmtsTrapControlGroup, docsDevCmtsDynServReqFailTrap=docsDevCmtsDynServReqFailTrap, docsDevCmSwUpgradeCVCFailTrap=docsDevCmSwUpgradeCVCFailTrap, docsDevTrapMIB=docsDevTrapMIB, docsDevCmDCCReqFailTrap=docsDevCmDCCReqFailTrap, docsDevCmtsDynServAckFailTrap=docsDevCmtsDynServAckFailTrap, docsDevCmDynServRspFailTrap=docsDevCmDynServRspFailTrap, docsDevCmBPKMTrap=docsDevCmBPKMTrap, docsDevCmSwUpgradeFailTrap=docsDevCmSwUpgradeFailTrap, docsDevCmtsDCCAckFailTrap=docsDevCmtsDCCAckFailTrap, docsDevCmtsTrapCompliance=docsDevCmtsTrapCompliance, docsDevCmtsTrapControl=docsDevCmtsTrapControl, docsDevCmDynServReqFailTrap=docsDevCmDynServReqFailTrap)
