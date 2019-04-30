#
# PySNMP MIB module DEVSERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DEVSERVER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:26:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
device, = mibBuilder.importSymbols("ANIROOT-MIB", "device")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, iso, Unsigned32, IpAddress, ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks, Integer32, NotificationType, Counter64, Gauge32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "Unsigned32", "IpAddress", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks", "Integer32", "NotificationType", "Counter64", "Gauge32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
aniDevServer = ModuleIdentity((1, 3, 6, 1, 4, 1, 4325, 2, 5))
if mibBuilder.loadTexts: aniDevServer.setLastUpdated('0105091130Z')
if mibBuilder.loadTexts: aniDevServer.setOrganization('Aperto Networks')
aniDevTftpServer = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 5, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevTftpServer.setStatus('current')
aniDevDhcpServer = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 5, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevDhcpServer.setStatus('current')
aniDevDhcpLeaseExpiration = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 5, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 22))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevDhcpLeaseExpiration.setStatus('current')
aniDevSuDhcpServer = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 5, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevSuDhcpServer.setStatus('current')
aniDevTimeServer = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 5, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aniDevTimeServer.setStatus('current')
aniDevSyslogServer = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 5, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aniDevSyslogServer.setStatus('current')
aniDevSmtpServer = MibScalar((1, 3, 6, 1, 4, 1, 4325, 2, 5, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aniDevSmtpServer.setStatus('current')
mibBuilder.exportSymbols("DEVSERVER-MIB", aniDevSyslogServer=aniDevSyslogServer, aniDevDhcpLeaseExpiration=aniDevDhcpLeaseExpiration, aniDevDhcpServer=aniDevDhcpServer, aniDevTftpServer=aniDevTftpServer, aniDevSmtpServer=aniDevSmtpServer, aniDevTimeServer=aniDevTimeServer, aniDevSuDhcpServer=aniDevSuDhcpServer, aniDevServer=aniDevServer, PYSNMP_MODULE_ID=aniDevServer)
