#
# PySNMP MIB module A3Com-PortPath-r6-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-PORTPATH-R6-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:53:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Integer32, ModuleIdentity, Bits, enterprises, Unsigned32, Counter32, MibIdentifier, iso, Gauge32, TimeTicks, IpAddress, NotificationType, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Integer32", "ModuleIdentity", "Bits", "enterprises", "Unsigned32", "Counter32", "MibIdentifier", "iso", "Gauge32", "TimeTicks", "IpAddress", "NotificationType", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
a3Com = MibIdentifier((1, 3, 6, 1, 4, 1, 43))
brouterMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2))
a3ComPath = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2, 16))
a3ComPort = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2, 17))
a3ComPathDial = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2, 18))
a3ComPortDial = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2, 19))
class RowStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6))

a3ComPathNumber = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 16, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComPathNumber.setStatus('mandatory')
a3ComPathTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 16, 2), )
if mibBuilder.loadTexts: a3ComPathTable.setStatus('mandatory')
a3ComPathEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1), ).setIndexNames((0, "A3Com-PortPath-r6-MIB", "a3ComPathIndex"))
if mibBuilder.loadTexts: a3ComPathEntry.setStatus('mandatory')
a3ComPathIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComPathIndex.setStatus('mandatory')
a3ComPathName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPathName.setStatus('mandatory')
a3ComPathPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPathPort.setStatus('mandatory')
a3ComPathItcmOption = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("compatible", 1), ("incompatible", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPathItcmOption.setStatus('mandatory')
a3ComPathT1Mode = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPathT1Mode.setStatus('mandatory')
a3ComPathCryptoResync = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPathCryptoResync.setStatus('mandatory')
a3ComPathCRC = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(16, 32))).clone(namedValues=NamedValues(("crc16", 16), ("crc32", 32)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPathCRC.setStatus('mandatory')
a3ComPathAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPathAdminStatus.setStatus('mandatory')
a3ComPathOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("disabled", 3), ("notAvailable", 4), ("other", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComPathOperStatus.setStatus('mandatory')
a3ComPathBaud = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22))).clone(namedValues=NamedValues(("notApplicable", 1), ("baud1200", 2), ("baud2400", 3), ("baud4800", 4), ("baud9600", 5), ("baud19200", 6), ("baud38400", 7), ("baud56k", 8), ("baud64k", 9), ("baud128k", 10), ("baud256k", 11), ("baud448k", 12), ("baud1536k", 13), ("baud2048k", 14), ("baud3072k", 15), ("baud4000k", 16), ("baud4608k", 17), ("baud6144k", 18), ("baud7680k", 19), ("baud9216k", 20), ("baud16000k", 21), ("other", 22))).clone('baud64k')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPathBaud.setStatus('deprecated')
a3ComPathConn = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("notApplicable", 1), ("v35", 2), ("rs232", 3), ("rs449", 4), ("g703", 5), ("t3", 6), ("isdnBri", 7), ("isdnPri", 8), ("auto", 9), ("other", 10), ("x21", 11)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPathConn.setStatus('mandatory')
a3ComPathClock = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notApplicable", 1), ("internal", 2), ("external", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPathClock.setStatus('mandatory')
a3ComPathLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 13), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComPathLastChange.setStatus('mandatory')
a3ComPathSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComPathSlotIndex.setStatus('mandatory')
a3ComPathConnPos = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComPathConnPos.setStatus('mandatory')
a3ComPathInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComPathInOctets.setStatus('mandatory')
a3ComPathInUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComPathInUcastPkts.setStatus('mandatory')
a3ComPathInNUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComPathInNUcastPkts.setStatus('mandatory')
a3ComPathInDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComPathInDiscards.setStatus('mandatory')
a3ComPathInErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComPathInErrors.setStatus('mandatory')
a3ComPathInUnknownProtos = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComPathInUnknownProtos.setStatus('mandatory')
a3ComPathOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComPathOutOctets.setStatus('mandatory')
a3ComPathOutUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComPathOutUcastPkts.setStatus('mandatory')
a3ComPathOutNUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComPathOutNUcastPkts.setStatus('mandatory')
a3ComPathOutDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComPathOutDiscards.setStatus('mandatory')
a3ComPathOutErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComPathOutErrors.setStatus('mandatory')
a3ComPathBaudRate = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 27), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPathBaudRate.setStatus('mandatory')
a3ComPathDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 16, 2, 1, 28), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("full", 1), ("half", 2), ("auto", 3))).clone('auto')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPathDuplex.setStatus('mandatory')
a3ComPortNumber = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 17, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComPortNumber.setStatus('mandatory')
a3ComPortTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 17, 2), )
if mibBuilder.loadTexts: a3ComPortTable.setStatus('mandatory')
a3ComPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1), ).setIndexNames((0, "A3Com-PortPath-r6-MIB", "a3ComPortIndex"))
if mibBuilder.loadTexts: a3ComPortEntry.setStatus('mandatory')
a3ComPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComPortIndex.setStatus('mandatory')
a3ComPortOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("ethernet", 1), ("tokenRing", 2), ("fddi", 3), ("ppp", 4), ("plg", 5), ("x25", 6), ("frameRelay", 7), ("smds", 8), ("auto", 9), ("autoPpp", 10), ("autoFr", 11)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPortOwner.setStatus('mandatory')
a3ComPortBoundaryRoute = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notApplicable", 1), ("enabled", 2), ("disabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPortBoundaryRoute.setStatus('mandatory')
a3ComPortBoundaryEncap = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("notApplicable", 1), ("ethernet", 2), ("tokenring", 3), ("fddi", 4), ("none", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPortBoundaryEncap.setStatus('mandatory')
a3ComPortCosInterleave = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPortCosInterleave.setStatus('deprecated')
a3ComPortMacAddrFmtARP = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("canonical", 1), ("nonCanonical", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPortMacAddrFmtARP.setStatus('mandatory')
a3ComPortMacAddrFmtIPX = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("canonical", 1), ("nonCanonical", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPortMacAddrFmtIPX.setStatus('mandatory')
a3ComPortMacAddrFmtXNS = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("canonical", 1), ("nonCanonical", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPortMacAddrFmtXNS.setStatus('mandatory')
a3ComPortPath = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPortPath.setStatus('mandatory')
a3ComQueueInterleave1 = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComQueueInterleave1.setStatus('mandatory')
a3ComQueueInterleave2 = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComQueueInterleave2.setStatus('mandatory')
a3ComQueuePattern = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("ratio3to3to2", 1), ("ratio4to2to2", 2), ("ratio4to3to1", 3), ("ratio5to2to1", 4), ("ratio6to1to1", 5), ("other", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComQueuePattern.setStatus('mandatory')
a3ComPortAsOwnerTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComPortAsOwnerTimer.setStatus('mandatory')
a3ComSmartFilteringCtl = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("smartFilter", 1), ("noSmartFilter", 2))).clone('smartFilter')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComSmartFilteringCtl.setStatus('mandatory')
a3ComBrCentralMacCtl = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("centralMac", 1), ("noCentralMac", 2))).clone('noCentralMac')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComBrCentralMacCtl.setStatus('mandatory')
a3ComPortLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 18), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComPortLabel.setStatus('mandatory')
a3ComPortCircuitID = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 19), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPortCircuitID.setStatus('mandatory')
a3ComPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 20), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPortStatus.setStatus('mandatory')
a3ComPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 21), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPortName.setStatus('mandatory')
a3ComPortVirtual = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("virtual", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComPortVirtual.setStatus('mandatory')
a3ComQueueThrottle = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComQueueThrottle.setStatus('mandatory')
a3ComPortInCallerId = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 24), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPortInCallerId.setStatus('mandatory')
a3ComPortCompType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("history", 2), ("perPacket", 3))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPortCompType.setStatus('mandatory')
a3ComPortX25ProtID = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 26), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(221)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPortX25ProtID.setStatus('mandatory')
a3ComPortIbmTraffic = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 17, 2, 1, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ibmTraffic", 1), ("noibmTraffic", 2))).clone('noibmTraffic')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPortIbmTraffic.setStatus('mandatory')
a3ComDefaultPriority = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 17, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("high", 1), ("med", 2), ("low", 3), ("unknown", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComDefaultPriority.setStatus('mandatory')
a3ComPathDialNumber = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 18, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComPathDialNumber.setStatus('mandatory')
a3ComPathDialTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 18, 2), )
if mibBuilder.loadTexts: a3ComPathDialTable.setStatus('mandatory')
a3ComPathDialEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 18, 2, 1), ).setIndexNames((0, "A3Com-PortPath-r6-MIB", "a3ComPathDialIndex"))
if mibBuilder.loadTexts: a3ComPathDialEntry.setStatus('mandatory')
a3ComPathDialIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 18, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComPathDialIndex.setStatus('mandatory')
a3ComPathDialType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 18, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("primaryLeased", 1), ("primaryDial", 2), ("secondaryDial", 3), ("other", 4), ("primaryAuto", 5), ("secondaryAuto", 6), ("secondaryLeased", 7), ("primaryAutoLeased", 8), ("primaryAutoDial", 9), ("secondaryAutoLeased", 10), ("secondaryAutoDial", 11)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPathDialType.setStatus('mandatory')
a3ComPathDialCtl = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 18, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("answerOriginate", 1), ("answerNoOriginate", 2), ("noAnswerOriginate", 3), ("noAnswerNoOriginate", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPathDialCtl.setStatus('mandatory')
a3ComPathDialAction = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 18, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("dial", 1), ("hangUp", 2), ("other", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPathDialAction.setStatus('mandatory')
a3ComPathDialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 18, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPathDialNum.setStatus('mandatory')
a3ComPathDialDodIdleTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 18, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3600)).clone(180)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPathDialDodIdleTime.setStatus('deprecated')
a3ComPathDialMode = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 18, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("v25Dial", 1), ("dtrDial", 2), ("autoV25", 3), ("autoDTR", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPathDialMode.setStatus('mandatory')
a3ComPathDialDynCont = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 18, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("static", 1), ("dynamic", 2), ("other", 3))).clone('static')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPathDialDynCont.setStatus('mandatory')
a3ComPathDialLocalDialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 18, 2, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPathDialLocalDialNumber.setStatus('mandatory')
a3ComPathDialLocalSubAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 18, 2, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPathDialLocalSubAddress.setStatus('mandatory')
a3ComPathDialSPIDDN1 = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 18, 2, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 37))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPathDialSPIDDN1.setStatus('mandatory')
a3ComPathDialSPIDDN2 = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 18, 2, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 37))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPathDialSPIDDN2.setStatus('mandatory')
a3ComPathDialRateAdaption = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 18, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("rate64", 2), ("rate56", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPathDialRateAdaption.setStatus('mandatory')
a3ComPathDialSwitchType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 18, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("etsi", 1), ("ntt", 2), ("ni1", 3), ("att5ess", 4), ("dms100", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPathDialSwitchType.setStatus('mandatory')
a3ComPathDialExDevType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 18, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("bri", 1), ("modem", 2), ("sw56", 3), ("other", 4))).clone('modem')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPathDialExDevType.setStatus('mandatory')
a3ComPortDIALNumber = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 19, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComPortDIALNumber.setStatus('mandatory')
a3ComPortDialTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 19, 2), )
if mibBuilder.loadTexts: a3ComPortDialTable.setStatus('mandatory')
a3ComPortDialEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 19, 2, 1), ).setIndexNames((0, "A3Com-PortPath-r6-MIB", "a3ComPortDialIndex"))
if mibBuilder.loadTexts: a3ComPortDialEntry.setStatus('mandatory')
a3ComPortDialIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 19, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComPortDialIndex.setStatus('mandatory')
a3ComPortDialDisasterCtl = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 19, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disasterRecovery", 1), ("noDisasterRecovery", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPortDialDisasterCtl.setStatus('mandatory')
a3ComPortDialBandOnDmnd = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 19, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("bandwidthOnDemand", 1), ("noBandwidthOnDemand", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPortDialBandOnDmnd.setStatus('mandatory')
a3ComPortDialDebounceTimeUp = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 19, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600)).clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPortDialDebounceTimeUp.setStatus('mandatory')
a3ComPortDialDebounceTimeDown = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 19, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600)).clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPortDialDebounceTimeDown.setStatus('mandatory')
a3ComPortDialInitState = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 19, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noDialOut", 1), ("manualDial", 2), ("dialOnDemand", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPortDialInitState.setStatus('mandatory')
a3ComPortDialRcvrState = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 19, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noAnswer", 1), ("answer", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPortDialRcvrState.setStatus('mandatory')
a3ComPortDialAction = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 19, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("dial", 1), ("hangUp", 2), ("other", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPortDialAction.setStatus('mandatory')
a3ComPortDialDodIdleTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 19, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3600)).clone(180)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPortDialDodIdleTime.setStatus('mandatory')
a3ComPortDialIdleTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 19, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600)).clone(180)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPortDialIdleTime.setStatus('mandatory')
a3ComPortDialDodCallsMade = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 19, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComPortDialDodCallsMade.setStatus('mandatory')
a3ComPortDialDodCallsFail = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 19, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComPortDialDodCallsFail.setStatus('mandatory')
a3ComPortDialDodUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 19, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComPortDialDodUpTime.setStatus('mandatory')
a3ComPortDialDodPktsOut = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 19, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComPortDialDodPktsOut.setStatus('mandatory')
a3ComPortDialBODTHreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 19, 2, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPortDialBODTHreshold.setStatus('mandatory')
a3ComPortDialPoolPrefTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 19, 3), )
if mibBuilder.loadTexts: a3ComPortDialPoolPrefTable.setStatus('mandatory')
a3ComPortDialPoolPrefEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 19, 3, 1), ).setIndexNames((0, "A3Com-PortPath-r6-MIB", "a3ComPortDialPoolPrefPort"), (0, "A3Com-PortPath-r6-MIB", "a3ComPortDialPoolPrefPathPos"))
if mibBuilder.loadTexts: a3ComPortDialPoolPrefEntry.setStatus('mandatory')
a3ComPortDialPoolPrefPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 19, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComPortDialPoolPrefPort.setStatus('mandatory')
a3ComPortDialPoolPrefPathPos = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 19, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComPortDialPoolPrefPathPos.setStatus('mandatory')
a3ComPortDialPoolPrefPathNum = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 19, 3, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPortDialPoolPrefPathNum.setStatus('mandatory')
a3ComPortDialPoolPrefStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 19, 3, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPortDialPoolPrefStatus.setStatus('mandatory')
a3ComPortDialPhoneListTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 19, 4), )
if mibBuilder.loadTexts: a3ComPortDialPhoneListTable.setStatus('mandatory')
a3ComPortDialPhoneListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 19, 4, 1), ).setIndexNames((0, "A3Com-PortPath-r6-MIB", "a3ComPortDialPhoneListPort"), (0, "A3Com-PortPath-r6-MIB", "a3ComPortDialPhoneListPos"))
if mibBuilder.loadTexts: a3ComPortDialPhoneListEntry.setStatus('mandatory')
a3ComPortDialPhoneListPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 19, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComPortDialPhoneListPort.setStatus('mandatory')
a3ComPortDialPhoneListPos = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 19, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComPortDialPhoneListPos.setStatus('mandatory')
a3ComPortDialPhoneListPhoneNo = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 19, 4, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 51))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPortDialPhoneListPhoneNo.setStatus('mandatory')
a3ComPortDialPhoneListType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 19, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("iSDN", 1), ("analog", 2), ("other", 3))).clone('analog')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPortDialPhoneListType.setStatus('mandatory')
a3ComPortDialPhoneListBaud = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 19, 4, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000000)).clone(9600)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPortDialPhoneListBaud.setStatus('mandatory')
a3ComPortDialPhoneListStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 19, 4, 1, 6), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComPortDialPhoneListStatus.setStatus('mandatory')
mibBuilder.exportSymbols("A3Com-PortPath-r6-MIB", a3ComPortInCallerId=a3ComPortInCallerId, a3ComDefaultPriority=a3ComDefaultPriority, a3ComPathDialEntry=a3ComPathDialEntry, a3ComPortDialInitState=a3ComPortDialInitState, a3ComPortDialPhoneListStatus=a3ComPortDialPhoneListStatus, a3ComPortDialDodPktsOut=a3ComPortDialDodPktsOut, a3ComPortIbmTraffic=a3ComPortIbmTraffic, a3ComPathOutDiscards=a3ComPathOutDiscards, a3ComPathInUcastPkts=a3ComPathInUcastPkts, a3ComPathDialNumber=a3ComPathDialNumber, a3ComPathClock=a3ComPathClock, a3ComPortDialPoolPrefTable=a3ComPortDialPoolPrefTable, a3ComPathDialRateAdaption=a3ComPathDialRateAdaption, a3ComPortDialPoolPrefEntry=a3ComPortDialPoolPrefEntry, a3ComPathCRC=a3ComPathCRC, a3ComPathAdminStatus=a3ComPathAdminStatus, a3ComPortDialPoolPrefPort=a3ComPortDialPoolPrefPort, a3ComPathOutUcastPkts=a3ComPathOutUcastPkts, a3ComPathDialMode=a3ComPathDialMode, a3ComPathOutOctets=a3ComPathOutOctets, a3ComPathPort=a3ComPathPort, a3ComPortDIALNumber=a3ComPortDIALNumber, a3ComPathName=a3ComPathName, a3ComPathDialLocalSubAddress=a3ComPathDialLocalSubAddress, a3ComPathDialAction=a3ComPathDialAction, a3ComPath=a3ComPath, a3ComPathBaudRate=a3ComPathBaudRate, a3ComPortDialDisasterCtl=a3ComPortDialDisasterCtl, a3ComPortMacAddrFmtIPX=a3ComPortMacAddrFmtIPX, a3ComPortMacAddrFmtXNS=a3ComPortMacAddrFmtXNS, a3ComPathDialDodIdleTime=a3ComPathDialDodIdleTime, a3ComPathDialExDevType=a3ComPathDialExDevType, a3ComPortDialBODTHreshold=a3ComPortDialBODTHreshold, a3ComPathNumber=a3ComPathNumber, a3ComPathDialTable=a3ComPathDialTable, a3ComPortDialPhoneListPos=a3ComPortDialPhoneListPos, a3ComPortDialDodUpTime=a3ComPortDialDodUpTime, a3ComPortDial=a3ComPortDial, a3ComPathOperStatus=a3ComPathOperStatus, a3ComPathDialSwitchType=a3ComPathDialSwitchType, a3ComPortOwner=a3ComPortOwner, a3ComPortBoundaryEncap=a3ComPortBoundaryEncap, a3ComPortDialRcvrState=a3ComPortDialRcvrState, a3ComPortDialPhoneListBaud=a3ComPortDialPhoneListBaud, a3ComPortNumber=a3ComPortNumber, a3ComPathSlotIndex=a3ComPathSlotIndex, a3ComPathDialSPIDDN1=a3ComPathDialSPIDDN1, a3ComPortTable=a3ComPortTable, a3ComQueueInterleave2=a3ComQueueInterleave2, a3ComPortDialDodIdleTime=a3ComPortDialDodIdleTime, a3ComPathInDiscards=a3ComPathInDiscards, a3ComPathOutErrors=a3ComPathOutErrors, a3ComPathInUnknownProtos=a3ComPathInUnknownProtos, a3ComPortDialDodCallsFail=a3ComPortDialDodCallsFail, a3ComPortDialPoolPrefPathNum=a3ComPortDialPoolPrefPathNum, a3ComPathItcmOption=a3ComPathItcmOption, a3ComPortName=a3ComPortName, a3ComPathBaud=a3ComPathBaud, a3ComSmartFilteringCtl=a3ComSmartFilteringCtl, a3ComPortAsOwnerTimer=a3ComPortAsOwnerTimer, a3ComPortLabel=a3ComPortLabel, a3ComPortDialPhoneListEntry=a3ComPortDialPhoneListEntry, a3ComPortDialIdleTime=a3ComPortDialIdleTime, a3ComQueuePattern=a3ComQueuePattern, a3Com=a3Com, a3ComPortBoundaryRoute=a3ComPortBoundaryRoute, a3ComPathDuplex=a3ComPathDuplex, a3ComPathDialDynCont=a3ComPathDialDynCont, a3ComPathInOctets=a3ComPathInOctets, a3ComPathEntry=a3ComPathEntry, a3ComPortDialPoolPrefStatus=a3ComPortDialPoolPrefStatus, a3ComPathDial=a3ComPathDial, a3ComPortDialPhoneListType=a3ComPortDialPhoneListType, a3ComPortMacAddrFmtARP=a3ComPortMacAddrFmtARP, a3ComPortDialPhoneListTable=a3ComPortDialPhoneListTable, a3ComPortCircuitID=a3ComPortCircuitID, a3ComPathDialSPIDDN2=a3ComPathDialSPIDDN2, a3ComPathConnPos=a3ComPathConnPos, a3ComPortDialIndex=a3ComPortDialIndex, a3ComPortDialPhoneListPhoneNo=a3ComPortDialPhoneListPhoneNo, a3ComPortDialBandOnDmnd=a3ComPortDialBandOnDmnd, a3ComPathDialIndex=a3ComPathDialIndex, a3ComPortDialTable=a3ComPortDialTable, a3ComPathT1Mode=a3ComPathT1Mode, a3ComPortDialDodCallsMade=a3ComPortDialDodCallsMade, a3ComPortDialPhoneListPort=a3ComPortDialPhoneListPort, a3ComPathTable=a3ComPathTable, a3ComPathInNUcastPkts=a3ComPathInNUcastPkts, a3ComPortVirtual=a3ComPortVirtual, a3ComPortDialAction=a3ComPortDialAction, a3ComPortCompType=a3ComPortCompType, brouterMIB=brouterMIB, a3ComPortDialDebounceTimeUp=a3ComPortDialDebounceTimeUp, a3ComPortDialPoolPrefPathPos=a3ComPortDialPoolPrefPathPos, a3ComPathConn=a3ComPathConn, a3ComPortX25ProtID=a3ComPortX25ProtID, a3ComPathInErrors=a3ComPathInErrors, a3ComPathDialLocalDialNumber=a3ComPathDialLocalDialNumber, a3ComPathOutNUcastPkts=a3ComPathOutNUcastPkts, a3ComPortCosInterleave=a3ComPortCosInterleave, a3ComQueueThrottle=a3ComQueueThrottle, a3ComPortStatus=a3ComPortStatus, a3ComPortPath=a3ComPortPath, a3ComPort=a3ComPort, a3ComBrCentralMacCtl=a3ComBrCentralMacCtl, a3ComPortDialDebounceTimeDown=a3ComPortDialDebounceTimeDown, a3ComQueueInterleave1=a3ComQueueInterleave1, a3ComPortIndex=a3ComPortIndex, RowStatus=RowStatus, a3ComPortEntry=a3ComPortEntry, a3ComPathCryptoResync=a3ComPathCryptoResync, a3ComPathIndex=a3ComPathIndex, a3ComPortDialEntry=a3ComPortDialEntry, a3ComPathDialType=a3ComPathDialType, a3ComPathDialCtl=a3ComPathDialCtl, a3ComPathLastChange=a3ComPathLastChange, a3ComPathDialNum=a3ComPathDialNum)
