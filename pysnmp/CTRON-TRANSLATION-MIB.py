#
# PySNMP MIB module CTRON-TRANSLATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CTRON-TRANSLATION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:16:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
MacAddress, = mibBuilder.importSymbols("BRIDGE-MIB", "MacAddress")
ctTranslation, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctTranslation")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Gauge32, MibIdentifier, TimeTicks, Unsigned32, ObjectIdentity, Counter64, NotificationType, IpAddress, Integer32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Gauge32", "MibIdentifier", "TimeTicks", "Unsigned32", "ObjectIdentity", "Counter64", "NotificationType", "IpAddress", "Integer32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ctTransFddiAtm = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 1))
ctTransFddiEthernet = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 2))
ctTransEthernetFddi = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 3))
ctTransRifDb = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 4))
ctTransBcastX = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 5))
ctTransIbmLlc = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 6))
ctTransSr = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 7))
ctTransNovellCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 8))
ctTransIPCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 9))
ctTransA2Cfg = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 10))
ctTransOtherCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11))
ctTranslfpsCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 12))
ctTransFddiAtmMtu = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("greater1518MTU", 1), ("less1518MTU", 2))).clone('greater1518MTU')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransFddiAtmMtu.setStatus('mandatory')
ctTransFddiAtmIPFrag = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransFddiAtmIPFrag.setStatus('mandatory')
ctTransFddiEthernetIPFrag = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransFddiEthernetIPFrag.setStatus('mandatory')
ctTransFddiSnapEthernetType = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ethernetII", 1), ("ethernetSnap", 2))).clone('ethernetII')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransFddiSnapEthernetType.setStatus('mandatory')
ctTransFddiEthernetAuto = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("notSupported", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransFddiEthernetAuto.setStatus('mandatory')
ctTransFddiEthernetSnapIPX = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ethernetII", 1), ("ethernetSnap", 2), ("ethernet802dot3", 3), ("ethernet802dot3Raw", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransFddiEthernetSnapIPX.setStatus('mandatory')
ctTransFddiEthernet802dot2IPX = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ethernetII", 1), ("ethernetSnap", 2), ("ethernet802dot3", 3), ("ethernet802dot3Raw", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransFddiEthernet802dot2IPX.setStatus('mandatory')
ctTransFddiEthernetMACIPX = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ethernetII", 1), ("ethernetSnap", 2), ("ethernet802dot3", 3), ("ethernet802dot3Raw", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransFddiEthernetMACIPX.setStatus('mandatory')
ctTransEthernetFddiRAW = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("fDDI802dot2", 1), ("fDDISnap", 2), ("fDDIMAC", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransEthernetFddiRAW.setStatus('mandatory')
ctTransEthernetFddiPadVerify = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("not-supported", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransEthernetFddiPadVerify.setStatus('mandatory')
ctTransRifDbTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 4, 1), )
if mibBuilder.loadTexts: ctTransRifDbTable.setStatus('mandatory')
ctTransRifDbEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 4, 1, 1), ).setIndexNames((0, "CTRON-TRANSLATION-MIB", "ctTransRifDbMacAddr"))
if mibBuilder.loadTexts: ctTransRifDbEntry.setStatus('mandatory')
ctTransRifDbMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 4, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTransRifDbMacAddr.setStatus('mandatory')
ctTransRifDbSrcPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 4, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTransRifDbSrcPort.setStatus('mandatory')
ctTransRifDbLength = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 4, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTransRifDbLength.setStatus('mandatory')
ctTransRifDbRIF = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 4, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTransRifDbRIF.setStatus('mandatory')
ctTransRifDbCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 4, 2), )
if mibBuilder.loadTexts: ctTransRifDbCtrlTable.setStatus('mandatory')
ctTransRifDbCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 4, 2, 1), ).setIndexNames((0, "CTRON-TRANSLATION-MIB", "ctTransRifDbCtrlPort"))
if mibBuilder.loadTexts: ctTransRifDbCtrlEntry.setStatus('mandatory')
ctTransRifDbCtrlPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 4, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTransRifDbCtrlPort.setStatus('mandatory')
ctTransRifDbWeightState = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 4, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("notsupported", 1), ("shortestpath", 2), ("quickestpath", 3), ("largestmtu", 4), ("lastseen", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransRifDbWeightState.setStatus('mandatory')
ctTransRifDbCtrlType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 4, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("explorer", 1), ("all", 2), ("notsupported", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransRifDbCtrlType.setStatus('mandatory')
ctTransRifDbAgingTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 4, 2, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransRifDbAgingTimer.setStatus('mandatory')
ctTransBcastXTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 5, 1), )
if mibBuilder.loadTexts: ctTransBcastXTable.setStatus('mandatory')
ctTransBcastXEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 5, 1, 1), ).setIndexNames((0, "CTRON-TRANSLATION-MIB", "ctTransBcastXPort"))
if mibBuilder.loadTexts: ctTransBcastXEntry.setStatus('mandatory')
ctTransBcastXPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 5, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTransBcastXPort.setStatus('mandatory')
ctTransBcastXMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransBcastXMode.setStatus('mandatory')
ctTransBcastXMedia = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 5, 1, 1, 3), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransBcastXMedia.setStatus('mandatory')
ctTransBcastXCanonical = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 5, 1, 1, 4), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransBcastXCanonical.setStatus('mandatory')
ctTransIbmLlcTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 6, 1), )
if mibBuilder.loadTexts: ctTransIbmLlcTable.setStatus('mandatory')
ctTransIbmLlcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 6, 1, 1), ).setIndexNames((0, "CTRON-TRANSLATION-MIB", "ctTransIbmLlcPort"))
if mibBuilder.loadTexts: ctTransIbmLlcEntry.setStatus('mandatory')
ctTransIbmLlcPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 6, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTransIbmLlcPort.setStatus('mandatory')
ctTransIbmLlcNullMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 6, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("notsupported", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransIbmLlcNullMode.setStatus('mandatory')
ctTransIbmLlcSnaPathMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 6, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("notsupported", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransIbmLlcSnaPathMode.setStatus('mandatory')
ctTransIbmLlcSnaMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 6, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("notsupported", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransIbmLlcSnaMode.setStatus('mandatory')
ctTransIbmLlcNbMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 6, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("notsupported", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransIbmLlcNbMode.setStatus('mandatory')
ctTransIbmLlcLnmMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 6, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("notsupported", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransIbmLlcLnmMode.setStatus('mandatory')
ctTransIbmLlcDscMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 6, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("notsupported", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransIbmLlcDscMode.setStatus('mandatory')
ctTransIbmLlcOtherMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 6, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("notsupported", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransIbmLlcOtherMode.setStatus('mandatory')
ctTransIbmLlcOtherValue = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 6, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransIbmLlcOtherValue.setStatus('mandatory')
ctTransSrTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 7, 1), )
if mibBuilder.loadTexts: ctTransSrTable.setStatus('mandatory')
ctTransSrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 7, 1, 1), ).setIndexNames((0, "CTRON-TRANSLATION-MIB", "ctTransSrPort"))
if mibBuilder.loadTexts: ctTransSrEntry.setStatus('mandatory')
ctTransSrPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 7, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTransSrPort.setStatus('mandatory')
ctTransSrIfMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 7, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("tp", 1), ("sr", 2), ("srt", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransSrIfMode.setStatus('mandatory')
ctTransSrExpMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 7, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("notsupported", 1), ("are", 2), ("ste", 3), ("inboundtype", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransSrExpMode.setStatus('mandatory')
ctTransSrIP = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 7, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("tp", 1), ("sr", 2), ("auto", 3), ("notsupported", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransSrIP.setStatus('mandatory')
ctTransSrIPX = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 7, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("tp", 1), ("sr", 2), ("auto", 3), ("notsupported", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransSrIPX.setStatus('mandatory')
ctTransSrNetBIOS = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 7, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("tp", 1), ("sr", 2), ("auto", 3), ("notsupported", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransSrNetBIOS.setStatus('mandatory')
ctTransSrSNA = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 7, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("tp", 1), ("sr", 2), ("auto", 3), ("notsupported", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransSrSNA.setStatus('mandatory')
ctTransSrOther = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 7, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("tp", 1), ("sr", 2), ("auto", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransSrOther.setStatus('mandatory')
ctTransSRLocalSegment = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 7, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransSRLocalSegment.setStatus('mandatory')
ctTransSrSRLF = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 7, 1, 1, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransSrSRLF.setStatus('mandatory')
ctTransSRAutoRingNumberDetect = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 7, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notsupported", 1), ("enable", 2), ("disable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransSRAutoRingNumberDetect.setStatus('mandatory')
ctTransNovellCfgTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 8, 1), )
if mibBuilder.loadTexts: ctTransNovellCfgTable.setStatus('mandatory')
ctTransNovellCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 8, 1, 1), ).setIndexNames((0, "CTRON-TRANSLATION-MIB", "ctTransNovellCfgPort"))
if mibBuilder.loadTexts: ctTransNovellCfgEntry.setStatus('mandatory')
ctTransNovellCfgPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 8, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTransNovellCfgPort.setStatus('mandatory')
ctTransNovellCfgMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 8, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("enabledType2", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransNovellCfgMode.setStatus('mandatory')
ctTransNovellGroupMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 8, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("notsupported", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransNovellGroupMode.setStatus('mandatory')
ctTransIPCfgTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 9, 1), )
if mibBuilder.loadTexts: ctTransIPCfgTable.setStatus('mandatory')
ctTransIPCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 9, 1, 1), ).setIndexNames((0, "CTRON-TRANSLATION-MIB", "ctTransIPCfgPort"))
if mibBuilder.loadTexts: ctTransIPCfgEntry.setStatus('mandatory')
ctTransIPCfgPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 9, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTransIPCfgPort.setStatus('mandatory')
ctTransIPDataCfgMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 9, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransIPDataCfgMode.setStatus('mandatory')
ctTransIPArpCfgMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 9, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransIPArpCfgMode.setStatus('mandatory')
ctTransIPRarpCfgMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 9, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransIPRarpCfgMode.setStatus('mandatory')
ctTransA2CfgTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 10, 1), )
if mibBuilder.loadTexts: ctTransA2CfgTable.setStatus('mandatory')
ctTransA2CfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 10, 1, 1), ).setIndexNames((0, "CTRON-TRANSLATION-MIB", "ctTransA2CfgPort"))
if mibBuilder.loadTexts: ctTransA2CfgEntry.setStatus('mandatory')
ctTransA2CfgPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 10, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTransA2CfgPort.setStatus('mandatory')
ctTransA2DataCfgMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 10, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransA2DataCfgMode.setStatus('mandatory')
ctTransA2ArpCfgMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 10, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransA2ArpCfgMode.setStatus('mandatory')
ctTransA2McastCfgMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 10, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransA2McastCfgMode.setStatus('mandatory')
ctTransOtherTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1), )
if mibBuilder.loadTexts: ctTransOtherTable.setStatus('mandatory')
ctTransOtherEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1, 1), ).setIndexNames((0, "CTRON-TRANSLATION-MIB", "ctTransOtherPort"))
if mibBuilder.loadTexts: ctTransOtherEntry.setStatus('mandatory')
ctTransOtherPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTransOtherPort.setStatus('mandatory')
ctTransOtherUnknownSap = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransOtherUnknownSap.setStatus('mandatory')
ctTransOtherUnknownSnap = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransOtherUnknownSnap.setStatus('mandatory')
ctTransOtherSapDsap1Mode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransOtherSapDsap1Mode.setStatus('mandatory')
ctTransOtherSapDsap1Val = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransOtherSapDsap1Val.setStatus('mandatory')
ctTransOtherSapDsap2Mode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransOtherSapDsap2Mode.setStatus('mandatory')
ctTransOtherSapDsap2Val = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransOtherSapDsap2Val.setStatus('mandatory')
ctTransOtherSapDsap3Mode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransOtherSapDsap3Mode.setStatus('mandatory')
ctTransOtherSapDsap3Val = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransOtherSapDsap3Val.setStatus('mandatory')
ctTransOtherSnap1Mode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransOtherSnap1Mode.setStatus('mandatory')
ctTransOtherSnap1Val = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransOtherSnap1Val.setStatus('mandatory')
ctTransOtherSnap2Mode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransOtherSnap2Mode.setStatus('mandatory')
ctTransOtherSnap2Val = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 11, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransOtherSnap2Val.setStatus('mandatory')
ctTransLfpsTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 12, 1), )
if mibBuilder.loadTexts: ctTransLfpsTable.setStatus('mandatory')
ctTransLfpsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 12, 1, 1), ).setIndexNames((0, "CTRON-TRANSLATION-MIB", "ctTransLfpsPort"))
if mibBuilder.loadTexts: ctTransLfpsEntry.setStatus('mandatory')
ctTransLfpsPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 12, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTransLfpsPort.setStatus('mandatory')
ctTransLfpsAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 12, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("large", 1), ("fragment-if-possible", 2), ("small", 3), ("auto", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctTransLfpsAdminStatus.setStatus('mandatory')
ctTransLfpsOperationalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4, 12, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("large", 1), ("fragment-if-possible", 2), ("small", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctTransLfpsOperationalStatus.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-TRANSLATION-MIB", ctTranslfpsCfg=ctTranslfpsCfg, ctTransSrIPX=ctTransSrIPX, ctTransSrOther=ctTransSrOther, ctTransRifDbLength=ctTransRifDbLength, ctTransIPCfg=ctTransIPCfg, ctTransRifDbAgingTimer=ctTransRifDbAgingTimer, ctTransSrTable=ctTransSrTable, ctTransIbmLlc=ctTransIbmLlc, ctTransSRLocalSegment=ctTransSRLocalSegment, ctTransOtherSapDsap2Mode=ctTransOtherSapDsap2Mode, ctTransIbmLlcNullMode=ctTransIbmLlcNullMode, ctTransSrIfMode=ctTransSrIfMode, ctTransBcastXCanonical=ctTransBcastXCanonical, ctTransNovellGroupMode=ctTransNovellGroupMode, ctTransA2DataCfgMode=ctTransA2DataCfgMode, ctTransIbmLlcTable=ctTransIbmLlcTable, ctTransOtherEntry=ctTransOtherEntry, ctTransA2Cfg=ctTransA2Cfg, ctTransRifDbMacAddr=ctTransRifDbMacAddr, ctTransIPCfgTable=ctTransIPCfgTable, ctTransOtherCfg=ctTransOtherCfg, ctTransRifDbCtrlType=ctTransRifDbCtrlType, ctTransFddiEthernetMACIPX=ctTransFddiEthernetMACIPX, ctTransIbmLlcSnaPathMode=ctTransIbmLlcSnaPathMode, ctTransIbmLlcDscMode=ctTransIbmLlcDscMode, ctTransRifDb=ctTransRifDb, ctTransLfpsPort=ctTransLfpsPort, ctTransRifDbEntry=ctTransRifDbEntry, ctTransOtherSnap2Val=ctTransOtherSnap2Val, ctTransRifDbWeightState=ctTransRifDbWeightState, ctTransLfpsOperationalStatus=ctTransLfpsOperationalStatus, ctTransOtherUnknownSnap=ctTransOtherUnknownSnap, ctTransOtherSnap2Mode=ctTransOtherSnap2Mode, ctTransSrExpMode=ctTransSrExpMode, ctTransSrNetBIOS=ctTransSrNetBIOS, ctTransOtherSapDsap1Val=ctTransOtherSapDsap1Val, ctTransSrEntry=ctTransSrEntry, ctTransIPCfgPort=ctTransIPCfgPort, ctTransBcastXPort=ctTransBcastXPort, ctTransLfpsEntry=ctTransLfpsEntry, ctTransRifDbTable=ctTransRifDbTable, ctTransBcastXMedia=ctTransBcastXMedia, ctTransLfpsTable=ctTransLfpsTable, ctTransEthernetFddiPadVerify=ctTransEthernetFddiPadVerify, ctTransFddiEthernet802dot2IPX=ctTransFddiEthernet802dot2IPX, ctTransIPCfgEntry=ctTransIPCfgEntry, ctTransOtherSapDsap1Mode=ctTransOtherSapDsap1Mode, ctTransFddiEthernetSnapIPX=ctTransFddiEthernetSnapIPX, ctTransSrIP=ctTransSrIP, ctTransOtherSapDsap3Val=ctTransOtherSapDsap3Val, ctTransBcastXMode=ctTransBcastXMode, ctTransFddiEthernet=ctTransFddiEthernet, ctTransBcastX=ctTransBcastX, ctTransRifDbCtrlTable=ctTransRifDbCtrlTable, ctTransFddiAtm=ctTransFddiAtm, ctTransRifDbRIF=ctTransRifDbRIF, ctTransNovellCfgTable=ctTransNovellCfgTable, ctTransLfpsAdminStatus=ctTransLfpsAdminStatus, ctTransFddiAtmMtu=ctTransFddiAtmMtu, ctTransFddiAtmIPFrag=ctTransFddiAtmIPFrag, ctTransIPRarpCfgMode=ctTransIPRarpCfgMode, ctTransOtherSnap1Mode=ctTransOtherSnap1Mode, ctTransIbmLlcSnaMode=ctTransIbmLlcSnaMode, ctTransRifDbCtrlPort=ctTransRifDbCtrlPort, ctTransNovellCfg=ctTransNovellCfg, ctTransIbmLlcOtherMode=ctTransIbmLlcOtherMode, ctTransFddiEthernetAuto=ctTransFddiEthernetAuto, ctTransEthernetFddi=ctTransEthernetFddi, ctTransIPArpCfgMode=ctTransIPArpCfgMode, ctTransIPDataCfgMode=ctTransIPDataCfgMode, ctTransSRAutoRingNumberDetect=ctTransSRAutoRingNumberDetect, ctTransA2CfgTable=ctTransA2CfgTable, ctTransA2McastCfgMode=ctTransA2McastCfgMode, ctTransOtherTable=ctTransOtherTable, ctTransA2CfgPort=ctTransA2CfgPort, ctTransOtherSapDsap2Val=ctTransOtherSapDsap2Val, ctTransOtherSnap1Val=ctTransOtherSnap1Val, ctTransFddiEthernetIPFrag=ctTransFddiEthernetIPFrag, ctTransOtherUnknownSap=ctTransOtherUnknownSap, ctTransSr=ctTransSr, ctTransRifDbCtrlEntry=ctTransRifDbCtrlEntry, ctTransOtherPort=ctTransOtherPort, ctTransIbmLlcEntry=ctTransIbmLlcEntry, ctTransSrSNA=ctTransSrSNA, ctTransEthernetFddiRAW=ctTransEthernetFddiRAW, ctTransIbmLlcPort=ctTransIbmLlcPort, ctTransFddiSnapEthernetType=ctTransFddiSnapEthernetType, ctTransRifDbSrcPort=ctTransRifDbSrcPort, ctTransSrSRLF=ctTransSrSRLF, ctTransA2CfgEntry=ctTransA2CfgEntry, ctTransNovellCfgPort=ctTransNovellCfgPort, ctTransIbmLlcNbMode=ctTransIbmLlcNbMode, ctTransA2ArpCfgMode=ctTransA2ArpCfgMode, ctTransIbmLlcLnmMode=ctTransIbmLlcLnmMode, ctTransSrPort=ctTransSrPort, ctTransOtherSapDsap3Mode=ctTransOtherSapDsap3Mode, ctTransBcastXEntry=ctTransBcastXEntry, ctTransIbmLlcOtherValue=ctTransIbmLlcOtherValue, ctTransNovellCfgEntry=ctTransNovellCfgEntry, ctTransNovellCfgMode=ctTransNovellCfgMode, ctTransBcastXTable=ctTransBcastXTable)
