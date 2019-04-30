#
# PySNMP MIB module QLGC-adapterInfo-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/QLGC-adapterInfo-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:35:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
InetAddressIPv6, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressIPv6")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, iso, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32, MibIdentifier, enterprises, Counter64, ModuleIdentity, Gauge32, TimeTicks, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32", "MibIdentifier", "enterprises", "Counter64", "ModuleIdentity", "Gauge32", "TimeTicks", "Bits", "Integer32")
TextualConvention, DisplayString, PhysAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "PhysAddress")
qlogic = MibIdentifier((1, 3, 6, 1, 4, 1, 3873))
enet = MibIdentifier((1, 3, 6, 1, 4, 1, 3873, 1))
qlasp = MibIdentifier((1, 3, 6, 1, 4, 1, 3873, 1, 2))
ifControllers = MibIdentifier((1, 3, 6, 1, 4, 1, 3873, 1, 3))
qlaspConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 3873, 1, 2, 1))
qlaspStat = MibIdentifier((1, 3, 6, 1, 4, 1, 3873, 1, 2, 2))
qlaspTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 3873, 1, 2, 3))
ifiNumber = MibScalar((1, 3, 6, 1, 4, 1, 3873, 1, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifiNumber.setStatus('mandatory')
ifiTable = MibTable((1, 3, 6, 1, 4, 1, 3873, 1, 3, 2), )
if mibBuilder.loadTexts: ifiTable.setStatus('mandatory')
ifiEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1), ).setIndexNames((0, "QLGC-adapterInfo-MIB", "ifiIndex"))
if mibBuilder.loadTexts: ifiEntry.setStatus('mandatory')
ifiIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: ifiIndex.setStatus('mandatory')
ifName = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifName.setStatus('mandatory')
ifiDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifiDescr.setStatus('mandatory')
ifNetworkAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifNetworkAddress.setStatus('mandatory')
ifSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifSubnetMask.setStatus('mandatory')
ifiPhysAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 6), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifiPhysAddress.setStatus('mandatory')
ifPermPhysAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 7), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifPermPhysAddress.setStatus('mandatory')
ifLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("link-up", 1), ("link-fail", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifLinkStatus.setStatus('mandatory')
ifState = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("normal-mode", 1), ("diagnotic-mode", 2), ("adapter-removed", 3), ("lowpower-mode", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifState.setStatus('mandatory')
ifLineSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unknown", 1), ("speed-10-Mbps", 2), ("speed-100-Mbps", 3), ("speed-1000-Mbps", 4), ("speed-2500-Mbps", 5), ("speed-10-Gbps", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifLineSpeed.setStatus('mandatory')
ifDuplexMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("half-duplex", 2), ("full-duplex", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifDuplexMode.setStatus('mandatory')
ifMemBaseLow = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifMemBaseLow.setStatus('mandatory')
ifMemBaseHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifMemBaseHigh.setStatus('mandatory')
ifInterrupt = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifInterrupt.setStatus('mandatory')
ifBusNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifBusNumber.setStatus('mandatory')
ifDeviceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifDeviceNumber.setStatus('mandatory')
ifFunctionNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifFunctionNumber.setStatus('mandatory')
ifIpv6NetworkAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3873, 1, 3, 2, 1, 18), InetAddressIPv6()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifIpv6NetworkAddress.setStatus('mandatory')
mibBuilder.exportSymbols("QLGC-adapterInfo-MIB", ifInterrupt=ifInterrupt, ifIpv6NetworkAddress=ifIpv6NetworkAddress, qlaspStat=qlaspStat, ifiIndex=ifiIndex, ifMemBaseHigh=ifMemBaseHigh, ifiDescr=ifiDescr, ifiNumber=ifiNumber, ifLineSpeed=ifLineSpeed, ifiTable=ifiTable, ifiEntry=ifiEntry, ifState=ifState, ifiPhysAddress=ifiPhysAddress, ifFunctionNumber=ifFunctionNumber, ifName=ifName, ifControllers=ifControllers, qlasp=qlasp, ifNetworkAddress=ifNetworkAddress, qlogic=qlogic, ifDuplexMode=ifDuplexMode, ifBusNumber=ifBusNumber, ifLinkStatus=ifLinkStatus, enet=enet, ifMemBaseLow=ifMemBaseLow, ifPermPhysAddress=ifPermPhysAddress, qlaspTrap=qlaspTrap, ifSubnetMask=ifSubnetMask, ifDeviceNumber=ifDeviceNumber, qlaspConfig=qlaspConfig)
