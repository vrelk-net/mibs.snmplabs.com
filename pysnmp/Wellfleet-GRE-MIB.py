#
# PySNMP MIB module Wellfleet-GRE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-GRE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:33:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Counter32, IpAddress, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Bits, MibIdentifier, iso, ModuleIdentity, NotificationType, ObjectIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "IpAddress", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Bits", "MibIdentifier", "iso", "ModuleIdentity", "NotificationType", "ObjectIdentity", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wfGreGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfGreGroup")
wfGreInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 1), )
if mibBuilder.loadTexts: wfGreInterfaceTable.setStatus('mandatory')
wfGreInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 1, 1), ).setIndexNames((0, "Wellfleet-GRE-MIB", "wfGreIntfIpAddr"), (0, "Wellfleet-GRE-MIB", "wfGreIntfCct"))
if mibBuilder.loadTexts: wfGreInterfaceEntry.setStatus('mandatory')
wfGreIntfCreate = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("create", 1), ("delete", 2))).clone('create')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfGreIntfCreate.setStatus('mandatory')
wfGreIntfEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfGreIntfEnable.setStatus('mandatory')
wfGreIntfState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("init", 3), ("notpres", 4))).clone('notpres')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfGreIntfState.setStatus('mandatory')
wfGreIntfIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfGreIntfIpAddr.setStatus('mandatory')
wfGreIntfCct = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfGreIntfCct.setStatus('mandatory')
wfGreIntfStatsEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfGreIntfStatsEnable.setStatus('mandatory')
wfGreIntfDebugLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 1, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfGreIntfDebugLevel.setStatus('mandatory')
wfGreTunnelTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2), )
if mibBuilder.loadTexts: wfGreTunnelTable.setStatus('mandatory')
wfGreTunnelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1), ).setIndexNames((0, "Wellfleet-GRE-MIB", "wfGreTunnelLocalAddr"), (0, "Wellfleet-GRE-MIB", "wfGreTunnelPeerAddress"), (0, "Wellfleet-GRE-MIB", "wfGreTunnelLocalIndex"))
if mibBuilder.loadTexts: wfGreTunnelEntry.setStatus('mandatory')
wfGreTunnelLocalAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfGreTunnelLocalAddr.setStatus('mandatory')
wfGreTunnelLocalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfGreTunnelLocalIndex.setStatus('mandatory')
wfGreTunnelType = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("generic", 1), ("udas", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfGreTunnelType.setStatus('mandatory')
wfGreTunnelId = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfGreTunnelId.setStatus('mandatory')
wfGreTunnelPeerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfGreTunnelPeerAddress.setStatus('mandatory')
wfGreRemotePayloadAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(10, 10)).setFixedLength(10)).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfGreRemotePayloadAddress.setStatus('deprecated')
wfGreTunnelState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfGreTunnelState.setStatus('mandatory')
wfGreVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfGreVersion.setStatus('mandatory')
wfGreProtoMap = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfGreProtoMap.setStatus('mandatory')
wfGreTunnelPktsTx = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfGreTunnelPktsTx.setStatus('mandatory')
wfGreTunnelPktsRx = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfGreTunnelPktsRx.setStatus('mandatory')
wfGreTunnelBytesTx = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfGreTunnelBytesTx.setStatus('mandatory')
wfGreTunnelBytesRx = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfGreTunnelBytesRx.setStatus('mandatory')
wfGreTunnelPktsTxDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfGreTunnelPktsTxDropped.setStatus('mandatory')
wfGreTunnelPktsRxDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfGreTunnelPktsRxDropped.setStatus('mandatory')
wfGreTunnelXsumErr = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfGreTunnelXsumErr.setStatus('mandatory')
wfGreTunnelSeqNumErr = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfGreTunnelSeqNumErr.setStatus('mandatory')
wfGreTunnelMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 20, 2, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4500))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfGreTunnelMtu.setStatus('mandatory')
mibBuilder.exportSymbols("Wellfleet-GRE-MIB", wfGreIntfEnable=wfGreIntfEnable, wfGreTunnelMtu=wfGreTunnelMtu, wfGreTunnelBytesTx=wfGreTunnelBytesTx, wfGreIntfCreate=wfGreIntfCreate, wfGreRemotePayloadAddress=wfGreRemotePayloadAddress, wfGreIntfDebugLevel=wfGreIntfDebugLevel, wfGreIntfStatsEnable=wfGreIntfStatsEnable, wfGreTunnelLocalAddr=wfGreTunnelLocalAddr, wfGreVersion=wfGreVersion, wfGreTunnelPeerAddress=wfGreTunnelPeerAddress, wfGreTunnelXsumErr=wfGreTunnelXsumErr, wfGreTunnelBytesRx=wfGreTunnelBytesRx, wfGreTunnelPktsRx=wfGreTunnelPktsRx, wfGreTunnelEntry=wfGreTunnelEntry, wfGreTunnelPktsRxDropped=wfGreTunnelPktsRxDropped, wfGreTunnelType=wfGreTunnelType, wfGreIntfCct=wfGreIntfCct, wfGreTunnelTable=wfGreTunnelTable, wfGreTunnelPktsTxDropped=wfGreTunnelPktsTxDropped, wfGreProtoMap=wfGreProtoMap, wfGreTunnelSeqNumErr=wfGreTunnelSeqNumErr, wfGreTunnelId=wfGreTunnelId, wfGreIntfState=wfGreIntfState, wfGreTunnelState=wfGreTunnelState, wfGreTunnelPktsTx=wfGreTunnelPktsTx, wfGreInterfaceTable=wfGreInterfaceTable, wfGreIntfIpAddr=wfGreIntfIpAddr, wfGreTunnelLocalIndex=wfGreTunnelLocalIndex, wfGreInterfaceEntry=wfGreInterfaceEntry)
