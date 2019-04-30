#
# PySNMP MIB module HP-ICF-IPV6-RA-GUARD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-IPV6-RA-GUARD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:21:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Integer32, TimeTicks, Bits, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity, Counter64, Counter32, Gauge32, Unsigned32, iso, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "Bits", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity", "Counter64", "Counter32", "Gauge32", "Unsigned32", "iso", "IpAddress")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
hpicfIpv6RAGuard = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87))
hpicfIpv6RAGuard.setRevisions(('2011-03-16 05:24',))
if mibBuilder.loadTexts: hpicfIpv6RAGuard.setLastUpdated('201103160524Z')
if mibBuilder.loadTexts: hpicfIpv6RAGuard.setOrganization('Hewlett-Packard Company HP Networking')
hpicfIpv6RAGuardObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 1))
hpicfIpv6RAGuardConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 1, 1))
hpicfRAGuardPortTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 1, 1, 1), )
if mibBuilder.loadTexts: hpicfRAGuardPortTable.setStatus('current')
hpicfRAGuardPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpicfRAGuardPortEntry.setStatus('current')
hpicfRAGuardPortBlocked = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 1, 1, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfRAGuardPortBlocked.setStatus('current')
hpicfRAGuardPortBlockedRAs = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 1, 1, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfRAGuardPortBlockedRAs.setStatus('current')
hpicfRAGuardPortBlockedRedirs = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 1, 1, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfRAGuardPortBlockedRedirs.setStatus('current')
hpicfRAGuardPortLog = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 1, 1, 1, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfRAGuardPortLog.setStatus('current')
hpicfRAGuardLastErrorCode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noError", 1), ("insufficientHardwareResources", 2), ("genericError", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfRAGuardLastErrorCode.setStatus('current')
hpicfIpv6RAGuardConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 2))
hpicfIpv6RAGuardCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 2, 1))
hpicfIpv6RAGuardGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 2, 2))
hpicfIpv6RAGuardGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 2, 2, 1)).setObjects(("HP-ICF-IPV6-RA-GUARD-MIB", "hpicfRAGuardPortBlocked"), ("HP-ICF-IPV6-RA-GUARD-MIB", "hpicfRAGuardPortBlockedRAs"), ("HP-ICF-IPV6-RA-GUARD-MIB", "hpicfRAGuardPortBlockedRedirs"), ("HP-ICF-IPV6-RA-GUARD-MIB", "hpicfRAGuardPortLog"), ("HP-ICF-IPV6-RA-GUARD-MIB", "hpicfRAGuardLastErrorCode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfIpv6RAGuardGroup = hpicfIpv6RAGuardGroup.setStatus('current')
hpicfIpv6RAGuardCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87, 2, 1, 1)).setObjects(("HP-ICF-IPV6-RA-GUARD-MIB", "hpicfIpv6RAGuardGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfIpv6RAGuardCompliance = hpicfIpv6RAGuardCompliance.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-IPV6-RA-GUARD-MIB", hpicfIpv6RAGuardCompliance=hpicfIpv6RAGuardCompliance, hpicfRAGuardPortBlockedRAs=hpicfRAGuardPortBlockedRAs, hpicfRAGuardPortTable=hpicfRAGuardPortTable, hpicfRAGuardPortLog=hpicfRAGuardPortLog, hpicfRAGuardLastErrorCode=hpicfRAGuardLastErrorCode, hpicfIpv6RAGuardConfig=hpicfIpv6RAGuardConfig, hpicfIpv6RAGuardObjects=hpicfIpv6RAGuardObjects, hpicfIpv6RAGuardCompliances=hpicfIpv6RAGuardCompliances, PYSNMP_MODULE_ID=hpicfIpv6RAGuard, hpicfRAGuardPortEntry=hpicfRAGuardPortEntry, hpicfRAGuardPortBlocked=hpicfRAGuardPortBlocked, hpicfIpv6RAGuard=hpicfIpv6RAGuard, hpicfRAGuardPortBlockedRedirs=hpicfRAGuardPortBlockedRedirs, hpicfIpv6RAGuardConformance=hpicfIpv6RAGuardConformance, hpicfIpv6RAGuardGroup=hpicfIpv6RAGuardGroup, hpicfIpv6RAGuardGroups=hpicfIpv6RAGuardGroups)
