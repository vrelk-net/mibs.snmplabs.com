#
# PySNMP MIB module HUAWEI-VP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-VP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:49:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
ifName, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifName", "ifIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter32, Counter64, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Bits, ObjectIdentity, IpAddress, MibIdentifier, TimeTicks, ModuleIdentity, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Bits", "ObjectIdentity", "IpAddress", "MibIdentifier", "TimeTicks", "ModuleIdentity", "Unsigned32", "Integer32")
RowStatus, DisplayString, TextualConvention, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention", "MacAddress")
hwVpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 307))
hwVpMIB.setRevisions(('2014-07-16 13:50',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hwVpMIB.setRevisionsDescriptions(('V1.11, modified the MAX-ACCESS of hwVpVmVlan, hwVpVmMac and hwVpVmProfileId.',))
if mibBuilder.loadTexts: hwVpMIB.setLastUpdated('201407161350Z')
if mibBuilder.loadTexts: hwVpMIB.setOrganization('Huawei Technologies Co.,Ltd.')
if mibBuilder.loadTexts: hwVpMIB.setContactInfo("Huawei Industrial Base Bantian, Longgang Shenzhen 518129 People's Republic of China Website: http://www.huawei.com Email: support@huawei.com")
if mibBuilder.loadTexts: hwVpMIB.setDescription('The HUAWEI-VP-MIB contains objects to Manage configuration and Monitor running state for virtual perception feature.')
hwVpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 307, 1))
hwVpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 307, 2))
hwVpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 307, 3))
hwVpVmTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 307, 1, 1), )
if mibBuilder.loadTexts: hwVpVmTable.setStatus('current')
if mibBuilder.loadTexts: hwVpVmTable.setDescription('Table of VM.')
hwVpVmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 307, 1, 1, 1), ).setIndexNames((0, "HUAWEI-VP-MIB", "hwVpVmVlan"), (0, "HUAWEI-VP-MIB", "hwVpVmMac"))
if mibBuilder.loadTexts: hwVpVmEntry.setStatus('current')
if mibBuilder.loadTexts: hwVpVmEntry.setDescription('Provides information about VM entry.')
hwVpVmVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 307, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwVpVmVlan.setStatus('current')
if mibBuilder.loadTexts: hwVpVmVlan.setDescription('This object indicates the VLAN of VM.')
hwVpVmMac = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 307, 1, 1, 1, 2), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwVpVmMac.setStatus('current')
if mibBuilder.loadTexts: hwVpVmMac.setDescription('This object indicates the MAC of VM.')
hwVpVmProfileId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 307, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwVpVmProfileId.setStatus('current')
if mibBuilder.loadTexts: hwVpVmProfileId.setDescription('This object indicates the profile ID of VM.')
hwVpVmDownloadProfileFault = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 307, 2, 1)).setObjects(("HUAWEI-VP-MIB", "hwVpVmVlan"), ("HUAWEI-VP-MIB", "hwVpVmMac"), ("HUAWEI-VP-MIB", "hwVpVmProfileId"), ("IF-MIB", "ifIndex"), ("IF-MIB", "ifName"))
if mibBuilder.loadTexts: hwVpVmDownloadProfileFault.setStatus('current')
if mibBuilder.loadTexts: hwVpVmDownloadProfileFault.setDescription('The alarm is reported when VM fail to download profile.')
hwVpVmDownloadProfileFaultResume = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 307, 2, 2)).setObjects(("HUAWEI-VP-MIB", "hwVpVmVlan"), ("HUAWEI-VP-MIB", "hwVpVmMac"), ("HUAWEI-VP-MIB", "hwVpVmProfileId"), ("IF-MIB", "ifIndex"), ("IF-MIB", "ifName"))
if mibBuilder.loadTexts: hwVpVmDownloadProfileFaultResume.setStatus('current')
if mibBuilder.loadTexts: hwVpVmDownloadProfileFaultResume.setDescription('The event is reported when VM succeed in downloading profile.')
hwVpVmAuthenticateFail = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 307, 2, 3)).setObjects(("HUAWEI-VP-MIB", "hwVpVmVlan"), ("HUAWEI-VP-MIB", "hwVpVmMac"), ("HUAWEI-VP-MIB", "hwVpVmProfileId"), ("IF-MIB", "ifIndex"), ("IF-MIB", "ifName"))
if mibBuilder.loadTexts: hwVpVmAuthenticateFail.setStatus('current')
if mibBuilder.loadTexts: hwVpVmAuthenticateFail.setDescription('The alarm is reported when VM fail to pass authentication.')
hwVpVmDeliverAuthorInformationFail = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 307, 2, 4)).setObjects(("HUAWEI-VP-MIB", "hwVpVmVlan"), ("HUAWEI-VP-MIB", "hwVpVmMac"), ("HUAWEI-VP-MIB", "hwVpVmProfileId"), ("IF-MIB", "ifIndex"), ("IF-MIB", "ifName"))
if mibBuilder.loadTexts: hwVpVmDeliverAuthorInformationFail.setStatus('current')
if mibBuilder.loadTexts: hwVpVmDeliverAuthorInformationFail.setDescription('The alarm is reported when VM fail to deliver authorization information.')
hwVpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 307, 3, 1))
hwVpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 307, 3, 1, 1)).setObjects(("HUAWEI-VP-MIB", "hwVpObjectGroup"), ("HUAWEI-VP-MIB", "hwVpNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwVpCompliance = hwVpCompliance.setStatus('current')
if mibBuilder.loadTexts: hwVpCompliance.setDescription('This is the virtual perception compliance.')
hwVpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 307, 3, 2))
hwVpObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 307, 3, 2, 1)).setObjects(("HUAWEI-VP-MIB", "hwVpVmMac"), ("HUAWEI-VP-MIB", "hwVpVmVlan"), ("HUAWEI-VP-MIB", "hwVpVmProfileId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwVpObjectGroup = hwVpObjectGroup.setStatus('current')
if mibBuilder.loadTexts: hwVpObjectGroup.setDescription('This is the virtual perception object group.')
hwVpNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 307, 3, 2, 2)).setObjects(("HUAWEI-VP-MIB", "hwVpVmDownloadProfileFault"), ("HUAWEI-VP-MIB", "hwVpVmDownloadProfileFaultResume"), ("HUAWEI-VP-MIB", "hwVpVmAuthenticateFail"), ("HUAWEI-VP-MIB", "hwVpVmDeliverAuthorInformationFail"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwVpNotificationGroup = hwVpNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: hwVpNotificationGroup.setDescription('This is the virtual perception notification group.')
mibBuilder.exportSymbols("HUAWEI-VP-MIB", hwVpObjects=hwVpObjects, hwVpVmDownloadProfileFault=hwVpVmDownloadProfileFault, hwVpVmProfileId=hwVpVmProfileId, PYSNMP_MODULE_ID=hwVpMIB, hwVpMIB=hwVpMIB, hwVpNotificationGroup=hwVpNotificationGroup, hwVpConformance=hwVpConformance, hwVpVmTable=hwVpVmTable, hwVpVmAuthenticateFail=hwVpVmAuthenticateFail, hwVpObjectGroup=hwVpObjectGroup, hwVpVmDeliverAuthorInformationFail=hwVpVmDeliverAuthorInformationFail, hwVpCompliance=hwVpCompliance, hwVpVmVlan=hwVpVmVlan, hwVpCompliances=hwVpCompliances, hwVpNotifications=hwVpNotifications, hwVpGroups=hwVpGroups, hwVpVmEntry=hwVpVmEntry, hwVpVmDownloadProfileFaultResume=hwVpVmDownloadProfileFaultResume, hwVpVmMac=hwVpVmMac)