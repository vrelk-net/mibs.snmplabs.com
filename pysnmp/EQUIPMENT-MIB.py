#
# PySNMP MIB module EQUIPMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EQUIPMENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:51:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
dlink_common_mgmt, AgentNotifyLevel = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt", "AgentNotifyLevel")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, iso, Integer32, Counter64, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, ObjectIdentity, MibIdentifier, NotificationType, Counter32, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "iso", "Integer32", "Counter64", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "ObjectIdentity", "MibIdentifier", "NotificationType", "Counter32", "TimeTicks", "Bits")
DateAndTime, TruthValue, TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TruthValue", "TextualConvention", "DisplayString", "RowStatus")
swTimeRangeMgmtRangeName, = mibBuilder.importSymbols("TIMERANGE-MIB", "swTimeRangeMgmtRangeName")
swEquipmentMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 11))
if mibBuilder.loadTexts: swEquipmentMIB.setLastUpdated('201104200000Z')
if mibBuilder.loadTexts: swEquipmentMIB.setOrganization('D-Link Corp.')
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

swEquipment = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 11, 1))
swEquipmentNotify = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 11, 2))
swEquipmentCapacity = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 1), Bits().clone(namedValues=NamedValues(("fanCapable", 0), ("redundantPowerCapable", 1), ("tempteratureDetection", 2), ("stackingCapable", 3), ("chassisCapable", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swEquipmentCapacity.setStatus('current')
swFanTrapState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swFanTrapState.setStatus('current')
swPowerTrapState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPowerTrapState.setStatus('current')
swPowerTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 6), )
if mibBuilder.loadTexts: swPowerTable.setStatus('current')
swPowerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 6, 1), ).setIndexNames((0, "EQUIPMENT-MIB", "swPowerUnitIndex"), (0, "EQUIPMENT-MIB", "swPowerID"))
if mibBuilder.loadTexts: swPowerEntry.setStatus('current')
swPowerUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPowerUnitIndex.setStatus('current')
swPowerID = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPowerID.setStatus('current')
swPowerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 0), ("lowVoltage", 1), ("overCurrent", 2), ("working", 3), ("fail", 4), ("connect", 5), ("disconnect", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swPowerStatus.setStatus('current')
swFanTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 7), )
if mibBuilder.loadTexts: swFanTable.setStatus('current')
swFanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 7, 1), ).setIndexNames((0, "EQUIPMENT-MIB", "swFanUnitIndex"), (0, "EQUIPMENT-MIB", "swFanID"))
if mibBuilder.loadTexts: swFanEntry.setStatus('current')
swFanUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swFanUnitIndex.setStatus('current')
swFanID = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 7, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swFanID.setStatus('current')
swFanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 0), ("working", 1), ("fail", 2), ("speed-0", 3), ("speed-low", 4), ("speed-middle", 5), ("speed-high", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swFanStatus.setStatus('current')
swFanPostion = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 7, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("left", 2), ("right", 3), ("back", 4), ("cpu", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swFanPostion.setStatus('current')
swFanNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 7, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swFanNumber.setStatus('current')
swFanSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 7, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swFanSpeed.setStatus('current')
swTemperatureTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 8), )
if mibBuilder.loadTexts: swTemperatureTable.setStatus('current')
swTemperatureEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 8, 1), ).setIndexNames((0, "EQUIPMENT-MIB", "swTemperatureUnitIndex"))
if mibBuilder.loadTexts: swTemperatureEntry.setStatus('current')
swTemperatureUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swTemperatureUnitIndex.setStatus('current')
swTemperatureCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 8, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-500, 500))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swTemperatureCurrent.setStatus('current')
swTemperatureHighThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 8, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-500, 500))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swTemperatureHighThresh.setStatus('current')
swTemperatureLowThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 8, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-500, 500))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swTemperatureLowThresh.setStatus('current')
swUnitMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9))
swUnitStackingVersion = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swUnitStackingVersion.setStatus('current')
swUnitMaxSupportedUnits = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swUnitMaxSupportedUnits.setStatus('current')
swUnitNumOfUnit = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swUnitNumOfUnit.setStatus('current')
swUnitMgmtTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4), )
if mibBuilder.loadTexts: swUnitMgmtTable.setStatus('current')
swUnitMgmtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1), ).setIndexNames((0, "EQUIPMENT-MIB", "swUnitMgmtId"))
if mibBuilder.loadTexts: swUnitMgmtEntry.setStatus('current')
swUnitMgmtId = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 13))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swUnitMgmtId.setStatus('current')
swUnitMgmtMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swUnitMgmtMacAddr.setStatus('current')
swUnitMgmtStartPort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swUnitMgmtStartPort.setStatus('current')
swUnitMgmtPortRange = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swUnitMgmtPortRange.setStatus('current')
swUnitMgmtFrontPanelLedStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swUnitMgmtFrontPanelLedStatus.setStatus('current')
swUnitMgmtCtrlMode = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("auto", 2), ("stand-alone", 3), ("master", 4), ("slave", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swUnitMgmtCtrlMode.setStatus('current')
swUnitMgmtCurrentMode = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("auto", 2), ("stand-alone", 3), ("master", 4), ("slave", 5), ("backup-master", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swUnitMgmtCurrentMode.setStatus('current')
swUnitMgmtVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swUnitMgmtVersion.setStatus('current')
swUnitMgmtModuleName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swUnitMgmtModuleName.setStatus('current')
swUnitMgmtPromVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swUnitMgmtPromVersion.setStatus('current')
swUnitMgmtFirmwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swUnitMgmtFirmwareVersion.setStatus('current')
swUnitMgmtHardwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swUnitMgmtHardwareVersion.setStatus('current')
swUnitMgmtPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swUnitMgmtPriority.setStatus('current')
swUnitMgmtUserSetState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("auto", 2), ("user", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swUnitMgmtUserSetState.setStatus('current')
swUnitMgmtExistState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("exist", 1), ("no-exist", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swUnitMgmtExistState.setStatus('current')
swUnitMgmtBoxId = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))).clone(namedValues=NamedValues(("box-1", 1), ("box-2", 2), ("box-3", 3), ("box-4", 4), ("box-5", 5), ("box-6", 6), ("box-7", 7), ("box-8", 8), ("box-9", 9), ("box-10", 10), ("box-11", 11), ("box-12", 12), ("auto", 13)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swUnitMgmtBoxId.setStatus('current')
swUnitMgmtSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 4, 1, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swUnitMgmtSerialNumber.setStatus('current')
swUnitTopology = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("stand-alone", 1), ("duplex-chain", 2), ("duplex-ring", 3), ("star", 4), ("unstable", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swUnitTopology.setStatus('current')
swUnitStackMode = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swUnitStackMode.setStatus('current')
swUnitStackForceMasterRole = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swUnitStackForceMasterRole.setStatus('current')
swUnitStackTrapState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swUnitStackTrapState.setStatus('current')
swUnitStackLogState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 9, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swUnitStackLogState.setStatus('current')
swExternalAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 10), )
if mibBuilder.loadTexts: swExternalAlarmTable.setStatus('current')
swExternalAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 10, 1), ).setIndexNames((0, "EQUIPMENT-MIB", "swExternalAlarmChannel"))
if mibBuilder.loadTexts: swExternalAlarmEntry.setStatus('current')
swExternalAlarmChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 10, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swExternalAlarmChannel.setStatus('current')
swExternalAlarmMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 10, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swExternalAlarmMessage.setStatus('current')
swExternalAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 10, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("alarming", 1), ("normal", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swExternalAlarmStatus.setStatus('current')
swEquipmentPowerSaving = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 11))
swEquipPowerSavingLinkDetectState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 11, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swEquipPowerSavingLinkDetectState.setStatus('current')
swEquipPowerSavingLenDetect = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 11, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swEquipPowerSavingLenDetect.setStatus('current')
swEquipPowerSavingHiberState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 11, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swEquipPowerSavingHiberState.setStatus('current')
swEquipPowerSavingPortLEDState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 11, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swEquipPowerSavingPortLEDState.setStatus('current')
swEquipPowerSavingPortState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 11, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swEquipPowerSavingPortState.setStatus('current')
swEquipPowerSavingScheduleCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 11, 6))
swEquipPowerSavingHibernationTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 11, 6, 1), )
if mibBuilder.loadTexts: swEquipPowerSavingHibernationTable.setStatus('current')
swEquipPowerSavingHibernationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 11, 6, 1, 1), ).setIndexNames((0, "TIMERANGE-MIB", "swTimeRangeMgmtRangeName"))
if mibBuilder.loadTexts: swEquipPowerSavingHibernationEntry.setStatus('current')
swEquipPowerSavingHiberRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 11, 6, 1, 1, 100), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swEquipPowerSavingHiberRowStatus.setStatus('current')
swEquipPowerSavingPortLedTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 11, 6, 2), )
if mibBuilder.loadTexts: swEquipPowerSavingPortLedTable.setStatus('current')
swEquipPowerSavingPortLedEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 11, 6, 2, 1), ).setIndexNames((0, "TIMERANGE-MIB", "swTimeRangeMgmtRangeName"))
if mibBuilder.loadTexts: swEquipPowerSavingPortLedEntry.setStatus('current')
swEquipPowerSavingPortLedRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 11, 6, 2, 1, 100), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swEquipPowerSavingPortLedRowStatus.setStatus('current')
swEquipPowerSavingPortTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 11, 6, 3), )
if mibBuilder.loadTexts: swEquipPowerSavingPortTable.setStatus('current')
swEquipPowerSavingPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 11, 6, 3, 1), ).setIndexNames((0, "EQUIPMENT-MIB", "swEquipPowerSavingPortIndex"), (0, "TIMERANGE-MIB", "swTimeRangeMgmtRangeName"))
if mibBuilder.loadTexts: swEquipPowerSavingPortEntry.setStatus('current')
swEquipPowerSavingPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 11, 6, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: swEquipPowerSavingPortIndex.setStatus('current')
swEquipPowerSavingPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 11, 6, 3, 1, 100), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swEquipPowerSavingPortRowStatus.setStatus('current')
swEquipmentTemperatureCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 12))
swTemperatureTrapState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 12, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swTemperatureTrapState.setStatus('current')
swTemperatureLogState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 12, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swTemperatureLogState.setStatus('current')
swEquipmentLEDCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 13))
swEquipmentPortLEDState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 13, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swEquipmentPortLEDState.setStatus('current')
swExternalAlarmStackingTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 15), )
if mibBuilder.loadTexts: swExternalAlarmStackingTable.setStatus('current')
swExternalAlarmStackingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 15, 1), ).setIndexNames((0, "EQUIPMENT-MIB", "swExternalAlarmStackingUnitIndex"), (0, "EQUIPMENT-MIB", "swExternalAlarmStackingChannel"))
if mibBuilder.loadTexts: swExternalAlarmStackingEntry.setStatus('current')
swExternalAlarmStackingUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 15, 1, 1), Integer32())
if mibBuilder.loadTexts: swExternalAlarmStackingUnitIndex.setStatus('current')
swExternalAlarmStackingChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 15, 1, 2), Integer32())
if mibBuilder.loadTexts: swExternalAlarmStackingChannel.setStatus('current')
swExternalAlarmStackingMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 15, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swExternalAlarmStackingMessage.setStatus('current')
swExternalAlarmStackingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 11, 1, 15, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("alarming", 1), ("normal", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swExternalAlarmStackingStatus.setStatus('current')
swEquipmentNotifyMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 1))
swEquipmentNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2))
swEquipUnitNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 1))
swEquipPowerNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 2))
swEquipFanNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 3))
swEquipTemperatureNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 4))
swEquipExternalAlarmNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 5))
swEquipUnitNotifyMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 1, 1))
swEquipPowerNotifyMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 1, 2))
swEquipFanNotifyMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 1, 3))
swEquipTemperatureNotifyMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 1, 4))
swUnitInsertSeverity = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 1, 1, 1), AgentNotifyLevel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swUnitInsertSeverity.setStatus('current')
swUnitRemoveSeverity = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 1, 1, 2), AgentNotifyLevel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swUnitRemoveSeverity.setStatus('current')
swUnitFailureSeverity = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 1, 1, 3), AgentNotifyLevel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swUnitFailureSeverity.setStatus('current')
swPowerStatusChgSeverity = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 1, 2, 1), AgentNotifyLevel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPowerStatusChgSeverity.setStatus('current')
swPowerFailureSeverity = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 1, 2, 2), AgentNotifyLevel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPowerFailureSeverity.setStatus('current')
swPowerRecoverSeverity = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 1, 2, 3), AgentNotifyLevel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swPowerRecoverSeverity.setStatus('current')
swFanFailureSeverity = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 1, 3, 1), AgentNotifyLevel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swFanFailureSeverity.setStatus('current')
swFanRecoverSeverity = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 1, 3, 2), AgentNotifyLevel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swFanRecoverSeverity.setStatus('current')
swHighTemperatureSeverity = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 1, 4, 1), AgentNotifyLevel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swHighTemperatureSeverity.setStatus('current')
swHighTemperatureRecoverSeverity = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 1, 4, 2), AgentNotifyLevel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swHighTemperatureRecoverSeverity.setStatus('current')
swLowTemperatureSeverity = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 1, 4, 3), AgentNotifyLevel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swLowTemperatureSeverity.setStatus('current')
swLowTemperatureRecoverSeverity = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 1, 4, 4), AgentNotifyLevel()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swLowTemperatureRecoverSeverity.setStatus('current')
swEquipUnitNotifyPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 1, 0))
swUnitInsert = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 1, 0, 1)).setObjects(("EQUIPMENT-MIB", "swUnitMgmtId"), ("EQUIPMENT-MIB", "swUnitMgmtMacAddr"))
if mibBuilder.loadTexts: swUnitInsert.setStatus('current')
swUnitRemove = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 1, 0, 2)).setObjects(("EQUIPMENT-MIB", "swUnitMgmtId"), ("EQUIPMENT-MIB", "swUnitMgmtMacAddr"))
if mibBuilder.loadTexts: swUnitRemove.setStatus('current')
swUnitFailure = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 1, 0, 3)).setObjects(("EQUIPMENT-MIB", "swUnitMgmtId"))
if mibBuilder.loadTexts: swUnitFailure.setStatus('current')
swUnitTPChange = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 1, 0, 4)).setObjects(("EQUIPMENT-MIB", "swStackTopologyType"), ("EQUIPMENT-MIB", "swUnitMgmtId"), ("EQUIPMENT-MIB", "swUnitMgmtMacAddr"))
if mibBuilder.loadTexts: swUnitTPChange.setStatus('current')
swUnitRoleChange = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 1, 0, 5)).setObjects(("EQUIPMENT-MIB", "swStackRoleChangeType"), ("EQUIPMENT-MIB", "swUnitMgmtId"))
if mibBuilder.loadTexts: swUnitRoleChange.setStatus('current')
swEquipPowerNotifyPerfix = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 2, 0))
swPowerStatusChg = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 2, 0, 1)).setObjects(("EQUIPMENT-MIB", "swPowerUnitIndex"), ("EQUIPMENT-MIB", "swPowerID"), ("EQUIPMENT-MIB", "swPowerStatus"))
if mibBuilder.loadTexts: swPowerStatusChg.setStatus('current')
swPowerFailure = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 2, 0, 2)).setObjects(("EQUIPMENT-MIB", "swPowerUnitIndex"), ("EQUIPMENT-MIB", "swPowerID"), ("EQUIPMENT-MIB", "swPowerStatus"))
if mibBuilder.loadTexts: swPowerFailure.setStatus('current')
swPowerRecover = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 2, 0, 3)).setObjects(("EQUIPMENT-MIB", "swPowerUnitIndex"), ("EQUIPMENT-MIB", "swPowerID"), ("EQUIPMENT-MIB", "swPowerStatus"))
if mibBuilder.loadTexts: swPowerRecover.setStatus('current')
swEquipFanNotifyPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 3, 0))
swFanFailure = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 3, 0, 1)).setObjects(("EQUIPMENT-MIB", "swFanUnitIndex"), ("EQUIPMENT-MIB", "swFanID"))
if mibBuilder.loadTexts: swFanFailure.setStatus('current')
swFanRecover = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 3, 0, 2)).setObjects(("EQUIPMENT-MIB", "swFanUnitIndex"), ("EQUIPMENT-MIB", "swFanID"))
if mibBuilder.loadTexts: swFanRecover.setStatus('current')
swEquipTemperatureNotifyPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 4, 0))
swHighTemperature = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 4, 0, 1)).setObjects(("EQUIPMENT-MIB", "swTemperatureUnitIndex"), ("EQUIPMENT-MIB", "swTemperSensorID"), ("EQUIPMENT-MIB", "swTemperatureCurrent"))
if mibBuilder.loadTexts: swHighTemperature.setStatus('current')
swHighTemperatureRecover = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 4, 0, 2)).setObjects(("EQUIPMENT-MIB", "swTemperatureUnitIndex"), ("EQUIPMENT-MIB", "swTemperSensorID"), ("EQUIPMENT-MIB", "swTemperatureCurrent"))
if mibBuilder.loadTexts: swHighTemperatureRecover.setStatus('current')
swLowTemperature = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 4, 0, 3)).setObjects(("EQUIPMENT-MIB", "swTemperatureUnitIndex"), ("EQUIPMENT-MIB", "swTemperSensorID"), ("EQUIPMENT-MIB", "swTemperatureCurrent"))
if mibBuilder.loadTexts: swLowTemperature.setStatus('current')
swLowTemperatureRecover = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 4, 0, 4)).setObjects(("EQUIPMENT-MIB", "swTemperatureUnitIndex"), ("EQUIPMENT-MIB", "swTemperSensorID"), ("EQUIPMENT-MIB", "swTemperatureCurrent"))
if mibBuilder.loadTexts: swLowTemperatureRecover.setStatus('current')
swEquipExternalAlarmNotifyPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 5, 0))
swExternalAlarm = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 5, 0, 1)).setObjects(("EQUIPMENT-MIB", "swExternalAlarmChannel"), ("EQUIPMENT-MIB", "swExternalAlarmMessage"))
if mibBuilder.loadTexts: swExternalAlarm.setStatus('current')
swExternalAlarmStacking = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 2, 5, 0, 2)).setObjects(("EQUIPMENT-MIB", "swExternalAlarmStackingUnitIndex"), ("EQUIPMENT-MIB", "swExternalAlarmStackingChannel"), ("EQUIPMENT-MIB", "swExternalAlarmStackingMessage"))
if mibBuilder.loadTexts: swExternalAlarmStacking.setStatus('current')
swNotificationBindings = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 3))
swEquipTemperNotifyBindings = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 3, 1))
swTemperSensorID = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 3, 1, 1), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: swTemperSensorID.setStatus('current')
swEquipUnitNotifyBindings = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 3, 2))
swStackTopologyType = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 3, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("chain", 1), ("ring", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: swStackTopologyType.setStatus('current')
swStackRoleChangeType = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 11, 2, 3, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("backup-to-master", 1), ("slave-to-master", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: swStackRoleChangeType.setStatus('current')
mibBuilder.exportSymbols("EQUIPMENT-MIB", swTemperatureHighThresh=swTemperatureHighThresh, swUnitFailureSeverity=swUnitFailureSeverity, swPowerStatus=swPowerStatus, swUnitMgmtStartPort=swUnitMgmtStartPort, swExternalAlarmStatus=swExternalAlarmStatus, swEquipPowerSavingPortTable=swEquipPowerSavingPortTable, swPowerFailureSeverity=swPowerFailureSeverity, swUnitMgmtPromVersion=swUnitMgmtPromVersion, swEquipUnitNotifyBindings=swEquipUnitNotifyBindings, swUnitFailure=swUnitFailure, swTemperatureTable=swTemperatureTable, swFanStatus=swFanStatus, swEquipTemperNotifyBindings=swEquipTemperNotifyBindings, swLowTemperatureRecoverSeverity=swLowTemperatureRecoverSeverity, swEquipTemperatureNotification=swEquipTemperatureNotification, swUnitMgmtBoxId=swUnitMgmtBoxId, swFanFailureSeverity=swFanFailureSeverity, swEquipmentCapacity=swEquipmentCapacity, swPowerRecover=swPowerRecover, swUnitInsert=swUnitInsert, swExternalAlarmStackingStatus=swExternalAlarmStackingStatus, swUnitStackingVersion=swUnitStackingVersion, swUnitMgmtModuleName=swUnitMgmtModuleName, swStackRoleChangeType=swStackRoleChangeType, swExternalAlarm=swExternalAlarm, swFanSpeed=swFanSpeed, swUnitTPChange=swUnitTPChange, swUnitMgmtSerialNumber=swUnitMgmtSerialNumber, swEquipExternalAlarmNotification=swEquipExternalAlarmNotification, swEquipmentPowerSaving=swEquipmentPowerSaving, swExternalAlarmStackingEntry=swExternalAlarmStackingEntry, swFanEntry=swFanEntry, swNotificationBindings=swNotificationBindings, swUnitMgmtHardwareVersion=swUnitMgmtHardwareVersion, swExternalAlarmStackingChannel=swExternalAlarmStackingChannel, swFanID=swFanID, swEquipPowerSavingLinkDetectState=swEquipPowerSavingLinkDetectState, swEquipmentNotifyMgmt=swEquipmentNotifyMgmt, swEquipPowerSavingPortEntry=swEquipPowerSavingPortEntry, swUnitStackForceMasterRole=swUnitStackForceMasterRole, PYSNMP_MODULE_ID=swEquipmentMIB, swUnitStackMode=swUnitStackMode, swPowerFailure=swPowerFailure, swUnitMgmtId=swUnitMgmtId, swEquipPowerSavingPortLEDState=swEquipPowerSavingPortLEDState, swUnitInsertSeverity=swUnitInsertSeverity, swEquipFanNotifyMgmt=swEquipFanNotifyMgmt, swExternalAlarmEntry=swExternalAlarmEntry, swFanUnitIndex=swFanUnitIndex, swTemperatureCurrent=swTemperatureCurrent, swUnitMgmtFirmwareVersion=swUnitMgmtFirmwareVersion, swExternalAlarmChannel=swExternalAlarmChannel, swUnitMgmtPortRange=swUnitMgmtPortRange, swEquipPowerSavingPortIndex=swEquipPowerSavingPortIndex, swEquipPowerSavingPortState=swEquipPowerSavingPortState, MacAddress=MacAddress, swExternalAlarmStackingTable=swExternalAlarmStackingTable, swEquipPowerSavingHibernationEntry=swEquipPowerSavingHibernationEntry, swHighTemperatureRecoverSeverity=swHighTemperatureRecoverSeverity, swUnitRoleChange=swUnitRoleChange, swExternalAlarmStackingMessage=swExternalAlarmStackingMessage, swEquipFanNotification=swEquipFanNotification, swExternalAlarmStacking=swExternalAlarmStacking, swEquipUnitNotifyPrefix=swEquipUnitNotifyPrefix, swEquipmentNotification=swEquipmentNotification, swUnitRemoveSeverity=swUnitRemoveSeverity, swUnitMaxSupportedUnits=swUnitMaxSupportedUnits, swEquipPowerSavingPortRowStatus=swEquipPowerSavingPortRowStatus, swEquipPowerNotifyMgmt=swEquipPowerNotifyMgmt, swEquipUnitNotification=swEquipUnitNotification, swEquipPowerSavingLenDetect=swEquipPowerSavingLenDetect, swTemperatureLogState=swTemperatureLogState, swUnitNumOfUnit=swUnitNumOfUnit, swPowerEntry=swPowerEntry, swEquipExternalAlarmNotifyPrefix=swEquipExternalAlarmNotifyPrefix, swUnitMgmtExistState=swUnitMgmtExistState, swUnitMgmtFrontPanelLedStatus=swUnitMgmtFrontPanelLedStatus, swUnitMgmtMacAddr=swUnitMgmtMacAddr, swFanRecoverSeverity=swFanRecoverSeverity, swLowTemperature=swLowTemperature, swEquipPowerSavingPortLedTable=swEquipPowerSavingPortLedTable, swTemperatureLowThresh=swTemperatureLowThresh, swFanFailure=swFanFailure, swUnitStackTrapState=swUnitStackTrapState, swPowerUnitIndex=swPowerUnitIndex, swEquipPowerSavingPortLedRowStatus=swEquipPowerSavingPortLedRowStatus, swExternalAlarmTable=swExternalAlarmTable, swPowerRecoverSeverity=swPowerRecoverSeverity, swEquipmentMIB=swEquipmentMIB, swEquipUnitNotifyMgmt=swEquipUnitNotifyMgmt, swLowTemperatureSeverity=swLowTemperatureSeverity, swEquipPowerSavingHiberRowStatus=swEquipPowerSavingHiberRowStatus, swEquipment=swEquipment, swEquipPowerSavingScheduleCtrl=swEquipPowerSavingScheduleCtrl, swEquipTemperatureNotifyPrefix=swEquipTemperatureNotifyPrefix, swUnitStackLogState=swUnitStackLogState, swFanTrapState=swFanTrapState, swHighTemperatureSeverity=swHighTemperatureSeverity, swEquipPowerSavingHiberState=swEquipPowerSavingHiberState, swUnitRemove=swUnitRemove, swEquipmentNotify=swEquipmentNotify, swEquipPowerNotifyPerfix=swEquipPowerNotifyPerfix, swPowerStatusChg=swPowerStatusChg, swTemperatureTrapState=swTemperatureTrapState, swUnitMgmtCtrlMode=swUnitMgmtCtrlMode, swEquipmentTemperatureCtrl=swEquipmentTemperatureCtrl, swEquipPowerNotification=swEquipPowerNotification, swLowTemperatureRecover=swLowTemperatureRecover, swEquipTemperatureNotifyMgmt=swEquipTemperatureNotifyMgmt, swHighTemperatureRecover=swHighTemperatureRecover, swUnitMgmtUserSetState=swUnitMgmtUserSetState, swExternalAlarmMessage=swExternalAlarmMessage, swTemperatureEntry=swTemperatureEntry, swUnitMgmt=swUnitMgmt, swPowerTable=swPowerTable, swPowerStatusChgSeverity=swPowerStatusChgSeverity, swTemperSensorID=swTemperSensorID, swEquipFanNotifyPrefix=swEquipFanNotifyPrefix, swEquipPowerSavingPortLedEntry=swEquipPowerSavingPortLedEntry, swFanTable=swFanTable, swPowerID=swPowerID, swExternalAlarmStackingUnitIndex=swExternalAlarmStackingUnitIndex, swFanNumber=swFanNumber, swEquipPowerSavingHibernationTable=swEquipPowerSavingHibernationTable, swPowerTrapState=swPowerTrapState, swFanPostion=swFanPostion, swTemperatureUnitIndex=swTemperatureUnitIndex, swHighTemperature=swHighTemperature, swUnitMgmtEntry=swUnitMgmtEntry, swUnitMgmtPriority=swUnitMgmtPriority, swUnitTopology=swUnitTopology, swUnitMgmtVersion=swUnitMgmtVersion, swEquipmentLEDCtrl=swEquipmentLEDCtrl, swFanRecover=swFanRecover, swEquipmentPortLEDState=swEquipmentPortLEDState, swUnitMgmtCurrentMode=swUnitMgmtCurrentMode, swStackTopologyType=swStackTopologyType, swUnitMgmtTable=swUnitMgmtTable)
