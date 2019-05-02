#
# PySNMP MIB module CROSSBEAM-SYSTEMS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CROSSBEAM-SYSTEMS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:47:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, TimeTicks, Integer32, Gauge32, Counter32, ModuleIdentity, ObjectIdentity, iso, Bits, Unsigned32, IpAddress, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "TimeTicks", "Integer32", "Gauge32", "Counter32", "ModuleIdentity", "ObjectIdentity", "iso", "Bits", "Unsigned32", "IpAddress", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
crossbeamSystems = MibIdentifier((1, 3, 6, 1, 4, 1, 6848))
cbsProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1))
cbsMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 2))
cbsMIBs = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 3))
cbsTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 4))
crossbeamSystemsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6848, 3, 1))
crossbeamSystemsMIB.setRevisions(('2003-05-09 00:00', '2002-03-15 00:00', '2004-03-10 00:00', '2004-05-10 00:00', '2004-07-07 00:00', '2005-08-22 00:00', '2005-10-25 00:00', '2006-02-07 00:00', '2010-04-14 00:00', '2010-06-17 00:00', '2010-08-10 00:00', '2010-08-11 00:00', '2010-10-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: crossbeamSystemsMIB.setRevisionsDescriptions(('Added new chassis and module types for X45 and X80', 'Initial Revision', 'Added Product Identifier for C10 Chassis Type', 'Added Product Identifier for C30i Chassis Type', 'Added Product Identifier for AP8400', 'Added Product Identifier for C2 and C6', 'Added Product Identifier for CP8400', 'Added Product Identifier for C12 and C25', 'Revise cbsCPM8650 to cbsCPM9600', 'Added new chassis type for X60', 'Added new chassis types for X20 and X30', 'Added new module type APM 9600', 'Added new module type APM 2030, NPM20 and NPM30',))
if mibBuilder.loadTexts: crossbeamSystemsMIB.setLastUpdated('200203150000Z')
if mibBuilder.loadTexts: crossbeamSystemsMIB.setOrganization('Crossbeam Systems, Inc.')
if mibBuilder.loadTexts: crossbeamSystemsMIB.setContactInfo('Email: mib-admin@crossbeamsys.com Postal: 80 Central Street Boxborough, MA 01719')
if mibBuilder.loadTexts: crossbeamSystemsMIB.setDescription('XOS, Release 9.5: This MIB module defines the objects used to identify the ProductIDs for Crossbeam Systems products.')
cbsX40 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1))
cbsXSeries = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 2))
cbsCSeries = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 3))
cbsXChassis = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 2, 1))
cbsX45Chassis = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 2, 1, 1))
cbsX80Chassis = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 2, 1, 2))
cbsX60Chassis = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 2, 1, 3))
cbsX20Chassis = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 2, 1, 4))
cbsX30Chassis = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 2, 1, 5))
cbsX40Chassis = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 1))
cbsCChassis = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 3, 1))
cbsC30Chassis = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 3, 1, 1))
cbsC10Chassis = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 3, 1, 2))
cbsC30iChassis = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 3, 1, 3))
cbsC2Chassis = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 3, 1, 4))
cbsC6Chassis = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 3, 1, 5))
cbsC12Chassis = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 3, 1, 6))
cbsC25Chassis = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 3, 1, 7))
cbsX40Modules = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2))
cbsCPModules = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 1))
cbsAPModules = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 2))
cbsNPModules = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 3))
cbsCPM4100 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 1, 1))
cbsCPM8100 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 1, 2))
cbsCPM8400 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 1, 3))
cbsCPM8600 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 1, 4))
cbsCPM9600 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 1, 5))
cbsAPM4100 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 2, 1))
cbsAPM4200 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 2, 2))
cbsAPM4250 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 2, 3))
cbsAPM8200 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 2, 4))
cbsAPM8400 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 2, 5))
cbsAPM8600 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 2, 6))
cbsAPM8650 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 2, 7))
cbsAPM9600 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 2, 8))
cbsAPM2030 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 2, 9))
cbsNPM4100 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 3, 1))
cbsNPM4110 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 3, 2))
cbsNPM8200 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 3, 3))
cbsNPM8210 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 3, 4))
cbsNPM8600 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 3, 5))
cbsNPM8650 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 3, 6))
cbsNPM30 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 3, 8))
cbsNPM8620 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 3, 7))
cbsNPM20 = MibIdentifier((1, 3, 6, 1, 4, 1, 6848, 1, 1, 2, 3, 9))
mibBuilder.exportSymbols("CROSSBEAM-SYSTEMS-MIB", cbsAPM8200=cbsAPM8200, cbsAPM8400=cbsAPM8400, cbsCPModules=cbsCPModules, cbsAPM4250=cbsAPM4250, cbsXChassis=cbsXChassis, cbsXSeries=cbsXSeries, cbsMgmt=cbsMgmt, PYSNMP_MODULE_ID=crossbeamSystemsMIB, cbsAPM8600=cbsAPM8600, cbsX40Chassis=cbsX40Chassis, cbsX40Modules=cbsX40Modules, cbsX20Chassis=cbsX20Chassis, cbsNPM4100=cbsNPM4100, crossbeamSystemsMIB=crossbeamSystemsMIB, cbsX40=cbsX40, crossbeamSystems=crossbeamSystems, cbsNPM8200=cbsNPM8200, cbsAPM2030=cbsAPM2030, cbsMIBs=cbsMIBs, cbsNPM8600=cbsNPM8600, cbsNPM8210=cbsNPM8210, cbsCSeries=cbsCSeries, cbsCPM9600=cbsCPM9600, cbsNPM8620=cbsNPM8620, cbsNPM20=cbsNPM20, cbsNPM8650=cbsNPM8650, cbsProducts=cbsProducts, cbsX30Chassis=cbsX30Chassis, cbsAPM4200=cbsAPM4200, cbsC10Chassis=cbsC10Chassis, cbsC30Chassis=cbsC30Chassis, cbsTraps=cbsTraps, cbsX60Chassis=cbsX60Chassis, cbsCPM8400=cbsCPM8400, cbsC6Chassis=cbsC6Chassis, cbsNPModules=cbsNPModules, cbsX45Chassis=cbsX45Chassis, cbsX80Chassis=cbsX80Chassis, cbsAPModules=cbsAPModules, cbsCPM8100=cbsCPM8100, cbsAPM4100=cbsAPM4100, cbsNPM30=cbsNPM30, cbsCPM4100=cbsCPM4100, cbsC12Chassis=cbsC12Chassis, cbsCChassis=cbsCChassis, cbsC30iChassis=cbsC30iChassis, cbsNPM4110=cbsNPM4110, cbsAPM8650=cbsAPM8650, cbsC25Chassis=cbsC25Chassis, cbsCPM8600=cbsCPM8600, cbsAPM9600=cbsAPM9600, cbsC2Chassis=cbsC2Chassis)