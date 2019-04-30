#
# PySNMP MIB module KEYING-PRIVATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/KEYING-PRIVATE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:54:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
switch, = mibBuilder.importSymbols("QUANTA-SWITCH-MIB", "switch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Bits, Integer32, IpAddress, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter64, MibIdentifier, ObjectIdentity, ModuleIdentity, Counter32, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "Integer32", "IpAddress", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter64", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "Counter32", "TimeTicks", "Gauge32")
TextualConvention, RowStatus, DisplayString, RowPointer = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString", "RowPointer")
keyingPrivate = ModuleIdentity((1, 3, 6, 1, 4, 1, 7244, 2, 24))
if mibBuilder.loadTexts: keyingPrivate.setLastUpdated('201108310000Z')
if mibBuilder.loadTexts: keyingPrivate.setOrganization('QCI')
agentFeatureKeyingGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 7244, 2, 24, 1))
agentFeatureKeyingEnableKey = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 24, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentFeatureKeyingEnableKey.setStatus('current')
agentFeatureKeyingDisableKey = MibScalar((1, 3, 6, 1, 4, 1, 7244, 2, 24, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentFeatureKeyingDisableKey.setStatus('current')
agentFeatureKeyingTable = MibTable((1, 3, 6, 1, 4, 1, 7244, 2, 24, 1, 3), )
if mibBuilder.loadTexts: agentFeatureKeyingTable.setStatus('current')
agentFeatureKeyingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7244, 2, 24, 1, 3, 1), ).setIndexNames((0, "KEYING-PRIVATE-MIB", "agentFeatureKeyingIndex"))
if mibBuilder.loadTexts: agentFeatureKeyingEntry.setStatus('current')
agentFeatureKeyingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 24, 1, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: agentFeatureKeyingIndex.setStatus('current')
agentFeatureKeyingName = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 24, 1, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentFeatureKeyingName.setStatus('current')
agentFeatureKeyingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7244, 2, 24, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentFeatureKeyingStatus.setStatus('current')
mibBuilder.exportSymbols("KEYING-PRIVATE-MIB", agentFeatureKeyingStatus=agentFeatureKeyingStatus, agentFeatureKeyingIndex=agentFeatureKeyingIndex, agentFeatureKeyingEnableKey=agentFeatureKeyingEnableKey, agentFeatureKeyingDisableKey=agentFeatureKeyingDisableKey, agentFeatureKeyingTable=agentFeatureKeyingTable, agentFeatureKeyingEntry=agentFeatureKeyingEntry, agentFeatureKeyingGroup=agentFeatureKeyingGroup, PYSNMP_MODULE_ID=keyingPrivate, agentFeatureKeyingName=agentFeatureKeyingName, keyingPrivate=keyingPrivate)