#
# PySNMP MIB module HUAWEI-USC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-USC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:37:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hwBRASMib, = mibBuilder.importSymbols("HUAWEI-MIB", "hwBRASMib")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ObjectIdentity, Gauge32, ModuleIdentity, Integer32, Counter32, Counter64, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso, Bits, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "ModuleIdentity", "Integer32", "Counter32", "Counter64", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso", "Bits", "Unsigned32", "TimeTicks")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
hwUSC = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19))
hwUSC.setRevisions(('2014-07-11 16:00', '2010-08-11 16:00',))
if mibBuilder.loadTexts: hwUSC.setLastUpdated('201407111600Z')
if mibBuilder.loadTexts: hwUSC.setOrganization('Huawei Technologies Co.,Ltd.')
hwUSCObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1))
hwUSCConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 1), )
if mibBuilder.loadTexts: hwUSCConfigTable.setStatus('current')
hwUSCConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 1, 1), ).setIndexNames((0, "HUAWEI-USC-MIB", "hwUSCPortIndex"))
if mibBuilder.loadTexts: hwUSCConfigEntry.setStatus('current')
hwUSCPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwUSCPortIndex.setStatus('current')
hwUSCInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUSCInterfaceName.setStatus('current')
hwAuthenControlPoint = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("enabled", 0), ("disabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwAuthenControlPoint.setStatus('current')
hwUSCLinkDownOffline = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUSCLinkDownOffline.setStatus('current')
hwUSCControlDownOffline = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUSCControlDownOffline.setStatus('current')
hwUSCUserSyncInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(60, 3600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUSCUserSyncInterval.setStatus('current')
hwUSCUserSyncRetry = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 19, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 300))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwUSCUserSyncRetry.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-USC-MIB", PYSNMP_MODULE_ID=hwUSC, hwUSCObjects=hwUSCObjects, hwUSCPortIndex=hwUSCPortIndex, hwUSC=hwUSC, hwUSCConfigTable=hwUSCConfigTable, hwUSCInterfaceName=hwUSCInterfaceName, hwUSCUserSyncRetry=hwUSCUserSyncRetry, hwUSCLinkDownOffline=hwUSCLinkDownOffline, hwAuthenControlPoint=hwAuthenControlPoint, hwUSCConfigEntry=hwUSCConfigEntry, hwUSCControlDownOffline=hwUSCControlDownOffline, hwUSCUserSyncInterval=hwUSCUserSyncInterval)
