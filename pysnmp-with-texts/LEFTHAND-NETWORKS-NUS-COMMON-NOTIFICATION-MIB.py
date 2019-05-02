#
# PySNMP MIB module LEFTHAND-NETWORKS-NUS-COMMON-NOTIFICATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LEFTHAND-NETWORKS-NUS-COMMON-NOTIFICATION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:06:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
lhnModules, = mibBuilder.importSymbols("LEFTHAND-NETWORKS-GLOBAL-REG", "lhnModules")
lhnNusCommonEvents, lhnNusCommonGroups, lhnNusCommonNotification = mibBuilder.importSymbols("LEFTHAND-NETWORKS-NUS-COMMON-MIB", "lhnNusCommonEvents", "lhnNusCommonGroups", "lhnNusCommonNotification")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, ObjectIdentity, ModuleIdentity, Integer32, Counter64, MibIdentifier, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, Unsigned32, Gauge32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "ModuleIdentity", "Integer32", "Counter64", "MibIdentifier", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "Unsigned32", "Gauge32", "IpAddress")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
lhnNusCommonNotificationModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 9804, 1, 1, 15))
if mibBuilder.loadTexts: lhnNusCommonNotificationModule.setLastUpdated('0206250000Z')
if mibBuilder.loadTexts: lhnNusCommonNotificationModule.setOrganization('LeftHand Networks, Inc.')
if mibBuilder.loadTexts: lhnNusCommonNotificationModule.setContactInfo(' Author: Jose Faria LeftHand Networks postal: 1688 Conestoga St. Boulder, CO 80301 USA email: jfaria@lefthandnetworks.com phone: +1 303 449-4100 ')
if mibBuilder.loadTexts: lhnNusCommonNotificationModule.setDescription('Notification (Trap) items for NUS Devices')
notificationMessageCount = MibScalar((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 13, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: notificationMessageCount.setStatus('current')
if mibBuilder.loadTexts: notificationMessageCount.setDescription('number of notification messages')
notificationMessageTable = MibTable((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 13, 2), )
if mibBuilder.loadTexts: notificationMessageTable.setStatus('current')
if mibBuilder.loadTexts: notificationMessageTable.setDescription('A table of notification messages for the NUS. The number of entries is given by notificationMessageCount.')
notificationMessageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 13, 2, 1), ).setIndexNames((0, "LEFTHAND-NETWORKS-NUS-COMMON-NOTIFICATION-MIB", "notificationIndex"))
if mibBuilder.loadTexts: notificationMessageEntry.setStatus('current')
if mibBuilder.loadTexts: notificationMessageEntry.setDescription('A row of notification messages for the NUS.')
notificationIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 13, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: notificationIndex.setStatus('current')
if mibBuilder.loadTexts: notificationIndex.setDescription('notification message index')
notificationMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 13, 2, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: notificationMessage.setStatus('current')
if mibBuilder.loadTexts: notificationMessage.setDescription('notification message contents')
notificationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 13, 2, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: notificationTime.setStatus('current')
if mibBuilder.loadTexts: notificationTime.setDescription('time notification occurred')
userNotification = NotificationType((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 3, 1)).setObjects(("LEFTHAND-NETWORKS-NUS-COMMON-NOTIFICATION-MIB", "notificationMessage"))
if mibBuilder.loadTexts: userNotification.setStatus('current')
if mibBuilder.loadTexts: userNotification.setDescription('A system variable being monitored reached a threshold. The user chose to be notified of this condition via SNMP. A table of messages exists which stores all the notifications issued. This trap will carry the OID referring to the corresponding message stored in this table.')
lhnNusCommonEventGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 1, 1, 2)).setObjects(("LEFTHAND-NETWORKS-NUS-COMMON-NOTIFICATION-MIB", "userNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lhnNusCommonEventGroup = lhnNusCommonEventGroup.setStatus('current')
if mibBuilder.loadTexts: lhnNusCommonEventGroup.setDescription('Events defined for NUS devices')
mibBuilder.exportSymbols("LEFTHAND-NETWORKS-NUS-COMMON-NOTIFICATION-MIB", notificationMessageCount=notificationMessageCount, notificationMessageTable=notificationMessageTable, notificationIndex=notificationIndex, notificationMessage=notificationMessage, notificationMessageEntry=notificationMessageEntry, lhnNusCommonNotificationModule=lhnNusCommonNotificationModule, notificationTime=notificationTime, lhnNusCommonEventGroup=lhnNusCommonEventGroup, PYSNMP_MODULE_ID=lhnNusCommonNotificationModule, userNotification=userNotification)