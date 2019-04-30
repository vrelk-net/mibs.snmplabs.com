#
# PySNMP MIB module CISCO-AAA-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-AAA-SERVER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:32:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Unsigned32, Gauge32, MibIdentifier, Counter64, ModuleIdentity, Bits, IpAddress, TimeTicks, ObjectIdentity, iso, Counter32, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Gauge32", "MibIdentifier", "Counter64", "ModuleIdentity", "Bits", "IpAddress", "TimeTicks", "ObjectIdentity", "iso", "Counter32", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
RowStatus, TextualConvention, TimeInterval, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "TimeInterval", "DisplayString", "TruthValue")
ciscoAAAServerMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 56))
ciscoAAAServerMIB.setRevisions(('2003-11-17 00:00', '2002-03-28 00:00', '2000-01-20 00:00',))
if mibBuilder.loadTexts: ciscoAAAServerMIB.setLastUpdated('200311170000Z')
if mibBuilder.loadTexts: ciscoAAAServerMIB.setOrganization('Cisco Systems, Inc.')
class CiscoAAAProtocol(TextualConvention, Integer32):
    reference = ' RFC 2138 Remote Authentication Dial In User Service (RADIUS) RFC 2139 RADIUS Accounting The TACACS+ Protocol Version 1.78, Internet Draft '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("tacacsplus", 1), ("radius", 2), ("ldap", 3), ("kerberos", 4), ("ntlm", 5), ("sdi", 6), ("other", 7))

cAAAServerMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 56, 1))
casConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 1))
casStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2))
casServerStateChangeEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: casServerStateChangeEnable.setStatus('current')
casConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 1, 2), )
if mibBuilder.loadTexts: casConfigTable.setStatus('current')
casConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-AAA-SERVER-MIB", "casProtocol"), (0, "CISCO-AAA-SERVER-MIB", "casIndex"))
if mibBuilder.loadTexts: casConfigEntry.setStatus('current')
casProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 1, 2, 1, 1), CiscoAAAProtocol())
if mibBuilder.loadTexts: casProtocol.setStatus('current')
casIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 1, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: casIndex.setStatus('current')
casAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 1, 2, 1, 3), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: casAddress.setStatus('current')
casAuthenPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(1645)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: casAuthenPort.setStatus('current')
casAcctPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(1646)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: casAcctPort.setStatus('current')
casKey = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 1, 2, 1, 6), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: casKey.setStatus('current')
casPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 1, 2, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: casPriority.setStatus('current')
casConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 1, 2, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: casConfigRowStatus.setStatus('current')
casStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1), )
if mibBuilder.loadTexts: casStatisticsTable.setStatus('current')
casStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1), )
casConfigEntry.registerAugmentions(("CISCO-AAA-SERVER-MIB", "casStatisticsEntry"))
casStatisticsEntry.setIndexNames(*casConfigEntry.getIndexNames())
if mibBuilder.loadTexts: casStatisticsEntry.setStatus('current')
casAuthenRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casAuthenRequests.setStatus('current')
casAuthenRequestTimeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casAuthenRequestTimeouts.setStatus('current')
casAuthenUnexpectedResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casAuthenUnexpectedResponses.setStatus('current')
casAuthenServerErrorResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casAuthenServerErrorResponses.setStatus('current')
casAuthenIncorrectResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casAuthenIncorrectResponses.setStatus('current')
casAuthenResponseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 6), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casAuthenResponseTime.setStatus('current')
casAuthenTransactionSuccesses = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casAuthenTransactionSuccesses.setStatus('current')
casAuthenTransactionFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casAuthenTransactionFailures.setStatus('current')
casAuthorRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casAuthorRequests.setStatus('current')
casAuthorRequestTimeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casAuthorRequestTimeouts.setStatus('current')
casAuthorUnexpectedResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casAuthorUnexpectedResponses.setStatus('current')
casAuthorServerErrorResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casAuthorServerErrorResponses.setStatus('current')
casAuthorIncorrectResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casAuthorIncorrectResponses.setStatus('current')
casAuthorResponseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 14), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casAuthorResponseTime.setStatus('current')
casAuthorTransactionSuccesses = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casAuthorTransactionSuccesses.setStatus('current')
casAuthorTransactionFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casAuthorTransactionFailures.setStatus('current')
casAcctRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casAcctRequests.setStatus('current')
casAcctRequestTimeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casAcctRequestTimeouts.setStatus('current')
casAcctUnexpectedResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casAcctUnexpectedResponses.setStatus('current')
casAcctServerErrorResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casAcctServerErrorResponses.setStatus('current')
casAcctIncorrectResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casAcctIncorrectResponses.setStatus('current')
casAcctResponseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 22), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casAcctResponseTime.setStatus('current')
casAcctTransactionSuccesses = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casAcctTransactionSuccesses.setStatus('current')
casAcctTransactionFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casAcctTransactionFailures.setStatus('current')
casState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("dead", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: casState.setStatus('current')
casCurrentStateDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 26), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casCurrentStateDuration.setStatus('current')
casPreviousStateDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 27), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casPreviousStateDuration.setStatus('current')
casTotalDeadTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 28), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casTotalDeadTime.setStatus('current')
casDeadCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 56, 1, 2, 1, 1, 29), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: casDeadCount.setStatus('current')
cAAAServerMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 56, 2))
cAAAServerMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 56, 2, 0))
casServerStateChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 10, 56, 2, 0, 1)).setObjects(("CISCO-AAA-SERVER-MIB", "casState"), ("CISCO-AAA-SERVER-MIB", "casPreviousStateDuration"), ("CISCO-AAA-SERVER-MIB", "casTotalDeadTime"))
if mibBuilder.loadTexts: casServerStateChange.setStatus('current')
cAAAServerMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 56, 3))
casMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 56, 3, 1))
casMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 56, 3, 2))
casMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 56, 3, 1, 1)).setObjects(("CISCO-AAA-SERVER-MIB", "casConfigGroup"), ("CISCO-AAA-SERVER-MIB", "casStatisticsGroup"), ("CISCO-AAA-SERVER-MIB", "casServerNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    casMIBCompliance = casMIBCompliance.setStatus('current')
casStatisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 56, 3, 2, 1)).setObjects(("CISCO-AAA-SERVER-MIB", "casAuthenRequests"), ("CISCO-AAA-SERVER-MIB", "casAuthenRequestTimeouts"), ("CISCO-AAA-SERVER-MIB", "casAuthenUnexpectedResponses"), ("CISCO-AAA-SERVER-MIB", "casAuthenServerErrorResponses"), ("CISCO-AAA-SERVER-MIB", "casAuthenIncorrectResponses"), ("CISCO-AAA-SERVER-MIB", "casAuthenResponseTime"), ("CISCO-AAA-SERVER-MIB", "casAuthenTransactionSuccesses"), ("CISCO-AAA-SERVER-MIB", "casAuthenTransactionFailures"), ("CISCO-AAA-SERVER-MIB", "casAuthorRequests"), ("CISCO-AAA-SERVER-MIB", "casAuthorRequestTimeouts"), ("CISCO-AAA-SERVER-MIB", "casAuthorUnexpectedResponses"), ("CISCO-AAA-SERVER-MIB", "casAuthorServerErrorResponses"), ("CISCO-AAA-SERVER-MIB", "casAuthorIncorrectResponses"), ("CISCO-AAA-SERVER-MIB", "casAuthorResponseTime"), ("CISCO-AAA-SERVER-MIB", "casAuthorTransactionSuccesses"), ("CISCO-AAA-SERVER-MIB", "casAuthorTransactionFailures"), ("CISCO-AAA-SERVER-MIB", "casAcctRequests"), ("CISCO-AAA-SERVER-MIB", "casAcctRequestTimeouts"), ("CISCO-AAA-SERVER-MIB", "casAcctUnexpectedResponses"), ("CISCO-AAA-SERVER-MIB", "casAcctServerErrorResponses"), ("CISCO-AAA-SERVER-MIB", "casAcctIncorrectResponses"), ("CISCO-AAA-SERVER-MIB", "casAcctResponseTime"), ("CISCO-AAA-SERVER-MIB", "casAcctTransactionSuccesses"), ("CISCO-AAA-SERVER-MIB", "casAcctTransactionFailures"), ("CISCO-AAA-SERVER-MIB", "casState"), ("CISCO-AAA-SERVER-MIB", "casCurrentStateDuration"), ("CISCO-AAA-SERVER-MIB", "casPreviousStateDuration"), ("CISCO-AAA-SERVER-MIB", "casTotalDeadTime"), ("CISCO-AAA-SERVER-MIB", "casDeadCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    casStatisticsGroup = casStatisticsGroup.setStatus('current')
casConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 56, 3, 2, 2)).setObjects(("CISCO-AAA-SERVER-MIB", "casServerStateChangeEnable"), ("CISCO-AAA-SERVER-MIB", "casAddress"), ("CISCO-AAA-SERVER-MIB", "casAuthenPort"), ("CISCO-AAA-SERVER-MIB", "casAcctPort"), ("CISCO-AAA-SERVER-MIB", "casKey"), ("CISCO-AAA-SERVER-MIB", "casPriority"), ("CISCO-AAA-SERVER-MIB", "casConfigRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    casConfigGroup = casConfigGroup.setStatus('current')
casServerNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 10, 56, 3, 2, 3)).setObjects(("CISCO-AAA-SERVER-MIB", "casServerStateChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    casServerNotificationGroup = casServerNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-AAA-SERVER-MIB", casConfigEntry=casConfigEntry, casAuthenTransactionSuccesses=casAuthenTransactionSuccesses, casAcctRequestTimeouts=casAcctRequestTimeouts, casAuthorTransactionFailures=casAuthorTransactionFailures, casCurrentStateDuration=casCurrentStateDuration, cAAAServerMIBConformance=cAAAServerMIBConformance, casAcctServerErrorResponses=casAcctServerErrorResponses, cAAAServerMIBNotificationPrefix=cAAAServerMIBNotificationPrefix, casConfigTable=casConfigTable, casAcctTransactionSuccesses=casAcctTransactionSuccesses, casAuthorTransactionSuccesses=casAuthorTransactionSuccesses, casAuthenIncorrectResponses=casAuthenIncorrectResponses, casAcctResponseTime=casAcctResponseTime, casStatistics=casStatistics, casAuthorServerErrorResponses=casAuthorServerErrorResponses, casAcctUnexpectedResponses=casAcctUnexpectedResponses, casDeadCount=casDeadCount, casConfigGroup=casConfigGroup, casProtocol=casProtocol, casConfig=casConfig, cAAAServerMIBObjects=cAAAServerMIBObjects, casConfigRowStatus=casConfigRowStatus, casAuthenRequests=casAuthenRequests, casAuthorUnexpectedResponses=casAuthorUnexpectedResponses, PYSNMP_MODULE_ID=ciscoAAAServerMIB, casAcctTransactionFailures=casAcctTransactionFailures, casAuthorRequests=casAuthorRequests, casState=casState, casPreviousStateDuration=casPreviousStateDuration, casKey=casKey, casServerStateChange=casServerStateChange, casStatisticsGroup=casStatisticsGroup, CiscoAAAProtocol=CiscoAAAProtocol, ciscoAAAServerMIB=ciscoAAAServerMIB, casAuthorResponseTime=casAuthorResponseTime, casAuthorIncorrectResponses=casAuthorIncorrectResponses, casAuthenUnexpectedResponses=casAuthenUnexpectedResponses, casPriority=casPriority, casStatisticsEntry=casStatisticsEntry, casStatisticsTable=casStatisticsTable, casAuthenResponseTime=casAuthenResponseTime, casMIBCompliances=casMIBCompliances, casMIBGroups=casMIBGroups, casMIBCompliance=casMIBCompliance, casAuthenRequestTimeouts=casAuthenRequestTimeouts, casIndex=casIndex, casAcctRequests=casAcctRequests, casAuthenTransactionFailures=casAuthenTransactionFailures, casTotalDeadTime=casTotalDeadTime, cAAAServerMIBNotifications=cAAAServerMIBNotifications, casServerNotificationGroup=casServerNotificationGroup, casAcctPort=casAcctPort, casAuthenPort=casAuthenPort, casAddress=casAddress, casAuthenServerErrorResponses=casAuthenServerErrorResponses, casAuthorRequestTimeouts=casAuthorRequestTimeouts, casAcctIncorrectResponses=casAcctIncorrectResponses, casServerStateChangeEnable=casServerStateChangeEnable)
