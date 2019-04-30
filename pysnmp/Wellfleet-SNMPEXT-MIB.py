#
# PySNMP MIB module Wellfleet-SNMPEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-SNMPEXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:35:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Gauge32, TimeTicks, NotificationType, ModuleIdentity, Counter64, Counter32, ObjectIdentity, Unsigned32, MibIdentifier, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Gauge32", "TimeTicks", "NotificationType", "ModuleIdentity", "Counter64", "Counter32", "ObjectIdentity", "Unsigned32", "MibIdentifier", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits")
AutonomousType, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "AutonomousType", "DisplayString", "TextualConvention")
wfSnmpGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfSnmpGroup")
wfSnmp = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1))
wfSnmpDisable = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSnmpDisable.setStatus('mandatory')
wfSnmpUseLock = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSnmpUseLock.setStatus('mandatory')
wfSnmpLockAddress = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSnmpLockAddress.setStatus('mandatory')
wfSnmpLockTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSnmpLockTimeOut.setStatus('mandatory')
wfSnmpAuth = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("trivial", 1), ("party", 2), ("proprietary", 3))).clone('trivial')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpAuth.setStatus('mandatory')
wfSnmpInPkts = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpInPkts.setStatus('mandatory')
wfSnmpOutPkts = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpOutPkts.setStatus('mandatory')
wfSnmpInBadVersions = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpInBadVersions.setStatus('mandatory')
wfSnmpInBadCommunityNames = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpInBadCommunityNames.setStatus('mandatory')
wfSnmpInBadCommunityUses = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpInBadCommunityUses.setStatus('mandatory')
wfSnmpInASNParseErrs = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpInASNParseErrs.setStatus('mandatory')
wfSnmpInBadTypes = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpInBadTypes.setStatus('mandatory')
wfSnmpInTooBigs = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpInTooBigs.setStatus('mandatory')
wfSnmpInNoSuchNames = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpInNoSuchNames.setStatus('mandatory')
wfSnmpInBadValues = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpInBadValues.setStatus('mandatory')
wfSnmpInReadOnlys = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpInReadOnlys.setStatus('mandatory')
wfSnmpInGenErrs = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpInGenErrs.setStatus('mandatory')
wfSnmpInTotalReqVars = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpInTotalReqVars.setStatus('mandatory')
wfSnmpInTotalSetVars = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpInTotalSetVars.setStatus('mandatory')
wfSnmpInGetRequests = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpInGetRequests.setStatus('mandatory')
wfSnmpInGetNexts = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpInGetNexts.setStatus('mandatory')
wfSnmpInSetRequests = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpInSetRequests.setStatus('mandatory')
wfSnmpInGetResponses = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpInGetResponses.setStatus('mandatory')
wfSnmpInTraps = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpInTraps.setStatus('mandatory')
wfSnmpOutTooBigs = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpOutTooBigs.setStatus('mandatory')
wfSnmpOutNoSuchNames = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpOutNoSuchNames.setStatus('mandatory')
wfSnmpOutBadValues = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpOutBadValues.setStatus('mandatory')
wfSnmpOutReadOnlys = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpOutReadOnlys.setStatus('mandatory')
wfSnmpOutGenErrs = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 29), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpOutGenErrs.setStatus('mandatory')
wfSnmpOutGetRequests = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpOutGetRequests.setStatus('mandatory')
wfSnmpOutGetNexts = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpOutGetNexts.setStatus('mandatory')
wfSnmpOutSetRequests = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 32), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpOutSetRequests.setStatus('mandatory')
wfSnmpOutGetResponses = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 33), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpOutGetResponses.setStatus('mandatory')
wfSnmpOutTraps = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 34), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpOutTraps.setStatus('mandatory')
wfSnmpEnableAuthTraps = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 35), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSnmpEnableAuthTraps.setStatus('mandatory')
wfSnmpTrapDebug = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 36), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2))).clone('on')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSnmpTrapDebug.setStatus('obsolete')
wfSnmpTrapTrace = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 37), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2))).clone('on')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSnmpTrapTrace.setStatus('obsolete')
wfSnmpTrapInfo = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 38), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2))).clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSnmpTrapInfo.setStatus('obsolete')
wfSnmpTrapWarn = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 39), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2))).clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSnmpTrapWarn.setStatus('obsolete')
wfSnmpTrapFault = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 40), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2))).clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSnmpTrapFault.setStatus('obsolete')
wfSnmpIpTos = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 41), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("reliability", 2))).clone('reliability')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSnmpIpTos.setStatus('obsolete')
wfSnmpPropEncryption = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 42), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("wflt", 1), ("others", 2))).clone('wflt')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpPropEncryption.setStatus('mandatory')
wfSnmpPDUThreads = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 43), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 20)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSnmpPDUThreads.setStatus('mandatory')
wfSnmpBusyPDUThreads = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 44), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpBusyPDUThreads.setStatus('mandatory')
wfSnmpLogLevel = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 45), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("apall", 1), ("aperror", 2), ("apwarn", 3), ("aptrace", 4), ("aptraceerr", 5), ("aptracewarn", 6), ("aperrwarn", 7), ("apnone", 8))).clone('apnone')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSnmpLogLevel.setStatus('mandatory')
wfSnmpDelete = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 46), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSnmpDelete.setStatus('mandatory')
wfSnmpScopeDelimiter = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 47), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1).clone('@')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSnmpScopeDelimiter.setStatus('mandatory')
wfSnmpMaxInPktChain = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 1, 48), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128)).clone(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSnmpMaxInPktChain.setStatus('mandatory')
wfSnmpCommTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 2), )
if mibBuilder.loadTexts: wfSnmpCommTable.setStatus('mandatory')
wfSnmpCommEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 2, 1), ).setIndexNames((0, "Wellfleet-SNMPEXT-MIB", "wfSnmpCommIndex"))
if mibBuilder.loadTexts: wfSnmpCommEntry.setStatus('mandatory')
wfSnmpCommDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSnmpCommDelete.setStatus('mandatory')
wfSnmpCommIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpCommIndex.setStatus('mandatory')
wfSnmpCommName = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 2, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSnmpCommName.setStatus('mandatory')
wfSnmpCommAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("read-only", 1), ("read-write", 2))).clone('read-only')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSnmpCommAccess.setStatus('mandatory')
wfSnmpCommScopeType = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 2, 1, 5), AutonomousType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSnmpCommScopeType.setStatus('mandatory')
wfSnmpCommViewIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 2, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSnmpCommViewIndex.setStatus('mandatory')
wfSnmpMgrTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 3), )
if mibBuilder.loadTexts: wfSnmpMgrTable.setStatus('mandatory')
wfSnmpMgrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 3, 1), ).setIndexNames((0, "Wellfleet-SNMPEXT-MIB", "wfSnmpMgrCommIndex"), (0, "Wellfleet-SNMPEXT-MIB", "wfSnmpMgrAddress"))
if mibBuilder.loadTexts: wfSnmpMgrEntry.setStatus('mandatory')
wfSnmpMgrDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSnmpMgrDelete.setStatus('mandatory')
wfSnmpMgrCommIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpMgrCommIndex.setStatus('mandatory')
wfSnmpMgrAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 3, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpMgrAddress.setStatus('mandatory')
wfSnmpMgrName = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 3, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSnmpMgrName.setStatus('mandatory')
wfSnmpMgrTrapPort = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 3, 1, 5), Integer32().clone(162)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSnmpMgrTrapPort.setStatus('mandatory')
wfSnmpMgrTraps = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 7))).clone(namedValues=NamedValues(("none", 1), ("generic", 2), ("specific", 4), ("all", 7))).clone('generic')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSnmpMgrTraps.setStatus('mandatory')
wfSnmpMgrEncrSeed1 = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 3, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpMgrEncrSeed1.setStatus('mandatory')
wfSnmpMgrEncrSeed2 = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 3, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpMgrEncrSeed2.setStatus('mandatory')
wfSnmpMgrEncrSeed3 = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 3, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpMgrEncrSeed3.setStatus('mandatory')
wfSnmpMgrEncrSeed4 = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 3, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpMgrEncrSeed4.setStatus('mandatory')
wfSnmpMgrEncrSeed5 = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 3, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpMgrEncrSeed5.setStatus('mandatory')
wfSnmpMgrCircuitlessTrap = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 3, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSnmpMgrCircuitlessTrap.setStatus('mandatory')
wfSnmpTrapEntityTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 5), )
if mibBuilder.loadTexts: wfSnmpTrapEntityTable.setStatus('mandatory')
wfSnmpTrapEntityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 5, 1), ).setIndexNames((0, "Wellfleet-SNMPEXT-MIB", "wfSnmpTrapEntityNumber"), (0, "Wellfleet-SNMPEXT-MIB", "wfSnmpTrapEntitySlot"))
if mibBuilder.loadTexts: wfSnmpTrapEntityEntry.setStatus('mandatory')
wfSnmpTrapEntityDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSnmpTrapEntityDelete.setStatus('mandatory')
wfSnmpTrapEntityDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSnmpTrapEntityDisable.setStatus('mandatory')
wfSnmpTrapEntityNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpTrapEntityNumber.setStatus('mandatory')
wfSnmpTrapEntitySlot = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 5, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpTrapEntitySlot.setStatus('mandatory')
wfSnmpTrapEntityName = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 5, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpTrapEntityName.setStatus('mandatory')
wfSnmpTrapEntityFault = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 5, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2))).clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSnmpTrapEntityFault.setStatus('mandatory')
wfSnmpTrapEntityWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 5, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2))).clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSnmpTrapEntityWarn.setStatus('mandatory')
wfSnmpTrapEntityInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 5, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2))).clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSnmpTrapEntityInfo.setStatus('mandatory')
wfSnmpTrapEntityTrace = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 5, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2))).clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSnmpTrapEntityTrace.setStatus('mandatory')
wfSnmpTrapEntityDebug = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 5, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2))).clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSnmpTrapEntityDebug.setStatus('mandatory')
wfSnmpTrapEventTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 6), )
if mibBuilder.loadTexts: wfSnmpTrapEventTable.setStatus('mandatory')
wfSnmpTrapEventEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 6, 1), ).setIndexNames((0, "Wellfleet-SNMPEXT-MIB", "wfSnmpTrapEventEntity"), (0, "Wellfleet-SNMPEXT-MIB", "wfSnmpTrapEventNumber"))
if mibBuilder.loadTexts: wfSnmpTrapEventEntry.setStatus('mandatory')
wfSnmpTrapEventDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 6, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSnmpTrapEventDelete.setStatus('mandatory')
wfSnmpTrapEventDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSnmpTrapEventDisable.setStatus('mandatory')
wfSnmpTrapEventEntity = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 6, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpTrapEventEntity.setStatus('mandatory')
wfSnmpTrapEventNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 6, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpTrapEventNumber.setStatus('mandatory')
wfSnmpTrapEventName = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 6, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpTrapEventName.setStatus('mandatory')
wfSnmpViewTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 7), )
if mibBuilder.loadTexts: wfSnmpViewTable.setStatus('mandatory')
wfSnmpViewEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 7, 1), ).setIndexNames((0, "Wellfleet-SNMPEXT-MIB", "wfSnmpViewIndex"), (0, "Wellfleet-SNMPEXT-MIB", "wfSnmpViewSubtree"))
if mibBuilder.loadTexts: wfSnmpViewEntry.setStatus('mandatory')
wfSnmpViewDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 7, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSnmpViewDelete.setStatus('mandatory')
wfSnmpViewIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 7, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpViewIndex.setStatus('mandatory')
wfSnmpViewSubtree = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 7, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfSnmpViewSubtree.setStatus('mandatory')
wfSnmpViewName = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 7, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSnmpViewName.setStatus('mandatory')
wfSnmpViewTree = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 7, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSnmpViewTree.setStatus('mandatory')
wfSnmpViewType = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 5, 7, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("included", 1), ("excluded", 2))).clone('included')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfSnmpViewType.setStatus('mandatory')
mibBuilder.exportSymbols("Wellfleet-SNMPEXT-MIB", wfSnmpInTotalReqVars=wfSnmpInTotalReqVars, wfSnmpInBadCommunityUses=wfSnmpInBadCommunityUses, wfSnmpTrapEntityInfo=wfSnmpTrapEntityInfo, wfSnmpOutGetNexts=wfSnmpOutGetNexts, wfSnmpCommViewIndex=wfSnmpCommViewIndex, wfSnmpMgrEntry=wfSnmpMgrEntry, wfSnmpLockAddress=wfSnmpLockAddress, wfSnmpIpTos=wfSnmpIpTos, wfSnmpMgrEncrSeed2=wfSnmpMgrEncrSeed2, wfSnmpOutNoSuchNames=wfSnmpOutNoSuchNames, wfSnmpInGetResponses=wfSnmpInGetResponses, wfSnmpCommEntry=wfSnmpCommEntry, wfSnmpViewType=wfSnmpViewType, wfSnmpOutGetRequests=wfSnmpOutGetRequests, wfSnmpLockTimeOut=wfSnmpLockTimeOut, wfSnmpTrapTrace=wfSnmpTrapTrace, wfSnmpViewIndex=wfSnmpViewIndex, wfSnmpMgrAddress=wfSnmpMgrAddress, wfSnmpInPkts=wfSnmpInPkts, wfSnmpAuth=wfSnmpAuth, wfSnmpInBadVersions=wfSnmpInBadVersions, wfSnmpOutSetRequests=wfSnmpOutSetRequests, wfSnmpOutGenErrs=wfSnmpOutGenErrs, wfSnmpCommScopeType=wfSnmpCommScopeType, wfSnmpInBadValues=wfSnmpInBadValues, wfSnmpTrapEntityDisable=wfSnmpTrapEntityDisable, wfSnmpInReadOnlys=wfSnmpInReadOnlys, wfSnmpTrapFault=wfSnmpTrapFault, wfSnmpTrapEventDisable=wfSnmpTrapEventDisable, wfSnmpInTooBigs=wfSnmpInTooBigs, wfSnmpDelete=wfSnmpDelete, wfSnmpEnableAuthTraps=wfSnmpEnableAuthTraps, wfSnmpMgrTrapPort=wfSnmpMgrTrapPort, wfSnmpTrapEntityTable=wfSnmpTrapEntityTable, wfSnmpTrapEntityNumber=wfSnmpTrapEntityNumber, wfSnmpTrapEntitySlot=wfSnmpTrapEntitySlot, wfSnmpInBadTypes=wfSnmpInBadTypes, wfSnmpOutTooBigs=wfSnmpOutTooBigs, wfSnmpTrapEventNumber=wfSnmpTrapEventNumber, wfSnmpTrapInfo=wfSnmpTrapInfo, wfSnmpBusyPDUThreads=wfSnmpBusyPDUThreads, wfSnmpInTraps=wfSnmpInTraps, wfSnmpCommName=wfSnmpCommName, wfSnmpMgrDelete=wfSnmpMgrDelete, wfSnmpMgrEncrSeed5=wfSnmpMgrEncrSeed5, wfSnmpScopeDelimiter=wfSnmpScopeDelimiter, wfSnmpTrapEntityName=wfSnmpTrapEntityName, wfSnmpInGetNexts=wfSnmpInGetNexts, wfSnmpTrapEventTable=wfSnmpTrapEventTable, wfSnmpViewTable=wfSnmpViewTable, wfSnmpMgrEncrSeed1=wfSnmpMgrEncrSeed1, wfSnmpInSetRequests=wfSnmpInSetRequests, wfSnmpViewEntry=wfSnmpViewEntry, wfSnmp=wfSnmp, wfSnmpTrapEventEntry=wfSnmpTrapEventEntry, wfSnmpInTotalSetVars=wfSnmpInTotalSetVars, wfSnmpMgrCircuitlessTrap=wfSnmpMgrCircuitlessTrap, wfSnmpInBadCommunityNames=wfSnmpInBadCommunityNames, wfSnmpTrapEntityEntry=wfSnmpTrapEntityEntry, wfSnmpInASNParseErrs=wfSnmpInASNParseErrs, wfSnmpOutGetResponses=wfSnmpOutGetResponses, wfSnmpInGetRequests=wfSnmpInGetRequests, wfSnmpTrapWarn=wfSnmpTrapWarn, wfSnmpTrapEntityFault=wfSnmpTrapEntityFault, wfSnmpTrapEventDelete=wfSnmpTrapEventDelete, wfSnmpTrapEntityWarn=wfSnmpTrapEntityWarn, wfSnmpOutReadOnlys=wfSnmpOutReadOnlys, wfSnmpTrapEventEntity=wfSnmpTrapEventEntity, wfSnmpViewTree=wfSnmpViewTree, wfSnmpLogLevel=wfSnmpLogLevel, wfSnmpDisable=wfSnmpDisable, wfSnmpTrapDebug=wfSnmpTrapDebug, wfSnmpInNoSuchNames=wfSnmpInNoSuchNames, wfSnmpCommDelete=wfSnmpCommDelete, wfSnmpViewName=wfSnmpViewName, wfSnmpMgrName=wfSnmpMgrName, wfSnmpViewDelete=wfSnmpViewDelete, wfSnmpMgrCommIndex=wfSnmpMgrCommIndex, wfSnmpCommIndex=wfSnmpCommIndex, wfSnmpPropEncryption=wfSnmpPropEncryption, wfSnmpViewSubtree=wfSnmpViewSubtree, wfSnmpOutTraps=wfSnmpOutTraps, wfSnmpInGenErrs=wfSnmpInGenErrs, wfSnmpOutBadValues=wfSnmpOutBadValues, wfSnmpCommTable=wfSnmpCommTable, wfSnmpPDUThreads=wfSnmpPDUThreads, wfSnmpMgrEncrSeed4=wfSnmpMgrEncrSeed4, wfSnmpTrapEntityDebug=wfSnmpTrapEntityDebug, wfSnmpTrapEventName=wfSnmpTrapEventName, wfSnmpOutPkts=wfSnmpOutPkts, wfSnmpTrapEntityTrace=wfSnmpTrapEntityTrace, wfSnmpMaxInPktChain=wfSnmpMaxInPktChain, wfSnmpUseLock=wfSnmpUseLock, wfSnmpMgrTraps=wfSnmpMgrTraps, wfSnmpMgrTable=wfSnmpMgrTable, wfSnmpCommAccess=wfSnmpCommAccess, wfSnmpTrapEntityDelete=wfSnmpTrapEntityDelete, wfSnmpMgrEncrSeed3=wfSnmpMgrEncrSeed3)