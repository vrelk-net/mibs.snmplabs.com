#
# PySNMP MIB module NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP
# Produced by pysmi-0.3.4 at Mon Apr 29 20:13:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
NoiEventTime, NoiAdditionalText, NoiAlarmTableCount = mibBuilder.importSymbols("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-COMMON-DEFINITION", "NoiEventTime", "NoiAdditionalText", "NoiAlarmTableCount")
NoiMeasurementActivationError, NoiMeasurementFileTransfer, NoiMeasurementResultIdentifier, NoiMeasurementResultTransfer, NoiMeasurementJobStatus, NoiMeasurementFileName, NoiMeasurementFileDirectory = mibBuilder.importSymbols("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-COMMON-DEFINITION", "NoiMeasurementActivationError", "NoiMeasurementFileTransfer", "NoiMeasurementResultIdentifier", "NoiMeasurementResultTransfer", "NoiMeasurementJobStatus", "NoiMeasurementFileName", "NoiMeasurementFileDirectory")
noiPmCompliance, noiPmNotification, noiPmTable, noiOpenInterfaceModule, noiPmVariable = mibBuilder.importSymbols("NOKIA-NE3S-REGISTRATION-MIB", "noiPmCompliance", "noiPmNotification", "noiPmTable", "noiOpenInterfaceModule", "noiPmVariable")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Integer32, IpAddress, iso, Counter64, Bits, Gauge32, ObjectIdentity, Unsigned32, NotificationType, MibIdentifier, TimeTicks, Counter32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "iso", "Counter64", "Bits", "Gauge32", "ObjectIdentity", "Unsigned32", "NotificationType", "MibIdentifier", "TimeTicks", "Counter32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
noiSnmpPmIrp = ModuleIdentity((1, 3, 6, 1, 4, 1, 94, 7, 1, 1, 4))
noiSnmpPmIrp.setRevisions(('1970-01-01 00:00',))
if mibBuilder.loadTexts: noiSnmpPmIrp.setLastUpdated('200227020000Z')
if mibBuilder.loadTexts: noiSnmpPmIrp.setOrganization('Nokia Networks')
noiPmIrpVersion = MibScalar((1, 3, 6, 1, 4, 1, 94, 7, 3, 2, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiPmIrpVersion.setStatus('current')
noiPmFileTransferProtocol = MibScalar((1, 3, 6, 1, 4, 1, 94, 7, 3, 2, 2), NoiMeasurementFileTransfer()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: noiPmFileTransferProtocol.setStatus('current')
noiPmResultTransfer = MibScalar((1, 3, 6, 1, 4, 1, 94, 7, 3, 2, 3), NoiMeasurementResultTransfer()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: noiPmResultTransfer.setStatus('current')
noiMeasurementScheduleFileDirectory = MibScalar((1, 3, 6, 1, 4, 1, 94, 7, 3, 2, 4), NoiMeasurementFileDirectory()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: noiMeasurementScheduleFileDirectory.setStatus('current')
noiMeasurementRepositoryDirectory = MibScalar((1, 3, 6, 1, 4, 1, 94, 7, 3, 2, 5), NoiMeasurementFileDirectory()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: noiMeasurementRepositoryDirectory.setStatus('current')
noiMeasurementRepositoryFile = MibScalar((1, 3, 6, 1, 4, 1, 94, 7, 3, 2, 6), NoiMeasurementFileName()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: noiMeasurementRepositoryFile.setStatus('current')
noiMeasurementJobStatus = MibScalar((1, 3, 6, 1, 4, 1, 94, 7, 3, 2, 7), NoiMeasurementJobStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: noiMeasurementJobStatus.setStatus('current')
noiMeasurementActivationError = MibScalar((1, 3, 6, 1, 4, 1, 94, 7, 3, 2, 8), NoiMeasurementActivationError()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiMeasurementActivationError.setStatus('current')
noiPmAdditionalText = MibScalar((1, 3, 6, 1, 4, 1, 94, 7, 3, 2, 9), NoiAdditionalText()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiPmAdditionalText.setStatus('current')
noiPmFileStoringPeriod = MibScalar((1, 3, 6, 1, 4, 1, 94, 7, 3, 2, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: noiPmFileStoringPeriod.setStatus('current')
noiMeasurementResultTableCount = MibScalar((1, 3, 6, 1, 4, 1, 94, 7, 3, 4, 1), NoiAlarmTableCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiMeasurementResultTableCount.setStatus('current')
noiMeasurementResultTableMaxCount = MibScalar((1, 3, 6, 1, 4, 1, 94, 7, 3, 4, 2), NoiAlarmTableCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiMeasurementResultTableMaxCount.setStatus('current')
noiPmLastMeasurementResultId = MibScalar((1, 3, 6, 1, 4, 1, 94, 7, 3, 4, 3), NoiMeasurementResultIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiPmLastMeasurementResultId.setStatus('current')
noiMeasurementResultTable = MibTable((1, 3, 6, 1, 4, 1, 94, 7, 3, 4, 4), )
if mibBuilder.loadTexts: noiMeasurementResultTable.setStatus('current')
noiMeasurementResultEntry = MibTableRow((1, 3, 6, 1, 4, 1, 94, 7, 3, 4, 4, 1), ).setIndexNames((0, "NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiMeasurementResultIdentifier"))
if mibBuilder.loadTexts: noiMeasurementResultEntry.setStatus('current')
noiMeasurementResultIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 7, 3, 4, 4, 1, 1), NoiMeasurementResultIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiMeasurementResultIdentifier.setStatus('current')
noiMeasurementFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 7, 3, 4, 4, 1, 2), NoiMeasurementFileName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiMeasurementFileName.setStatus('current')
noiMeasurementFileDirectory = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 7, 3, 4, 4, 1, 3), NoiMeasurementFileDirectory()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiMeasurementFileDirectory.setStatus('current')
noiPmEventTime = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 7, 3, 4, 4, 1, 4), NoiEventTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: noiPmEventTime.setStatus('current')
noiMeasurementResultReady = NotificationType((1, 3, 6, 1, 4, 1, 94, 7, 3, 3, 0, 1)).setObjects(("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiMeasurementResultIdentifier"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiMeasurementFileDirectory"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiMeasurementFileName"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiPmEventTime"))
if mibBuilder.loadTexts: noiMeasurementResultReady.setStatus('current')
noiMeasurementResultTableRebuild = NotificationType((1, 3, 6, 1, 4, 1, 94, 7, 3, 3, 0, 2)).setObjects(("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiPmAdditionalText"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiPmEventTime"))
if mibBuilder.loadTexts: noiMeasurementResultTableRebuild.setStatus('current')
noiPmIRPCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 94, 7, 3, 6, 1)).setObjects(("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiPmMandatoryGroup"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiPmNotificationOptionalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    noiPmIRPCompliance = noiPmIRPCompliance.setStatus('current')
noiPmMandatoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 94, 7, 3, 6, 2)).setObjects(("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiPmIrpVersion"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiPmLastMeasurementResultId"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiMeasurementScheduleFileDirectory"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiMeasurementResultTableCount"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiMeasurementResultTableMaxCount"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiMeasurementResultIdentifier"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiMeasurementFileDirectory"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiMeasurementFileName"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiPmEventTime"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiPmFileStoringPeriod"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    noiPmMandatoryGroup = noiPmMandatoryGroup.setStatus('current')
noiPmNotificationOptionalGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 94, 7, 3, 6, 3)).setObjects(("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiMeasurementResultReady"), ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiMeasurementResultTableRebuild"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    noiPmNotificationOptionalGroup = noiPmNotificationOptionalGroup.setStatus('current')
mibBuilder.exportSymbols("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", noiMeasurementResultTable=noiMeasurementResultTable, noiPmEventTime=noiPmEventTime, noiMeasurementFileName=noiMeasurementFileName, noiPmFileTransferProtocol=noiPmFileTransferProtocol, noiMeasurementResultIdentifier=noiMeasurementResultIdentifier, noiMeasurementResultTableCount=noiMeasurementResultTableCount, noiMeasurementRepositoryDirectory=noiMeasurementRepositoryDirectory, noiMeasurementResultReady=noiMeasurementResultReady, noiMeasurementActivationError=noiMeasurementActivationError, noiPmAdditionalText=noiPmAdditionalText, noiMeasurementRepositoryFile=noiMeasurementRepositoryFile, noiSnmpPmIrp=noiSnmpPmIrp, noiPmIRPCompliance=noiPmIRPCompliance, noiMeasurementResultTableRebuild=noiMeasurementResultTableRebuild, noiPmResultTransfer=noiPmResultTransfer, PYSNMP_MODULE_ID=noiSnmpPmIrp, noiMeasurementResultEntry=noiMeasurementResultEntry, noiMeasurementScheduleFileDirectory=noiMeasurementScheduleFileDirectory, noiMeasurementResultTableMaxCount=noiMeasurementResultTableMaxCount, noiPmIrpVersion=noiPmIrpVersion, noiMeasurementJobStatus=noiMeasurementJobStatus, noiPmLastMeasurementResultId=noiPmLastMeasurementResultId, noiMeasurementFileDirectory=noiMeasurementFileDirectory, noiPmFileStoringPeriod=noiPmFileStoringPeriod, noiPmNotificationOptionalGroup=noiPmNotificationOptionalGroup, noiPmMandatoryGroup=noiPmMandatoryGroup)