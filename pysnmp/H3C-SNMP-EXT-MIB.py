#
# PySNMP MIB module H3C-SNMP-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-SNMP-EXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:10:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
SnmpSecurityModel, SnmpAdminString, SnmpSecurityLevel = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpSecurityModel", "SnmpAdminString", "SnmpSecurityLevel")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ModuleIdentity, TimeTicks, MibIdentifier, Counter64, Counter32, ObjectIdentity, Integer32, IpAddress, Unsigned32, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ModuleIdentity", "TimeTicks", "MibIdentifier", "Counter64", "Counter32", "ObjectIdentity", "Integer32", "IpAddress", "Unsigned32", "iso", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
h3cSnmpExt = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 104))
h3cSnmpExt.setRevisions(('2009-04-07 17:00',))
if mibBuilder.loadTexts: h3cSnmpExt.setLastUpdated('200904071700Z')
if mibBuilder.loadTexts: h3cSnmpExt.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
h3cSnmpExtScalarObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 104, 1))
h3cSnmpExtTables = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 104, 2))
h3cSnmpExtNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 104, 3))
h3cSnmpExtSnmpChannel = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 104, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(161)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSnmpExtSnmpChannel.setStatus('current')
h3cSnmpExtReadCommunitySingle = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 104, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSnmpExtReadCommunitySingle.setStatus('current')
h3cSnmpExtWriteCommunitySingle = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 104, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSnmpExtWriteCommunitySingle.setStatus('current')
h3cSnmpExtCommunityTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 104, 2, 1), )
if mibBuilder.loadTexts: h3cSnmpExtCommunityTable.setStatus('current')
h3cSnmpExtCommunityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 104, 2, 1, 1), ).setIndexNames((0, "H3C-SNMP-EXT-MIB", "h3cSnmpExtCommunitySecurityLevel"), (0, "H3C-SNMP-EXT-MIB", "h3cSnmpExtCommunitySecurityName"))
if mibBuilder.loadTexts: h3cSnmpExtCommunityEntry.setStatus('current')
h3cSnmpExtCommunitySecurityLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 104, 2, 1, 1, 1), SnmpSecurityModel())
if mibBuilder.loadTexts: h3cSnmpExtCommunitySecurityLevel.setStatus('current')
h3cSnmpExtCommunitySecurityName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 104, 2, 1, 1, 2), SnmpAdminString())
if mibBuilder.loadTexts: h3cSnmpExtCommunitySecurityName.setStatus('current')
h3cSnmpExtCommunityName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 104, 2, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cSnmpExtCommunityName.setStatus('current')
h3cSnmpExtCommunityAclNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 104, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(2000, 2999), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cSnmpExtCommunityAclNum.setStatus('current')
mibBuilder.exportSymbols("H3C-SNMP-EXT-MIB", h3cSnmpExtReadCommunitySingle=h3cSnmpExtReadCommunitySingle, h3cSnmpExtCommunitySecurityLevel=h3cSnmpExtCommunitySecurityLevel, h3cSnmpExtScalarObjects=h3cSnmpExtScalarObjects, h3cSnmpExtCommunityTable=h3cSnmpExtCommunityTable, h3cSnmpExtTables=h3cSnmpExtTables, h3cSnmpExtCommunityEntry=h3cSnmpExtCommunityEntry, h3cSnmpExt=h3cSnmpExt, h3cSnmpExtWriteCommunitySingle=h3cSnmpExtWriteCommunitySingle, h3cSnmpExtSnmpChannel=h3cSnmpExtSnmpChannel, h3cSnmpExtCommunityAclNum=h3cSnmpExtCommunityAclNum, h3cSnmpExtNotifications=h3cSnmpExtNotifications, h3cSnmpExtCommunityName=h3cSnmpExtCommunityName, PYSNMP_MODULE_ID=h3cSnmpExt, h3cSnmpExtCommunitySecurityName=h3cSnmpExtCommunitySecurityName)
