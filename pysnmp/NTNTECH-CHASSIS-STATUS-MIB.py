#
# PySNMP MIB module NTNTECH-CHASSIS-STATUS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NTNTECH-CHASSIS-STATUS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:15:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ntntechChassis, NtnDisplayString, NtnMacAddress = mibBuilder.importSymbols("NTNTECH-ROOT-MIB", "ntntechChassis", "NtnDisplayString", "NtnMacAddress")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Bits, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, iso, IpAddress, TimeTicks, Counter64, Integer32, NotificationType, Unsigned32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Bits", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "iso", "IpAddress", "TimeTicks", "Counter64", "Integer32", "NotificationType", "Unsigned32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ntntechChassisStatusMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2))
ntntechChassisStatusMIB.setRevisions(('1902-05-06 10:54', '1902-08-06 10:45', '1902-08-28 09:35', '1902-09-24 11:24', '1902-10-11 09:00', '1902-10-22 02:00', '1902-11-04 10:36', '1903-11-14 08:42', '1904-03-15 10:16', '1904-04-27 10:42', '1904-10-11 09:19', '1904-11-17 10:00',))
if mibBuilder.loadTexts: ntntechChassisStatusMIB.setLastUpdated('0411170200Z')
if mibBuilder.loadTexts: ntntechChassisStatusMIB.setOrganization('Paradyne Corporation')
chsStaMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1))
chsStaValues = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1))
valMultiplexerUplinkModule = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1))
mumStaChassisType = MibScalar((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("iPD12000", 1), ("iPD4000", 2), ("miniDSLAM", 3), ("microDSLAM", 4), ("networkExtender", 5), ("iPD12000E", 6), ("iPD4000E", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mumStaChassisType.setStatus('current')
mumStaFanState = MibScalar((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("on", 1), ("fault", 2), ("alert", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mumStaFanState.setStatus('current')
mumStaTable = MibTable((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 4), )
if mibBuilder.loadTexts: mumStaTable.setStatus('current')
mumStaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 4, 1), ).setIndexNames((0, "NTNTECH-CHASSIS-STATUS-MIB", "mumStaIndex"))
if mibBuilder.loadTexts: mumStaEntry.setStatus('current')
mumStaIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mumStaIndex.setStatus('current')
mumStaMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 4, 1, 2), NtnMacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mumStaMacAddress.setStatus('current')
mumStaFirmWareRev = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 4, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(7, 7)).setFixedLength(7)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mumStaFirmWareRev.setStatus('current')
mumStaType = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(129, 128, 11, 7, 8, 19, 130, 22, 23, 24, 25, 26, 27, 28, 29, 135, 14, 137))).clone(namedValues=NamedValues(("mum2000p2", 129), ("mum200p2", 128), ("amD8000p12", 11), ("smD2000p12", 7), ("smD2000Qp12", 8), ("smD2000Gp12", 19), ("smD2000p24", 130), ("suD2011p12T", 22), ("suD2011p12E", 23), ("suD2003p12T", 24), ("suD2003p12E", 25), ("suD2011p6T", 26), ("suD2011p6E", 27), ("suD2002p6T", 28), ("suD2002p6E", 29), ("ane8420", 135), ("sne2040", 14), ("bsx8000", 137)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mumStaType.setStatus('current')
mumStaMgmtPortTable = MibTable((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 5), )
if mibBuilder.loadTexts: mumStaMgmtPortTable.setStatus('current')
mumStaMgmtPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 5, 1), ).setIndexNames((0, "NTNTECH-CHASSIS-STATUS-MIB", "mumStaMgmtPortMumIndex"))
if mibBuilder.loadTexts: mumStaMgmtPortEntry.setStatus('current')
mumStaMgmtPortMumIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mumStaMgmtPortMumIndex.setStatus('current')
mumStaMgmtPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mgmt", 1), ("uplink", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mumStaMgmtPortType.setStatus('current')
mumStaMgmtPortLinkState = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("link", 1), ("noLink", 2), ("fault", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mumStaMgmtPortLinkState.setStatus('current')
mumStaMgmtPortRxTxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("uimEthNoLink", 0), ("uimEth10", 1), ("uimEth100", 2), ("uimEthGig", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mumStaMgmtPortRxTxRate.setStatus('current')
mumStaMgmtPortDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("uimEthNoLink", 0), ("uimEthHalf", 1), ("uimEthFull", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mumStaMgmtPortDuplex.setStatus('current')
mumStaUplinkInterfaceModule = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6))
uimStaTable = MibTable((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6, 1), )
if mibBuilder.loadTexts: uimStaTable.setStatus('current')
uimStaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6, 1, 1), ).setIndexNames((0, "NTNTECH-CHASSIS-STATUS-MIB", "uimStaMumIndex"), (0, "NTNTECH-CHASSIS-STATUS-MIB", "uimStaIndex"))
if mibBuilder.loadTexts: uimStaEntry.setStatus('current')
uimStaMumIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: uimStaMumIndex.setStatus('current')
uimStaIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: uimStaIndex.setStatus('current')
uimStaType = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("uimEther100", 1), ("uimT1", 2), ("uimDS3", 3), ("uimE1", 4), ("uimE3", 5), ("uimGig", 6), ("uimGigFx", 7), ("uim100Fx", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: uimStaType.setStatus('current')
uimStaLinkState = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("link", 1), ("noLink", 2), ("fault", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: uimStaLinkState.setStatus('current')
uimStaEthTable = MibTable((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6, 2), )
if mibBuilder.loadTexts: uimStaEthTable.setStatus('current')
uimStaEthEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6, 2, 1), ).setIndexNames((0, "NTNTECH-CHASSIS-STATUS-MIB", "uimStaEthMumIndex"), (0, "NTNTECH-CHASSIS-STATUS-MIB", "uimStaEthIndex"))
if mibBuilder.loadTexts: uimStaEthEntry.setStatus('current')
uimStaEthMumIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: uimStaEthMumIndex.setStatus('current')
uimStaEthIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: uimStaEthIndex.setStatus('current')
uimStaEthRxTxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("uimEthNoLink", 0), ("uimEth10", 1), ("uimEth100", 2), ("uimEthGig", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: uimStaEthRxTxRate.setStatus('current')
uimStaEthDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("uimEthNoLink", 0), ("uimEthHalf", 1), ("uimEthFull", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: uimStaEthDuplex.setStatus('current')
uimStaT1Table = MibTable((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6, 3), )
if mibBuilder.loadTexts: uimStaT1Table.setStatus('current')
uimStaT1Entry = MibTableRow((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6, 3, 1), ).setIndexNames((0, "NTNTECH-CHASSIS-STATUS-MIB", "uimStaT1MumIndex"), (0, "NTNTECH-CHASSIS-STATUS-MIB", "uimStaT1Index"))
if mibBuilder.loadTexts: uimStaT1Entry.setStatus('current')
uimStaT1MumIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: uimStaT1MumIndex.setStatus('current')
uimStaT1Index = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: uimStaT1Index.setStatus('current')
uimStaT1RxTxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("uimT1NoLink", 0), ("uimT1Rate192", 1), ("uimT1Rate384", 2), ("uimT1Rate576", 3), ("uimT1Rate768", 4), ("uimT1Rate960", 5), ("uimT1Rate1152", 6), ("uimT1Rate1344", 7), ("uimT1Rate1536", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: uimStaT1RxTxRate.setStatus('current')
uimStaE1Table = MibTable((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6, 4), )
if mibBuilder.loadTexts: uimStaE1Table.setStatus('current')
uimStaE1Entry = MibTableRow((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6, 4, 1), ).setIndexNames((0, "NTNTECH-CHASSIS-STATUS-MIB", "uimStaE1MumIndex"), (0, "NTNTECH-CHASSIS-STATUS-MIB", "uimStaE1Index"))
if mibBuilder.loadTexts: uimStaE1Entry.setStatus('current')
uimStaE1MumIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: uimStaE1MumIndex.setStatus('current')
uimStaE1Index = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: uimStaE1Index.setStatus('current')
uimStaE1RxTxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 2, 1, 1, 1, 6, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("uimE1NoLink", 0), ("uimE1Rate256", 1), ("uimE1Rate512", 2), ("uimE1Rate768", 3), ("uimE1Rate1024", 4), ("uimE1Rate1280", 5), ("uimE1Rate1536", 6), ("uimE1Rate1792", 7), ("uimE1Rate1984", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: uimStaE1RxTxRate.setStatus('current')
mibBuilder.exportSymbols("NTNTECH-CHASSIS-STATUS-MIB", mumStaChassisType=mumStaChassisType, uimStaE1Index=uimStaE1Index, uimStaE1MumIndex=uimStaE1MumIndex, chsStaValues=chsStaValues, valMultiplexerUplinkModule=valMultiplexerUplinkModule, mumStaMgmtPortEntry=mumStaMgmtPortEntry, mumStaType=mumStaType, mumStaFirmWareRev=mumStaFirmWareRev, uimStaType=uimStaType, ntntechChassisStatusMIB=ntntechChassisStatusMIB, mumStaMgmtPortType=mumStaMgmtPortType, mumStaIndex=mumStaIndex, uimStaE1Table=uimStaE1Table, uimStaIndex=uimStaIndex, mumStaMgmtPortDuplex=mumStaMgmtPortDuplex, mumStaMgmtPortTable=mumStaMgmtPortTable, uimStaTable=uimStaTable, mumStaUplinkInterfaceModule=mumStaUplinkInterfaceModule, uimStaEntry=uimStaEntry, uimStaE1Entry=uimStaE1Entry, mumStaMgmtPortLinkState=mumStaMgmtPortLinkState, mumStaTable=mumStaTable, uimStaT1Entry=uimStaT1Entry, uimStaEthTable=uimStaEthTable, uimStaT1Table=uimStaT1Table, uimStaEthIndex=uimStaEthIndex, mumStaEntry=mumStaEntry, mumStaMacAddress=mumStaMacAddress, uimStaT1RxTxRate=uimStaT1RxTxRate, uimStaMumIndex=uimStaMumIndex, uimStaEthMumIndex=uimStaEthMumIndex, uimStaT1MumIndex=uimStaT1MumIndex, uimStaE1RxTxRate=uimStaE1RxTxRate, uimStaEthDuplex=uimStaEthDuplex, mumStaMgmtPortRxTxRate=mumStaMgmtPortRxTxRate, mumStaMgmtPortMumIndex=mumStaMgmtPortMumIndex, uimStaEthEntry=uimStaEthEntry, uimStaT1Index=uimStaT1Index, uimStaEthRxTxRate=uimStaEthRxTxRate, mumStaFanState=mumStaFanState, uimStaLinkState=uimStaLinkState, PYSNMP_MODULE_ID=ntntechChassisStatusMIB, chsStaMIBObjects=chsStaMIBObjects)