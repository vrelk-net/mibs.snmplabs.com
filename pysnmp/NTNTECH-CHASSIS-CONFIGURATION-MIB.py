#
# PySNMP MIB module NTNTECH-CHASSIS-CONFIGURATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NTNTECH-CHASSIS-CONFIGURATION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:15:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NtnDefaultGateway, NtnDisplayString, ntntechChassis, NtnSubnetMask, NtnTimeTicks = mibBuilder.importSymbols("NTNTECH-ROOT-MIB", "NtnDefaultGateway", "NtnDisplayString", "ntntechChassis", "NtnSubnetMask", "NtnTimeTicks")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Bits, Integer32, TimeTicks, Counter32, NotificationType, ModuleIdentity, iso, Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Bits", "Integer32", "TimeTicks", "Counter32", "NotificationType", "ModuleIdentity", "iso", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Unsigned32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ntntechChassisConfigurationMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1))
ntntechChassisConfigurationMIB.setRevisions(('1902-08-13 11:12', '1902-08-28 09:12', '1902-10-11 09:13', '1902-10-22 02:00', '1902-11-04 12:58', '1904-03-15 10:15', '1904-04-27 11:16', '1904-10-11 09:09', '1904-11-17 09:58',))
if mibBuilder.loadTexts: ntntechChassisConfigurationMIB.setLastUpdated('0411170200Z')
if mibBuilder.loadTexts: ntntechChassisConfigurationMIB.setOrganization('Paradyne Corporation')
chsCfgMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1))
chsCfgParameterConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1))
prmCfgMultiplexerUplinkModule = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1))
mumCfgNotes = MibScalar((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 1), NtnDisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mumCfgNotes.setStatus('current')
mumCfgTable = MibTable((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 2), )
if mibBuilder.loadTexts: mumCfgTable.setStatus('current')
mumCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 2, 1), ).setIndexNames((0, "NTNTECH-CHASSIS-CONFIGURATION-MIB", "mumCfgIndex"))
if mibBuilder.loadTexts: mumCfgEntry.setStatus('current')
mumCfgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mumCfgIndex.setStatus('current')
mumCfgIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 2, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mumCfgIpAddress.setStatus('current')
mumCfgSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 2, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mumCfgSubnetMask.setStatus('current')
mumCfgDefaultGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 2, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mumCfgDefaultGateway.setStatus('current')
mumCfgInbandMgmt = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mumCfgInbandMgmt.setStatus('current')
mumCfgInbandMGMTVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4085))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mumCfgInbandMGMTVlanID.setStatus('current')
mumCfgInterConnection = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("neither", 1), ("uplink1", 2), ("uplink2", 3), ("uplink3", 4), ("uplink4", 5), ("mgmt", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mumCfgInterConnection.setStatus('current')
mumCfgCommitChange = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mumCfgCommitChange.setStatus('current')
mumCfgUplinkInterfaceModule = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3))
uimCfgEthTable = MibTable((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 1), )
if mibBuilder.loadTexts: uimCfgEthTable.setStatus('current')
uimCfgEthEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 1, 1), ).setIndexNames((0, "NTNTECH-CHASSIS-CONFIGURATION-MIB", "uimCfgEthMumIndex"), (0, "NTNTECH-CHASSIS-CONFIGURATION-MIB", "uimCfgEthIndex"))
if mibBuilder.loadTexts: uimCfgEthEntry.setStatus('current')
uimCfgEthMumIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: uimCfgEthMumIndex.setStatus('current')
uimCfgEthIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: uimCfgEthIndex.setStatus('current')
uimCfgEthRxTxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("uimEthAutoNegotiate", 0), ("uimEth10", 1), ("uimEth100", 2), ("uimEthGig", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uimCfgEthRxTxRate.setStatus('current')
uimCfgEthDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("uimEthAutoNegotiate", 0), ("uimEthHalf", 1), ("uimEthFull", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uimCfgEthDuplex.setStatus('current')
uimCfgT1Table = MibTable((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 2), )
if mibBuilder.loadTexts: uimCfgT1Table.setStatus('current')
uimCfgT1Entry = MibTableRow((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 2, 1), ).setIndexNames((0, "NTNTECH-CHASSIS-CONFIGURATION-MIB", "uimCfgT1MumIndex"), (0, "NTNTECH-CHASSIS-CONFIGURATION-MIB", "uimCfgT1Index"))
if mibBuilder.loadTexts: uimCfgT1Entry.setStatus('current')
uimCfgT1MumIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: uimCfgT1MumIndex.setStatus('current')
uimCfgT1Index = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: uimCfgT1Index.setStatus('current')
uimCfgT1Frame = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("uimT1ESF", 1), ("uimT1SFD4", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uimCfgT1Frame.setStatus('current')
uimCfgT1LineCode = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("uimT1B8ZS", 1), ("uimT1AMI", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uimCfgT1LineCode.setStatus('current')
uimCfgT1LineBuildout = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("uimT10db", 1), ("uimT1N7p5db", 2), ("uimT1N15db", 3), ("uimT1N22p5db", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uimCfgT1LineBuildout.setStatus('current')
uimCfgE1Table = MibTable((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 3), )
if mibBuilder.loadTexts: uimCfgE1Table.setStatus('current')
uimCfgE1Entry = MibTableRow((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 3, 1), ).setIndexNames((0, "NTNTECH-CHASSIS-CONFIGURATION-MIB", "uimCfgE1MumIndex"), (0, "NTNTECH-CHASSIS-CONFIGURATION-MIB", "uimCfgE1Index"))
if mibBuilder.loadTexts: uimCfgE1Entry.setStatus('current')
uimCfgE1MumIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: uimCfgE1MumIndex.setStatus('current')
uimCfgE1Index = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: uimCfgE1Index.setStatus('current')
uimCfgE1Frame = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("uimE1CRC", 1), ("uimE1NoCRC", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uimCfgE1Frame.setStatus('current')
uimCfgE1LineCode = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 3, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("uimE1HDB3", 1), ("uimE1AMI", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uimCfgE1LineCode.setStatus('current')
mumSNMPConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 4))
snmpCfgNoticeIpTable = MibTable((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 4, 1), )
if mibBuilder.loadTexts: snmpCfgNoticeIpTable.setStatus('current')
snmpCfgNoticeIpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 4, 1, 1), ).setIndexNames((0, "NTNTECH-CHASSIS-CONFIGURATION-MIB", "snmpCfgNoticeIndex"))
if mibBuilder.loadTexts: snmpCfgNoticeIpEntry.setStatus('current')
snmpCfgNoticeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpCfgNoticeIndex.setStatus('current')
snmpCfgNoticeIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 4, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpCfgNoticeIpAddress.setStatus('current')
snmpCfgAuthenticationTrapState = MibScalar((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpCfgAuthenticationTrapState.setStatus('current')
snmpCfgEnvironmentTrapState = MibScalar((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 4, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpCfgEnvironmentTrapState.setStatus('current')
snmpCfgColdstartTrapState = MibScalar((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 4, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpCfgColdstartTrapState.setStatus('current')
snmpCfgModulePortTrapState = MibScalar((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 4, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpCfgModulePortTrapState.setStatus('current')
snmpCfgCommunity = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 4, 6))
comReadWriteAccess = MibScalar((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 4, 6, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: comReadWriteAccess.setStatus('current')
comReadOnlyAccess = MibScalar((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 4, 6, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: comReadOnlyAccess.setStatus('current')
mumCfgUniques = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 5))
unqEmbHttpWebsrvrState = MibScalar((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: unqEmbHttpWebsrvrState.setStatus('current')
mumCfgAdvanced = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 6))
advCfgTable = MibTable((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 6, 1), )
if mibBuilder.loadTexts: advCfgTable.setStatus('current')
advCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 6, 1, 1), ).setIndexNames((0, "NTNTECH-CHASSIS-CONFIGURATION-MIB", "advCfgMumIndex"))
if mibBuilder.loadTexts: advCfgEntry.setStatus('current')
advCfgMumIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: advCfgMumIndex.setStatus('current')
advCfgTFTPState = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 6, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: advCfgTFTPState.setStatus('current')
advCfgTelnetState = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 6, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: advCfgTelnetState.setStatus('current')
advCfgMgmtFltrIpStart = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 6, 1, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: advCfgMgmtFltrIpStart.setStatus('current')
advCfgMgmtFltrIpEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 6, 1, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: advCfgMgmtFltrIpEnd.setStatus('current')
advCfgMgmtSessionTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 6, 1, 1, 6), NtnTimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: advCfgMgmtSessionTimeout.setStatus('current')
mumCfgManagementPort = MibIdentifier((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 7))
mgmtPortCfgTable = MibTable((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 7, 1), )
if mibBuilder.loadTexts: mgmtPortCfgTable.setStatus('current')
mgmtPortCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 7, 1, 1), ).setIndexNames((0, "NTNTECH-CHASSIS-CONFIGURATION-MIB", "mgmtPortCfgMumIndex"))
if mibBuilder.loadTexts: mgmtPortCfgEntry.setStatus('current')
mgmtPortCfgMumIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 7, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgmtPortCfgMumIndex.setStatus('current')
mgmtPortCfgRxTxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 7, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("uimEthAutoNegotiate", 0), ("uimEth10", 1), ("uimEth100", 2), ("uimEthGig", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mgmtPortCfgRxTxRate.setStatus('current')
mgmtPortCfgDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 7, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("uimEthAutoNegotiate", 0), ("uimEthHalf", 1), ("uimEthFull", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mgmtPortCfgDuplex.setStatus('current')
mgmtPortCfgType = MibTableColumn((1, 3, 6, 1, 4, 1, 8059, 1, 1, 1, 1, 1, 1, 7, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mgmt", 1), ("uplink", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mgmtPortCfgType.setStatus('current')
mibBuilder.exportSymbols("NTNTECH-CHASSIS-CONFIGURATION-MIB", uimCfgEthMumIndex=uimCfgEthMumIndex, mumCfgEntry=mumCfgEntry, uimCfgT1MumIndex=uimCfgT1MumIndex, snmpCfgModulePortTrapState=snmpCfgModulePortTrapState, snmpCfgNoticeIndex=snmpCfgNoticeIndex, mumCfgInbandMGMTVlanID=mumCfgInbandMGMTVlanID, uimCfgT1LineBuildout=uimCfgT1LineBuildout, snmpCfgEnvironmentTrapState=snmpCfgEnvironmentTrapState, mumCfgManagementPort=mumCfgManagementPort, uimCfgE1LineCode=uimCfgE1LineCode, uimCfgEthRxTxRate=uimCfgEthRxTxRate, advCfgTable=advCfgTable, mumCfgUniques=mumCfgUniques, mumCfgUplinkInterfaceModule=mumCfgUplinkInterfaceModule, uimCfgE1Entry=uimCfgE1Entry, mgmtPortCfgTable=mgmtPortCfgTable, uimCfgT1Table=uimCfgT1Table, advCfgMgmtSessionTimeout=advCfgMgmtSessionTimeout, mgmtPortCfgEntry=mgmtPortCfgEntry, mumCfgCommitChange=mumCfgCommitChange, uimCfgT1Entry=uimCfgT1Entry, advCfgEntry=advCfgEntry, uimCfgEthDuplex=uimCfgEthDuplex, uimCfgEthEntry=uimCfgEthEntry, uimCfgT1Index=uimCfgT1Index, chsCfgMIBObjects=chsCfgMIBObjects, prmCfgMultiplexerUplinkModule=prmCfgMultiplexerUplinkModule, advCfgTFTPState=advCfgTFTPState, advCfgMumIndex=advCfgMumIndex, uimCfgE1Frame=uimCfgE1Frame, snmpCfgAuthenticationTrapState=snmpCfgAuthenticationTrapState, mgmtPortCfgMumIndex=mgmtPortCfgMumIndex, uimCfgEthIndex=uimCfgEthIndex, mumSNMPConfiguration=mumSNMPConfiguration, comReadWriteAccess=comReadWriteAccess, snmpCfgNoticeIpTable=snmpCfgNoticeIpTable, PYSNMP_MODULE_ID=ntntechChassisConfigurationMIB, uimCfgEthTable=uimCfgEthTable, uimCfgT1LineCode=uimCfgT1LineCode, unqEmbHttpWebsrvrState=unqEmbHttpWebsrvrState, mgmtPortCfgType=mgmtPortCfgType, advCfgTelnetState=advCfgTelnetState, mumCfgInbandMgmt=mumCfgInbandMgmt, mumCfgDefaultGateway=mumCfgDefaultGateway, ntntechChassisConfigurationMIB=ntntechChassisConfigurationMIB, uimCfgE1Table=uimCfgE1Table, snmpCfgNoticeIpAddress=snmpCfgNoticeIpAddress, snmpCfgCommunity=snmpCfgCommunity, mumCfgAdvanced=mumCfgAdvanced, advCfgMgmtFltrIpStart=advCfgMgmtFltrIpStart, mumCfgTable=mumCfgTable, mumCfgInterConnection=mumCfgInterConnection, mgmtPortCfgDuplex=mgmtPortCfgDuplex, mgmtPortCfgRxTxRate=mgmtPortCfgRxTxRate, snmpCfgColdstartTrapState=snmpCfgColdstartTrapState, mumCfgIndex=mumCfgIndex, snmpCfgNoticeIpEntry=snmpCfgNoticeIpEntry, comReadOnlyAccess=comReadOnlyAccess, uimCfgT1Frame=uimCfgT1Frame, mumCfgIpAddress=mumCfgIpAddress, advCfgMgmtFltrIpEnd=advCfgMgmtFltrIpEnd, mumCfgSubnetMask=mumCfgSubnetMask, chsCfgParameterConfiguration=chsCfgParameterConfiguration, uimCfgE1Index=uimCfgE1Index, uimCfgE1MumIndex=uimCfgE1MumIndex, mumCfgNotes=mumCfgNotes)