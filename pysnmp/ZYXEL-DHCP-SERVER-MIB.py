#
# PySNMP MIB module ZYXEL-DHCP-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-DHCP-SERVER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:43:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, IpAddress, ModuleIdentity, Counter32, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, MibIdentifier, TimeTicks, Integer32, ObjectIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "IpAddress", "ModuleIdentity", "Counter32", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "MibIdentifier", "TimeTicks", "Integer32", "ObjectIdentity", "Counter64")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelDhcpServer = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 19))
if mibBuilder.loadTexts: zyxelDhcpServer.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelDhcpServer.setOrganization('Enterprise Solution ZyXEL')
zyxelDhcpServerSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 19, 1))
zyDhcpServerMaxNumberOfServers = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 19, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyDhcpServerMaxNumberOfServers.setStatus('current')
zyxelDhcpServerTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 19, 1, 2), )
if mibBuilder.loadTexts: zyxelDhcpServerTable.setStatus('current')
zyxelDhcpServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 19, 1, 2, 1), ).setIndexNames((0, "ZYXEL-DHCP-SERVER-MIB", "zyDhcpServerVid"))
if mibBuilder.loadTexts: zyxelDhcpServerEntry.setStatus('current')
zyDhcpServerVid = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 19, 1, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: zyDhcpServerVid.setStatus('current')
zyDhcpServerStartIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 19, 1, 2, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDhcpServerStartIpAddress.setStatus('current')
zyDhcpServerPoolSize = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 19, 1, 2, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDhcpServerPoolSize.setStatus('current')
zyDhcpServerMask = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 19, 1, 2, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDhcpServerMask.setStatus('current')
zyDhcpServerGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 19, 1, 2, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDhcpServerGateway.setStatus('current')
zyDhcpServerPrimaryDNS = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 19, 1, 2, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDhcpServerPrimaryDNS.setStatus('current')
zyDhcpServerSecondaryDNS = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 19, 1, 2, 1, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyDhcpServerSecondaryDNS.setStatus('current')
zyDhcpServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 19, 1, 2, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zyDhcpServerRowStatus.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-DHCP-SERVER-MIB", zyxelDhcpServerTable=zyxelDhcpServerTable, PYSNMP_MODULE_ID=zyxelDhcpServer, zyDhcpServerVid=zyDhcpServerVid, zyDhcpServerSecondaryDNS=zyDhcpServerSecondaryDNS, zyDhcpServerMask=zyDhcpServerMask, zyDhcpServerMaxNumberOfServers=zyDhcpServerMaxNumberOfServers, zyDhcpServerPrimaryDNS=zyDhcpServerPrimaryDNS, zyDhcpServerStartIpAddress=zyDhcpServerStartIpAddress, zyxelDhcpServerEntry=zyxelDhcpServerEntry, zyxelDhcpServerSetup=zyxelDhcpServerSetup, zyDhcpServerRowStatus=zyDhcpServerRowStatus, zyDhcpServerPoolSize=zyDhcpServerPoolSize, zyDhcpServerGateway=zyDhcpServerGateway, zyxelDhcpServer=zyxelDhcpServer)