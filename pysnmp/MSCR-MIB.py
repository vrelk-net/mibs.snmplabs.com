#
# PySNMP MIB module MSCR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MSCR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:05:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, iso, ModuleIdentity, Bits, Integer32, Unsigned32, TimeTicks, NotificationType, ObjectIdentity, MibIdentifier, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Gauge32, Counter64, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "ModuleIdentity", "Bits", "Integer32", "Unsigned32", "TimeTicks", "NotificationType", "ObjectIdentity", "MibIdentifier", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Gauge32", "Counter64", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

nbase = MibIdentifier((1, 3, 6, 1, 4, 1, 629))
nbSwitchG1 = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1))
nbSwitchG1Il = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50))
nbMacScr = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50, 1))
nbMacScrRun = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 1))
nbMacScrPerm = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 2))
nbMacScrRunSecurityLevel = MibScalar((1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("perPort", 2), ("perSwitch", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbMacScrRunSecurityLevel.setStatus('mandatory')
nbMacScrRunSaveMS = MibScalar((1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("manual", 1), ("save", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbMacScrRunSaveMS.setStatus('mandatory')
nbMacScrRunClearMS = MibScalar((1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("running", 1), ("clear", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbMacScrRunClearMS.setStatus('mandatory')
nbMacScrRunPortsTable = MibTable((1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 1, 4), )
if mibBuilder.loadTexts: nbMacScrRunPortsTable.setStatus('mandatory')
nbMacScrRunPortsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 1, 4, 1), ).setIndexNames((0, "MSCR-MIB", "nbMacScrRunPort"))
if mibBuilder.loadTexts: nbMacScrRunPortsEntry.setStatus('mandatory')
nbMacScrRunPort = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 1, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbMacScrRunPort.setStatus('mandatory')
nbMacScrRunPortScrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbMacScrRunPortScrStatus.setStatus('mandatory')
nbMacScrRunPortSaveMS = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("manual", 1), ("save", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbMacScrRunPortSaveMS.setStatus('mandatory')
nbMacScrRunPortClearMS = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("running", 1), ("clear", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbMacScrRunPortClearMS.setStatus('mandatory')
nbMacScrRunPortLockingMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 1, 4, 1, 5), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbMacScrRunPortLockingMAC.setStatus('mandatory')
nbMacScrRunMsTable = MibTable((1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 1, 5), )
if mibBuilder.loadTexts: nbMacScrRunMsTable.setStatus('mandatory')
nbMacScrRunMsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 1, 5, 1), ).setIndexNames((0, "MSCR-MIB", "nbMacScrRunMsIndex"))
if mibBuilder.loadTexts: nbMacScrRunMsEntry.setStatus('mandatory')
nbMacScrRunMsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 1, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbMacScrRunMsIndex.setStatus('mandatory')
nbMacScrRunMsAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 1, 5, 1, 2), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbMacScrRunMsAddress.setStatus('mandatory')
nbMacScrRunMsPort = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbMacScrRunMsPort.setStatus('mandatory')
nbMacScrRunMsState = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbMacScrRunMsState.setStatus('mandatory')
nbMacScrRunMsMaxNum = MibScalar((1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbMacScrRunMsMaxNum.setStatus('mandatory')
nbMacScrRunTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbMacScrRunTableSize.setStatus('mandatory')
nbMacScrPermSecurityLevel = MibScalar((1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("perPort", 2), ("perSwitch", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbMacScrPermSecurityLevel.setStatus('mandatory')
nbMacScrPermSaveMS = MibScalar((1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("manual", 1), ("save", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbMacScrPermSaveMS.setStatus('mandatory')
nbMacScrPermClearMS = MibScalar((1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("running", 1), ("clear", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbMacScrPermClearMS.setStatus('mandatory')
nbMacScrPermPortsTable = MibTable((1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 2, 4), )
if mibBuilder.loadTexts: nbMacScrPermPortsTable.setStatus('mandatory')
nbMacScrPermPortsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 2, 4, 1), ).setIndexNames((0, "MSCR-MIB", "nbMacScrPermPort"))
if mibBuilder.loadTexts: nbMacScrPermPortsEntry.setStatus('mandatory')
nbMacScrPermPort = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 2, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbMacScrPermPort.setStatus('mandatory')
nbMacScrPermPortScrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbMacScrPermPortScrStatus.setStatus('mandatory')
nbMacScrPermPortSaveMS = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("manual", 1), ("save", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbMacScrPermPortSaveMS.setStatus('mandatory')
nbMacScrPermPortClearMS = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 2, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("running", 1), ("clear", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbMacScrPermPortClearMS.setStatus('mandatory')
nbMacScrPermMsTable = MibTable((1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 2, 5), )
if mibBuilder.loadTexts: nbMacScrPermMsTable.setStatus('mandatory')
nbMacScrPermMsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 2, 5, 1), ).setIndexNames((0, "MSCR-MIB", "nbMacScrPermMsIndex"))
if mibBuilder.loadTexts: nbMacScrPermMsEntry.setStatus('mandatory')
nbMacScrPermMsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 2, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbMacScrPermMsIndex.setStatus('mandatory')
nbMacScrPermMsAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 2, 5, 1, 2), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbMacScrPermMsAddress.setStatus('mandatory')
nbMacScrPermMsPort = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 2, 5, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbMacScrPermMsPort.setStatus('mandatory')
nbMacScrPermMsState = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 2, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbMacScrPermMsState.setStatus('mandatory')
nbMacScrPermMsMaxNum = MibScalar((1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 2, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbMacScrPermMsMaxNum.setStatus('mandatory')
nbMacScrPermTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 2, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbMacScrPermTableSize.setStatus('mandatory')
nbMacScrPermLoadMS = MibScalar((1, 3, 6, 1, 4, 1, 629, 1, 50, 1, 2, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("manual", 1), ("load", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbMacScrPermLoadMS.setStatus('mandatory')
unresolvedMAC = NotificationType((1, 3, 6, 1, 4, 1, 629, 1, 50, 1) + (0,1)).setObjects(("MSCR-MIB", "nbMacScrRunPort"), ("MSCR-MIB", "nbMacScrRunPortLockingMAC"))
mibBuilder.exportSymbols("MSCR-MIB", nbMacScrRunMsState=nbMacScrRunMsState, nbMacScrRunMsIndex=nbMacScrRunMsIndex, nbMacScrRunSecurityLevel=nbMacScrRunSecurityLevel, nbMacScrPermMsTable=nbMacScrPermMsTable, nbase=nbase, nbMacScrPermSecurityLevel=nbMacScrPermSecurityLevel, nbMacScrRun=nbMacScrRun, nbMacScrRunSaveMS=nbMacScrRunSaveMS, nbMacScrRunMsPort=nbMacScrRunMsPort, nbMacScrPermPort=nbMacScrPermPort, nbSwitchG1Il=nbSwitchG1Il, nbMacScrRunPortsTable=nbMacScrRunPortsTable, nbMacScrPermMsEntry=nbMacScrPermMsEntry, nbMacScrRunMsEntry=nbMacScrRunMsEntry, nbMacScr=nbMacScr, nbMacScrPermMsIndex=nbMacScrPermMsIndex, nbMacScrRunClearMS=nbMacScrRunClearMS, nbMacScrPerm=nbMacScrPerm, nbMacScrRunMsTable=nbMacScrRunMsTable, nbMacScrRunPortLockingMAC=nbMacScrRunPortLockingMAC, nbMacScrPermMsMaxNum=nbMacScrPermMsMaxNum, nbMacScrPermMsAddress=nbMacScrPermMsAddress, nbMacScrPermLoadMS=nbMacScrPermLoadMS, nbMacScrPermPortSaveMS=nbMacScrPermPortSaveMS, nbMacScrRunMsMaxNum=nbMacScrRunMsMaxNum, unresolvedMAC=unresolvedMAC, nbMacScrRunPortsEntry=nbMacScrRunPortsEntry, nbMacScrRunPortClearMS=nbMacScrRunPortClearMS, nbMacScrPermPortsEntry=nbMacScrPermPortsEntry, nbMacScrPermMsPort=nbMacScrPermMsPort, nbMacScrPermMsState=nbMacScrPermMsState, nbMacScrPermPortClearMS=nbMacScrPermPortClearMS, nbSwitchG1=nbSwitchG1, MacAddress=MacAddress, nbMacScrRunTableSize=nbMacScrRunTableSize, nbMacScrRunMsAddress=nbMacScrRunMsAddress, nbMacScrPermTableSize=nbMacScrPermTableSize, nbMacScrRunPort=nbMacScrRunPort, nbMacScrPermSaveMS=nbMacScrPermSaveMS, nbMacScrRunPortScrStatus=nbMacScrRunPortScrStatus, nbMacScrPermClearMS=nbMacScrPermClearMS, nbMacScrPermPortsTable=nbMacScrPermPortsTable, nbMacScrPermPortScrStatus=nbMacScrPermPortScrStatus, nbMacScrRunPortSaveMS=nbMacScrRunPortSaveMS)
