#
# PySNMP MIB module ZXROS-AMAT-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZXROS-AMAT-IF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:42:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, iso, Gauge32, ObjectIdentity, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, MibIdentifier, NotificationType, ModuleIdentity, Counter64, TimeTicks, Integer32, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "Gauge32", "ObjectIdentity", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "MibIdentifier", "NotificationType", "ModuleIdentity", "Counter64", "TimeTicks", "Integer32", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
zte = MibIdentifier((1, 3, 6, 1, 4, 1, 3902))
zxros = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 100))
zxrosAMATIF = MibIdentifier((1, 3, 6, 1, 4, 1, 3902, 100, 1001))
zxrosAMATInterfaceEnableTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 100, 1001, 1), )
if mibBuilder.loadTexts: zxrosAMATInterfaceEnableTable.setStatus('current')
zxrosAMATInterfaceEnableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 100, 1001, 1, 1), ).setIndexNames((0, "ZXROS-AMAT-IF-MIB", "zxrosAMATInterfaceEnableIfIndex"))
if mibBuilder.loadTexts: zxrosAMATInterfaceEnableEntry.setStatus('current')
zxrosAMATInterfaceEnableIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 100, 1001, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxrosAMATInterfaceEnableIfIndex.setStatus('current')
zxrosAMATInterfaceInAmatEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 100, 1001, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxrosAMATInterfaceInAmatEnable.setStatus('current')
zxrosAMATInterfaceOutAmatEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 100, 1001, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zxrosAMATInterfaceOutAmatEnable.setStatus('current')
zxrosAMATInterfaceStatisticTable = MibTable((1, 3, 6, 1, 4, 1, 3902, 100, 1001, 2), )
if mibBuilder.loadTexts: zxrosAMATInterfaceStatisticTable.setStatus('current')
zxrosAMATInterfaceStatisticEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3902, 100, 1001, 2, 1), ).setIndexNames((0, "ZXROS-AMAT-IF-MIB", "zxrosAMATInterfaceStatisticIfIndex"))
if mibBuilder.loadTexts: zxrosAMATInterfaceStatisticEntry.setStatus('current')
zxrosAMATInterfaceStatisticIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 100, 1001, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxrosAMATInterfaceStatisticIfIndex.setStatus('current')
zxrosAMATInFilterpackets = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 100, 1001, 2, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxrosAMATInFilterpackets.setStatus('current')
zxrosAMATOutFilterpackets = MibTableColumn((1, 3, 6, 1, 4, 1, 3902, 100, 1001, 2, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zxrosAMATOutFilterpackets.setStatus('current')
mibBuilder.exportSymbols("ZXROS-AMAT-IF-MIB", zxrosAMATInterfaceOutAmatEnable=zxrosAMATInterfaceOutAmatEnable, zxrosAMATInFilterpackets=zxrosAMATInFilterpackets, zxrosAMATInterfaceEnableIfIndex=zxrosAMATInterfaceEnableIfIndex, zxrosAMATInterfaceStatisticIfIndex=zxrosAMATInterfaceStatisticIfIndex, zxrosAMATOutFilterpackets=zxrosAMATOutFilterpackets, zxrosAMATInterfaceEnableEntry=zxrosAMATInterfaceEnableEntry, zxrosAMATInterfaceInAmatEnable=zxrosAMATInterfaceInAmatEnable, zte=zte, zxrosAMATInterfaceEnableTable=zxrosAMATInterfaceEnableTable, zxrosAMATInterfaceStatisticEntry=zxrosAMATInterfaceStatisticEntry, zxrosAMATInterfaceStatisticTable=zxrosAMATInterfaceStatisticTable, zxros=zxros, zxrosAMATIF=zxrosAMATIF)
