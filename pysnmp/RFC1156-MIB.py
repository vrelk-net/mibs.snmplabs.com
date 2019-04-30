#
# PySNMP MIB module RFC1156-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RFC1156-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:47:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
mgmt, TimeTicks, Integer32, ModuleIdentity, iso, Counter32, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter64, ObjectIdentity, IpAddress, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "mgmt", "TimeTicks", "Integer32", "ModuleIdentity", "iso", "Counter32", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter64", "ObjectIdentity", "IpAddress", "Unsigned32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mib = MibIdentifier((1, 3, 6, 1, 2, 1))
system = MibIdentifier((1, 3, 6, 1, 2, 1, 1))
interfaces = MibIdentifier((1, 3, 6, 1, 2, 1, 2))
at = MibIdentifier((1, 3, 6, 1, 2, 1, 3))
ip = MibIdentifier((1, 3, 6, 1, 2, 1, 4))
icmp = MibIdentifier((1, 3, 6, 1, 2, 1, 5))
tcp = MibIdentifier((1, 3, 6, 1, 2, 1, 6))
udp = MibIdentifier((1, 3, 6, 1, 2, 1, 7))
egp = MibIdentifier((1, 3, 6, 1, 2, 1, 8))
sysDescr = MibScalar((1, 3, 6, 1, 2, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysDescr.setStatus('mandatory')
sysObjectID = MibScalar((1, 3, 6, 1, 2, 1, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysObjectID.setStatus('mandatory')
sysUpTime = MibScalar((1, 3, 6, 1, 2, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysUpTime.setStatus('mandatory')
ifNumber = MibScalar((1, 3, 6, 1, 2, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifNumber.setStatus('mandatory')
ifTable = MibTable((1, 3, 6, 1, 2, 1, 2, 2), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifTable.setStatus('mandatory')
ifEntry = MibTableRow((1, 3, 6, 1, 2, 1, 2, 2, 1), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifEntry.setStatus('mandatory')
ifIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifIndex.setStatus('mandatory')
ifDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 2, 2, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifDescr.setStatus('mandatory')
ifType = MibTableColumn((1, 3, 6, 1, 2, 1, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22))).clone(namedValues=NamedValues(("other", 1), ("regular1822", 2), ("hdh1822", 3), ("ddn-x25", 4), ("rfc877-x25", 5), ("ethernet-csmacd", 6), ("iso88023-csmacd", 7), ("iso88024-tokenBus", 8), ("iso88025-tokenRing", 9), ("iso88026-man", 10), ("starLan", 11), ("proteon-10MBit", 12), ("proteon-80MBit", 13), ("hyperchannel", 14), ("fddi", 15), ("lapb", 16), ("sdlc", 17), ("t1-carrier", 18), ("cept", 19), ("basicIsdn", 20), ("primaryIsdn", 21), ("propPointToPointSerial", 22)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifType.setStatus('mandatory')
ifMtu = MibTableColumn((1, 3, 6, 1, 2, 1, 2, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifMtu.setStatus('mandatory')
ifSpeed = MibTableColumn((1, 3, 6, 1, 2, 1, 2, 2, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifSpeed.setStatus('mandatory')
ifPhysAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 2, 2, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifPhysAddress.setStatus('mandatory')
ifAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifAdminStatus.setStatus('mandatory')
ifOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifOperStatus.setStatus('mandatory')
ifLastChange = MibTableColumn((1, 3, 6, 1, 2, 1, 2, 2, 1, 9), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifLastChange.setStatus('mandatory')
ifInOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 2, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifInOctets.setStatus('mandatory')
ifInUcastPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 2, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifInUcastPkts.setStatus('mandatory')
ifInNUcastPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 2, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifInNUcastPkts.setStatus('mandatory')
ifInDiscards = MibTableColumn((1, 3, 6, 1, 2, 1, 2, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifInDiscards.setStatus('mandatory')
ifInErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 2, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifInErrors.setStatus('mandatory')
ifInUnknownProtos = MibTableColumn((1, 3, 6, 1, 2, 1, 2, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifInUnknownProtos.setStatus('mandatory')
ifOutOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 2, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifOutOctets.setStatus('mandatory')
ifOutUcastPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 2, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifOutUcastPkts.setStatus('mandatory')
ifOutNUcastPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 2, 2, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifOutNUcastPkts.setStatus('mandatory')
ifOutDiscards = MibTableColumn((1, 3, 6, 1, 2, 1, 2, 2, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifOutDiscards.setStatus('mandatory')
ifOutErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 2, 2, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifOutErrors.setStatus('mandatory')
ifOutQLen = MibTableColumn((1, 3, 6, 1, 2, 1, 2, 2, 1, 21), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifOutQLen.setStatus('mandatory')
atTable = MibTable((1, 3, 6, 1, 2, 1, 3, 1), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atTable.setStatus('mandatory')
atEntry = MibTableRow((1, 3, 6, 1, 2, 1, 3, 1, 1), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atEntry.setStatus('mandatory')
atIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 3, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atIfIndex.setStatus('mandatory')
atPhysAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 3, 1, 1, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atPhysAddress.setStatus('mandatory')
atNetAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 3, 1, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atNetAddress.setStatus('mandatory')
ipForwarding = MibScalar((1, 3, 6, 1, 2, 1, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("gateway", 1), ("host", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipForwarding.setStatus('mandatory')
ipDefaultTTL = MibScalar((1, 3, 6, 1, 2, 1, 4, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipDefaultTTL.setStatus('mandatory')
ipInReceives = MibScalar((1, 3, 6, 1, 2, 1, 4, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipInReceives.setStatus('mandatory')
ipInHdrErrors = MibScalar((1, 3, 6, 1, 2, 1, 4, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipInHdrErrors.setStatus('mandatory')
ipInAddrErrors = MibScalar((1, 3, 6, 1, 2, 1, 4, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipInAddrErrors.setStatus('mandatory')
ipForwDatagrams = MibScalar((1, 3, 6, 1, 2, 1, 4, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipForwDatagrams.setStatus('mandatory')
ipInUnknownProtos = MibScalar((1, 3, 6, 1, 2, 1, 4, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipInUnknownProtos.setStatus('mandatory')
ipInDiscards = MibScalar((1, 3, 6, 1, 2, 1, 4, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipInDiscards.setStatus('mandatory')
ipInDelivers = MibScalar((1, 3, 6, 1, 2, 1, 4, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipInDelivers.setStatus('mandatory')
ipOutRequests = MibScalar((1, 3, 6, 1, 2, 1, 4, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipOutRequests.setStatus('mandatory')
ipOutDiscards = MibScalar((1, 3, 6, 1, 2, 1, 4, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipOutDiscards.setStatus('mandatory')
ipOutNoRoutes = MibScalar((1, 3, 6, 1, 2, 1, 4, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipOutNoRoutes.setStatus('mandatory')
ipReasmTimeout = MibScalar((1, 3, 6, 1, 2, 1, 4, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipReasmTimeout.setStatus('mandatory')
ipReasmReqds = MibScalar((1, 3, 6, 1, 2, 1, 4, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipReasmReqds.setStatus('mandatory')
ipReasmOKs = MibScalar((1, 3, 6, 1, 2, 1, 4, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipReasmOKs.setStatus('mandatory')
ipReasmFails = MibScalar((1, 3, 6, 1, 2, 1, 4, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipReasmFails.setStatus('mandatory')
ipFragOKs = MibScalar((1, 3, 6, 1, 2, 1, 4, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFragOKs.setStatus('mandatory')
ipFragFails = MibScalar((1, 3, 6, 1, 2, 1, 4, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFragFails.setStatus('mandatory')
ipFragCreates = MibScalar((1, 3, 6, 1, 2, 1, 4, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipFragCreates.setStatus('mandatory')
ipAddrTable = MibTable((1, 3, 6, 1, 2, 1, 4, 20), ).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipAddrTable.setStatus('mandatory')
ipAddrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 4, 20, 1), ).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipAddrEntry.setStatus('mandatory')
ipAdEntAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 20, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipAdEntAddr.setStatus('mandatory')
ipAdEntIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 20, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipAdEntIfIndex.setStatus('mandatory')
ipAdEntNetMask = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 20, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipAdEntNetMask.setStatus('mandatory')
ipAdEntBcastAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 20, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipAdEntBcastAddr.setStatus('mandatory')
ipRoutingTable = MibTable((1, 3, 6, 1, 2, 1, 4, 21), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipRoutingTable.setStatus('mandatory')
ipRouteEntry = MibTableRow((1, 3, 6, 1, 2, 1, 4, 21, 1), ).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipRouteEntry.setStatus('mandatory')
ipRouteDest = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 21, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipRouteDest.setStatus('mandatory')
ipRouteIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 21, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipRouteIfIndex.setStatus('mandatory')
ipRouteMetric1 = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 21, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipRouteMetric1.setStatus('mandatory')
ipRouteMetric2 = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 21, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipRouteMetric2.setStatus('mandatory')
ipRouteMetric3 = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 21, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipRouteMetric3.setStatus('mandatory')
ipRouteMetric4 = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 21, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipRouteMetric4.setStatus('mandatory')
ipRouteNextHop = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 21, 1, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipRouteNextHop.setStatus('mandatory')
ipRouteType = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 21, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2), ("direct", 3), ("remote", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipRouteType.setStatus('mandatory')
ipRouteProto = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 21, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))).clone(namedValues=NamedValues(("other", 1), ("local", 2), ("netmgmt", 3), ("icmp", 4), ("egp", 5), ("ggp", 6), ("hello", 7), ("rip", 8), ("is-is", 9), ("es-is", 10), ("ciscoIgrp", 11), ("bbnSpfIgp", 12), ("oigp", 13)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipRouteProto.setStatus('mandatory')
ipRouteAge = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 21, 1, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipRouteAge.setStatus('mandatory')
icmpInMsgs = MibScalar((1, 3, 6, 1, 2, 1, 5, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icmpInMsgs.setStatus('mandatory')
icmpInErrors = MibScalar((1, 3, 6, 1, 2, 1, 5, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icmpInErrors.setStatus('mandatory')
icmpInDestUnreachs = MibScalar((1, 3, 6, 1, 2, 1, 5, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icmpInDestUnreachs.setStatus('mandatory')
icmpInTimeExcds = MibScalar((1, 3, 6, 1, 2, 1, 5, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icmpInTimeExcds.setStatus('mandatory')
icmpInParmProbs = MibScalar((1, 3, 6, 1, 2, 1, 5, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icmpInParmProbs.setStatus('mandatory')
icmpInSrcQuenchs = MibScalar((1, 3, 6, 1, 2, 1, 5, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icmpInSrcQuenchs.setStatus('mandatory')
icmpInRedirects = MibScalar((1, 3, 6, 1, 2, 1, 5, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icmpInRedirects.setStatus('mandatory')
icmpInEchos = MibScalar((1, 3, 6, 1, 2, 1, 5, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icmpInEchos.setStatus('mandatory')
icmpInEchoReps = MibScalar((1, 3, 6, 1, 2, 1, 5, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icmpInEchoReps.setStatus('mandatory')
icmpInTimestamps = MibScalar((1, 3, 6, 1, 2, 1, 5, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icmpInTimestamps.setStatus('mandatory')
icmpInTimestampReps = MibScalar((1, 3, 6, 1, 2, 1, 5, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icmpInTimestampReps.setStatus('mandatory')
icmpInAddrMasks = MibScalar((1, 3, 6, 1, 2, 1, 5, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icmpInAddrMasks.setStatus('mandatory')
icmpInAddrMaskReps = MibScalar((1, 3, 6, 1, 2, 1, 5, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icmpInAddrMaskReps.setStatus('mandatory')
icmpOutMsgs = MibScalar((1, 3, 6, 1, 2, 1, 5, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icmpOutMsgs.setStatus('mandatory')
icmpOutErrors = MibScalar((1, 3, 6, 1, 2, 1, 5, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icmpOutErrors.setStatus('mandatory')
icmpOutDestUnreachs = MibScalar((1, 3, 6, 1, 2, 1, 5, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icmpOutDestUnreachs.setStatus('mandatory')
icmpOutTimeExcds = MibScalar((1, 3, 6, 1, 2, 1, 5, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icmpOutTimeExcds.setStatus('mandatory')
icmpOutParmProbs = MibScalar((1, 3, 6, 1, 2, 1, 5, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icmpOutParmProbs.setStatus('mandatory')
icmpOutSrcQuenchs = MibScalar((1, 3, 6, 1, 2, 1, 5, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icmpOutSrcQuenchs.setStatus('mandatory')
icmpOutRedirects = MibScalar((1, 3, 6, 1, 2, 1, 5, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icmpOutRedirects.setStatus('mandatory')
icmpOutEchos = MibScalar((1, 3, 6, 1, 2, 1, 5, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icmpOutEchos.setStatus('mandatory')
icmpOutEchoReps = MibScalar((1, 3, 6, 1, 2, 1, 5, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icmpOutEchoReps.setStatus('mandatory')
icmpOutTimestamps = MibScalar((1, 3, 6, 1, 2, 1, 5, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icmpOutTimestamps.setStatus('mandatory')
icmpOutTimestampReps = MibScalar((1, 3, 6, 1, 2, 1, 5, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icmpOutTimestampReps.setStatus('mandatory')
icmpOutAddrMasks = MibScalar((1, 3, 6, 1, 2, 1, 5, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icmpOutAddrMasks.setStatus('mandatory')
icmpOutAddrMaskReps = MibScalar((1, 3, 6, 1, 2, 1, 5, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icmpOutAddrMaskReps.setStatus('mandatory')
tcpRtoAlgorithm = MibScalar((1, 3, 6, 1, 2, 1, 6, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("constant", 2), ("rsre", 3), ("vanj", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpRtoAlgorithm.setStatus('mandatory')
tcpRtoMin = MibScalar((1, 3, 6, 1, 2, 1, 6, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpRtoMin.setStatus('mandatory')
tcpRtoMax = MibScalar((1, 3, 6, 1, 2, 1, 6, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpRtoMax.setStatus('mandatory')
tcpMaxConn = MibScalar((1, 3, 6, 1, 2, 1, 6, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpMaxConn.setStatus('mandatory')
tcpActiveOpens = MibScalar((1, 3, 6, 1, 2, 1, 6, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpActiveOpens.setStatus('mandatory')
tcpPassiveOpens = MibScalar((1, 3, 6, 1, 2, 1, 6, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpPassiveOpens.setStatus('mandatory')
tcpAttemptFails = MibScalar((1, 3, 6, 1, 2, 1, 6, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpAttemptFails.setStatus('mandatory')
tcpEstabResets = MibScalar((1, 3, 6, 1, 2, 1, 6, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpEstabResets.setStatus('mandatory')
tcpCurrEstab = MibScalar((1, 3, 6, 1, 2, 1, 6, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpCurrEstab.setStatus('mandatory')
tcpInSegs = MibScalar((1, 3, 6, 1, 2, 1, 6, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpInSegs.setStatus('mandatory')
tcpOutSegs = MibScalar((1, 3, 6, 1, 2, 1, 6, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpOutSegs.setStatus('mandatory')
tcpRetransSegs = MibScalar((1, 3, 6, 1, 2, 1, 6, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpRetransSegs.setStatus('mandatory')
tcpConnTable = MibTable((1, 3, 6, 1, 2, 1, 6, 13), ).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpConnTable.setStatus('mandatory')
tcpConnEntry = MibTableRow((1, 3, 6, 1, 2, 1, 6, 13, 1), ).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpConnEntry.setStatus('mandatory')
tcpConnState = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 13, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("closed", 1), ("listen", 2), ("synSent", 3), ("synReceived", 4), ("established", 5), ("finWait1", 6), ("finWait2", 7), ("closeWait", 8), ("lastAck", 9), ("closing", 10), ("timeWait", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpConnState.setStatus('mandatory')
tcpConnLocalAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 13, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpConnLocalAddress.setStatus('mandatory')
tcpConnLocalPort = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 13, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpConnLocalPort.setStatus('mandatory')
tcpConnRemAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 13, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpConnRemAddress.setStatus('mandatory')
tcpConnRemPort = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 13, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpConnRemPort.setStatus('mandatory')
udpInDatagrams = MibScalar((1, 3, 6, 1, 2, 1, 7, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpInDatagrams.setStatus('mandatory')
udpNoPorts = MibScalar((1, 3, 6, 1, 2, 1, 7, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpNoPorts.setStatus('mandatory')
udpInErrors = MibScalar((1, 3, 6, 1, 2, 1, 7, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpInErrors.setStatus('mandatory')
udpOutDatagrams = MibScalar((1, 3, 6, 1, 2, 1, 7, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: udpOutDatagrams.setStatus('mandatory')
egpInMsgs = MibScalar((1, 3, 6, 1, 2, 1, 8, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: egpInMsgs.setStatus('mandatory')
egpInErrors = MibScalar((1, 3, 6, 1, 2, 1, 8, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: egpInErrors.setStatus('mandatory')
egpOutMsgs = MibScalar((1, 3, 6, 1, 2, 1, 8, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: egpOutMsgs.setStatus('mandatory')
egpOutErrors = MibScalar((1, 3, 6, 1, 2, 1, 8, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: egpOutErrors.setStatus('mandatory')
egpNeighTable = MibTable((1, 3, 6, 1, 2, 1, 8, 5), ).setMaxAccess("readonly")
if mibBuilder.loadTexts: egpNeighTable.setStatus('mandatory')
egpNeighEntry = MibTableRow((1, 3, 6, 1, 2, 1, 8, 5, 1), ).setMaxAccess("readonly")
if mibBuilder.loadTexts: egpNeighEntry.setStatus('mandatory')
egpNeighState = MibTableColumn((1, 3, 6, 1, 2, 1, 8, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("idle", 1), ("acquisition", 2), ("down", 3), ("up", 4), ("cease", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: egpNeighState.setStatus('mandatory')
egpNeighAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 8, 5, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: egpNeighAddr.setStatus('mandatory')
mibBuilder.exportSymbols("RFC1156-MIB", ipRouteIfIndex=ipRouteIfIndex, ipInAddrErrors=ipInAddrErrors, tcpCurrEstab=tcpCurrEstab, ifIndex=ifIndex, ifInDiscards=ifInDiscards, egpNeighEntry=egpNeighEntry, tcpRtoAlgorithm=tcpRtoAlgorithm, tcpOutSegs=tcpOutSegs, icmpInDestUnreachs=icmpInDestUnreachs, tcpMaxConn=tcpMaxConn, tcpAttemptFails=tcpAttemptFails, tcpConnEntry=tcpConnEntry, ipReasmReqds=ipReasmReqds, egpOutMsgs=egpOutMsgs, ipAdEntAddr=ipAdEntAddr, ipRouteAge=ipRouteAge, ipReasmOKs=ipReasmOKs, ifNumber=ifNumber, ipRouteMetric2=ipRouteMetric2, ipRouteProto=ipRouteProto, egpNeighAddr=egpNeighAddr, ipRouteMetric3=ipRouteMetric3, egpOutErrors=egpOutErrors, tcpConnLocalAddress=tcpConnLocalAddress, tcp=tcp, egpInMsgs=egpInMsgs, icmpOutRedirects=icmpOutRedirects, icmpOutTimestamps=icmpOutTimestamps, ipAdEntNetMask=ipAdEntNetMask, ipRouteType=ipRouteType, tcpConnState=tcpConnState, icmpInTimestamps=icmpInTimestamps, icmpInSrcQuenchs=icmpInSrcQuenchs, icmpOutAddrMaskReps=icmpOutAddrMaskReps, atEntry=atEntry, ipForwDatagrams=ipForwDatagrams, ipOutDiscards=ipOutDiscards, ifInErrors=ifInErrors, ipForwarding=ipForwarding, ifInOctets=ifInOctets, egpInErrors=egpInErrors, tcpRtoMax=tcpRtoMax, tcpPassiveOpens=tcpPassiveOpens, icmpOutSrcQuenchs=icmpOutSrcQuenchs, ifLastChange=ifLastChange, mib=mib, ipOutRequests=ipOutRequests, icmpOutErrors=icmpOutErrors, ipDefaultTTL=ipDefaultTTL, ifOutQLen=ifOutQLen, sysDescr=sysDescr, ifMtu=ifMtu, tcpRetransSegs=tcpRetransSegs, ifDescr=ifDescr, ip=ip, ifPhysAddress=ifPhysAddress, ifOutUcastPkts=ifOutUcastPkts, sysObjectID=sysObjectID, tcpInSegs=tcpInSegs, egpNeighTable=egpNeighTable, atNetAddress=atNetAddress, ifOperStatus=ifOperStatus, ipAdEntBcastAddr=ipAdEntBcastAddr, atPhysAddress=atPhysAddress, icmpOutParmProbs=icmpOutParmProbs, ifAdminStatus=ifAdminStatus, ipAddrTable=ipAddrTable, icmpInEchoReps=icmpInEchoReps, ifOutDiscards=ifOutDiscards, ipAddrEntry=ipAddrEntry, ifInUcastPkts=ifInUcastPkts, icmpInParmProbs=icmpInParmProbs, tcpEstabResets=tcpEstabResets, atIfIndex=atIfIndex, udpOutDatagrams=udpOutDatagrams, ipInUnknownProtos=ipInUnknownProtos, tcpConnRemAddress=tcpConnRemAddress, tcpConnRemPort=tcpConnRemPort, ifTable=ifTable, ipRouteNextHop=ipRouteNextHop, sysUpTime=sysUpTime, at=at, ipFragCreates=ipFragCreates, icmpOutDestUnreachs=icmpOutDestUnreachs, tcpConnLocalPort=tcpConnLocalPort, icmpOutEchos=icmpOutEchos, tcpActiveOpens=tcpActiveOpens, udpInDatagrams=udpInDatagrams, ipRouteEntry=ipRouteEntry, icmpOutMsgs=icmpOutMsgs, interfaces=interfaces, ipReasmFails=ipReasmFails, ipFragFails=ipFragFails, udp=udp, icmpInTimestampReps=icmpInTimestampReps, ifEntry=ifEntry, icmpInMsgs=icmpInMsgs, icmpInErrors=icmpInErrors, ipRouteMetric1=ipRouteMetric1, atTable=atTable, udpInErrors=udpInErrors, icmpInTimeExcds=icmpInTimeExcds, ifType=ifType, icmpInRedirects=icmpInRedirects, icmpOutTimestampReps=icmpOutTimestampReps, icmp=icmp, ipRoutingTable=ipRoutingTable, ifInUnknownProtos=ifInUnknownProtos, ifOutNUcastPkts=ifOutNUcastPkts, icmpInAddrMaskReps=icmpInAddrMaskReps, icmpOutAddrMasks=icmpOutAddrMasks, ifSpeed=ifSpeed, ifOutErrors=ifOutErrors, ipFragOKs=ipFragOKs, ipInHdrErrors=ipInHdrErrors, ipRouteMetric4=ipRouteMetric4, tcpRtoMin=tcpRtoMin, ipReasmTimeout=ipReasmTimeout, ipInReceives=ipInReceives, ipInDelivers=ipInDelivers, system=system, udpNoPorts=udpNoPorts, ipAdEntIfIndex=ipAdEntIfIndex, ipOutNoRoutes=ipOutNoRoutes, ifInNUcastPkts=ifInNUcastPkts, ipRouteDest=ipRouteDest, ifOutOctets=ifOutOctets, icmpOutTimeExcds=icmpOutTimeExcds, icmpOutEchoReps=icmpOutEchoReps, tcpConnTable=tcpConnTable, egpNeighState=egpNeighState, egp=egp, ipInDiscards=ipInDiscards, icmpInEchos=icmpInEchos, icmpInAddrMasks=icmpInAddrMasks)
