#
# PySNMP MIB module PANDATEL-FX-MODEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PANDATEL-FX-MODEM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:28:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
device_id, mdmSpecifics = mibBuilder.importSymbols("PANDATEL-MODEM-MIB", "device-id", "mdmSpecifics")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, ModuleIdentity, Gauge32, iso, enterprises, IpAddress, ObjectIdentity, Counter64, MibIdentifier, NotificationType, Unsigned32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "Gauge32", "iso", "enterprises", "IpAddress", "ObjectIdentity", "Counter64", "MibIdentifier", "NotificationType", "Unsigned32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fx_modem = MibIdentifier((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 2, 502)).setLabel("fx-modem")
fx = MibIdentifier((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 502))
fxModemTable = MibTable((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 502, 1), )
if mibBuilder.loadTexts: fxModemTable.setStatus('mandatory')
fxTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 502, 1, 1), ).setIndexNames((0, "PANDATEL-FX-MODEM-MIB", "mdmRack"), (0, "PANDATEL-FX-MODEM-MIB", "mdmModem"), (0, "PANDATEL-FX-MODEM-MIB", "mdmPosition"))
if mibBuilder.loadTexts: fxTableEntry.setStatus('mandatory')
mdmRack = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 502, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmRack.setStatus('mandatory')
mdmModem = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 502, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmModem.setStatus('mandatory')
mdmPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 502, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("local", 1), ("remote", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmPosition.setStatus('mandatory')
mdmModemName = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 502, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmModemName.setStatus('mandatory')
mdmRemoteAccessMode = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 502, 1, 1, 64), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 5))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmRemoteAccessMode.setStatus('mandatory')
mdmForcedRemoteAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 502, 1, 1, 65), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmForcedRemoteAccess.setStatus('mandatory')
mdmClockRecovery = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 502, 1, 1, 70), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 100))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("stm1-oc3-155mbps", 3), ("stm4-oc12-622mbps", 4), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmClockRecovery.setStatus('mandatory')
mdmInterfaceAlarmCondition = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 502, 1, 1, 98), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 100))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("no-link-signal", 3), ("laser-fail", 4), ("no-link-signal-or-laser-fail", 5), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmInterfaceAlarmCondition.setStatus('mandatory')
mdmLineAlarmCondition = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 502, 1, 1, 99), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 100))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("no-link-signal", 3), ("laser-fail", 4), ("no-link-signal-or-laser-fail", 5), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmLineAlarmCondition.setStatus('mandatory')
mibBuilder.exportSymbols("PANDATEL-FX-MODEM-MIB", mdmPosition=mdmPosition, mdmModemName=mdmModemName, mdmRemoteAccessMode=mdmRemoteAccessMode, mdmClockRecovery=mdmClockRecovery, mdmLineAlarmCondition=mdmLineAlarmCondition, mdmRack=mdmRack, fxModemTable=fxModemTable, mdmForcedRemoteAccess=mdmForcedRemoteAccess, fx_modem=fx_modem, mdmModem=mdmModem, mdmInterfaceAlarmCondition=mdmInterfaceAlarmCondition, fx=fx, fxTableEntry=fxTableEntry)
