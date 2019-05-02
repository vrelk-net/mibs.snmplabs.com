#
# PySNMP MIB module TSMEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TSMEXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:27:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, IpAddress, TimeTicks, ObjectIdentity, Integer32, NotificationType, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, Bits, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "IpAddress", "TimeTicks", "ObjectIdentity", "Integer32", "NotificationType", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "Bits", "MibIdentifier", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
xylanTsmArch, = mibBuilder.importSymbols("XYLAN-BASE-MIB", "xylanTsmArch")
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

tsmExtensions = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 19, 1))
tsmAdmin = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 1))
tsmOper = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2))
tsmAdminPortTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 1, 1), )
if mibBuilder.loadTexts: tsmAdminPortTable.setStatus('mandatory')
if mibBuilder.loadTexts: tsmAdminPortTable.setDescription('TSM Port Configuration Table.')
tsmAdminPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 1, 1, 1), ).setIndexNames((0, "TSMEXT-MIB", "tsmAdminPortSlotNumber"), (0, "TSMEXT-MIB", "tsmAdminPortNumber"))
if mibBuilder.loadTexts: tsmAdminPortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: tsmAdminPortEntry.setDescription('A TSM Port Configuration Entry.')
tsmAdminPortSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsmAdminPortSlotNumber.setStatus('mandatory')
if mibBuilder.loadTexts: tsmAdminPortSlotNumber.setDescription('The slot number of the Token Ring Switching Module.')
tsmAdminPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsmAdminPortNumber.setStatus('mandatory')
if mibBuilder.loadTexts: tsmAdminPortNumber.setDescription('The port number of the Token Ring Switching Module.')
tsmAdminPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsmAdminPortState.setStatus('mandatory')
if mibBuilder.loadTexts: tsmAdminPortState.setDescription('The configured state of the port. 1 = enable. 2 = disable.')
tsmAdminPortActiveMon = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsmAdminPortActiveMon.setStatus('mandatory')
if mibBuilder.loadTexts: tsmAdminPortActiveMon.setDescription('The configured active monitor participation of the port. 1 = yes. Participate in the active monitor selection process. 2 = no. Do NOT participate in the active monitor selection process.')
tsmAdminPortAcBitSet = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("nonLocal", 1), ("repeat", 2), ("always", 3), ("never", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsmAdminPortAcBitSet.setStatus('mandatory')
if mibBuilder.loadTexts: tsmAdminPortAcBitSet.setDescription('The configured control mode for handling the ARI/FCI Bits of the port. 1 = nonLocal. Set ARI/FCI bits on all non-local LLC frames repeated by the port. For local frames repeat the ARI/FCI bits just as they are received. 2 = repeat. Repeat ARI/FCI bit on all LLC frames just as they are received. 3 = always. Set ARI/FCI bits on all LLC frames repeated by the port. 4 = never. Do not set ARI/FCI bits on any LLC frames repeated by the port.')
tsmAdminPortConfigType = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("auto", 1), ("fixed", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsmAdminPortConfigType.setStatus('mandatory')
if mibBuilder.loadTexts: tsmAdminPortConfigType.setDescription("The configured config-type of the port. 1 = auto. Automatically set the port's ring speed, mode, duplex and switching mode parameters. 2 = fixed. Use customer defined values for the port's ring speed, mode, duplex and switching mode parameters.")
tsmAdminPortRingSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("fourMegabit", 2), ("sixteenMegabit", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsmAdminPortRingSpeed.setStatus('mandatory')
if mibBuilder.loadTexts: tsmAdminPortRingSpeed.setDescription("The configured ring speed of the port. 1 = auto. Automatically set the port's ring speed. 2 = fourMegabit. Always set the port's ring speed at four megabits. 3 = sixteenMegabit. Always set the port's ring speed at sixteen megabits. This object may ONLY be set if the value of port's tsmAdminPortConfigType is fixed(1).")
tsmAdminPortPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("portMode", 2), ("adapterMode", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsmAdminPortPortMode.setStatus('mandatory')
if mibBuilder.loadTexts: tsmAdminPortPortMode.setDescription("The configured port mode of the port. 1 = auto. Automatically sense the port mode. This value is set by the switch when the tsmAdminPortConfigMode is set to auto. This object CANNOT be changed to auto by an SNMP SET. 2 = portMode. Only a dedicated connection to a station is supported. 3 = adapterMode. The port operates like a station. The connection can be either dedicated or shared. This object may ONLY be set if the value of port's tsmAdminPortConfigType is fixed(1). auto(1) is NOT a valid SET value.")
tsmAdminPortDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("halfDuplex", 2), ("fullDuplex", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsmAdminPortDuplex.setStatus('mandatory')
if mibBuilder.loadTexts: tsmAdminPortDuplex.setDescription("The configured duplex mode of the port. 1 = auto. Automatically set the port's duplex mode. 2 = halfDuplex. Alway run the port in half duplex mode. 3 = fullDuplex. Alway run the port in full duplex mode. This object may ONLY be set if the value of port's tsmAdminPortConfigType is fixed(1).")
tsmAdminPortSwMode = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("cutThrough", 1), ("storeAndForward", 2), ("adaptive", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsmAdminPortSwMode.setStatus('mandatory')
if mibBuilder.loadTexts: tsmAdminPortSwMode.setDescription('The configured duplex mode of the port. 1 = cutThrough. A scheme that allows frame transmission to begin at the output port prior to end-of-frame reception at the input port. 2 = storeAndForward. The entire packet is received and stored before switching begins. 3 = adaptive. Alternate between cut-through and store-and-forward base on the specified error threshold.')
tsmAdminPortReset = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ready", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsmAdminPortReset.setStatus('mandatory')
if mibBuilder.loadTexts: tsmAdminPortReset.setDescription('This object is used to reset the port. 1 = ready. The port is ready to be reset. 2 = reset. Reset the port.')
tsmAdminSwModeTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 1, 2), )
if mibBuilder.loadTexts: tsmAdminSwModeTable.setStatus('mandatory')
if mibBuilder.loadTexts: tsmAdminSwModeTable.setDescription('TSM Switching Mode Configuration Table.')
tsmAdminSwModeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 1, 2, 1), ).setIndexNames((0, "TSMEXT-MIB", "tsmAdminSwModeSlotNumber"))
if mibBuilder.loadTexts: tsmAdminSwModeEntry.setStatus('mandatory')
if mibBuilder.loadTexts: tsmAdminSwModeEntry.setDescription('A TSM Switching Mode Configuration Entry.')
tsmAdminSwModeSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsmAdminSwModeSlotNumber.setStatus('mandatory')
if mibBuilder.loadTexts: tsmAdminSwModeSlotNumber.setDescription('The slot number of the Token Ring Switching Module.')
tsmAdminSwModeHiErrThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsmAdminSwModeHiErrThresh.setStatus('mandatory')
if mibBuilder.loadTexts: tsmAdminSwModeHiErrThresh.setDescription("The high error threshold in percent for all ports associated with the TSM which are configured to run in adaptive mode. If the percentage of errors in a sampling period meets or exceeds this value, the port's switching mode will change from cut-through to store-and-forward mode.")
tsmAdminSwModeLoErrThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsmAdminSwModeLoErrThresh.setStatus('mandatory')
if mibBuilder.loadTexts: tsmAdminSwModeLoErrThresh.setDescription("The low error threshold in percent for all ports associated with the TSM which are configured to run in adaptive mode. If the percentage of errors in a sampling period falls below this value, the port's switching mode will change from store-and-forward to cut-through mode.")
tsmAdminSwModeTrendThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsmAdminSwModeTrendThresh.setStatus('mandatory')
if mibBuilder.loadTexts: tsmAdminSwModeTrendThresh.setDescription("The error rate trend threshold in percent for all ports associated with the TSM which are configured to run in adaptive mode. When the percentage of errors is between the high and low error thresholds AND the port is currently running in cut-through mode, the error rate trend which is the difference in errors between two sampling periods is compared to the error rate trend threshold. If the error rate trend is greater than this value, the port's switching mode will change from cut-through mode to store-and-forward. The error rate trend threshold should be no greater than the difference between the high and low threshold values.")
tsmAdminSwModeSamplePeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 120))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsmAdminSwModeSamplePeriod.setStatus('mandatory')
if mibBuilder.loadTexts: tsmAdminSwModeSamplePeriod.setDescription('The sampling period in seconds for all ports associated with the TSM which are configured to run in adaptive mode.')
tsmAdminSwModeReset = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ready", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tsmAdminSwModeReset.setStatus('mandatory')
if mibBuilder.loadTexts: tsmAdminSwModeReset.setDescription('This object is used to reset the TSM. 1 = ready. The TSM is ready to be reset. 2 = reset. Reset the TSM.')
tsmOperPortTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 1), )
if mibBuilder.loadTexts: tsmOperPortTable.setStatus('mandatory')
if mibBuilder.loadTexts: tsmOperPortTable.setDescription('TSM Port Operational Table.')
tsmOperPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 1, 1), ).setIndexNames((0, "TSMEXT-MIB", "tsmOperPortSlotNumber"), (0, "TSMEXT-MIB", "tsmOperPortNumber"))
if mibBuilder.loadTexts: tsmOperPortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: tsmOperPortEntry.setDescription('A TSM Port Operational Entry.')
tsmOperPortSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsmOperPortSlotNumber.setStatus('mandatory')
if mibBuilder.loadTexts: tsmOperPortSlotNumber.setDescription('The slot number of the Token Ring Switching Module.')
tsmOperPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsmOperPortNumber.setStatus('mandatory')
if mibBuilder.loadTexts: tsmOperPortNumber.setDescription('The port number of the Token Ring Switching Module.')
tsmOperPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsmOperPortState.setStatus('mandatory')
if mibBuilder.loadTexts: tsmOperPortState.setDescription('The operational state of the port. 1 = enable. 2 = disable.')
tsmOperPortActiveMon = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsmOperPortActiveMon.setStatus('mandatory')
if mibBuilder.loadTexts: tsmOperPortActiveMon.setDescription('The operational active monitor participation of the port. 1 = yes. Participate in the active monitor selection process. 2 = no. Do NOT participate in the active monitor selection process.')
tsmOperPortAcBitSet = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("nonLocal", 1), ("repeat", 2), ("always", 3), ("never", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsmOperPortAcBitSet.setStatus('mandatory')
if mibBuilder.loadTexts: tsmOperPortAcBitSet.setDescription('The operational control mode for handling the ARI/FCI Bits of the port. 1 = nonLocal. Set ARI/FCI bits on all non-local LLC frames repeated by the port. For local frames repeat the ARI/FCI bits just as they are received. 2 = repeat. Repeat ARI/FCI bit on all LLC frames just as they are received. 3 = always. Set ARI/FCI bits on all LLC frames repeated by the port. 4 = never. Do not set ARI/FCI bits on any LLC frames repeated by the port.')
tsmOperPortConfigType = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("auto", 1), ("fixed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsmOperPortConfigType.setStatus('mandatory')
if mibBuilder.loadTexts: tsmOperPortConfigType.setDescription("The operational config-type of the port. 1 = auto. Automatically set the port's ring speed, mode and duplex parameters. 2 = fixed. Use customer defined values for the port's ring speed, mode and duplex parameters.")
tsmOperPortRingSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("fourMegabit", 2), ("sixteenMegabit", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsmOperPortRingSpeed.setStatus('mandatory')
if mibBuilder.loadTexts: tsmOperPortRingSpeed.setDescription('The operational ring speed of the port. 1 = auto. The port has not yet automatically set the ring speed. 2 = fourMegabit. 3 = sixteenMegabit.')
tsmOperPortPortMode = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("portMode", 2), ("adapterMode", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsmOperPortPortMode.setStatus('mandatory')
if mibBuilder.loadTexts: tsmOperPortPortMode.setDescription('The operational port mode of the port. 1 = auto. Automatically sense the port mode. 2 = portMode. Only a dedicated connection to a station is supported. 3 = adapterMode. The port operates like a station. The connection can be either dedicated or shared.')
tsmOperPortDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("halfDuplex", 2), ("fullDuplex", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsmOperPortDuplex.setStatus('mandatory')
if mibBuilder.loadTexts: tsmOperPortDuplex.setDescription("The configured duplex mode of the port. 1 = auto. The port has not yet automatically set the port's duplex mode. 2 = halfDuplex. 3 = fullDuplex.")
tsmOperPortSwMode = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("cutThrough", 1), ("storeAndForward", 2), ("adaptive", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsmOperPortSwMode.setStatus('mandatory')
if mibBuilder.loadTexts: tsmOperPortSwMode.setDescription('The configured switch mode of the port. 1 = cutThrough. A scheme that allows frame transmission to begin at the output port prior to end-of-frame reception at the input port. 2 = storeAndForward. The entire packet is received and stored before switching begins. 3 = adaptive. Alternate between cut-through and store-and-forward base on the specified error threshold.')
tsmOperPortAdaptSwMode = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("cutThrough", 1), ("storeAndForward", 2), ("notAdaptive", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsmOperPortAdaptSwMode.setStatus('mandatory')
if mibBuilder.loadTexts: tsmOperPortAdaptSwMode.setDescription('The operational adaptive switch mode of the port. 1 = cutThrough. A scheme that allows frame transmission to begin at the output port prior to end-of-frame reception at the input port. 2 = storeAndForward. The entire packet is received and stored before switching begins. 3 = notAdaptive. The port is not running in adaptive mode.')
tsmOperPortAdaptErrRate = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsmOperPortAdaptErrRate.setStatus('mandatory')
if mibBuilder.loadTexts: tsmOperPortAdaptErrRate.setDescription('The operational adaptive error rate in percent of the port. This value is the percent of errors in the last sampling period.')
tsmOperPortAdaptTrend = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsmOperPortAdaptTrend.setStatus('mandatory')
if mibBuilder.loadTexts: tsmOperPortAdaptTrend.setDescription('The operational adaptive error rate trend in percent of the port. This value is the difference in errors between the last two sampling periods.')
tsmOperPortOpenState = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("opened", 1), ("closed", 2), ("opening", 3), ("closing", 4), ("openFailure", 5), ("ringFailure", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsmOperPortOpenState.setStatus('mandatory')
if mibBuilder.loadTexts: tsmOperPortOpenState.setDescription('The operational open status of the port. 1 = opened 2 = closed 3 = opening 4 = closing 5 = openFailure 6 = ringFailure')
tsmOperPortUpStream = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 1, 1, 15), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsmOperPortUpStream.setStatus('mandatory')
if mibBuilder.loadTexts: tsmOperPortUpStream.setDescription(' The operational MAC Address of the up stream neighbour in the ring. ')
tsmOperSwModeTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 2), )
if mibBuilder.loadTexts: tsmOperSwModeTable.setStatus('mandatory')
if mibBuilder.loadTexts: tsmOperSwModeTable.setDescription('TSM Switch Mode Operational Table.')
tsmOperSwModeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 2, 1), ).setIndexNames((0, "TSMEXT-MIB", "tsmOperSwModeSlotNumber"))
if mibBuilder.loadTexts: tsmOperSwModeEntry.setStatus('mandatory')
if mibBuilder.loadTexts: tsmOperSwModeEntry.setDescription('A TSM Port Operational Entry.')
tsmOperSwModeSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsmOperSwModeSlotNumber.setStatus('mandatory')
if mibBuilder.loadTexts: tsmOperSwModeSlotNumber.setDescription('The slot number of the Token Ring Switching Module.')
tsmOperSwModeHiErrThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsmOperSwModeHiErrThresh.setStatus('mandatory')
if mibBuilder.loadTexts: tsmOperSwModeHiErrThresh.setDescription("The operational high error threshold for all ports associated with the TSM which are configured to run in adaptive mode. If the percentage of errors in a sampling period meets or exceeds this value, the port's switching mode will change from cut-through to store-and-forward mode.")
tsmOperSwModeLoErrThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsmOperSwModeLoErrThresh.setStatus('mandatory')
if mibBuilder.loadTexts: tsmOperSwModeLoErrThresh.setDescription("The operational low error threshold for all ports associated with the TSM which are configured to run in adaptive mode. If the percentage of errors in a sampling period falls below this value, the port's switching mode will change from store-and-forward to cut-through mode.")
tsmOperSwModeTrendThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsmOperSwModeTrendThresh.setStatus('mandatory')
if mibBuilder.loadTexts: tsmOperSwModeTrendThresh.setDescription("The operational error rate trend threshold in percent for all ports associated with the TSM which are configured to run in adaptive mode. When the percentage of errors is between the high and low error thresholds AND the port is currently running in cut-through mode, the error rate trend which is the difference in errors between two sampling periods is compared to the error rate trend threshold. If the error rate trend is greater than this value, the port's switching mode will change from cut-through mode to store-and-forward.")
tsmOperSwModeSamplePeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 19, 1, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 120))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tsmOperSwModeSamplePeriod.setStatus('mandatory')
if mibBuilder.loadTexts: tsmOperSwModeSamplePeriod.setDescription('The operational sampling period in seconds for all ports associated with the TSM which are configured to run in adaptive mode.')
mibBuilder.exportSymbols("TSMEXT-MIB", tsmOperPortConfigType=tsmOperPortConfigType, tsmOperSwModeTable=tsmOperSwModeTable, tsmOperSwModeTrendThresh=tsmOperSwModeTrendThresh, tsmAdminPortSlotNumber=tsmAdminPortSlotNumber, tsmOperPortTable=tsmOperPortTable, tsmAdminPortNumber=tsmAdminPortNumber, tsmAdminPortPortMode=tsmAdminPortPortMode, tsmAdminPortDuplex=tsmAdminPortDuplex, tsmAdminPortAcBitSet=tsmAdminPortAcBitSet, tsmOperPortActiveMon=tsmOperPortActiveMon, tsmOperPortAdaptErrRate=tsmOperPortAdaptErrRate, tsmOperSwModeLoErrThresh=tsmOperSwModeLoErrThresh, MacAddress=MacAddress, tsmAdminSwModeSlotNumber=tsmAdminSwModeSlotNumber, tsmOperSwModeEntry=tsmOperSwModeEntry, tsmAdminSwModeTrendThresh=tsmAdminSwModeTrendThresh, tsmAdminSwModeHiErrThresh=tsmAdminSwModeHiErrThresh, tsmOperPortDuplex=tsmOperPortDuplex, tsmAdminPortTable=tsmAdminPortTable, tsmAdminPortState=tsmAdminPortState, tsmOperPortUpStream=tsmOperPortUpStream, tsmOperPortPortMode=tsmOperPortPortMode, tsmAdminPortRingSpeed=tsmAdminPortRingSpeed, tsmOperSwModeHiErrThresh=tsmOperSwModeHiErrThresh, tsmAdminSwModeSamplePeriod=tsmAdminSwModeSamplePeriod, tsmAdminSwModeTable=tsmAdminSwModeTable, tsmOperSwModeSamplePeriod=tsmOperSwModeSamplePeriod, tsmOperPortState=tsmOperPortState, tsmOperPortSwMode=tsmOperPortSwMode, tsmOperPortOpenState=tsmOperPortOpenState, tsmAdminPortConfigType=tsmAdminPortConfigType, tsmAdmin=tsmAdmin, tsmAdminPortEntry=tsmAdminPortEntry, tsmAdminPortSwMode=tsmAdminPortSwMode, tsmOperPortAdaptTrend=tsmOperPortAdaptTrend, tsmOper=tsmOper, tsmExtensions=tsmExtensions, tsmOperPortAdaptSwMode=tsmOperPortAdaptSwMode, tsmAdminSwModeLoErrThresh=tsmAdminSwModeLoErrThresh, tsmOperPortSlotNumber=tsmOperPortSlotNumber, tsmOperPortNumber=tsmOperPortNumber, tsmOperPortRingSpeed=tsmOperPortRingSpeed, tsmOperSwModeSlotNumber=tsmOperSwModeSlotNumber, tsmAdminSwModeReset=tsmAdminSwModeReset, tsmAdminPortReset=tsmAdminPortReset, tsmOperPortEntry=tsmOperPortEntry, tsmAdminPortActiveMon=tsmAdminPortActiveMon, tsmOperPortAcBitSet=tsmOperPortAcBitSet, tsmAdminSwModeEntry=tsmAdminSwModeEntry)