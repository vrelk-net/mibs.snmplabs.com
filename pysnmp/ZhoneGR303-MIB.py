#
# PySNMP MIB module ZhoneGR303-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZhoneGR303-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:46:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
PerfCurrentCount, = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfCurrentCount")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, MibIdentifier, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, Counter64, Unsigned32, NotificationType, IpAddress, Gauge32, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "Counter64", "Unsigned32", "NotificationType", "IpAddress", "Gauge32", "ObjectIdentity", "iso")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
zhoneSystemConfigurationDateAndTime, = mibBuilder.importSymbols("ZHONE-SYSTEM-MIB", "zhoneSystemConfigurationDateAndTime")
zhoneVoice, = mibBuilder.importSymbols("Zhone", "zhoneVoice")
ZhoneAdminString, ZhoneSlotValueOrZero, ZhoneRowStatus, ZhoneShelfValueOrZero = mibBuilder.importSymbols("Zhone-TC", "ZhoneAdminString", "ZhoneSlotValueOrZero", "ZhoneRowStatus", "ZhoneShelfValueOrZero")
zhoneGR303 = ModuleIdentity((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1))
zhoneGR303.setRevisions(('2003-12-23 11:09', '2003-11-14 13:10', '2001-11-15 10:45', '2001-08-31 12:30', '2001-08-14 14:47', '2001-06-26 15:00', '2001-03-28 10:55', '2001-02-15 18:47', '2001-02-01 13:01', '2001-01-26 11:48', '2000-12-12 11:57', '2000-09-12 12:12',))
if mibBuilder.loadTexts: zhoneGR303.setLastUpdated('200312231109Z')
if mibBuilder.loadTexts: zhoneGR303.setOrganization('Zhone Technologies, Inc.')
interfaceGroupTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 1), )
if mibBuilder.loadTexts: interfaceGroupTable.setStatus('current')
interfaceGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 1, 1), ).setIndexNames((0, "ZhoneGR303-MIB", "igNameId"))
if mibBuilder.loadTexts: interfaceGroupEntry.setStatus('current')
igNameId = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 1, 1, 1), ZhoneAdminString())
if mibBuilder.loadTexts: igNameId.setStatus('current')
igShelf = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 1, 1, 2), ZhoneShelfValueOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igShelf.setStatus('current')
igSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 1, 1, 3), ZhoneSlotValueOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igSlot.setStatus('current')
igPeerShelf = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 1, 1, 4), ZhoneShelfValueOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igPeerShelf.setStatus('current')
igPeerSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 1, 1, 5), ZhoneSlotValueOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igPeerSlot.setStatus('current')
igSwitchType = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("lucent5Ess", 2), ("nortelDms100", 3), ("lucentGtd5", 4), ("santeraSanteraOne", 5), ("telicaPlexus9000", 6), ("taquaIx7000", 7)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: igSwitchType.setStatus('current')
igPrimaryEocTmcDs1IfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 1, 1, 7), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igPrimaryEocTmcDs1IfIndex.setStatus('current')
igSecondaryEocTmcDs1IfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 1, 1, 8), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: igSecondaryEocTmcDs1IfIndex.setStatus('current')
igAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inService", 1), ("outOfService", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: igAdminStatus.setStatus('current')
igOperationalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("operable", 1), ("inoperable", 2), ("standby", 3), ("inoperableIsInProgress", 4), ("inoperableOosInProgress", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: igOperationalStatus.setStatus('current')
igPeerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noStandbyConfigured", 1), ("configuredAndAvailable", 2), ("configuredAndUnavailable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: igPeerStatus.setStatus('current')
igMaxConfigCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 1, 1, 12), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(22, 670))).setUnits('calls').setMaxAccess("readonly")
if mibBuilder.loadTexts: igMaxConfigCalls.setStatus('current')
igCurrActiveCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 1, 1, 13), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 670))).setUnits('calls').setMaxAccess("readonly")
if mibBuilder.loadTexts: igCurrActiveCalls.setStatus('current')
igStatsTimeElapsed = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 899))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: igStatsTimeElapsed.setStatus('current')
igStatsValidIntervals = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 96))).setUnits('intervals').setMaxAccess("readonly")
if mibBuilder.loadTexts: igStatsValidIntervals.setStatus('current')
igStatsInvalidIntervals = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 96))).setUnits('intervals').setMaxAccess("readonly")
if mibBuilder.loadTexts: igStatsInvalidIntervals.setStatus('current')
igRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 1, 1, 17), ZhoneRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: igRowStatus.setStatus('current')
igWorkingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("passive", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: igWorkingMode.setStatus('current')
igControlChannelTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 2), )
if mibBuilder.loadTexts: igControlChannelTable.setStatus('current')
igControlChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 2, 1), )
interfaceGroupEntry.registerAugmentions(("ZhoneGR303-MIB", "igControlChannelEntry"))
igControlChannelEntry.setIndexNames(*interfaceGroupEntry.getIndexNames())
if mibBuilder.loadTexts: igControlChannelEntry.setStatus('current')
igControlChannelTmcPrimarySvcState = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("active", 1), ("standby", 2), ("outOfService", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: igControlChannelTmcPrimarySvcState.setStatus('current')
igControlChannelTmcSecondarySvcState = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("active", 1), ("standby", 2), ("outOfService", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: igControlChannelTmcSecondarySvcState.setStatus('current')
igControlChannelT303 = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(700, 700), ValueRangeConstraint(1200, 1200), ValueRangeConstraint(1700, 1700), ValueRangeConstraint(2200, 2200), ValueRangeConstraint(2700, 2700), ValueRangeConstraint(3200, 3200), ValueRangeConstraint(3700, 3700), ValueRangeConstraint(4200, 4200), ValueRangeConstraint(4700, 4700), )).clone(700)).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: igControlChannelT303.setStatus('current')
igControlChannelT396 = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(700, 700), ValueRangeConstraint(1700, 1700), ValueRangeConstraint(2700, 2700), ValueRangeConstraint(3700, 3700), ValueRangeConstraint(4700, 4700), ValueRangeConstraint(5700, 5700), ValueRangeConstraint(6700, 6700), ValueRangeConstraint(7700, 7700), ValueRangeConstraint(8700, 8700), ValueRangeConstraint(9700, 9700), ValueRangeConstraint(10700, 10700), ValueRangeConstraint(11700, 11700), ValueRangeConstraint(12700, 12700), ValueRangeConstraint(13700, 13700), ValueRangeConstraint(14700, 14700), )).clone(14700)).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: igControlChannelT396.setStatus('current')
igSapi0MaxOutstandingFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 7)).clone(7)).setUnits('frames').setMaxAccess("readcreate")
if mibBuilder.loadTexts: igSapi0MaxOutstandingFrames.setStatus('current')
igSapi0N200 = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: igSapi0N200.setStatus('current')
igSapi0T200 = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(100, 100), ValueRangeConstraint(150, 150), ValueRangeConstraint(200, 200), ValueRangeConstraint(250, 250), ValueRangeConstraint(300, 300), ValueRangeConstraint(350, 350), )).clone(150)).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: igSapi0T200.setStatus('current')
igSapi0T203 = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(10, 10), ValueRangeConstraint(20, 20), ValueRangeConstraint(30, 30), ValueRangeConstraint(40, 40), ValueRangeConstraint(50, 50), ValueRangeConstraint(60, 60), ValueRangeConstraint(70, 70), ValueRangeConstraint(80, 80), ValueRangeConstraint(90, 90), ValueRangeConstraint(100, 100), ValueRangeConstraint(110, 110), ValueRangeConstraint(120, 120), ValueRangeConstraint(130, 130), ValueRangeConstraint(140, 140), ValueRangeConstraint(150, 150), ValueRangeConstraint(160, 160), ValueRangeConstraint(170, 170), ValueRangeConstraint(180, 180), ValueRangeConstraint(190, 190), ValueRangeConstraint(200, 200), ValueRangeConstraint(210, 210), ValueRangeConstraint(220, 220), ValueRangeConstraint(230, 230), ValueRangeConstraint(240, 240), ValueRangeConstraint(250, 250), ValueRangeConstraint(260, 260), ValueRangeConstraint(270, 270), ValueRangeConstraint(280, 280), ValueRangeConstraint(290, 290), ValueRangeConstraint(300, 300), )).clone(30)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: igSapi0T203.setStatus('current')
igSapi0PpsMode = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("inhibit", 1), ("notInhibited", 2), ("notApplicable", 3))).clone('notInhibited')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: igSapi0PpsMode.setStatus('current')
igSapi1MaxOutstandingFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 7)).clone(7)).setUnits('frames').setMaxAccess("readcreate")
if mibBuilder.loadTexts: igSapi1MaxOutstandingFrames.setStatus('current')
igSapi1N200 = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: igSapi1N200.setStatus('current')
igSapi1T200 = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(100, 100), ValueRangeConstraint(150, 150), ValueRangeConstraint(200, 200), ValueRangeConstraint(250, 250), ValueRangeConstraint(300, 300), ValueRangeConstraint(350, 350), )).clone(150)).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: igSapi1T200.setStatus('current')
igSapi1T203 = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(10, 10), ValueRangeConstraint(20, 20), ValueRangeConstraint(30, 30), ValueRangeConstraint(40, 40), ValueRangeConstraint(50, 50), ValueRangeConstraint(60, 60), ValueRangeConstraint(70, 70), ValueRangeConstraint(80, 80), ValueRangeConstraint(90, 90), ValueRangeConstraint(100, 100), ValueRangeConstraint(110, 110), ValueRangeConstraint(120, 120), ValueRangeConstraint(130, 130), ValueRangeConstraint(140, 140), ValueRangeConstraint(150, 150), ValueRangeConstraint(160, 160), ValueRangeConstraint(170, 170), ValueRangeConstraint(180, 180), ValueRangeConstraint(190, 190), ValueRangeConstraint(200, 200), ValueRangeConstraint(210, 210), ValueRangeConstraint(220, 220), ValueRangeConstraint(230, 230), ValueRangeConstraint(240, 240), ValueRangeConstraint(250, 250), ValueRangeConstraint(260, 260), ValueRangeConstraint(270, 270), ValueRangeConstraint(280, 280), ValueRangeConstraint(290, 290), ValueRangeConstraint(300, 300), )).clone(30)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: igSapi1T203.setStatus('current')
igSapi1PpsMode = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("inhibit", 1), ("notInhibited", 2), ("notApplicable", 3))).clone('notInhibited')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: igSapi1PpsMode.setStatus('current')
igControlChannelEocPrimarySvcState = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("active", 1), ("standby", 2), ("outOfService", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: igControlChannelEocPrimarySvcState.setStatus('current')
igControlChannelEocSecondarySvcState = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 2, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("active", 1), ("standby", 2), ("outOfService", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: igControlChannelEocSecondarySvcState.setStatus('current')
igStatsCurrentTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 3), )
if mibBuilder.loadTexts: igStatsCurrentTable.setStatus('current')
igStatsCurrentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 3, 1), )
interfaceGroupEntry.registerAugmentions(("ZhoneGR303-MIB", "igStatsCurrentEntry"))
igStatsCurrentEntry.setIndexNames(*interfaceGroupEntry.getIndexNames())
if mibBuilder.loadTexts: igStatsCurrentEntry.setStatus('current')
igCurrentOutboundCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 3, 1, 1), PerfCurrentCount()).setUnits('calls').setMaxAccess("readonly")
if mibBuilder.loadTexts: igCurrentOutboundCalls.setStatus('current')
igCurrentInboundCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 3, 1, 2), PerfCurrentCount()).setUnits('calls').setMaxAccess("readonly")
if mibBuilder.loadTexts: igCurrentInboundCalls.setStatus('current')
igCurrentOutboundCallsBlocked = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 3, 1, 3), PerfCurrentCount()).setUnits('calls').setMaxAccess("readonly")
if mibBuilder.loadTexts: igCurrentOutboundCallsBlocked.setStatus('current')
igCurrentGR303ProtocolErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 3, 1, 4), PerfCurrentCount()).setUnits('errors').setMaxAccess("readonly")
if mibBuilder.loadTexts: igCurrentGR303ProtocolErrors.setStatus('current')
igCurrentTMCLapdSent = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 3, 1, 5), PerfCurrentCount()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: igCurrentTMCLapdSent.setStatus('current')
igCurrentTMCLapdRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 3, 1, 6), PerfCurrentCount()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: igCurrentTMCLapdRcvd.setStatus('current')
igCurrentTMCLapdRcvdErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 3, 1, 7), PerfCurrentCount()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: igCurrentTMCLapdRcvdErrs.setStatus('current')
igCurrentEOCLapdSent = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 3, 1, 8), PerfCurrentCount()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: igCurrentEOCLapdSent.setStatus('current')
igCurrentEOCLapdRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 3, 1, 9), PerfCurrentCount()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: igCurrentEOCLapdRcvd.setStatus('current')
igCurrentEOCLapdRcvdErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 3, 1, 10), PerfCurrentCount()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: igCurrentEOCLapdRcvdErrs.setStatus('current')
igStatsIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 4), )
if mibBuilder.loadTexts: igStatsIntervalTable.setStatus('current')
igStatsIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 4, 1), ).setIndexNames((0, "ZhoneGR303-MIB", "igNameId"), (0, "ZhoneGR303-MIB", "igIntervalNumber"))
if mibBuilder.loadTexts: igStatsIntervalEntry.setStatus('current')
igIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 96)))
if mibBuilder.loadTexts: igIntervalNumber.setStatus('current')
igIntervalOutboundCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 4, 1, 2), PerfCurrentCount()).setUnits('calls').setMaxAccess("readonly")
if mibBuilder.loadTexts: igIntervalOutboundCalls.setStatus('current')
igIntervalInboundCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 4, 1, 3), PerfCurrentCount()).setUnits('calls').setMaxAccess("readonly")
if mibBuilder.loadTexts: igIntervalInboundCalls.setStatus('current')
igIntervalOutboundCallsBlocked = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 4, 1, 4), PerfCurrentCount()).setUnits('calls').setMaxAccess("readonly")
if mibBuilder.loadTexts: igIntervalOutboundCallsBlocked.setStatus('current')
igIntervalGR303ProtocolErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 4, 1, 5), PerfCurrentCount()).setUnits('errors').setMaxAccess("readonly")
if mibBuilder.loadTexts: igIntervalGR303ProtocolErrors.setStatus('current')
igIntervalTMCLapdSent = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 4, 1, 6), PerfCurrentCount()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: igIntervalTMCLapdSent.setStatus('current')
igIntervalTMCLapdRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 4, 1, 7), PerfCurrentCount()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: igIntervalTMCLapdRcvd.setStatus('current')
igintervalTMCLapdRcvdErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 4, 1, 8), PerfCurrentCount()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: igintervalTMCLapdRcvdErrs.setStatus('current')
igIntervalEOCLapdSent = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 4, 1, 9), PerfCurrentCount()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: igIntervalEOCLapdSent.setStatus('current')
igIntervalEOCLapdRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 4, 1, 10), PerfCurrentCount()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: igIntervalEOCLapdRcvd.setStatus('current')
igIntervalEOCLapdRcvdErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 4, 1, 11), PerfCurrentCount()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: igIntervalEOCLapdRcvdErrs.setStatus('current')
igIntervalValidData = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 4, 1, 12), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: igIntervalValidData.setStatus('current')
igStatsTotalTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 5), )
if mibBuilder.loadTexts: igStatsTotalTable.setStatus('current')
igStatsTotalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 5, 1), )
interfaceGroupEntry.registerAugmentions(("ZhoneGR303-MIB", "igStatsTotalEntry"))
igStatsTotalEntry.setIndexNames(*interfaceGroupEntry.getIndexNames())
if mibBuilder.loadTexts: igStatsTotalEntry.setStatus('current')
igTotalOutboundCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 5, 1, 1), PerfCurrentCount()).setUnits('calls').setMaxAccess("readonly")
if mibBuilder.loadTexts: igTotalOutboundCalls.setStatus('current')
igTotalInboundCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 5, 1, 2), PerfCurrentCount()).setUnits('calls').setMaxAccess("readonly")
if mibBuilder.loadTexts: igTotalInboundCalls.setStatus('current')
igTotalOutboundCallsBlocked = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 5, 1, 3), PerfCurrentCount()).setUnits('calls').setMaxAccess("readonly")
if mibBuilder.loadTexts: igTotalOutboundCallsBlocked.setStatus('current')
igTotalGR303ProtocolErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 5, 1, 4), PerfCurrentCount()).setUnits('errors').setMaxAccess("readonly")
if mibBuilder.loadTexts: igTotalGR303ProtocolErrors.setStatus('current')
igTotalTMCLapdSent = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 5, 1, 5), PerfCurrentCount()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: igTotalTMCLapdSent.setStatus('current')
igTotalTMCLapdRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 5, 1, 6), PerfCurrentCount()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: igTotalTMCLapdRcvd.setStatus('current')
igTotalTMCLapdRcvdErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 5, 1, 7), PerfCurrentCount()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: igTotalTMCLapdRcvdErrs.setStatus('current')
igTotalEOCLapdSent = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 5, 1, 8), PerfCurrentCount()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: igTotalEOCLapdSent.setStatus('current')
igTotalEOCLapdRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 5, 1, 9), PerfCurrentCount()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: igTotalEOCLapdRcvd.setStatus('current')
igTotalEOCLapdRcvdErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 5, 1, 10), PerfCurrentCount()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: igTotalEOCLapdRcvdErrs.setStatus('current')
ds1LineMappingTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 6), )
if mibBuilder.loadTexts: ds1LineMappingTable.setStatus('current')
ds1LineMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 6, 1), ).setIndexNames((0, "ZhoneGR303-MIB", "igNameId"), (0, "ZhoneGR303-MIB", "dsnLgId"), (0, "ZhoneGR303-MIB", "ds1ChannelNumber"))
if mibBuilder.loadTexts: ds1LineMappingEntry.setStatus('current')
dsnLgId = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: dsnLgId.setStatus('current')
ds1ChannelNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 28)))
if mibBuilder.loadTexts: ds1ChannelNumber.setStatus('current')
ds1Role = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("payload", 1), ("secondary", 2), ("primary", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ds1Role.setStatus('current')
ds1IfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 6, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ds1IfIndex.setStatus('current')
ds1LineMappingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 6, 1, 5), ZhoneRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ds1LineMappingRowStatus.setStatus('current')
ds1LogicalId = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 6, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 28))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ds1LogicalId.setStatus('current')
igCrvTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 7), )
if mibBuilder.loadTexts: igCrvTable.setStatus('current')
igCrvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 7, 1), ).setIndexNames((0, "ZhoneGR303-MIB", "igNameId"), (0, "ZhoneGR303-MIB", "igCrv"))
if mibBuilder.loadTexts: igCrvEntry.setStatus('current')
igCrv = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2048)))
if mibBuilder.loadTexts: igCrv.setStatus('current')
igCrvLocalAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inService", 1), ("outOfService", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: igCrvLocalAdminState.setStatus('current')
igCrvRemoteAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inService", 1), ("outOfService", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: igCrvRemoteAdminState.setStatus('current')
igCrvOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 7, 1, 4), Bits().clone(namedValues=NamedValues(("up", 0), ("fault", 1), ("manualOos", 2), ("removedFromServiceBySwitch", 3), ("unEquipped", 4), ("notConnected", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: igCrvOperStatus.setStatus('current')
igCrvTmcState = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 7, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inService", 1), ("permanentSignal", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: igCrvTmcState.setStatus('current')
igCrvSignalType = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 7, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5))).clone(namedValues=NamedValues(("loopstart", 2), ("groundstart", 3), ("loopreversebattery", 4), ("electronicbusinessset", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: igCrvSignalType.setStatus('current')
igCrvRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 7, 1, 7), ZhoneRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: igCrvRowStatus.setStatus('current')
gr303Traps = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 8))
if mibBuilder.loadTexts: gr303Traps.setStatus('current')
gr303TrapsPrefix = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 8, 0))
if mibBuilder.loadTexts: gr303TrapsPrefix.setStatus('current')
igOperStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 8, 0, 1)).setObjects(("ZhoneGR303-MIB", "igAdminStatus"), ("ZhoneGR303-MIB", "igOperationalStatus"))
if mibBuilder.loadTexts: igOperStatusChange.setStatus('current')
igTmcPrimaryStateChange = NotificationType((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 8, 0, 2)).setObjects(("ZhoneGR303-MIB", "igControlChannelTmcPrimarySvcState"))
if mibBuilder.loadTexts: igTmcPrimaryStateChange.setStatus('current')
igTmcSecondaryStateChange = NotificationType((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 8, 0, 3)).setObjects(("ZhoneGR303-MIB", "igControlChannelTmcSecondarySvcState"))
if mibBuilder.loadTexts: igTmcSecondaryStateChange.setStatus('current')
igEocPrimaryStateChange = NotificationType((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 8, 0, 4)).setObjects(("ZhoneGR303-MIB", "igControlChannelEocPrimarySvcState"))
if mibBuilder.loadTexts: igEocPrimaryStateChange.setStatus('current')
igEocSecondaryStateChange = NotificationType((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 8, 0, 5)).setObjects(("ZhoneGR303-MIB", "igControlChannelEocSecondarySvcState"))
if mibBuilder.loadTexts: igEocSecondaryStateChange.setStatus('current')
igCrvRemoteStateChange = NotificationType((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 8, 0, 6)).setObjects(("ZhoneGR303-MIB", "igCrvLocalAdminState"), ("ZhoneGR303-MIB", "igCrvRemoteAdminState"), ("ZhoneGR303-MIB", "igCrvOperStatus"))
if mibBuilder.loadTexts: igCrvRemoteStateChange.setStatus('current')
igCrvTmcStateChange = NotificationType((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 8, 0, 7)).setObjects(("ZhoneGR303-MIB", "igCrvTmcState"))
if mibBuilder.loadTexts: igCrvTmcStateChange.setStatus('current')
igSystemTimeChange = NotificationType((1, 3, 6, 1, 4, 1, 5504, 4, 3, 1, 8, 0, 8)).setObjects(("ZHONE-SYSTEM-MIB", "zhoneSystemConfigurationDateAndTime"), ("ZhoneGR303-MIB", "igRowStatus"))
if mibBuilder.loadTexts: igSystemTimeChange.setStatus('current')
mibBuilder.exportSymbols("ZhoneGR303-MIB", ds1LineMappingEntry=ds1LineMappingEntry, igCurrentEOCLapdSent=igCurrentEOCLapdSent, igRowStatus=igRowStatus, igStatsTotalTable=igStatsTotalTable, ds1ChannelNumber=ds1ChannelNumber, igCrvSignalType=igCrvSignalType, igSapi1N200=igSapi1N200, igControlChannelT303=igControlChannelT303, igCrvOperStatus=igCrvOperStatus, igControlChannelT396=igControlChannelT396, igTmcPrimaryStateChange=igTmcPrimaryStateChange, igStatsTimeElapsed=igStatsTimeElapsed, igIntervalTMCLapdSent=igIntervalTMCLapdSent, igTotalEOCLapdRcvd=igTotalEOCLapdRcvd, igTotalEOCLapdRcvdErrs=igTotalEOCLapdRcvdErrs, igCurrentTMCLapdSent=igCurrentTMCLapdSent, igCrv=igCrv, igCurrentTMCLapdRcvdErrs=igCurrentTMCLapdRcvdErrs, igOperationalStatus=igOperationalStatus, igStatsCurrentTable=igStatsCurrentTable, dsnLgId=dsnLgId, igCurrentOutboundCallsBlocked=igCurrentOutboundCallsBlocked, igCurrentTMCLapdRcvd=igCurrentTMCLapdRcvd, igStatsCurrentEntry=igStatsCurrentEntry, ds1LineMappingRowStatus=ds1LineMappingRowStatus, igOperStatusChange=igOperStatusChange, igSapi0N200=igSapi0N200, igCurrentEOCLapdRcvd=igCurrentEOCLapdRcvd, igControlChannelEocSecondarySvcState=igControlChannelEocSecondarySvcState, igIntervalInboundCalls=igIntervalInboundCalls, igStatsIntervalTable=igStatsIntervalTable, igIntervalNumber=igIntervalNumber, igSapi0MaxOutstandingFrames=igSapi0MaxOutstandingFrames, igCrvTmcState=igCrvTmcState, igTotalOutboundCallsBlocked=igTotalOutboundCallsBlocked, igControlChannelTmcSecondarySvcState=igControlChannelTmcSecondarySvcState, igNameId=igNameId, igCrvTable=igCrvTable, igTotalOutboundCalls=igTotalOutboundCalls, gr303TrapsPrefix=gr303TrapsPrefix, igTmcSecondaryStateChange=igTmcSecondaryStateChange, zhoneGR303=zhoneGR303, igPeerShelf=igPeerShelf, igSapi0T203=igSapi0T203, interfaceGroupTable=interfaceGroupTable, igSapi0T200=igSapi0T200, igEocPrimaryStateChange=igEocPrimaryStateChange, igCrvRemoteStateChange=igCrvRemoteStateChange, igControlChannelEocPrimarySvcState=igControlChannelEocPrimarySvcState, igPeerStatus=igPeerStatus, igIntervalValidData=igIntervalValidData, gr303Traps=gr303Traps, igStatsIntervalEntry=igStatsIntervalEntry, igIntervalEOCLapdRcvdErrs=igIntervalEOCLapdRcvdErrs, igCurrActiveCalls=igCurrActiveCalls, igSapi1T200=igSapi1T200, igIntervalTMCLapdRcvd=igIntervalTMCLapdRcvd, igCrvRowStatus=igCrvRowStatus, igTotalTMCLapdSent=igTotalTMCLapdSent, igStatsValidIntervals=igStatsValidIntervals, igControlChannelTmcPrimarySvcState=igControlChannelTmcPrimarySvcState, igMaxConfigCalls=igMaxConfigCalls, igTotalEOCLapdSent=igTotalEOCLapdSent, igSlot=igSlot, igCrvEntry=igCrvEntry, igSwitchType=igSwitchType, igEocSecondaryStateChange=igEocSecondaryStateChange, PYSNMP_MODULE_ID=zhoneGR303, igTotalTMCLapdRcvdErrs=igTotalTMCLapdRcvdErrs, igCurrentEOCLapdRcvdErrs=igCurrentEOCLapdRcvdErrs, igIntervalEOCLapdSent=igIntervalEOCLapdSent, igTotalInboundCalls=igTotalInboundCalls, igSecondaryEocTmcDs1IfIndex=igSecondaryEocTmcDs1IfIndex, igSapi1T203=igSapi1T203, igIntervalGR303ProtocolErrors=igIntervalGR303ProtocolErrors, igTotalTMCLapdRcvd=igTotalTMCLapdRcvd, ds1Role=ds1Role, igControlChannelEntry=igControlChannelEntry, igShelf=igShelf, igCrvLocalAdminState=igCrvLocalAdminState, igCrvTmcStateChange=igCrvTmcStateChange, igSapi1MaxOutstandingFrames=igSapi1MaxOutstandingFrames, igintervalTMCLapdRcvdErrs=igintervalTMCLapdRcvdErrs, ds1LogicalId=ds1LogicalId, igPrimaryEocTmcDs1IfIndex=igPrimaryEocTmcDs1IfIndex, ds1IfIndex=ds1IfIndex, igStatsTotalEntry=igStatsTotalEntry, igPeerSlot=igPeerSlot, igSapi1PpsMode=igSapi1PpsMode, igStatsInvalidIntervals=igStatsInvalidIntervals, igCurrentOutboundCalls=igCurrentOutboundCalls, igSystemTimeChange=igSystemTimeChange, igCurrentGR303ProtocolErrors=igCurrentGR303ProtocolErrors, igCurrentInboundCalls=igCurrentInboundCalls, igTotalGR303ProtocolErrors=igTotalGR303ProtocolErrors, igAdminStatus=igAdminStatus, ds1LineMappingTable=ds1LineMappingTable, igWorkingMode=igWorkingMode, interfaceGroupEntry=interfaceGroupEntry, igIntervalOutboundCalls=igIntervalOutboundCalls, igControlChannelTable=igControlChannelTable, igIntervalOutboundCallsBlocked=igIntervalOutboundCallsBlocked, igIntervalEOCLapdRcvd=igIntervalEOCLapdRcvd, igCrvRemoteAdminState=igCrvRemoteAdminState, igSapi0PpsMode=igSapi0PpsMode)