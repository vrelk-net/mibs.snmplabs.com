#
# PySNMP MIB module ZhoneAAL2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZhoneAAL2-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:46:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
atmVclVci, atmVclVpi = mibBuilder.importSymbols("ATM-MIB", "atmVclVci", "atmVclVpi")
AtmVorXOperStatus, AtmVcIdentifier, AtmVorXAdminStatus, AtmVorXLastChange, AtmVpIdentifier = mibBuilder.importSymbols("ATM-TC-MIB", "AtmVorXOperStatus", "AtmVcIdentifier", "AtmVorXAdminStatus", "AtmVorXLastChange", "AtmVpIdentifier")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso, Unsigned32, Counter32, MibIdentifier, TimeTicks, Bits, Integer32, NotificationType, ObjectIdentity, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso", "Unsigned32", "Counter32", "MibIdentifier", "TimeTicks", "Bits", "Integer32", "NotificationType", "ObjectIdentity", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
subVoiceAal2Cid, = mibBuilder.importSymbols("ZHONE-GEN-SUBSCRIBER", "subVoiceAal2Cid")
zhoneAtm, = mibBuilder.importSymbols("Zhone", "zhoneAtm")
ZhoneRowStatus, = mibBuilder.importSymbols("Zhone-TC", "ZhoneRowStatus")
zhoneAtmAAl2 = ModuleIdentity((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1))
zhoneAtmAAl2.setRevisions(('2003-11-19 18:00', '2003-11-14 14:19', '2003-10-03 11:45', '2003-09-02 11:30', '2003-01-21 16:50', '2002-10-01 10:59', '2002-05-29 14:15', '2001-12-07 17:23', '2001-11-16 10:25', '2001-10-09 10:28', '2001-07-11 13:58', '2001-04-11 09:55', '2001-01-29 17:10', '2000-12-20 11:02', '2000-11-06 18:54', '2000-10-30 11:58', '2000-09-11 14:53',))
if mibBuilder.loadTexts: zhoneAtmAAl2.setLastUpdated('200403021202Z')
if mibBuilder.loadTexts: zhoneAtmAAl2.setOrganization('Zhone Technologies, Inc.')
aal2Traps = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 0))
if mibBuilder.loadTexts: aal2Traps.setStatus('current')
aal2ExternalAIS = NotificationType((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("ZhoneAAL2-MIB", "aal2vpi"), ("ZhoneAAL2-MIB", "aal2Vci"))
if mibBuilder.loadTexts: aal2ExternalAIS.setStatus('current')
aal2ExternalRAI = NotificationType((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 0, 2)).setObjects(("IF-MIB", "ifIndex"), ("ZhoneAAL2-MIB", "aal2vpi"), ("ZhoneAAL2-MIB", "aal2Vci"))
if mibBuilder.loadTexts: aal2ExternalRAI.setStatus('current')
aal2InternalAIS = NotificationType((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 0, 3)).setObjects(("IF-MIB", "ifIndex"), ("ZhoneAAL2-MIB", "aal2vpi"), ("ZhoneAAL2-MIB", "aal2Vci"), ("ZHONE-GEN-SUBSCRIBER", "subVoiceAal2Cid"))
if mibBuilder.loadTexts: aal2InternalAIS.setStatus('current')
aal2InternalRDI = NotificationType((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 0, 4)).setObjects(("IF-MIB", "ifIndex"), ("ZhoneAAL2-MIB", "aal2vpi"), ("ZhoneAAL2-MIB", "aal2Vci"), ("ZHONE-GEN-SUBSCRIBER", "subVoiceAal2Cid"))
if mibBuilder.loadTexts: aal2InternalRDI.setStatus('current')
aal2PvcDown = NotificationType((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 0, 5)).setObjects(("IF-MIB", "ifIndex"), ("ZhoneAAL2-MIB", "aal2vpi"), ("ZhoneAAL2-MIB", "aal2Vci"))
if mibBuilder.loadTexts: aal2PvcDown.setStatus('current')
aal2PerfCellLossThreshTrap = NotificationType((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 0, 6)).setObjects(("ZhoneAAL2-MIB", "aal2CpsPerfSTFBadSeq"), ("ZhoneAAL2-MIB", "aal2AlarmConfigThreshCellLoss"))
if mibBuilder.loadTexts: aal2PerfCellLossThreshTrap.setStatus('current')
aal2PerfCongestionThreshTrap = NotificationType((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 0, 7)).setObjects(("ZhoneAAL2-MIB", "aal2CpsPerfCongestion"), ("ZhoneAAL2-MIB", "aal2AlarmConfigThreshCongestion"))
if mibBuilder.loadTexts: aal2PerfCongestionThreshTrap.setStatus('current')
aal2ElcpIgOperStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 0, 8)).setObjects(("ZhoneAAL2-MIB", "aal2ElcpIgOperStatus"))
if mibBuilder.loadTexts: aal2ElcpIgOperStatusChange.setStatus('current')
aal2VclTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 1), )
if mibBuilder.loadTexts: aal2VclTable.setStatus('current')
aal2VclEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ATM-MIB", "atmVclVpi"), (0, "ATM-MIB", "atmVclVci"))
if mibBuilder.loadTexts: aal2VclEntry.setStatus('current')
atmVccAal2AppId = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(10, 11, 12, 13, 14, 15, 16, 17, 18, 255))).clone(namedValues=NamedValues(("casPotsOnlyNoElcp", 10), ("pstnPotsOnlyNoElcp", 11), ("pstnPotsOnlyElcp", 12), ("dss1BriOnlyNoElcp", 13), ("dss1BriOnlyElcp", 14), ("casPotsDss1BriNoElcp", 15), ("pstnPotsDss1BriNoElcp", 16), ("pstnPotsDss1BriElcp", 17), ("otherCcs", 18), ("jetstream", 255)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmVccAal2AppId.setStatus('current')
atmVccAal2VccI = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmVccAal2VccI.setStatus('current')
atmVccAal2SigVccI = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmVccAal2SigVccI.setStatus('current')
aal2VclAudioProfileIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 512))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aal2VclAudioProfileIdentifier.setStatus('current')
aal2VclSscsDefaultType = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("i3661", 1), ("i3662", 2), ("jetstreamvoice", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aal2VclSscsDefaultType.setStatus('current')
aal2VclMaxCpsSduSize = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(45, 45), ValueRangeConstraint(64, 64), ))).setUnits('octets').setMaxAccess("readwrite")
if mibBuilder.loadTexts: aal2VclMaxCpsSduSize.setStatus('current')
aal2VclMaxNumberMultiplexChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setUnits('channels').setMaxAccess("readwrite")
if mibBuilder.loadTexts: aal2VclMaxNumberMultiplexChannels.setStatus('current')
aal2VclMinCidForAal2UserChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aal2VclMinCidForAal2UserChannels.setStatus('current')
aal2VclMaxCidForAal2UserChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aal2VclMaxCidForAal2UserChannels.setStatus('current')
aal2VclNextCid = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 255), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal2VclNextCid.setStatus('current')
aal2VclTimerCU = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 1, 1, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aal2VclTimerCU.setStatus('current')
aal2VclAudioService = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("enabledEchoCancelOff", 3), ("enabledDynamic", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aal2VclAudioService.setStatus('current')
aal2VclCircuitModeData = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aal2VclCircuitModeData.setStatus('current')
aal2VclFrameModeData = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aal2VclFrameModeData.setStatus('current')
aal2VclFaxDemoRemo = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aal2VclFaxDemoRemo.setStatus('current')
aal2VclCAS = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aal2VclCAS.setStatus('current')
aal2VclTrunkType = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("loopstart", 2), ("groundstart", 3), ("loopreversebattery", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aal2VclTrunkType.setStatus('current')
aal2VclDTMFDialedDigits = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aal2VclDTMFDialedDigits.setStatus('current')
aal2VclMfR1DialedDigits = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aal2VclMfR1DialedDigits.setStatus('current')
aal2VclMfR2DialedDigits = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aal2VclMfR2DialedDigits.setStatus('current')
aal2VclPCMEncoding = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 1, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("muLaw", 1), ("aLaw", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aal2VclPCMEncoding.setStatus('current')
aal2VclMaxLengthFrame = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 1, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setUnits('octets').setMaxAccess("readwrite")
if mibBuilder.loadTexts: aal2VclMaxLengthFrame.setStatus('current')
aal2VclMaxSDULength = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 1, 1, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65568))).setUnits('octets').setMaxAccess("readwrite")
if mibBuilder.loadTexts: aal2VclMaxSDULength.setStatus('current')
aal2VclRasTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 1, 1, 24), Integer32()).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: aal2VclRasTimer.setStatus('current')
aal2VclCellsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 1, 1, 25), Gauge32()).setUnits('cells').setMaxAccess("readonly")
if mibBuilder.loadTexts: aal2VclCellsReceived.setStatus('current')
aal2VclCellsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 1, 1, 26), Gauge32()).setUnits('cells').setMaxAccess("readonly")
if mibBuilder.loadTexts: aal2VclCellsSent.setStatus('current')
aal2VclStatsTimeElapsed = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 1, 1, 27), Integer32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: aal2VclStatsTimeElapsed.setStatus('current')
aal2CidTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 2), )
if mibBuilder.loadTexts: aal2CidTable.setStatus('current')
aal2CidEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ATM-MIB", "atmVclVpi"), (0, "ATM-MIB", "atmVclVci"), (0, "ZhoneAAL2-MIB", "aal2Cid"))
if mibBuilder.loadTexts: aal2CidEntry.setStatus('current')
aal2Cid = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: aal2Cid.setStatus('current')
aal2CidAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 2, 1, 2), AtmVorXAdminStatus().clone('down')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aal2CidAdminStatus.setStatus('current')
aal2CidOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 2, 1, 3), AtmVorXOperStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal2CidOperStatus.setStatus('current')
aal2CidLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 2, 1, 4), AtmVorXLastChange()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal2CidLastChange.setStatus('current')
aal2CidSscsType = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("i3661", 1), ("i3662", 2), ("jetstreamvoice", 3))).clone('i3662')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aal2CidSscsType.setStatus('current')
aal2CidAudioService = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("enabledEchoCancelOff", 3), ("enabledDynamic", 4))).clone('enabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aal2CidAudioService.setStatus('current')
aal2CidCircuitModeData = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aal2CidCircuitModeData.setStatus('current')
aal2CidFrameModeData = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aal2CidFrameModeData.setStatus('current')
aal2CidFaxDemoRemo = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aal2CidFaxDemoRemo.setStatus('current')
aal2CidCAS = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aal2CidCAS.setStatus('current')
aal2CidDTMFDialedDigits = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aal2CidDTMFDialedDigits.setStatus('current')
aal2CidMfR1DialedDigits = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aal2CidMfR1DialedDigits.setStatus('current')
aal2CidMfR2DialedDigits = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aal2CidMfR2DialedDigits.setStatus('current')
aal2CidPCMEncoding = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("muLaw", 1), ("aLaw", 2))).clone('muLaw')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aal2CidPCMEncoding.setStatus('current')
aal2CidMaxLengthFrame = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 2, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(65535)).setUnits('octets').setMaxAccess("readcreate")
if mibBuilder.loadTexts: aal2CidMaxLengthFrame.setStatus('current')
aal2CidMaxSDULength = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 2, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65568)).clone(1536)).setUnits('octets').setMaxAccess("readcreate")
if mibBuilder.loadTexts: aal2CidMaxSDULength.setStatus('current')
aal2CidRasTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 2, 1, 17), Integer32()).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: aal2CidRasTimer.setStatus('current')
aal2CidPreferredApIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 2, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 512)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aal2CidPreferredApIndex.setStatus('current')
aal2CidCellsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 2, 1, 19), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal2CidCellsReceived.setStatus('current')
aal2CidCellsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 2, 1, 20), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal2CidCellsSent.setStatus('current')
aal2CidStatsTimeElapsed = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 2, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal2CidStatsTimeElapsed.setStatus('current')
aal2CidRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 2, 1, 22), ZhoneRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aal2CidRowStatus.setStatus('current')
aal2CidCompletedCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 2, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal2CidCompletedCalls.setStatus('current')
aal2CidBlockedCallsNoBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 2, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal2CidBlockedCallsNoBandwidth.setStatus('current')
aal2UserDefinedAudioProfileNextIndexTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 3), )
if mibBuilder.loadTexts: aal2UserDefinedAudioProfileNextIndexTable.setStatus('current')
aal2UserDefinedAudioProfileNextIndexEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 3, 1), ).setIndexNames((0, "ZhoneAAL2-MIB", "aal2VclAudioProfileIdentifier"))
if mibBuilder.loadTexts: aal2UserDefinedAudioProfileNextIndexEntry.setStatus('current')
aal2UdApNextIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal2UdApNextIndex.setStatus('current')
aal2AudioProfileTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 4), )
if mibBuilder.loadTexts: aal2AudioProfileTable.setStatus('current')
aal2AudioProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 4, 1), ).setIndexNames((0, "ZhoneAAL2-MIB", "aal2VclAudioProfileIdentifier"), (0, "ZhoneAAL2-MIB", "aal2ApIndex"))
if mibBuilder.loadTexts: aal2AudioProfileEntry.setStatus('current')
aal2ApIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 512)))
if mibBuilder.loadTexts: aal2ApIndex.setStatus('current')
aal2ApMinUUI = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aal2ApMinUUI.setStatus('current')
aal2ApMaxUUI = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)).clone(15)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aal2ApMaxUUI.setStatus('current')
aal2ApSduMultiples = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aal2ApSduMultiples.setStatus('current')
aal2ApAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("g711", 1), ("g722", 2), ("g723", 3), ("g72632", 4), ("g727", 5), ("g728", 6), ("g729Edu", 7), ("g729Sid", 8), ("g72964", 9), ("g72912", 10), ("genericSid", 11))).clone('g711')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aal2ApAlgorithm.setStatus('current')
aal2ApPktTime = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 4, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(50, 110)).clone(55)).setUnits('tenths of milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: aal2ApPktTime.setStatus('current')
aal2ApSequence = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 4, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(50, 110)).clone(55)).setUnits('tenths of milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: aal2ApSequence.setStatus('current')
aal2ApRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 4, 1, 8), ZhoneRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aal2ApRowStatus.setStatus('current')
aal2ApSilenceSupression = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 4, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aal2ApSilenceSupression.setStatus('current')
aal2ApPacketLength = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 4, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64)).clone(44)).setUnits('octets').setMaxAccess("readcreate")
if mibBuilder.loadTexts: aal2ApPacketLength.setStatus('current')
aal2CpsPerformanceTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 5), )
if mibBuilder.loadTexts: aal2CpsPerformanceTable.setStatus('current')
aal2CpsPerformanceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 5, 1), )
aal2VclEntry.registerAugmentions(("ZhoneAAL2-MIB", "aal2CpsPerformanceEntry"))
aal2CpsPerformanceEntry.setIndexNames(*aal2VclEntry.getIndexNames())
if mibBuilder.loadTexts: aal2CpsPerformanceEntry.setStatus('current')
aal2CpsPerfSTFParity = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 5, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal2CpsPerfSTFParity.setStatus('current')
aal2CpsPerfSTFBadSeq = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 5, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal2CpsPerfSTFBadSeq.setStatus('current')
aal2CpsPerfBadCPSLength = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 5, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal2CpsPerfBadCPSLength.setStatus('current')
aal2CpsPerfBadPayloadLength = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 5, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal2CpsPerfBadPayloadLength.setStatus('current')
aal2CpsPerfHEC = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 5, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal2CpsPerfHEC.setStatus('current')
aal2CpsPerfPayloadTooLong = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 5, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal2CpsPerfPayloadTooLong.setStatus('current')
aal2CpsPerfRessError = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 5, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal2CpsPerfRessError.setStatus('current')
aal2CpsPerfTransError = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 5, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal2CpsPerfTransError.setStatus('current')
aal2CpsPerfIllegalUUI = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 5, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal2CpsPerfIllegalUUI.setStatus('current')
aal2CpsPerfIllegalCID = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 5, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal2CpsPerfIllegalCID.setStatus('current')
aal2CpsPerfCongestion = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 5, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal2CpsPerfCongestion.setStatus('current')
aal2SscsI3662PerfTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 6), )
if mibBuilder.loadTexts: aal2SscsI3662PerfTable.setStatus('current')
aal2SscsI3662PerfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 6, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ATM-MIB", "atmVclVpi"), (0, "ATM-MIB", "atmVclVci"), (0, "ZhoneAAL2-MIB", "aal2Cid"))
if mibBuilder.loadTexts: aal2SscsI3662PerfEntry.setStatus('current')
aal2SscsI3662IllegalUUI = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 6, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal2SscsI3662IllegalUUI.setStatus('current')
aal2SscsI3662Type3CRC = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 6, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal2SscsI3662Type3CRC.setStatus('current')
aal2SscsI3662ProfileError = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 6, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal2SscsI3662ProfileError.setStatus('current')
aal2SscsI3661PerfTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 7), )
if mibBuilder.loadTexts: aal2SscsI3661PerfTable.setStatus('current')
aal2SscsI3661PerfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 7, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ATM-MIB", "atmVclVpi"), (0, "ATM-MIB", "atmVclVci"), (0, "ZhoneAAL2-MIB", "aal2Cid"))
if mibBuilder.loadTexts: aal2SscsI3661PerfEntry.setStatus('current')
aal2SscsI3661MsgTooLong = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 7, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal2SscsI3661MsgTooLong.setStatus('current')
aal2SscsI3661RasTimerExpired = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 7, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal2SscsI3661RasTimerExpired.setStatus('current')
aal2SscsI3661MsgTooShort = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 7, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal2SscsI3661MsgTooShort.setStatus('current')
aal2SscsI3661BadLength = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 7, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal2SscsI3661BadLength.setStatus('current')
aal2SscsI3661CRC = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 7, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal2SscsI3661CRC.setStatus('current')
aal2vpi = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 8), AtmVpIdentifier()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: aal2vpi.setStatus('current')
aal2Vci = MibScalar((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 9), AtmVcIdentifier()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: aal2Vci.setStatus('current')
aal2AlarmConfigTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 10), )
if mibBuilder.loadTexts: aal2AlarmConfigTable.setStatus('current')
aal2AlarmConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 10, 1), )
aal2VclEntry.registerAugmentions(("ZhoneAAL2-MIB", "aal2AlarmConfigEntry"))
aal2AlarmConfigEntry.setIndexNames(*aal2VclEntry.getIndexNames())
if mibBuilder.loadTexts: aal2AlarmConfigEntry.setStatus('current')
aal2AlarmConfigThreshCellLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 10, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 900))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aal2AlarmConfigThreshCellLoss.setStatus('current')
aal2AlarmConfigThreshCongestion = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 10, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 900))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aal2AlarmConfigThreshCongestion.setStatus('current')
aal2ElcpPortTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 11), )
if mibBuilder.loadTexts: aal2ElcpPortTable.setStatus('current')
aal2ElcpPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 11, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ATM-MIB", "atmVclVpi"), (0, "ATM-MIB", "atmVclVci"), (0, "ZhoneAAL2-MIB", "aal2ElcpPortId"), (0, "ZhoneAAL2-MIB", "aal2ElcpPortType"))
if mibBuilder.loadTexts: aal2ElcpPortEntry.setStatus('current')
aal2ElcpPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 11, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32767)))
if mibBuilder.loadTexts: aal2ElcpPortId.setStatus('current')
aal2ElcpPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 11, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("pstn", 1), ("isdnBra", 2))))
if mibBuilder.loadTexts: aal2ElcpPortType.setStatus('current')
aal2ElcpPortAudioService = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 11, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("enabledEchoCancelOff", 3), ("enabledDynamic", 4))).clone('enabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aal2ElcpPortAudioService.setStatus('current')
aal2ElcpPortPCMEncoding = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 11, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("muLaw", 1), ("aLaw", 2))).clone('aLaw')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aal2ElcpPortPCMEncoding.setStatus('current')
aal2ElcpPortMaxLengthFrame = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 11, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(65535)).setUnits('octets').setMaxAccess("readcreate")
if mibBuilder.loadTexts: aal2ElcpPortMaxLengthFrame.setStatus('current')
aal2ElcpPortMaxSDULength = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 11, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65568)).clone(1536)).setUnits('octets').setMaxAccess("readcreate")
if mibBuilder.loadTexts: aal2ElcpPortMaxSDULength.setStatus('current')
aal2ElcpPortPreferredApIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 11, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 512)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aal2ElcpPortPreferredApIndex.setStatus('current')
aal2ElcpPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 11, 1, 8), ZhoneRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aal2ElcpPortRowStatus.setStatus('current')
aal2ElcpIgTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 12), )
if mibBuilder.loadTexts: aal2ElcpIgTable.setStatus('current')
aal2ElcpIgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 12, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ATM-MIB", "atmVclVpi"), (0, "ATM-MIB", "atmVclVci"))
if mibBuilder.loadTexts: aal2ElcpIgEntry.setStatus('current')
aal2ElcpIgOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 12, 1, 1), AtmVorXOperStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal2ElcpIgOperStatus.setStatus('current')
aal2ElcpIgOperStatusChangeCount = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 12, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal2ElcpIgOperStatusChangeCount.setStatus('current')
aal2ElcpIgLapvReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 12, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal2ElcpIgLapvReceived.setStatus('current')
aal2ElcpIgLapvSent = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 4, 2, 1, 12, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aal2ElcpIgLapvSent.setStatus('current')
mibBuilder.exportSymbols("ZhoneAAL2-MIB", aal2CidCAS=aal2CidCAS, aal2SscsI3662IllegalUUI=aal2SscsI3662IllegalUUI, aal2ElcpPortPreferredApIndex=aal2ElcpPortPreferredApIndex, aal2CidSscsType=aal2CidSscsType, aal2ExternalRAI=aal2ExternalRAI, aal2PerfCongestionThreshTrap=aal2PerfCongestionThreshTrap, aal2VclMaxSDULength=aal2VclMaxSDULength, aal2UserDefinedAudioProfileNextIndexTable=aal2UserDefinedAudioProfileNextIndexTable, aal2SscsI3661RasTimerExpired=aal2SscsI3661RasTimerExpired, aal2CidEntry=aal2CidEntry, aal2SscsI3661PerfTable=aal2SscsI3661PerfTable, aal2VclSscsDefaultType=aal2VclSscsDefaultType, aal2VclAudioProfileIdentifier=aal2VclAudioProfileIdentifier, aal2CpsPerfPayloadTooLong=aal2CpsPerfPayloadTooLong, aal2AudioProfileTable=aal2AudioProfileTable, aal2VclTimerCU=aal2VclTimerCU, aal2InternalRDI=aal2InternalRDI, aal2CidCircuitModeData=aal2CidCircuitModeData, aal2ExternalAIS=aal2ExternalAIS, aal2CpsPerfHEC=aal2CpsPerfHEC, aal2UdApNextIndex=aal2UdApNextIndex, aal2VclMaxCpsSduSize=aal2VclMaxCpsSduSize, aal2ApSilenceSupression=aal2ApSilenceSupression, aal2SscsI3662ProfileError=aal2SscsI3662ProfileError, aal2VclMaxLengthFrame=aal2VclMaxLengthFrame, aal2VclFrameModeData=aal2VclFrameModeData, aal2CpsPerfIllegalUUI=aal2CpsPerfIllegalUUI, aal2CidTable=aal2CidTable, aal2Traps=aal2Traps, aal2VclCircuitModeData=aal2VclCircuitModeData, aal2CidCellsReceived=aal2CidCellsReceived, aal2CidMaxSDULength=aal2CidMaxSDULength, aal2SscsI3662PerfTable=aal2SscsI3662PerfTable, aal2SscsI3661BadLength=aal2SscsI3661BadLength, zhoneAtmAAl2=zhoneAtmAAl2, aal2VclFaxDemoRemo=aal2VclFaxDemoRemo, aal2CidMaxLengthFrame=aal2CidMaxLengthFrame, aal2VclAudioService=aal2VclAudioService, aal2CidPreferredApIndex=aal2CidPreferredApIndex, aal2ElcpIgOperStatus=aal2ElcpIgOperStatus, aal2vpi=aal2vpi, aal2ElcpPortMaxSDULength=aal2ElcpPortMaxSDULength, aal2CidCellsSent=aal2CidCellsSent, aal2PerfCellLossThreshTrap=aal2PerfCellLossThreshTrap, aal2SscsI3661CRC=aal2SscsI3661CRC, aal2CidRasTimer=aal2CidRasTimer, aal2SscsI3661MsgTooLong=aal2SscsI3661MsgTooLong, aal2AlarmConfigThreshCellLoss=aal2AlarmConfigThreshCellLoss, aal2CidMfR2DialedDigits=aal2CidMfR2DialedDigits, aal2ApIndex=aal2ApIndex, aal2ElcpIgOperStatusChange=aal2ElcpIgOperStatusChange, aal2CpsPerfIllegalCID=aal2CpsPerfIllegalCID, aal2ApMinUUI=aal2ApMinUUI, aal2CidPCMEncoding=aal2CidPCMEncoding, aal2ElcpIgLapvSent=aal2ElcpIgLapvSent, aal2PvcDown=aal2PvcDown, aal2VclMaxNumberMultiplexChannels=aal2VclMaxNumberMultiplexChannels, aal2CidRowStatus=aal2CidRowStatus, aal2AlarmConfigThreshCongestion=aal2AlarmConfigThreshCongestion, aal2CidCompletedCalls=aal2CidCompletedCalls, aal2VclCellsReceived=aal2VclCellsReceived, aal2VclMaxCidForAal2UserChannels=aal2VclMaxCidForAal2UserChannels, aal2CidAdminStatus=aal2CidAdminStatus, aal2CidFaxDemoRemo=aal2CidFaxDemoRemo, aal2SscsI3661MsgTooShort=aal2SscsI3661MsgTooShort, aal2ElcpPortId=aal2ElcpPortId, aal2ElcpPortPCMEncoding=aal2ElcpPortPCMEncoding, aal2ApAlgorithm=aal2ApAlgorithm, atmVccAal2SigVccI=atmVccAal2SigVccI, aal2ElcpIgOperStatusChangeCount=aal2ElcpIgOperStatusChangeCount, aal2ElcpIgTable=aal2ElcpIgTable, aal2CidMfR1DialedDigits=aal2CidMfR1DialedDigits, aal2ApMaxUUI=aal2ApMaxUUI, aal2ApSequence=aal2ApSequence, aal2VclStatsTimeElapsed=aal2VclStatsTimeElapsed, aal2CidStatsTimeElapsed=aal2CidStatsTimeElapsed, aal2ApPacketLength=aal2ApPacketLength, aal2CpsPerfBadPayloadLength=aal2CpsPerfBadPayloadLength, aal2CidBlockedCallsNoBandwidth=aal2CidBlockedCallsNoBandwidth, aal2Vci=aal2Vci, aal2ElcpIgLapvReceived=aal2ElcpIgLapvReceived, aal2ElcpPortAudioService=aal2ElcpPortAudioService, aal2ElcpPortType=aal2ElcpPortType, aal2Cid=aal2Cid, aal2CidLastChange=aal2CidLastChange, aal2ElcpPortMaxLengthFrame=aal2ElcpPortMaxLengthFrame, aal2VclCAS=aal2VclCAS, aal2ApSduMultiples=aal2ApSduMultiples, aal2VclDTMFDialedDigits=aal2VclDTMFDialedDigits, aal2ApPktTime=aal2ApPktTime, aal2VclMinCidForAal2UserChannels=aal2VclMinCidForAal2UserChannels, aal2CpsPerfCongestion=aal2CpsPerfCongestion, aal2AlarmConfigEntry=aal2AlarmConfigEntry, aal2SscsI3661PerfEntry=aal2SscsI3661PerfEntry, aal2CpsPerfRessError=aal2CpsPerfRessError, aal2CpsPerfTransError=aal2CpsPerfTransError, aal2ElcpPortEntry=aal2ElcpPortEntry, atmVccAal2AppId=atmVccAal2AppId, aal2VclMfR2DialedDigits=aal2VclMfR2DialedDigits, aal2VclTrunkType=aal2VclTrunkType, aal2CpsPerfSTFBadSeq=aal2CpsPerfSTFBadSeq, aal2VclMfR1DialedDigits=aal2VclMfR1DialedDigits, aal2CpsPerformanceEntry=aal2CpsPerformanceEntry, aal2AudioProfileEntry=aal2AudioProfileEntry, aal2CpsPerfSTFParity=aal2CpsPerfSTFParity, aal2VclCellsSent=aal2VclCellsSent, aal2VclRasTimer=aal2VclRasTimer, aal2ApRowStatus=aal2ApRowStatus, PYSNMP_MODULE_ID=zhoneAtmAAl2, aal2VclNextCid=aal2VclNextCid, aal2CidOperStatus=aal2CidOperStatus, atmVccAal2VccI=atmVccAal2VccI, aal2SscsI3662Type3CRC=aal2SscsI3662Type3CRC, aal2CpsPerfBadCPSLength=aal2CpsPerfBadCPSLength, aal2AlarmConfigTable=aal2AlarmConfigTable, aal2CidDTMFDialedDigits=aal2CidDTMFDialedDigits, aal2ElcpPortTable=aal2ElcpPortTable, aal2VclPCMEncoding=aal2VclPCMEncoding, aal2VclEntry=aal2VclEntry, aal2ElcpPortRowStatus=aal2ElcpPortRowStatus, aal2InternalAIS=aal2InternalAIS, aal2UserDefinedAudioProfileNextIndexEntry=aal2UserDefinedAudioProfileNextIndexEntry, aal2SscsI3662PerfEntry=aal2SscsI3662PerfEntry, aal2CidAudioService=aal2CidAudioService, aal2CidFrameModeData=aal2CidFrameModeData, aal2ElcpIgEntry=aal2ElcpIgEntry, aal2VclTable=aal2VclTable, aal2CpsPerformanceTable=aal2CpsPerformanceTable)