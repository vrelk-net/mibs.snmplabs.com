#
# PySNMP MIB module G6-FACTORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/G6-FACTORY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:04:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
g6, = mibBuilder.importSymbols("MICROSENS-G6-MIB", "g6")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Bits, Counter32, NotificationType, Counter64, ObjectIdentity, TimeTicks, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, IpAddress, MibIdentifier, enterprises, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "Counter32", "NotificationType", "Counter64", "ObjectIdentity", "TimeTicks", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "IpAddress", "MibIdentifier", "enterprises", "ModuleIdentity")
DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention")
device = ModuleIdentity((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1))
device.setRevisions(('2015-05-22 10:59',))
if mibBuilder.loadTexts: device.setLastUpdated('201505221059Z')
if mibBuilder.loadTexts: device.setOrganization('MICROSENS GmbH & Co. KG')
factory = MibIdentifier((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 32))
factoryArticleNumber = MibScalar((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 32, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: factoryArticleNumber.setStatus('current')
factorySerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 32, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: factorySerialNumber.setStatus('current')
factoryDeviceMac = MibScalar((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 32, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: factoryDeviceMac.setStatus('current')
factoryNumberOfMacs = MibScalar((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 32, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: factoryNumberOfMacs.setStatus('current')
factoryHardwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 32, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: factoryHardwareVersion.setStatus('current')
factoryBoardId = MibScalar((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 32, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: factoryBoardId.setStatus('current')
factoryProjectNumber = MibScalar((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 32, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: factoryProjectNumber.setStatus('current')
factoryMechanicalFeatures = MibScalar((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 32, 8), Bits().clone(namedValues=NamedValues(("desktop", 0), ("rail", 1), ("ductVertical", 2), ("ductHorizontal", 3), ("rack", 4), ("stackable", 5), ("unused6", 6), ("unused7", 7), ("dc", 8), ("ac", 9), ("dualPwr", 10), ("unused11", 11), ("extTemp", 12), ("extSupply", 13), ("exSecure", 14), ("unused15", 15), ("unused16", 16), ("microSd", 17), ("sdcard", 18), ("internalMemory", 19), ("unused20", 20), ("unused21", 21), ("ip30", 22), ("ip42", 23), ("ip44", 24), ("ip55", 25), ("ip67", 26), ("unused27", 27), ("unused28", 28), ("unused29", 29), ("unused30", 30), ("unused31", 31)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: factoryMechanicalFeatures.setStatus('current')
factoryHardwareFeatures = MibScalar((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 32, 9), Bits().clone(namedValues=NamedValues(("poePlus", 0), ("poePse", 1), ("poePd", 2), ("unused3", 3), ("unused4", 4), ("unused5", 5), ("eee", 6), ("synce", 7), ("ms1588", 8), ("usb", 9), ("relays", 10), ("rtc", 11), ("unused12", 12), ("unused13", 13), ("unused14", 14), ("csfp", 15), ("sfp", 16), ("lc", 17), ("sc", 18), ("st", 19), ("e2000", 20), ("unused21", 21), ("unused22", 22), ("unused23", 23), ("unused24", 24), ("unused25", 25), ("unused26", 26), ("unused27", 27), ("unused28", 28), ("unused29", 29), ("unused30", 30), ("unused31", 31)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: factoryHardwareFeatures.setStatus('current')
factoryCompanyName = MibScalar((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 32, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: factoryCompanyName.setStatus('current')
factoryCompanyShort = MibScalar((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 32, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: factoryCompanyShort.setStatus('current')
factoryWebLink = MibScalar((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 32, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: factoryWebLink.setStatus('current')
factoryWebDescription = MibScalar((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 32, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: factoryWebDescription.setStatus('current')
factoryCustomInfo = MibScalar((1, 3, 6, 1, 4, 1, 3181, 10, 6, 1, 32, 14), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: factoryCustomInfo.setStatus('current')
mibBuilder.exportSymbols("G6-FACTORY-MIB", factoryWebLink=factoryWebLink, factoryCompanyName=factoryCompanyName, device=device, factoryWebDescription=factoryWebDescription, factoryArticleNumber=factoryArticleNumber, factoryProjectNumber=factoryProjectNumber, factoryBoardId=factoryBoardId, factoryMechanicalFeatures=factoryMechanicalFeatures, factoryCustomInfo=factoryCustomInfo, factoryHardwareVersion=factoryHardwareVersion, factoryNumberOfMacs=factoryNumberOfMacs, factoryCompanyShort=factoryCompanyShort, factoryHardwareFeatures=factoryHardwareFeatures, factoryDeviceMac=factoryDeviceMac, factorySerialNumber=factorySerialNumber, factory=factory, PYSNMP_MODULE_ID=device)