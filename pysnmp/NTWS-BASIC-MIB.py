#
# PySNMP MIB module NTWS-BASIC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NTWS-BASIC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:16:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NtwsLicenseFeature, = mibBuilder.importSymbols("NTWS-LICENSE-FEATURE-TC-MIB", "NtwsLicenseFeature")
ntwsMibs, = mibBuilder.importSymbols("NTWS-ROOT-MIB", "ntwsMibs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Unsigned32, Gauge32, MibIdentifier, Counter32, NotificationType, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, Bits, Integer32, iso, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "Gauge32", "MibIdentifier", "Counter32", "NotificationType", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "Bits", "Integer32", "iso", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ntwsBasic = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 2))
ntwsBasic.setRevisions(('2009-11-16 00:10', '2007-08-16 00:09', '2006-07-10 00:08', '2006-04-14 00:07', '2005-01-01 00:00',))
if mibBuilder.loadTexts: ntwsBasic.setLastUpdated('200911160010Z')
if mibBuilder.loadTexts: ntwsBasic.setOrganization('Nortel Networks')
ntwsBasicSystemInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 2, 1))
ntwsSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsSerialNumber.setStatus('current')
ntwsSwMajorVersionNumber = MibScalar((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsSwMajorVersionNumber.setStatus('current')
ntwsSwMinorVersionNumber = MibScalar((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsSwMinorVersionNumber.setStatus('current')
ntwsVersionString = MibScalar((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsVersionString.setStatus('current')
ntwsMobilityDomainInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 2, 2))
ntwsMobilityDomainName = MibScalar((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 2, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsMobilityDomainName.setStatus('current')
ntwsMobilitySeedIp = MibScalar((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 2, 2, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsMobilitySeedIp.setStatus('current')
ntwsMobilityMemberTableSize = MibScalar((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 2, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsMobilityMemberTableSize.setStatus('current')
ntwsMobilityMemberTable = MibTable((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 2, 2, 4), )
if mibBuilder.loadTexts: ntwsMobilityMemberTable.setStatus('current')
ntwsMobilityMemberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 2, 2, 4, 1), ).setIndexNames((0, "NTWS-BASIC-MIB", "ntwsMobilityMemberEntryAddr"))
if mibBuilder.loadTexts: ntwsMobilityMemberEntry.setStatus('current')
ntwsMobilityMemberEntryAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 2, 2, 4, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsMobilityMemberEntryAddr.setStatus('current')
ntwsLicenseInfoGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 2, 3))
ntwsLicenseInfoTableSize = MibScalar((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 2, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsLicenseInfoTableSize.setStatus('current')
ntwsLicenseInfoTable = MibTable((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 2, 3, 2), )
if mibBuilder.loadTexts: ntwsLicenseInfoTable.setStatus('current')
ntwsLicenseInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 2, 3, 2, 1), ).setIndexNames((0, "NTWS-BASIC-MIB", "ntwsLicenseInfoEntryFeature"))
if mibBuilder.loadTexts: ntwsLicenseInfoEntry.setStatus('current')
ntwsLicenseInfoEntryFeature = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 2, 3, 2, 1, 1), NtwsLicenseFeature())
if mibBuilder.loadTexts: ntwsLicenseInfoEntryFeature.setStatus('current')
ntwsLicenseInfoEntryValue = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 2, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4096))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsLicenseInfoEntryValue.setStatus('current')
ntwsLicenseInfoEntryDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 2, 3, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsLicenseInfoEntryDescr.setStatus('current')
mibBuilder.exportSymbols("NTWS-BASIC-MIB", ntwsVersionString=ntwsVersionString, ntwsMobilityMemberEntryAddr=ntwsMobilityMemberEntryAddr, ntwsBasicSystemInfo=ntwsBasicSystemInfo, ntwsLicenseInfoEntry=ntwsLicenseInfoEntry, ntwsLicenseInfoEntryValue=ntwsLicenseInfoEntryValue, ntwsLicenseInfoTable=ntwsLicenseInfoTable, ntwsSwMajorVersionNumber=ntwsSwMajorVersionNumber, ntwsMobilityMemberTableSize=ntwsMobilityMemberTableSize, ntwsLicenseInfoEntryDescr=ntwsLicenseInfoEntryDescr, ntwsLicenseInfoTableSize=ntwsLicenseInfoTableSize, ntwsLicenseInfoGroup=ntwsLicenseInfoGroup, ntwsBasic=ntwsBasic, ntwsSerialNumber=ntwsSerialNumber, ntwsLicenseInfoEntryFeature=ntwsLicenseInfoEntryFeature, ntwsMobilityMemberEntry=ntwsMobilityMemberEntry, ntwsMobilitySeedIp=ntwsMobilitySeedIp, PYSNMP_MODULE_ID=ntwsBasic, ntwsSwMinorVersionNumber=ntwsSwMinorVersionNumber, ntwsMobilityDomainName=ntwsMobilityDomainName, ntwsMobilityMemberTable=ntwsMobilityMemberTable, ntwsMobilityDomainInfo=ntwsMobilityDomainInfo)
