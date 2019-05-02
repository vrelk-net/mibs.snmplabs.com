#
# PySNMP MIB module HPN-ICF-PPP-OVER-SONET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-PPP-OVER-SONET-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:40:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ifDescr, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifDescr", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, IpAddress, ModuleIdentity, iso, TimeTicks, ObjectIdentity, Unsigned32, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType, MibIdentifier, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "IpAddress", "ModuleIdentity", "iso", "TimeTicks", "ObjectIdentity", "Unsigned32", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType", "MibIdentifier", "Gauge32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
hpnicfPos = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19))
hpnicfPos.setRevisions(('2013-10-10 17:00', '2010-05-19 17:00', '2007-07-19 17:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpnicfPos.setRevisionsDescriptions(('Update the version of this MIB module', 'Update the version of this MIB module', 'The initial version of this MIB module',))
if mibBuilder.loadTexts: hpnicfPos.setLastUpdated('201310101700Z')
if mibBuilder.loadTexts: hpnicfPos.setOrganization('')
if mibBuilder.loadTexts: hpnicfPos.setContactInfo('')
if mibBuilder.loadTexts: hpnicfPos.setDescription('This MIB manages POS(PPP Over Sonet)interfaces by providing an operational table which controls parameters of each POS interface and reports alarm conditions. ')
hpnicfPosMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1))
hpnicfPosParamTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1), )
if mibBuilder.loadTexts: hpnicfPosParamTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosParamTable.setDescription('The pos parameter table.')
hpnicfPosParamTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfPosParamTableEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosParamTableEntry.setDescription('The entry of pos table.')
hpnicfPosCRC = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("crc32", 1), ("crc16", 2))).clone('crc32')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfPosCRC.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosCRC.setDescription('The length of CRC')
hpnicfPosMTU = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfPosMTU.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosMTU.setDescription('Maximum Transfer Unit (MTU) of POS interface')
hpnicfPosScramble = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 3), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfPosScramble.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosScramble.setDescription('Scrambling is used to avoid continuous 0 or 1 in signals. This object is to decide whether to scramble or not')
hpnicfPosClockSource = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("system", 1), ("line", 2))).clone('line')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfPosClockSource.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosClockSource.setDescription('The value indicates the source of clock signal. System indicates that clock signals are from device itself and line for clock signals from remote')
hpnicfPosSdhFlagJ0 = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfPosSdhFlagJ0.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosSdhFlagJ0.setDescription('The section trace byte. This node is used when the frame type is sdh.')
hpnicfPosSdhFlagJ1 = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfPosSdhFlagJ1.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosSdhFlagJ1.setDescription('The path trace byte. This node is used when the frame type is sdh.')
hpnicfPosSonetFlagJ0 = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfPosSonetFlagJ0.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosSonetFlagJ0.setDescription('The section trace byte. This node is used when the frame type is sonet.')
hpnicfPosSonetFlagJ1 = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 62))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfPosSonetFlagJ1.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosSonetFlagJ1.setDescription('The path trace byte. This node is used when the frame type is sonet.')
hpnicfPosFlagC2 = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(22)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfPosFlagC2.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosFlagC2.setDescription('The parameter for the channel signal value of C2 byte')
hpnicfPosFrameType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sdh", 1), ("sonet", 2))).clone('sdh')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfPosFrameType.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosFrameType.setDescription('The frame type that encapsulates the packet. Default frame type is sdh(Synchronous Digital Hierarchy) It also can be configured using sonet type(Synchronous Optical Network).')
hpnicfPosBindVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfPosBindVlanId.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosBindVlanId.setDescription('The vlan that this pos port binds. The vlan can not include any other port, otherwise error will be returned. If the vlan has a virtual interface, the status of virtual interface will be up or down according to the link status or this pos.')
hpnicfPosEncapsulation = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ppp", 1), ("hdlc", 2), ("fr", 3))).clone('ppp')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfPosEncapsulation.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosEncapsulation.setDescription('The type of encapsulation ')
hpnicfPoskeepaliveTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32767))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfPoskeepaliveTimeout.setStatus('current')
if mibBuilder.loadTexts: hpnicfPoskeepaliveTimeout.setDescription('The keeplive of ppp, hdlc or fr. It is the query interval of link status. Two members of a link should have same keeplive. The default 0 prohibits detecting status of link.')
hpnicfPosBERthresholdSF = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 9)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfPosBERthresholdSF.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosBERthresholdSF.setDescription('The bit-error rate threshold for Signal Fault. SF threshold should be greater than SD threshold.')
hpnicfPosBERthresholdSD = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 9)).clone(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfPosBERthresholdSD.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosBERthresholdSD.setDescription('The bit-error rate threshold for Signal Degrade. SD threshold should be less than SF threshold.')
hpnicfPosB1Error = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfPosB1Error.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosB1Error.setDescription('Counter for SBIPE(Section Bit Interleave Parity Error)')
hpnicfPosB2Error = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfPosB2Error.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosB2Error.setDescription('Counter for LBIPE(Line Bit Interleave Parity Error)')
hpnicfPosB3Error = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfPosB3Error.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosB3Error.setDescription('Counter for PBIPE(Path Bit Interleave Parity Error)')
hpnicfPosM1Error = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfPosM1Error.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosM1Error.setDescription('How many times does LREI(Line Remote Error Indication) occur')
hpnicfPosG1Error = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 20), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfPosG1Error.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosG1Error.setDescription('How many times does PREI(Path Remote Error Indication) occur')
hpnicfPosFlagJ0Type = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sdh", 1), ("sonet", 2))).clone('sdh')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfPosFlagJ0Type.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosFlagJ0Type.setDescription('The frame type that encapsulates the flag J0. Default frame type is sdh(Synchronous Digital Hierarchy). It also can be configured using sonet(Synchronous Optical Network) type.')
hpnicfPosFlagJ1Type = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sdh", 1), ("sonet", 2))).clone('sdh')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfPosFlagJ1Type.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosFlagJ1Type.setDescription('The frame type that encapsulates the flag J1. Default frame type is sdh(Synchronous Digital Hierarchy). It also can be configured using sonet(Synchronous Optical Network) type.')
hpnicfPosB1TCAThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 9)).clone(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfPosB1TCAThreshold.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosB1TCAThreshold.setDescription('Threshold for B1 TCA.')
hpnicfPosB2TCAThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 24), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 9)).clone(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfPosB2TCAThreshold.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosB2TCAThreshold.setDescription('Threshold for B2 TCA.')
hpnicfPosB3TCAThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 25), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 9)).clone(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfPosB3TCAThreshold.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosB3TCAThreshold.setDescription('Threshold for B3 TCA.')
hpnicfPosB1TCAEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfPosB1TCAEnable.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosB1TCAEnable.setDescription('Enable traps of B1 TCA.')
hpnicfPosB2TCAEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfPosB2TCAEnable.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosB2TCAEnable.setDescription('Enable traps of B2 TCA.')
hpnicfPosB3TCAEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 1, 1, 1, 28), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfPosB3TCAEnable.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosB3TCAEnable.setDescription('Enable traps of B3 TCA.')
hpnicfPosMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 2))
hpnicfPosMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 2, 0))
hpnicfPosLOSAlarm = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 2, 0, 1)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfPosLOSAlarm.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosLOSAlarm.setDescription('Alarm indicates loss of signal')
hpnicfPosLOFAlarm = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 2, 0, 2)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfPosLOFAlarm.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosLOFAlarm.setDescription('Alarm indicates loss of frame')
hpnicfPosOOFAlarm = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 2, 0, 3)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfPosOOFAlarm.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosOOFAlarm.setDescription('Alarm indicates out of frame')
hpnicfPosLAISAlarm = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 2, 0, 4)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfPosLAISAlarm.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosLAISAlarm.setDescription('Alarm when LAIS(Line Alarm Indication Signal) arrives')
hpnicfPosLRDIAlarm = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 2, 0, 5)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfPosLRDIAlarm.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosLRDIAlarm.setDescription('Alarm when LRDI(Line Remote Defect Indication) arrives')
hpnicfPosPRDIAlarm = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 2, 0, 6)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfPosPRDIAlarm.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosPRDIAlarm.setDescription('Alarm when PRDI(Path Remote Defect Indication) arrives')
hpnicfPosPAISAlarm = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 2, 0, 7)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfPosPAISAlarm.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosPAISAlarm.setDescription('Alarm when PAIS(Path Alarm Indication Signal) arrives')
hpnicfPosLOPAlarm = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 2, 0, 8)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfPosLOPAlarm.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosLOPAlarm.setDescription('Alarm indicates loss of pointer')
hpnicfPosSTIMAlarm = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 2, 0, 9)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfPosSTIMAlarm.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosSTIMAlarm.setDescription('Alarm indicates inconsistency between sent and received J0 bytes.')
hpnicfPosPTIMAlarm = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 2, 0, 10)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfPosPTIMAlarm.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosPTIMAlarm.setDescription('Alarm indicates inconsistency between sent and received J1 bytes.')
hpnicfPosPSLMAlarm = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 2, 0, 11)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfPosPSLMAlarm.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosPSLMAlarm.setDescription('Alarm indicates a mismatched C2 byte.')
hpnicfPosLSDAlarm = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 2, 0, 12)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfPosLSDAlarm.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosLSDAlarm.setDescription('Alarm indicates that the B2 bit-error rate exceeds SD threshold.')
hpnicfPosLSFAlarm = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 2, 0, 13)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfPosLSFAlarm.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosLSFAlarm.setDescription('Alarm indicates that the B2 bit-error rate exceeds SF threshold.')
hpnicfPosNormalAlarm = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 2, 0, 14)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfPosNormalAlarm.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosNormalAlarm.setDescription('Alarm indicates that the Pos interface state returns normal.')
hpnicfPosB1TCAlarm = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 2, 0, 15)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: hpnicfPosB1TCAlarm.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosB1TCAlarm.setDescription('Threshold crossing alarms for B1.')
hpnicfPosB2TCAlarm = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 2, 0, 16)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: hpnicfPosB2TCAlarm.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosB2TCAlarm.setDescription('Threshold crossing alarms for B2.')
hpnicfPosB3TCAlarm = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 19, 2, 0, 17)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: hpnicfPosB3TCAlarm.setStatus('current')
if mibBuilder.loadTexts: hpnicfPosB3TCAlarm.setDescription('Threshold crossing alarms for B3.')
mibBuilder.exportSymbols("HPN-ICF-PPP-OVER-SONET-MIB", hpnicfPosB1TCAlarm=hpnicfPosB1TCAlarm, hpnicfPosPTIMAlarm=hpnicfPosPTIMAlarm, hpnicfPosSonetFlagJ1=hpnicfPosSonetFlagJ1, hpnicfPos=hpnicfPos, hpnicfPosB1TCAEnable=hpnicfPosB1TCAEnable, hpnicfPosMIBObjects=hpnicfPosMIBObjects, hpnicfPosFlagJ0Type=hpnicfPosFlagJ0Type, hpnicfPosB2TCAEnable=hpnicfPosB2TCAEnable, hpnicfPosLOFAlarm=hpnicfPosLOFAlarm, hpnicfPosB1Error=hpnicfPosB1Error, hpnicfPosPRDIAlarm=hpnicfPosPRDIAlarm, hpnicfPosMIBNotificationsPrefix=hpnicfPosMIBNotificationsPrefix, hpnicfPosB2Error=hpnicfPosB2Error, hpnicfPosBERthresholdSD=hpnicfPosBERthresholdSD, hpnicfPosParamTableEntry=hpnicfPosParamTableEntry, hpnicfPosLOPAlarm=hpnicfPosLOPAlarm, hpnicfPosSdhFlagJ1=hpnicfPosSdhFlagJ1, hpnicfPosFrameType=hpnicfPosFrameType, hpnicfPosMIBNotifications=hpnicfPosMIBNotifications, hpnicfPosLOSAlarm=hpnicfPosLOSAlarm, hpnicfPosB3TCAThreshold=hpnicfPosB3TCAThreshold, hpnicfPosMTU=hpnicfPosMTU, hpnicfPosSTIMAlarm=hpnicfPosSTIMAlarm, hpnicfPosNormalAlarm=hpnicfPosNormalAlarm, hpnicfPosOOFAlarm=hpnicfPosOOFAlarm, hpnicfPosG1Error=hpnicfPosG1Error, hpnicfPosBERthresholdSF=hpnicfPosBERthresholdSF, hpnicfPosB2TCAlarm=hpnicfPosB2TCAlarm, hpnicfPosB2TCAThreshold=hpnicfPosB2TCAThreshold, hpnicfPosCRC=hpnicfPosCRC, hpnicfPosClockSource=hpnicfPosClockSource, hpnicfPosB1TCAThreshold=hpnicfPosB1TCAThreshold, hpnicfPosLRDIAlarm=hpnicfPosLRDIAlarm, hpnicfPosLSFAlarm=hpnicfPosLSFAlarm, hpnicfPosB3TCAlarm=hpnicfPosB3TCAlarm, hpnicfPosM1Error=hpnicfPosM1Error, hpnicfPosParamTable=hpnicfPosParamTable, hpnicfPosBindVlanId=hpnicfPosBindVlanId, PYSNMP_MODULE_ID=hpnicfPos, hpnicfPosSonetFlagJ0=hpnicfPosSonetFlagJ0, hpnicfPoskeepaliveTimeout=hpnicfPoskeepaliveTimeout, hpnicfPosScramble=hpnicfPosScramble, hpnicfPosEncapsulation=hpnicfPosEncapsulation, hpnicfPosPSLMAlarm=hpnicfPosPSLMAlarm, hpnicfPosLSDAlarm=hpnicfPosLSDAlarm, hpnicfPosFlagJ1Type=hpnicfPosFlagJ1Type, hpnicfPosLAISAlarm=hpnicfPosLAISAlarm, hpnicfPosB3Error=hpnicfPosB3Error, hpnicfPosB3TCAEnable=hpnicfPosB3TCAEnable, hpnicfPosFlagC2=hpnicfPosFlagC2, hpnicfPosSdhFlagJ0=hpnicfPosSdhFlagJ0, hpnicfPosPAISAlarm=hpnicfPosPAISAlarm)