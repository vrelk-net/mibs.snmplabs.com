#
# PySNMP MIB module RUCKUS-WLINK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RUCKUS-WLINK-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:50:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ruckusCommonWLINKModule, = mibBuilder.importSymbols("RUCKUS-ROOT-MIB", "ruckusCommonWLINKModule")
RuckusSSID, = mibBuilder.importSymbols("RUCKUS-TC-MIB", "RuckusSSID")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, ModuleIdentity, Counter32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, Counter64, Gauge32, IpAddress, TimeTicks, ObjectIdentity, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ModuleIdentity", "Counter32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "Counter64", "Gauge32", "IpAddress", "TimeTicks", "ObjectIdentity", "Unsigned32", "iso")
DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention")
ruckusWLINKMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1))
if mibBuilder.loadTexts: ruckusWLINKMIB.setLastUpdated('201010150800Z')
if mibBuilder.loadTexts: ruckusWLINKMIB.setOrganization('Ruckus Wireless, Inc.')
ruckusWLINKObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1))
ruckusWLINKInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1))
ruckusWLINKEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 2))
ruckusWLINKTable = MibTable((1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1), )
if mibBuilder.loadTexts: ruckusWLINKTable.setStatus('current')
ruckusWLINKEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ruckusWLINKEntry.setStatus('current')
ruckusWLINKSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 1), RuckusSSID()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusWLINKSSID.setStatus('current')
ruckusWLINKRole = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("rootBridge", 1), ("nonRootBridge", 2), ("notDecided", 3), ("notAvailable", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusWLINKRole.setStatus('current')
ruckusWLINKLocalMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusWLINKLocalMAC.setStatus('current')
ruckusWLINKRemoteMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusWLINKRemoteMAC.setStatus('current')
ruckusWLINKTxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusWLINKTxPkts.setStatus('current')
ruckusWLINKTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusWLINKTxBytes.setStatus('current')
ruckusWLINKRxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusWLINKRxPkts.setStatus('current')
ruckusWLINKRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusWLINKRxBytes.setStatus('current')
ruckusWLINKEstablishTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusWLINKEstablishTime.setStatus('current')
ruckusWLINKUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusWLINKUpTime.setStatus('current')
ruckusWLINKRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusWLINKRssi.setStatus('current')
ruckusWLINKUpCount = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusWLINKUpCount.setStatus('current')
ruckusWLINKDownCount = MibTableColumn((1, 3, 6, 1, 4, 1, 25053, 1, 1, 15, 1, 1, 1, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusWLINKDownCount.setStatus('current')
mibBuilder.exportSymbols("RUCKUS-WLINK-MIB", ruckusWLINKEstablishTime=ruckusWLINKEstablishTime, ruckusWLINKRssi=ruckusWLINKRssi, ruckusWLINKMIB=ruckusWLINKMIB, ruckusWLINKRole=ruckusWLINKRole, ruckusWLINKObjects=ruckusWLINKObjects, ruckusWLINKLocalMAC=ruckusWLINKLocalMAC, ruckusWLINKTable=ruckusWLINKTable, ruckusWLINKEvents=ruckusWLINKEvents, ruckusWLINKRemoteMAC=ruckusWLINKRemoteMAC, ruckusWLINKDownCount=ruckusWLINKDownCount, ruckusWLINKRxPkts=ruckusWLINKRxPkts, ruckusWLINKSSID=ruckusWLINKSSID, ruckusWLINKEntry=ruckusWLINKEntry, ruckusWLINKTxPkts=ruckusWLINKTxPkts, ruckusWLINKRxBytes=ruckusWLINKRxBytes, ruckusWLINKUpTime=ruckusWLINKUpTime, ruckusWLINKUpCount=ruckusWLINKUpCount, ruckusWLINKInfo=ruckusWLINKInfo, PYSNMP_MODULE_ID=ruckusWLINKMIB, ruckusWLINKTxBytes=ruckusWLINKTxBytes)
