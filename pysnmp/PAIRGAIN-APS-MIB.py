#
# PySNMP MIB module PAIRGAIN-APS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PAIRGAIN-APS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:27:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
pgApsMIB, = mibBuilder.importSymbols("PAIRGAIN-COMMON-HD-MIB", "pgApsMIB")
TimeSeconds, = mibBuilder.importSymbols("PAIRGAIN-DSLAM-CHASSIS-MIB", "TimeSeconds")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress, Gauge32, Counter64, Integer32, Unsigned32, Bits, ModuleIdentity, ObjectIdentity, TimeTicks, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress", "Gauge32", "Counter64", "Integer32", "Unsigned32", "Bits", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "iso", "NotificationType")
TruthValue, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "TextualConvention", "DisplayString")
pgAps = ModuleIdentity((1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1))
if mibBuilder.loadTexts: pgAps.setLastUpdated('9910110000Z')
if mibBuilder.loadTexts: pgAps.setOrganization('PairGain Technologies, Inc.')
pgApsMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 0))
pgApsMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1))
class Byte(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class PgApsK1K2(TextualConvention, Integer32):
    status = 'current'

pgApsConfigTable = MibTable((1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 1), )
if mibBuilder.loadTexts: pgApsConfigTable.setStatus('current')
pgApsConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 1, 1), ).setIndexNames((0, "PAIRGAIN-APS-MIB", "pgApsIndex"))
if mibBuilder.loadTexts: pgApsConfigEntry.setStatus('current')
pgApsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgApsIndex.setStatus('current')
pgApsEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgApsEnable.setStatus('current')
pgApsTrapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgApsTrapEnable.setStatus('current')
pgApsWorkChanIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgApsWorkChanIfIndex.setStatus('current')
pgApsProtChanIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgApsProtChanIfIndex.setStatus('current')
pgApsConfigMode = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("nonRevertive", 1), ("nonRevertiveAuto", 2), ("revertive", 3))).clone('nonRevertive')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgApsConfigMode.setStatus('current')
pgApsConfigSigDegradeThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 9))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgApsConfigSigDegradeThresh.setStatus('current')
pgApsConfigWaitToRevert = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(300, 720)).clone(300)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgApsConfigWaitToRevert.setStatus('current')
pgApsSwitchCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgApsSwitchCommand.setStatus('current')
pgApsStatusTable = MibTable((1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 2), )
if mibBuilder.loadTexts: pgApsStatusTable.setStatus('current')
pgApsStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 2, 1), ).setIndexNames((0, "PAIRGAIN-APS-MIB", "pgApsIndex"))
if mibBuilder.loadTexts: pgApsStatusEntry.setStatus('current')
pgApsStatusK1K2Rx = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 2, 1, 1), PgApsK1K2()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgApsStatusK1K2Rx.setStatus('current')
pgApsStatusK1K2Tx = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 2, 1, 2), PgApsK1K2()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgApsStatusK1K2Tx.setStatus('current')
pgApsStatusCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 2, 1, 3), Byte()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgApsStatusCurrent.setStatus('current')
pgApsWorkChanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 2, 1, 4), Bits().clone(namedValues=NamedValues(("lockedOut", 0), ("sd", 1), ("sf", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgApsWorkChanStatus.setStatus('current')
pgApsWorkChanLastSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 2, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgApsWorkChanLastSwitch.setStatus('current')
pgApsWorkChanSDs = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgApsWorkChanSDs.setStatus('current')
pgApsWorkChanSFs = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgApsWorkChanSFs.setStatus('current')
pgApsWorkNumSwitchOvers = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgApsWorkNumSwitchOvers.setStatus('current')
pgApsProtChanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 2, 1, 9), Bits().clone(namedValues=NamedValues(("lockedOut", 0), ("sd", 1), ("sf", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgApsProtChanStatus.setStatus('current')
pgApsProtChanLastSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 2, 1, 10), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgApsProtChanLastSwitch.setStatus('current')
pgApsProtChanSDs = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgApsProtChanSDs.setStatus('current')
pgApsProtChanSFs = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgApsProtChanSFs.setStatus('current')
pgApsProtNumSwitchOvers = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 1, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgApsProtNumSwitchOvers.setStatus('current')
pgApsTrapSwitchOver = NotificationType((1, 3, 6, 1, 4, 1, 927, 1, 9, 12, 1, 0, 1)).setObjects(("PAIRGAIN-APS-MIB", "pgApsStatusEntry"))
if mibBuilder.loadTexts: pgApsTrapSwitchOver.setStatus('current')
mibBuilder.exportSymbols("PAIRGAIN-APS-MIB", pgAps=pgAps, pgApsStatusK1K2Tx=pgApsStatusK1K2Tx, PYSNMP_MODULE_ID=pgAps, Byte=Byte, pgApsEnable=pgApsEnable, pgApsConfigMode=pgApsConfigMode, pgApsProtChanLastSwitch=pgApsProtChanLastSwitch, pgApsStatusTable=pgApsStatusTable, pgApsStatusEntry=pgApsStatusEntry, pgApsStatusK1K2Rx=pgApsStatusK1K2Rx, pgApsWorkChanStatus=pgApsWorkChanStatus, pgApsProtChanSDs=pgApsProtChanSDs, pgApsStatusCurrent=pgApsStatusCurrent, pgApsConfigTable=pgApsConfigTable, pgApsWorkChanLastSwitch=pgApsWorkChanLastSwitch, pgApsWorkChanSFs=pgApsWorkChanSFs, pgApsConfigEntry=pgApsConfigEntry, pgApsProtNumSwitchOvers=pgApsProtNumSwitchOvers, pgApsMibObjects=pgApsMibObjects, PgApsK1K2=PgApsK1K2, pgApsIndex=pgApsIndex, pgApsConfigWaitToRevert=pgApsConfigWaitToRevert, pgApsWorkChanIfIndex=pgApsWorkChanIfIndex, pgApsTrapEnable=pgApsTrapEnable, pgApsProtChanSFs=pgApsProtChanSFs, pgApsWorkNumSwitchOvers=pgApsWorkNumSwitchOvers, pgApsWorkChanSDs=pgApsWorkChanSDs, pgApsSwitchCommand=pgApsSwitchCommand, pgApsProtChanStatus=pgApsProtChanStatus, pgApsProtChanIfIndex=pgApsProtChanIfIndex, pgApsMIBNotifications=pgApsMIBNotifications, pgApsConfigSigDegradeThresh=pgApsConfigSigDegradeThresh, pgApsTrapSwitchOver=pgApsTrapSwitchOver)
