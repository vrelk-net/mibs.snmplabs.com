#
# PySNMP MIB module ALTIGA-CERT-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALTIGA-CERT-STATS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:05:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
alCertMibModule, = mibBuilder.importSymbols("ALTIGA-GLOBAL-REG", "alCertMibModule")
alCertGroup, alStatsCert = mibBuilder.importSymbols("ALTIGA-MIB", "alCertGroup", "alStatsCert")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, MibIdentifier, Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, Counter64, Gauge32, Unsigned32, NotificationType, iso, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibIdentifier", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "Counter64", "Gauge32", "Unsigned32", "NotificationType", "iso", "TimeTicks", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
altigaCertStatsMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3076, 1, 1, 32, 2))
altigaCertStatsMibModule.setRevisions(('2002-09-05 13:00', '2002-07-10 00:00',))
if mibBuilder.loadTexts: altigaCertStatsMibModule.setLastUpdated('200209051300Z')
if mibBuilder.loadTexts: altigaCertStatsMibModule.setOrganization('Cisco Systems, Inc.')
alStatsCertGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 27, 1))
alCertStatsServerTable = MibTable((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 27, 2), )
if mibBuilder.loadTexts: alCertStatsServerTable.setStatus('current')
alCertStatsServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 27, 2, 1), ).setIndexNames((0, "ALTIGA-CERT-STATS-MIB", "alCertStatsServerIndex"))
if mibBuilder.loadTexts: alCertStatsServerEntry.setStatus('current')
alCertStatsServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 27, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alCertStatsServerIndex.setStatus('current')
alCertStatsServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 27, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alCertStatsServerAddress.setStatus('current')
alCertStatsServerPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 27, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alCertStatsServerPortNumber.setStatus('current')
alCertStatsServerCertRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 27, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alCertStatsServerCertRequests.setStatus('current')
alCertStatsServerCertRetransmissions = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 27, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alCertStatsServerCertRetransmissions.setStatus('current')
alCertStatsServerCertRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 27, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alCertStatsServerCertRcvd.setStatus('current')
alCertStatsServerCertPendingRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 27, 2, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alCertStatsServerCertPendingRequests.setStatus('current')
alCertStatsServerCertTimeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 27, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alCertStatsServerCertTimeouts.setStatus('current')
alCertStatsServerCRLRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 27, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alCertStatsServerCRLRequests.setStatus('current')
alCertStatsServerCRLRetransmissions = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 27, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alCertStatsServerCRLRetransmissions.setStatus('current')
alCertStatsServerCRLRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 27, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alCertStatsServerCRLRcvd.setStatus('current')
alCertStatsServerCRLPendingRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 27, 2, 1, 12), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alCertStatsServerCRLPendingRequests.setStatus('current')
alCertStatsServerCRLTimeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 27, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alCertStatsServerCRLTimeouts.setStatus('current')
altigaCertStatsMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 32, 2, 1))
altigaCertStatsMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3076, 1, 1, 32, 2, 1, 1))
altigaCertStatsMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3076, 1, 1, 32, 2, 1, 1, 1)).setObjects(("ALTIGA-CERT-STATS-MIB", "altigaCertStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaCertStatsMibCompliance = altigaCertStatsMibCompliance.setStatus('current')
altigaCertStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 27, 2)).setObjects(("ALTIGA-CERT-STATS-MIB", "alCertStatsServerIndex"), ("ALTIGA-CERT-STATS-MIB", "alCertStatsServerAddress"), ("ALTIGA-CERT-STATS-MIB", "alCertStatsServerPortNumber"), ("ALTIGA-CERT-STATS-MIB", "alCertStatsServerCertRequests"), ("ALTIGA-CERT-STATS-MIB", "alCertStatsServerCertRetransmissions"), ("ALTIGA-CERT-STATS-MIB", "alCertStatsServerCertRcvd"), ("ALTIGA-CERT-STATS-MIB", "alCertStatsServerCertPendingRequests"), ("ALTIGA-CERT-STATS-MIB", "alCertStatsServerCertTimeouts"), ("ALTIGA-CERT-STATS-MIB", "alCertStatsServerCRLRequests"), ("ALTIGA-CERT-STATS-MIB", "alCertStatsServerCRLRetransmissions"), ("ALTIGA-CERT-STATS-MIB", "alCertStatsServerCRLRcvd"), ("ALTIGA-CERT-STATS-MIB", "alCertStatsServerCRLPendingRequests"), ("ALTIGA-CERT-STATS-MIB", "alCertStatsServerCRLTimeouts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    altigaCertStatsGroup = altigaCertStatsGroup.setStatus('current')
mibBuilder.exportSymbols("ALTIGA-CERT-STATS-MIB", alCertStatsServerAddress=alCertStatsServerAddress, alCertStatsServerTable=alCertStatsServerTable, alCertStatsServerIndex=alCertStatsServerIndex, alCertStatsServerCertRequests=alCertStatsServerCertRequests, alCertStatsServerCRLPendingRequests=alCertStatsServerCRLPendingRequests, alCertStatsServerPortNumber=alCertStatsServerPortNumber, alCertStatsServerEntry=alCertStatsServerEntry, altigaCertStatsGroup=altigaCertStatsGroup, alStatsCertGlobal=alStatsCertGlobal, alCertStatsServerCertRetransmissions=alCertStatsServerCertRetransmissions, altigaCertStatsMibCompliance=altigaCertStatsMibCompliance, altigaCertStatsMibCompliances=altigaCertStatsMibCompliances, alCertStatsServerCRLTimeouts=alCertStatsServerCRLTimeouts, altigaCertStatsMibConformance=altigaCertStatsMibConformance, altigaCertStatsMibModule=altigaCertStatsMibModule, alCertStatsServerCertRcvd=alCertStatsServerCertRcvd, alCertStatsServerCRLRcvd=alCertStatsServerCRLRcvd, alCertStatsServerCRLRetransmissions=alCertStatsServerCRLRetransmissions, PYSNMP_MODULE_ID=altigaCertStatsMibModule, alCertStatsServerCertPendingRequests=alCertStatsServerCertPendingRequests, alCertStatsServerCRLRequests=alCertStatsServerCRLRequests, alCertStatsServerCertTimeouts=alCertStatsServerCertTimeouts)
