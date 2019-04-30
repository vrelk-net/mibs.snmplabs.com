#
# PySNMP MIB module CIENA-CES-CONFIG-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CIENA-CES-CONFIG-MGMT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:31:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
cienaGlobalSeverity, = mibBuilder.importSymbols("CIENA-GLOBAL-MIB", "cienaGlobalSeverity")
cienaCesNotifications, cienaCesConfig = mibBuilder.importSymbols("CIENA-SMI", "cienaCesNotifications", "cienaCesConfig")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, NotificationType, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ObjectIdentity, IpAddress, Counter32, Gauge32, MibIdentifier, Counter64, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ObjectIdentity", "IpAddress", "Counter32", "Gauge32", "MibIdentifier", "Counter64", "TimeTicks", "iso")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
cienaCesConfigMgmtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1271, 2, 1, 36))
cienaCesConfigMgmtMIB.setRevisions(('2015-02-11 00:00',))
if mibBuilder.loadTexts: cienaCesConfigMgmtMIB.setLastUpdated('201502110000Z')
if mibBuilder.loadTexts: cienaCesConfigMgmtMIB.setOrganization('Ciena, Inc')
class CienaCesConfigMgmtContext(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("cli", 2), ("snmp", 3), ("netconf", 4))

cienaCesConfigMgmtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 2, 1, 36, 1))
cienaCesConfigMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 2, 1, 36, 1, 1))
cienaCesConfigMgmtMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 2, 2, 36))
cienaCesConfigMgmtMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 2, 2, 36, 0))
cienaCesConfigMgmtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 2, 1, 36, 2))
cienaCesConfigMgmtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 2, 1, 36, 2, 1))
cienaCesConfigMgmtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 2, 1, 36, 2, 2))
cienaCesConfigMgmtConfigLastSaved = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 36, 1, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesConfigMgmtConfigLastSaved.setStatus('current')
cienaCesConfigMgmtConfigLastChanged = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 36, 1, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesConfigMgmtConfigLastChanged.setStatus('current')
cienaCesConfigMgmtConfigLastContext = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 36, 1, 1, 3), CienaCesConfigMgmtContext()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesConfigMgmtConfigLastContext.setStatus('current')
cienaCesConfigMgmtConfigLastUser = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 36, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesConfigMgmtConfigLastUser.setStatus('current')
cienaCesConfigMgmtConfigLastOrigin = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 36, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesConfigMgmtConfigLastOrigin.setStatus('current')
cienaCesConfigMgmtConfigSavedNotification = NotificationType((1, 3, 6, 1, 4, 1, 1271, 2, 2, 36, 0, 1)).setObjects(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"), ("CIENA-CES-CONFIG-MGMT-MIB", "cienaCesConfigMgmtConfigLastSaved"), ("CIENA-CES-CONFIG-MGMT-MIB", "cienaCesConfigMgmtConfigLastChanged"))
if mibBuilder.loadTexts: cienaCesConfigMgmtConfigSavedNotification.setStatus('current')
cienaCesConfigMgmtConfigChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 1271, 2, 2, 36, 0, 2)).setObjects(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"), ("CIENA-CES-CONFIG-MGMT-MIB", "cienaCesConfigMgmtConfigLastContext"), ("CIENA-CES-CONFIG-MGMT-MIB", "cienaCesConfigMgmtConfigLastUser"), ("CIENA-CES-CONFIG-MGMT-MIB", "cienaCesConfigMgmtConfigLastOrigin"), ("CIENA-CES-CONFIG-MGMT-MIB", "cienaCesConfigMgmtConfigLastChanged"))
if mibBuilder.loadTexts: cienaCesConfigMgmtConfigChangeNotification.setStatus('current')
mibBuilder.exportSymbols("CIENA-CES-CONFIG-MGMT-MIB", cienaCesConfigMgmtConfigLastChanged=cienaCesConfigMgmtConfigLastChanged, cienaCesConfigMgmtConfigLastUser=cienaCesConfigMgmtConfigLastUser, cienaCesConfigMgmtMIB=cienaCesConfigMgmtMIB, CienaCesConfigMgmtContext=CienaCesConfigMgmtContext, cienaCesConfigMgmtMIBObjects=cienaCesConfigMgmtMIBObjects, cienaCesConfigMgmtMIBNotifications=cienaCesConfigMgmtMIBNotifications, cienaCesConfigMgmtMIBGroups=cienaCesConfigMgmtMIBGroups, cienaCesConfigMgmtConfigLastSaved=cienaCesConfigMgmtConfigLastSaved, cienaCesConfigMgmtConfigSavedNotification=cienaCesConfigMgmtConfigSavedNotification, PYSNMP_MODULE_ID=cienaCesConfigMgmtMIB, cienaCesConfigMgmtConfigChangeNotification=cienaCesConfigMgmtConfigChangeNotification, cienaCesConfigMgmtConfigLastOrigin=cienaCesConfigMgmtConfigLastOrigin, cienaCesConfigMgmtConfigLastContext=cienaCesConfigMgmtConfigLastContext, cienaCesConfigMgmtMIBNotificationsPrefix=cienaCesConfigMgmtMIBNotificationsPrefix, cienaCesConfigMgmtMIBCompliances=cienaCesConfigMgmtMIBCompliances, cienaCesConfigMgmt=cienaCesConfigMgmt, cienaCesConfigMgmtMIBConformance=cienaCesConfigMgmtMIBConformance)
