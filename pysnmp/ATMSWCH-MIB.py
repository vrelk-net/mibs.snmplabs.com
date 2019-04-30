#
# PySNMP MIB module ATMSWCH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ATMSWCH-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:15:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
lannet, = mibBuilder.importSymbols("GEN-MIB", "lannet")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Bits, MibIdentifier, Unsigned32, iso, Integer32, NotificationType, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, Counter32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Bits", "MibIdentifier", "Unsigned32", "iso", "Integer32", "NotificationType", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "Counter32", "Counter64")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
class AtmAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(20, 20)
    fixedLength = 20

class AtmPrefix(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(13, 13)
    fixedLength = 13

atmSwch = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 33))
atmSwchBase = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 33, 1))
atmSwchCpu = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 33, 2))
atmSwchSlot = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 33, 5))
atmSwchPort = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 33, 6))
atmSwchVPort = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 33, 7))
atmSwchSlotRoute = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 33, 8))
atmSwchSlotAddrVcl = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 33, 9))
atmSwchBaseCurrentPrefix = MibScalar((1, 3, 6, 1, 4, 1, 81, 33, 1, 1), AtmPrefix()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchBaseCurrentPrefix.setStatus('mandatory')
atmSwchBaseConfigPrefix = MibScalar((1, 3, 6, 1, 4, 1, 81, 33, 1, 2), AtmPrefix()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSwchBaseConfigPrefix.setStatus('mandatory')
atmSwchBaseEpdThreshold = MibScalar((1, 3, 6, 1, 4, 1, 81, 33, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(50, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSwchBaseEpdThreshold.setStatus('mandatory')
atmSwchBaseAmonAdminState = MibScalar((1, 3, 6, 1, 4, 1, 81, 33, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSwchBaseAmonAdminState.setStatus('mandatory')
atmSwchCpuTable = MibTable((1, 3, 6, 1, 4, 1, 81, 33, 2, 1), )
if mibBuilder.loadTexts: atmSwchCpuTable.setStatus('mandatory')
atmSwchCpuEntry = MibTableRow((1, 3, 6, 1, 4, 1, 81, 33, 2, 1, 1), ).setIndexNames((0, "ATMSWCH-MIB", "atmSwchCpuIndex"))
if mibBuilder.loadTexts: atmSwchCpuEntry.setStatus('mandatory')
atmSwchCpuIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchCpuIndex.setStatus('mandatory')
atmSwchCpuHwVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 2, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3)).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchCpuHwVersion.setStatus('mandatory')
atmSwchCpuSoftErrCode = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchCpuSoftErrCode.setStatus('mandatory')
atmSwchCpuSoftErrString = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 2, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchCpuSoftErrString.setStatus('mandatory')
atmSwchCpuUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchCpuUtilization.setStatus('mandatory')
atmSwchCpuRamSize = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 2, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchCpuRamSize.setStatus('mandatory')
atmSwchCpuRamUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 2, 1, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchCpuRamUsed.setStatus('mandatory')
atmSwchCpuFlashSize = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 2, 1, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchCpuFlashSize.setStatus('mandatory')
atmSwchCpuFlashUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 2, 1, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchCpuFlashUsed.setStatus('mandatory')
atmSwchCpuEepromSize = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 2, 1, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchCpuEepromSize.setStatus('mandatory')
atmSwchCpuEepromUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 2, 1, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchCpuEepromUsed.setStatus('mandatory')
atmSwchCpuTime = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 2, 1, 1, 12), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSwchCpuTime.setStatus('mandatory')
atmSwchCpuSysUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 2, 1, 1, 13), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchCpuSysUpTime.setStatus('mandatory')
atmSwchCpuSvcPtPtInConns = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 2, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchCpuSvcPtPtInConns.setStatus('mandatory')
atmSwchCpuSvcPtPtOutConns = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 2, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchCpuSvcPtPtOutConns.setStatus('mandatory')
atmSwchCpuSvcPtMptRootConns = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 2, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchCpuSvcPtMptRootConns.setStatus('mandatory')
atmSwchCpuSvcPtMptLeafConns = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 2, 1, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchCpuSvcPtMptLeafConns.setStatus('mandatory')
atmSwchCpuPvcPtPtConns = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 2, 1, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchCpuPvcPtPtConns.setStatus('mandatory')
atmSwchSlotTable = MibTable((1, 3, 6, 1, 4, 1, 81, 33, 5, 1), )
if mibBuilder.loadTexts: atmSwchSlotTable.setStatus('mandatory')
atmSwchSlotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 81, 33, 5, 1, 1), ).setIndexNames((0, "ATMSWCH-MIB", "atmSwchSlotIndex"))
if mibBuilder.loadTexts: atmSwchSlotEntry.setStatus('mandatory')
atmSwchSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 5, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchSlotIndex.setStatus('mandatory')
atmSwchSlotRxCellDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 5, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchSlotRxCellDiscards.setStatus('mandatory')
atmSwchSlotRouteNextId = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 5, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchSlotRouteNextId.setStatus('mandatory')
atmSwchSlotAPSMode = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 5, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("uniDirectionalNonRevertive", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchSlotAPSMode.setStatus('mandatory')
atmSwchSlotAPSCurrentState = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 5, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("noRequest", 1), ("sf", 2), ("sd", 3), ("forcedSwitch", 4), ("manualSwitch", 5), ("doNotRevert", 6), ("noAPS", 7), ("notActive", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchSlotAPSCurrentState.setStatus('mandatory')
atmSwchSlotAPSSwitchCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 5, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("noCmd", 1), ("clear", 2), ("forcedSwitchWorkToProtect", 3), ("forcedSwitchProtectToWork", 4), ("manualSwitchWorkToProtect", 5), ("manualSwitchProtectToWork", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSwchSlotAPSSwitchCommand.setStatus('mandatory')
atmSwchSlotAPSSFBerThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 5, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 9))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchSlotAPSSFBerThreshold.setStatus('mandatory')
atmSwchSlotAPSSDBerThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 5, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 9))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSwchSlotAPSSDBerThreshold.setStatus('mandatory')
atmSwchSlotAPSDecision = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 5, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("working", 1), ("protection", 2), ("not-Active", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchSlotAPSDecision.setStatus('mandatory')
atmSwchPortTable = MibTable((1, 3, 6, 1, 4, 1, 81, 33, 6, 1), )
if mibBuilder.loadTexts: atmSwchPortTable.setStatus('mandatory')
atmSwchPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 81, 33, 6, 1, 1), ).setIndexNames((0, "ATMSWCH-MIB", "atmSwchSlotIndex"), (0, "ATMSWCH-MIB", "atmSwchPortIndex"))
if mibBuilder.loadTexts: atmSwchPortEntry.setStatus('mandatory')
atmSwchPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 6, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchPortIndex.setStatus('mandatory')
atmSwchPortRootVportIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 6, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchPortRootVportIndex.setStatus('mandatory')
atmSwchPortNumVPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 6, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchPortNumVPorts.setStatus('mandatory')
atmSwchPortPayloadScramble = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 6, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSwchPortPayloadScramble.setStatus('mandatory')
atmSwchPortPhysicalType = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 6, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sonet", 1), ("sdh", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSwchPortPhysicalType.setStatus('mandatory')
atmSwchPortMaxTxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 6, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSwchPortMaxTxRate.setStatus('mandatory')
atmSwchPortSvcPtPtInConns = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 6, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchPortSvcPtPtInConns.setStatus('mandatory')
atmSwchPortSvcPtPtOutConns = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 6, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchPortSvcPtPtOutConns.setStatus('mandatory')
atmSwchPortSvcPtMptRootConns = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 6, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchPortSvcPtMptRootConns.setStatus('mandatory')
atmSwchPortSvcPtMptLeafConns = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 6, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchPortSvcPtMptLeafConns.setStatus('mandatory')
atmSwchPortPvcPtPtConns = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 6, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchPortPvcPtPtConns.setStatus('mandatory')
atmSwchPortPvcPtMptRootConns = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 6, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchPortPvcPtMptRootConns.setStatus('mandatory')
atmSwchPortPvcPtMptLeafConns = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 6, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchPortPvcPtMptLeafConns.setStatus('mandatory')
atmSwchPortPvpPtPtConns = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 6, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchPortPvpPtPtConns.setStatus('mandatory')
atmSwchPortPvpPtMptRootConns = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 6, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchPortPvpPtMptRootConns.setStatus('mandatory')
atmSwchPortPvpPtMptLeafConns = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 6, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchPortPvpPtMptLeafConns.setStatus('mandatory')
atmSwchPortdsx3CellMaping = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 6, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dsx3ADM", 1), ("dsx3PLCP", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSwchPortdsx3CellMaping.setStatus('mandatory')
atmSwchVPortTable = MibTable((1, 3, 6, 1, 4, 1, 81, 33, 7, 1), )
if mibBuilder.loadTexts: atmSwchVPortTable.setStatus('mandatory')
atmSwchVPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1), ).setIndexNames((0, "ATMSWCH-MIB", "atmSwchSlotIndex"), (0, "ATMSWCH-MIB", "atmSwchPortIndex"), (0, "ATMSWCH-MIB", "atmSwchVPortIndex"))
if mibBuilder.loadTexts: atmSwchVPortEntry.setStatus('mandatory')
atmSwchVPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchVPortIndex.setStatus('mandatory')
atmSwchVPortIsRoot = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("isRoot", 1), ("notRoot", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchVPortIsRoot.setStatus('mandatory')
atmSwchVPortAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSwchVPortAdminStatus.setStatus('mandatory')
atmSwchVPortOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchVPortOperStatus.setStatus('mandatory')
atmSwchVPortCurrentSignallingState = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("up", 2), ("down", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchVPortCurrentSignallingState.setStatus('mandatory')
atmSwchVPortCurrentILMIState = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("stackOff", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchVPortCurrentILMIState.setStatus('mandatory')
atmSwchVPortCurrentAddrRegEn = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("enabled", 2), ("disabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchVPortCurrentAddrRegEn.setStatus('mandatory')
atmSwchVPortCurrentLinkType = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 1), ("uni30", 2), ("uni31", 3), ("iisp30", 4), ("iisp31", 5), ("pnni10", 6), ("uni40", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchVPortCurrentLinkType.setStatus('mandatory')
atmSwchVPortCurrentTermType = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("user", 2), ("network", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchVPortCurrentTermType.setStatus('mandatory')
atmSwchVPortConfigILMIState = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("stackEnabled", 1), ("stackDisabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSwchVPortConfigILMIState.setStatus('mandatory')
atmSwchVPortConfigAddrRegEn = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("automatic", 1), ("enabled", 2), ("disabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSwchVPortConfigAddrRegEn.setStatus('mandatory')
atmSwchVPortConfigLinkType = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("automatic", 1), ("unknown", 2), ("uni30", 3), ("uni31", 4), ("iisp30", 5), ("iisp31", 6), ("pnni10", 7), ("uni40", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSwchVPortConfigLinkType.setStatus('mandatory')
atmSwchVPortConfigTermType = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("automatic", 1), ("user", 2), ("network", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSwchVPortConfigTermType.setStatus('mandatory')
atmSwchVPortNeighbourSysName = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchVPortNeighbourSysName.setStatus('mandatory')
atmSwchVPortNeighbourUNIVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("notKnown", 1), ("uni30", 2), ("uni31", 3), ("uni40", 4), ("iisp", 5), ("pnni10", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchVPortNeighbourUNIVersion.setStatus('mandatory')
atmSwchVPortNeighbourATMAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 16), AtmAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchVPortNeighbourATMAddress.setStatus('mandatory')
atmSwchVPortNeighbourIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchVPortNeighbourIfName.setStatus('mandatory')
atmSwchVPortMibProbe = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSwchVPortMibProbe.setStatus('mandatory')
atmSwchVPortConfMinSvccVci = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSwchVPortConfMinSvccVci.setStatus('mandatory')
atmSwchVPortConfMaxSvccVci = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 20), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSwchVPortConfMaxSvccVci.setStatus('mandatory')
atmSwchVPortConfMinVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSwchVPortConfMinVpi.setStatus('mandatory')
atmSwchVPortConfMaxVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSwchVPortConfMaxVpi.setStatus('mandatory')
atmSwchVPortNeighbourIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 23), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchVPortNeighbourIpAddress.setStatus('mandatory')
atmSwchVPortPcr = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 24), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSwchVPortPcr.setStatus('mandatory')
atmSwchVPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 7, 1, 1, 25), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSwchVPortRowStatus.setStatus('mandatory')
atmSwchSlotRouteTable = MibTable((1, 3, 6, 1, 4, 1, 81, 33, 8, 1), )
if mibBuilder.loadTexts: atmSwchSlotRouteTable.setStatus('mandatory')
atmSwchSlotRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 81, 33, 8, 1, 1), ).setIndexNames((0, "ATMSWCH-MIB", "atmSwchSlotIndex"), (0, "ATMSWCH-MIB", "atmSwchSlotRouteId"))
if mibBuilder.loadTexts: atmSwchSlotRouteEntry.setStatus('mandatory')
atmSwchSlotRouteId = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 8, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchSlotRouteId.setStatus('mandatory')
atmSwchSlotRouteRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 8, 1, 1, 2), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSwchSlotRouteRowStatus.setStatus('mandatory')
atmSwchSlotRouteAddressPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 8, 1, 1, 3), AtmAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSwchSlotRouteAddressPrefix.setStatus('mandatory')
atmSwchSlotRoutePrefixLength = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 8, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 152))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSwchSlotRoutePrefixLength.setStatus('mandatory')
atmSwchSlotRoutePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 8, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 999))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSwchSlotRoutePriority.setStatus('mandatory')
atmSwchSlotRouteSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 8, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSwchSlotRouteSlot.setStatus('mandatory')
atmSwchSlotRoutePort = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 8, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSwchSlotRoutePort.setStatus('mandatory')
atmSwchSlotRouteVport = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 8, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmSwchSlotRouteVport.setStatus('mandatory')
atmSwchSlotRouteOrigin = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 8, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("nonVolatile", 1), ("snmp", 2), ("ilmi", 3), ("lane", 4), ("dynamic", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchSlotRouteOrigin.setStatus('mandatory')
atmSwchSlotRouteOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 8, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchSlotRouteOperStatus.setStatus('mandatory')
atmSwchSlotAddrVclTable = MibTable((1, 3, 6, 1, 4, 1, 81, 33, 9, 1), )
if mibBuilder.loadTexts: atmSwchSlotAddrVclTable.setStatus('mandatory')
atmSwchSlotAddrVclEntry = MibTableRow((1, 3, 6, 1, 4, 1, 81, 33, 9, 1, 1), ).setIndexNames((0, "ATMSWCH-MIB", "atmSwchSlotIndex"), (0, "ATMSWCH-MIB", "atmSwchSlotAddrVclAddr"), (0, "ATMSWCH-MIB", "atmSwchSlotAddrVclAtmIfIndex"), (0, "ATMSWCH-MIB", "atmSwchSlotAddrVclVpi"), (0, "ATMSWCH-MIB", "atmSwchSlotAddrVclVci"))
if mibBuilder.loadTexts: atmSwchSlotAddrVclEntry.setStatus('mandatory')
atmSwchSlotAddrVclAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 9, 1, 1, 1), AtmAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchSlotAddrVclAddr.setStatus('mandatory')
atmSwchSlotAddrVclAtmIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 9, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchSlotAddrVclAtmIfIndex.setStatus('mandatory')
atmSwchSlotAddrVclVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 9, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchSlotAddrVclVpi.setStatus('mandatory')
atmSwchSlotAddrVclVci = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 9, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchSlotAddrVclVci.setStatus('mandatory')
atmSwchSlotAddrVclAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 33, 9, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("callingParty", 1), ("calledParty", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSwchSlotAddrVclAddrType.setStatus('mandatory')
mibBuilder.exportSymbols("ATMSWCH-MIB", atmSwchCpuSvcPtPtInConns=atmSwchCpuSvcPtPtInConns, atmSwchVPortIndex=atmSwchVPortIndex, atmSwchVPortIsRoot=atmSwchVPortIsRoot, atmSwchVPortNeighbourUNIVersion=atmSwchVPortNeighbourUNIVersion, atmSwchSlotRouteId=atmSwchSlotRouteId, atmSwchPort=atmSwchPort, atmSwchSlotRxCellDiscards=atmSwchSlotRxCellDiscards, atmSwchVPortCurrentTermType=atmSwchVPortCurrentTermType, atmSwchSlotAddrVclVci=atmSwchSlotAddrVclVci, atmSwchVPortRowStatus=atmSwchVPortRowStatus, atmSwchVPortConfMinSvccVci=atmSwchVPortConfMinSvccVci, atmSwchSlotIndex=atmSwchSlotIndex, atmSwchCpuSoftErrCode=atmSwchCpuSoftErrCode, atmSwchCpuEntry=atmSwchCpuEntry, atmSwchCpuTime=atmSwchCpuTime, atmSwchSlotAddrVcl=atmSwchSlotAddrVcl, atmSwchPortPvpPtPtConns=atmSwchPortPvpPtPtConns, atmSwchVPortConfMaxVpi=atmSwchVPortConfMaxVpi, atmSwchVPortEntry=atmSwchVPortEntry, atmSwchSlotRouteVport=atmSwchSlotRouteVport, atmSwchVPort=atmSwchVPort, atmSwchSlotAPSDecision=atmSwchSlotAPSDecision, atmSwchPortPvpPtMptLeafConns=atmSwchPortPvpPtMptLeafConns, atmSwchVPortOperStatus=atmSwchVPortOperStatus, atmSwchCpuSvcPtPtOutConns=atmSwchCpuSvcPtPtOutConns, atmSwchSlotAPSSFBerThreshold=atmSwchSlotAPSSFBerThreshold, atmSwchCpuRamSize=atmSwchCpuRamSize, atmSwchCpuHwVersion=atmSwchCpuHwVersion, atmSwchCpuUtilization=atmSwchCpuUtilization, atmSwchVPortNeighbourIpAddress=atmSwchVPortNeighbourIpAddress, atmSwchPortSvcPtMptRootConns=atmSwchPortSvcPtMptRootConns, atmSwchCpuSvcPtMptLeafConns=atmSwchCpuSvcPtMptLeafConns, atmSwchVPortTable=atmSwchVPortTable, atmSwchPortNumVPorts=atmSwchPortNumVPorts, atmSwchPortPvcPtPtConns=atmSwchPortPvcPtPtConns, atmSwchSlotAddrVclAtmIfIndex=atmSwchSlotAddrVclAtmIfIndex, atmSwchPortSvcPtPtInConns=atmSwchPortSvcPtPtInConns, AtmPrefix=AtmPrefix, atmSwchVPortNeighbourSysName=atmSwchVPortNeighbourSysName, atmSwchVPortNeighbourIfName=atmSwchVPortNeighbourIfName, atmSwchVPortConfigTermType=atmSwchVPortConfigTermType, atmSwchPortdsx3CellMaping=atmSwchPortdsx3CellMaping, atmSwchCpuSysUpTime=atmSwchCpuSysUpTime, atmSwchVPortConfigILMIState=atmSwchVPortConfigILMIState, atmSwchBaseConfigPrefix=atmSwchBaseConfigPrefix, atmSwchCpuEepromUsed=atmSwchCpuEepromUsed, atmSwchVPortCurrentAddrRegEn=atmSwchVPortCurrentAddrRegEn, atmSwchPortIndex=atmSwchPortIndex, atmSwch=atmSwch, atmSwchPortEntry=atmSwchPortEntry, atmSwchPortSvcPtMptLeafConns=atmSwchPortSvcPtMptLeafConns, atmSwchCpuFlashUsed=atmSwchCpuFlashUsed, atmSwchVPortNeighbourATMAddress=atmSwchVPortNeighbourATMAddress, atmSwchCpuFlashSize=atmSwchCpuFlashSize, atmSwchSlotAPSSwitchCommand=atmSwchSlotAPSSwitchCommand, atmSwchPortPayloadScramble=atmSwchPortPayloadScramble, atmSwchBaseCurrentPrefix=atmSwchBaseCurrentPrefix, atmSwchSlotRouteSlot=atmSwchSlotRouteSlot, atmSwchSlotRoutePriority=atmSwchSlotRoutePriority, AtmAddress=AtmAddress, atmSwchSlotAddrVclTable=atmSwchSlotAddrVclTable, atmSwchCpuPvcPtPtConns=atmSwchCpuPvcPtPtConns, atmSwchSlotAPSCurrentState=atmSwchSlotAPSCurrentState, atmSwchSlotRoutePrefixLength=atmSwchSlotRoutePrefixLength, atmSwchBase=atmSwchBase, atmSwchSlotRouteOperStatus=atmSwchSlotRouteOperStatus, atmSwchCpuRamUsed=atmSwchCpuRamUsed, atmSwchSlotAddrVclAddrType=atmSwchSlotAddrVclAddrType, atmSwchCpu=atmSwchCpu, atmSwchPortSvcPtPtOutConns=atmSwchPortSvcPtPtOutConns, atmSwchSlotRouteAddressPrefix=atmSwchSlotRouteAddressPrefix, atmSwchSlotRouteNextId=atmSwchSlotRouteNextId, atmSwchPortPvcPtMptRootConns=atmSwchPortPvcPtMptRootConns, atmSwchSlotAPSMode=atmSwchSlotAPSMode, atmSwchSlotAddrVclVpi=atmSwchSlotAddrVclVpi, atmSwchPortRootVportIndex=atmSwchPortRootVportIndex, atmSwchVPortMibProbe=atmSwchVPortMibProbe, atmSwchBaseAmonAdminState=atmSwchBaseAmonAdminState, atmSwchPortTable=atmSwchPortTable, atmSwchCpuSoftErrString=atmSwchCpuSoftErrString, atmSwchSlotRouteOrigin=atmSwchSlotRouteOrigin, atmSwchSlotRoute=atmSwchSlotRoute, atmSwchBaseEpdThreshold=atmSwchBaseEpdThreshold, atmSwchPortMaxTxRate=atmSwchPortMaxTxRate, atmSwchCpuIndex=atmSwchCpuIndex, atmSwchPortPvcPtMptLeafConns=atmSwchPortPvcPtMptLeafConns, atmSwchVPortCurrentILMIState=atmSwchVPortCurrentILMIState, atmSwchVPortCurrentSignallingState=atmSwchVPortCurrentSignallingState, atmSwchVPortConfMinVpi=atmSwchVPortConfMinVpi, atmSwchVPortAdminStatus=atmSwchVPortAdminStatus, atmSwchSlotEntry=atmSwchSlotEntry, atmSwchCpuTable=atmSwchCpuTable, atmSwchSlot=atmSwchSlot, atmSwchVPortConfigAddrRegEn=atmSwchVPortConfigAddrRegEn, atmSwchSlotAPSSDBerThreshold=atmSwchSlotAPSSDBerThreshold, atmSwchPortPhysicalType=atmSwchPortPhysicalType, atmSwchVPortPcr=atmSwchVPortPcr, atmSwchSlotAddrVclAddr=atmSwchSlotAddrVclAddr, atmSwchCpuSvcPtMptRootConns=atmSwchCpuSvcPtMptRootConns, atmSwchCpuEepromSize=atmSwchCpuEepromSize, atmSwchSlotTable=atmSwchSlotTable, atmSwchVPortConfMaxSvccVci=atmSwchVPortConfMaxSvccVci, atmSwchVPortCurrentLinkType=atmSwchVPortCurrentLinkType, atmSwchSlotRouteTable=atmSwchSlotRouteTable, atmSwchSlotRouteRowStatus=atmSwchSlotRouteRowStatus, atmSwchSlotRouteEntry=atmSwchSlotRouteEntry, atmSwchPortPvpPtMptRootConns=atmSwchPortPvpPtMptRootConns, atmSwchSlotRoutePort=atmSwchSlotRoutePort, atmSwchVPortConfigLinkType=atmSwchVPortConfigLinkType, atmSwchSlotAddrVclEntry=atmSwchSlotAddrVclEntry)