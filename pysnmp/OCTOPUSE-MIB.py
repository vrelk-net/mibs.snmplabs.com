#
# PySNMP MIB module OCTOPUSE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/OCTOPUSE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:22:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Gauge32, Unsigned32, Counter32, enterprises, MibIdentifier, TimeTicks, Integer32, Bits, Counter64, ObjectIdentity, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Gauge32", "Unsigned32", "Counter32", "enterprises", "MibIdentifier", "TimeTicks", "Integer32", "Bits", "Counter64", "ObjectIdentity", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sni = MibIdentifier((1, 3, 6, 1, 4, 1, 231))
siemensUnits = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 7))
pn = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 7, 2))
octopusE = ModuleIdentity((1, 3, 6, 1, 4, 1, 231, 7, 2, 9))
if mibBuilder.loadTexts: octopusE.setLastUpdated('24.11.00')
if mibBuilder.loadTexts: octopusE.setOrganization('Siemens Information & Communication Networks')
octoControlGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 1))
octoErrorHistoryGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2))
octoSystemInfoGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3))
octoStatisticsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 4))
octoCdrConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5))
octoTrapSpecifications = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 6))
octoNetworkGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 7))
class DisplayString(OctetString):
    pass

class DateAndTime(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2d-1d-1d,1d:1d:1d.1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class ReadWrite(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("readWrite", 1), ("readOnly", 2))

octoSysState = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("normal", 1), ("warning", 2), ("minor", 3), ("major", 4), ("critical", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: octoSysState.setStatus('current')
tftpSwitchoverDateTime = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 1, 2), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tftpSwitchoverDateTime.setStatus('current')
tftpDownloadAction = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("notDownloading", 1), ("downloadAndImmediateSwitchover", 2), ("downloadAndDelayedSwitchover", 3), ("downloadWithoutSwitchover", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tftpDownloadAction.setStatus('current')
octoResetControl = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("running", 1), ("warmBoot", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: octoResetControl.setStatus('current')
octoSwitchoverState = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("readyForSwitchover", 1), ("notReadyForSwitchover", 2), ("initSwitchoverNow", 3), ("initSwitchoverDelayed", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: octoSwitchoverState.setStatus('current')
octoShadowFlashState = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("flashDeleted", 1), ("flashNotDeleted", 2), ("flashWriteProtected", 3), ("flashTooSmall", 4), ("deleteFlashNow", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: octoShadowFlashState.setStatus('current')
octoLoadLevel = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: octoLoadLevel.setStatus('current')
octoTrapRepetitions = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: octoTrapRepetitions.setStatus('current')
octoCdrBufferState = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("accounting", 1), ("deleteBufferNow", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: octoCdrBufferState.setStatus('current')
octoLogBufferState = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("logging", 1), ("deleteBufferNow", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: octoLogBufferState.setStatus('current')
numberOfErrorHistoryEntries = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483187))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: numberOfErrorHistoryEntries.setStatus('current')
octoErrorHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2, 2), )
if mibBuilder.loadTexts: octoErrorHistoryTable.setStatus('current')
octoErrorHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2, 2, 1), ).setIndexNames((0, "OCTOPUSE-MIB", "octoErrorIndex"))
if mibBuilder.loadTexts: octoErrorHistoryEntry.setStatus('current')
octoErrorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: octoErrorIndex.setStatus('current')
octoErrorDateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2, 2, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: octoErrorDateTime.setStatus('current')
octoErrorClass = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: octoErrorClass.setStatus('current')
octoErrorCode = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: octoErrorCode.setStatus('current')
octoAccessSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: octoAccessSlot.setStatus('current')
octoAccessPort = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: octoAccessPort.setStatus('current')
octoErrorDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: octoErrorDescription.setStatus('current')
octoErrorSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("normal", 1), ("warning", 2), ("minor", 3), ("major", 4), ("critical", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: octoErrorSeverity.setStatus('current')
sysHardwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 25))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysHardwareVersion.setStatus('current')
sysSoftwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 25))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysSoftwareVersion.setStatus('current')
sysCodeNumber = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 25))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysCodeNumber.setStatus('current')
sysSoftwareLocation = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("lower", 1), ("upper", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysSoftwareLocation.setStatus('current')
numberOfSlotTableEntries = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: numberOfSlotTableEntries.setStatus('current')
octoSlotTable = MibTable((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 6), )
if mibBuilder.loadTexts: octoSlotTable.setStatus('current')
octoSlotTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 6, 1), ).setIndexNames((0, "OCTOPUSE-MIB", "cardIndex"))
if mibBuilder.loadTexts: octoSlotTableEntry.setStatus('current')
cardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardIndex.setStatus('current')
cardBoxNum = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardBoxNum.setStatus('current')
cardSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 6, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardSlotNum.setStatus('current')
cardType = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 6, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardType.setStatus('current')
cardDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 6, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardDescription.setStatus('current')
cardCodeNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 6, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 25))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardCodeNumber.setStatus('current')
cardState = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 6, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("normal", 1), ("warning", 2), ("minor", 3), ("major", 4), ("critical", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardState.setStatus('current')
numberOfPortTableEntries = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: numberOfPortTableEntries.setStatus('current')
octoPortTable = MibTable((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 8), )
if mibBuilder.loadTexts: octoPortTable.setStatus('current')
octoPortTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 8, 1), ).setIndexNames((0, "OCTOPUSE-MIB", "portIndex"))
if mibBuilder.loadTexts: octoPortTableEntry.setStatus('current')
portIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portIndex.setStatus('current')
portCardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 8, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portCardIndex.setStatus('current')
portType = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 8, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portType.setStatus('current')
portState = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 8, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inactive", 1), ("active", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portState.setStatus('current')
portLock = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 8, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unlocked", 1), ("lockedBySoftware", 2), ("lockedByHardware", 3), ("lockedBySoftAndHardware", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portLock.setStatus('current')
numberOfExtensionTableEntries = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: numberOfExtensionTableEntries.setStatus('current')
octoExtensionTable = MibTable((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 10), )
if mibBuilder.loadTexts: octoExtensionTable.setStatus('current')
octoExtensionTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 10, 1), ).setIndexNames((0, "OCTOPUSE-MIB", "extensionIndex"))
if mibBuilder.loadTexts: octoExtensionTableEntry.setStatus('current')
extensionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 10, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extensionIndex.setStatus('current')
extensionDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 10, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extensionDescription.setStatus('current')
extensionCodeNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 10, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extensionCodeNumber.setStatus('current')
numberOfLanConnTableEntries = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: numberOfLanConnTableEntries.setStatus('current')
octoLanConnTable = MibTable((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 12), )
if mibBuilder.loadTexts: octoLanConnTable.setStatus('current')
octoLanConnTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 12, 1), ).setIndexNames((0, "OCTOPUSE-MIB", "lanConnIndex"))
if mibBuilder.loadTexts: octoLanConnTableEntry.setStatus('current')
lanConnIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 12, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lanConnIndex.setStatus('current')
lanConnDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 12, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lanConnDescription.setStatus('current')
lanConnIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 12, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lanConnIpAddress.setStatus('current')
lanConnSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 12, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lanConnSubnetMask.setStatus('current')
lanConnStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 12, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lanConnStatus.setStatus('current')
hiPathAllServeServerIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 13), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hiPathAllServeServerIpAddress.setStatus('current')
indexOfLastPortStatusNotificationTrap = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: indexOfLastPortStatusNotificationTrap.setStatus('current')
sysSnmpAgentVersion = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 3, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysSnmpAgentVersion.setStatus('current')
numberOfFeatureStatTableEntries = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: numberOfFeatureStatTableEntries.setStatus('current')
octoFeatureStatTable = MibTable((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 4, 2), )
if mibBuilder.loadTexts: octoFeatureStatTable.setStatus('current')
octoFeatureStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 4, 2, 1), ).setIndexNames((0, "OCTOPUSE-MIB", "featureIndex"))
if mibBuilder.loadTexts: octoFeatureStatEntry.setStatus('current')
featureIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: featureIndex.setStatus('current')
featureDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 4, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: featureDescription.setStatus('current')
featureCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 4, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: featureCounter.setStatus('current')
featureStatTableReset = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 4, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("counting", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: featureStatTableReset.setStatus('current')
octoCdrSeparator = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dosMode", 1), ("unixMode", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: octoCdrSeparator.setStatus('current')
octoCdrElementSeparator = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(124, 59, 32))).clone(namedValues=NamedValues(("pipe", 124), ("semicolon", 59), ("blank", 32)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: octoCdrElementSeparator.setStatus('current')
octoCdrThresholdValue = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: octoCdrThresholdValue.setStatus('current')
octoCdrTftpFileCounter = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: octoCdrTftpFileCounter.setStatus('current')
octoCdrTftpServerDestAddress = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: octoCdrTftpServerDestAddress.setStatus('current')
octoCdrTftpServerAlternateDestAddress = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: octoCdrTftpServerAlternateDestAddress.setStatus('current')
octoCdrTftpClientTimer = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: octoCdrTftpClientTimer.setStatus('current')
octoCdrTcpServerDestAddress = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 8), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: octoCdrTcpServerDestAddress.setStatus('current')
octoCdrTcpServerDestPort = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: octoCdrTcpServerDestPort.setStatus('current')
octoCdrOutputMode = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("v24port", 1), ("uPNport", 2), ("pCVPLport", 3), ("tftpClient", 4), ("tftpServer", 5), ("tcpClient", 6), ("noOutput", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: octoCdrOutputMode.setStatus('current')
octoIndexOfLastCdrNotificationTrap = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: octoIndexOfLastCdrNotificationTrap.setStatus('current')
octoTypeOfLastCdrNotificationTrap = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: octoTypeOfLastCdrNotificationTrap.setStatus('current')
octoDescriptionOfLastCdrNotificationTrap = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 5, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: octoDescriptionOfLastCdrNotificationTrap.setStatus('current')
sendAlarm = NotificationType((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 6, 1)).setObjects(("OCTOPUSE-MIB", "octoErrorIndex"), ("OCTOPUSE-MIB", "octoErrorDateTime"), ("OCTOPUSE-MIB", "octoErrorClass"), ("OCTOPUSE-MIB", "octoErrorCode"), ("OCTOPUSE-MIB", "octoAccessSlot"), ("OCTOPUSE-MIB", "octoAccessPort"), ("OCTOPUSE-MIB", "octoErrorDescription"), ("OCTOPUSE-MIB", "octoSysState"), ("OCTOPUSE-MIB", "octoErrorSeverity"))
if mibBuilder.loadTexts: sendAlarm.setStatus('current')
sendCdrNotification = NotificationType((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 6, 2)).setObjects(("OCTOPUSE-MIB", "octoIndexOfLastCdrNotificationTrap"), ("OCTOPUSE-MIB", "octoTypeOfLastCdrNotificationTrap"), ("OCTOPUSE-MIB", "octoDescriptionOfLastCdrNotificationTrap"))
if mibBuilder.loadTexts: sendCdrNotification.setStatus('current')
sendPortStatusNotification = NotificationType((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 6, 3)).setObjects(("OCTOPUSE-MIB", "indexOfLastPortStatusNotificationTrap"))
if mibBuilder.loadTexts: sendPortStatusNotification.setStatus('current')
numberOfIpConnControlTableEntries = MibScalar((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 7, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: numberOfIpConnControlTableEntries.setStatus('current')
ipConnControlTable = MibTable((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 7, 2), )
if mibBuilder.loadTexts: ipConnControlTable.setStatus('current')
ipConnControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 7, 2, 1), ).setIndexNames((0, "OCTOPUSE-MIB", "connControlIndex"))
if mibBuilder.loadTexts: ipConnControlEntry.setStatus('current')
connControlIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 7, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readonly")
if mibBuilder.loadTexts: connControlIndex.setStatus('current')
connPartnerIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 7, 2, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: connPartnerIpAddress.setStatus('current')
connTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 7, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: connTimeout.setStatus('current')
connRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 7, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: connRetries.setStatus('current')
connRetryTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 7, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483187))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: connRetryTimer.setStatus('current')
connResult = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 7, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("disconnected", 1), ("connected", 2), ("notActivated", 3), ("activated", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: connResult.setStatus('current')
connControlState = MibTableColumn((1, 3, 6, 1, 4, 1, 231, 7, 2, 9, 7, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("singleTest", 1), ("periodicalTest", 2), ("noTest", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: connControlState.setStatus('current')
mibBuilder.exportSymbols("OCTOPUSE-MIB", sysCodeNumber=sysCodeNumber, sysHardwareVersion=sysHardwareVersion, octoErrorClass=octoErrorClass, octoLoadLevel=octoLoadLevel, octoCdrTftpServerDestAddress=octoCdrTftpServerDestAddress, indexOfLastPortStatusNotificationTrap=indexOfLastPortStatusNotificationTrap, DisplayString=DisplayString, octoErrorHistoryGroup=octoErrorHistoryGroup, octoFeatureStatEntry=octoFeatureStatEntry, octoLogBufferState=octoLogBufferState, connRetries=connRetries, octoResetControl=octoResetControl, sendPortStatusNotification=sendPortStatusNotification, portIndex=portIndex, numberOfIpConnControlTableEntries=numberOfIpConnControlTableEntries, octoCdrSeparator=octoCdrSeparator, portType=portType, pn=pn, octoSysState=octoSysState, cardBoxNum=cardBoxNum, extensionCodeNumber=extensionCodeNumber, connTimeout=connTimeout, octoLanConnTableEntry=octoLanConnTableEntry, octoExtensionTable=octoExtensionTable, tftpSwitchoverDateTime=tftpSwitchoverDateTime, sendCdrNotification=sendCdrNotification, octoLanConnTable=octoLanConnTable, octoNetworkGroup=octoNetworkGroup, ipConnControlEntry=ipConnControlEntry, sni=sni, octoControlGroup=octoControlGroup, connPartnerIpAddress=connPartnerIpAddress, octoShadowFlashState=octoShadowFlashState, octoSystemInfoGroup=octoSystemInfoGroup, lanConnDescription=lanConnDescription, octoTypeOfLastCdrNotificationTrap=octoTypeOfLastCdrNotificationTrap, octoCdrThresholdValue=octoCdrThresholdValue, octoErrorSeverity=octoErrorSeverity, extensionIndex=extensionIndex, octoAccessSlot=octoAccessSlot, octoCdrTftpServerAlternateDestAddress=octoCdrTftpServerAlternateDestAddress, octoDescriptionOfLastCdrNotificationTrap=octoDescriptionOfLastCdrNotificationTrap, featureIndex=featureIndex, octoCdrTftpClientTimer=octoCdrTftpClientTimer, cardSlotNum=cardSlotNum, octoErrorIndex=octoErrorIndex, numberOfErrorHistoryEntries=numberOfErrorHistoryEntries, portCardIndex=portCardIndex, octoTrapRepetitions=octoTrapRepetitions, octoErrorDateTime=octoErrorDateTime, octoPortTable=octoPortTable, cardDescription=cardDescription, octoErrorHistoryTable=octoErrorHistoryTable, PYSNMP_MODULE_ID=octopusE, numberOfExtensionTableEntries=numberOfExtensionTableEntries, octoSlotTable=octoSlotTable, siemensUnits=siemensUnits, octoErrorDescription=octoErrorDescription, connRetryTimer=connRetryTimer, octopusE=octopusE, sysSnmpAgentVersion=sysSnmpAgentVersion, featureCounter=featureCounter, octoSwitchoverState=octoSwitchoverState, ipConnControlTable=ipConnControlTable, cardState=cardState, lanConnIpAddress=lanConnIpAddress, numberOfSlotTableEntries=numberOfSlotTableEntries, cardIndex=cardIndex, sendAlarm=sendAlarm, numberOfLanConnTableEntries=numberOfLanConnTableEntries, connResult=connResult, octoCdrElementSeparator=octoCdrElementSeparator, octoExtensionTableEntry=octoExtensionTableEntry, cardCodeNumber=cardCodeNumber, octoErrorCode=octoErrorCode, sysSoftwareVersion=sysSoftwareVersion, cardType=cardType, connControlIndex=connControlIndex, sysSoftwareLocation=sysSoftwareLocation, octoCdrBufferState=octoCdrBufferState, octoCdrConfigGroup=octoCdrConfigGroup, octoCdrTftpFileCounter=octoCdrTftpFileCounter, ReadWrite=ReadWrite, octoPortTableEntry=octoPortTableEntry, lanConnSubnetMask=lanConnSubnetMask, octoAccessPort=octoAccessPort, lanConnIndex=lanConnIndex, octoErrorHistoryEntry=octoErrorHistoryEntry, numberOfPortTableEntries=numberOfPortTableEntries, extensionDescription=extensionDescription, featureDescription=featureDescription, octoCdrOutputMode=octoCdrOutputMode, DateAndTime=DateAndTime, portLock=portLock, portState=portState, lanConnStatus=lanConnStatus, connControlState=connControlState, hiPathAllServeServerIpAddress=hiPathAllServeServerIpAddress, featureStatTableReset=featureStatTableReset, octoStatisticsGroup=octoStatisticsGroup, octoSlotTableEntry=octoSlotTableEntry, octoCdrTcpServerDestAddress=octoCdrTcpServerDestAddress, octoCdrTcpServerDestPort=octoCdrTcpServerDestPort, numberOfFeatureStatTableEntries=numberOfFeatureStatTableEntries, octoFeatureStatTable=octoFeatureStatTable, octoIndexOfLastCdrNotificationTrap=octoIndexOfLastCdrNotificationTrap, octoTrapSpecifications=octoTrapSpecifications, tftpDownloadAction=tftpDownloadAction)
