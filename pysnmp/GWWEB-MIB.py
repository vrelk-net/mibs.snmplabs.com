#
# PySNMP MIB module GWWEB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GWWEB-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:07:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Counter64, IpAddress, MibIdentifier, Integer32, iso, ObjectIdentity, NotificationType, Bits, Unsigned32, ModuleIdentity, enterprises, Counter32, TimeTicks, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter64", "IpAddress", "MibIdentifier", "Integer32", "iso", "ObjectIdentity", "NotificationType", "Bits", "Unsigned32", "ModuleIdentity", "enterprises", "Counter32", "TimeTicks", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
novell = MibIdentifier((1, 3, 6, 1, 4, 1, 23))
mibDoc = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2))
gwWeb = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 77))
gwWebAccess = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 77, 1))
gwWebAccessTable = MibTable((1, 3, 6, 1, 4, 1, 23, 2, 77, 1, 1), )
if mibBuilder.loadTexts: gwWebAccessTable.setStatus('mandatory')
webAccessEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23, 2, 77, 1, 1, 1), ).setIndexNames((0, "GWWEB-MIB", "gwWebAccessIndex"))
if mibBuilder.loadTexts: webAccessEntry.setStatus('mandatory')
gwWebAccessIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 77, 1, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gwWebAccessIndex.setStatus('mandatory')
gwWebAccessName = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 77, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gwWebAccessName.setStatus('mandatory')
gwWebAccessCompletedRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 77, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gwWebAccessCompletedRequests.setStatus('mandatory')
gwWebAccessFailedRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 77, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gwWebAccessFailedRequests.setStatus('mandatory')
gwWebAccessTotalThreads = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 77, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gwWebAccessTotalThreads.setStatus('mandatory')
gwWebAccessBusyThreads = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 77, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gwWebAccessBusyThreads.setStatus('mandatory')
gwWebAccessPeakBusyThreads = MibScalar((1, 3, 6, 1, 4, 1, 23, 2, 77, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gwWebAccessPeakBusyThreads.setStatus('mandatory')
gwWebAccessCurrentUsers = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 77, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gwWebAccessCurrentUsers.setStatus('mandatory')
gwWebAccessTotalUsers = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 77, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gwWebAccessTotalUsers.setStatus('mandatory')
gwWebAccessPeakUsers = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 77, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gwWebAccessPeakUsers.setStatus('mandatory')
gwWebAccessUptime = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 77, 1, 1, 1, 11), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gwWebAccessUptime.setStatus('mandatory')
gwWebAccessOS = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 77, 1, 1, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gwWebAccessOS.setStatus('mandatory')
gwWebAccessVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 77, 1, 1, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gwWebAccessVersion.setStatus('mandatory')
gwWebAccessHTTPPort = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 77, 1, 1, 1, 14), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gwWebAccessHTTPPort.setStatus('mandatory')
mibBuilder.exportSymbols("GWWEB-MIB", gwWebAccess=gwWebAccess, gwWebAccessCompletedRequests=gwWebAccessCompletedRequests, gwWebAccessTotalUsers=gwWebAccessTotalUsers, gwWebAccessName=gwWebAccessName, mibDoc=mibDoc, gwWebAccessIndex=gwWebAccessIndex, gwWebAccessPeakUsers=gwWebAccessPeakUsers, gwWebAccessTotalThreads=gwWebAccessTotalThreads, gwWebAccessCurrentUsers=gwWebAccessCurrentUsers, gwWebAccessPeakBusyThreads=gwWebAccessPeakBusyThreads, gwWeb=gwWeb, gwWebAccessHTTPPort=gwWebAccessHTTPPort, gwWebAccessOS=gwWebAccessOS, gwWebAccessUptime=gwWebAccessUptime, gwWebAccessFailedRequests=gwWebAccessFailedRequests, gwWebAccessVersion=gwWebAccessVersion, webAccessEntry=webAccessEntry, gwWebAccessBusyThreads=gwWebAccessBusyThreads, gwWebAccessTable=gwWebAccessTable, novell=novell)