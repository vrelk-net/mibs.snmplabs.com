#
# PySNMP MIB module MIMOSA-NETWORKS-BASE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MIMOSA-NETWORKS-BASE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:12:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, enterprises, ObjectIdentity, Gauge32, IpAddress, iso, Integer32, Unsigned32, Bits, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "enterprises", "ObjectIdentity", "Gauge32", "IpAddress", "iso", "Integer32", "Unsigned32", "Bits", "NotificationType", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mimosa = ModuleIdentity((1, 3, 6, 1, 4, 1, 43356))
mimosa.setRevisions(('2015-06-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mimosa.setRevisionsDescriptions(('First draft',))
if mibBuilder.loadTexts: mimosa.setLastUpdated('201506030000Z')
if mibBuilder.loadTexts: mimosa.setOrganization('Mimosa Networks www.mimosa.co')
if mibBuilder.loadTexts: mimosa.setContactInfo('postal: Mimosa Networks, Inc. 300 Orchard City Dr. Campbell, CA 95008 email: support@mimosa.co')
if mibBuilder.loadTexts: mimosa.setDescription('Mimosa device MIB definitions')
mimosaProduct = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 1))
mimosaMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2))
mimosaHardware = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 1, 1))
mimosaSoftware = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 1, 2))
mimosaB5 = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 1, 1, 1))
mimosaB5Lite = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 1, 1, 2))
mimosaA5 = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 1, 1, 3))
mimosaC5 = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 1, 1, 4))
mimosaTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2, 0))
mimosaMib = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2, 1))
mimosaMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2, 3))
mimosaConformanceGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2, 4))
mimosaTrapMib = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2, 1, 1))
mimosaWireless = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2))
mimosaTrapMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 43356, 2, 3, 1)).setObjects(("MIMOSA-NETWORKS-BASE-MIB", "mimosaTrapMessage"), ("MIMOSA-NETWORKS-BASE-MIB", "mimosaOldSpeed"), ("MIMOSA-NETWORKS-BASE-MIB", "mimosaNewSpeed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mimosaTrapMIBGroup = mimosaTrapMIBGroup.setStatus('current')
if mibBuilder.loadTexts: mimosaTrapMIBGroup.setDescription('A collection of objects providing basic Trap function.')
mimosaTrapMessage = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaTrapMessage.setStatus('current')
if mibBuilder.loadTexts: mimosaTrapMessage.setDescription('General Octet String object to contain message sent with traps.')
mimosaOldSpeed = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaOldSpeed.setStatus('current')
if mibBuilder.loadTexts: mimosaOldSpeed.setDescription('The speed of the Ethernet link before the change within Ethernet Speed Change Notifications.')
mimosaNewSpeed = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaNewSpeed.setStatus('current')
if mibBuilder.loadTexts: mimosaNewSpeed.setDescription('The speed of the Ethernet link after the change within Ethernet Speed Change Notifications.')
mimosaGenericNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 43356, 2, 3, 2)).setObjects(("MIMOSA-NETWORKS-BASE-MIB", "mimosaCriticalFault"), ("MIMOSA-NETWORKS-BASE-MIB", "mimosaTempWarning"), ("MIMOSA-NETWORKS-BASE-MIB", "mimosaTempNormal"), ("MIMOSA-NETWORKS-BASE-MIB", "mimosaEthernetSpeedChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mimosaGenericNotificationsGroup = mimosaGenericNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: mimosaGenericNotificationsGroup.setDescription('The basic Trap notifications for all Mimosa products.')
mimosaCriticalFault = NotificationType((1, 3, 6, 1, 4, 1, 43356, 2, 0, 1)).setObjects(("MIMOSA-NETWORKS-BASE-MIB", "mimosaTrapMessage"))
if mibBuilder.loadTexts: mimosaCriticalFault.setStatus('current')
if mibBuilder.loadTexts: mimosaCriticalFault.setDescription('The mimosaCriticalFault notification is sent when the log manager in the Mimosa product determines that a fault with a critical severity has been detected. The mimosaCriticalFaultLog contains the description of the general error.')
mimosaTempWarning = NotificationType((1, 3, 6, 1, 4, 1, 43356, 2, 0, 2)).setObjects(("MIMOSA-NETWORKS-BASE-MIB", "mimosaTrapMessage"))
if mibBuilder.loadTexts: mimosaTempWarning.setStatus('current')
if mibBuilder.loadTexts: mimosaTempWarning.setDescription('The mimosaTempWarning notification is sent when the log manager in the Mimosa product receives an indication that the temperature is outside the safe range.')
mimosaTempNormal = NotificationType((1, 3, 6, 1, 4, 1, 43356, 2, 0, 3)).setObjects(("MIMOSA-NETWORKS-BASE-MIB", "mimosaTrapMessage"))
if mibBuilder.loadTexts: mimosaTempNormal.setStatus('current')
if mibBuilder.loadTexts: mimosaTempNormal.setDescription('The mimosaTempNormal notification is sent when the log manager in the Mimosa product receives an indication that the temperature is with in the safe range.')
mimosaEthernetSpeedChange = NotificationType((1, 3, 6, 1, 4, 1, 43356, 2, 0, 4)).setObjects(("IF-MIB", "ifIndex"), ("MIMOSA-NETWORKS-BASE-MIB", "mimosaOldSpeed"), ("MIMOSA-NETWORKS-BASE-MIB", "mimosaNewSpeed"))
if mibBuilder.loadTexts: mimosaEthernetSpeedChange.setStatus('current')
if mibBuilder.loadTexts: mimosaEthernetSpeedChange.setDescription('The mimosaEthernetSpeedChange notification is sent when the log manager in the Mimosa product determines that a speed change on the Ethernet port was detected. The mimosaOldSpeed and mimosaNewSpeed indicates the speed in bits per second of the change. ifIndex is used per the ifTable in the IF-MIB.')
mibBuilder.exportSymbols("MIMOSA-NETWORKS-BASE-MIB", mimosaGenericNotificationsGroup=mimosaGenericNotificationsGroup, mimosaProduct=mimosaProduct, mimosaTempNormal=mimosaTempNormal, mimosa=mimosa, mimosaHardware=mimosaHardware, mimosaConformanceGroup=mimosaConformanceGroup, mimosaNewSpeed=mimosaNewSpeed, mimosaMgmt=mimosaMgmt, mimosaTrapMIBGroup=mimosaTrapMIBGroup, mimosaTrapMessage=mimosaTrapMessage, mimosaB5=mimosaB5, mimosaMIBGroups=mimosaMIBGroups, mimosaOldSpeed=mimosaOldSpeed, mimosaTrap=mimosaTrap, mimosaEthernetSpeedChange=mimosaEthernetSpeedChange, mimosaMib=mimosaMib, mimosaTrapMib=mimosaTrapMib, mimosaTempWarning=mimosaTempWarning, mimosaA5=mimosaA5, mimosaCriticalFault=mimosaCriticalFault, mimosaB5Lite=mimosaB5Lite, mimosaC5=mimosaC5, mimosaWireless=mimosaWireless, PYSNMP_MODULE_ID=mimosa, mimosaSoftware=mimosaSoftware)