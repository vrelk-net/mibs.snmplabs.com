#
# PySNMP MIB module CISCO-DMN-DSG-DR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DMN-DSG-DR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:37:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
IpAddress, NotificationType, Integer32, Counter64, TimeTicks, MibIdentifier, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, iso, Bits, Gauge32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "NotificationType", "Integer32", "Counter64", "TimeTicks", "MibIdentifier", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "iso", "Bits", "Gauge32", "ModuleIdentity")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
ciscoDSGDR = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43))
ciscoDSGDR.setRevisions(('2014-08-30 08:00',))
if mibBuilder.loadTexts: ciscoDSGDR.setLastUpdated('201408300800Z')
if mibBuilder.loadTexts: ciscoDSGDR.setOrganization('Cisco Systems, Inc.')
drGlobalCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 1))
enable = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: enable.setStatus('current')
sigLockTime = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sigLockTime.setStatus('current')
sigLossTime = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 2160000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sigLossTime.setStatus('current')
verifyTimer = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: verifyTimer.setStatus('current')
profile = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("local", 1), ("uplink", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: profile.setStatus('current')
backupTransportTable = MibTable((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 2), )
if mibBuilder.loadTexts: backupTransportTable.setStatus('current')
backupTransportEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 2, 1), ).setIndexNames((0, "CISCO-DMN-DSG-DR-MIB", "backupTransportIndex"))
if mibBuilder.loadTexts: backupTransportEntry.setStatus('current')
backupTransportIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupTransportIndex.setStatus('current')
backupTransportSetIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupTransportSetIdx.setStatus('current')
backupTransportDvbsFec = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3, 4, 6, 7, 10))).clone(namedValues=NamedValues(("oneHalf", 1), ("twoThirds", 3), ("threeQuarters", 4), ("fiveSixths", 6), ("sevenEigths", 7), ("auto", 10)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupTransportDvbsFec.setStatus('current')
backupTransportEwFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("east", 1), ("west", 2), ("notApplicable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupTransportEwFlag.setStatus('current')
backupTransportFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupTransportFrequency.setStatus('current')
backupTransportRFInput = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("rf1", 1), ("rf2", 2), ("rf3", 3), ("rf4", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupTransportRFInput.setStatus('current')
backupTransportModSys = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("qpsk_dvb-s", 1), ("qpsk_dvb-S2", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupTransportModSys.setStatus('current')
backupTransportNetId = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupTransportNetId.setStatus('current')
backupTransportOrbitalPos = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupTransportOrbitalPos.setStatus('current')
backupTransportOrbpolarization = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupTransportOrbpolarization.setStatus('current')
backupTransportSymbRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10000, 450000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupTransportSymbRate.setStatus('current')
backupTransportRollOffFactor = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 25, 3))).clone(namedValues=NamedValues(("f35", 1), ("f25", 25), ("f20", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupTransportRollOffFactor.setStatus('current')
backupTransportRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2), ("delete", 3), ("add", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupTransportRowstatus.setStatus('current')
backupSetTable = MibTable((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 3), )
if mibBuilder.loadTexts: backupSetTable.setStatus('current')
backupSetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 3, 1), ).setIndexNames((0, "CISCO-DMN-DSG-DR-MIB", "backupSetPeid"), (0, "CISCO-DMN-DSG-DR-MIB", "backupSetRecid"))
if mibBuilder.loadTexts: backupSetEntry.setStatus('current')
backupSetPeid = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupSetPeid.setStatus('current')
backupSetRecid = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupSetRecid.setStatus('current')
backupSetCsiidx = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupSetCsiidx.setStatus('current')
backupSetBkpch = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupSetBkpch.setStatus('current')
backupSetBkpchDispText = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 3, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupSetBkpchDispText.setStatus('current')
backupSetRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 43, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupSetRowStatus.setStatus('current')
mibBuilder.exportSymbols("CISCO-DMN-DSG-DR-MIB", backupTransportSetIdx=backupTransportSetIdx, sigLockTime=sigLockTime, enable=enable, backupTransportDvbsFec=backupTransportDvbsFec, backupTransportModSys=backupTransportModSys, backupTransportRollOffFactor=backupTransportRollOffFactor, backupSetRecid=backupSetRecid, backupTransportOrbitalPos=backupTransportOrbitalPos, backupTransportRowstatus=backupTransportRowstatus, backupSetBkpch=backupSetBkpch, PYSNMP_MODULE_ID=ciscoDSGDR, backupTransportNetId=backupTransportNetId, sigLossTime=sigLossTime, backupTransportSymbRate=backupTransportSymbRate, backupTransportIndex=backupTransportIndex, backupTransportFrequency=backupTransportFrequency, backupSetTable=backupSetTable, backupTransportEntry=backupTransportEntry, backupTransportTable=backupTransportTable, backupSetBkpchDispText=backupSetBkpchDispText, backupSetRowStatus=backupSetRowStatus, ciscoDSGDR=ciscoDSGDR, backupTransportEwFlag=backupTransportEwFlag, verifyTimer=verifyTimer, backupSetPeid=backupSetPeid, backupTransportRFInput=backupTransportRFInput, drGlobalCfg=drGlobalCfg, backupSetEntry=backupSetEntry, backupTransportOrbpolarization=backupTransportOrbpolarization, backupSetCsiidx=backupSetCsiidx, profile=profile)