#
# PySNMP MIB module CISCO-DOT11-HT-MAC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DOT11-HT-MAC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:38:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, Bits, Counter64, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, MibIdentifier, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "Bits", "Counter64", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "MibIdentifier", "Integer32", "Counter32")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
ciscoDot11HtMacMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 626))
ciscoDot11HtMacMIB.setRevisions(('2007-05-16 00:00',))
if mibBuilder.loadTexts: ciscoDot11HtMacMIB.setLastUpdated('200705160000Z')
if mibBuilder.loadTexts: ciscoDot11HtMacMIB.setOrganization('Cisco Systems, Inc.')
ciscoDot11HtMacMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 626, 0))
ciscoDot11HtMacMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 626, 1))
ciscoDot11HtMacMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 626, 2))
cD11HtMacStationConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1))
cD11HtMacOperations = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2))
cD11HtMacStationConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1), )
if mibBuilder.loadTexts: cD11HtMacStationConfigTable.setStatus('current')
cD11HtMacStationConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cD11HtMacStationConfigEntry.setStatus('current')
cD11HtMacOperationalMCSSet = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cD11HtMacOperationalMCSSet.setStatus('current')
cD11HtMacMIMOPowerSave = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("static", 1), ("dynamic", 2), ("mimo", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtMacMIMOPowerSave.setStatus('current')
cD11HtMacNDelayedBlockAckImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1, 3), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtMacNDelayedBlockAckImplemented.setStatus('current')
cD11HtMacMaxAMSDULength = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(3839, 7935))).clone(namedValues=NamedValues(("amsduSize3839", 3839), ("amsduSize7935", 7935))).clone('amsduSize3839')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtMacMaxAMSDULength.setStatus('current')
cD11HtMacPSMPImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtMacPSMPImplemented.setStatus('current')
cD11HtMacSTBCControlFrameImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1, 6), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtMacSTBCControlFrameImplemented.setStatus('current')
cD11HtMacLsigTxOpProtectImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1, 7), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtMacLsigTxOpProtectImplemented.setStatus('current')
cD11HtMacMaxRxAMPDUFactor = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtMacMaxRxAMPDUFactor.setStatus('current')
cD11HtMacMPDUDensity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("noTimeRestriction", 1), ("oneEighth", 2), ("oneFourth", 3), ("half", 4), ("one", 5), ("two", 6), ("four", 7), ("eight", 8))).clone('one')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtMacMPDUDensity.setStatus('current')
cD11HtMacPCOImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1, 10), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtMacPCOImplemented.setStatus('current')
cD11HtMacTransitionTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(400, 1500, 5000))).clone(namedValues=NamedValues(("fourHundred", 400), ("oneThousandFiveHundred", 1500), ("fiveThousand", 5000))).clone('fiveThousand')).setUnits('microseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtMacTransitionTime.setStatus('current')
cD11HtMacMCSFeedbackImplemented = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("unsolicited", 2), ("both", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cD11HtMacMCSFeedbackImplemented.setStatus('current')
cD11HtMacAMSDUEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1, 13), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cD11HtMacAMSDUEnable.setStatus('current')
cD11HtMacAMPDUEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 1, 1, 1, 14), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cD11HtMacAMPDUEnable.setStatus('current')
cD11HtMacOperationTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2, 1), )
if mibBuilder.loadTexts: cD11HtMacOperationTable.setStatus('current')
cD11HtMacOperationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cD11HtMacOperationEntry.setStatus('current')
cD11HtMacOperatingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("pureHt", 1), ("optionalProtection", 2), ("mandatoryFortyProtection", 3), ("mandatoryAllProtection", 4))).clone('pureHt')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cD11HtMacOperatingMode.setStatus('current')
cD11HtMacRIFSMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cD11HtMacRIFSMode.setStatus('current')
cD11HtMacPSMPControlledAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2, 1, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cD11HtMacPSMPControlledAccess.setStatus('current')
cD11HtMacServiceIntervalGranularity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cD11HtMacServiceIntervalGranularity.setStatus('current')
cD11HtMacDualCTSProtection = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cD11HtMacDualCTSProtection.setStatus('current')
cD11HtMacLSigTxOpFullProtectionEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2, 1, 1, 6), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cD11HtMacLSigTxOpFullProtectionEnabled.setStatus('current')
cD11HtMacNonGFEntitiesPresent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2, 1, 1, 7), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cD11HtMacNonGFEntitiesPresent.setStatus('current')
cD11HtMacPCOActivated = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2, 1, 1, 8), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cD11HtMacPCOActivated.setStatus('current')
cD11HtMacPCO20MaxDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(60)).setUnits('TU').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cD11HtMacPCO20MaxDuration.setStatus('current')
cD11HtMacPCO40MaxDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(60)).setUnits('TU').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cD11HtMacPCO40MaxDuration.setStatus('current')
cD11HtMacPCO20MinDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(40)).setUnits('TU').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cD11HtMacPCO20MinDuration.setStatus('current')
cD11HtMacPCO40MinDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 626, 1, 2, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(40)).setUnits('TU').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cD11HtMacPCO40MinDuration.setStatus('current')
ciscoDot11HtMacMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 626, 2, 1))
ciscoDot11HtMacMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 626, 2, 2))
cD11HtMacCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 626, 2, 1, 1)).setObjects(("CISCO-DOT11-HT-MAC-MIB", "ciscoDot11HtMacStationConfigGroup"), ("CISCO-DOT11-HT-MAC-MIB", "ciscoDot11HtMacOperationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cD11HtMacCompliance = cD11HtMacCompliance.setStatus('current')
ciscoDot11HtMacStationConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 626, 2, 2, 1)).setObjects(("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacOperationalMCSSet"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacMIMOPowerSave"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacNDelayedBlockAckImplemented"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacMaxAMSDULength"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacPSMPImplemented"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacSTBCControlFrameImplemented"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacLsigTxOpProtectImplemented"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacMaxRxAMPDUFactor"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacMPDUDensity"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacPCOImplemented"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacTransitionTime"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacMCSFeedbackImplemented"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacAMSDUEnable"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacAMPDUEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11HtMacStationConfigGroup = ciscoDot11HtMacStationConfigGroup.setStatus('current')
ciscoDot11HtMacOperationsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 626, 2, 2, 2)).setObjects(("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacOperatingMode"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacRIFSMode"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacPSMPControlledAccess"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacServiceIntervalGranularity"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacDualCTSProtection"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacLSigTxOpFullProtectionEnabled"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacNonGFEntitiesPresent"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacPCOActivated"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacPCO40MaxDuration"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacPCO20MaxDuration"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacPCO40MinDuration"), ("CISCO-DOT11-HT-MAC-MIB", "cD11HtMacPCO20MinDuration"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11HtMacOperationsGroup = ciscoDot11HtMacOperationsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-DOT11-HT-MAC-MIB", cD11HtMacMPDUDensity=cD11HtMacMPDUDensity, ciscoDot11HtMacStationConfigGroup=ciscoDot11HtMacStationConfigGroup, cD11HtMacPCO40MaxDuration=cD11HtMacPCO40MaxDuration, PYSNMP_MODULE_ID=ciscoDot11HtMacMIB, cD11HtMacTransitionTime=cD11HtMacTransitionTime, cD11HtMacPSMPImplemented=cD11HtMacPSMPImplemented, cD11HtMacPCO20MinDuration=cD11HtMacPCO20MinDuration, cD11HtMacLsigTxOpProtectImplemented=cD11HtMacLsigTxOpProtectImplemented, cD11HtMacLSigTxOpFullProtectionEnabled=cD11HtMacLSigTxOpFullProtectionEnabled, cD11HtMacAMSDUEnable=cD11HtMacAMSDUEnable, cD11HtMacServiceIntervalGranularity=cD11HtMacServiceIntervalGranularity, cD11HtMacOperationEntry=cD11HtMacOperationEntry, cD11HtMacPCO40MinDuration=cD11HtMacPCO40MinDuration, cD11HtMacPCOActivated=cD11HtMacPCOActivated, cD11HtMacCompliance=cD11HtMacCompliance, ciscoDot11HtMacMIBObjects=ciscoDot11HtMacMIBObjects, cD11HtMacMaxAMSDULength=cD11HtMacMaxAMSDULength, cD11HtMacPCOImplemented=cD11HtMacPCOImplemented, cD11HtMacSTBCControlFrameImplemented=cD11HtMacSTBCControlFrameImplemented, cD11HtMacOperations=cD11HtMacOperations, cD11HtMacOperatingMode=cD11HtMacOperatingMode, cD11HtMacDualCTSProtection=cD11HtMacDualCTSProtection, cD11HtMacPCO20MaxDuration=cD11HtMacPCO20MaxDuration, ciscoDot11HtMacMIB=ciscoDot11HtMacMIB, ciscoDot11HtMacMIBNotifs=ciscoDot11HtMacMIBNotifs, cD11HtMacStationConfigTable=cD11HtMacStationConfigTable, cD11HtMacOperationalMCSSet=cD11HtMacOperationalMCSSet, ciscoDot11HtMacMIBConform=ciscoDot11HtMacMIBConform, cD11HtMacStationConfig=cD11HtMacStationConfig, cD11HtMacPSMPControlledAccess=cD11HtMacPSMPControlledAccess, ciscoDot11HtMacMIBGroups=ciscoDot11HtMacMIBGroups, cD11HtMacNDelayedBlockAckImplemented=cD11HtMacNDelayedBlockAckImplemented, cD11HtMacRIFSMode=cD11HtMacRIFSMode, ciscoDot11HtMacOperationsGroup=ciscoDot11HtMacOperationsGroup, cD11HtMacNonGFEntitiesPresent=cD11HtMacNonGFEntitiesPresent, cD11HtMacOperationTable=cD11HtMacOperationTable, cD11HtMacMCSFeedbackImplemented=cD11HtMacMCSFeedbackImplemented, cD11HtMacMaxRxAMPDUFactor=cD11HtMacMaxRxAMPDUFactor, ciscoDot11HtMacMIBCompliances=ciscoDot11HtMacMIBCompliances, cD11HtMacAMPDUEnable=cD11HtMacAMPDUEnable, cD11HtMacStationConfigEntry=cD11HtMacStationConfigEntry, cD11HtMacMIMOPowerSave=cD11HtMacMIMOPowerSave)