#
# PySNMP MIB module HP-SN-ROUTER-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-SN-MIBS
# Produced by pysmi-0.3.4 at Mon Apr 29 19:23:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
snOspfVirtIfStatusAreaID, snOspfNbrIpAddr, snOspfNbrState, snOspfPacketType, snOspfIfStatusState, snOspfLsdbLsId, snOspfVirtIfStatusNeighbor, snOspfVirtNbrArea, snOspfLsdbType, snOspfVirtNbrState, snOspfIfStatusIpAddress, snOspfConfigErrorType, snOspfVirtNbrRtrId, snOspfNbrRtrId, snOspfVirtIfStatusState, snOspfExtLsdbLimit, snOspfPacketSrc, snOspfLsdbRouterId, snOspfRouterId, snOspfLsdbAreaId = mibBuilder.importSymbols("HP-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusAreaID", "snOspfNbrIpAddr", "snOspfNbrState", "snOspfPacketType", "snOspfIfStatusState", "snOspfLsdbLsId", "snOspfVirtIfStatusNeighbor", "snOspfVirtNbrArea", "snOspfLsdbType", "snOspfVirtNbrState", "snOspfIfStatusIpAddress", "snOspfConfigErrorType", "snOspfVirtNbrRtrId", "snOspfNbrRtrId", "snOspfVirtIfStatusState", "snOspfExtLsdbLimit", "snOspfPacketSrc", "snOspfLsdbRouterId", "snOspfRouterId", "snOspfLsdbAreaId")
hp, = mibBuilder.importSymbols("HP-SN-ROOT-MIB", "hp")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, IpAddress, Integer32, Counter32, Counter64, iso, Bits, NotificationType, TimeTicks, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ObjectIdentity, MibIdentifier, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "IpAddress", "Integer32", "Counter32", "Counter64", "iso", "Bits", "NotificationType", "TimeTicks", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ObjectIdentity", "MibIdentifier", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
snTrapOspfIfStateChange = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,3)).setObjects(("HP-SN-OSPF-GROUP-MIB", "snOspfRouterId"), ("HP-SN-OSPF-GROUP-MIB", "snOspfIfStatusIpAddress"), ("HP-SN-OSPF-GROUP-MIB", "snOspfIfStatusState"))
snTrapOspfVirtIfStateChange = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,4)).setObjects(("HP-SN-OSPF-GROUP-MIB", "snOspfRouterId"), ("HP-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusAreaID"), ("HP-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusNeighbor"), ("HP-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusState"))
snOspfNbrStateChange = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,5)).setObjects(("HP-SN-OSPF-GROUP-MIB", "snOspfRouterId"), ("HP-SN-OSPF-GROUP-MIB", "snOspfNbrIpAddr"), ("HP-SN-OSPF-GROUP-MIB", "snOspfNbrRtrId"), ("HP-SN-OSPF-GROUP-MIB", "snOspfNbrState"))
snOspfVirtNbrStateChange = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,6)).setObjects(("HP-SN-OSPF-GROUP-MIB", "snOspfRouterId"), ("HP-SN-OSPF-GROUP-MIB", "snOspfVirtNbrArea"), ("HP-SN-OSPF-GROUP-MIB", "snOspfVirtNbrRtrId"), ("HP-SN-OSPF-GROUP-MIB", "snOspfVirtNbrState"))
snOspfIfConfigError = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,7)).setObjects(("HP-SN-OSPF-GROUP-MIB", "snOspfRouterId"), ("HP-SN-OSPF-GROUP-MIB", "snOspfIfStatusIpAddress"), ("HP-SN-OSPF-GROUP-MIB", "snOspfPacketSrc"), ("HP-SN-OSPF-GROUP-MIB", "snOspfConfigErrorType"), ("HP-SN-OSPF-GROUP-MIB", "snOspfPacketType"))
snOspfVirtIfConfigError = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,8)).setObjects(("HP-SN-OSPF-GROUP-MIB", "snOspfRouterId"), ("HP-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusAreaID"), ("HP-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusNeighbor"), ("HP-SN-OSPF-GROUP-MIB", "snOspfConfigErrorType"), ("HP-SN-OSPF-GROUP-MIB", "snOspfPacketType"))
snOspfIfAuthFailure = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,9)).setObjects(("HP-SN-OSPF-GROUP-MIB", "snOspfRouterId"), ("HP-SN-OSPF-GROUP-MIB", "snOspfIfStatusIpAddress"), ("HP-SN-OSPF-GROUP-MIB", "snOspfPacketSrc"), ("HP-SN-OSPF-GROUP-MIB", "snOspfConfigErrorType"), ("HP-SN-OSPF-GROUP-MIB", "snOspfPacketType"))
snOspfVirtIfAuthFailure = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,10)).setObjects(("HP-SN-OSPF-GROUP-MIB", "snOspfRouterId"), ("HP-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusAreaID"), ("HP-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusNeighbor"), ("HP-SN-OSPF-GROUP-MIB", "snOspfConfigErrorType"), ("HP-SN-OSPF-GROUP-MIB", "snOspfPacketType"))
snOspfIfRxBadPacket = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,11)).setObjects(("HP-SN-OSPF-GROUP-MIB", "snOspfRouterId"), ("HP-SN-OSPF-GROUP-MIB", "snOspfIfStatusIpAddress"), ("HP-SN-OSPF-GROUP-MIB", "snOspfPacketSrc"), ("HP-SN-OSPF-GROUP-MIB", "snOspfPacketType"))
snOspfVirtIfRxBadPacket = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,12)).setObjects(("HP-SN-OSPF-GROUP-MIB", "snOspfRouterId"), ("HP-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusAreaID"), ("HP-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusNeighbor"), ("HP-SN-OSPF-GROUP-MIB", "snOspfPacketType"))
snOspfTxRetransmit = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,13)).setObjects(("HP-SN-OSPF-GROUP-MIB", "snOspfRouterId"), ("HP-SN-OSPF-GROUP-MIB", "snOspfIfStatusIpAddress"), ("HP-SN-OSPF-GROUP-MIB", "snOspfNbrRtrId"), ("HP-SN-OSPF-GROUP-MIB", "snOspfPacketType"), ("HP-SN-OSPF-GROUP-MIB", "snOspfLsdbType"), ("HP-SN-OSPF-GROUP-MIB", "snOspfLsdbLsId"), ("HP-SN-OSPF-GROUP-MIB", "snOspfLsdbRouterId"))
ospfVirtIfTxRetransmit = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,14)).setObjects(("HP-SN-OSPF-GROUP-MIB", "snOspfRouterId"), ("HP-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusAreaID"), ("HP-SN-OSPF-GROUP-MIB", "snOspfVirtIfStatusNeighbor"), ("HP-SN-OSPF-GROUP-MIB", "snOspfPacketType"), ("HP-SN-OSPF-GROUP-MIB", "snOspfLsdbType"), ("HP-SN-OSPF-GROUP-MIB", "snOspfLsdbLsId"), ("HP-SN-OSPF-GROUP-MIB", "snOspfLsdbRouterId"))
snOspfOriginateLsa = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,15)).setObjects(("HP-SN-OSPF-GROUP-MIB", "snOspfRouterId"), ("HP-SN-OSPF-GROUP-MIB", "snOspfLsdbAreaId"), ("HP-SN-OSPF-GROUP-MIB", "snOspfLsdbType"), ("HP-SN-OSPF-GROUP-MIB", "snOspfLsdbLsId"), ("HP-SN-OSPF-GROUP-MIB", "snOspfLsdbRouterId"))
snOspfMaxAgeLsa = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,16)).setObjects(("HP-SN-OSPF-GROUP-MIB", "snOspfRouterId"), ("HP-SN-OSPF-GROUP-MIB", "snOspfLsdbAreaId"), ("HP-SN-OSPF-GROUP-MIB", "snOspfLsdbType"), ("HP-SN-OSPF-GROUP-MIB", "snOspfLsdbLsId"), ("HP-SN-OSPF-GROUP-MIB", "snOspfLsdbRouterId"))
snOspfLsdbOverflow = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,17)).setObjects(("HP-SN-OSPF-GROUP-MIB", "snOspfRouterId"), ("HP-SN-OSPF-GROUP-MIB", "snOspfExtLsdbLimit"))
snOspfLsdbApproachingOverflow = NotificationType((1, 3, 6, 1, 4, 1, 11) + (0,18)).setObjects(("HP-SN-OSPF-GROUP-MIB", "snOspfRouterId"), ("HP-SN-OSPF-GROUP-MIB", "snOspfExtLsdbLimit"))
mibBuilder.exportSymbols("HP-SN-ROUTER-TRAP-MIB", snOspfVirtNbrStateChange=snOspfVirtNbrStateChange, snOspfVirtIfRxBadPacket=snOspfVirtIfRxBadPacket, snOspfNbrStateChange=snOspfNbrStateChange, snOspfIfAuthFailure=snOspfIfAuthFailure, snTrapOspfVirtIfStateChange=snTrapOspfVirtIfStateChange, snOspfVirtIfConfigError=snOspfVirtIfConfigError, snTrapOspfIfStateChange=snTrapOspfIfStateChange, snOspfIfRxBadPacket=snOspfIfRxBadPacket, snOspfTxRetransmit=snOspfTxRetransmit, ospfVirtIfTxRetransmit=ospfVirtIfTxRetransmit, snOspfVirtIfAuthFailure=snOspfVirtIfAuthFailure, snOspfMaxAgeLsa=snOspfMaxAgeLsa, snOspfIfConfigError=snOspfIfConfigError, snOspfLsdbOverflow=snOspfLsdbOverflow, snOspfLsdbApproachingOverflow=snOspfLsdbApproachingOverflow, snOspfOriginateLsa=snOspfOriginateLsa)