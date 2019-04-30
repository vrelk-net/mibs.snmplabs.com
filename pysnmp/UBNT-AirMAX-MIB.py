#
# PySNMP MIB module UBNT-AirMAX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/UBNT-AirMAX-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:21:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ObjectIdentity, TimeTicks, iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, Counter64, Bits, MibIdentifier, Integer32, ModuleIdentity, IpAddress, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "TimeTicks", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "Counter64", "Bits", "MibIdentifier", "Integer32", "ModuleIdentity", "IpAddress", "Counter32")
DisplayString, TruthValue, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "MacAddress", "TextualConvention")
ubntAirosGroups, ubntMIB = mibBuilder.importSymbols("UBNT-MIB", "ubntAirosGroups", "ubntMIB")
ubntAirMAX = ModuleIdentity((1, 3, 6, 1, 4, 1, 41112, 1, 4))
ubntAirMAX.setRevisions(('2015-09-17 00:00',))
if mibBuilder.loadTexts: ubntAirMAX.setLastUpdated('201509170000Z')
if mibBuilder.loadTexts: ubntAirMAX.setOrganization('Ubiquiti Networks, Inc.')
ubntRadioTable = MibTable((1, 3, 6, 1, 4, 1, 41112, 1, 4, 1), )
if mibBuilder.loadTexts: ubntRadioTable.setStatus('current')
ubntRadioEntry = MibTableRow((1, 3, 6, 1, 4, 1, 41112, 1, 4, 1, 1), ).setIndexNames((0, "UBNT-AirMAX-MIB", "ubntRadioIndex"))
if mibBuilder.loadTexts: ubntRadioEntry.setStatus('current')
ubntRadioIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: ubntRadioIndex.setStatus('current')
ubntRadioMode = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("sta", 1), ("ap", 2), ("aprepeater", 3), ("apwds", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntRadioMode.setStatus('current')
ubntRadioCCode = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntRadioCCode.setStatus('current')
ubntRadioFreq = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntRadioFreq.setStatus('current')
ubntRadioDfsEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntRadioDfsEnabled.setStatus('current')
ubntRadioTxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntRadioTxPower.setStatus('current')
ubntRadioDistance = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntRadioDistance.setStatus('current')
ubntRadioChainmask = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntRadioChainmask.setStatus('current')
ubntRadioAntenna = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntRadioAntenna.setStatus('current')
ubntRadioRssiTable = MibTable((1, 3, 6, 1, 4, 1, 41112, 1, 4, 2), )
if mibBuilder.loadTexts: ubntRadioRssiTable.setStatus('current')
ubntRadioRssiEntry = MibTableRow((1, 3, 6, 1, 4, 1, 41112, 1, 4, 2, 1), ).setIndexNames((0, "UBNT-AirMAX-MIB", "ubntRadioIndex"), (0, "UBNT-AirMAX-MIB", "ubntRadioRssiIndex"))
if mibBuilder.loadTexts: ubntRadioRssiEntry.setStatus('current')
ubntRadioRssiIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: ubntRadioRssiIndex.setStatus('current')
ubntRadioRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntRadioRssi.setStatus('current')
ubntRadioRssiMgmt = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntRadioRssiMgmt.setStatus('current')
ubntRadioRssiExt = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntRadioRssiExt.setStatus('current')
ubntAirMaxTable = MibTable((1, 3, 6, 1, 4, 1, 41112, 1, 4, 6), )
if mibBuilder.loadTexts: ubntAirMaxTable.setStatus('current')
ubntAirMaxEntry = MibTableRow((1, 3, 6, 1, 4, 1, 41112, 1, 4, 6, 1), ).setIndexNames((0, "UBNT-AirMAX-MIB", "ubntAirMaxIfIndex"))
if mibBuilder.loadTexts: ubntAirMaxEntry.setStatus('current')
ubntAirMaxIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: ubntAirMaxIfIndex.setStatus('current')
ubntAirMaxEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 6, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntAirMaxEnabled.setStatus('current')
ubntAirMaxQuality = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 6, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntAirMaxQuality.setStatus('current')
ubntAirMaxCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 6, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntAirMaxCapacity.setStatus('current')
ubntAirMaxPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 6, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("high", 0), ("medium", 1), ("low", 2), ("none", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntAirMaxPriority.setStatus('current')
ubntAirMaxNoAck = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 6, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntAirMaxNoAck.setStatus('current')
ubntAirSyncTable = MibTable((1, 3, 6, 1, 4, 1, 41112, 1, 4, 3), )
if mibBuilder.loadTexts: ubntAirSyncTable.setStatus('current')
ubntAirSyncEntry = MibTableRow((1, 3, 6, 1, 4, 1, 41112, 1, 4, 3, 1), ).setIndexNames((0, "UBNT-AirMAX-MIB", "ubntAirSyncIfIndex"))
if mibBuilder.loadTexts: ubntAirSyncEntry.setStatus('current')
ubntAirSyncIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: ubntAirSyncIfIndex.setStatus('current')
ubntAirSyncMode = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("disabled", 0), ("master", 1), ("slave", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntAirSyncMode.setStatus('current')
ubntAirSyncCount = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntAirSyncCount.setStatus('current')
ubntAirSyncDownUtil = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntAirSyncDownUtil.setStatus('current')
ubntAirSyncUpUtil = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntAirSyncUpUtil.setStatus('current')
ubntAirSelTable = MibTable((1, 3, 6, 1, 4, 1, 41112, 1, 4, 4), )
if mibBuilder.loadTexts: ubntAirSelTable.setStatus('current')
ubntAirSelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 41112, 1, 4, 4, 1), ).setIndexNames((0, "UBNT-AirMAX-MIB", "ubntAirSelIfIndex"))
if mibBuilder.loadTexts: ubntAirSelEntry.setStatus('current')
ubntAirSelIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: ubntAirSelIfIndex.setStatus('current')
ubntAirSelEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 4, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntAirSelEnabled.setStatus('current')
ubntAirSelInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntAirSelInterval.setStatus('current')
ubntWlStatTable = MibTable((1, 3, 6, 1, 4, 1, 41112, 1, 4, 5), )
if mibBuilder.loadTexts: ubntWlStatTable.setStatus('current')
ubntWlStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1), ).setIndexNames((0, "UBNT-AirMAX-MIB", "ubntWlStatIndex"))
if mibBuilder.loadTexts: ubntWlStatEntry.setStatus('current')
ubntWlStatIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: ubntWlStatIndex.setStatus('current')
ubntWlStatSsid = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntWlStatSsid.setStatus('current')
ubntWlStatHideSsid = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntWlStatHideSsid.setStatus('current')
ubntWlStatApMac = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntWlStatApMac.setStatus('current')
ubntWlStatSignal = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntWlStatSignal.setStatus('current')
ubntWlStatRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntWlStatRssi.setStatus('current')
ubntWlStatCcq = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntWlStatCcq.setStatus('current')
ubntWlStatNoiseFloor = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntWlStatNoiseFloor.setStatus('current')
ubntWlStatTxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntWlStatTxRate.setStatus('current')
ubntWlStatRxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntWlStatRxRate.setStatus('current')
ubntWlStatSecurity = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntWlStatSecurity.setStatus('current')
ubntWlStatWdsEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 12), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntWlStatWdsEnabled.setStatus('current')
ubntWlStatApRepeater = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 13), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntWlStatApRepeater.setStatus('current')
ubntWlStatChanWidth = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntWlStatChanWidth.setStatus('current')
ubntWlStatStaCount = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 15), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntWlStatStaCount.setStatus('current')
ubntStaTable = MibTable((1, 3, 6, 1, 4, 1, 41112, 1, 4, 7), )
if mibBuilder.loadTexts: ubntStaTable.setStatus('current')
ubntStaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1), ).setIndexNames((0, "UBNT-AirMAX-MIB", "ubntWlStatIndex"), (0, "UBNT-AirMAX-MIB", "ubntStaMac"))
if mibBuilder.loadTexts: ubntStaEntry.setStatus('current')
ubntStaMac = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 1), MacAddress())
if mibBuilder.loadTexts: ubntStaMac.setStatus('current')
ubntStaName = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntStaName.setStatus('current')
ubntStaSignal = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntStaSignal.setStatus('current')
ubntStaNoiseFloor = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntStaNoiseFloor.setStatus('current')
ubntStaDistance = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntStaDistance.setStatus('current')
ubntStaCcq = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntStaCcq.setStatus('current')
ubntStaAmp = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntStaAmp.setStatus('current')
ubntStaAmq = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntStaAmq.setStatus('current')
ubntStaAmc = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntStaAmc.setStatus('current')
ubntStaLastIp = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 10), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntStaLastIp.setStatus('current')
ubntStaTxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntStaTxRate.setStatus('current')
ubntStaRxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntStaRxRate.setStatus('current')
ubntStaTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntStaTxBytes.setStatus('current')
ubntStaRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntStaRxBytes.setStatus('current')
ubntStaConnTime = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 15), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntStaConnTime.setStatus('current')
ubntStaLocalCINR = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntStaLocalCINR.setStatus('current')
ubntStaTxCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntStaTxCapacity.setStatus('current')
ubntStaRxCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntStaRxCapacity.setStatus('current')
ubntStaTxAirtime = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntStaTxAirtime.setStatus('current')
ubntStaRxAirtime = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntStaRxAirtime.setStatus('current')
ubntStaTxLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ubntStaTxLatency.setStatus('current')
ubntAirMAXStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 41112, 1, 2, 2, 1)).setObjects(("UBNT-AirMAX-MIB", "ubntStaName"), ("UBNT-AirMAX-MIB", "ubntStaSignal"), ("UBNT-AirMAX-MIB", "ubntStaNoiseFloor"), ("UBNT-AirMAX-MIB", "ubntStaDistance"), ("UBNT-AirMAX-MIB", "ubntStaCcq"), ("UBNT-AirMAX-MIB", "ubntStaAmp"), ("UBNT-AirMAX-MIB", "ubntStaAmq"), ("UBNT-AirMAX-MIB", "ubntStaAmc"), ("UBNT-AirMAX-MIB", "ubntStaLastIp"), ("UBNT-AirMAX-MIB", "ubntStaTxRate"), ("UBNT-AirMAX-MIB", "ubntStaRxRate"), ("UBNT-AirMAX-MIB", "ubntStaTxBytes"), ("UBNT-AirMAX-MIB", "ubntStaRxBytes"), ("UBNT-AirMAX-MIB", "ubntStaConnTime"), ("UBNT-AirMAX-MIB", "ubntStaLocalCINR"), ("UBNT-AirMAX-MIB", "ubntStaTxCapacity"), ("UBNT-AirMAX-MIB", "ubntStaRxCapacity"), ("UBNT-AirMAX-MIB", "ubntStaTxAirtime"), ("UBNT-AirMAX-MIB", "ubntStaRxAirtime"), ("UBNT-AirMAX-MIB", "ubntStaTxLatency"), ("UBNT-AirMAX-MIB", "ubntRadioMode"), ("UBNT-AirMAX-MIB", "ubntRadioCCode"), ("UBNT-AirMAX-MIB", "ubntRadioFreq"), ("UBNT-AirMAX-MIB", "ubntRadioDfsEnabled"), ("UBNT-AirMAX-MIB", "ubntRadioTxPower"), ("UBNT-AirMAX-MIB", "ubntRadioDistance"), ("UBNT-AirMAX-MIB", "ubntRadioChainmask"), ("UBNT-AirMAX-MIB", "ubntRadioAntenna"), ("UBNT-AirMAX-MIB", "ubntRadioRssi"), ("UBNT-AirMAX-MIB", "ubntRadioRssiMgmt"), ("UBNT-AirMAX-MIB", "ubntRadioRssiExt"), ("UBNT-AirMAX-MIB", "ubntAirMaxEnabled"), ("UBNT-AirMAX-MIB", "ubntAirMaxQuality"), ("UBNT-AirMAX-MIB", "ubntAirMaxCapacity"), ("UBNT-AirMAX-MIB", "ubntAirMaxPriority"), ("UBNT-AirMAX-MIB", "ubntAirMaxNoAck"), ("UBNT-AirMAX-MIB", "ubntAirSyncMode"), ("UBNT-AirMAX-MIB", "ubntAirSyncCount"), ("UBNT-AirMAX-MIB", "ubntAirSyncDownUtil"), ("UBNT-AirMAX-MIB", "ubntAirSyncUpUtil"), ("UBNT-AirMAX-MIB", "ubntAirSelEnabled"), ("UBNT-AirMAX-MIB", "ubntAirSelInterval"), ("UBNT-AirMAX-MIB", "ubntWlStatSsid"), ("UBNT-AirMAX-MIB", "ubntWlStatHideSsid"), ("UBNT-AirMAX-MIB", "ubntWlStatApMac"), ("UBNT-AirMAX-MIB", "ubntWlStatSignal"), ("UBNT-AirMAX-MIB", "ubntWlStatRssi"), ("UBNT-AirMAX-MIB", "ubntWlStatCcq"), ("UBNT-AirMAX-MIB", "ubntWlStatNoiseFloor"), ("UBNT-AirMAX-MIB", "ubntWlStatTxRate"), ("UBNT-AirMAX-MIB", "ubntWlStatRxRate"), ("UBNT-AirMAX-MIB", "ubntWlStatSecurity"), ("UBNT-AirMAX-MIB", "ubntWlStatWdsEnabled"), ("UBNT-AirMAX-MIB", "ubntWlStatApRepeater"), ("UBNT-AirMAX-MIB", "ubntWlStatChanWidth"), ("UBNT-AirMAX-MIB", "ubntWlStatStaCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ubntAirMAXStatusGroup = ubntAirMAXStatusGroup.setStatus('current')
ubntAirMAXStatusCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 41112, 1, 2, 2, 2)).setObjects(("UBNT-AirMAX-MIB", "ubntAirMAXStatusGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ubntAirMAXStatusCompliance = ubntAirMAXStatusCompliance.setStatus('current')
mibBuilder.exportSymbols("UBNT-AirMAX-MIB", ubntStaEntry=ubntStaEntry, ubntStaAmp=ubntStaAmp, ubntRadioDfsEnabled=ubntRadioDfsEnabled, ubntWlStatTxRate=ubntWlStatTxRate, ubntStaCcq=ubntStaCcq, ubntStaAmq=ubntStaAmq, ubntRadioRssiIndex=ubntRadioRssiIndex, ubntStaTxAirtime=ubntStaTxAirtime, ubntWlStatNoiseFloor=ubntWlStatNoiseFloor, ubntRadioFreq=ubntRadioFreq, ubntWlStatEntry=ubntWlStatEntry, ubntStaTxBytes=ubntStaTxBytes, ubntWlStatRxRate=ubntWlStatRxRate, ubntRadioRssiExt=ubntRadioRssiExt, ubntRadioRssiTable=ubntRadioRssiTable, ubntAirMAXStatusGroup=ubntAirMAXStatusGroup, ubntWlStatStaCount=ubntWlStatStaCount, ubntRadioChainmask=ubntRadioChainmask, ubntRadioTxPower=ubntRadioTxPower, ubntRadioDistance=ubntRadioDistance, ubntRadioIndex=ubntRadioIndex, ubntAirSelEntry=ubntAirSelEntry, ubntWlStatSignal=ubntWlStatSignal, ubntAirSyncEntry=ubntAirSyncEntry, ubntAirMaxEntry=ubntAirMaxEntry, ubntWlStatWdsEnabled=ubntWlStatWdsEnabled, ubntAirMaxTable=ubntAirMaxTable, ubntRadioTable=ubntRadioTable, ubntAirSyncTable=ubntAirSyncTable, ubntAirSyncMode=ubntAirSyncMode, ubntStaConnTime=ubntStaConnTime, ubntRadioCCode=ubntRadioCCode, ubntWlStatIndex=ubntWlStatIndex, ubntAirMaxEnabled=ubntAirMaxEnabled, ubntStaMac=ubntStaMac, ubntAirSyncIfIndex=ubntAirSyncIfIndex, ubntAirMaxNoAck=ubntAirMaxNoAck, ubntAirSyncUpUtil=ubntAirSyncUpUtil, PYSNMP_MODULE_ID=ubntAirMAX, ubntWlStatSsid=ubntWlStatSsid, ubntStaDistance=ubntStaDistance, ubntStaSignal=ubntStaSignal, ubntWlStatSecurity=ubntWlStatSecurity, ubntWlStatChanWidth=ubntWlStatChanWidth, ubntStaAmc=ubntStaAmc, ubntAirSyncCount=ubntAirSyncCount, ubntStaLocalCINR=ubntStaLocalCINR, ubntStaTxCapacity=ubntStaTxCapacity, ubntAirMaxQuality=ubntAirMaxQuality, ubntAirMAX=ubntAirMAX, ubntWlStatCcq=ubntWlStatCcq, ubntStaNoiseFloor=ubntStaNoiseFloor, ubntRadioRssiMgmt=ubntRadioRssiMgmt, ubntRadioAntenna=ubntRadioAntenna, ubntWlStatRssi=ubntWlStatRssi, ubntStaRxCapacity=ubntStaRxCapacity, ubntAirMAXStatusCompliance=ubntAirMAXStatusCompliance, ubntAirSelTable=ubntAirSelTable, ubntAirSelEnabled=ubntAirSelEnabled, ubntStaTable=ubntStaTable, ubntAirSelInterval=ubntAirSelInterval, ubntStaTxRate=ubntStaTxRate, ubntStaRxBytes=ubntStaRxBytes, ubntRadioMode=ubntRadioMode, ubntRadioRssiEntry=ubntRadioRssiEntry, ubntWlStatApMac=ubntWlStatApMac, ubntWlStatApRepeater=ubntWlStatApRepeater, ubntWlStatTable=ubntWlStatTable, ubntAirSelIfIndex=ubntAirSelIfIndex, ubntStaRxAirtime=ubntStaRxAirtime, ubntWlStatHideSsid=ubntWlStatHideSsid, ubntStaLastIp=ubntStaLastIp, ubntStaTxLatency=ubntStaTxLatency, ubntAirSyncDownUtil=ubntAirSyncDownUtil, ubntRadioEntry=ubntRadioEntry, ubntAirMaxPriority=ubntAirMaxPriority, ubntAirMaxCapacity=ubntAirMaxCapacity, ubntAirMaxIfIndex=ubntAirMaxIfIndex, ubntRadioRssi=ubntRadioRssi, ubntStaName=ubntStaName, ubntStaRxRate=ubntStaRxRate)
