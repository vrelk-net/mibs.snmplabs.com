#
# PySNMP MIB module CISCO-LWAPP-WAPI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-LWAPP-WAPI-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:49:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
cLApSysMacAddress, = mibBuilder.importSymbols("CISCO-LWAPP-AP-MIB", "cLApSysMacAddress")
cldcClientMacAddress, = mibBuilder.importSymbols("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress")
CLSecKeyFormat, = mibBuilder.importSymbols("CISCO-LWAPP-TC-MIB", "CLSecKeyFormat")
cLWlanIndex, = mibBuilder.importSymbols("CISCO-LWAPP-WLAN-MIB", "cLWlanIndex")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, iso, MibIdentifier, Gauge32, Counter64, IpAddress, Bits, TimeTicks, Unsigned32, Counter32, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "MibIdentifier", "Gauge32", "Counter64", "IpAddress", "Bits", "TimeTicks", "Unsigned32", "Counter32", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity")
TruthValue, MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "MacAddress", "TextualConvention", "DisplayString")
ciscoLwappWapiMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 9997))
ciscoLwappWapiMIB.setRevisions(('2010-12-18 00:00',))
if mibBuilder.loadTexts: ciscoLwappWapiMIB.setLastUpdated('201005230000Z')
if mibBuilder.loadTexts: ciscoLwappWapiMIB.setOrganization('Cisco Systems, Inc.')
ciscoLwappWapiMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1))
cLWapiWlanStats = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 1), )
if mibBuilder.loadTexts: cLWapiWlanStats.setStatus('current')
cLWapiWlanStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 1, 1), ).setIndexNames((0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"))
if mibBuilder.loadTexts: cLWapiWlanStatsEntry.setStatus('current')
cLWWSWAISignatureErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLWWSWAISignatureErrors.setStatus('current')
cLWWSWAIHMACErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLWWSWAIHMACErrors.setStatus('current')
cLWWSWAIAuthResultFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLWWSWAIAuthResultFailures.setStatus('current')
cLWWSWAIDiscardCounters = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLWWSWAIDiscardCounters.setStatus('current')
cLWWSWAITimeoutCounters = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLWWSWAITimeoutCounters.setStatus('current')
cLWWSWAIFormatErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLWWSWAIFormatErrors.setStatus('current')
cLWWSWAICertHandshakeFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLWWSWAICertHandshakeFailures.setStatus('current')
cLWWSWAIUnicastHandshakeFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLWWSWAIUnicastHandshakeFailures.setStatus('current')
cLWWSWAIMulticastHandshakeFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLWWSWAIMulticastHandshakeFailures.setStatus('current')
cLWWSWPIRXReplayCounters = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLWWSWPIRXReplayCounters.setStatus('current')
cLWWSWPIRXMicErrorCounters = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLWWSWPIRXMicErrorCounters.setStatus('current')
cLWWSWPIRXDecryptErrorCounters = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLWWSWPIRXDecryptErrorCounters.setStatus('current')
cLWapiClientStats = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 2), )
if mibBuilder.loadTexts: cLWapiClientStats.setStatus('current')
cLWapiClientStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 2, 1), ).setIndexNames((0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"))
if mibBuilder.loadTexts: cLWapiClientStatsEntry.setStatus('current')
cLWCSWapiClientVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLWCSWapiClientVersion.setStatus('current')
cLWCSWAISignatureErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLWCSWAISignatureErrors.setStatus('current')
cLWCSWAIHMACErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLWCSWAIHMACErrors.setStatus('current')
cLWCSWAIAuthResultFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLWCSWAIAuthResultFailures.setStatus('current')
cLWCSWAIDiscardCounters = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLWCSWAIDiscardCounters.setStatus('current')
cLWCSWAITimeoutCounters = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLWCSWAITimeoutCounters.setStatus('current')
cLWCSWAIFormatErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLWCSWAIFormatErrors.setStatus('current')
cLWCSWAICertHandshakeFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLWCSWAICertHandshakeFailures.setStatus('current')
cLWCSWAIUnicastHandshakeFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLWCSWAIUnicastHandshakeFailures.setStatus('current')
cLWCSWAIMulticastHandshakeFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLWCSWAIMulticastHandshakeFailures.setStatus('current')
cLWCSWAIUnicastCipherSuite = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 2, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLWCSWAIUnicastCipherSuite.setStatus('current')
cLWCSWAIMcastCipherSuite = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 2, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLWCSWAIMcastCipherSuite.setStatus('current')
cLWCSWAIAuthenticationSuiteRequested = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 2, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLWCSWAIAuthenticationSuiteRequested.setStatus('current')
cLWCSWAIBKIDUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 2, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLWCSWAIBKIDUsed.setStatus('current')
cLWCSWAICtrPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 2, 1, 15), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLWCSWAICtrPortState.setStatus('current')
cLWapiWlanConfig = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 3), )
if mibBuilder.loadTexts: cLWapiWlanConfig.setStatus('current')
cLWapiWlanConfigEntrty = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 3, 1), ).setIndexNames((0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"))
if mibBuilder.loadTexts: cLWapiWlanConfigEntrty.setStatus('current')
cLWCSWlanWapiEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 3, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLWCSWlanWapiEnable.setStatus('current')
cLWCSWlanWapiAkmKeyMgmtMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("invalid", 0), ("cert", 1), ("psk", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLWCSWlanWapiAkmKeyMgmtMode.setStatus('current')
cLWCSWlanWapiEncryptType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 3, 1, 3), Bits().clone(namedValues=NamedValues(("sms4", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLWCSWlanWapiEncryptType.setStatus('current')
cLWCSWlanWapiPskFmt = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 3, 1, 4), CLSecKeyFormat().clone('default')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLWCSWlanWapiPskFmt.setStatus('current')
cLWCSWlanWapiPsk = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 3, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLWCSWlanWapiPsk.setStatus('current')
cLWCSWlanWapiConfigUnicasCiphersEntry = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 3, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLWCSWlanWapiConfigUnicasCiphersEntry.setStatus('current')
cLWCSWlanWapiConfigUnicastCipherSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 3, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLWCSWlanWapiConfigUnicastCipherSize.setStatus('current')
cLWCSWlanWapiMcastCipherSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 3, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLWCSWlanWapiMcastCipherSize.setStatus('current')
cLWCSWlanBKLifeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 3, 1, 9), Unsigned32().clone(43200)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLWCSWlanBKLifeTime.setStatus('current')
cLWCSWlanBKReauthThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 3, 1, 10), Unsigned32().clone(70)).setUnits('percentage').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLWCSWlanBKReauthThreshold.setStatus('current')
cLWCSWlanWapiConfigMulticastCipher = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 3, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLWCSWlanWapiConfigMulticastCipher.setStatus('current')
cLWCSWlanWapiAuthenticationSuiteSelected = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 3, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLWCSWlanWapiAuthenticationSuiteSelected.setStatus('current')
cLWCSWlanWapiUnicastCipherSelected = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 3, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLWCSWlanWapiUnicastCipherSelected.setStatus('current')
cLWCSWlanWapiMulticastCipherSelected = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 3, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLWCSWlanWapiMulticastCipherSelected.setStatus('current')
cLWCSWlanWapiPreauthenticationState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 3, 1, 15), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLWCSWlanWapiPreauthenticationState.setStatus('current')
cLWapiAPTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 4), )
if mibBuilder.loadTexts: cLWapiAPTable.setStatus('current')
cLWapiAPEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 4, 1), ).setIndexNames((0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"))
if mibBuilder.loadTexts: cLWapiAPEntry.setStatus('current')
cLWCSWapiAPMaxUnicastKeysSupport = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLWCSWapiAPMaxUnicastKeysSupport.setStatus('current')
cLWapiWlanAKMSuitesConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 5), )
if mibBuilder.loadTexts: cLWapiWlanAKMSuitesConfigTable.setStatus('current')
cLWapiWlanAKMSuitesConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 5, 1), ).setIndexNames((0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"), (0, "CISCO-LWAPP-WAPI-MIB", "cLWCSWlanWapiAuthenticationSuiteIndex"))
if mibBuilder.loadTexts: cLWapiWlanAKMSuitesConfigEntry.setStatus('current')
cLWCSWlanWapiAuthenticationSuiteIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("cert", 1), ("psk", 2))))
if mibBuilder.loadTexts: cLWCSWlanWapiAuthenticationSuiteIndex.setStatus('current')
cLWCSWlanWapiAuthenticationSuite = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 5, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLWCSWlanWapiAuthenticationSuite.setStatus('current')
cLWCSWlanWapiAuthenticationSuiteEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 5, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLWCSWlanWapiAuthenticationSuiteEnable.setStatus('current')
cLWapiCiphers = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 6), )
if mibBuilder.loadTexts: cLWapiCiphers.setStatus('current')
cLWapiCiphersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 6, 1), ).setIndexNames((0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"), (0, "CISCO-LWAPP-WAPI-MIB", "cLWCSWlanCipherIndex"))
if mibBuilder.loadTexts: cLWapiCiphersEntry.setStatus('current')
cLWCSWlanCipherIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 6, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cLWCSWlanCipherIndex.setStatus('current')
cLWCSWlanCipherEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 6, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLWCSWlanCipherEnabled.setStatus('current')
ciscoLwappWapiConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9997, 2))
clWapiASIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9997, 2, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clWapiASIpAddress.setStatus('current')
clWapiASPortNumber = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9997, 2, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clWapiASPortNumber.setStatus('current')
clWapiASRequestTimeout = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9997, 2, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clWapiASRequestTimeout.setStatus('current')
clWapiMulticastRekeyMethod = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9997, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("disabled", 1), ("timeBased", 2), ("messageBased", 3), ("timemessageBased", 4))).clone('timeBased')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clWapiMulticastRekeyMethod.setStatus('current')
clWapiMulticastRekeyTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9997, 2, 5), Unsigned32().clone(86400)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: clWapiMulticastRekeyTime.setStatus('current')
clWapiMulticastRekeyMessages = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9997, 2, 6), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clWapiMulticastRekeyMessages.setStatus('current')
clWapiMulticastRekeyStrict = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9997, 2, 7), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clWapiMulticastRekeyStrict.setStatus('current')
clWapiConfigCertificateUpdateCount = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9997, 2, 8), Unsigned32().clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clWapiConfigCertificateUpdateCount.setStatus('current')
clWapiConfigMulticastUpdateCount = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9997, 2, 9), Unsigned32().clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clWapiConfigMulticastUpdateCount.setStatus('current')
clWapiConfigUnicastUpdateCount = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9997, 2, 10), Unsigned32().clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clWapiConfigUnicastUpdateCount.setStatus('current')
cLWCSWapiConfigureVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9997, 2, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLWCSWapiConfigureVersion.setStatus('current')
clWapiConfigControlledPortControl = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9997, 2, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0))).clone(namedValues=NamedValues(("auto", 0)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clWapiConfigControlledPortControl.setStatus('current')
clWapiUserInvalidCertificationInbreakNetwork = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9997, 2, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clWapiUserInvalidCertificationInbreakNetwork.setStatus('current')
cLApWAPISecurityLowAttack = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9997, 2, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLApWAPISecurityLowAttack.setStatus('current')
clWapiUnicastRekeyMethod = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9997, 2, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("disabled", 1), ("timeBased", 2), ("messageBased", 3), ("timeMessageBased", 4))).clone('timeBased')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clWapiUnicastRekeyMethod.setStatus('current')
clWapiUnicastRekeyTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9997, 2, 16), Unsigned32().clone(86400)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: clWapiUnicastRekeyTime.setStatus('current')
clWapiUnicastRekeyMessage = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9997, 2, 17), Unsigned32()).setUnits('1000 messages').setMaxAccess("readwrite")
if mibBuilder.loadTexts: clWapiUnicastRekeyMessage.setStatus('current')
clWapiConfigSATimeout = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9997, 2, 18), Unsigned32().clone(60)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: clWapiConfigSATimeout.setStatus('current')
cLApWAPIReplayAttack = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9997, 2, 19), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLApWAPIReplayAttack.setStatus('current')
cLApWAPITamperAttack = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9997, 2, 20), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLApWAPITamperAttack.setStatus('current')
clWapiAddressRedirectAttack = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9997, 2, 21), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clWapiAddressRedirectAttack.setStatus('current')
ciscoLwappWapiCertificateObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9997, 3))
clWapiWLCCertificateStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9997, 3, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clWapiWLCCertificateStatus.setStatus('current')
clWapiCACertificateStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9997, 3, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clWapiCACertificateStatus.setStatus('current')
clWapiASCertificateStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9997, 3, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clWapiASCertificateStatus.setStatus('current')
ciscoLwappWapiMIBNotifObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9997, 4))
ciscoLwappWapiUserInvalidCertificateNetworkTrap = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 9997, 4, 1)).setObjects(("CISCO-LWAPP-WAPI-MIB", "clWapiUserInvalidCertificationInbreakNetwork"))
if mibBuilder.loadTexts: ciscoLwappWapiUserInvalidCertificateNetworkTrap.setStatus('current')
ciscoLwappWapiSecurityLowAttackTrap = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 9997, 4, 2)).setObjects(("CISCO-LWAPP-WAPI-MIB", "cLApWAPISecurityLowAttack"))
if mibBuilder.loadTexts: ciscoLwappWapiSecurityLowAttackTrap.setStatus('current')
ciscoLwappWapiReplayAttackTrap = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 9997, 4, 3)).setObjects(("CISCO-LWAPP-WAPI-MIB", "cLApWAPIReplayAttack"))
if mibBuilder.loadTexts: ciscoLwappWapiReplayAttackTrap.setStatus('current')
ciscoLwappWapiTamperAttackTrap = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 9997, 4, 4)).setObjects(("CISCO-LWAPP-WAPI-MIB", "cLApWAPITamperAttack"))
if mibBuilder.loadTexts: ciscoLwappWapiTamperAttackTrap.setStatus('current')
ciscoLwappWapiAddressRedirectAttackTrap = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 9997, 4, 5)).setObjects(("CISCO-LWAPP-WAPI-MIB", "clWapiAddressRedirectAttack"))
if mibBuilder.loadTexts: ciscoLwappWapiAddressRedirectAttackTrap.setStatus('current')
mibBuilder.exportSymbols("CISCO-LWAPP-WAPI-MIB", cLWCSWapiConfigureVersion=cLWCSWapiConfigureVersion, cLWapiWlanAKMSuitesConfigTable=cLWapiWlanAKMSuitesConfigTable, ciscoLwappWapiConfig=ciscoLwappWapiConfig, cLWWSWAIDiscardCounters=cLWWSWAIDiscardCounters, cLWWSWPIRXDecryptErrorCounters=cLWWSWPIRXDecryptErrorCounters, cLWapiAPTable=cLWapiAPTable, clWapiASCertificateStatus=clWapiASCertificateStatus, cLWWSWAIFormatErrors=cLWWSWAIFormatErrors, cLWCSWlanWapiUnicastCipherSelected=cLWCSWlanWapiUnicastCipherSelected, cLWCSWAITimeoutCounters=cLWCSWAITimeoutCounters, cLApWAPITamperAttack=cLApWAPITamperAttack, cLWapiClientStats=cLWapiClientStats, cLWCSWAIAuthenticationSuiteRequested=cLWCSWAIAuthenticationSuiteRequested, cLWCSWAICtrPortState=cLWCSWAICtrPortState, ciscoLwappWapiMIBNotifObjects=ciscoLwappWapiMIBNotifObjects, cLWCSWlanWapiMcastCipherSize=cLWCSWlanWapiMcastCipherSize, cLWWSWAIAuthResultFailures=cLWWSWAIAuthResultFailures, cLWCSWAICertHandshakeFailures=cLWCSWAICertHandshakeFailures, cLWWSWAISignatureErrors=cLWWSWAISignatureErrors, clWapiUnicastRekeyMethod=clWapiUnicastRekeyMethod, cLWCSWlanWapiPsk=cLWCSWlanWapiPsk, ciscoLwappWapiSecurityLowAttackTrap=ciscoLwappWapiSecurityLowAttackTrap, cLWapiWlanStats=cLWapiWlanStats, cLWCSWAIMcastCipherSuite=cLWCSWAIMcastCipherSuite, cLWCSWlanWapiAuthenticationSuite=cLWCSWlanWapiAuthenticationSuite, cLWCSWlanWapiAuthenticationSuiteEnable=cLWCSWlanWapiAuthenticationSuiteEnable, ciscoLwappWapiReplayAttackTrap=ciscoLwappWapiReplayAttackTrap, cLWapiWlanStatsEntry=cLWapiWlanStatsEntry, clWapiAddressRedirectAttack=clWapiAddressRedirectAttack, cLWCSWAIHMACErrors=cLWCSWAIHMACErrors, ciscoLwappWapiUserInvalidCertificateNetworkTrap=ciscoLwappWapiUserInvalidCertificateNetworkTrap, cLWCSWlanWapiPskFmt=cLWCSWlanWapiPskFmt, clWapiConfigMulticastUpdateCount=clWapiConfigMulticastUpdateCount, cLWapiAPEntry=cLWapiAPEntry, ciscoLwappWapiMIB=ciscoLwappWapiMIB, cLWCSWlanWapiMulticastCipherSelected=cLWCSWlanWapiMulticastCipherSelected, clWapiUnicastRekeyTime=clWapiUnicastRekeyTime, clWapiASRequestTimeout=clWapiASRequestTimeout, cLWCSWlanBKLifeTime=cLWCSWlanBKLifeTime, cLWCSWlanWapiConfigUnicastCipherSize=cLWCSWlanWapiConfigUnicastCipherSize, cLWCSWAIBKIDUsed=cLWCSWAIBKIDUsed, PYSNMP_MODULE_ID=ciscoLwappWapiMIB, cLWCSWlanWapiAuthenticationSuiteIndex=cLWCSWlanWapiAuthenticationSuiteIndex, cLWCSWAIAuthResultFailures=cLWCSWAIAuthResultFailures, cLWWSWPIRXReplayCounters=cLWWSWPIRXReplayCounters, cLWWSWPIRXMicErrorCounters=cLWWSWPIRXMicErrorCounters, clWapiConfigControlledPortControl=clWapiConfigControlledPortControl, cLWCSWAIDiscardCounters=cLWCSWAIDiscardCounters, clWapiASIpAddress=clWapiASIpAddress, cLWCSWlanBKReauthThreshold=cLWCSWlanBKReauthThreshold, clWapiASPortNumber=clWapiASPortNumber, cLWWSWAIUnicastHandshakeFailures=cLWWSWAIUnicastHandshakeFailures, clWapiMulticastRekeyTime=clWapiMulticastRekeyTime, cLApWAPIReplayAttack=cLApWAPIReplayAttack, cLWCSWAIFormatErrors=cLWCSWAIFormatErrors, cLWCSWlanWapiConfigMulticastCipher=cLWCSWlanWapiConfigMulticastCipher, clWapiUnicastRekeyMessage=clWapiUnicastRekeyMessage, cLWCSWapiClientVersion=cLWCSWapiClientVersion, cLWCSWlanWapiPreauthenticationState=cLWCSWlanWapiPreauthenticationState, cLWCSWAISignatureErrors=cLWCSWAISignatureErrors, cLWWSWAIMulticastHandshakeFailures=cLWWSWAIMulticastHandshakeFailures, cLWapiWlanConfig=cLWapiWlanConfig, cLWCSWlanWapiConfigUnicasCiphersEntry=cLWCSWlanWapiConfigUnicasCiphersEntry, clWapiMulticastRekeyMethod=clWapiMulticastRekeyMethod, cLWapiCiphers=cLWapiCiphers, cLWWSWAICertHandshakeFailures=cLWWSWAICertHandshakeFailures, clWapiUserInvalidCertificationInbreakNetwork=clWapiUserInvalidCertificationInbreakNetwork, ciscoLwappWapiTamperAttackTrap=ciscoLwappWapiTamperAttackTrap, ciscoLwappWapiAddressRedirectAttackTrap=ciscoLwappWapiAddressRedirectAttackTrap, clWapiConfigSATimeout=clWapiConfigSATimeout, cLWCSWAIMulticastHandshakeFailures=cLWCSWAIMulticastHandshakeFailures, clWapiConfigCertificateUpdateCount=clWapiConfigCertificateUpdateCount, clWapiMulticastRekeyMessages=clWapiMulticastRekeyMessages, ciscoLwappWapiMIBObjects=ciscoLwappWapiMIBObjects, clWapiCACertificateStatus=clWapiCACertificateStatus, clWapiWLCCertificateStatus=clWapiWLCCertificateStatus, cLWWSWAIHMACErrors=cLWWSWAIHMACErrors, cLWCSWlanWapiAuthenticationSuiteSelected=cLWCSWlanWapiAuthenticationSuiteSelected, cLWapiCiphersEntry=cLWapiCiphersEntry, cLWapiClientStatsEntry=cLWapiClientStatsEntry, cLWCSWlanWapiEncryptType=cLWCSWlanWapiEncryptType, cLWCSWapiAPMaxUnicastKeysSupport=cLWCSWapiAPMaxUnicastKeysSupport, cLWCSWAIUnicastCipherSuite=cLWCSWAIUnicastCipherSuite, cLWapiWlanConfigEntrty=cLWapiWlanConfigEntrty, cLWCSWlanWapiAkmKeyMgmtMode=cLWCSWlanWapiAkmKeyMgmtMode, cLWCSWlanWapiEnable=cLWCSWlanWapiEnable, cLWCSWAIUnicastHandshakeFailures=cLWCSWAIUnicastHandshakeFailures, cLWCSWlanCipherEnabled=cLWCSWlanCipherEnabled, clWapiConfigUnicastUpdateCount=clWapiConfigUnicastUpdateCount, cLWCSWlanCipherIndex=cLWCSWlanCipherIndex, ciscoLwappWapiCertificateObjects=ciscoLwappWapiCertificateObjects, cLWapiWlanAKMSuitesConfigEntry=cLWapiWlanAKMSuitesConfigEntry, cLApWAPISecurityLowAttack=cLApWAPISecurityLowAttack, clWapiMulticastRekeyStrict=clWapiMulticastRekeyStrict, cLWWSWAITimeoutCounters=cLWWSWAITimeoutCounters)