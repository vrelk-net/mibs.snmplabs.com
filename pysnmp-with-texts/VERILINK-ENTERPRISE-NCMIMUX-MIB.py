#
# PySNMP MIB module VERILINK-ENTERPRISE-NCMIMUX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VERILINK-ENTERPRISE-NCMIMUX-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:33:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, TimeTicks, NotificationType, Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, MibIdentifier, Counter64, Gauge32, iso, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "TimeTicks", "NotificationType", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "MibIdentifier", "Counter64", "Gauge32", "iso", "Integer32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ncm_imux, = mibBuilder.importSymbols("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncm-imux")
ncmimuxConfigTable = MibTable((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7000), )
if mibBuilder.loadTexts: ncmimuxConfigTable.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxConfigTable.setDescription('The IMUX Configuration table.')
ncmimuxConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7000, 1), ).setIndexNames((0, "VERILINK-ENTERPRISE-NCMIMUX-MIB", "ncmimuxNIDConfigIndex"), (0, "VERILINK-ENTERPRISE-NCMIMUX-MIB", "ncmimuxLineIndex"))
if mibBuilder.loadTexts: ncmimuxConfigEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxConfigEntry.setDescription('An entry in the ncm IMUX Configuration table.')
ncmimuxNIDConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7000, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmimuxNIDConfigIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxNIDConfigIndex.setDescription('This variable indicates the node id value of the node.')
ncmimuxLineIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7000, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmimuxLineIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxLineIndex.setDescription('This object is the identifier of a Inter- face on a managed device. If there is an ifEn- try that is directly associated with this it should have the same value as ifIndex. Otherwise, the value exceeds ifNumber, and is a unique identifier following this rule: inside interfaces (e.g., equipment side) with even numbers and outside interfaces (e.g., network side) with odd numbers.')
ncmimuxEndId = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7000, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("near-End", 1), ("far-End", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmimuxEndId.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxEndId.setDescription('This value for this object indicates which end of the equipment it is accessing.')
ncmimuxIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7000, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmimuxIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxIfIndex.setDescription('This value for this object is equal to the value of ifIndex from the Interfaces table of MIB II (RFC 1213).')
ncmimuxBkplaneBusSelect = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7000, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))).clone(namedValues=NamedValues(("bus-AAAAAAAA", 1), ("bus-AABBAABB", 2), ("bus-AACCAACC", 3), ("bus-AADDAADD", 4), ("bus-BBAABBAA", 5), ("bus-BBBBBBBB", 6), ("bus-BBCCBBCC", 7), ("bus-BBDDBBDD", 8), ("bus-CCAACCAA", 9), ("bus-CCBBCCBB", 10), ("bus-CCCCCCCC", 11), ("bus-CCDDCCDD", 12), ("bus-DDAADDAA", 13), ("bus-DDBBDDBB", 14), ("bus-DDCCDDCC", 15), ("bus-DDDDDDDD", 16), ("bus-XXEEXXEE", 17), ("bus-EEXXEEXX", 18)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmimuxBkplaneBusSelect.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxBkplaneBusSelect.setDescription("This object only has signifiance for IMUX 2164. This variable specifies which IMUX line(s) is used, and which backplane bus is assigned to which line(s). The pattern of the the word is compsed as :- line# 8 7 6 5 4 3 2 1 bus # bus-B B D D B B D D(8) means lines 1,2,5,6 use bus - B lines 3,4,7,8 use bus - D The 'X' means no bus selection has been made.")
ncmimuxCarrierLineRate = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7000, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("t1-rate", 1), ("e1-rate", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmimuxCarrierLineRate.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxCarrierLineRate.setDescription('This variable specifies whether the carrier line rate is T1 or carrier line is E1.')
ncmimuxCarrierLinesEqp = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7000, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmimuxCarrierLinesEqp.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxCarrierLinesEqp.setDescription('This variable indicates the inverse multiplexer carrier lines equipped. One bit per line. Here each bit in this byte represents one of the eight carrier lines that may be used by the Imux. Bit zero represents carrierline number one, and bit seven represents carrier line number eight. For each bit that is set to one, the corresponding carrier line will be configured for use by the ncmimux. For each bit that is set to zero, the corresponding carrier line will be excluded from the ncmimux configuration i.e., 1 = 0000 0001(bin). The range for this variable is from (in decimals 0 to 256).')
ncmimuxChanneling = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7000, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mode-64k", 1), ("mode-56k", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmimuxChanneling.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxChanneling.setDescription('This variable indicates the inverse multiplexer mode for T1 which by default is set to 64 Kbps and when the field is set to (1) the 56 kbps mode is selected.')
ncmimuxDTEClkTransmit = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7000, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("inverted", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmimuxDTEClkTransmit.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxDTEClkTransmit.setDescription("This field request to determine the DTE data port clock phase is normal or inverted. 'Normal' refers to inverse multiplexer DTE clock phase is normal. 'Inverted' refers to inverse multiplexer DTE clock phase is inverted.")
ncmimuxDTEClkRecv = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7000, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("inverted", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmimuxDTEClkRecv.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxDTEClkRecv.setDescription("This field request to determine the DTE data port clock phase is normal or inverted. 'Normal' refers to inverse multiplexer DTE clock phase is normal. 'Inverted' refers to inverse multiplexer DTE clock phase is inverted.")
ncmimuxDTEClkRefern = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7000, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("inverted", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmimuxDTEClkRefern.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxDTEClkRefern.setDescription("This field request to determine the DTE data port clock phase is normal or inverted. 'Normal' refers to inverse multiplexer DTE clock phase is normal. 'Inverted' refers to inverse multiplexer DTE clock phase is inverted.")
ncmimuxDTEMode = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7000, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("automatic", 1), ("manual", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmimuxDTEMode.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxDTEMode.setDescription('This variable represents the DTE mode of the ncmimux')
ncmimuxDSR = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7000, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmimuxDSR.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxDSR.setDescription('This variable represents Data Set Ready for the ncmimux which could be set for all interfaces.')
ncmimuxTM = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7000, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmimuxTM.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxTM.setDescription('This variable represents Test Mode for the ncmimux which could be set for all interfaces.')
ncmimuxCTS = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7000, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmimuxCTS.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxCTS.setDescription('This variable represents Clear To Send for the ncmimux which could be set for only V.35, EI530 and RS449 interfaces.')
ncmimuxDCD = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7000, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmimuxDCD.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxDCD.setDescription('This variable represents Data Carrier Detect for the ncmimux which could be set for only V.35, EI530 and RS449 interfaces.')
ncmimuxRI = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7000, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmimuxRI.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxRI.setDescription('This variable represents Ring Indicator for the ncmimux which could be set for only V.35 interfaces.')
ncmimuxSnapType = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7000, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unknown", 1), ("hssi", 2), ("v35", 3), ("eia530a", 4), ("eia530", 5), ("rs449", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmimuxSnapType.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxSnapType.setDescription('This variable represents the snap type for the ncmimux')
ncmimuxQuadSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7000, 1, 19), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmimuxQuadSlot.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxQuadSlot.setDescription('This variable represents the DTE control mode of the ncmimux')
ncmimuxStatusTable = MibTable((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7001), )
if mibBuilder.loadTexts: ncmimuxStatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxStatusTable.setDescription('The IMUX Status table.')
ncmimuxStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7001, 1), ).setIndexNames((0, "VERILINK-ENTERPRISE-NCMIMUX-MIB", "ncmimuxNIDStatusIndex"), (0, "VERILINK-ENTERPRISE-NCMIMUX-MIB", "ncmimuxStatusIndex"))
if mibBuilder.loadTexts: ncmimuxStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxStatusEntry.setDescription('An entry in the IMUX Status table.')
ncmimuxNIDStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7001, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmimuxNIDStatusIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxNIDStatusIndex.setDescription('This variable indicates the node id value of the node.')
ncmimuxStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7001, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmimuxStatusIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxStatusIndex.setDescription('This object is the identifier of a Inter- face on a managed device. If there is an ifEn- try that is directly associated with this it should have the same value as ifIndex. Otherwise, the value exceeds ifNumber, and is a unique identifier following this rule: inside interfaces (e.g., equipment side) with even numbers and outside interfaces (e.g., network side) with odd numbers.')
ncmimuxStatEndId = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7001, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("near-End", 1), ("far-End", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmimuxStatEndId.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxStatEndId.setDescription('This value for this object indicates which end of the equipment it is accessing.')
ncmimuxLinesEqp = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7001, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmimuxLinesEqp.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxLinesEqp.setDescription('This variable indicates the inverse multiplexer carrier lines equipped. One bit per line. Here each bit in this byte represents one of the eight carrier lines that may be used by the Imux. Bit zero represents carrierline number one, and bit seven represents carrier line number eight. For each bit that is set to one, the corresponding carrier line will be configured for use by the ncmimux. For each bit that is set to zero, the corresponding carrier line will be excluded from the ncmimux configuration i.e., 1 = 0000 0001(bin). The range for this variable is from (in decimals 0 to 256).')
ncmimuxLinesStat = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7001, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmimuxLinesStat.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxLinesStat.setDescription(' This represents the lines active equivalent in tabs message, indicating when a carrier line has been allocated for use by the ncmimux. (Loop integrity must be established before the line can be put into active service).Options supported active, inactive or none.')
ncmimuxFrameStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7001, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmimuxFrameStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxFrameStatus.setDescription(' This variable indicates the ncmimux frame structure is transmitted over each carrier line that has been allocated for use by the ncmimux. This field indicates that this frame structure has been recongnized and validated in the signal received on the carrier line or invalidated.')
ncmimuxCTSStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7001, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmimuxCTSStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxCTSStatus.setDescription(" This variable indicates Clear To Send status that is encoded into the ncmimux frame structure on each carrier line to indicate that the integrity of the incoming signal has been validated. 'validCTS' refers to Clear To Send indication has been detected in the receive signal on the corresponding carrier line. 'invalidCTS' refers to Clear To send has not been detected. 'none' represents to not supported")
ncmimuxCRCStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7001, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmimuxCRCStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxCRCStatus.setDescription(' This variable represents the crc error of the incoming frame structure corresponding to a Carrier Line.')
ncmimuxFarEndCRCStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7001, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmimuxFarEndCRCStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxFarEndCRCStatus.setDescription(' This variable represents the crc error of the incoming frame structure received at the far end of the corresponding Carrier Lines.')
ncmimuxDataValidStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7001, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmimuxDataValidStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxDataValidStatus.setDescription(' This variable represents the data valid of the Carrier Lines.')
ncmimuxNetworkAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7001, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("off", 1), ("red", 2), ("green", 3), ("yellow", 4), ("flashing-Red", 5), ("flashing-Green", 6), ("flashing-Yellow", 7), ("flashing-Red-Green", 8), ("flashing-Green-Yellow", 9), ("flashing-Yellow-Red", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmimuxNetworkAlarm.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxNetworkAlarm.setDescription('The value for this object indicates the front panel LED alarm status for the network interface.')
ncmimuxAlarmLED = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7001, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("off", 1), ("red", 2), ("green", 3), ("yellow", 4), ("flashing-Red", 5), ("flashing-Green", 6), ("flashing-Yellow", 7), ("flashing-Red-Green", 8), ("flashing-Green-Yellow", 9), ("flashing-Yellow-Red", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmimuxAlarmLED.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxAlarmLED.setDescription('The value for this object indicates the front panel LED alarm status for the IMux.')
ncmimuxEventMessages = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7001, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmimuxEventMessages.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxEventMessages.setDescription('The value for this object indicates the number of event messages in the event queue. The event queue is a list of state changes which are time-stamped and recorded. ')
ncmimuxControlTable = MibTable((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7002), )
if mibBuilder.loadTexts: ncmimuxControlTable.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxControlTable.setDescription('The IMUX Control table.')
ncmimuxControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7002, 1), ).setIndexNames((0, "VERILINK-ENTERPRISE-NCMIMUX-MIB", "ncmimuxNIDControlIndex"), (0, "VERILINK-ENTERPRISE-NCMIMUX-MIB", "ncmimuxControlIndex"))
if mibBuilder.loadTexts: ncmimuxControlEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxControlEntry.setDescription('An entry in the IMUX Control table.')
ncmimuxNIDControlIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7002, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmimuxNIDControlIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxNIDControlIndex.setDescription('This variable indicates the node id value of the node.')
ncmimuxControlIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7002, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmimuxControlIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxControlIndex.setDescription('This object is the identifier of a Inter- face on a managed device. If there is an ifEn- try that is directly associated with this it should have the same value as ifIndex. Otherwise, the value exceeds ifNumber, and is a unique identifier following this rule: inside interfaces (e.g., equipment side) with even numbers and outside interfaces (e.g., network side) with odd numbers.')
ncmimuxCntEndId = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7002, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("near-End", 1), ("far-End", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmimuxCntEndId.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxCntEndId.setDescription('This value for this object indicates which end of the equipment it is accessing.')
ncmimuxLoopback = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7002, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("no-ELB-AND-PLB", 1), ("actv-ELB", 2), ("actv-PLB", 3), ("actv-ELB-AND-PLB", 4), ("deactv-ELB", 5), ("deactv-PLB", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmimuxLoopback.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxLoopback.setDescription(' This variable represents the Loopback status of Imux, ELB or PLB i.e., Equipment Loop back or Payload loop back.')
ncmimuxAISPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7002, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disable", 1), ("all-Ones", 2), ("all-Zeros", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmimuxAISPattern.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxAISPattern.setDescription(' This refers to the AIS test pattern initiated')
ncmimuxTestPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7002, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disable", 1), ("pat-127", 2), ("inv-Pat-127", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmimuxTestPattern.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxTestPattern.setDescription(' This refers to the test pattern initiated')
ncmimuxDTEStatTable = MibTable((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7003), )
if mibBuilder.loadTexts: ncmimuxDTEStatTable.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxDTEStatTable.setDescription('The IMUX DTE Status table.')
ncmimuxDTEStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7003, 1), ).setIndexNames((0, "VERILINK-ENTERPRISE-NCMIMUX-MIB", "ncmimuxNIDDTEStatIndex"), (0, "VERILINK-ENTERPRISE-NCMIMUX-MIB", "ncmimuxDTEStatIndex"))
if mibBuilder.loadTexts: ncmimuxDTEStatEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxDTEStatEntry.setDescription('An entry in the IMUX DTEStatus table.')
ncmimuxNIDDTEStatIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7003, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmimuxNIDDTEStatIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxNIDDTEStatIndex.setDescription('This variable indicates the node id value of the node.')
ncmimuxDTEStatIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7003, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmimuxDTEStatIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxDTEStatIndex.setDescription('This object is the identifier of a Inter- face on a managed device. If there is an ifEn- try that is directly associated with this it should have the same value as ifIndex. Otherwise, the value exceeds ifNumber, and is a unique identifier following this rule: inside interfaces (e.g., equipment side) with even numbers and outside interfaces (e.g., network side) with odd numbers.')
ncmimuxDTEStatReg = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7003, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("hSSI-DTR", 1), ("hSSI-Loopback-A", 2), ("hSSI-Loopback-B", 3), ("v35-RTS", 4), ("v54-RL", 5), ("v54-LL", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmimuxDTEStatReg.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxDTEStatReg.setDescription('This object reports the contents of the DTE Status Register as read from the IMUX hardware.')
ncmimuxDTEStatLPBK = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7003, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("v54-LoopUp", 1), ("v54-Ptrn-Loop-Errors", 2), ("v54-LoopDown", 3), ("v35-LoopDown-Errors", 4), ("pRBS", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmimuxDTEStatLPBK.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxDTEStatLPBK.setDescription('This object reports the DTE Pattern and Loopback Code Register Status. (0) indicates that a Loop Up Code was detected. (1) indicates that Data Pattern or Loop Up Code errors were detected. (2) indicates a Loop Down Code was detected. (3) indicates Loop Down Code Errors were detected. (4) indicates PRBS 2 x 10^25 Aggregate Data Bandwidth. ')
ncmimuxDTEStatAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3030, 7003, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("off", 1), ("red", 2), ("green", 3), ("yellow", 4), ("flashing-Red", 5), ("flashing-Green", 6), ("flashing-Yellow", 7), ("flashing-Red-Green", 8), ("flashing-Green-Yellow", 9), ("flashing-Yellow-Red", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmimuxDTEStatAlarm.setStatus('mandatory')
if mibBuilder.loadTexts: ncmimuxDTEStatAlarm.setDescription('This object reports the front panel alarm LED status for the DTE interface. ')
mibBuilder.exportSymbols("VERILINK-ENTERPRISE-NCMIMUX-MIB", ncmimuxStatusIndex=ncmimuxStatusIndex, ncmimuxNIDStatusIndex=ncmimuxNIDStatusIndex, ncmimuxFrameStatus=ncmimuxFrameStatus, ncmimuxSnapType=ncmimuxSnapType, ncmimuxQuadSlot=ncmimuxQuadSlot, ncmimuxDataValidStatus=ncmimuxDataValidStatus, ncmimuxTestPattern=ncmimuxTestPattern, ncmimuxDTEStatTable=ncmimuxDTEStatTable, ncmimuxDTEMode=ncmimuxDTEMode, ncmimuxControlEntry=ncmimuxControlEntry, ncmimuxAISPattern=ncmimuxAISPattern, ncmimuxStatEndId=ncmimuxStatEndId, ncmimuxDTEStatEntry=ncmimuxDTEStatEntry, ncmimuxLinesEqp=ncmimuxLinesEqp, ncmimuxDTEStatLPBK=ncmimuxDTEStatLPBK, ncmimuxCarrierLineRate=ncmimuxCarrierLineRate, ncmimuxStatusTable=ncmimuxStatusTable, ncmimuxDTEClkRefern=ncmimuxDTEClkRefern, ncmimuxBkplaneBusSelect=ncmimuxBkplaneBusSelect, ncmimuxDCD=ncmimuxDCD, ncmimuxControlIndex=ncmimuxControlIndex, ncmimuxDTEClkRecv=ncmimuxDTEClkRecv, ncmimuxConfigTable=ncmimuxConfigTable, ncmimuxDTEClkTransmit=ncmimuxDTEClkTransmit, ncmimuxCTS=ncmimuxCTS, ncmimuxIfIndex=ncmimuxIfIndex, ncmimuxNetworkAlarm=ncmimuxNetworkAlarm, ncmimuxFarEndCRCStatus=ncmimuxFarEndCRCStatus, ncmimuxLoopback=ncmimuxLoopback, ncmimuxEventMessages=ncmimuxEventMessages, ncmimuxDSR=ncmimuxDSR, ncmimuxNIDControlIndex=ncmimuxNIDControlIndex, ncmimuxDTEStatReg=ncmimuxDTEStatReg, ncmimuxTM=ncmimuxTM, ncmimuxEndId=ncmimuxEndId, ncmimuxConfigEntry=ncmimuxConfigEntry, ncmimuxLinesStat=ncmimuxLinesStat, ncmimuxCarrierLinesEqp=ncmimuxCarrierLinesEqp, ncmimuxCntEndId=ncmimuxCntEndId, ncmimuxCRCStatus=ncmimuxCRCStatus, ncmimuxStatusEntry=ncmimuxStatusEntry, ncmimuxNIDConfigIndex=ncmimuxNIDConfigIndex, ncmimuxAlarmLED=ncmimuxAlarmLED, ncmimuxRI=ncmimuxRI, ncmimuxChanneling=ncmimuxChanneling, ncmimuxCTSStatus=ncmimuxCTSStatus, ncmimuxDTEStatIndex=ncmimuxDTEStatIndex, ncmimuxControlTable=ncmimuxControlTable, ncmimuxNIDDTEStatIndex=ncmimuxNIDDTEStatIndex, ncmimuxLineIndex=ncmimuxLineIndex, ncmimuxDTEStatAlarm=ncmimuxDTEStatAlarm)