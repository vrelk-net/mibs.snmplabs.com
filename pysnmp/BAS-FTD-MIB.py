#
# PySNMP MIB module BAS-FTD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BAS-FTD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:17:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
basFtd, = mibBuilder.importSymbols("BAS-MIB", "basFtd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Gauge32, MibIdentifier, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, Bits, TimeTicks, Counter64, iso, ModuleIdentity, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "MibIdentifier", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "Bits", "TimeTicks", "Counter64", "iso", "ModuleIdentity", "Integer32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
basFtdMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3493, 2, 5, 1))
if mibBuilder.loadTexts: basFtdMib.setLastUpdated('9810071415Z')
if mibBuilder.loadTexts: basFtdMib.setOrganization('Broadband Access Systems')
basFtdObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1))
basFtdHeartBeatTimer = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basFtdHeartBeatTimer.setStatus('current')
basFtdTableEligibilityCounter = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basFtdTableEligibilityCounter.setStatus('current')
basFtdTableEligibilityCounterThreshold = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(5)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basFtdTableEligibilityCounterThreshold.setStatus('current')
basFtdIdleCounter = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basFtdIdleCounter.setStatus('current')
basFtdIdleCounterThreshold = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(5)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basFtdIdleCounterThreshold.setStatus('current')
basFtdTableRequestCounter = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basFtdTableRequestCounter.setStatus('current')
basFtdPendingCallbackCounter = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basFtdPendingCallbackCounter.setStatus('current')
basFtdPendingCallbackThreshold = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(10)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basFtdPendingCallbackThreshold.setStatus('current')
basFtdBootState = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("null", 1), ("cold", 2), ("warm", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basFtdBootState.setStatus('current')
basFtdPurgeConfiguration = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("immediate", 1), ("delayed", 2))).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basFtdPurgeConfiguration.setStatus('current')
basFtdUpdateRequests = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basFtdUpdateRequests.setStatus('current')
basFtdUpdatepackets = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basFtdUpdatepackets.setStatus('current')
basFtdTableRequests = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basFtdTableRequests.setStatus('current')
basFtdTablePackets = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basFtdTablePackets.setStatus('current')
basFtdAllocatedPackets = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basFtdAllocatedPackets.setStatus('current')
basFtdSentPackets = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basFtdSentPackets.setStatus('current')
basFtdFreedPackets = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basFtdFreedPackets.setStatus('current')
basFtdSpuriousUpdatePackets = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basFtdSpuriousUpdatePackets.setStatus('current')
basFtdSpuriousTablePackets = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basFtdSpuriousTablePackets.setStatus('current')
basFtdIgnoredUpdatePackets = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basFtdIgnoredUpdatePackets.setStatus('current')
basFtdIgnoredTablePackets = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basFtdIgnoredTablePackets.setStatus('current')
basFtdInstalledUpdatePackets = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basFtdInstalledUpdatePackets.setStatus('current')
basFtdInstalledTablePackets = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basFtdInstalledTablePackets.setStatus('current')
basFtdStoredTablePackets = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basFtdStoredTablePackets.setStatus('current')
basFtdRevisionPackets = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basFtdRevisionPackets.setStatus('current')
basFtdFailureCode = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109))).clone(namedValues=NamedValues(("finite-state-machine", 1), ("dequeue", 2), ("null-table-fia", 3), ("nonnull-update-pkt", 4), ("nonnull-table-pkt", 5), ("pending-threshold", 6), ("uninitialized-storage", 7), ("external", 100), ("rbp-registration", 101), ("unknown-pkt", 102), ("rbp-send", 103), ("rbp-callback", 104), ("packet-allocation", 105), ("packet-corruption", 106), ("rte-error-bad-prefix", 107), ("rte-error-bad-version", 108), ("add-route-failure", 109)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: basFtdFailureCode.setStatus('current')
basFtdRevision = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 27), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basFtdRevision.setStatus('current')
basFtdPresentFsmState = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 28), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basFtdPresentFsmState.setStatus('current')
basFtdFsmRestarts = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 5, 1, 1, 29), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basFtdFsmRestarts.setStatus('current')
mibBuilder.exportSymbols("BAS-FTD-MIB", basFtdTablePackets=basFtdTablePackets, basFtdFailureCode=basFtdFailureCode, basFtdTableRequestCounter=basFtdTableRequestCounter, basFtdHeartBeatTimer=basFtdHeartBeatTimer, basFtdTableEligibilityCounterThreshold=basFtdTableEligibilityCounterThreshold, basFtdInstalledTablePackets=basFtdInstalledTablePackets, basFtdSpuriousTablePackets=basFtdSpuriousTablePackets, basFtdTableEligibilityCounter=basFtdTableEligibilityCounter, basFtdObjects=basFtdObjects, basFtdMib=basFtdMib, basFtdTableRequests=basFtdTableRequests, basFtdFsmRestarts=basFtdFsmRestarts, basFtdStoredTablePackets=basFtdStoredTablePackets, basFtdInstalledUpdatePackets=basFtdInstalledUpdatePackets, basFtdSpuriousUpdatePackets=basFtdSpuriousUpdatePackets, basFtdUpdatepackets=basFtdUpdatepackets, basFtdSentPackets=basFtdSentPackets, basFtdPendingCallbackThreshold=basFtdPendingCallbackThreshold, basFtdIdleCounterThreshold=basFtdIdleCounterThreshold, basFtdIgnoredTablePackets=basFtdIgnoredTablePackets, basFtdPresentFsmState=basFtdPresentFsmState, basFtdUpdateRequests=basFtdUpdateRequests, basFtdFreedPackets=basFtdFreedPackets, basFtdRevision=basFtdRevision, basFtdRevisionPackets=basFtdRevisionPackets, basFtdAllocatedPackets=basFtdAllocatedPackets, PYSNMP_MODULE_ID=basFtdMib, basFtdPendingCallbackCounter=basFtdPendingCallbackCounter, basFtdIdleCounter=basFtdIdleCounter, basFtdPurgeConfiguration=basFtdPurgeConfiguration, basFtdIgnoredUpdatePackets=basFtdIgnoredUpdatePackets, basFtdBootState=basFtdBootState)
