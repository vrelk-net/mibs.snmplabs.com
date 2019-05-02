#
# PySNMP MIB module ZYXEL-IPSG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-IPSG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:50:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, ModuleIdentity, IpAddress, Counter32, Counter64, Bits, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity, Unsigned32, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ModuleIdentity", "IpAddress", "Counter32", "Counter64", "Bits", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity", "Unsigned32", "Integer32", "TimeTicks")
RowStatus, MacAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "MacAddress", "DisplayString", "TextualConvention")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelIpsg = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33))
if mibBuilder.loadTexts: zyxelIpsg.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelIpsg.setOrganization('Enterprise Solution ZyXEL')
if mibBuilder.loadTexts: zyxelIpsg.setContactInfo('')
if mibBuilder.loadTexts: zyxelIpsg.setDescription('The subtree for IP Source Guard (IPSG)')
zyxelArpFreezeSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33, 1))
zyxelIpsgStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33, 2))
zyxelStaticBindingSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33, 3))
zyArpFreeze = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyArpFreeze.setStatus('current')
if mibBuilder.loadTexts: zyArpFreeze.setDescription("Add all learned ARP table entries to static binding table. It's meaningless while reading this entry.")
zyArpFreezePorts = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33, 1, 2), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyArpFreezePorts.setStatus('current')
if mibBuilder.loadTexts: zyArpFreezePorts.setDescription("Add learned ARP table entries to static binding table by ports. It's meaningless while reading this entry.")
zyArpFreezeVlan = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyArpFreezeVlan.setStatus('current')
if mibBuilder.loadTexts: zyArpFreezeVlan.setDescription("Add learned ARP table entries to static binding table by VLAN. It's meaningless while reading this entry.")
zyxelIpsgInfoTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33, 2, 1), )
if mibBuilder.loadTexts: zyxelIpsgInfoTable.setStatus('current')
if mibBuilder.loadTexts: zyxelIpsgInfoTable.setDescription('The table contains IGMP information.')
zyxelIpsgInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33, 2, 1, 1), ).setIndexNames((0, "ZYXEL-IPSG-MIB", "zyIpsgInfoMacAddress"), (0, "ZYXEL-IPSG-MIB", "zyIpsgInfoVid"))
if mibBuilder.loadTexts: zyxelIpsgInfoEntry.setStatus('current')
if mibBuilder.loadTexts: zyxelIpsgInfoEntry.setDescription('An entry contains IGMP information. ')
zyIpsgInfoMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33, 2, 1, 1, 1), MacAddress())
if mibBuilder.loadTexts: zyIpsgInfoMacAddress.setStatus('current')
if mibBuilder.loadTexts: zyIpsgInfoMacAddress.setDescription('The source MAC address in the binding.')
zyIpsgInfoVid = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)))
if mibBuilder.loadTexts: zyIpsgInfoVid.setStatus('current')
if mibBuilder.loadTexts: zyIpsgInfoVid.setDescription('The source VLAN ID in the binding.')
zyIpsgInfoIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33, 2, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIpsgInfoIpAddress.setStatus('current')
if mibBuilder.loadTexts: zyIpsgInfoIpAddress.setDescription('The IP address assigned to the MAC address in the binding.')
zyIpsgInfoLeaseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIpsgInfoLeaseTime.setStatus('current')
if mibBuilder.loadTexts: zyIpsgInfoLeaseTime.setDescription('This entry displays how much time (seconds) the binding is valid. This entry displays value 0 if the binding is always valid (for example, a static binding).')
zyIpsgInfoType = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("static", 1), ("dhcp", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIpsgInfoType.setStatus('current')
if mibBuilder.loadTexts: zyIpsgInfoType.setDescription('This entry displays how the switch learned the binding. static: This binding was learned from information provided manually by an administrator. dhcp: This binding was learned by snooping DHCP packets.')
zyIpsgInfoPort = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyIpsgInfoPort.setStatus('current')
if mibBuilder.loadTexts: zyIpsgInfoPort.setDescription('The port number in the binding. The value 0 means any port.')
zyStaticBindingMaxNumberOfRules = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyStaticBindingMaxNumberOfRules.setStatus('current')
if mibBuilder.loadTexts: zyStaticBindingMaxNumberOfRules.setDescription('The maximum number of static binding rules that can be created.')
zyxelStaticBindingTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33, 3, 2), )
if mibBuilder.loadTexts: zyxelStaticBindingTable.setStatus('current')
if mibBuilder.loadTexts: zyxelStaticBindingTable.setDescription('The table contains static binding configuration. ')
zyxelStaticBindingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33, 3, 2, 1), ).setIndexNames((0, "ZYXEL-IPSG-MIB", "zyStaticBindingMacAddress"), (0, "ZYXEL-IPSG-MIB", "zyStaticBindingVid"))
if mibBuilder.loadTexts: zyxelStaticBindingEntry.setStatus('current')
if mibBuilder.loadTexts: zyxelStaticBindingEntry.setDescription('An entry contains static binding configuration.')
zyStaticBindingMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33, 3, 2, 1, 1), MacAddress())
if mibBuilder.loadTexts: zyStaticBindingMacAddress.setStatus('current')
if mibBuilder.loadTexts: zyStaticBindingMacAddress.setDescription('The source MAC address in the binding.')
zyStaticBindingVid = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)))
if mibBuilder.loadTexts: zyStaticBindingVid.setStatus('current')
if mibBuilder.loadTexts: zyStaticBindingVid.setDescription('The IP address assigned to the MAC address in the binding.')
zyStaticBindingIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33, 3, 2, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyStaticBindingIpAddress.setStatus('current')
if mibBuilder.loadTexts: zyStaticBindingIpAddress.setDescription('Enter the source VLAN ID in the binding.')
zyStaticBindingPort = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33, 3, 2, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyStaticBindingPort.setStatus('current')
if mibBuilder.loadTexts: zyStaticBindingPort.setDescription('Enter the port number in the binding. The value 0 means any port.')
zyStaticBindingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33, 3, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zyStaticBindingRowStatus.setStatus('current')
if mibBuilder.loadTexts: zyStaticBindingRowStatus.setDescription('This object allows static binding entries to be created and deleted from static binding table.')
mibBuilder.exportSymbols("ZYXEL-IPSG-MIB", zyIpsgInfoLeaseTime=zyIpsgInfoLeaseTime, zyIpsgInfoPort=zyIpsgInfoPort, zyStaticBindingRowStatus=zyStaticBindingRowStatus, zyxelIpsgInfoTable=zyxelIpsgInfoTable, zyIpsgInfoVid=zyIpsgInfoVid, zyStaticBindingIpAddress=zyStaticBindingIpAddress, zyxelIpsgStatus=zyxelIpsgStatus, zyxelStaticBindingTable=zyxelStaticBindingTable, zyStaticBindingMaxNumberOfRules=zyStaticBindingMaxNumberOfRules, zyArpFreeze=zyArpFreeze, zyStaticBindingMacAddress=zyStaticBindingMacAddress, zyIpsgInfoIpAddress=zyIpsgInfoIpAddress, zyxelStaticBindingSetup=zyxelStaticBindingSetup, zyArpFreezePorts=zyArpFreezePorts, zyStaticBindingPort=zyStaticBindingPort, zyArpFreezeVlan=zyArpFreezeVlan, zyxelArpFreezeSetup=zyxelArpFreezeSetup, zyIpsgInfoMacAddress=zyIpsgInfoMacAddress, zyxelIpsgInfoEntry=zyxelIpsgInfoEntry, zyStaticBindingVid=zyStaticBindingVid, zyxelIpsg=zyxelIpsg, PYSNMP_MODULE_ID=zyxelIpsg, zyIpsgInfoType=zyIpsgInfoType, zyxelStaticBindingEntry=zyxelStaticBindingEntry)