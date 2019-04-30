#
# PySNMP MIB module TPLINK-IP-SOURCE-GUARD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-IP-SOURCE-GUARD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:17:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, MibIdentifier, IpAddress, TimeTicks, Unsigned32, ModuleIdentity, Counter32, ObjectIdentity, Integer32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "IpAddress", "TimeTicks", "Unsigned32", "ModuleIdentity", "Counter32", "ObjectIdentity", "Integer32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
tplinkIpSourceGuardMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 29))
tplinkIpSourceGuardMIB.setRevisions(('2012-12-13 09:30',))
if mibBuilder.loadTexts: tplinkIpSourceGuardMIB.setLastUpdated('201212130930Z')
if mibBuilder.loadTexts: tplinkIpSourceGuardMIB.setOrganization('TPLINK')
tplinkIpSourceGuardMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 29, 1))
tplinkIpSourceGuardNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 29, 2))
tpIpSourceGuardConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 29, 1, 1))
tpIpSourceGuardConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 29, 1, 1, 1), )
if mibBuilder.loadTexts: tpIpSourceGuardConfigTable.setStatus('current')
tpIpSourceGuardConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 29, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tpIpSourceGuardConfigEntry.setStatus('current')
tpIpSourceGuardConfigPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 29, 1, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIpSourceGuardConfigPort.setStatus('current')
tpIpSourceGuardConfigType = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 29, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2))).clone(namedValues=NamedValues(("disable", 0), ("sip-mac", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpIpSourceGuardConfigType.setStatus('current')
tpIpSourceGuardConfigPortLag = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 29, 1, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIpSourceGuardConfigPortLag.setStatus('current')
mibBuilder.exportSymbols("TPLINK-IP-SOURCE-GUARD-MIB", tpIpSourceGuardConfigPort=tpIpSourceGuardConfigPort, tpIpSourceGuardConfigTable=tpIpSourceGuardConfigTable, PYSNMP_MODULE_ID=tplinkIpSourceGuardMIB, tpIpSourceGuardConfig=tpIpSourceGuardConfig, tpIpSourceGuardConfigType=tpIpSourceGuardConfigType, tplinkIpSourceGuardNotifications=tplinkIpSourceGuardNotifications, tpIpSourceGuardConfigEntry=tpIpSourceGuardConfigEntry, tplinkIpSourceGuardMIB=tplinkIpSourceGuardMIB, tplinkIpSourceGuardMIBObjects=tplinkIpSourceGuardMIBObjects, tpIpSourceGuardConfigPortLag=tpIpSourceGuardConfigPortLag)
