#
# PySNMP MIB module CYAN-SHELF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CYAN-SHELF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:18:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
CyanTypeTc, cyanEntityModules = mibBuilder.importSymbols("CYAN-MIB", "CyanTypeTc", "cyanEntityModules")
CyanOpStateTc, CyanNoYesTc, CyanOpStateQualTc, CyanSecServiceStateTc = mibBuilder.importSymbols("CYAN-TC-MIB", "CyanOpStateTc", "CyanNoYesTc", "CyanOpStateQualTc", "CyanSecServiceStateTc")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter32, Unsigned32, Integer32, IpAddress, ObjectIdentity, Gauge32, Counter64, MibIdentifier, TimeTicks, NotificationType, iso, ModuleIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Unsigned32", "Integer32", "IpAddress", "ObjectIdentity", "Gauge32", "Counter64", "MibIdentifier", "TimeTicks", "NotificationType", "iso", "ModuleIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cyanShelfModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 28533, 5, 30, 20))
cyanShelfModule.setRevisions(('2014-12-07 05:45',))
if mibBuilder.loadTexts: cyanShelfModule.setLastUpdated('201412070545Z')
if mibBuilder.loadTexts: cyanShelfModule.setOrganization('Cyan, Inc.')
cyanShelfMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1))
cyanShelfTable = MibTable((1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1), )
if mibBuilder.loadTexts: cyanShelfTable.setStatus('current')
cyanShelfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1), ).setIndexNames((0, "CYAN-SHELF-MIB", "cyanShelfShelfId"))
if mibBuilder.loadTexts: cyanShelfEntry.setStatus('current')
cyanShelfShelfId = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: cyanShelfShelfId.setStatus('current')
cyanShelfAssetTag = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 124))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanShelfAssetTag.setStatus('current')
cyanShelfAutoprovisioningFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 3), CyanNoYesTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanShelfAutoprovisioningFlag.setStatus('current')
cyanShelfBaseMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanShelfBaseMacAddress.setStatus('current')
cyanShelfBay = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanShelfBay.setStatus('current')
cyanShelfDaysSinceLastReplacement = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanShelfDaysSinceLastReplacement.setStatus('current')
cyanShelfDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanShelfDescription.setStatus('current')
cyanShelfFanFilterReplacingIntervalDays = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanShelfFanFilterReplacingIntervalDays.setStatus('current')
cyanShelfFanSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanShelfFanSpeed.setStatus('current')
cyanShelfIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanShelfIdentifier.setStatus('current')
cyanShelfMacBlockSize = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanShelfMacBlockSize.setStatus('current')
cyanShelfMfgCleiCode = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanShelfMfgCleiCode.setStatus('current')
cyanShelfMfgEciCode = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanShelfMfgEciCode.setStatus('current')
cyanShelfMfgModuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanShelfMfgModuleId.setStatus('current')
cyanShelfMfgPartNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanShelfMfgPartNumber.setStatus('current')
cyanShelfMfgRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 16), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanShelfMfgRevision.setStatus('current')
cyanShelfMfgSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 17), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanShelfMfgSerialNumber.setStatus('current')
cyanShelfName = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 18), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanShelfName.setStatus('current')
cyanShelfOidClass = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 19), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanShelfOidClass.setStatus('current')
cyanShelfOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 20), CyanOpStateTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanShelfOperState.setStatus('current')
cyanShelfOperStateQual = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 21), CyanOpStateQualTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanShelfOperStateQual.setStatus('current')
cyanShelfOssLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 22), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanShelfOssLabel.setStatus('current')
cyanShelfOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 23), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanShelfOwner.setStatus('current')
cyanShelfRackUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 24), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanShelfRackUnits.setStatus('current')
cyanShelfRelayRack = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 25), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanShelfRelayRack.setStatus('current')
cyanShelfSecServState = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 26), CyanSecServiceStateTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanShelfSecServState.setStatus('current')
cyanShelfType = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 1, 1, 1, 27), CyanTypeTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanShelfType.setStatus('current')
cyanShelfObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 20)).setObjects(("CYAN-SHELF-MIB", "cyanShelfAssetTag"), ("CYAN-SHELF-MIB", "cyanShelfAutoprovisioningFlag"), ("CYAN-SHELF-MIB", "cyanShelfBaseMacAddress"), ("CYAN-SHELF-MIB", "cyanShelfBay"), ("CYAN-SHELF-MIB", "cyanShelfDaysSinceLastReplacement"), ("CYAN-SHELF-MIB", "cyanShelfDescription"), ("CYAN-SHELF-MIB", "cyanShelfFanFilterReplacingIntervalDays"), ("CYAN-SHELF-MIB", "cyanShelfFanSpeed"), ("CYAN-SHELF-MIB", "cyanShelfIdentifier"), ("CYAN-SHELF-MIB", "cyanShelfMacBlockSize"), ("CYAN-SHELF-MIB", "cyanShelfMfgCleiCode"), ("CYAN-SHELF-MIB", "cyanShelfMfgEciCode"), ("CYAN-SHELF-MIB", "cyanShelfMfgModuleId"), ("CYAN-SHELF-MIB", "cyanShelfMfgPartNumber"), ("CYAN-SHELF-MIB", "cyanShelfMfgRevision"), ("CYAN-SHELF-MIB", "cyanShelfMfgSerialNumber"), ("CYAN-SHELF-MIB", "cyanShelfName"), ("CYAN-SHELF-MIB", "cyanShelfOidClass"), ("CYAN-SHELF-MIB", "cyanShelfOperState"), ("CYAN-SHELF-MIB", "cyanShelfOperStateQual"), ("CYAN-SHELF-MIB", "cyanShelfOssLabel"), ("CYAN-SHELF-MIB", "cyanShelfOwner"), ("CYAN-SHELF-MIB", "cyanShelfRackUnits"), ("CYAN-SHELF-MIB", "cyanShelfRelayRack"), ("CYAN-SHELF-MIB", "cyanShelfSecServState"), ("CYAN-SHELF-MIB", "cyanShelfType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cyanShelfObjectGroup = cyanShelfObjectGroup.setStatus('current')
cyanShelfCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 28533, 5, 30, 20, 30)).setObjects(("CYAN-SHELF-MIB", "cyanShelfObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cyanShelfCompliance = cyanShelfCompliance.setStatus('current')
mibBuilder.exportSymbols("CYAN-SHELF-MIB", cyanShelfMfgSerialNumber=cyanShelfMfgSerialNumber, cyanShelfCompliance=cyanShelfCompliance, cyanShelfMacBlockSize=cyanShelfMacBlockSize, cyanShelfTable=cyanShelfTable, cyanShelfMfgPartNumber=cyanShelfMfgPartNumber, cyanShelfMfgCleiCode=cyanShelfMfgCleiCode, cyanShelfEntry=cyanShelfEntry, cyanShelfObjectGroup=cyanShelfObjectGroup, cyanShelfOperState=cyanShelfOperState, cyanShelfOperStateQual=cyanShelfOperStateQual, cyanShelfMibObjects=cyanShelfMibObjects, cyanShelfBaseMacAddress=cyanShelfBaseMacAddress, cyanShelfRelayRack=cyanShelfRelayRack, cyanShelfSecServState=cyanShelfSecServState, cyanShelfType=cyanShelfType, cyanShelfDescription=cyanShelfDescription, cyanShelfMfgModuleId=cyanShelfMfgModuleId, cyanShelfOssLabel=cyanShelfOssLabel, cyanShelfShelfId=cyanShelfShelfId, cyanShelfAssetTag=cyanShelfAssetTag, cyanShelfBay=cyanShelfBay, cyanShelfDaysSinceLastReplacement=cyanShelfDaysSinceLastReplacement, cyanShelfIdentifier=cyanShelfIdentifier, cyanShelfMfgRevision=cyanShelfMfgRevision, cyanShelfFanSpeed=cyanShelfFanSpeed, cyanShelfFanFilterReplacingIntervalDays=cyanShelfFanFilterReplacingIntervalDays, cyanShelfName=cyanShelfName, cyanShelfAutoprovisioningFlag=cyanShelfAutoprovisioningFlag, cyanShelfMfgEciCode=cyanShelfMfgEciCode, PYSNMP_MODULE_ID=cyanShelfModule, cyanShelfRackUnits=cyanShelfRackUnits, cyanShelfModule=cyanShelfModule, cyanShelfOidClass=cyanShelfOidClass, cyanShelfOwner=cyanShelfOwner)
