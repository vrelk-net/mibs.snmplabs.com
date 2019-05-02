#
# PySNMP MIB module BIANCA-BRICK-X25STAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BIANCA-BRICK-X25STAT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:38:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
DisplayString, = mibBuilder.importSymbols("RFC1158-MIB", "DisplayString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, MibIdentifier, iso, Counter32, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType, Integer32, ObjectIdentity, Gauge32, Unsigned32, ModuleIdentity, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibIdentifier", "iso", "Counter32", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType", "Integer32", "ObjectIdentity", "Gauge32", "Unsigned32", "ModuleIdentity", "enterprises")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bintec = MibIdentifier((1, 3, 6, 1, 4, 1, 272))
bibo = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4))
x25 = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 6))
x25statMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 6, 16))
x25SwStats = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 1))
x25MuxStats = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 2))
x25ToTcpStats = MibIdentifier((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3))
x25SwIncomingAttempts = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25SwIncomingAttempts.setStatus('mandatory')
if mibBuilder.loadTexts: x25SwIncomingAttempts.setDescription('')
x25SwIncomingSucceeded = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25SwIncomingSucceeded.setStatus('mandatory')
if mibBuilder.loadTexts: x25SwIncomingSucceeded.setDescription('')
x25SwIncomingFailed = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25SwIncomingFailed.setStatus('mandatory')
if mibBuilder.loadTexts: x25SwIncomingFailed.setDescription('')
x25SwIncCurrentCalls = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25SwIncCurrentCalls.setStatus('mandatory')
if mibBuilder.loadTexts: x25SwIncCurrentCalls.setDescription('')
x25SwIncMaxConcCalls = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25SwIncMaxConcCalls.setStatus('mandatory')
if mibBuilder.loadTexts: x25SwIncMaxConcCalls.setDescription('')
x25SwIncCurrentPending = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25SwIncCurrentPending.setStatus('mandatory')
if mibBuilder.loadTexts: x25SwIncCurrentPending.setDescription('')
x25SwIncMaxConcPending = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25SwIncMaxConcPending.setStatus('mandatory')
if mibBuilder.loadTexts: x25SwIncMaxConcPending.setDescription('')
x25SwIncFailedTimeout = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25SwIncFailedTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: x25SwIncFailedTimeout.setDescription('')
x25SwOutgoingAttempts = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25SwOutgoingAttempts.setStatus('mandatory')
if mibBuilder.loadTexts: x25SwOutgoingAttempts.setDescription('')
x25SwOutgoingSucceeded = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25SwOutgoingSucceeded.setStatus('mandatory')
if mibBuilder.loadTexts: x25SwOutgoingSucceeded.setDescription('')
x25SwOutgoingFailed = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25SwOutgoingFailed.setStatus('mandatory')
if mibBuilder.loadTexts: x25SwOutgoingFailed.setDescription('')
x25SwOutCurrentCalls = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25SwOutCurrentCalls.setStatus('mandatory')
if mibBuilder.loadTexts: x25SwOutCurrentCalls.setDescription('')
x25SwOutMaxConcCalls = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25SwOutMaxConcCalls.setStatus('mandatory')
if mibBuilder.loadTexts: x25SwOutMaxConcCalls.setDescription('')
x25SwOutCurrentPending = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25SwOutCurrentPending.setStatus('mandatory')
if mibBuilder.loadTexts: x25SwOutCurrentPending.setDescription('')
x25SwOutMaxConcPending = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25SwOutMaxConcPending.setStatus('mandatory')
if mibBuilder.loadTexts: x25SwOutMaxConcPending.setDescription('')
x25SwOutFailedTimeout = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25SwOutFailedTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: x25SwOutFailedTimeout.setDescription('')
x25SwCallCnt = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25SwCallCnt.setStatus('mandatory')
if mibBuilder.loadTexts: x25SwCallCnt.setDescription('')
x25MuxIncomingAttempts = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25MuxIncomingAttempts.setStatus('mandatory')
if mibBuilder.loadTexts: x25MuxIncomingAttempts.setDescription('')
x25MuxIncomingSucceeded = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25MuxIncomingSucceeded.setStatus('mandatory')
if mibBuilder.loadTexts: x25MuxIncomingSucceeded.setDescription('')
x25MuxIncomingFailed = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25MuxIncomingFailed.setStatus('mandatory')
if mibBuilder.loadTexts: x25MuxIncomingFailed.setDescription('')
x25MuxIncCurrentCalls = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 2, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25MuxIncCurrentCalls.setStatus('mandatory')
if mibBuilder.loadTexts: x25MuxIncCurrentCalls.setDescription('')
x25MuxIncMaxConcCalls = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 2, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25MuxIncMaxConcCalls.setStatus('mandatory')
if mibBuilder.loadTexts: x25MuxIncMaxConcCalls.setDescription('')
x25MuxIncCurrentPending = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 2, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25MuxIncCurrentPending.setStatus('mandatory')
if mibBuilder.loadTexts: x25MuxIncCurrentPending.setDescription('')
x25MuxIncMaxConcPending = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 2, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25MuxIncMaxConcPending.setStatus('mandatory')
if mibBuilder.loadTexts: x25MuxIncMaxConcPending.setDescription('')
x25MuxIncResets = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 2, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25MuxIncResets.setStatus('mandatory')
if mibBuilder.loadTexts: x25MuxIncResets.setDescription('')
x25MuxOutgoingAttempts = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 2, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25MuxOutgoingAttempts.setStatus('mandatory')
if mibBuilder.loadTexts: x25MuxOutgoingAttempts.setDescription('')
x25MuxOutgoingSucceeded = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 2, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25MuxOutgoingSucceeded.setStatus('mandatory')
if mibBuilder.loadTexts: x25MuxOutgoingSucceeded.setDescription('')
x25MuxOutgoingFailed = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 2, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25MuxOutgoingFailed.setStatus('mandatory')
if mibBuilder.loadTexts: x25MuxOutgoingFailed.setDescription('')
x25MuxOutCurrentCalls = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 2, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25MuxOutCurrentCalls.setStatus('mandatory')
if mibBuilder.loadTexts: x25MuxOutCurrentCalls.setDescription('')
x25MuxOutMaxConcCalls = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 2, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25MuxOutMaxConcCalls.setStatus('mandatory')
if mibBuilder.loadTexts: x25MuxOutMaxConcCalls.setDescription('')
x25MuxOutCurrentPending = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 2, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25MuxOutCurrentPending.setStatus('mandatory')
if mibBuilder.loadTexts: x25MuxOutCurrentPending.setDescription('')
x25MuxOutMaxConcPending = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 2, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25MuxOutMaxConcPending.setStatus('mandatory')
if mibBuilder.loadTexts: x25MuxOutMaxConcPending.setDescription('')
x25MuxOutResets = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 2, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25MuxOutResets.setStatus('mandatory')
if mibBuilder.loadTexts: x25MuxOutResets.setDescription('')
x25MuxInstCnt = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 2, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25MuxInstCnt.setStatus('mandatory')
if mibBuilder.loadTexts: x25MuxInstCnt.setDescription('')
x25ToTcpRestart = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2))).clone('no')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: x25ToTcpRestart.setStatus('mandatory')
if mibBuilder.loadTexts: x25ToTcpRestart.setDescription('')
x25ToTcpCurrentRestart = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25ToTcpCurrentRestart.setStatus('mandatory')
if mibBuilder.loadTexts: x25ToTcpCurrentRestart.setDescription('')
x25ToTcpTotalRestart = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25ToTcpTotalRestart.setStatus('mandatory')
if mibBuilder.loadTexts: x25ToTcpTotalRestart.setDescription('')
x25ToTcpIncX25Attempts = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25ToTcpIncX25Attempts.setStatus('mandatory')
if mibBuilder.loadTexts: x25ToTcpIncX25Attempts.setDescription('')
x25ToTcpIncX25Succeeded = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25ToTcpIncX25Succeeded.setStatus('mandatory')
if mibBuilder.loadTexts: x25ToTcpIncX25Succeeded.setDescription('')
x25ToTcpIncX25Failed = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25ToTcpIncX25Failed.setStatus('mandatory')
if mibBuilder.loadTexts: x25ToTcpIncX25Failed.setDescription('')
x25ToTcpOutTcpAttempts = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25ToTcpOutTcpAttempts.setStatus('mandatory')
if mibBuilder.loadTexts: x25ToTcpOutTcpAttempts.setDescription('')
x25ToTcpOutTcpSucceeded = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25ToTcpOutTcpSucceeded.setStatus('mandatory')
if mibBuilder.loadTexts: x25ToTcpOutTcpSucceeded.setDescription('')
x25ToTcpOutTcpFailed = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25ToTcpOutTcpFailed.setStatus('mandatory')
if mibBuilder.loadTexts: x25ToTcpOutTcpFailed.setDescription('')
x25ToTcpIncX25CurrentCalls = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25ToTcpIncX25CurrentCalls.setStatus('mandatory')
if mibBuilder.loadTexts: x25ToTcpIncX25CurrentCalls.setDescription('')
x25ToTcpIncX25MaxConcCalls = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25ToTcpIncX25MaxConcCalls.setStatus('mandatory')
if mibBuilder.loadTexts: x25ToTcpIncX25MaxConcCalls.setDescription('')
x25ToTcpIncX25CurrentPending = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25ToTcpIncX25CurrentPending.setStatus('mandatory')
if mibBuilder.loadTexts: x25ToTcpIncX25CurrentPending.setDescription('')
x25ToTcpIncX25MaxConcPending = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25ToTcpIncX25MaxConcPending.setStatus('mandatory')
if mibBuilder.loadTexts: x25ToTcpIncX25MaxConcPending.setDescription('')
x25ToTcpIncTcpAttempts = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25ToTcpIncTcpAttempts.setStatus('mandatory')
if mibBuilder.loadTexts: x25ToTcpIncTcpAttempts.setDescription('')
x25ToTcpIncTcpSucceeded = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25ToTcpIncTcpSucceeded.setStatus('mandatory')
if mibBuilder.loadTexts: x25ToTcpIncTcpSucceeded.setDescription('')
x25ToTcpIncTcpFailed = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25ToTcpIncTcpFailed.setStatus('mandatory')
if mibBuilder.loadTexts: x25ToTcpIncTcpFailed.setDescription('')
x25ToTcpOutX25Attempts = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25ToTcpOutX25Attempts.setStatus('mandatory')
if mibBuilder.loadTexts: x25ToTcpOutX25Attempts.setDescription('')
x25ToTcpOutX25Succeeded = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25ToTcpOutX25Succeeded.setStatus('mandatory')
if mibBuilder.loadTexts: x25ToTcpOutX25Succeeded.setDescription('')
x25ToTcpOutX25Failed = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25ToTcpOutX25Failed.setStatus('mandatory')
if mibBuilder.loadTexts: x25ToTcpOutX25Failed.setDescription('')
x25ToTcpIncTcpCurrentCalls = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25ToTcpIncTcpCurrentCalls.setStatus('mandatory')
if mibBuilder.loadTexts: x25ToTcpIncTcpCurrentCalls.setDescription('')
x25ToTcpIncTcpMaxConcCalls = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25ToTcpIncTcpMaxConcCalls.setStatus('mandatory')
if mibBuilder.loadTexts: x25ToTcpIncTcpMaxConcCalls.setDescription('')
x25ToTcpIncTcpCurrentPending = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25ToTcpIncTcpCurrentPending.setStatus('mandatory')
if mibBuilder.loadTexts: x25ToTcpIncTcpCurrentPending.setDescription('')
x25ToTcpIncTcpMaxConcPending = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25ToTcpIncTcpMaxConcPending.setStatus('mandatory')
if mibBuilder.loadTexts: x25ToTcpIncTcpMaxConcPending.setDescription('')
x25ToTcpUEvTcpListen = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25ToTcpUEvTcpListen.setStatus('mandatory')
if mibBuilder.loadTexts: x25ToTcpUEvTcpListen.setDescription('')
x25ToTcpUEvTcpData = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25ToTcpUEvTcpData.setStatus('mandatory')
if mibBuilder.loadTexts: x25ToTcpUEvTcpData.setDescription('')
x25ToTcpUEvX25Listen = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25ToTcpUEvX25Listen.setStatus('mandatory')
if mibBuilder.loadTexts: x25ToTcpUEvX25Listen.setDescription('')
x25ToTcpUEvX25Data = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25ToTcpUEvX25Data.setStatus('mandatory')
if mibBuilder.loadTexts: x25ToTcpUEvX25Data.setDescription('')
x25ToTcpX25CanPutEvDisc = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25ToTcpX25CanPutEvDisc.setStatus('mandatory')
if mibBuilder.loadTexts: x25ToTcpX25CanPutEvDisc.setDescription('')
x25ToTcpX25CanPutEvTok = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 29), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25ToTcpX25CanPutEvTok.setStatus('mandatory')
if mibBuilder.loadTexts: x25ToTcpX25CanPutEvTok.setDescription('')
x25ToTcpX25CanPutEvReset = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25ToTcpX25CanPutEvReset.setStatus('mandatory')
if mibBuilder.loadTexts: x25ToTcpX25CanPutEvReset.setDescription('')
x25ToTcpTcpCanPutEvDisc = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25ToTcpTcpCanPutEvDisc.setStatus('mandatory')
if mibBuilder.loadTexts: x25ToTcpTcpCanPutEvDisc.setDescription('')
x25ToTcpTcpCanPutEvTok = MibScalar((1, 3, 6, 1, 4, 1, 272, 4, 6, 16, 3, 32), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: x25ToTcpTcpCanPutEvTok.setStatus('mandatory')
if mibBuilder.loadTexts: x25ToTcpTcpCanPutEvTok.setDescription('')
mibBuilder.exportSymbols("BIANCA-BRICK-X25STAT-MIB", x25SwOutMaxConcPending=x25SwOutMaxConcPending, x25MuxIncMaxConcCalls=x25MuxIncMaxConcCalls, x25MuxOutMaxConcPending=x25MuxOutMaxConcPending, x25ToTcpIncTcpMaxConcPending=x25ToTcpIncTcpMaxConcPending, x25MuxIncomingSucceeded=x25MuxIncomingSucceeded, x25MuxOutCurrentCalls=x25MuxOutCurrentCalls, x25ToTcpIncX25Attempts=x25ToTcpIncX25Attempts, x25SwOutgoingSucceeded=x25SwOutgoingSucceeded, x25SwOutCurrentCalls=x25SwOutCurrentCalls, x25SwIncomingSucceeded=x25SwIncomingSucceeded, x25ToTcpIncX25Failed=x25ToTcpIncX25Failed, x25ToTcpCurrentRestart=x25ToTcpCurrentRestart, x25ToTcpTcpCanPutEvDisc=x25ToTcpTcpCanPutEvDisc, x25SwStats=x25SwStats, x25SwOutCurrentPending=x25SwOutCurrentPending, x25MuxIncomingFailed=x25MuxIncomingFailed, x25ToTcpOutX25Failed=x25ToTcpOutX25Failed, x25MuxIncCurrentCalls=x25MuxIncCurrentCalls, x25ToTcpIncTcpFailed=x25ToTcpIncTcpFailed, x25SwIncMaxConcCalls=x25SwIncMaxConcCalls, x25MuxStats=x25MuxStats, x25ToTcpStats=x25ToTcpStats, x25ToTcpX25CanPutEvTok=x25ToTcpX25CanPutEvTok, x25ToTcpTcpCanPutEvTok=x25ToTcpTcpCanPutEvTok, x25ToTcpIncX25CurrentCalls=x25ToTcpIncX25CurrentCalls, x25ToTcpX25CanPutEvReset=x25ToTcpX25CanPutEvReset, x25ToTcpIncTcpCurrentPending=x25ToTcpIncTcpCurrentPending, x25ToTcpIncX25MaxConcCalls=x25ToTcpIncX25MaxConcCalls, x25SwOutMaxConcCalls=x25SwOutMaxConcCalls, x25ToTcpOutTcpAttempts=x25ToTcpOutTcpAttempts, x25ToTcpOutTcpFailed=x25ToTcpOutTcpFailed, x25SwIncCurrentCalls=x25SwIncCurrentCalls, x25statMIB=x25statMIB, x25SwOutgoingFailed=x25SwOutgoingFailed, x25ToTcpTotalRestart=x25ToTcpTotalRestart, x25ToTcpRestart=x25ToTcpRestart, x25ToTcpIncTcpAttempts=x25ToTcpIncTcpAttempts, x25ToTcpIncX25CurrentPending=x25ToTcpIncX25CurrentPending, x25ToTcpUEvTcpData=x25ToTcpUEvTcpData, x25SwIncomingFailed=x25SwIncomingFailed, x25MuxOutgoingFailed=x25MuxOutgoingFailed, x25ToTcpIncTcpMaxConcCalls=x25ToTcpIncTcpMaxConcCalls, x25ToTcpUEvX25Listen=x25ToTcpUEvX25Listen, x25MuxOutgoingSucceeded=x25MuxOutgoingSucceeded, x25ToTcpIncTcpCurrentCalls=x25ToTcpIncTcpCurrentCalls, x25ToTcpX25CanPutEvDisc=x25ToTcpX25CanPutEvDisc, x25MuxOutResets=x25MuxOutResets, x25MuxOutgoingAttempts=x25MuxOutgoingAttempts, x25ToTcpIncX25MaxConcPending=x25ToTcpIncX25MaxConcPending, x25ToTcpOutTcpSucceeded=x25ToTcpOutTcpSucceeded, x25SwIncFailedTimeout=x25SwIncFailedTimeout, x25MuxIncomingAttempts=x25MuxIncomingAttempts, x25ToTcpUEvTcpListen=x25ToTcpUEvTcpListen, bibo=bibo, bintec=bintec, x25ToTcpOutX25Attempts=x25ToTcpOutX25Attempts, x25SwIncMaxConcPending=x25SwIncMaxConcPending, x25SwIncomingAttempts=x25SwIncomingAttempts, x25MuxIncMaxConcPending=x25MuxIncMaxConcPending, x25MuxOutMaxConcCalls=x25MuxOutMaxConcCalls, x25MuxIncCurrentPending=x25MuxIncCurrentPending, x25=x25, x25MuxIncResets=x25MuxIncResets, x25ToTcpUEvX25Data=x25ToTcpUEvX25Data, x25SwOutgoingAttempts=x25SwOutgoingAttempts, x25MuxOutCurrentPending=x25MuxOutCurrentPending, x25ToTcpOutX25Succeeded=x25ToTcpOutX25Succeeded, x25SwIncCurrentPending=x25SwIncCurrentPending, x25SwCallCnt=x25SwCallCnt, x25MuxInstCnt=x25MuxInstCnt, x25ToTcpIncTcpSucceeded=x25ToTcpIncTcpSucceeded, x25SwOutFailedTimeout=x25SwOutFailedTimeout, x25ToTcpIncX25Succeeded=x25ToTcpIncX25Succeeded)