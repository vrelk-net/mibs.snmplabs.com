#
# PySNMP MIB module CADANT-SW-MEAS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CADANT-SW-MEAS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:28:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
cadExperimental, = mibBuilder.importSymbols("CADANT-PRODUCTS-MIB", "cadExperimental")
CardId, = mibBuilder.importSymbols("CADANT-TC", "CardId")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, MibIdentifier, Counter64, iso, TimeTicks, ObjectIdentity, Counter32, Unsigned32, Bits, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "Counter64", "iso", "TimeTicks", "ObjectIdentity", "Counter32", "Unsigned32", "Bits", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "ModuleIdentity")
MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString")
cadSoftwareMeasMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9))
cadSoftwareMeasMib.setRevisions(('2014-09-04 00:00', '2012-07-07 00:00', '2006-12-14 00:00', '2006-04-14 00:00', '2006-02-08 00:00', '2006-01-30 00:00', '2006-01-24 00:00', '2006-01-10 00:00', '2005-10-11 00:00', '2005-08-18 00:00', '2003-12-22 00:00', '2001-10-23 00:00',))
if mibBuilder.loadTexts: cadSoftwareMeasMib.setLastUpdated('201409040000Z')
if mibBuilder.loadTexts: cadSoftwareMeasMib.setOrganization('Arris International, Inc.')
cadChassisScaleGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 1))
cadantTotalDevices = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadantTotalDevices.setStatus('current')
cadantDsBondedDevices = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadantDsBondedDevices.setStatus('current')
cadantUsBondedDevices = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadantUsBondedDevices.setStatus('current')
cadantTotalServiceFlows = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadantTotalServiceFlows.setStatus('current')
cadantTotalClassifiers = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadantTotalClassifiers.setStatus('current')
cadantTotalArpEntries = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadantTotalArpEntries.setStatus('current')
cadantTotalIpv4Routes = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadantTotalIpv4Routes.setStatus('current')
cadantTotalNdEntries = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadantTotalNdEntries.setStatus('current')
cadantTotalIpv6Routes = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadantTotalIpv6Routes.setStatus('current')
cadantDocsisMulticastStreams = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadantDocsisMulticastStreams.setStatus('current')
cadantVideoMulticastStreams = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadantVideoMulticastStreams.setStatus('current')
cadantTotalCpe = MibScalar((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadantTotalCpe.setStatus('current')
cadSWUChannelMeasTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 2), )
if mibBuilder.loadTexts: cadSWUChannelMeasTable.setStatus('current')
cadSWUChannelMeasEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cadSWUChannelMeasEntry.setStatus('current')
cadUpChannelRequestSizeMslots = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 2, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadUpChannelRequestSizeMslots.setStatus('current')
cadUpChannelInitialMaintSizeMslots = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 2, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadUpChannelInitialMaintSizeMslots.setStatus('current')
cadUpChannelIngressCancellationBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: cadUpChannelIngressCancellationBandwidth.setStatus('current')
cadUpChannelAttenuation = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadUpChannelAttenuation.setStatus('current')
cadUpChannelRFCalibration = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 2, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadUpChannelRFCalibration.setStatus('current')
cadUpChannelTScale = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadUpChannelTScale.setStatus('current')
cadUpChannelSScale = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadUpChannelSScale.setStatus('current')
cadUpChannelStatsTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 3), )
if mibBuilder.loadTexts: cadUpChannelStatsTable.setStatus('current')
cadUpChannelStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cadUpChannelStatsEntry.setStatus('current')
cadUpChannelMaxUGSLastOneHour = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 3, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadUpChannelMaxUGSLastOneHour.setStatus('current')
cadUpChannelAvgUGSLastOneHour = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 3, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadUpChannelAvgUGSLastOneHour.setStatus('current')
cadUpChannelMinUGSLastOneHour = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 3, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadUpChannelMinUGSLastOneHour.setStatus('current')
cadUpChannelMaxUGSLastFiveMins = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 3, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadUpChannelMaxUGSLastFiveMins.setStatus('current')
cadUpChannelAvgUGSLastFiveMins = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 3, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadUpChannelAvgUGSLastFiveMins.setStatus('current')
cadUpChannelMinUGSLastFiveMins = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 3, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadUpChannelMinUGSLastFiveMins.setStatus('current')
cadUpChannelNormalUGSDeniedLastOneHour = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 3, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadUpChannelNormalUGSDeniedLastOneHour.setStatus('current')
cadUpChannelNormalUGSDeniedLastFiveMins = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 3, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadUpChannelNormalUGSDeniedLastFiveMins.setStatus('current')
cadUpChannelEmergencyUGSDeniedLastOneHour = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 3, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadUpChannelEmergencyUGSDeniedLastOneHour.setStatus('current')
cadUpChannelEmergencyUGSDeniedLastFiveMins = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 3, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadUpChannelEmergencyUGSDeniedLastFiveMins.setStatus('current')
cadUpChannelTotalNormalUGSLastOneHour = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 3, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadUpChannelTotalNormalUGSLastOneHour.setStatus('current')
cadUpChannelTotalNormalUGSLastFiveMins = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 3, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadUpChannelTotalNormalUGSLastFiveMins.setStatus('current')
cadUpChannelTotalEmergencyUGSLastOneHour = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 3, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadUpChannelTotalEmergencyUGSLastOneHour.setStatus('current')
cadUpChannelTotalEmergencyUGSLastFiveMins = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 3, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadUpChannelTotalEmergencyUGSLastFiveMins.setStatus('current')
cadCamScaleTable = MibTable((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 4), )
if mibBuilder.loadTexts: cadCamScaleTable.setStatus('current')
cadCamScaleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 4, 1), ).setIndexNames((0, "CADANT-SW-MEAS-MIB", "cadCamScaleCardId"))
if mibBuilder.loadTexts: cadCamScaleEntry.setStatus('current')
cadCamScaleCardId = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 4, 1, 1), CardId().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 6), ValueRangeConstraint(9, 14), )))
if mibBuilder.loadTexts: cadCamScaleCardId.setStatus('current')
cadCamScaleDevices = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 4, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadCamScaleDevices.setStatus('current')
cadCamScaleBondedDevices = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 4, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadCamScaleBondedDevices.setStatus('current')
cadCamScaleServiceFlows = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 4, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadCamScaleServiceFlows.setStatus('current')
cadCamScaleClassifiers = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 4, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadCamScaleClassifiers.setStatus('current')
cadCamScaleIpv4Addresses = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 4, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadCamScaleIpv4Addresses.setStatus('current')
cadCamScaleIpv6Addresses = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 4, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadCamScaleIpv6Addresses.setStatus('current')
cadCamScaleUsRangeCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 4, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadCamScaleUsRangeCount.setStatus('current')
cadCamScaleTotalCpe = MibTableColumn((1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 9, 4, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cadCamScaleTotalCpe.setStatus('current')
mibBuilder.exportSymbols("CADANT-SW-MEAS-MIB", cadCamScaleServiceFlows=cadCamScaleServiceFlows, cadantTotalDevices=cadantTotalDevices, cadantUsBondedDevices=cadantUsBondedDevices, cadantDsBondedDevices=cadantDsBondedDevices, cadantTotalArpEntries=cadantTotalArpEntries, cadUpChannelInitialMaintSizeMslots=cadUpChannelInitialMaintSizeMslots, cadUpChannelNormalUGSDeniedLastOneHour=cadUpChannelNormalUGSDeniedLastOneHour, cadSWUChannelMeasTable=cadSWUChannelMeasTable, cadCamScaleIpv4Addresses=cadCamScaleIpv4Addresses, cadCamScaleUsRangeCount=cadCamScaleUsRangeCount, cadantTotalCpe=cadantTotalCpe, cadUpChannelTotalEmergencyUGSLastOneHour=cadUpChannelTotalEmergencyUGSLastOneHour, cadChassisScaleGroup=cadChassisScaleGroup, cadSWUChannelMeasEntry=cadSWUChannelMeasEntry, cadUpChannelMaxUGSLastFiveMins=cadUpChannelMaxUGSLastFiveMins, cadUpChannelSScale=cadUpChannelSScale, cadUpChannelRequestSizeMslots=cadUpChannelRequestSizeMslots, cadUpChannelAvgUGSLastOneHour=cadUpChannelAvgUGSLastOneHour, cadUpChannelMaxUGSLastOneHour=cadUpChannelMaxUGSLastOneHour, cadUpChannelNormalUGSDeniedLastFiveMins=cadUpChannelNormalUGSDeniedLastFiveMins, cadantTotalNdEntries=cadantTotalNdEntries, cadantVideoMulticastStreams=cadantVideoMulticastStreams, cadCamScaleClassifiers=cadCamScaleClassifiers, cadUpChannelTotalNormalUGSLastFiveMins=cadUpChannelTotalNormalUGSLastFiveMins, cadUpChannelTotalNormalUGSLastOneHour=cadUpChannelTotalNormalUGSLastOneHour, cadUpChannelStatsEntry=cadUpChannelStatsEntry, cadantTotalIpv6Routes=cadantTotalIpv6Routes, cadantDocsisMulticastStreams=cadantDocsisMulticastStreams, cadCamScaleIpv6Addresses=cadCamScaleIpv6Addresses, cadUpChannelTotalEmergencyUGSLastFiveMins=cadUpChannelTotalEmergencyUGSLastFiveMins, cadUpChannelEmergencyUGSDeniedLastOneHour=cadUpChannelEmergencyUGSDeniedLastOneHour, cadUpChannelMinUGSLastOneHour=cadUpChannelMinUGSLastOneHour, cadUpChannelIngressCancellationBandwidth=cadUpChannelIngressCancellationBandwidth, cadantTotalClassifiers=cadantTotalClassifiers, cadUpChannelStatsTable=cadUpChannelStatsTable, cadUpChannelAttenuation=cadUpChannelAttenuation, cadUpChannelRFCalibration=cadUpChannelRFCalibration, cadCamScaleCardId=cadCamScaleCardId, cadCamScaleBondedDevices=cadCamScaleBondedDevices, cadCamScaleTotalCpe=cadCamScaleTotalCpe, cadantTotalIpv4Routes=cadantTotalIpv4Routes, cadUpChannelTScale=cadUpChannelTScale, cadCamScaleTable=cadCamScaleTable, PYSNMP_MODULE_ID=cadSoftwareMeasMib, cadCamScaleEntry=cadCamScaleEntry, cadantTotalServiceFlows=cadantTotalServiceFlows, cadCamScaleDevices=cadCamScaleDevices, cadSoftwareMeasMib=cadSoftwareMeasMib, cadUpChannelMinUGSLastFiveMins=cadUpChannelMinUGSLastFiveMins, cadUpChannelAvgUGSLastFiveMins=cadUpChannelAvgUGSLastFiveMins, cadUpChannelEmergencyUGSDeniedLastFiveMins=cadUpChannelEmergencyUGSDeniedLastFiveMins)
