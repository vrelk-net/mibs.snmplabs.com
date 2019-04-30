#
# PySNMP MIB module XYLAN-IMA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XYLAN-IMA-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:38:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, TimeTicks, Counter64, Counter32, MibIdentifier, Unsigned32, iso, Bits, Gauge32, ModuleIdentity, IpAddress, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "TimeTicks", "Counter64", "Counter32", "MibIdentifier", "Unsigned32", "iso", "Bits", "Gauge32", "ModuleIdentity", "IpAddress", "Integer32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
xylanPportArch, = mibBuilder.importSymbols("XYLAN-BASE-MIB", "xylanPportArch")
xylanImaMib = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 11, 3))
xylanImaLinkTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 1), )
if mibBuilder.loadTexts: xylanImaLinkTable.setStatus('mandatory')
xylanImaLinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 1, 1), ).setIndexNames((0, "XYLAN-IMA-MIB", "xylanImaLinkSlotIndex"), (0, "XYLAN-IMA-MIB", "xylanImaLinkPortIndex"))
if mibBuilder.loadTexts: xylanImaLinkEntry.setStatus('mandatory')
xylanImaLinkSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanImaLinkSlotIndex.setStatus('mandatory')
xylanImaLinkPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanImaLinkPortIndex.setStatus('mandatory')
xylanImaLinkDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanImaLinkDescription.setStatus('mandatory')
xylanImaLinkAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanImaLinkAdminStatus.setStatus('mandatory')
xylanImaLinkIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanImaLinkIfIndex.setStatus('mandatory')
xylanImaLinkRxIcpCells = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanImaLinkRxIcpCells.setStatus('mandatory')
xylanImaLinkTxIcpCells = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanImaLinkTxIcpCells.setStatus('mandatory')
xylanImaLinkRxFillerCells = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanImaLinkRxFillerCells.setStatus('mandatory')
xylanImaLinkTxFillerCells = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanImaLinkTxFillerCells.setStatus('mandatory')
xylanImaLinkRxAtmLayerCells = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanImaLinkRxAtmLayerCells.setStatus('mandatory')
xylanImaLinkTxAtmLayerCells = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanImaLinkTxAtmLayerCells.setStatus('mandatory')
xylanImaLinkRxBadIcpCells = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanImaLinkRxBadIcpCells.setStatus('mandatory')
xylanImaLinkRxBadCrcIcpCells = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanImaLinkRxBadCrcIcpCells.setStatus('mandatory')
xylanImaLinkCellsInRxBuffer = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanImaLinkCellsInRxBuffer.setStatus('mandatory')
xylanImaLinkRxBufferFlush = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanImaLinkRxBufferFlush.setStatus('mandatory')
xylanImaLinkRxBufferOverflow = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 1, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanImaLinkRxBufferOverflow.setStatus('mandatory')
xylanImaLinkRxCellDiscarded = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 1, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanImaLinkRxCellDiscarded.setStatus('mandatory')
xylanImaLinkRxStuffEvents = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 1, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanImaLinkRxStuffEvents.setStatus('mandatory')
xylanImaLinkTxStuffEvents = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 1, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanImaLinkTxStuffEvents.setStatus('mandatory')
xylanImaLinkClearStatistics = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noAction", 1), ("clear", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanImaLinkClearStatistics.setStatus('mandatory')
xylanImaGroupTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 2), )
if mibBuilder.loadTexts: xylanImaGroupTable.setStatus('mandatory')
xylanImaGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 2, 1), ).setIndexNames((0, "XYLAN-IMA-MIB", "xylanImaGroupIndex"))
if mibBuilder.loadTexts: xylanImaGroupEntry.setStatus('mandatory')
xylanImaGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanImaGroupIndex.setStatus('mandatory')
xylanImaGroupDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanImaGroupDescription.setStatus('mandatory')
xylanImaGroupAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanImaGroupAdminStatus.setStatus('mandatory')
xylanImaGroupMaxDelaySlot = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanImaGroupMaxDelaySlot.setStatus('mandatory')
xylanImaGroupMaxDelayPort = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanImaGroupMaxDelayPort.setStatus('mandatory')
xylanImaGroupAtmLayerSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanImaGroupAtmLayerSlot.setStatus('mandatory')
xylanImaGroupAtmLayerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanImaGroupAtmLayerPort.setStatus('mandatory')
xylanImaGroupRxAtmLayerCells = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanImaGroupRxAtmLayerCells.setStatus('mandatory')
xylanImaGroupTxAtmLayerCells = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xylanImaGroupTxAtmLayerCells.setStatus('mandatory')
xylanImaGroupPhyFrameFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("esf", 2), ("sf", 3), ("e1", 4), ("e1-crc", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanImaGroupPhyFrameFormat.setStatus('mandatory')
xylanImaGroupPhyLoopbackMode = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("payloop", 2), ("line", 3), ("other", 4), ("inward", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanImaGroupPhyLoopbackMode.setStatus('mandatory')
xylanImaGroupPhyLineLength = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 2, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanImaGroupPhyLineLength.setStatus('mandatory')
xylanImaGroupPhyTxClkSource = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("loopTiming", 1), ("localTiming", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanImaGroupPhyTxClkSource.setStatus('mandatory')
xylanImaGroupClearStatistics = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noAction", 1), ("clear", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanImaGroupClearStatistics.setStatus('mandatory')
xylanImaGroupPhyUniqueParameter = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xylanImaGroupPhyUniqueParameter.setStatus('mandatory')
mibBuilder.exportSymbols("XYLAN-IMA-MIB", xylanImaLinkRxBadCrcIcpCells=xylanImaLinkRxBadCrcIcpCells, xylanImaLinkTable=xylanImaLinkTable, xylanImaGroupEntry=xylanImaGroupEntry, xylanImaGroupRxAtmLayerCells=xylanImaGroupRxAtmLayerCells, xylanImaLinkRxBadIcpCells=xylanImaLinkRxBadIcpCells, xylanImaLinkRxAtmLayerCells=xylanImaLinkRxAtmLayerCells, xylanImaLinkTxStuffEvents=xylanImaLinkTxStuffEvents, xylanImaGroupTxAtmLayerCells=xylanImaGroupTxAtmLayerCells, xylanImaLinkRxFillerCells=xylanImaLinkRxFillerCells, xylanImaLinkDescription=xylanImaLinkDescription, xylanImaGroupPhyFrameFormat=xylanImaGroupPhyFrameFormat, xylanImaLinkSlotIndex=xylanImaLinkSlotIndex, xylanImaLinkRxBufferOverflow=xylanImaLinkRxBufferOverflow, xylanImaGroupPhyLoopbackMode=xylanImaGroupPhyLoopbackMode, xylanImaGroupPhyUniqueParameter=xylanImaGroupPhyUniqueParameter, xylanImaGroupClearStatistics=xylanImaGroupClearStatistics, xylanImaMib=xylanImaMib, xylanImaLinkAdminStatus=xylanImaLinkAdminStatus, xylanImaGroupAdminStatus=xylanImaGroupAdminStatus, xylanImaLinkRxCellDiscarded=xylanImaLinkRxCellDiscarded, xylanImaLinkRxBufferFlush=xylanImaLinkRxBufferFlush, xylanImaGroupPhyTxClkSource=xylanImaGroupPhyTxClkSource, xylanImaGroupIndex=xylanImaGroupIndex, xylanImaLinkPortIndex=xylanImaLinkPortIndex, xylanImaGroupDescription=xylanImaGroupDescription, xylanImaGroupMaxDelayPort=xylanImaGroupMaxDelayPort, xylanImaLinkRxIcpCells=xylanImaLinkRxIcpCells, xylanImaLinkTxAtmLayerCells=xylanImaLinkTxAtmLayerCells, xylanImaLinkCellsInRxBuffer=xylanImaLinkCellsInRxBuffer, xylanImaLinkTxFillerCells=xylanImaLinkTxFillerCells, xylanImaLinkTxIcpCells=xylanImaLinkTxIcpCells, xylanImaGroupPhyLineLength=xylanImaGroupPhyLineLength, xylanImaLinkEntry=xylanImaLinkEntry, xylanImaLinkRxStuffEvents=xylanImaLinkRxStuffEvents, xylanImaGroupAtmLayerPort=xylanImaGroupAtmLayerPort, xylanImaLinkClearStatistics=xylanImaLinkClearStatistics, xylanImaGroupTable=xylanImaGroupTable, xylanImaLinkIfIndex=xylanImaLinkIfIndex, xylanImaGroupAtmLayerSlot=xylanImaGroupAtmLayerSlot, xylanImaGroupMaxDelaySlot=xylanImaGroupMaxDelaySlot)