#
# PySNMP MIB module XYLO-MODEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XYLO-MODEM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:39:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ObjectIdentity, Unsigned32, Integer32, TimeTicks, Bits, Gauge32, MibIdentifier, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ObjectIdentity", "Unsigned32", "Integer32", "TimeTicks", "Bits", "Gauge32", "MibIdentifier", "Counter64", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
anxModem, = mibBuilder.importSymbols("XYLO-MIB-SMI", "anxModem")
mdmIdObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 15, 2, 100, 3))
mdmCtlObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 15, 2, 100, 4))
mdmStatsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 15, 2, 100, 7))
mdmIdTable = MibTable((1, 3, 6, 1, 4, 1, 15, 2, 100, 3, 1), )
if mibBuilder.loadTexts: mdmIdTable.setStatus('mandatory')
mdmIdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15, 2, 100, 3, 1, 1), ).setIndexNames((0, "XYLO-MODEM-MIB", "mdmNumber"))
if mibBuilder.loadTexts: mdmIdEntry.setStatus('mandatory')
mdmNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 15, 2, 100, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmNumber.setStatus('mandatory')
mdmIdHardwareRev = MibTableColumn((1, 3, 6, 1, 4, 1, 15, 2, 100, 3, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmIdHardwareRev.setStatus('mandatory')
mdmIdSoftwareRev = MibTableColumn((1, 3, 6, 1, 4, 1, 15, 2, 100, 3, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmIdSoftwareRev.setStatus('mandatory')
mdmId56kProprietaryCode = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 100, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("x2-v34", 2), ("k56flex-v34", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmId56kProprietaryCode.setStatus('mandatory')
mdmCtlResetAll = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 100, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ready", 1), ("execute", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmCtlResetAll.setStatus('mandatory')
mdmCtlReadConfig = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 100, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ready", 1), ("execute", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmCtlReadConfig.setStatus('mandatory')
mdmCtlTable = MibTable((1, 3, 6, 1, 4, 1, 15, 2, 100, 4, 3), )
if mibBuilder.loadTexts: mdmCtlTable.setStatus('mandatory')
mdmCtlResetModemThresh = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 100, 4, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmCtlResetModemThresh.setStatus('mandatory')
mdmCtlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15, 2, 100, 4, 3, 1), ).setIndexNames((0, "XYLO-MODEM-MIB", "mdmNumber"))
if mibBuilder.loadTexts: mdmCtlEntry.setStatus('mandatory')
mdmCtlReset = MibTableColumn((1, 3, 6, 1, 4, 1, 15, 2, 100, 4, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ready", 1), ("execute", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmCtlReset.setStatus('mandatory')
mdmCtlState = MibTableColumn((1, 3, 6, 1, 4, 1, 15, 2, 100, 4, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("busy", 1), ("available", 2), ("busiedOut", 3), ("failed", 4), ("crashed", 5), ("outOfService", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmCtlState.setStatus('mandatory')
mdmStatTable = MibTable((1, 3, 6, 1, 4, 1, 15, 2, 100, 7, 1), )
if mibBuilder.loadTexts: mdmStatTable.setStatus('mandatory')
mdmStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15, 2, 100, 7, 1, 1), ).setIndexNames((0, "XYLO-MODEM-MIB", "mdmNumber"))
if mibBuilder.loadTexts: mdmStatEntry.setStatus('mandatory')
mdmStatAssign = MibTableColumn((1, 3, 6, 1, 4, 1, 15, 2, 100, 7, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmStatAssign.setStatus('mandatory')
mdmStatChat = MibTableColumn((1, 3, 6, 1, 4, 1, 15, 2, 100, 7, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmStatChat.setStatus('mandatory')
mdmStatDcd = MibTableColumn((1, 3, 6, 1, 4, 1, 15, 2, 100, 7, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmStatDcd.setStatus('mandatory')
mdmStatConsecFail = MibTableColumn((1, 3, 6, 1, 4, 1, 15, 2, 100, 7, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmStatConsecFail.setStatus('mandatory')
mdmStatStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 15, 2, 100, 7, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("busy", 1), ("available", 2), ("busiedOut", 3), ("failed", 4), ("crashed", 5), ("outOfService", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmStatStatus.setStatus('mandatory')
mdmStatTotCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 15, 2, 100, 7, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmStatTotCalls.setStatus('mandatory')
mdmStatTotFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 15, 2, 100, 7, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmStatTotFailures.setStatus('mandatory')
mdmAvailModems = MibScalar((1, 3, 6, 1, 4, 1, 15, 2, 100, 7, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmAvailModems.setStatus('mandatory')
mibBuilder.exportSymbols("XYLO-MODEM-MIB", mdmStatStatus=mdmStatStatus, mdmCtlState=mdmCtlState, mdmCtlReadConfig=mdmCtlReadConfig, mdmStatTotCalls=mdmStatTotCalls, mdmAvailModems=mdmAvailModems, mdmIdEntry=mdmIdEntry, mdmStatEntry=mdmStatEntry, mdmStatConsecFail=mdmStatConsecFail, mdmIdHardwareRev=mdmIdHardwareRev, mdmStatTable=mdmStatTable, mdmIdObjects=mdmIdObjects, mdmStatTotFailures=mdmStatTotFailures, mdmCtlTable=mdmCtlTable, mdmCtlObjects=mdmCtlObjects, mdmCtlResetModemThresh=mdmCtlResetModemThresh, mdmStatChat=mdmStatChat, mdmStatsObjects=mdmStatsObjects, mdmNumber=mdmNumber, mdmStatAssign=mdmStatAssign, mdmCtlReset=mdmCtlReset, mdmIdSoftwareRev=mdmIdSoftwareRev, mdmStatDcd=mdmStatDcd, mdmCtlResetAll=mdmCtlResetAll, mdmId56kProprietaryCode=mdmId56kProprietaryCode, mdmIdTable=mdmIdTable, mdmCtlEntry=mdmCtlEntry)
