#
# PySNMP MIB module REDLINE-AN80I-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/REDLINE-AN80I-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:46:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
InetAddressType, InetPortNumber, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetPortNumber", "InetAddress")
redlineSystem, = mibBuilder.importSymbols("REDLINE-MIB", "redlineSystem")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Integer32, Gauge32, Counter64, ObjectIdentity, MibIdentifier, NotificationType, IpAddress, Bits, TimeTicks, ModuleIdentity, iso, Counter32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "Counter64", "ObjectIdentity", "MibIdentifier", "NotificationType", "IpAddress", "Bits", "TimeTicks", "ModuleIdentity", "iso", "Counter32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
redlineAn80iMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3))
redlineAn80iMib.setRevisions(('2005-11-29 15:43',))
if mibBuilder.loadTexts: redlineAn80iMib.setLastUpdated('200511291543Z')
if mibBuilder.loadTexts: redlineAn80iMib.setOrganization('Redline Communications Inc.')
redlineAn80iPtpPmpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1))
redlineAn80iSystemObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 1))
an80iOptionsKeyTable = MibTable((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 1, 1), )
if mibBuilder.loadTexts: an80iOptionsKeyTable.setStatus('current')
an80iOptionsKeyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 1, 1, 1), ).setIndexNames((0, "REDLINE-AN80I-MIB", "an80iOptionsKeyId"))
if mibBuilder.loadTexts: an80iOptionsKeyEntry.setStatus('current')
an80iOptionsKeyId = MibTableColumn((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2)))
if mibBuilder.loadTexts: an80iOptionsKeyId.setStatus('current')
an80iOptionsKey = MibTableColumn((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: an80iOptionsKey.setStatus('current')
an80iOptionsKeyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: an80iOptionsKeyStatus.setStatus('current')
an80iHardwareType = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: an80iHardwareType.setStatus('current')
an80iRadioType = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: an80iRadioType.setStatus('current')
an80iSaveConfig = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noop", 1), ("saveConfig", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iSaveConfig.setStatus('current')
an80iActivateConfig = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noop", 1), ("activeConfig", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iActivateConfig.setStatus('current')
redlineAn80iWirelesObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2))
an80iAntennaAllignmentMode = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("buzzer", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iAntennaAllignmentMode.setStatus('current')
an80iCurrTxPower = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-10, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: an80iCurrTxPower.setStatus('current')
an80iChannelAutoScan = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iChannelAutoScan.setStatus('current')
an80iCurrFrequency = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2, 4), Integer32()).setUnits('KHz').setMaxAccess("readonly")
if mibBuilder.loadTexts: an80iCurrFrequency.setStatus('current')
an80iOPeratingFrequency = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2, 5), Integer32()).setUnits('KHz').setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iOPeratingFrequency.setStatus('current')
an80iMaxTxPower = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-20, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iMaxTxPower.setStatus('current')
an80iSystemMode = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ptpSlave", 1), ("ptpMaster", 2), ("pmpSlave", 3), ("pmpMaster", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iSystemMode.setStatus('current')
an80iRFStatusCode = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: an80iRFStatusCode.setStatus('current')
an80iDFSAction = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("txDisabled", 2), ("changeFreq", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iDFSAction.setStatus('current')
an80iAntennaGain = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iAntennaGain.setStatus('current')
an80iActiveRFLinks = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: an80iActiveRFLinks.setStatus('current')
an80iAtpControl = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iAtpControl.setStatus('current')
an80iTurboModeControl = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iTurboModeControl.setStatus('current')
an80iChannelWidth = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 2, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(7, 6, 5))).clone(namedValues=NamedValues(("chWidth40MHz", 7), ("chWidth20MHz", 6), ("chWidth10MHz", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iChannelWidth.setStatus('current')
redlineAn80iEthernetObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 3))
an80iEtherPortConn = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("auto", 1), ("normal", 2), ("crossover", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iEtherPortConn.setStatus('current')
an80iEtherPortMode = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("auto", 1), ("e10hd", 2), ("e10fd", 3), ("e100hd", 4), ("e100fd", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iEtherPortMode.setStatus('current')
an80iFlowControl = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iFlowControl.setStatus('current')
an80iLowLatencyMode = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iLowLatencyMode.setStatus('current')
an80iEthernetFollowsWireless = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 3, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iEthernetFollowsWireless.setStatus('current')
an80iEthernetFollowsWirelessTimeout = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 3, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iEthernetFollowsWirelessTimeout.setStatus('current')
redlineAn80iManagObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 4))
an80iHttpAccess = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iHttpAccess.setStatus('current')
an80iTelnetAccess = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iTelnetAccess.setStatus('current')
an80iTelnetPort = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 4, 3), InetPortNumber()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iTelnetPort.setStatus('current')
redlineAn80iSWUpgradeObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 5))
an80iSwDownloadTftpAddressType = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 5, 1), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iSwDownloadTftpAddressType.setStatus('current')
an80iSwDownloadTftpAddress = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 5, 2), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iSwDownloadTftpAddress.setStatus('current')
an80iSwDownloadTftpFile = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 5, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iSwDownloadTftpFile.setStatus('current')
an80iSwDownloadStatus = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 5, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("download", 1), ("inProgress", 2), ("success", 3), ("failed", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: an80iSwDownloadStatus.setStatus('current')
an80iSwDownloadControl = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 1, 5, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noop", 1), ("startUpgrade", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iSwDownloadControl.setStatus('current')
redlineAn80iPmpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 2))
redlineAn80iPmpWirelesObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 2, 1))
an80iRegistrationPeriod = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iRegistrationPeriod.setStatus('current')
an80iMaximumDistance = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iMaximumDistance.setStatus('current')
an80iRegisteredStations = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: an80iRegisteredStations.setStatus('current')
an80iRegisteredConnections = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: an80iRegisteredConnections.setStatus('current')
an80iMaxId = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1023))).setMaxAccess("readonly")
if mibBuilder.loadTexts: an80iMaxId.setStatus('current')
an80iNextAvailId = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: an80iNextAvailId.setStatus('current')
an80iLastModifId = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: an80iLastModifId.setStatus('current')
an80iSaveIdConfiguration = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noop", 1), ("save", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iSaveIdConfiguration.setStatus('current')
redlineAn80iPtpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 3))
redlineAn80iPtpSystemObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 3, 1))
an80iResetStatistics = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noop", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: an80iResetStatistics.setStatus('current')
redlineAn80iTrapDefinitions = MibIdentifier((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 0))
an80iPswdChangeFailTrap = NotificationType((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 0, 1))
if mibBuilder.loadTexts: an80iPswdChangeFailTrap.setStatus('current')
an80iFirmwareConfigFailTrap = NotificationType((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 0, 2))
if mibBuilder.loadTexts: an80iFirmwareConfigFailTrap.setStatus('current')
an80iEepromCorruptedTrap = NotificationType((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 0, 3))
if mibBuilder.loadTexts: an80iEepromCorruptedTrap.setStatus('current')
an80iHardwareFailTrap = NotificationType((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 0, 4))
if mibBuilder.loadTexts: an80iHardwareFailTrap.setStatus('current')
an80iSaveConfigTrap = NotificationType((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 0, 5))
if mibBuilder.loadTexts: an80iSaveConfigTrap.setStatus('current')
an80iDFSEventTrap = NotificationType((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 0, 6))
if mibBuilder.loadTexts: an80iDFSEventTrap.setStatus('current')
an80iIdChangedTrap = NotificationType((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 0, 7)).setObjects(("REDLINE-AN80I-MIB", "an80iLastModifId"))
if mibBuilder.loadTexts: an80iIdChangedTrap.setStatus('current')
an80iSWUpgradeFailed = NotificationType((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 0, 8)).setObjects(("REDLINE-AN80I-MIB", "an80iSwDownloadTftpAddressType"), ("REDLINE-AN80I-MIB", "an80iSwDownloadTftpAddress"), ("REDLINE-AN80I-MIB", "an80iSwDownloadTftpFile"))
if mibBuilder.loadTexts: an80iSWUpgradeFailed.setStatus('current')
an80iSWUpgradeSuccess = NotificationType((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 0, 9)).setObjects(("REDLINE-AN80I-MIB", "an80iSwDownloadTftpAddressType"), ("REDLINE-AN80I-MIB", "an80iSwDownloadTftpAddress"), ("REDLINE-AN80I-MIB", "an80iSwDownloadTftpFile"))
if mibBuilder.loadTexts: an80iSWUpgradeSuccess.setStatus('current')
redlineAn80iConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 5))
redlineAn80iGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 5, 1))
redlineAn80iCompls = MibIdentifier((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 5, 2))
redlineAn80iPtpPmpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 5, 1, 1)).setObjects(("REDLINE-AN80I-MIB", "an80iOptionsKey"), ("REDLINE-AN80I-MIB", "an80iHardwareType"), ("REDLINE-AN80I-MIB", "an80iRadioType"), ("REDLINE-AN80I-MIB", "an80iSaveConfig"), ("REDLINE-AN80I-MIB", "an80iActivateConfig"), ("REDLINE-AN80I-MIB", "an80iAntennaAllignmentMode"), ("REDLINE-AN80I-MIB", "an80iCurrTxPower"), ("REDLINE-AN80I-MIB", "an80iChannelAutoScan"), ("REDLINE-AN80I-MIB", "an80iCurrFrequency"), ("REDLINE-AN80I-MIB", "an80iOPeratingFrequency"), ("REDLINE-AN80I-MIB", "an80iMaxTxPower"), ("REDLINE-AN80I-MIB", "an80iSystemMode"), ("REDLINE-AN80I-MIB", "an80iRFStatusCode"), ("REDLINE-AN80I-MIB", "an80iDFSAction"), ("REDLINE-AN80I-MIB", "an80iAntennaGain"), ("REDLINE-AN80I-MIB", "an80iActiveRFLinks"), ("REDLINE-AN80I-MIB", "an80iAtpControl"), ("REDLINE-AN80I-MIB", "an80iTurboModeControl"), ("REDLINE-AN80I-MIB", "an80iEtherPortConn"), ("REDLINE-AN80I-MIB", "an80iEtherPortMode"), ("REDLINE-AN80I-MIB", "an80iFlowControl"), ("REDLINE-AN80I-MIB", "an80iLowLatencyMode"), ("REDLINE-AN80I-MIB", "an80iEthernetFollowsWireless"), ("REDLINE-AN80I-MIB", "an80iEthernetFollowsWirelessTimeout"), ("REDLINE-AN80I-MIB", "an80iHttpAccess"), ("REDLINE-AN80I-MIB", "an80iTelnetAccess"), ("REDLINE-AN80I-MIB", "an80iTelnetPort"), ("REDLINE-AN80I-MIB", "an80iSwDownloadTftpAddressType"), ("REDLINE-AN80I-MIB", "an80iSwDownloadTftpAddress"), ("REDLINE-AN80I-MIB", "an80iSwDownloadTftpFile"), ("REDLINE-AN80I-MIB", "an80iSwDownloadStatus"), ("REDLINE-AN80I-MIB", "an80iSwDownloadControl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    redlineAn80iPtpPmpGroup = redlineAn80iPtpPmpGroup.setStatus('current')
redlineAn80iPmpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 5, 1, 2)).setObjects(("REDLINE-AN80I-MIB", "an80iRegistrationPeriod"), ("REDLINE-AN80I-MIB", "an80iMaximumDistance"), ("REDLINE-AN80I-MIB", "an80iRegisteredStations"), ("REDLINE-AN80I-MIB", "an80iRegisteredConnections"), ("REDLINE-AN80I-MIB", "an80iMaxId"), ("REDLINE-AN80I-MIB", "an80iNextAvailId"), ("REDLINE-AN80I-MIB", "an80iLastModifId"), ("REDLINE-AN80I-MIB", "an80iSaveIdConfiguration"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    redlineAn80iPmpGroup = redlineAn80iPmpGroup.setStatus('current')
redlineAn80iPtpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 5, 1, 3)).setObjects(("REDLINE-AN80I-MIB", "an80iResetStatistics"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    redlineAn80iPtpGroup = redlineAn80iPtpGroup.setStatus('current')
redlineAn80iNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 5, 1, 4)).setObjects(("REDLINE-AN80I-MIB", "an80iPswdChangeFailTrap"), ("REDLINE-AN80I-MIB", "an80iFirmwareConfigFailTrap"), ("REDLINE-AN80I-MIB", "an80iEepromCorruptedTrap"), ("REDLINE-AN80I-MIB", "an80iHardwareFailTrap"), ("REDLINE-AN80I-MIB", "an80iSaveConfigTrap"), ("REDLINE-AN80I-MIB", "an80iDFSEventTrap"), ("REDLINE-AN80I-MIB", "an80iIdChangedTrap"), ("REDLINE-AN80I-MIB", "an80iSWUpgradeFailed"), ("REDLINE-AN80I-MIB", "an80iSWUpgradeSuccess"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    redlineAn80iNotificationGroup = redlineAn80iNotificationGroup.setStatus('current')
redlineAn80iCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 10728, 2, 1, 3, 5, 2, 1)).setObjects(("REDLINE-AN80I-MIB", "redlineAn80iPtpPmpGroup"), ("REDLINE-AN80I-MIB", "redlineAn80iPmpGroup"), ("REDLINE-AN80I-MIB", "redlineAn80iPtpGroup"), ("REDLINE-AN80I-MIB", "redlineAn80iNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    redlineAn80iCompliance = redlineAn80iCompliance.setStatus('current')
mibBuilder.exportSymbols("REDLINE-AN80I-MIB", PYSNMP_MODULE_ID=redlineAn80iMib, an80iChannelAutoScan=an80iChannelAutoScan, an80iFlowControl=an80iFlowControl, an80iCurrTxPower=an80iCurrTxPower, an80iOPeratingFrequency=an80iOPeratingFrequency, an80iMaxTxPower=an80iMaxTxPower, redlineAn80iSystemObjects=redlineAn80iSystemObjects, an80iDFSAction=an80iDFSAction, redlineAn80iPmpGroup=redlineAn80iPmpGroup, an80iMaximumDistance=an80iMaximumDistance, redlineAn80iCompliance=redlineAn80iCompliance, an80iOptionsKey=an80iOptionsKey, redlineAn80iConformance=redlineAn80iConformance, an80iTelnetAccess=an80iTelnetAccess, an80iAtpControl=an80iAtpControl, an80iSaveConfigTrap=an80iSaveConfigTrap, an80iIdChangedTrap=an80iIdChangedTrap, an80iOptionsKeyTable=an80iOptionsKeyTable, an80iEthernetFollowsWireless=an80iEthernetFollowsWireless, an80iHardwareFailTrap=an80iHardwareFailTrap, an80iEtherPortMode=an80iEtherPortMode, an80iChannelWidth=an80iChannelWidth, redlineAn80iPmpObjects=redlineAn80iPmpObjects, redlineAn80iPtpSystemObjects=redlineAn80iPtpSystemObjects, an80iActiveRFLinks=an80iActiveRFLinks, redlineAn80iPmpWirelesObjects=redlineAn80iPmpWirelesObjects, redlineAn80iNotificationGroup=redlineAn80iNotificationGroup, an80iRegistrationPeriod=an80iRegistrationPeriod, an80iHttpAccess=an80iHttpAccess, redlineAn80iGroups=redlineAn80iGroups, an80iEepromCorruptedTrap=an80iEepromCorruptedTrap, an80iAntennaAllignmentMode=an80iAntennaAllignmentMode, redlineAn80iPtpGroup=redlineAn80iPtpGroup, an80iSWUpgradeFailed=an80iSWUpgradeFailed, an80iTurboModeControl=an80iTurboModeControl, an80iRFStatusCode=an80iRFStatusCode, an80iRegisteredStations=an80iRegisteredStations, an80iLowLatencyMode=an80iLowLatencyMode, an80iOptionsKeyEntry=an80iOptionsKeyEntry, redlineAn80iWirelesObjects=redlineAn80iWirelesObjects, an80iNextAvailId=an80iNextAvailId, an80iDFSEventTrap=an80iDFSEventTrap, an80iCurrFrequency=an80iCurrFrequency, redlineAn80iCompls=redlineAn80iCompls, an80iLastModifId=an80iLastModifId, an80iSwDownloadStatus=an80iSwDownloadStatus, an80iPswdChangeFailTrap=an80iPswdChangeFailTrap, redlineAn80iPtpPmpGroup=redlineAn80iPtpPmpGroup, an80iResetStatistics=an80iResetStatistics, redlineAn80iPtpPmpObjects=redlineAn80iPtpPmpObjects, an80iOptionsKeyId=an80iOptionsKeyId, an80iSaveConfig=an80iSaveConfig, an80iEthernetFollowsWirelessTimeout=an80iEthernetFollowsWirelessTimeout, an80iMaxId=an80iMaxId, an80iSwDownloadTftpAddress=an80iSwDownloadTftpAddress, an80iSwDownloadControl=an80iSwDownloadControl, an80iAntennaGain=an80iAntennaGain, an80iTelnetPort=an80iTelnetPort, an80iRadioType=an80iRadioType, an80iFirmwareConfigFailTrap=an80iFirmwareConfigFailTrap, an80iActivateConfig=an80iActivateConfig, an80iOptionsKeyStatus=an80iOptionsKeyStatus, an80iSWUpgradeSuccess=an80iSWUpgradeSuccess, redlineAn80iEthernetObjects=redlineAn80iEthernetObjects, redlineAn80iSWUpgradeObjects=redlineAn80iSWUpgradeObjects, redlineAn80iPtpObjects=redlineAn80iPtpObjects, an80iHardwareType=an80iHardwareType, an80iRegisteredConnections=an80iRegisteredConnections, an80iSystemMode=an80iSystemMode, an80iSaveIdConfiguration=an80iSaveIdConfiguration, an80iSwDownloadTftpFile=an80iSwDownloadTftpFile, redlineAn80iManagObjects=redlineAn80iManagObjects, redlineAn80iTrapDefinitions=redlineAn80iTrapDefinitions, an80iSwDownloadTftpAddressType=an80iSwDownloadTftpAddressType, an80iEtherPortConn=an80iEtherPortConn, redlineAn80iMib=redlineAn80iMib)
