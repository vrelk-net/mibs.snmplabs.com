#
# PySNMP MIB module INTELCORPORATION-MULTI-FLEX-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/INTELCORPORATION-MULTI-FLEX-SERVER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:43:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
regModule, groups, eventType, detail, component, severity, instanceId, notifications, components, user, eventId = mibBuilder.importSymbols("INTELCORPORATION-MULTI-FLEX-SERVER-REG", "regModule", "groups", "eventType", "detail", "component", "severity", "instanceId", "notifications", "components", "user", "eventId")
Power, IdromBinary16 = mibBuilder.importSymbols("INTELCORPORATION-MULTI-FLEX-SERVER-TC", "Power", "IdromBinary16")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter64, IpAddress, Gauge32, ObjectIdentity, Bits, MibIdentifier, Unsigned32, ModuleIdentity, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "Gauge32", "ObjectIdentity", "Bits", "MibIdentifier", "Unsigned32", "ModuleIdentity", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
multiFlexServerMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 1, 1, 10))
multiFlexServerMibModule.setRevisions(('2007-08-21 17:00', '2007-08-16 13:30', '2007-07-16 11:30', '2007-06-07 20:30', '2007-06-07 13:30', '2007-05-30 13:30', '2007-05-30 10:30', '2007-04-09 10:30', '2007-03-12 18:30', '2007-03-06 10:30', '2007-02-22 17:00', '2006-11-01 10:00', '2006-09-29 15:29', '2006-09-28 17:32', '2006-09-01 06:24',))
if mibBuilder.loadTexts: multiFlexServerMibModule.setLastUpdated('200708211700Z')
if mibBuilder.loadTexts: multiFlexServerMibModule.setOrganization('Intel Corporation')
chassis = ObjectIdentity((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10))
if mibBuilder.loadTexts: chassis.setStatus('current')
chassisVendor = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisVendor.setStatus('current')
chassisMfgDate = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisMfgDate.setStatus('current')
chassisDeviceName = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisDeviceName.setStatus('current')
chassisPart = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 4), IdromBinary16()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisPart.setStatus('current')
chassisSerialNo = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 5), IdromBinary16()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisSerialNo.setStatus('current')
chassisMaximumPower = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 6), Power()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisMaximumPower.setStatus('current')
chassisNominalPower = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 7), Power()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisNominalPower.setStatus('current')
chassisAssetTag = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 8), IdromBinary16()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisAssetTag.setStatus('current')
chassisGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 2, 2, 10)).setObjects(("INTELCORPORATION-MULTI-FLEX-SERVER-MIB", "chassisVendor"), ("INTELCORPORATION-MULTI-FLEX-SERVER-MIB", "chassisMfgDate"), ("INTELCORPORATION-MULTI-FLEX-SERVER-MIB", "chassisDeviceName"), ("INTELCORPORATION-MULTI-FLEX-SERVER-MIB", "chassisPart"), ("INTELCORPORATION-MULTI-FLEX-SERVER-MIB", "chassisSerialNo"), ("INTELCORPORATION-MULTI-FLEX-SERVER-MIB", "chassisMaximumPower"), ("INTELCORPORATION-MULTI-FLEX-SERVER-MIB", "chassisNominalPower"), ("INTELCORPORATION-MULTI-FLEX-SERVER-MIB", "chassisAssetTag"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chassisGroup = chassisGroup.setStatus('current')
genericChassisEvent = NotificationType((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 0, 10)).setObjects(("INTELCORPORATION-MULTI-FLEX-SERVER-REG", "component"), ("INTELCORPORATION-MULTI-FLEX-SERVER-REG", "severity"), ("INTELCORPORATION-MULTI-FLEX-SERVER-REG", "eventType"), ("INTELCORPORATION-MULTI-FLEX-SERVER-REG", "user"), ("INTELCORPORATION-MULTI-FLEX-SERVER-REG", "instanceId"), ("INTELCORPORATION-MULTI-FLEX-SERVER-REG", "detail"), ("INTELCORPORATION-MULTI-FLEX-SERVER-REG", "eventId"))
if mibBuilder.loadTexts: genericChassisEvent.setStatus('current')
chassisNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 2, 2, 110)).setObjects(("INTELCORPORATION-MULTI-FLEX-SERVER-MIB", "genericChassisEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    chassisNotificationGroup = chassisNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("INTELCORPORATION-MULTI-FLEX-SERVER-MIB", multiFlexServerMibModule=multiFlexServerMibModule, chassisPart=chassisPart, chassisGroup=chassisGroup, chassisMaximumPower=chassisMaximumPower, chassisNotificationGroup=chassisNotificationGroup, PYSNMP_MODULE_ID=multiFlexServerMibModule, chassisMfgDate=chassisMfgDate, chassisNominalPower=chassisNominalPower, chassis=chassis, chassisVendor=chassisVendor, chassisDeviceName=chassisDeviceName, chassisSerialNo=chassisSerialNo, genericChassisEvent=genericChassisEvent, chassisAssetTag=chassisAssetTag)
