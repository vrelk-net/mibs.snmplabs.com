#
# PySNMP MIB module HH3C-POWER-ETH-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-POWER-ETH-EXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:16:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
pethPsePortIndex, pethPsePortGroupIndex, pethMainPseGroupIndex, pethPsePortDetectionStatus = mibBuilder.importSymbols("POWER-ETHERNET-MIB", "pethPsePortIndex", "pethPsePortGroupIndex", "pethMainPseGroupIndex", "pethPsePortDetectionStatus")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier, iso, Counter32, NotificationType, ObjectIdentity, TimeTicks, ModuleIdentity, Gauge32, Unsigned32, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier", "iso", "Counter32", "NotificationType", "ObjectIdentity", "TimeTicks", "ModuleIdentity", "Gauge32", "Unsigned32", "IpAddress", "Integer32")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
hh3cPowerEthernetExt = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 14))
if mibBuilder.loadTexts: hh3cPowerEthernetExt.setLastUpdated('200407261023Z')
if mibBuilder.loadTexts: hh3cPowerEthernetExt.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
hh3cPsePortTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 14, 1), )
if mibBuilder.loadTexts: hh3cPsePortTable.setStatus('current')
hh3cPsePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 14, 1, 1), ).setIndexNames((0, "POWER-ETHERNET-MIB", "pethPsePortGroupIndex"), (0, "POWER-ETHERNET-MIB", "pethPsePortIndex"))
if mibBuilder.loadTexts: hh3cPsePortEntry.setStatus('current')
hh3cPsePortFaultDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 1, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPsePortFaultDescription.setStatus('current')
hh3cPsePortPeakPower = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPsePortPeakPower.setStatus('current')
hh3cPsePortAveragePower = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPsePortAveragePower.setStatus('current')
hh3cPsePortCurrentPower = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPsePortCurrentPower.setStatus('current')
hh3cPsePortPowerLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPsePortPowerLimit.setStatus('current')
hh3cPsePortProfileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPsePortProfileIndex.setStatus('current')
hh3cMainPseTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 14, 2), )
if mibBuilder.loadTexts: hh3cMainPseTable.setStatus('current')
hh3cMainPseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 14, 2, 1), ).setIndexNames((0, "POWER-ETHERNET-MIB", "pethMainPseGroupIndex"))
if mibBuilder.loadTexts: hh3cMainPseEntry.setStatus('current')
hh3cMainPsePowerLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 2, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cMainPsePowerLimit.setStatus('current')
hh3cMainPseAveragePower = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 2, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cMainPseAveragePower.setStatus('current')
hh3cMainPsePeakPower = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 2, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cMainPsePeakPower.setStatus('current')
hh3cMainGuaranteedPowerRemaining = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cMainGuaranteedPowerRemaining.setStatus('current')
hh3cMainPsePriorityMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disconnection", 0), ("non-disconnection", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cMainPsePriorityMode.setStatus('current')
hh3cMainPseLegacy = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("enable", 0), ("disable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cMainPseLegacy.setStatus('current')
hh3cMainPsePowerPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("critical", 1), ("high", 2), ("low", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cMainPsePowerPriority.setStatus('current')
hh3cPseProfilesTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 14, 7), )
if mibBuilder.loadTexts: hh3cPseProfilesTable.setStatus('current')
hh3cPseProfilesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 14, 7, 1), ).setIndexNames((0, "HH3C-POWER-ETH-EXT-MIB", "hh3cPseProfileIndex"))
if mibBuilder.loadTexts: hh3cPseProfilesEntry.setStatus('current')
hh3cPseProfileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)))
if mibBuilder.loadTexts: hh3cPseProfileIndex.setStatus('current')
hh3cPseProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 7, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 15))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPseProfileName.setStatus('current')
hh3cPseProfilePowerMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("powerDisabled", 1), ("powerEnabled", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPseProfilePowerMode.setStatus('current')
hh3cPseProfilePowerLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 7, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15400))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPseProfilePowerLimit.setStatus('current')
hh3cPseProfilePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 7, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("critical", 1), ("high", 2), ("low", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPseProfilePriority.setStatus('current')
hh3cPseProfilePairs = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 7, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("signal", 1), ("spare", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPseProfilePairs.setStatus('current')
hh3cPseProfileApplyNum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 7, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPseProfileApplyNum.setStatus('current')
hh3cPseProfileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 7, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cPseProfileRowStatus.setStatus('current')
hh3cPseAutoDetectActive = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 14, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPseAutoDetectActive.setStatus('current')
hh3cPsePowerMaxValue = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 14, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPsePowerMaxValue.setStatus('current')
hh3cPsePolicyMode = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 14, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("priority", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPsePolicyMode.setStatus('current')
hh3cPDPolicyMode = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 14, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("priority", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPDPolicyMode.setStatus('current')
hh3cpseportNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 14, 6))
hh3cpsePDChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 14, 6, 1)).setObjects(("POWER-ETHERNET-MIB", "pethPsePortDetectionStatus"))
if mibBuilder.loadTexts: hh3cpsePDChangeNotification.setStatus('current')
hh3cPOEDisconnectNotification = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 14, 6, 2)).setObjects(("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEAlarmModuleInfoIndex"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEModuleDisconnect"))
if mibBuilder.loadTexts: hh3cPOEDisconnectNotification.setStatus('current')
hh3cPOEInputErrorNotification = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 14, 6, 3)).setObjects(("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEAlarmModuleInfoIndex"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEModuleInputError"))
if mibBuilder.loadTexts: hh3cPOEInputErrorNotification.setStatus('current')
hh3cPOEOutputErrorNotification = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 14, 6, 4)).setObjects(("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEAlarmModuleInfoIndex"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEModuleOutputError"))
if mibBuilder.loadTexts: hh3cPOEOutputErrorNotification.setStatus('current')
hh3cPOEOverVoltageNotification = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 14, 6, 5)).setObjects(("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEAlarmModuleInfoIndex"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEModuleOverVoltage"))
if mibBuilder.loadTexts: hh3cPOEOverVoltageNotification.setStatus('current')
hh3cPOEOverTempNotification = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 14, 6, 6)).setObjects(("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEAlarmModuleInfoIndex"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEModuleOverTemp"))
if mibBuilder.loadTexts: hh3cPOEOverTempNotification.setStatus('current')
hh3cPOEFanErrorNotification = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 14, 6, 7)).setObjects(("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEAlarmModuleInfoIndex"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEModuleFanError"))
if mibBuilder.loadTexts: hh3cPOEFanErrorNotification.setStatus('current')
hh3cPOEModuleShutdownNotification = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 14, 6, 8)).setObjects(("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEAlarmModuleInfoIndex"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEModuleShutdown"))
if mibBuilder.loadTexts: hh3cPOEModuleShutdownNotification.setStatus('current')
hh3cPOECurRestrictedNotification = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 14, 6, 9)).setObjects(("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEAlarmModuleInfoIndex"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEModuleCurRestricted"))
if mibBuilder.loadTexts: hh3cPOECurRestrictedNotification.setStatus('current')
hh3cPOEACSwitchNotification = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 14, 6, 10)).setObjects(("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEACSwitchStateIndex"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEACSwitchState"))
if mibBuilder.loadTexts: hh3cPOEACSwitchNotification.setStatus('current')
hh3cPOEACInCurANotification = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 14, 6, 11)).setObjects(("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEInCurAState"))
if mibBuilder.loadTexts: hh3cPOEACInCurANotification.setStatus('current')
hh3cPOEACInCurBNotification = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 14, 6, 12)).setObjects(("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEInCurBState"))
if mibBuilder.loadTexts: hh3cPOEACInCurBNotification.setStatus('current')
hh3cPOEACInCurCNotification = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 14, 6, 13)).setObjects(("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEInCurCState"))
if mibBuilder.loadTexts: hh3cPOEACInCurCNotification.setStatus('current')
hh3cPOEACSwitchVolABNotification = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 14, 6, 14)).setObjects(("HH3C-POWER-ETH-EXT-MIB", "hh3cPOESwitchStateVolExIndex"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOESwitchStateInVolAB"))
if mibBuilder.loadTexts: hh3cPOEACSwitchVolABNotification.setStatus('current')
hh3cPOEACSwitchVolBCNotification = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 14, 6, 15)).setObjects(("HH3C-POWER-ETH-EXT-MIB", "hh3cPOESwitchStateVolExIndex"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOESwitchStateInVolBC"))
if mibBuilder.loadTexts: hh3cPOEACSwitchVolBCNotification.setStatus('current')
hh3cPOEACSwitchVolCANotification = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 14, 6, 16)).setObjects(("HH3C-POWER-ETH-EXT-MIB", "hh3cPOESwitchStateVolExIndex"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOESwitchStateInVolCA"))
if mibBuilder.loadTexts: hh3cPOEACSwitchVolCANotification.setStatus('current')
hh3cPOEDCOutVolNotification = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 14, 6, 17)).setObjects(("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEDCOutStateIndex"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEDCOutDCVolAlarm"))
if mibBuilder.loadTexts: hh3cPOEDCOutVolNotification.setStatus('current')
hh3cPOEShutdownNotification = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 14, 6, 18))
if mibBuilder.loadTexts: hh3cPOEShutdownNotification.setStatus('current')
hh3cPseComformance = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 14, 4))
hh3cPseCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 14, 4, 1))
hh3cPseCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 25506, 2, 14, 4, 1, 1)).setObjects(("HH3C-POWER-ETH-EXT-MIB", "hh3cPsePortGroup"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cMainPseGroup"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cPseScalarGroup"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cPsePDNotificationGroup"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cPseProfilesGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cPseCompliance = hh3cPseCompliance.setStatus('current')
hh3cPseGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 14, 4, 2))
hh3cPsePortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25506, 2, 14, 4, 2, 1)).setObjects(("HH3C-POWER-ETH-EXT-MIB", "hh3cPsePortProfileIndex"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cPsePortPowerLimit"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cPsePortCurrentPower"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cPsePortAveragePower"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cPsePortPeakPower"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cPsePortFaultDescription"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cMainPsePriorityMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cPsePortGroup = hh3cPsePortGroup.setStatus('current')
hh3cMainPseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25506, 2, 14, 4, 2, 2)).setObjects(("HH3C-POWER-ETH-EXT-MIB", "hh3cMainPsePowerLimit"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cMainPseAveragePower"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cMainPsePeakPower"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cMainGuaranteedPowerRemaining"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cMainPseGroup = hh3cMainPseGroup.setStatus('current')
hh3cPseScalarGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25506, 2, 14, 4, 2, 3)).setObjects(("HH3C-POWER-ETH-EXT-MIB", "hh3cPseAutoDetectActive"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cPsePowerMaxValue"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cPsePolicyMode"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cPDPolicyMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cPseScalarGroup = hh3cPseScalarGroup.setStatus('current')
hh3cPsePDNotificationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25506, 2, 14, 4, 2, 4)).setObjects(("HH3C-POWER-ETH-EXT-MIB", "hh3cpsePDChangeNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cPsePDNotificationGroup = hh3cPsePDNotificationGroup.setStatus('current')
hh3cPseProfilesGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25506, 2, 14, 4, 2, 5)).setObjects(("HH3C-POWER-ETH-EXT-MIB", "hh3cPseProfileName"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cPseProfilePowerMode"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cPseProfilePowerLimit"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cPseProfilePriority"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cPseProfilePairs"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cPseProfileApplyNum"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cPseProfileRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cPseProfilesGroup = hh3cPseProfilesGroup.setStatus('current')
hh3cPOEPowerThresholdLimitGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25506, 2, 14, 4, 2, 6)).setObjects(("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEThresholdACMimimum"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEThresholdACMaximum"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEThresholdDCMinimum"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEThresholdDCMaximum"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cPOEPowerThresholdLimitGroup = hh3cPOEPowerThresholdLimitGroup.setStatus('current')
hh3cPOEPowerSupInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25506, 2, 14, 4, 2, 7)).setObjects(("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEPowerType"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEPowerModuleNum"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOESupervisionModuleName"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOESMMajorVersion"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOESMMinorVersion"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOESMFactorName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cPOEPowerSupInfoGroup = hh3cPOEPowerSupInfoGroup.setStatus('current')
hh3cPOEPowerDCOutStateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25506, 2, 14, 4, 2, 8)).setObjects(("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEDCOutStateModuleNum"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cPOEPowerDCOutStateGroup = hh3cPOEPowerDCOutStateGroup.setStatus('current')
hh3cPOEPowerDCOutInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25506, 2, 14, 4, 2, 9)).setObjects(("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEDCOutCurNum"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cPOEPowerDCOutInfoGroup = hh3cPOEPowerDCOutInfoGroup.setStatus('current')
hh3cPOEPowerACSwitchStateModuleGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25506, 2, 14, 4, 2, 10)).setObjects(("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEACSwitchStateModuleNum"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cPOEPowerACSwitchStateModuleGroup = hh3cPOEPowerACSwitchStateModuleGroup.setStatus('current')
hh3cPOEPowerInCurStateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25506, 2, 14, 4, 2, 11)).setObjects(("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEInCurStateModuleNum"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEInCurAState"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEInCurBState"), ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEInCurCState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cPOEPowerInCurStateGroup = hh3cPOEPowerInCurStateGroup.setStatus('current')
hh3cPOEPowerAlarmStateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 25506, 2, 14, 4, 2, 12)).setObjects(("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEAlarmStateModuleNum"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hh3cPOEPowerAlarmStateGroup = hh3cPOEPowerAlarmStateGroup.setStatus('current')
class ACAlarmState(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("normal", 1), ("underLimit", 2), ("aboveLimit", 3), ("lackPhrase", 4), ("fuseBroken", 5), ("switchOff", 6), ("otherError", 7))

class DCAlarmState(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("normal", 1), ("underLimit", 2), ("aboveLimit", 3), ("fuseBroken", 4), ("switchOff", 5), ("otherError", 6))

class SwitchState(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("on", 1), ("off", 2), ("highVoltInput", 3), ("lowVoltInput", 4))

class ModuleAlarmState(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("normal", 1), ("alarm", 2))

hh3cPOEPowerObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8))
hh3cPOEThresholdLimitObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 1))
hh3cPOEThresholdACMimimum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPOEThresholdACMimimum.setStatus('current')
hh3cPOEThresholdACMaximum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPOEThresholdACMaximum.setStatus('current')
hh3cPOEThresholdDCMinimum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPOEThresholdDCMinimum.setStatus('current')
hh3cPOEThresholdDCMaximum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cPOEThresholdDCMaximum.setStatus('current')
hh3cPOESupModuleInfoObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 2))
hh3cPOEPowerType = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 2, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPOEPowerType.setStatus('current')
hh3cPOEPowerModuleNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPOEPowerModuleNum.setStatus('current')
hh3cPOESupervisionModuleName = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 2, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPOESupervisionModuleName.setStatus('current')
hh3cPOESMMajorVersion = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPOESMMajorVersion.setStatus('current')
hh3cPOESMMinorVersion = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPOESMMinorVersion.setStatus('current')
hh3cPOESMFactorName = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 2, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPOESMFactorName.setStatus('current')
hh3cPOEModuleInfoTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 2, 7), )
if mibBuilder.loadTexts: hh3cPOEModuleInfoTable.setStatus('current')
hh3cPOEModuleInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 2, 7, 1), ).setIndexNames((0, "HH3C-POWER-ETH-EXT-MIB", "hh3cPOEModuleIndex"))
if mibBuilder.loadTexts: hh3cPOEModuleInfoEntry.setStatus('current')
hh3cPOEModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 2, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cPOEModuleIndex.setStatus('current')
hh3cPOEModuleID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 2, 7, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPOEModuleID.setStatus('current')
hh3cPOEModuleInfoPower = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 2, 7, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPOEModuleInfoPower.setStatus('current')
hh3cPOEModuleHardVerInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 2, 7, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPOEModuleHardVerInfo.setStatus('current')
hh3cPOEDCOutStateObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 3))
hh3cPOEDCOutStateModuleNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPOEDCOutStateModuleNum.setStatus('current')
hh3cPOEDCOutStateTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 3, 2), )
if mibBuilder.loadTexts: hh3cPOEDCOutStateTable.setStatus('current')
hh3cPOEDCOutStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 3, 2, 1), ).setIndexNames((0, "HH3C-POWER-ETH-EXT-MIB", "hh3cPOEDCOutStateIndex"))
if mibBuilder.loadTexts: hh3cPOEDCOutStateEntry.setStatus('current')
hh3cPOEDCOutStateIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cPOEDCOutStateIndex.setStatus('current')
hh3cPOEDCOutDCVolAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 3, 2, 1, 2), DCAlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPOEDCOutDCVolAlarm.setStatus('current')
hh3cPOEDCOutInfoObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 4))
hh3cPOEDCOutCurNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPOEDCOutCurNum.setStatus('current')
hh3cPOEDCOutInfoTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 4, 2), )
if mibBuilder.loadTexts: hh3cPOEDCOutInfoTable.setStatus('current')
hh3cPOEDCOutInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 4, 2, 1), ).setIndexNames((0, "HH3C-POWER-ETH-EXT-MIB", "hh3cPOEDCOutInfoIndex"))
if mibBuilder.loadTexts: hh3cPOEDCOutInfoEntry.setStatus('current')
hh3cPOEDCOutInfoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cPOEDCOutInfoIndex.setStatus('current')
hh3cPOEDCOutVol = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 4, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPOEDCOutVol.setStatus('current')
hh3cPOEDCOutInfoLoadCur = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 4, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPOEDCOutInfoLoadCur.setStatus('current')
hh3cPOEACSwitchStateModuleObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 5))
hh3cPOEACSwitchStateModuleNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 5, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPOEACSwitchStateModuleNum.setStatus('current')
hh3cPOEACSwitchStateTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 5, 2), )
if mibBuilder.loadTexts: hh3cPOEACSwitchStateTable.setStatus('current')
hh3cPOEACSwitchStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 5, 2, 1), ).setIndexNames((0, "HH3C-POWER-ETH-EXT-MIB", "hh3cPOEACSwitchStateIndex"))
if mibBuilder.loadTexts: hh3cPOEACSwitchStateEntry.setStatus('current')
hh3cPOEACSwitchStateIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 5, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cPOEACSwitchStateIndex.setStatus('current')
hh3cPOEACSwitchState = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 5, 2, 1, 2), SwitchState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPOEACSwitchState.setStatus('current')
hh3cPOEInCurStateObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 6))
hh3cPOEInCurStateModuleNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 6, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPOEInCurStateModuleNum.setStatus('current')
hh3cPOEInCurAState = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 6, 2), ACAlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPOEInCurAState.setStatus('current')
hh3cPOEInCurBState = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 6, 3), ACAlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPOEInCurBState.setStatus('current')
hh3cPOEInCurCState = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 6, 4), ACAlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPOEInCurCState.setStatus('current')
hh3cPOESwitchStateVolExTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 6, 5), )
if mibBuilder.loadTexts: hh3cPOESwitchStateVolExTable.setStatus('current')
hh3cPOESwitchStateVolExEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 6, 5, 1), ).setIndexNames((0, "HH3C-POWER-ETH-EXT-MIB", "hh3cPOESwitchStateVolExIndex"))
if mibBuilder.loadTexts: hh3cPOESwitchStateVolExEntry.setStatus('current')
hh3cPOESwitchStateVolExIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 6, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cPOESwitchStateVolExIndex.setStatus('current')
hh3cPOESwitchStateInVolAB = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 6, 5, 1, 2), ACAlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPOESwitchStateInVolAB.setStatus('current')
hh3cPOESwitchStateInVolBC = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 6, 5, 1, 3), ACAlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPOESwitchStateInVolBC.setStatus('current')
hh3cPOESwitchStateInVolCA = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 6, 5, 1, 4), ACAlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPOESwitchStateInVolCA.setStatus('current')
hh3cPOEAlarmStateObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 7))
hh3cPOEAlarmStateModuleNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 7, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPOEAlarmStateModuleNum.setStatus('current')
hh3cPOEAlarmStateInfoTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 7, 2), )
if mibBuilder.loadTexts: hh3cPOEAlarmStateInfoTable.setStatus('current')
hh3cPOEAlarmStateInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 7, 2, 1), ).setIndexNames((0, "HH3C-POWER-ETH-EXT-MIB", "hh3cPOEAlarmModuleInfoIndex"))
if mibBuilder.loadTexts: hh3cPOEAlarmStateInfoEntry.setStatus('current')
hh3cPOEAlarmModuleInfoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 7, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cPOEAlarmModuleInfoIndex.setStatus('current')
hh3cPOEModuleDisconnect = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 7, 2, 1, 2), ModuleAlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPOEModuleDisconnect.setStatus('current')
hh3cPOEModuleInputError = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 7, 2, 1, 3), ModuleAlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPOEModuleInputError.setStatus('current')
hh3cPOEModuleOutputError = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 7, 2, 1, 4), ModuleAlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPOEModuleOutputError.setStatus('current')
hh3cPOEModuleOverVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 7, 2, 1, 5), ModuleAlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPOEModuleOverVoltage.setStatus('current')
hh3cPOEModuleOverTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 7, 2, 1, 6), ModuleAlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPOEModuleOverTemp.setStatus('current')
hh3cPOEModuleFanError = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 7, 2, 1, 7), ModuleAlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPOEModuleFanError.setStatus('current')
hh3cPOEModuleShutdown = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 7, 2, 1, 8), ModuleAlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPOEModuleShutdown.setStatus('current')
hh3cPOEModuleCurRestricted = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 7, 2, 1, 9), ModuleAlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cPOEModuleCurRestricted.setStatus('current')
mibBuilder.exportSymbols("HH3C-POWER-ETH-EXT-MIB", hh3cPOEModuleInfoEntry=hh3cPOEModuleInfoEntry, hh3cPOEACSwitchStateTable=hh3cPOEACSwitchStateTable, hh3cPDPolicyMode=hh3cPDPolicyMode, hh3cpseportNotification=hh3cpseportNotification, hh3cPOEACSwitchNotification=hh3cPOEACSwitchNotification, hh3cPOEDCOutVol=hh3cPOEDCOutVol, hh3cPOEOutputErrorNotification=hh3cPOEOutputErrorNotification, hh3cPOEModuleCurRestricted=hh3cPOEModuleCurRestricted, hh3cPOEDCOutStateObjects=hh3cPOEDCOutStateObjects, hh3cPsePowerMaxValue=hh3cPsePowerMaxValue, hh3cPseProfilePriority=hh3cPseProfilePriority, hh3cMainPsePriorityMode=hh3cMainPsePriorityMode, hh3cPsePortAveragePower=hh3cPsePortAveragePower, hh3cPOEThresholdACMaximum=hh3cPOEThresholdACMaximum, hh3cPOEPowerACSwitchStateModuleGroup=hh3cPOEPowerACSwitchStateModuleGroup, hh3cPOEDCOutStateModuleNum=hh3cPOEDCOutStateModuleNum, hh3cPOEACSwitchStateEntry=hh3cPOEACSwitchStateEntry, hh3cPOECurRestrictedNotification=hh3cPOECurRestrictedNotification, hh3cPseCompliances=hh3cPseCompliances, hh3cPOEModuleShutdownNotification=hh3cPOEModuleShutdownNotification, hh3cPsePortFaultDescription=hh3cPsePortFaultDescription, hh3cPOEACSwitchStateModuleObjs=hh3cPOEACSwitchStateModuleObjs, hh3cPOEDCOutInfoObjects=hh3cPOEDCOutInfoObjects, hh3cPOEAlarmModuleInfoIndex=hh3cPOEAlarmModuleInfoIndex, hh3cPOEACSwitchVolBCNotification=hh3cPOEACSwitchVolBCNotification, hh3cPOEACInCurBNotification=hh3cPOEACInCurBNotification, hh3cPOESwitchStateVolExIndex=hh3cPOESwitchStateVolExIndex, hh3cPOEAlarmStateInfoEntry=hh3cPOEAlarmStateInfoEntry, hh3cPOEModuleShutdown=hh3cPOEModuleShutdown, SwitchState=SwitchState, hh3cPOEDisconnectNotification=hh3cPOEDisconnectNotification, hh3cPOEShutdownNotification=hh3cPOEShutdownNotification, hh3cMainPseEntry=hh3cMainPseEntry, hh3cMainPsePowerPriority=hh3cMainPsePowerPriority, hh3cPseProfilesTable=hh3cPseProfilesTable, DCAlarmState=DCAlarmState, hh3cPsePortCurrentPower=hh3cPsePortCurrentPower, hh3cPOEModuleID=hh3cPOEModuleID, hh3cPsePortProfileIndex=hh3cPsePortProfileIndex, hh3cPseProfilePowerMode=hh3cPseProfilePowerMode, hh3cPOEACSwitchVolABNotification=hh3cPOEACSwitchVolABNotification, hh3cPOESupModuleInfoObjs=hh3cPOESupModuleInfoObjs, hh3cPOEACSwitchState=hh3cPOEACSwitchState, hh3cPOESMFactorName=hh3cPOESMFactorName, hh3cPseProfilePairs=hh3cPseProfilePairs, hh3cPseGroup=hh3cPseGroup, hh3cPOEDCOutInfoEntry=hh3cPOEDCOutInfoEntry, hh3cMainPseGroup=hh3cMainPseGroup, hh3cPseProfileName=hh3cPseProfileName, hh3cPOEInCurBState=hh3cPOEInCurBState, hh3cPOEPowerObjects=hh3cPOEPowerObjects, hh3cPsePDNotificationGroup=hh3cPsePDNotificationGroup, hh3cPOEDCOutCurNum=hh3cPOEDCOutCurNum, hh3cPOESwitchStateInVolBC=hh3cPOESwitchStateInVolBC, hh3cPOEACInCurANotification=hh3cPOEACInCurANotification, hh3cPOEACSwitchStateIndex=hh3cPOEACSwitchStateIndex, hh3cPOEInCurCState=hh3cPOEInCurCState, hh3cPOEAlarmStateInfoTable=hh3cPOEAlarmStateInfoTable, hh3cPOEThresholdACMimimum=hh3cPOEThresholdACMimimum, hh3cPsePortEntry=hh3cPsePortEntry, hh3cPOESwitchStateVolExTable=hh3cPOESwitchStateVolExTable, hh3cPOEModuleInfoTable=hh3cPOEModuleInfoTable, hh3cPOEDCOutInfoTable=hh3cPOEDCOutInfoTable, hh3cPOEDCOutStateEntry=hh3cPOEDCOutStateEntry, hh3cPOEInputErrorNotification=hh3cPOEInputErrorNotification, hh3cPseScalarGroup=hh3cPseScalarGroup, hh3cMainPseTable=hh3cMainPseTable, hh3cPOEInCurStateModuleNum=hh3cPOEInCurStateModuleNum, hh3cPsePolicyMode=hh3cPsePolicyMode, hh3cPseCompliance=hh3cPseCompliance, hh3cPOEDCOutVolNotification=hh3cPOEDCOutVolNotification, hh3cPOEAlarmStateModuleNum=hh3cPOEAlarmStateModuleNum, hh3cPOEDCOutInfoIndex=hh3cPOEDCOutInfoIndex, hh3cMainPseLegacy=hh3cMainPseLegacy, hh3cPOEPowerModuleNum=hh3cPOEPowerModuleNum, hh3cPOEPowerThresholdLimitGroup=hh3cPOEPowerThresholdLimitGroup, hh3cPseProfilePowerLimit=hh3cPseProfilePowerLimit, hh3cPOEFanErrorNotification=hh3cPOEFanErrorNotification, hh3cPOEOverTempNotification=hh3cPOEOverTempNotification, hh3cPOEPowerDCOutStateGroup=hh3cPOEPowerDCOutStateGroup, hh3cPOEModuleIndex=hh3cPOEModuleIndex, hh3cPseProfileIndex=hh3cPseProfileIndex, hh3cPOEInCurAState=hh3cPOEInCurAState, hh3cPOEACInCurCNotification=hh3cPOEACInCurCNotification, hh3cPOEModuleOverTemp=hh3cPOEModuleOverTemp, hh3cPseProfilesGroup=hh3cPseProfilesGroup, hh3cPOEDCOutStateTable=hh3cPOEDCOutStateTable, hh3cPOEAlarmStateObjects=hh3cPOEAlarmStateObjects, hh3cPowerEthernetExt=hh3cPowerEthernetExt, hh3cPOEPowerInCurStateGroup=hh3cPOEPowerInCurStateGroup, hh3cMainGuaranteedPowerRemaining=hh3cMainGuaranteedPowerRemaining, hh3cPOEDCOutStateIndex=hh3cPOEDCOutStateIndex, hh3cPOEACSwitchVolCANotification=hh3cPOEACSwitchVolCANotification, hh3cPOESwitchStateVolExEntry=hh3cPOESwitchStateVolExEntry, hh3cMainPseAveragePower=hh3cMainPseAveragePower, PYSNMP_MODULE_ID=hh3cPowerEthernetExt, hh3cPOEDCOutDCVolAlarm=hh3cPOEDCOutDCVolAlarm, hh3cPsePortPowerLimit=hh3cPsePortPowerLimit, hh3cPOEModuleOverVoltage=hh3cPOEModuleOverVoltage, hh3cMainPsePowerLimit=hh3cMainPsePowerLimit, hh3cPseProfilesEntry=hh3cPseProfilesEntry, hh3cPOEModuleOutputError=hh3cPOEModuleOutputError, hh3cPOEPowerDCOutInfoGroup=hh3cPOEPowerDCOutInfoGroup, hh3cPOESwitchStateInVolAB=hh3cPOESwitchStateInVolAB, hh3cPOEOverVoltageNotification=hh3cPOEOverVoltageNotification, hh3cPOEPowerType=hh3cPOEPowerType, hh3cPsePortTable=hh3cPsePortTable, hh3cpsePDChangeNotification=hh3cpsePDChangeNotification, hh3cPOEPowerSupInfoGroup=hh3cPOEPowerSupInfoGroup, hh3cPOEModuleDisconnect=hh3cPOEModuleDisconnect, hh3cPOEDCOutInfoLoadCur=hh3cPOEDCOutInfoLoadCur, hh3cMainPsePeakPower=hh3cMainPsePeakPower, hh3cPOEPowerAlarmStateGroup=hh3cPOEPowerAlarmStateGroup, hh3cPsePortGroup=hh3cPsePortGroup, hh3cPOEThresholdDCMaximum=hh3cPOEThresholdDCMaximum, hh3cPOESupervisionModuleName=hh3cPOESupervisionModuleName, hh3cPOEThresholdDCMinimum=hh3cPOEThresholdDCMinimum, ModuleAlarmState=ModuleAlarmState, hh3cPseComformance=hh3cPseComformance, hh3cPOEModuleHardVerInfo=hh3cPOEModuleHardVerInfo, hh3cPOEThresholdLimitObjs=hh3cPOEThresholdLimitObjs, hh3cPOEModuleInfoPower=hh3cPOEModuleInfoPower, hh3cPOESMMinorVersion=hh3cPOESMMinorVersion, hh3cPseAutoDetectActive=hh3cPseAutoDetectActive, hh3cPOEACSwitchStateModuleNum=hh3cPOEACSwitchStateModuleNum, hh3cPOEInCurStateObjects=hh3cPOEInCurStateObjects, hh3cPOESwitchStateInVolCA=hh3cPOESwitchStateInVolCA, hh3cPseProfileRowStatus=hh3cPseProfileRowStatus, hh3cPOEModuleFanError=hh3cPOEModuleFanError, hh3cPseProfileApplyNum=hh3cPseProfileApplyNum, ACAlarmState=ACAlarmState, hh3cPOESMMajorVersion=hh3cPOESMMajorVersion, hh3cPOEModuleInputError=hh3cPOEModuleInputError, hh3cPsePortPeakPower=hh3cPsePortPeakPower)
