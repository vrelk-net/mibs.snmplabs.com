#
# PySNMP MIB module CHECKPOINT-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CHECKPOINT-TRAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:31:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
tempertureSensorStatus, haProblemVerified, fanSpeedSensorType, multiDiskFreeAvailablePercent, raidDiskID, memActiveReal64, haBlockState, haProblemPriority, voltageSensorName, svnNetIfState, fwLSConnState, fanSpeedSensorValue, haIfName, raidVolumeID, voltageSensorType, voltageSensorValue, raidDiskFlags, multiDiskName, fwLocalLoggingStat, fanSpeedSensorStatus, haIP, fanSpeedSensorUnit, tempertureSensorName, haTrusted, haStatShort, haStatus, multiProcIndex, svnNetIfName, haState, multiProcRunQueue, voltageSensorUnit, multiProcUsage, memTotalReal64, multiProcInterrupts, multiProcSystemTime, voltageSensorStatus, tempertureSensorUnit, haProblemStatus, tempertureSensorValue, fwLSConnOverall, fwLSConnStateDesc, fanSpeedSensorName, raidVolumeState, raidDiskVolumeID, fwLSConnOverallDesc, haIdentifier, memTotalVirtual64, memActiveVirtual64, raidDiskState, haStatCode, haStatLong, haProblemName, multiProcIdleTime, haProblemDescr, fwLSConnName, multiProcUserTime, fwLocalLoggingDesc, tempertureSensorType, haShared, svnNetIfAddress, svnNetIfOperState = mibBuilder.importSymbols("CHECKPOINT-MIB", "tempertureSensorStatus", "haProblemVerified", "fanSpeedSensorType", "multiDiskFreeAvailablePercent", "raidDiskID", "memActiveReal64", "haBlockState", "haProblemPriority", "voltageSensorName", "svnNetIfState", "fwLSConnState", "fanSpeedSensorValue", "haIfName", "raidVolumeID", "voltageSensorType", "voltageSensorValue", "raidDiskFlags", "multiDiskName", "fwLocalLoggingStat", "fanSpeedSensorStatus", "haIP", "fanSpeedSensorUnit", "tempertureSensorName", "haTrusted", "haStatShort", "haStatus", "multiProcIndex", "svnNetIfName", "haState", "multiProcRunQueue", "voltageSensorUnit", "multiProcUsage", "memTotalReal64", "multiProcInterrupts", "multiProcSystemTime", "voltageSensorStatus", "tempertureSensorUnit", "haProblemStatus", "tempertureSensorValue", "fwLSConnOverall", "fwLSConnStateDesc", "fanSpeedSensorName", "raidVolumeState", "raidDiskVolumeID", "fwLSConnOverallDesc", "haIdentifier", "memTotalVirtual64", "memActiveVirtual64", "raidDiskState", "haStatCode", "haStatLong", "haProblemName", "multiProcIdleTime", "haProblemDescr", "fwLSConnName", "multiProcUserTime", "fwLocalLoggingDesc", "tempertureSensorType", "haShared", "svnNetIfAddress", "svnNetIfOperState")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, NotificationType, iso, Integer32, IpAddress, TimeTicks, ObjectIdentity, Bits, Unsigned32, MibIdentifier, ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "iso", "Integer32", "IpAddress", "TimeTicks", "ObjectIdentity", "Bits", "Unsigned32", "MibIdentifier", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
chkpntTrapMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 0))
chkpntTrapMibModule.setRevisions(('2013-12-26 13:09',))
if mibBuilder.loadTexts: chkpntTrapMibModule.setLastUpdated('201312261309Z')
if mibBuilder.loadTexts: chkpntTrapMibModule.setOrganization('Check Point')
checkpoint = MibIdentifier((1, 3, 6, 1, 4, 1, 2620))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 2620, 1))
chkpntTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 2620, 1, 2000))
chkpntTrapInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0))
chkpntTrapNet = MibIdentifier((1, 3, 6, 1, 4, 1, 2620, 1, 2000, 1))
chkpntTrapDisk = MibIdentifier((1, 3, 6, 1, 4, 1, 2620, 1, 2000, 2))
chkpntTrapCPU = MibIdentifier((1, 3, 6, 1, 4, 1, 2620, 1, 2000, 3))
chkpntTrapMemory = MibIdentifier((1, 3, 6, 1, 4, 1, 2620, 1, 2000, 4))
chkpntTrapHWSensor = MibIdentifier((1, 3, 6, 1, 4, 1, 2620, 1, 2000, 5))
chkpntTrapHA = MibIdentifier((1, 3, 6, 1, 4, 1, 2620, 1, 2000, 6))
chkpntTrapLSConn = MibIdentifier((1, 3, 6, 1, 4, 1, 2620, 1, 2000, 7))
chkpntTrapOID = MibScalar((1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chkpntTrapOID.setStatus('current')
chkpntTrapOIDValue = MibScalar((1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chkpntTrapOIDValue.setStatus('current')
chkpntTrapMsgText = MibScalar((1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chkpntTrapMsgText.setStatus('current')
chkpntTrapSeverity = MibScalar((1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chkpntTrapSeverity.setStatus('current')
chkpntTrapCategory = MibScalar((1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chkpntTrapCategory.setStatus('current')
chkpntDiskSpaceTrap = NotificationType((1, 3, 6, 1, 4, 1, 2620, 1, 2000, 2, 1)).setObjects(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"), ("CHECKPOINT-MIB", "multiDiskName"), ("CHECKPOINT-MIB", "multiDiskFreeAvailablePercent"))
if mibBuilder.loadTexts: chkpntDiskSpaceTrap.setStatus('current')
chkpntRAIDVolumeTrap = NotificationType((1, 3, 6, 1, 4, 1, 2620, 1, 2000, 2, 2)).setObjects(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"), ("CHECKPOINT-MIB", "raidVolumeID"), ("CHECKPOINT-MIB", "raidVolumeState"))
if mibBuilder.loadTexts: chkpntRAIDVolumeTrap.setStatus('current')
chkpntRAIDDiskTrap = NotificationType((1, 3, 6, 1, 4, 1, 2620, 1, 2000, 2, 3)).setObjects(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"), ("CHECKPOINT-MIB", "raidDiskVolumeID"), ("CHECKPOINT-MIB", "raidDiskID"), ("CHECKPOINT-MIB", "raidDiskState"))
if mibBuilder.loadTexts: chkpntRAIDDiskTrap.setStatus('current')
chkpntRAIDDiskFlagsTrap = NotificationType((1, 3, 6, 1, 4, 1, 2620, 1, 2000, 2, 4)).setObjects(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"), ("CHECKPOINT-MIB", "raidDiskVolumeID"), ("CHECKPOINT-MIB", "raidDiskID"), ("CHECKPOINT-MIB", "raidDiskState"), ("CHECKPOINT-MIB", "raidDiskFlags"))
if mibBuilder.loadTexts: chkpntRAIDDiskFlagsTrap.setStatus('current')
chkpntTrapNetIfState = NotificationType((1, 3, 6, 1, 4, 1, 2620, 1, 2000, 1, 1)).setObjects(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"), ("CHECKPOINT-MIB", "svnNetIfName"), ("CHECKPOINT-MIB", "svnNetIfAddress"), ("CHECKPOINT-MIB", "svnNetIfState"))
if mibBuilder.loadTexts: chkpntTrapNetIfState.setStatus('current')
chkpntTrapNetIfUnplugged = NotificationType((1, 3, 6, 1, 4, 1, 2620, 1, 2000, 1, 2)).setObjects(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"), ("CHECKPOINT-MIB", "svnNetIfName"), ("CHECKPOINT-MIB", "svnNetIfAddress"))
if mibBuilder.loadTexts: chkpntTrapNetIfUnplugged.setStatus('current')
chkpntTrapNewConnRate = NotificationType((1, 3, 6, 1, 4, 1, 2620, 1, 2000, 1, 3)).setObjects(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"))
if mibBuilder.loadTexts: chkpntTrapNewConnRate.setStatus('current')
chkpntTrapConcurrentConnRate = NotificationType((1, 3, 6, 1, 4, 1, 2620, 1, 2000, 1, 4)).setObjects(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"))
if mibBuilder.loadTexts: chkpntTrapConcurrentConnRate.setStatus('current')
chkpntTrapBytesThroughput = NotificationType((1, 3, 6, 1, 4, 1, 2620, 1, 2000, 1, 5)).setObjects(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"))
if mibBuilder.loadTexts: chkpntTrapBytesThroughput.setStatus('current')
chkpntTrapAcceptedPacketRate = NotificationType((1, 3, 6, 1, 4, 1, 2620, 1, 2000, 1, 6)).setObjects(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"))
if mibBuilder.loadTexts: chkpntTrapAcceptedPacketRate.setStatus('current')
chkpntTrapNetIfOperState = NotificationType((1, 3, 6, 1, 4, 1, 2620, 1, 2000, 1, 7)).setObjects(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"), ("CHECKPOINT-MIB", "svnNetIfName"), ("CHECKPOINT-MIB", "svnNetIfAddress"), ("CHECKPOINT-MIB", "svnNetIfOperState"))
if mibBuilder.loadTexts: chkpntTrapNetIfOperState.setStatus('current')
chkpntCPUCoreUtilTrap = NotificationType((1, 3, 6, 1, 4, 1, 2620, 1, 2000, 3, 1)).setObjects(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"), ("CHECKPOINT-MIB", "multiProcIndex"), ("CHECKPOINT-MIB", "multiProcUserTime"), ("CHECKPOINT-MIB", "multiProcSystemTime"), ("CHECKPOINT-MIB", "multiProcIdleTime"), ("CHECKPOINT-MIB", "multiProcUsage"), ("CHECKPOINT-MIB", "multiProcRunQueue"), ("CHECKPOINT-MIB", "multiProcInterrupts"))
if mibBuilder.loadTexts: chkpntCPUCoreUtilTrap.setStatus('current')
chkpntCPUCoreInterruptsTrap = NotificationType((1, 3, 6, 1, 4, 1, 2620, 1, 2000, 3, 2)).setObjects(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"), ("CHECKPOINT-MIB", "multiProcIndex"), ("CHECKPOINT-MIB", "multiProcUserTime"), ("CHECKPOINT-MIB", "multiProcSystemTime"), ("CHECKPOINT-MIB", "multiProcIdleTime"), ("CHECKPOINT-MIB", "multiProcUsage"), ("CHECKPOINT-MIB", "multiProcRunQueue"), ("CHECKPOINT-MIB", "multiProcInterrupts"))
if mibBuilder.loadTexts: chkpntCPUCoreInterruptsTrap.setStatus('current')
chkpntSwapMemoryTrap = NotificationType((1, 3, 6, 1, 4, 1, 2620, 1, 2000, 4, 1)).setObjects(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"), ("CHECKPOINT-MIB", "memTotalVirtual64"), ("CHECKPOINT-MIB", "memActiveVirtual64"))
if mibBuilder.loadTexts: chkpntSwapMemoryTrap.setStatus('current')
chkpntRealMemoryTrap = NotificationType((1, 3, 6, 1, 4, 1, 2620, 1, 2000, 4, 2)).setObjects(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"), ("CHECKPOINT-MIB", "memTotalReal64"), ("CHECKPOINT-MIB", "memActiveReal64"))
if mibBuilder.loadTexts: chkpntRealMemoryTrap.setStatus('current')
chkpntTrapTempertureSensor = MibIdentifier((1, 3, 6, 1, 4, 1, 2620, 1, 2000, 5, 1))
chkpntTrapFanSpeedSensor = MibIdentifier((1, 3, 6, 1, 4, 1, 2620, 1, 2000, 5, 2))
chkpntTrapVoltageSensor = MibIdentifier((1, 3, 6, 1, 4, 1, 2620, 1, 2000, 5, 3))
chkpntTempertureTrap = NotificationType((1, 3, 6, 1, 4, 1, 2620, 1, 2000, 5, 1, 1)).setObjects(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"), ("CHECKPOINT-MIB", "tempertureSensorName"), ("CHECKPOINT-MIB", "tempertureSensorValue"), ("CHECKPOINT-MIB", "tempertureSensorUnit"), ("CHECKPOINT-MIB", "tempertureSensorType"), ("CHECKPOINT-MIB", "tempertureSensorStatus"))
if mibBuilder.loadTexts: chkpntTempertureTrap.setStatus('current')
chkpntFanSpeedTrap = NotificationType((1, 3, 6, 1, 4, 1, 2620, 1, 2000, 5, 2, 1)).setObjects(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"), ("CHECKPOINT-MIB", "fanSpeedSensorName"), ("CHECKPOINT-MIB", "fanSpeedSensorValue"), ("CHECKPOINT-MIB", "fanSpeedSensorUnit"), ("CHECKPOINT-MIB", "fanSpeedSensorType"), ("CHECKPOINT-MIB", "fanSpeedSensorStatus"))
if mibBuilder.loadTexts: chkpntFanSpeedTrap.setStatus('current')
chkpntVoltageTrap = NotificationType((1, 3, 6, 1, 4, 1, 2620, 1, 2000, 5, 3, 1)).setObjects(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"), ("CHECKPOINT-MIB", "voltageSensorName"), ("CHECKPOINT-MIB", "voltageSensorValue"), ("CHECKPOINT-MIB", "voltageSensorUnit"), ("CHECKPOINT-MIB", "voltageSensorType"), ("CHECKPOINT-MIB", "voltageSensorStatus"))
if mibBuilder.loadTexts: chkpntVoltageTrap.setStatus('current')
chkpntClusterMemberStateTrap = NotificationType((1, 3, 6, 1, 4, 1, 2620, 1, 2000, 6, 1)).setObjects(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"), ("CHECKPOINT-MIB", "haIdentifier"), ("CHECKPOINT-MIB", "haState"))
if mibBuilder.loadTexts: chkpntClusterMemberStateTrap.setStatus('current')
chkpntClusterBlockStateTrap = NotificationType((1, 3, 6, 1, 4, 1, 2620, 1, 2000, 6, 2)).setObjects(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"), ("CHECKPOINT-MIB", "haIdentifier"), ("CHECKPOINT-MIB", "haBlockState"), ("CHECKPOINT-MIB", "haState"))
if mibBuilder.loadTexts: chkpntClusterBlockStateTrap.setStatus('current')
chkpntClusterStateTrap = NotificationType((1, 3, 6, 1, 4, 1, 2620, 1, 2000, 6, 3)).setObjects(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"), ("CHECKPOINT-MIB", "haIdentifier"), ("CHECKPOINT-MIB", "haBlockState"), ("CHECKPOINT-MIB", "haState"), ("CHECKPOINT-MIB", "haStatCode"), ("CHECKPOINT-MIB", "haStatShort"), ("CHECKPOINT-MIB", "haStatLong"))
if mibBuilder.loadTexts: chkpntClusterStateTrap.setStatus('current')
chkpntClusterProblemStateTrap = NotificationType((1, 3, 6, 1, 4, 1, 2620, 1, 2000, 6, 4)).setObjects(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"), ("CHECKPOINT-MIB", "haProblemName"), ("CHECKPOINT-MIB", "haProblemStatus"), ("CHECKPOINT-MIB", "haProblemPriority"), ("CHECKPOINT-MIB", "haProblemVerified"), ("CHECKPOINT-MIB", "haProblemDescr"))
if mibBuilder.loadTexts: chkpntClusterProblemStateTrap.setStatus('current')
chkpntClusterInterfaceStateTrap = NotificationType((1, 3, 6, 1, 4, 1, 2620, 1, 2000, 6, 5)).setObjects(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"), ("CHECKPOINT-MIB", "haIfName"), ("CHECKPOINT-MIB", "haIP"), ("CHECKPOINT-MIB", "haStatus"), ("CHECKPOINT-MIB", "haTrusted"), ("CHECKPOINT-MIB", "haShared"))
if mibBuilder.loadTexts: chkpntClusterInterfaceStateTrap.setStatus('current')
chkpntTrapLSConnState = NotificationType((1, 3, 6, 1, 4, 1, 2620, 1, 2000, 7, 1)).setObjects(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"), ("CHECKPOINT-MIB", "fwLSConnName"), ("CHECKPOINT-MIB", "fwLSConnState"), ("CHECKPOINT-MIB", "fwLSConnStateDesc"), ("CHECKPOINT-MIB", "fwLocalLoggingDesc"), ("CHECKPOINT-MIB", "fwLocalLoggingStat"))
if mibBuilder.loadTexts: chkpntTrapLSConnState.setStatus('current')
chkpntTrapOverallLSConnState = NotificationType((1, 3, 6, 1, 4, 1, 2620, 1, 2000, 7, 2)).setObjects(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"), ("CHECKPOINT-MIB", "fwLSConnOverall"), ("CHECKPOINT-MIB", "fwLSConnOverallDesc"), ("CHECKPOINT-MIB", "fwLocalLoggingDesc"), ("CHECKPOINT-MIB", "fwLocalLoggingStat"))
if mibBuilder.loadTexts: chkpntTrapOverallLSConnState.setStatus('current')
chkpntTrapLocalLoggingState = NotificationType((1, 3, 6, 1, 4, 1, 2620, 1, 2000, 7, 3)).setObjects(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"), ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"), ("CHECKPOINT-MIB", "fwLSConnOverall"), ("CHECKPOINT-MIB", "fwLSConnOverallDesc"), ("CHECKPOINT-MIB", "fwLocalLoggingDesc"), ("CHECKPOINT-MIB", "fwLocalLoggingStat"))
if mibBuilder.loadTexts: chkpntTrapLocalLoggingState.setStatus('current')
mibBuilder.exportSymbols("CHECKPOINT-TRAP-MIB", chkpntTrapBytesThroughput=chkpntTrapBytesThroughput, chkpntClusterBlockStateTrap=chkpntClusterBlockStateTrap, chkpntTrap=chkpntTrap, chkpntRAIDDiskTrap=chkpntRAIDDiskTrap, chkpntCPUCoreInterruptsTrap=chkpntCPUCoreInterruptsTrap, chkpntTempertureTrap=chkpntTempertureTrap, chkpntTrapConcurrentConnRate=chkpntTrapConcurrentConnRate, chkpntTrapNewConnRate=chkpntTrapNewConnRate, chkpntFanSpeedTrap=chkpntFanSpeedTrap, chkpntSwapMemoryTrap=chkpntSwapMemoryTrap, chkpntVoltageTrap=chkpntVoltageTrap, chkpntTrapFanSpeedSensor=chkpntTrapFanSpeedSensor, chkpntCPUCoreUtilTrap=chkpntCPUCoreUtilTrap, chkpntTrapMsgText=chkpntTrapMsgText, checkpoint=checkpoint, chkpntRealMemoryTrap=chkpntRealMemoryTrap, chkpntTrapOID=chkpntTrapOID, chkpntTrapSeverity=chkpntTrapSeverity, chkpntClusterStateTrap=chkpntClusterStateTrap, chkpntTrapOverallLSConnState=chkpntTrapOverallLSConnState, chkpntTrapTempertureSensor=chkpntTrapTempertureSensor, chkpntClusterProblemStateTrap=chkpntClusterProblemStateTrap, chkpntClusterInterfaceStateTrap=chkpntClusterInterfaceStateTrap, chkpntTrapHWSensor=chkpntTrapHWSensor, chkpntTrapCategory=chkpntTrapCategory, chkpntTrapLocalLoggingState=chkpntTrapLocalLoggingState, chkpntTrapLSConnState=chkpntTrapLSConnState, chkpntTrapLSConn=chkpntTrapLSConn, chkpntTrapMibModule=chkpntTrapMibModule, chkpntTrapMemory=chkpntTrapMemory, chkpntTrapNetIfUnplugged=chkpntTrapNetIfUnplugged, chkpntTrapCPU=chkpntTrapCPU, chkpntDiskSpaceTrap=chkpntDiskSpaceTrap, products=products, chkpntTrapNet=chkpntTrapNet, chkpntTrapAcceptedPacketRate=chkpntTrapAcceptedPacketRate, chkpntTrapNetIfOperState=chkpntTrapNetIfOperState, chkpntTrapNetIfState=chkpntTrapNetIfState, chkpntTrapOIDValue=chkpntTrapOIDValue, chkpntRAIDVolumeTrap=chkpntRAIDVolumeTrap, chkpntClusterMemberStateTrap=chkpntClusterMemberStateTrap, chkpntTrapInfo=chkpntTrapInfo, chkpntRAIDDiskFlagsTrap=chkpntRAIDDiskFlagsTrap, chkpntTrapHA=chkpntTrapHA, chkpntTrapVoltageSensor=chkpntTrapVoltageSensor, chkpntTrapDisk=chkpntTrapDisk, PYSNMP_MODULE_ID=chkpntTrapMibModule)
