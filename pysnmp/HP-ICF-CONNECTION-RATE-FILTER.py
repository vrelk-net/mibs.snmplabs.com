#
# PySNMP MIB module HP-ICF-CONNECTION-RATE-FILTER (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-CONNECTION-RATE-FILTER
# Produced by pysmi-0.3.4 at Mon Apr 29 19:20:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ObjectIdentity, ModuleIdentity, iso, IpAddress, Integer32, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32, Gauge32, Counter64, NotificationType, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "ModuleIdentity", "iso", "IpAddress", "Integer32", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32", "Gauge32", "Counter64", "NotificationType", "MibIdentifier")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
hpicfConnectionRateFilter = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24))
hpicfConnectionRateFilter.setRevisions(('2009-05-12 01:08', '2004-09-07 01:08',))
if mibBuilder.loadTexts: hpicfConnectionRateFilter.setLastUpdated('200905120108Z')
if mibBuilder.loadTexts: hpicfConnectionRateFilter.setOrganization('HP Networking')
hpicfConnectionRateFilterNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24, 0))
hpicfConnectionRateFilterNotificationControl = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24, 1))
hpicfConnectionRateFilterObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24, 2))
hpicfConnectionRateFilterConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24, 3))
hpicfConnectionRateFilterIfModeConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24, 4))
hpicfConnectionRateFilterNotification = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24, 0, 1)).setObjects(("HP-ICF-CONNECTION-RATE-FILTER", "hpicifConnectionRateFilterVlanId"), ("HP-ICF-CONNECTION-RATE-FILTER", "hpicifConnectionRateFilterInetAddress"), ("HP-ICF-CONNECTION-RATE-FILTER", "hpicifConnectionRateFilterInetAddressType"), ("HP-ICF-CONNECTION-RATE-FILTER", "hpicifConnectionRateFilterMode"))
if mibBuilder.loadTexts: hpicfConnectionRateFilterNotification.setStatus('current')
hpicifConnectionRateFilterVlanId = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpicifConnectionRateFilterVlanId.setStatus('current')
hpicifConnectionRateFilterInetAddress = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24, 2, 2), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpicifConnectionRateFilterInetAddress.setStatus('current')
hpicifConnectionRateFilterInetAddressType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24, 2, 3), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpicifConnectionRateFilterInetAddressType.setStatus('current')
hpicifConnectionRateFilterMode = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("inform", 0), ("throttle", 1), ("block", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpicifConnectionRateFilterMode.setStatus('current')
hpicfConnectionRateFilterIfModeConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24, 4, 1), )
if mibBuilder.loadTexts: hpicfConnectionRateFilterIfModeConfigTable.setStatus('current')
hpicfConnectionRateFilterIfModeConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24, 4, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpicfConnectionRateFilterIfModeConfigEntry.setStatus('current')
hpicfConnectionRateFilterIfModeValue = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("none", 0), ("inform", 1), ("throttle", 2), ("block", 3))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfConnectionRateFilterIfModeValue.setStatus('current')
hpicfConnectionRateFilterNotificationControlEnable = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfConnectionRateFilterNotificationControlEnable.setStatus('current')
hpicfConnectionRateFilterSensitivity = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 0), ("low", 1), ("medium", 2), ("high", 3), ("aggressive", 4))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfConnectionRateFilterSensitivity.setStatus('current')
hpicfConnectionRateFilterCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24, 3, 1))
hpicfConnectionRateFilterGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24, 3, 2))
hpicfConnectionRateFilterCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24, 3, 1, 1)).setObjects(("HP-ICF-CONNECTION-RATE-FILTER", "hpicfConnectionRateFilterNotifyGroup"), ("HP-ICF-CONNECTION-RATE-FILTER", "hpicfConnectionRateFilterObjectGroup"), ("HP-ICF-CONNECTION-RATE-FILTER", "hpicfConnectionRateFilterNotifyGroup"), ("HP-ICF-CONNECTION-RATE-FILTER", "hpicfConnectionRateFilterObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfConnectionRateFilterCompliance = hpicfConnectionRateFilterCompliance.setStatus('current')
hpicfConnectionRateFilterCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24, 3, 1, 2)).setObjects(("HP-ICF-CONNECTION-RATE-FILTER", "hpicfConnectionRateFilterObjectGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfConnectionRateFilterCompliance1 = hpicfConnectionRateFilterCompliance1.setStatus('current')
hpicfConnectionRateFilterNotifyGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24, 3, 2, 1)).setObjects(("HP-ICF-CONNECTION-RATE-FILTER", "hpicfConnectionRateFilterNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfConnectionRateFilterNotifyGroup = hpicfConnectionRateFilterNotifyGroup.setStatus('current')
hpicfConnectionRateFilterObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24, 3, 2, 2)).setObjects(("HP-ICF-CONNECTION-RATE-FILTER", "hpicfConnectionRateFilterNotificationControlEnable"), ("HP-ICF-CONNECTION-RATE-FILTER", "hpicfConnectionRateFilterIfModeValue"), ("HP-ICF-CONNECTION-RATE-FILTER", "hpicfConnectionRateFilterSensitivity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfConnectionRateFilterObjectGroup = hpicfConnectionRateFilterObjectGroup.setStatus('current')
hpicfConnectionRateFilterObjectGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24, 3, 2, 3)).setObjects(("HP-ICF-CONNECTION-RATE-FILTER", "hpicifConnectionRateFilterVlanId"), ("HP-ICF-CONNECTION-RATE-FILTER", "hpicifConnectionRateFilterInetAddress"), ("HP-ICF-CONNECTION-RATE-FILTER", "hpicifConnectionRateFilterInetAddressType"), ("HP-ICF-CONNECTION-RATE-FILTER", "hpicifConnectionRateFilterMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfConnectionRateFilterObjectGroup1 = hpicfConnectionRateFilterObjectGroup1.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-CONNECTION-RATE-FILTER", hpicifConnectionRateFilterInetAddressType=hpicifConnectionRateFilterInetAddressType, hpicfConnectionRateFilterNotification=hpicfConnectionRateFilterNotification, hpicfConnectionRateFilterNotifications=hpicfConnectionRateFilterNotifications, hpicfConnectionRateFilterIfModeConfig=hpicfConnectionRateFilterIfModeConfig, hpicifConnectionRateFilterMode=hpicifConnectionRateFilterMode, hpicfConnectionRateFilterObjects=hpicfConnectionRateFilterObjects, PYSNMP_MODULE_ID=hpicfConnectionRateFilter, hpicifConnectionRateFilterInetAddress=hpicifConnectionRateFilterInetAddress, hpicfConnectionRateFilterNotificationControlEnable=hpicfConnectionRateFilterNotificationControlEnable, hpicfConnectionRateFilterObjectGroup1=hpicfConnectionRateFilterObjectGroup1, hpicifConnectionRateFilterVlanId=hpicifConnectionRateFilterVlanId, hpicfConnectionRateFilterSensitivity=hpicfConnectionRateFilterSensitivity, hpicfConnectionRateFilterNotifyGroup=hpicfConnectionRateFilterNotifyGroup, hpicfConnectionRateFilter=hpicfConnectionRateFilter, hpicfConnectionRateFilterCompliance1=hpicfConnectionRateFilterCompliance1, hpicfConnectionRateFilterIfModeConfigTable=hpicfConnectionRateFilterIfModeConfigTable, hpicfConnectionRateFilterObjectGroup=hpicfConnectionRateFilterObjectGroup, hpicfConnectionRateFilterCompliance=hpicfConnectionRateFilterCompliance, hpicfConnectionRateFilterIfModeValue=hpicfConnectionRateFilterIfModeValue, hpicfConnectionRateFilterNotificationControl=hpicfConnectionRateFilterNotificationControl, hpicfConnectionRateFilterCompliances=hpicfConnectionRateFilterCompliances, hpicfConnectionRateFilterIfModeConfigEntry=hpicfConnectionRateFilterIfModeConfigEntry, hpicfConnectionRateFilterGroups=hpicfConnectionRateFilterGroups, hpicfConnectionRateFilterConformance=hpicfConnectionRateFilterConformance)
