#
# PySNMP MIB module ONEFS-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ONEFS-TRAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:25:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
onefs, TimeTicks64 = mibBuilder.importSymbols("ONEFS-MIB", "onefs", "TimeTicks64")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
TimeTicks, ObjectIdentity, NotificationType, IpAddress, ModuleIdentity, Bits, MibIdentifier, iso, Integer32, Counter32, Counter64, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "NotificationType", "IpAddress", "ModuleIdentity", "Bits", "MibIdentifier", "iso", "Integer32", "Counter32", "Counter64", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
PhysAddress, DisplayString, TextualConvention, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress", "DisplayString", "TextualConvention", "MacAddress")
oneFSTraps = ModuleIdentity((1, 3, 6, 1, 4, 1, 12124, 251))
if mibBuilder.loadTexts: oneFSTraps.setLastUpdated('0201172301Z')
if mibBuilder.loadTexts: oneFSTraps.setOrganization('COMPANY_NAME')
oneFSTrapByPriority = MibIdentifier((1, 3, 6, 1, 4, 1, 12124, 251, 1))
oneFSTrapByFacility = MibIdentifier((1, 3, 6, 1, 4, 1, 12124, 251, 2))
oneFSTrapCrit = NotificationType((1, 3, 6, 1, 4, 1, 12124, 251, 1, 1))
if mibBuilder.loadTexts: oneFSTrapCrit.setStatus('current')
oneFSTrapWarn = NotificationType((1, 3, 6, 1, 4, 1, 12124, 251, 1, 2))
if mibBuilder.loadTexts: oneFSTrapWarn.setStatus('current')
oneFSTrapInfo = NotificationType((1, 3, 6, 1, 4, 1, 12124, 251, 1, 3))
if mibBuilder.loadTexts: oneFSTrapInfo.setStatus('current')
oneFSTrapEmrg = NotificationType((1, 3, 6, 1, 4, 1, 12124, 251, 1, 4))
if mibBuilder.loadTexts: oneFSTrapEmrg.setStatus('current')
oneFSTrapDefault = NotificationType((1, 3, 6, 1, 4, 1, 12124, 251, 2, 1))
if mibBuilder.loadTexts: oneFSTrapDefault.setStatus('current')
oneFSTrapNode = NotificationType((1, 3, 6, 1, 4, 1, 12124, 251, 2, 2))
if mibBuilder.loadTexts: oneFSTrapNode.setStatus('current')
oneFSTrapWindowsNetworking = NotificationType((1, 3, 6, 1, 4, 1, 12124, 251, 2, 3))
if mibBuilder.loadTexts: oneFSTrapWindowsNetworking.setStatus('current')
oneFSTrapProcesses = NotificationType((1, 3, 6, 1, 4, 1, 12124, 251, 2, 4))
if mibBuilder.loadTexts: oneFSTrapProcesses.setStatus('current')
oneFSTrapPower = NotificationType((1, 3, 6, 1, 4, 1, 12124, 251, 2, 5))
if mibBuilder.loadTexts: oneFSTrapPower.setStatus('current')
oneFSTrapSpace = NotificationType((1, 3, 6, 1, 4, 1, 12124, 251, 2, 6))
if mibBuilder.loadTexts: oneFSTrapSpace.setStatus('current')
oneFSTrapRestripe = NotificationType((1, 3, 6, 1, 4, 1, 12124, 251, 2, 7))
if mibBuilder.loadTexts: oneFSTrapRestripe.setStatus('current')
oneFSTrapGeneral = NotificationType((1, 3, 6, 1, 4, 1, 12124, 251, 2, 8))
if mibBuilder.loadTexts: oneFSTrapGeneral.setStatus('current')
oneFSTrapNVRAM = NotificationType((1, 3, 6, 1, 4, 1, 12124, 251, 2, 9))
if mibBuilder.loadTexts: oneFSTrapNVRAM.setStatus('current')
oneFSTrapTemp = NotificationType((1, 3, 6, 1, 4, 1, 12124, 251, 2, 10))
if mibBuilder.loadTexts: oneFSTrapTemp.setStatus('current')
oneFSTrapFan = NotificationType((1, 3, 6, 1, 4, 1, 12124, 251, 2, 11))
if mibBuilder.loadTexts: oneFSTrapFan.setStatus('current')
oneFSTrapFilesystem = NotificationType((1, 3, 6, 1, 4, 1, 12124, 251, 2, 12))
if mibBuilder.loadTexts: oneFSTrapFilesystem.setStatus('current')
oneFSTrapDisk = NotificationType((1, 3, 6, 1, 4, 1, 12124, 251, 2, 13))
if mibBuilder.loadTexts: oneFSTrapDisk.setStatus('current')
oneFSTrapCPU = NotificationType((1, 3, 6, 1, 4, 1, 12124, 251, 2, 14))
if mibBuilder.loadTexts: oneFSTrapCPU.setStatus('current')
oneFSTrapTest = NotificationType((1, 3, 6, 1, 4, 1, 12124, 251, 2, 15))
if mibBuilder.loadTexts: oneFSTrapTest.setStatus('current')
oneFSTrapLicensing = NotificationType((1, 3, 6, 1, 4, 1, 12124, 251, 2, 16))
if mibBuilder.loadTexts: oneFSTrapLicensing.setStatus('current')
oneFSTrapSnapshots = NotificationType((1, 3, 6, 1, 4, 1, 12124, 251, 2, 17))
if mibBuilder.loadTexts: oneFSTrapSnapshots.setStatus('current')
oneFSTrapSmartQuotas = NotificationType((1, 3, 6, 1, 4, 1, 12124, 251, 2, 18))
if mibBuilder.loadTexts: oneFSTrapSmartQuotas.setStatus('current')
mibBuilder.exportSymbols("ONEFS-TRAP-MIB", oneFSTrapLicensing=oneFSTrapLicensing, oneFSTrapCrit=oneFSTrapCrit, oneFSTrapCPU=oneFSTrapCPU, oneFSTrapWindowsNetworking=oneFSTrapWindowsNetworking, oneFSTrapDisk=oneFSTrapDisk, oneFSTrapInfo=oneFSTrapInfo, oneFSTrapSnapshots=oneFSTrapSnapshots, oneFSTrapRestripe=oneFSTrapRestripe, oneFSTrapGeneral=oneFSTrapGeneral, oneFSTrapEmrg=oneFSTrapEmrg, oneFSTrapFilesystem=oneFSTrapFilesystem, oneFSTrapProcesses=oneFSTrapProcesses, PYSNMP_MODULE_ID=oneFSTraps, oneFSTrapNode=oneFSTrapNode, oneFSTraps=oneFSTraps, oneFSTrapTest=oneFSTrapTest, oneFSTrapWarn=oneFSTrapWarn, oneFSTrapSmartQuotas=oneFSTrapSmartQuotas, oneFSTrapFan=oneFSTrapFan, oneFSTrapSpace=oneFSTrapSpace, oneFSTrapNVRAM=oneFSTrapNVRAM, oneFSTrapByPriority=oneFSTrapByPriority, oneFSTrapByFacility=oneFSTrapByFacility, oneFSTrapDefault=oneFSTrapDefault, oneFSTrapPower=oneFSTrapPower, oneFSTrapTemp=oneFSTrapTemp)
