#
# PySNMP MIB module CISCO-DMN-DSG-ABOUT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DMN-DSG-ABOUT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:37:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter32, ObjectIdentity, Counter64, Gauge32, NotificationType, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32, ModuleIdentity, Integer32, Bits, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "Counter64", "Gauge32", "NotificationType", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32", "ModuleIdentity", "Integer32", "Bits", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDSGAbout = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7))
ciscoDSGAbout.setRevisions(('2010-08-03 06:00', '2010-03-22 05:00', '2009-12-20 15:00',))
if mibBuilder.loadTexts: ciscoDSGAbout.setLastUpdated('201008030600Z')
if mibBuilder.loadTexts: ciscoDSGAbout.setOrganization('Cisco Systems, Inc.')
aboutTable = MibIdentifier((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2))
boardTable = MibTable((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 1), )
if mibBuilder.loadTexts: boardTable.setStatus('current')
boardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 1, 1), ).setIndexNames((0, "CISCO-DMN-DSG-ABOUT-MIB", "boardIdx"))
if mibBuilder.loadTexts: boardEntry.setStatus('current')
boardIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: boardIdx.setStatus('current')
boardPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardPosition.setStatus('current')
boardID = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 49))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardID.setStatus('current')
boardRev = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 49))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardRev.setStatus('current')
boardOptionBits = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardOptionBits.setStatus('current')
boardSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 49))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardSerialNum.setStatus('current')
swTable = MibTable((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 3), )
if mibBuilder.loadTexts: swTable.setStatus('current')
swEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 3, 1), ).setIndexNames((0, "CISCO-DMN-DSG-ABOUT-MIB", "swIdx"))
if mibBuilder.loadTexts: swEntry.setStatus('current')
swIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: swIdx.setStatus('current')
swBoardIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swBoardIdx.setStatus('current')
swID = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swID.setStatus('current')
swFileIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swFileIdx.setStatus('current')
swVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 3, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 35))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swVersion.setStatus('current')
swValidationCode = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 3, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 35))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swValidationCode.setStatus('current')
swStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("running", 1), ("ready", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swStatus.setStatus('current')
swCtrl = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("select", 2), ("erase", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swCtrl.setStatus('current')
firmwareTable = MibTable((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 4), )
if mibBuilder.loadTexts: firmwareTable.setStatus('current')
firmwareEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 4, 1), ).setIndexNames((0, "CISCO-DMN-DSG-ABOUT-MIB", "firmwareIdx"))
if mibBuilder.loadTexts: firmwareEntry.setStatus('current')
firmwareIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: firmwareIdx.setStatus('current')
firmwareBoardID = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: firmwareBoardID.setStatus('current')
firmwareID = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 4, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: firmwareID.setStatus('current')
firmwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 4, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 49))).setMaxAccess("readonly")
if mibBuilder.loadTexts: firmwareVersion.setStatus('current')
firmwareValidationCode = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 7, 2, 4, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 49))).setMaxAccess("readonly")
if mibBuilder.loadTexts: firmwareValidationCode.setStatus('current')
mibBuilder.exportSymbols("CISCO-DMN-DSG-ABOUT-MIB", swEntry=swEntry, boardTable=boardTable, boardIdx=boardIdx, boardPosition=boardPosition, firmwareIdx=firmwareIdx, swBoardIdx=swBoardIdx, PYSNMP_MODULE_ID=ciscoDSGAbout, firmwareValidationCode=firmwareValidationCode, swFileIdx=swFileIdx, ciscoDSGAbout=ciscoDSGAbout, swID=swID, boardRev=boardRev, swVersion=swVersion, boardOptionBits=boardOptionBits, firmwareID=firmwareID, boardID=boardID, swTable=swTable, aboutTable=aboutTable, swStatus=swStatus, swCtrl=swCtrl, firmwareEntry=firmwareEntry, firmwareTable=firmwareTable, firmwareVersion=firmwareVersion, swIdx=swIdx, boardSerialNum=boardSerialNum, swValidationCode=swValidationCode, firmwareBoardID=firmwareBoardID, boardEntry=boardEntry)