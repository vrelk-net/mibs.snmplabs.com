#
# PySNMP MIB module NET-SNMP-PERIODIC-NOTIFY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NET-SNMP-PERIODIC-NOTIFY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:08:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
netSnmpModuleIDs, netSnmpNotifications, netSnmpObjects = mibBuilder.importSymbols("NET-SNMP-MIB", "netSnmpModuleIDs", "netSnmpNotifications", "netSnmpObjects")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, TimeTicks, Gauge32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter64, Unsigned32, Counter32, Integer32, iso, IpAddress, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "Gauge32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter64", "Unsigned32", "Counter32", "Integer32", "iso", "IpAddress", "ObjectIdentity", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
netSnmpPeriodicNotifyMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 8072, 3, 1, 5))
netSnmpPeriodicNotifyMib.setRevisions(('2011-04-20 00:00',))
if mibBuilder.loadTexts: netSnmpPeriodicNotifyMib.setLastUpdated('201104200000Z')
if mibBuilder.loadTexts: netSnmpPeriodicNotifyMib.setOrganization('www.net-snmp.org')
nsPNScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 1, 5, 1))
nsPNTables = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 1, 5, 2))
nsPNotifyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 1, 5, 3))
nsPNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 1, 5, 4))
nsPNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 1, 5, 4, 0))
nsPNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 3, 1, 5, 4, 1))
nsNotifyPeriodicNotification = NotificationType((1, 3, 6, 1, 4, 1, 8072, 3, 1, 5, 4, 0, 1))
if mibBuilder.loadTexts: nsNotifyPeriodicNotification.setStatus('current')
nsPNPeriodicTime = MibScalar((1, 3, 6, 1, 4, 1, 8072, 3, 1, 5, 3, 1), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: nsPNPeriodicTime.setStatus('current')
nsPNotifyMessageNumber = MibScalar((1, 3, 6, 1, 4, 1, 8072, 3, 1, 5, 3, 2), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: nsPNotifyMessageNumber.setStatus('current')
nsPNotifyMaxMessageNumber = MibScalar((1, 3, 6, 1, 4, 1, 8072, 3, 1, 5, 3, 3), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: nsPNotifyMaxMessageNumber.setStatus('current')
mibBuilder.exportSymbols("NET-SNMP-PERIODIC-NOTIFY-MIB", PYSNMP_MODULE_ID=netSnmpPeriodicNotifyMib, nsPNotifyMaxMessageNumber=nsPNotifyMaxMessageNumber, netSnmpPeriodicNotifyMib=netSnmpPeriodicNotifyMib, nsPNotificationPrefix=nsPNotificationPrefix, nsPNotifyObjects=nsPNotifyObjects, nsPNScalars=nsPNScalars, nsPNotifications=nsPNotifications, nsNotifyPeriodicNotification=nsNotifyPeriodicNotification, nsPNotifyMessageNumber=nsPNotifyMessageNumber, nsPNotificationObjects=nsPNotificationObjects, nsPNPeriodicTime=nsPNPeriodicTime, nsPNTables=nsPNTables)
