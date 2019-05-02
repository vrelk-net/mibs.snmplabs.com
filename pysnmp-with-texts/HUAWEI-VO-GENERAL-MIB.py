#
# PySNMP MIB module HUAWEI-VO-GENERAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-VO-GENERAL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:49:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
voice, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "voice")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, NotificationType, ObjectIdentity, Unsigned32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, iso, Bits, Counter64, MibIdentifier, Counter32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "ObjectIdentity", "Unsigned32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "iso", "Bits", "Counter64", "MibIdentifier", "Counter32", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hwVoiceGeneralMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1))
hwVoiceGeneralMIB.setRevisions(('2004-04-08 13:45',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hwVoiceGeneralMIB.setRevisionsDescriptions(('',))
if mibBuilder.loadTexts: hwVoiceGeneralMIB.setLastUpdated('200410200000Z')
if mibBuilder.loadTexts: hwVoiceGeneralMIB.setOrganization('Huawei-3COM Technologies Co., Ltd.')
if mibBuilder.loadTexts: hwVoiceGeneralMIB.setContactInfo('PLAT Team Huawei 3Com Technologies co.,Ltd. Shang-Di Information Industry Base, Hai-Dian District Beijing P.R. China http://www.huawei-3com.com Zip:100085')
if mibBuilder.loadTexts: hwVoiceGeneralMIB.setDescription(' ')
class EntryStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("valid", 1), ("createRequest", 2), ("underCreation", 3), ("invalid", 4))

hwVoiceGeneralObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1))
hwVoiceGeneralGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 1))
hwVoGeneralJitterLen = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoGeneralJitterLen.setStatus('current')
if mibBuilder.loadTexts: hwVoGeneralJitterLen.setDescription('This object specifies the length of the Jitter buffer. The default value is 3.')
hwVoGeneralMatchPolicy = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("long", 1), ("short", 2))).clone('short')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoGeneralMatchPolicy.setStatus('current')
if mibBuilder.loadTexts: hwVoGeneralMatchPolicy.setDescription('This object specifies match number policy of this gateway. The default value is short.')
hwVoGeneralSendPerformance = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("fast", 2))).clone('normal')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoGeneralSendPerformance.setStatus('current')
if mibBuilder.loadTexts: hwVoGeneralSendPerformance.setDescription('This object specifies the performance of sending voice data. The default value is normal.')
hwVoGeneralReceivePerformance = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("fast", 2))).clone('normal')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoGeneralReceivePerformance.setStatus('current')
if mibBuilder.loadTexts: hwVoGeneralReceivePerformance.setDescription('This object specifies the performance of receiving voice data. The default value is normal')
hwVoGeneralDataStatistics = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoGeneralDataStatistics.setStatus('current')
if mibBuilder.loadTexts: hwVoGeneralDataStatistics.setDescription('Enable/disable data statistics')
hwVoGeneralPacketPrecedence = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoGeneralPacketPrecedence.setStatus('current')
if mibBuilder.loadTexts: hwVoGeneralPacketPrecedence.setDescription('Set global Voip packet precedence')
hwVoGeneralDialTerminator = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoGeneralDialTerminator.setStatus('current')
if mibBuilder.loadTexts: hwVoGeneralDialTerminator.setDescription('Set global Dial Terminator')
hwVoGeneralCallStart = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fast", 1), ("normal", 2))).clone('fast')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoGeneralCallStart.setStatus('current')
if mibBuilder.loadTexts: hwVoGeneralCallStart.setDescription('Set the start mode of called over IP')
hwVoGeneralCalledTunnel = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoGeneralCalledTunnel.setStatus('current')
if mibBuilder.loadTexts: hwVoGeneralCalledTunnel.setDescription('Enable/disable Called tunnel function')
hwVoGeneralSpecialServiceEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoGeneralSpecialServiceEnable.setStatus('current')
if mibBuilder.loadTexts: hwVoGeneralSpecialServiceEnable.setDescription('This object sepcifies whether special service number function is enable or disable.')
hwVoGeneralCallTransferSpecialServiceNumber = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 12)).clone('*12*')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoGeneralCallTransferSpecialServiceNumber.setStatus('current')
if mibBuilder.loadTexts: hwVoGeneralCallTransferSpecialServiceNumber.setDescription('This object specifies the call-transfer special service number in talking.')
hwVoGeneralPeerSearchStop = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 200)).clone(200)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoGeneralPeerSearchStop.setStatus('current')
if mibBuilder.loadTexts: hwVoGeneralPeerSearchStop.setDescription('This object specifies the maximum in searching entities.')
hwVoGeneralPeerSelectOrderRule = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 18))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoGeneralPeerSelectOrderRule.setStatus('current')
if mibBuilder.loadTexts: hwVoGeneralPeerSelectOrderRule.setDescription('This object specifies the rule order applied in voice entity selection. 0 --- explicit match, priority, random 1 --- explicit match, priority, longest no use 2 --- explicit match, longest no use, priority 3 --- explicit match, longest no use, random 4 --- priority, explicit match, random 5 --- priority, explicit match, longest no usep 6 --- riority, longest no use, explicit match 7 --- priority, longest no use, random 8 --- longest no use, explicit match, priority 9 --- longest no use, explicit match, random 10 --- longest no use, priority, explicit match 11 --- longest no use, priority, random 12 --- explicit match, random 13 --- priority, random 14 --- longest no use, random 15 --- explicit match 16 --- priority 17 --- random 18 --- longest no use ')
hwVoGeneralPeerSelectTypePriority = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 6))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoGeneralPeerSelectTypePriority.setStatus('current')
if mibBuilder.loadTexts: hwVoGeneralPeerSelectTypePriority.setDescription('This object specifies the priority-ranked type of voice entity. 1ST 2DN 3RD 0 --- NONE TYPE 1 --- VOIP POTS VOFR 2 --- VOIP VOFR POTS 3 --- POTS VOIP VOFR 4 --- POTS VOFR VOIP 5 --- VOFR POTS VOIP 6 --- VOFR POTS POTS ')
hwVoDialExpansionTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 3), )
if mibBuilder.loadTexts: hwVoDialExpansionTable.setStatus('current')
if mibBuilder.loadTexts: hwVoDialExpansionTable.setDescription('The table contains the information of the Dial Expansion Record .')
hwVoDialExpansionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 3, 1), ).setIndexNames((0, "HUAWEI-VO-GENERAL-MIB", "hwVoDialExpansionType"), (0, "HUAWEI-VO-GENERAL-MIB", "hwVoDialExpansionSource"))
if mibBuilder.loadTexts: hwVoDialExpansionEntry.setStatus('current')
if mibBuilder.loadTexts: hwVoDialExpansionEntry.setDescription('The information regarding a Dial Expansion Record.')
hwVoDialExpansionType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("callin", 0), ("callout", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoDialExpansionType.setStatus('current')
if mibBuilder.loadTexts: hwVoDialExpansionType.setDescription('The call direction of the Dial Expansion. ')
hwVoDialExpansionSource = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoDialExpansionSource.setStatus('current')
if mibBuilder.loadTexts: hwVoDialExpansionSource.setDescription('This source telephone of the Dial Expansion. ')
hwVoDialExpansionTarget = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 3, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoDialExpansionTarget.setStatus('current')
if mibBuilder.loadTexts: hwVoDialExpansionTarget.setDescription('This target telephone of the Dial Expansion. ')
hwVoDialExpansionRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 3, 1, 4), EntryStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoDialExpansionRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwVoDialExpansionRowStatus.setDescription('This object is used to create a new row or modify or delete an existing row in this table. ')
hwVoLtoPTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 2), )
if mibBuilder.loadTexts: hwVoLtoPTable.setStatus('current')
if mibBuilder.loadTexts: hwVoLtoPTable.setDescription('The table contains the relation information of Voice logic channel and voice physical channel.')
hwVoLtoPEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 2, 1), ).setIndexNames((0, "HUAWEI-VO-GENERAL-MIB", "hwVoLtoPChannel"))
if mibBuilder.loadTexts: hwVoLtoPEntry.setStatus('current')
if mibBuilder.loadTexts: hwVoLtoPEntry.setDescription('The information regarding a single logic voice channel .')
hwVoLtoPChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoLtoPChannel.setStatus('current')
if mibBuilder.loadTexts: hwVoLtoPChannel.setDescription('The number of this logic voice channel .')
hwVoLtoPSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoLtoPSlot.setStatus('current')
if mibBuilder.loadTexts: hwVoLtoPSlot.setDescription('The physical slot number which this logic voice channel based on.')
hwVoLtoPPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoLtoPPort.setStatus('current')
if mibBuilder.loadTexts: hwVoLtoPPort.setDescription('The physical port number which this logic voice channel based on.')
hwVoLtoPTimeSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoLtoPTimeSlot.setStatus('current')
if mibBuilder.loadTexts: hwVoLtoPTimeSlot.setDescription("The timeslots map this logic channel is using . -1 represent this channel cann't be used by voice.")
hwVoLtoPStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoLtoPStatus.setStatus('current')
if mibBuilder.loadTexts: hwVoLtoPStatus.setDescription('The current status of the physical voice channel.')
hwVoLtoPBoardType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("fxs2", 1), ("fxo2", 2), ("em2", 3), ("fxs4", 4), ("fxo4", 5), ("em4", 6), ("e1vi", 7), ("t1vi", 8), ("sic-fxs1", 9), ("sic-fxo1", 10), ("sic-fxs2", 11), ("sic-fxo2", 12)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoLtoPBoardType.setStatus('current')
if mibBuilder.loadTexts: hwVoLtoPBoardType.setDescription('The board type of the physical voice channel.')
hwVoLtoPPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoLtoPPortNumber.setStatus('current')
if mibBuilder.loadTexts: hwVoLtoPPortNumber.setDescription("The global port number of the logic voice channel. -1 represent this channel cann't be used by voice.")
hwVoLtoPGroupNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, 30), ValueRangeConstraint(255, 255), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoLtoPGroupNumber.setStatus('current')
if mibBuilder.loadTexts: hwVoLtoPGroupNumber.setDescription("The global group number of the logic voice channel. . -1 represent this channel cann't be used by voice .")
hwVoiceNumberSubstGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 4))
hwVoNumSubstTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 4, 1), )
if mibBuilder.loadTexts: hwVoNumSubstTable.setStatus('current')
if mibBuilder.loadTexts: hwVoNumSubstTable.setDescription('The table is the number-substitute rule table. It contains the table index, dot match rule and the first rule tag that the rule is used firstly.')
hwVoNumSubstEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 4, 1, 1), ).setIndexNames((0, "HUAWEI-VO-GENERAL-MIB", "hwVoNumSubstIndex"))
if mibBuilder.loadTexts: hwVoNumSubstEntry.setStatus('current')
if mibBuilder.loadTexts: hwVoNumSubstEntry.setDescription('A number-substitute rule list. One entry per number-substite rule list.')
hwVoNumSubstIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoNumSubstIndex.setStatus('current')
if mibBuilder.loadTexts: hwVoNumSubstIndex.setDescription('The index uniquely identifies a number-substitute rule list. It is valid if its value is between 1 and 2147483647.')
hwVoNumSubstFirstRule = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 127), ValueRangeConstraint(65535, 65535), )).clone(65535)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoNumSubstFirstRule.setStatus('current')
if mibBuilder.loadTexts: hwVoNumSubstFirstRule.setDescription('This object specifies the first rule to be used firstly. It is valid if its value is between 0 and 127.')
hwVoNumSubstDotMatchRule = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("end-only", 1), ("left-right", 2), ("right-left", 3))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoNumSubstDotMatchRule.setStatus('current')
if mibBuilder.loadTexts: hwVoNumSubstDotMatchRule.setDescription('This object specifies the dot wildcard match rule. end-only - only end of E.164 number (input format) left-right - match form left to right (input format) right-left - match form right to left (input format) ')
hwVoNumSubstRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 4, 1, 1, 4), EntryStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoNumSubstRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwVoNumSubstRowStatus.setDescription('This object is used to create a new row or modify or delete an existing row in this table.')
hwVoNumSubstRuleTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 4, 2), )
if mibBuilder.loadTexts: hwVoNumSubstRuleTable.setStatus('current')
if mibBuilder.loadTexts: hwVoNumSubstRuleTable.setDescription('The table contains the number-substitute rule information that is used to create an rule row with an appropriate rule index.')
hwVoNumSubstRuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 4, 2, 1), ).setIndexNames((0, "HUAWEI-VO-GENERAL-MIB", "hwVoNumSubstIndex"), (0, "HUAWEI-VO-GENERAL-MIB", "hwVoNumSubstRuleIndex"))
if mibBuilder.loadTexts: hwVoNumSubstRuleEntry.setStatus('current')
if mibBuilder.loadTexts: hwVoNumSubstRuleEntry.setDescription('A single number-substitute rule. One entry per number-substitute rule.')
hwVoNumSubstRuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoNumSubstRuleIndex.setStatus('current')
if mibBuilder.loadTexts: hwVoNumSubstRuleIndex.setDescription('The index uniquely identifies a number-substitute rule. It is valid if its value is between 0 and 127.')
hwVoNumSubstRuleInputFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 4, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoNumSubstRuleInputFormat.setStatus('current')
if mibBuilder.loadTexts: hwVoNumSubstRuleInputFormat.setDescription('This object specifies the input match format that must be of the form ^(\\^)!(\\+)!([0-9ABCD.*%!#]+)(\\$)!$.')
hwVoNumSubstRuleOutputFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 4, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoNumSubstRuleOutputFormat.setStatus('current')
if mibBuilder.loadTexts: hwVoNumSubstRuleOutputFormat.setDescription('This object specifies the output format that must be of the form ^[0-9#.]+$.')
hwVoNumSubstRuleRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 4, 2, 1, 4), EntryStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoNumSubstRuleRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwVoNumSubstRuleRowStatus.setDescription('This object is used to create a new row or modify or delete an existing row in this table.')
hwVoMaxCallTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 5), )
if mibBuilder.loadTexts: hwVoMaxCallTable.setStatus('current')
if mibBuilder.loadTexts: hwVoMaxCallTable.setDescription('The table stores The table stores the maximum number of allowed connections for a set of voice entities.')
hwVoMaxCallEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 5, 1), ).setIndexNames((0, "HUAWEI-VO-GENERAL-MIB", "hwVoMaxCallTableIndex"))
if mibBuilder.loadTexts: hwVoMaxCallEntry.setStatus('current')
if mibBuilder.loadTexts: hwVoMaxCallEntry.setDescription('A single value of maximum call connections. One entry per maximum call connections.')
hwVoMaxCallTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoMaxCallTableIndex.setStatus('current')
if mibBuilder.loadTexts: hwVoMaxCallTableIndex.setDescription('The index uniquely identifies a single maximum call value. It is valid if its value is between 1 and 2147483647.')
hwVoMaxCallValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 120))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoMaxCallValue.setStatus('current')
if mibBuilder.loadTexts: hwVoMaxCallValue.setDescription('This object specifies a single maximum call value. It is valid if its value is between 0 and 120.')
hwVoMaxCallTableRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 5, 1, 3), EntryStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoMaxCallTableRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwVoMaxCallTableRowStatus.setDescription('This object is used to create a new row or modify or delete an existing row in this table.')
hwVoIncomingCallingNumSubstTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 6), )
if mibBuilder.loadTexts: hwVoIncomingCallingNumSubstTable.setStatus('current')
if mibBuilder.loadTexts: hwVoIncomingCallingNumSubstTable.setDescription('The table stores the number-substitute rule list tag that these number-substitute rule list will be used for incoming-call caller number.The table can hold max 32 rows.')
hwVoIncomingCallingNumSubstEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 6, 1), ).setIndexNames((0, "HUAWEI-VO-GENERAL-MIB", "hwVoIncomingCallingNumSubstIndex"))
if mibBuilder.loadTexts: hwVoIncomingCallingNumSubstEntry.setStatus('current')
if mibBuilder.loadTexts: hwVoIncomingCallingNumSubstEntry.setDescription('A number-substitute rule list tag. One entry per number-substite rule list tag.')
hwVoIncomingCallingNumSubstIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoIncomingCallingNumSubstIndex.setStatus('current')
if mibBuilder.loadTexts: hwVoIncomingCallingNumSubstIndex.setDescription('This object specifies a number-substitute rule that apply caller number for incoming call. It is valid if its value is between 1 and 2147483647.')
hwVoIncomingCallingNumSubstRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 6, 1, 2), EntryStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoIncomingCallingNumSubstRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwVoIncomingCallingNumSubstRowStatus.setDescription('This object is used to create a new row or modify or delete an existing row in this table.')
hwVoIncomingCalledNumSubstTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 7), )
if mibBuilder.loadTexts: hwVoIncomingCalledNumSubstTable.setStatus('current')
if mibBuilder.loadTexts: hwVoIncomingCalledNumSubstTable.setDescription('The table stores the number-substitute rule list tag that these number-substitute rule list will be used for incoming-call caller number.The table can hold max 32 rows.')
hwVoIncomingCalledNumSubstEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 7, 1), ).setIndexNames((0, "HUAWEI-VO-GENERAL-MIB", "hwVoIncomingCalledNumSubstIndex"))
if mibBuilder.loadTexts: hwVoIncomingCalledNumSubstEntry.setStatus('current')
if mibBuilder.loadTexts: hwVoIncomingCalledNumSubstEntry.setDescription('A number-substitute rule list tag. One entry per number-substite rule list tag.')
hwVoIncomingCalledNumSubstIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoIncomingCalledNumSubstIndex.setStatus('current')
if mibBuilder.loadTexts: hwVoIncomingCalledNumSubstIndex.setDescription('This object specifies a number-substitute rule that apply caller number for incoming call. It is valid if its value is between 1 and 2147483647.')
hwVoIncomingCalledNumSubstRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 7, 1, 2), EntryStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoIncomingCalledNumSubstRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwVoIncomingCalledNumSubstRowStatus.setDescription('This object is used to create a new row or modify or delete an existing row in this table.')
hwVoOutgoingCallingNumSubstTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 8), )
if mibBuilder.loadTexts: hwVoOutgoingCallingNumSubstTable.setStatus('current')
if mibBuilder.loadTexts: hwVoOutgoingCallingNumSubstTable.setDescription('The table stores the number-substitute rule list tag that these number-substitute rule list will be used for incoming-call caller number.The table can hold max 32 rows.')
hwVoOutgoingCallingNumSubstEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 8, 1), ).setIndexNames((0, "HUAWEI-VO-GENERAL-MIB", "hwVoOutgoingCallingNumSubstIndex"))
if mibBuilder.loadTexts: hwVoOutgoingCallingNumSubstEntry.setStatus('current')
if mibBuilder.loadTexts: hwVoOutgoingCallingNumSubstEntry.setDescription('A number-substitute rule list tag. One entry per number-substite rule list tag.')
hwVoOutgoingCallingNumSubstIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoOutgoingCallingNumSubstIndex.setStatus('current')
if mibBuilder.loadTexts: hwVoOutgoingCallingNumSubstIndex.setDescription('This object specifies a number-substitute rule that apply caller number for incoming call. It is valid if its value is between 1 and 2147483647.')
hwVoOutgoingCallingNumSubstRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 8, 1, 2), EntryStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoOutgoingCallingNumSubstRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwVoOutgoingCallingNumSubstRowStatus.setDescription('This object is used to create a new row or modify or delete an existing row in this table.')
hwVoOutgoingCalledNumSubstTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 9), )
if mibBuilder.loadTexts: hwVoOutgoingCalledNumSubstTable.setStatus('current')
if mibBuilder.loadTexts: hwVoOutgoingCalledNumSubstTable.setDescription('The table stores the number-substitute rule list tag that these number-substitute rule list will be used for incoming-call caller number.The table can hold max 32 rows.')
hwVoOutgoingCalledNumSubstEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 9, 1), ).setIndexNames((0, "HUAWEI-VO-GENERAL-MIB", "hwVoOutgoingCalledNumSubstIndex"))
if mibBuilder.loadTexts: hwVoOutgoingCalledNumSubstEntry.setStatus('current')
if mibBuilder.loadTexts: hwVoOutgoingCalledNumSubstEntry.setDescription('A number-substitute rule list tag. One entry per number-substite rule list tag.')
hwVoOutgoingCalledNumSubstIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 9, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoOutgoingCalledNumSubstIndex.setStatus('current')
if mibBuilder.loadTexts: hwVoOutgoingCalledNumSubstIndex.setDescription('This object specifies a number-substitute rule that apply caller number for incoming call. It is valid if its value is between 1 and 2147483647.')
hwVoOutgoingCalledNumSubstRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 1, 1, 9, 1, 2), EntryStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoOutgoingCalledNumSubstRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwVoOutgoingCalledNumSubstRowStatus.setDescription('This object is used to create a new row or modify or delete an existing row in this table.')
mibBuilder.exportSymbols("HUAWEI-VO-GENERAL-MIB", hwVoLtoPPort=hwVoLtoPPort, hwVoNumSubstIndex=hwVoNumSubstIndex, hwVoiceGeneralObjects=hwVoiceGeneralObjects, hwVoNumSubstRuleInputFormat=hwVoNumSubstRuleInputFormat, hwVoNumSubstTable=hwVoNumSubstTable, hwVoDialExpansionTarget=hwVoDialExpansionTarget, hwVoGeneralSendPerformance=hwVoGeneralSendPerformance, hwVoDialExpansionEntry=hwVoDialExpansionEntry, hwVoMaxCallEntry=hwVoMaxCallEntry, hwVoIncomingCalledNumSubstEntry=hwVoIncomingCalledNumSubstEntry, hwVoOutgoingCallingNumSubstTable=hwVoOutgoingCallingNumSubstTable, hwVoGeneralCallTransferSpecialServiceNumber=hwVoGeneralCallTransferSpecialServiceNumber, hwVoMaxCallTable=hwVoMaxCallTable, hwVoNumSubstRuleTable=hwVoNumSubstRuleTable, hwVoOutgoingCalledNumSubstIndex=hwVoOutgoingCalledNumSubstIndex, hwVoGeneralPacketPrecedence=hwVoGeneralPacketPrecedence, hwVoIncomingCallingNumSubstIndex=hwVoIncomingCallingNumSubstIndex, hwVoOutgoingCallingNumSubstEntry=hwVoOutgoingCallingNumSubstEntry, hwVoDialExpansionTable=hwVoDialExpansionTable, hwVoGeneralMatchPolicy=hwVoGeneralMatchPolicy, hwVoLtoPEntry=hwVoLtoPEntry, hwVoGeneralPeerSearchStop=hwVoGeneralPeerSearchStop, hwVoLtoPSlot=hwVoLtoPSlot, hwVoLtoPStatus=hwVoLtoPStatus, hwVoNumSubstRuleRowStatus=hwVoNumSubstRuleRowStatus, hwVoMaxCallValue=hwVoMaxCallValue, hwVoMaxCallTableRowStatus=hwVoMaxCallTableRowStatus, hwVoNumSubstEntry=hwVoNumSubstEntry, hwVoGeneralPeerSelectTypePriority=hwVoGeneralPeerSelectTypePriority, hwVoLtoPBoardType=hwVoLtoPBoardType, hwVoOutgoingCalledNumSubstRowStatus=hwVoOutgoingCalledNumSubstRowStatus, hwVoNumSubstRuleIndex=hwVoNumSubstRuleIndex, hwVoDialExpansionRowStatus=hwVoDialExpansionRowStatus, hwVoIncomingCallingNumSubstEntry=hwVoIncomingCallingNumSubstEntry, hwVoOutgoingCallingNumSubstRowStatus=hwVoOutgoingCallingNumSubstRowStatus, hwVoIncomingCallingNumSubstTable=hwVoIncomingCallingNumSubstTable, hwVoLtoPChannel=hwVoLtoPChannel, hwVoNumSubstRowStatus=hwVoNumSubstRowStatus, hwVoNumSubstDotMatchRule=hwVoNumSubstDotMatchRule, hwVoGeneralDialTerminator=hwVoGeneralDialTerminator, hwVoIncomingCallingNumSubstRowStatus=hwVoIncomingCallingNumSubstRowStatus, PYSNMP_MODULE_ID=hwVoiceGeneralMIB, hwVoOutgoingCalledNumSubstTable=hwVoOutgoingCalledNumSubstTable, hwVoGeneralPeerSelectOrderRule=hwVoGeneralPeerSelectOrderRule, hwVoGeneralCallStart=hwVoGeneralCallStart, hwVoLtoPPortNumber=hwVoLtoPPortNumber, hwVoGeneralCalledTunnel=hwVoGeneralCalledTunnel, hwVoGeneralJitterLen=hwVoGeneralJitterLen, hwVoGeneralReceivePerformance=hwVoGeneralReceivePerformance, hwVoDialExpansionType=hwVoDialExpansionType, hwVoLtoPGroupNumber=hwVoLtoPGroupNumber, hwVoiceNumberSubstGroup=hwVoiceNumberSubstGroup, hwVoIncomingCalledNumSubstTable=hwVoIncomingCalledNumSubstTable, hwVoIncomingCalledNumSubstIndex=hwVoIncomingCalledNumSubstIndex, hwVoNumSubstRuleEntry=hwVoNumSubstRuleEntry, hwVoiceGeneralGroup=hwVoiceGeneralGroup, hwVoNumSubstFirstRule=hwVoNumSubstFirstRule, hwVoIncomingCalledNumSubstRowStatus=hwVoIncomingCalledNumSubstRowStatus, hwVoMaxCallTableIndex=hwVoMaxCallTableIndex, hwVoDialExpansionSource=hwVoDialExpansionSource, hwVoLtoPTable=hwVoLtoPTable, hwVoGeneralDataStatistics=hwVoGeneralDataStatistics, hwVoNumSubstRuleOutputFormat=hwVoNumSubstRuleOutputFormat, hwVoGeneralSpecialServiceEnable=hwVoGeneralSpecialServiceEnable, hwVoOutgoingCalledNumSubstEntry=hwVoOutgoingCalledNumSubstEntry, hwVoLtoPTimeSlot=hwVoLtoPTimeSlot, EntryStatus=EntryStatus, hwVoOutgoingCallingNumSubstIndex=hwVoOutgoingCallingNumSubstIndex, hwVoiceGeneralMIB=hwVoiceGeneralMIB)