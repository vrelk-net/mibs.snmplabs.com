#
# PySNMP MIB module CISCO-DNS-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DNS-CLIENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:38:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ModuleIdentity, Bits, Unsigned32, Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Integer32, Counter64, Gauge32, TimeTicks, ObjectIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "Unsigned32", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Integer32", "Counter64", "Gauge32", "TimeTicks", "ObjectIdentity", "MibIdentifier")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
ciscoDNSClientMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 436))
ciscoDNSClientMIB.setRevisions(('2004-09-09 00:00',))
if mibBuilder.loadTexts: ciscoDNSClientMIB.setLastUpdated('200409090000Z')
if mibBuilder.loadTexts: ciscoDNSClientMIB.setOrganization('Cisco Systems Inc. ')
ciscoDNSClientMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 436, 0))
ciscoDNSClientMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 436, 1))
ciscoDNSClientMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 436, 2))
cdcConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 436, 1, 1))
cdcDNSConfigEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 436, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdcDNSConfigEnable.setStatus('current')
cdcNoOfDNSServerConfig = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 436, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdcNoOfDNSServerConfig.setStatus('current')
cdcDNSServerNextAvailIndex = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 436, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdcDNSServerNextAvailIndex.setStatus('current')
cdcDNSServerTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 436, 1, 1, 4), )
if mibBuilder.loadTexts: cdcDNSServerTable.setStatus('current')
cdcDNSServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 436, 1, 1, 4, 1), ).setIndexNames((0, "CISCO-DNS-CLIENT-MIB", "cdcDNSServerIndex"))
if mibBuilder.loadTexts: cdcDNSServerEntry.setStatus('current')
cdcDNSServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 436, 1, 1, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: cdcDNSServerIndex.setStatus('current')
cdcDNSServerAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 436, 1, 1, 4, 1, 2), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdcDNSServerAddrType.setStatus('current')
cdcDNSServerAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 436, 1, 1, 4, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdcDNSServerAddr.setStatus('current')
cdcDNSServerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 436, 1, 1, 4, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdcDNSServerStatus.setStatus('current')
cdcDefaultDNSDomainName = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 436, 1, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdcDefaultDNSDomainName.setStatus('current')
cdcDNSDomainNameTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 436, 1, 1, 6), )
if mibBuilder.loadTexts: cdcDNSDomainNameTable.setStatus('current')
cdcDNSDomainNameEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 436, 1, 1, 6, 1), ).setIndexNames((0, "CISCO-DNS-CLIENT-MIB", "cdcDNSDomainNameIndex"))
if mibBuilder.loadTexts: cdcDNSDomainNameEntry.setStatus('current')
cdcDNSDomainNameIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 436, 1, 1, 6, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 64)))
if mibBuilder.loadTexts: cdcDNSDomainNameIndex.setStatus('current')
cdcDNSDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 436, 1, 1, 6, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 80))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdcDNSDomainName.setStatus('current')
cdcDNSDomainNameStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 436, 1, 1, 6, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdcDNSDomainNameStatus.setStatus('current')
ciscoDNSClientMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 436, 2, 1))
ciscoDNSClientMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 436, 2, 2))
ciscoDNSClientMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 436, 2, 1, 1)).setObjects(("CISCO-DNS-CLIENT-MIB", "ciscoDNSServerConfigGroup"), ("CISCO-DNS-CLIENT-MIB", "ciscoDNSDomainNameConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDNSClientMIBCompliance = ciscoDNSClientMIBCompliance.setStatus('current')
ciscoDNSServerConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 436, 2, 2, 1)).setObjects(("CISCO-DNS-CLIENT-MIB", "cdcDNSConfigEnable"), ("CISCO-DNS-CLIENT-MIB", "cdcNoOfDNSServerConfig"), ("CISCO-DNS-CLIENT-MIB", "cdcDNSServerNextAvailIndex"), ("CISCO-DNS-CLIENT-MIB", "cdcDNSServerAddrType"), ("CISCO-DNS-CLIENT-MIB", "cdcDNSServerAddr"), ("CISCO-DNS-CLIENT-MIB", "cdcDNSServerStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDNSServerConfigGroup = ciscoDNSServerConfigGroup.setStatus('current')
ciscoDNSDomainNameConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 436, 2, 2, 2)).setObjects(("CISCO-DNS-CLIENT-MIB", "cdcDefaultDNSDomainName"), ("CISCO-DNS-CLIENT-MIB", "cdcDNSDomainName"), ("CISCO-DNS-CLIENT-MIB", "cdcDNSDomainNameStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDNSDomainNameConfigGroup = ciscoDNSDomainNameConfigGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-DNS-CLIENT-MIB", cdcDNSDomainName=cdcDNSDomainName, ciscoDNSClientMIBCompliances=ciscoDNSClientMIBCompliances, cdcDNSServerStatus=cdcDNSServerStatus, cdcConfigGroup=cdcConfigGroup, cdcDNSDomainNameIndex=cdcDNSDomainNameIndex, ciscoDNSClientMIBCompliance=ciscoDNSClientMIBCompliance, cdcDNSDomainNameStatus=cdcDNSDomainNameStatus, ciscoDNSClientMIBGroups=ciscoDNSClientMIBGroups, PYSNMP_MODULE_ID=ciscoDNSClientMIB, cdcDNSDomainNameEntry=cdcDNSDomainNameEntry, ciscoDNSClientMIBNotifs=ciscoDNSClientMIBNotifs, cdcDNSServerNextAvailIndex=cdcDNSServerNextAvailIndex, cdcDNSDomainNameTable=cdcDNSDomainNameTable, cdcDNSServerAddrType=cdcDNSServerAddrType, ciscoDNSDomainNameConfigGroup=ciscoDNSDomainNameConfigGroup, ciscoDNSServerConfigGroup=ciscoDNSServerConfigGroup, ciscoDNSClientMIB=ciscoDNSClientMIB, cdcDNSServerEntry=cdcDNSServerEntry, cdcDefaultDNSDomainName=cdcDefaultDNSDomainName, cdcDNSServerIndex=cdcDNSServerIndex, cdcNoOfDNSServerConfig=cdcNoOfDNSServerConfig, cdcDNSConfigEnable=cdcDNSConfigEnable, cdcDNSServerTable=cdcDNSServerTable, ciscoDNSClientMIBObjects=ciscoDNSClientMIBObjects, cdcDNSServerAddr=cdcDNSServerAddr, ciscoDNSClientMIBConformance=ciscoDNSClientMIBConformance)