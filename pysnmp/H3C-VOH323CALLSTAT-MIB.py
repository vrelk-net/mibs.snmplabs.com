#
# PySNMP MIB module H3C-VOH323CALLSTAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-VOH323CALLSTAT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:11:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
h3cVoice, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cVoice")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, Gauge32, iso, Counter32, TimeTicks, MibIdentifier, Bits, NotificationType, ObjectIdentity, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "Gauge32", "iso", "Counter32", "TimeTicks", "MibIdentifier", "Bits", "NotificationType", "ObjectIdentity", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
h3cVoiceH323CallStat = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 11))
h3cVoiceH323CallStat.setRevisions(('2005-03-15 00:00',))
if mibBuilder.loadTexts: h3cVoiceH323CallStat.setLastUpdated('200503150000Z')
if mibBuilder.loadTexts: h3cVoiceH323CallStat.setOrganization('Huawei-3COM Technologies Co., Ltd.')
h3cVOIPH225StatTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 11, 1), )
if mibBuilder.loadTexts: h3cVOIPH225StatTable.setStatus('current')
h3cVOIPH225StatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 11, 1, 1), ).setIndexNames((0, "H3C-VOH323CALLSTAT-MIB", "h3cH225MsgIndex"))
if mibBuilder.loadTexts: h3cVOIPH225StatEntry.setStatus('current')
h3cH225MsgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 11, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cH225MsgIndex.setStatus('current')
h3cH225MsgName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 11, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cH225MsgName.setStatus('current')
h3cH225MsgSend = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 11, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cH225MsgSend.setStatus('current')
h3cH225MsgReceive = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 11, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cH225MsgReceive.setStatus('current')
h3cVOIPH245StatTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 11, 2), )
if mibBuilder.loadTexts: h3cVOIPH245StatTable.setStatus('current')
h3cVOIPH245StatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 11, 2, 1), ).setIndexNames((0, "H3C-VOH323CALLSTAT-MIB", "h3cH245MsgIndex"))
if mibBuilder.loadTexts: h3cVOIPH245StatEntry.setStatus('current')
h3cH245MsgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 11, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cH245MsgIndex.setStatus('current')
h3cH245MsgName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 11, 2, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cH245MsgName.setStatus('current')
h3cH245MsgSend = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 11, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cH245MsgSend.setStatus('current')
h3cH245MsgReceive = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 11, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cH245MsgReceive.setStatus('current')
h3cVOIPRasStatTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 11, 3), )
if mibBuilder.loadTexts: h3cVOIPRasStatTable.setStatus('current')
h3cVOIPRasStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 11, 3, 1), ).setIndexNames((0, "H3C-VOH323CALLSTAT-MIB", "h3cRasMsgIndex"))
if mibBuilder.loadTexts: h3cVOIPRasStatEntry.setStatus('current')
h3cRasMsgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 11, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cRasMsgIndex.setStatus('current')
h3cRasMsgName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 11, 3, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRasMsgName.setStatus('current')
h3cRasMsgSend = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 11, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRasMsgSend.setStatus('current')
h3cRasMsgReceive = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 11, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRasMsgReceive.setStatus('current')
mibBuilder.exportSymbols("H3C-VOH323CALLSTAT-MIB", h3cH225MsgSend=h3cH225MsgSend, h3cVOIPH245StatTable=h3cVOIPH245StatTable, h3cH225MsgReceive=h3cH225MsgReceive, h3cH225MsgName=h3cH225MsgName, h3cH245MsgName=h3cH245MsgName, h3cVOIPH225StatEntry=h3cVOIPH225StatEntry, PYSNMP_MODULE_ID=h3cVoiceH323CallStat, h3cVoiceH323CallStat=h3cVoiceH323CallStat, h3cVOIPRasStatTable=h3cVOIPRasStatTable, h3cRasMsgName=h3cRasMsgName, h3cH245MsgReceive=h3cH245MsgReceive, h3cVOIPRasStatEntry=h3cVOIPRasStatEntry, h3cRasMsgSend=h3cRasMsgSend, h3cRasMsgReceive=h3cRasMsgReceive, h3cH225MsgIndex=h3cH225MsgIndex, h3cH245MsgSend=h3cH245MsgSend, h3cVOIPH245StatEntry=h3cVOIPH245StatEntry, h3cRasMsgIndex=h3cRasMsgIndex, h3cH245MsgIndex=h3cH245MsgIndex, h3cVOIPH225StatTable=h3cVOIPH225StatTable)