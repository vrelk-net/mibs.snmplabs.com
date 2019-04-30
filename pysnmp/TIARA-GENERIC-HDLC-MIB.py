#
# PySNMP MIB module TIARA-GENERIC-HDLC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TIARA-GENERIC-HDLC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:08:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, NotificationType, Counter32, IpAddress, MibIdentifier, ObjectIdentity, Integer32, ModuleIdentity, Bits, Unsigned32, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "NotificationType", "Counter32", "IpAddress", "MibIdentifier", "ObjectIdentity", "Integer32", "ModuleIdentity", "Bits", "Unsigned32", "Gauge32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bundleId, = mibBuilder.importSymbols("TIARA-BUNDLE-MIB", "bundleId")
tiaraMgmt, = mibBuilder.importSymbols("TIARA-NETWORKS-SMI", "tiaraMgmt")
tiaraGenHdlcMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3174, 2, 15))
if mibBuilder.loadTexts: tiaraGenHdlcMib.setLastUpdated('9907010000Z')
if mibBuilder.loadTexts: tiaraGenHdlcMib.setOrganization('Tiara Networks Inc.')
genHdlcTable = MibTable((1, 3, 6, 1, 4, 1, 3174, 2, 15, 1), )
if mibBuilder.loadTexts: genHdlcTable.setStatus('current')
genHdlcTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3174, 2, 15, 1, 1), ).setIndexNames((0, "TIARA-BUNDLE-MIB", "bundleId"))
if mibBuilder.loadTexts: genHdlcTableEntry.setStatus('current')
genHdlcKeepAlive = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 15, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 120)).clone(10)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: genHdlcKeepAlive.setStatus('current')
genHdlcMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 15, 1, 1, 2), Integer32().clone(1500)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: genHdlcMtu.setStatus('current')
genHdlcStatsTable = MibTable((1, 3, 6, 1, 4, 1, 3174, 2, 15, 2), )
if mibBuilder.loadTexts: genHdlcStatsTable.setStatus('current')
genHdlcStatsTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3174, 2, 15, 2, 1), ).setIndexNames((0, "TIARA-BUNDLE-MIB", "bundleId"))
if mibBuilder.loadTexts: genHdlcStatsTableEntry.setStatus('current')
genHdlcStatsBytesRxLastBootClear = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 15, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: genHdlcStatsBytesRxLastBootClear.setStatus('current')
genHdlcStatsBytesTxLastBootClear = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 15, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: genHdlcStatsBytesTxLastBootClear.setStatus('current')
genHdlcStatsPktsRxLastBootClear = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 15, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: genHdlcStatsPktsRxLastBootClear.setStatus('current')
genHdlcStatsPktsTxLastBootClear = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 15, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: genHdlcStatsPktsTxLastBootClear.setStatus('current')
genHdlcStatsErrPktsRxLastBootClear = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 15, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: genHdlcStatsErrPktsRxLastBootClear.setStatus('current')
genHdlcStatsUpDownStatesLastBootClear = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 15, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: genHdlcStatsUpDownStatesLastBootClear.setStatus('current')
genHdlcStatsBytesRxLastFiveMins = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 15, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: genHdlcStatsBytesRxLastFiveMins.setStatus('current')
genHdlcStatsBytesTxLastFiveMins = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 15, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: genHdlcStatsBytesTxLastFiveMins.setStatus('current')
genHdlcStatsPktsRxLastFiveMins = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 15, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: genHdlcStatsPktsRxLastFiveMins.setStatus('current')
genHdlcStatsPktsTxLastFiveMins = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 15, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: genHdlcStatsPktsTxLastFiveMins.setStatus('current')
genHdlcStatsErrPktsRxLastFiveMins = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 15, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: genHdlcStatsErrPktsRxLastFiveMins.setStatus('current')
genHdlcStatsUpDownStatesLastFiveMins = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 15, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: genHdlcStatsUpDownStatesLastFiveMins.setStatus('current')
mibBuilder.exportSymbols("TIARA-GENERIC-HDLC-MIB", genHdlcStatsUpDownStatesLastBootClear=genHdlcStatsUpDownStatesLastBootClear, genHdlcMtu=genHdlcMtu, genHdlcStatsBytesTxLastFiveMins=genHdlcStatsBytesTxLastFiveMins, genHdlcStatsTableEntry=genHdlcStatsTableEntry, genHdlcStatsPktsRxLastBootClear=genHdlcStatsPktsRxLastBootClear, PYSNMP_MODULE_ID=tiaraGenHdlcMib, genHdlcStatsBytesRxLastFiveMins=genHdlcStatsBytesRxLastFiveMins, genHdlcStatsTable=genHdlcStatsTable, genHdlcKeepAlive=genHdlcKeepAlive, genHdlcTable=genHdlcTable, genHdlcStatsErrPktsRxLastBootClear=genHdlcStatsErrPktsRxLastBootClear, genHdlcStatsErrPktsRxLastFiveMins=genHdlcStatsErrPktsRxLastFiveMins, genHdlcStatsBytesRxLastBootClear=genHdlcStatsBytesRxLastBootClear, genHdlcStatsPktsTxLastBootClear=genHdlcStatsPktsTxLastBootClear, genHdlcStatsUpDownStatesLastFiveMins=genHdlcStatsUpDownStatesLastFiveMins, genHdlcStatsBytesTxLastBootClear=genHdlcStatsBytesTxLastBootClear, genHdlcStatsPktsRxLastFiveMins=genHdlcStatsPktsRxLastFiveMins, tiaraGenHdlcMib=tiaraGenHdlcMib, genHdlcTableEntry=genHdlcTableEntry, genHdlcStatsPktsTxLastFiveMins=genHdlcStatsPktsTxLastFiveMins)
