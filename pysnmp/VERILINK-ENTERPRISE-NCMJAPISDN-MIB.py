#
# PySNMP MIB module VERILINK-ENTERPRISE-NCMJAPISDN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VERILINK-ENTERPRISE-NCMJAPISDN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:26:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, NotificationType, Gauge32, ModuleIdentity, IpAddress, Counter64, MibIdentifier, Counter32, ObjectIdentity, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "NotificationType", "Gauge32", "ModuleIdentity", "IpAddress", "Counter64", "MibIdentifier", "Counter32", "ObjectIdentity", "Integer32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ncm_japisdn, = mibBuilder.importSymbols("VERILINK-ENTERPRISE-NCMALARM-MIB", "ncm-japisdn")
ncmJapPRIPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8000), )
if mibBuilder.loadTexts: ncmJapPRIPortConfigTable.setStatus('mandatory')
ncmJapPRIPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8000, 1), ).setIndexNames((0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRIPortNIDIndex"), (0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRIPortLineIndex"))
if mibBuilder.loadTexts: ncmJapPRIPortConfigEntry.setStatus('mandatory')
ncmJapPRIPortNIDIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8000, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRIPortNIDIndex.setStatus('mandatory')
ncmJapPRIPortLineIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8000, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRIPortLineIndex.setStatus('mandatory')
ncmJapPRIPortInService = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8000, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmJapPRIPortInService.setStatus('mandatory')
ncmJapPRIPortNFASMode = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8000, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("no-Nfas", 1), ("nfas-No-Backup", 2), ("nfas-Backup", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmJapPRIPortNFASMode.setStatus('mandatory')
ncmJapPRIPortDChanMode = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8000, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("inverted", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmJapPRIPortDChanMode.setStatus('mandatory')
ncmJapPRIPortDChanBits = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8000, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("chan-8-Bit", 1), ("chan-7-Bit", 2), ("chan-6-Bit", 3), ("undefined", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmJapPRIPortDChanBits.setStatus('mandatory')
ncmJapPRIPortTimeslotMap = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8000, 1, 7), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmJapPRIPortTimeslotMap.setStatus('mandatory')
ncmJapPRIPortSwitchType = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8000, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(15))).clone(namedValues=NamedValues(("sw-NTT", 15)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmJapPRIPortSwitchType.setStatus('mandatory')
ncmJapPRIPortOwnNumPlan = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8000, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("unkn-NumPlan", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmJapPRIPortOwnNumPlan.setStatus('mandatory')
ncmJapPRIPortOwnNumType = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8000, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("unkn-NumType", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmJapPRIPortOwnNumType.setStatus('mandatory')
ncmJapPRIPortSecurityLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8000, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("no-Checks", 1), ("own-Numbers", 2), ("ext-Numbers", 3), ("both-Numbers", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmJapPRIPortSecurityLevel.setStatus('mandatory')
ncmJapPRIPortConfigStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8000, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("configuration-OK", 1), ("configuration-Error", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRIPortConfigStatus.setStatus('mandatory')
ncmJapPRIPortSetConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8000, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("set-Config", 1), ("not-in-use", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmJapPRIPortSetConfig.setStatus('mandatory')
ncmJapPRICallProfCallRefCount = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8000, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRICallProfCallRefCount.setStatus('mandatory')
ncmJapPRIL2AutoEstablish = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8000, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmJapPRIL2AutoEstablish.setStatus('mandatory')
ncmJapPRICallProfileTable = MibTable((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8001), )
if mibBuilder.loadTexts: ncmJapPRICallProfileTable.setStatus('mandatory')
ncmJapPRICallProfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8001, 1), ).setIndexNames((0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRICallProfNIDIndex"), (0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRICallProfLineIndex"), (0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRICPCallProfileRef"))
if mibBuilder.loadTexts: ncmJapPRICallProfEntry.setStatus('mandatory')
ncmJapPRICallProfNIDIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8001, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRICallProfNIDIndex.setStatus('mandatory')
ncmJapPRICallProfLineIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8001, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRICallProfLineIndex.setStatus('mandatory')
ncmJapPRICPCallProfileRef = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8001, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmJapPRICPCallProfileRef.setStatus('mandatory')
ncmJapPRICallProfCallDir = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8001, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("no-Direction", 1), ("incoming", 2), ("outgoing", 3), ("both-Directions", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmJapPRICallProfCallDir.setStatus('mandatory')
ncmJapPRICallProfNumOwnDigit = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8001, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmJapPRICallProfNumOwnDigit.setStatus('mandatory')
ncmJapPRICallProfOwnCallNum = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8001, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmJapPRICallProfOwnCallNum.setStatus('mandatory')
ncmJapPRICallProfExtNumPlan = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8001, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("unkn-NumPlan", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmJapPRICallProfExtNumPlan.setStatus('mandatory')
ncmJapPRICallProfExtNumType = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8001, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("unkn-NumType", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmJapPRICallProfExtNumType.setStatus('mandatory')
ncmJapPRICallProfExtNumDigit = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8001, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmJapPRICallProfExtNumDigit.setStatus('mandatory')
ncmJapPRICallProfExtCallNum = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8001, 1, 10), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmJapPRICallProfExtCallNum.setStatus('mandatory')
ncmJapPRICallProfTransferMode = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8001, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(8))).clone(namedValues=NamedValues(("unrestricted-digital", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmJapPRICallProfTransferMode.setStatus('mandatory')
ncmJapPRICallProfCallBandWth = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8001, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(16, 19, 21))).clone(namedValues=NamedValues(("b1-64K", 16), ("h0-6X64K", 19), ("h11-24X64K", 21)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmJapPRICallProfCallBandWth.setStatus('mandatory')
ncmJapPRICallProfMultiRateCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8001, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 4, 6, 8, 12, 23, 24, 30, 31))).clone(namedValues=NamedValues(("mR-2", 2), ("mR-4", 4), ("mR-6", 6), ("mR-8", 8), ("mR-12", 12), ("mR-23", 23), ("mR-24", 24), ("mR-30", 30), ("mR-31", 31)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmJapPRICallProfMultiRateCnt.setStatus('mandatory')
ncmJapPRICallProfRateAdaptn = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8001, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no-Adapt", 1), ("adapt-56K", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmJapPRICallProfRateAdaptn.setStatus('mandatory')
ncmJapPRICallProfTestCallIntvl = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8001, 1, 15), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmJapPRICallProfTestCallIntvl.setStatus('mandatory')
ncmJapPRICallProfCallStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8001, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("fail-Takedown-Idle", 1), ("successful-Setup", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRICallProfCallStatus.setStatus('mandatory')
ncmJapPRICallProfCallAction = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8001, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("setup-Call", 1), ("takedown-Call", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmJapPRICallProfCallAction.setStatus('mandatory')
ncmJapPRICPSetCallProf = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8001, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("set-CallProf", 1), ("not-in-use", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmJapPRICPSetCallProf.setStatus('mandatory')
ncmJapPRICPSetCallProfResp = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8001, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("configuration-OK", 1), ("configuration-Error", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRICPSetCallProfResp.setStatus('mandatory')
ncmJapPRICPCallActionResp = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8001, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("configuration-OK", 1), ("configuration-Error", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRICPCallActionResp.setStatus('mandatory')
ncmJapPRICallProfListTable = MibTable((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8002), )
if mibBuilder.loadTexts: ncmJapPRICallProfListTable.setStatus('mandatory')
ncmJapPRICallProfListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8002, 1), ).setIndexNames((0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRICPListNIDIndex"), (0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRICPListLineIndex"), (0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRICPListIndex"))
if mibBuilder.loadTexts: ncmJapPRICallProfListEntry.setStatus('mandatory')
ncmJapPRICPListNIDIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8002, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRICPListNIDIndex.setStatus('mandatory')
ncmJapPRICPListLineIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8002, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRICPListLineIndex.setStatus('mandatory')
ncmJapPRICPListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8002, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRICPListIndex.setStatus('mandatory')
ncmJapPRICPListValidCPRefNum = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8002, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRICPListValidCPRefNum.setStatus('mandatory')
ncmJapPRICurrentTable = MibTable((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003), )
if mibBuilder.loadTexts: ncmJapPRICurrentTable.setStatus('mandatory')
ncmJapPRICurrentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1), ).setIndexNames((0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRICurrNIDIndex"), (0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRICurrLineIndex"), (0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRICurrEndType"))
if mibBuilder.loadTexts: ncmJapPRICurrentEntry.setStatus('mandatory')
ncmJapPRICurrNIDIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRICurrNIDIndex.setStatus('mandatory')
ncmJapPRICurrLineIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRICurrLineIndex.setStatus('mandatory')
ncmJapPRICurrEndType = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("near-End", 1), ("far-End", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRICurrEndType.setStatus('mandatory')
ncmJapPRICurrTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRICurrTimestamp.setStatus('mandatory')
ncmJapPRICurrSecsInCurrIntvl = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRICurrSecsInCurrIntvl.setStatus('mandatory')
ncmJapPRICurrInfoRx = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRICurrInfoRx.setStatus('mandatory')
ncmJapPRICurrInfoTx = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRICurrInfoTx.setStatus('mandatory')
ncmJapPRICurrCRCErrRx = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRICurrCRCErrRx.setStatus('mandatory')
ncmJapPRICurrInvalidFrameRx = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRICurrInvalidFrameRx.setStatus('mandatory')
ncmJapPRICurrFrameAbortRx = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRICurrFrameAbortRx.setStatus('mandatory')
ncmJapPRICurrDISCSRx = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRICurrDISCSRx.setStatus('mandatory')
ncmJapPRICurrDISCSTx = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRICurrDISCSTx.setStatus('mandatory')
ncmJapPRICurrFramerRx = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRICurrFramerRx.setStatus('mandatory')
ncmJapPRICurrFramerTx = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRICurrFramerTx.setStatus('mandatory')
ncmJapPRICurrLyr3ProtErr = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRICurrLyr3ProtErr.setStatus('mandatory')
ncmJapPRICurrCallSetupSent = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRICurrCallSetupSent.setStatus('mandatory')
ncmJapPRICurrCallSetupSentnFail = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRICurrCallSetupSentnFail.setStatus('mandatory')
ncmJapPRICurrCallSetupRx = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRICurrCallSetupRx.setStatus('mandatory')
ncmJapPRICurrCallSetupRxnFail = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRICurrCallSetupRxnFail.setStatus('mandatory')
ncmJapPRICurrUnSupportMsgRx = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRICurrUnSupportMsgRx.setStatus('mandatory')
ncmJapPRICurrTstCalSetupSentnFail = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRICurrTstCalSetupSentnFail.setStatus('mandatory')
ncmJapPRICurrValidIntvls = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRICurrValidIntvls.setStatus('mandatory')
ncmJapPRICurrStatisticReset = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8003, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("statistic-Reset", 1), ("not-in-use", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmJapPRICurrStatisticReset.setStatus('mandatory')
ncmJapPRIIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004), )
if mibBuilder.loadTexts: ncmJapPRIIntervalTable.setStatus('mandatory')
ncmJapPRIIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1), ).setIndexNames((0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRIntvlNIDIndex"), (0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRIntvlLineIndex"), (0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRIntvlEndType"), (0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRIntvlIndex"))
if mibBuilder.loadTexts: ncmJapPRIIntervalEntry.setStatus('mandatory')
ncmJapPRIntvlNIDIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRIntvlNIDIndex.setStatus('mandatory')
ncmJapPRIntvlLineIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRIntvlLineIndex.setStatus('mandatory')
ncmJapPRIntvlEndType = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("near-End", 1), ("far-End", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRIntvlEndType.setStatus('mandatory')
ncmJapPRIntvlIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRIntvlIndex.setStatus('mandatory')
ncmJapPRIntvlTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRIntvlTimestamp.setStatus('mandatory')
ncmJapPRIntvlSecsInCurrIntvl = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRIntvlSecsInCurrIntvl.setStatus('mandatory')
ncmJapPRIntvlInfoRx = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRIntvlInfoRx.setStatus('mandatory')
ncmJapPRIntvlInfoTx = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRIntvlInfoTx.setStatus('mandatory')
ncmJapPRIntvlCRCErrRx = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRIntvlCRCErrRx.setStatus('mandatory')
ncmJapPRIntvlInvalidFrameRx = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRIntvlInvalidFrameRx.setStatus('mandatory')
ncmJapPRIntvlFrameAbortRx = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRIntvlFrameAbortRx.setStatus('mandatory')
ncmJapPRIntvlDISCSRx = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRIntvlDISCSRx.setStatus('mandatory')
ncmJapPRIntvlDISCSTx = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRIntvlDISCSTx.setStatus('mandatory')
ncmJapPRIntvlFramerRx = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRIntvlFramerRx.setStatus('mandatory')
ncmJapPRIntvlFramerTx = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRIntvlFramerTx.setStatus('mandatory')
ncmJapPRIntvlLyr3ProtErr = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRIntvlLyr3ProtErr.setStatus('mandatory')
ncmJapPRIntvlCallSetupSent = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRIntvlCallSetupSent.setStatus('mandatory')
ncmJapPRIntvlCallSetupSentnFail = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRIntvlCallSetupSentnFail.setStatus('mandatory')
ncmJapPRIntvlCallSetupRx = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRIntvlCallSetupRx.setStatus('mandatory')
ncmJapPRIntvlCallSetupRxnFail = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRIntvlCallSetupRxnFail.setStatus('mandatory')
ncmJapPRIntvlUnSupportMsgRx = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRIntvlUnSupportMsgRx.setStatus('mandatory')
ncmJapPRIntvlTstCalSetupSentnFail = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8004, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRIntvlTstCalSetupSentnFail.setStatus('mandatory')
ncmJapPRISecurOperTable = MibTable((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8005), )
if mibBuilder.loadTexts: ncmJapPRISecurOperTable.setStatus('mandatory')
ncmJapPRISecurOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8005, 1), ).setIndexNames((0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRISecOpNIDIndex"), (0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRISecOpLineIndex"))
if mibBuilder.loadTexts: ncmJapPRISecurOperEntry.setStatus('mandatory')
ncmJapPRISecOpNIDIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8005, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRISecOpNIDIndex.setStatus('mandatory')
ncmJapPRISecOpLineIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8005, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRISecOpLineIndex.setStatus('mandatory')
ncmJapPRISecOpFirstNum = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8005, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 13, 25, 37, 49))).clone(namedValues=NamedValues(("zeroth", 1), ("twelfth", 13), ("twenty-Fourth", 25), ("thirty-Sixth", 37), ("fourty-Eighth", 49)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmJapPRISecOpFirstNum.setStatus('mandatory')
ncmJapPRISecOpListype = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8005, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("own-number", 1), ("remote-number", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmJapPRISecOpListype.setStatus('mandatory')
ncmJapPRISecOpCountNum = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8005, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRISecOpCountNum.setStatus('mandatory')
ncmJapPRISecOpClearElement = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8005, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmJapPRISecOpClearElement.setStatus('mandatory')
ncmJapPRISecOpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8005, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("configuration-OK", 1), ("configuration-Error", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRISecOpStatus.setStatus('mandatory')
ncmJapPRISecOpAction = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8005, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("clear-Security-List", 1), ("set-Security-List", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmJapPRISecOpAction.setStatus('mandatory')
ncmJapPRISecurNumbTable = MibTable((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8006), )
if mibBuilder.loadTexts: ncmJapPRISecurNumbTable.setStatus('mandatory')
ncmJapPRISecurNumbEntry = MibTableRow((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8006, 1), ).setIndexNames((0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRISecNumNIDIndex"), (0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRISecNumLineIndex"), (0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRISecNumIndex"))
if mibBuilder.loadTexts: ncmJapPRISecurNumbEntry.setStatus('mandatory')
ncmJapPRISecNumNIDIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8006, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRISecNumNIDIndex.setStatus('mandatory')
ncmJapPRISecNumLineIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8006, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRISecNumLineIndex.setStatus('mandatory')
ncmJapPRISecNumIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8006, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRISecNumIndex.setStatus('mandatory')
ncmJapPRISecNumCount = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8006, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmJapPRISecNumCount.setStatus('mandatory')
ncmJapPRISecNumNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8006, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ncmJapPRISecNumNumber.setStatus('mandatory')
ncmJapPRICallLogLineTable = MibTable((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8007), )
if mibBuilder.loadTexts: ncmJapPRICallLogLineTable.setStatus('mandatory')
ncmJapPRICallLogLineEntry = MibTableRow((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8007, 1), ).setIndexNames((0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRICaloglinNIDIndex"), (0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRICaloglinLineIndex"), (0, "VERILINK-ENTERPRISE-NCMJAPISDN-MIB", "ncmJapPRICaloglinLineNum"))
if mibBuilder.loadTexts: ncmJapPRICallLogLineEntry.setStatus('mandatory')
ncmJapPRICaloglinNIDIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8007, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRICaloglinNIDIndex.setStatus('mandatory')
ncmJapPRICaloglinLineIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8007, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRICaloglinLineIndex.setStatus('mandatory')
ncmJapPRICaloglinLineNum = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8007, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRICaloglinLineNum.setStatus('mandatory')
ncmJapPRICaloglinLogLine = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8007, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRICaloglinLogLine.setStatus('mandatory')
ncmJapPRICaloglinStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 1, 3038, 8007, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid-CallLogLine", 1), ("invalid-CallLogLine", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ncmJapPRICaloglinStatus.setStatus('mandatory')
mibBuilder.exportSymbols("VERILINK-ENTERPRISE-NCMJAPISDN-MIB", ncmJapPRISecOpStatus=ncmJapPRISecOpStatus, ncmJapPRIIntervalTable=ncmJapPRIIntervalTable, ncmJapPRIntvlUnSupportMsgRx=ncmJapPRIntvlUnSupportMsgRx, ncmJapPRIntvlLyr3ProtErr=ncmJapPRIntvlLyr3ProtErr, ncmJapPRIntvlFramerRx=ncmJapPRIntvlFramerRx, ncmJapPRIPortNIDIndex=ncmJapPRIPortNIDIndex, ncmJapPRICallProfLineIndex=ncmJapPRICallProfLineIndex, ncmJapPRISecOpAction=ncmJapPRISecOpAction, ncmJapPRICallProfExtCallNum=ncmJapPRICallProfExtCallNum, ncmJapPRICurrCallSetupSentnFail=ncmJapPRICurrCallSetupSentnFail, ncmJapPRIntvlSecsInCurrIntvl=ncmJapPRIntvlSecsInCurrIntvl, ncmJapPRISecOpLineIndex=ncmJapPRISecOpLineIndex, ncmJapPRIPortOwnNumPlan=ncmJapPRIPortOwnNumPlan, ncmJapPRICPCallProfileRef=ncmJapPRICPCallProfileRef, ncmJapPRICurrDISCSTx=ncmJapPRICurrDISCSTx, ncmJapPRICurrValidIntvls=ncmJapPRICurrValidIntvls, ncmJapPRICaloglinNIDIndex=ncmJapPRICaloglinNIDIndex, ncmJapPRIntvlDISCSRx=ncmJapPRIntvlDISCSRx, ncmJapPRICurrUnSupportMsgRx=ncmJapPRICurrUnSupportMsgRx, ncmJapPRIntvlCRCErrRx=ncmJapPRIntvlCRCErrRx, ncmJapPRIIntervalEntry=ncmJapPRIIntervalEntry, ncmJapPRICurrFramerRx=ncmJapPRICurrFramerRx, ncmJapPRIPortDChanBits=ncmJapPRIPortDChanBits, ncmJapPRICurrNIDIndex=ncmJapPRICurrNIDIndex, ncmJapPRISecurOperTable=ncmJapPRISecurOperTable, ncmJapPRIntvlLineIndex=ncmJapPRIntvlLineIndex, ncmJapPRIPortConfigTable=ncmJapPRIPortConfigTable, ncmJapPRIPortInService=ncmJapPRIPortInService, ncmJapPRIPortSetConfig=ncmJapPRIPortSetConfig, ncmJapPRIntvlCallSetupRxnFail=ncmJapPRIntvlCallSetupRxnFail, ncmJapPRIntvlInfoRx=ncmJapPRIntvlInfoRx, ncmJapPRISecNumCount=ncmJapPRISecNumCount, ncmJapPRISecOpFirstNum=ncmJapPRISecOpFirstNum, ncmJapPRISecNumNIDIndex=ncmJapPRISecNumNIDIndex, ncmJapPRISecOpClearElement=ncmJapPRISecOpClearElement, ncmJapPRIPortOwnNumType=ncmJapPRIPortOwnNumType, ncmJapPRICallProfNIDIndex=ncmJapPRICallProfNIDIndex, ncmJapPRIntvlInvalidFrameRx=ncmJapPRIntvlInvalidFrameRx, ncmJapPRIPortSecurityLevel=ncmJapPRIPortSecurityLevel, ncmJapPRICallProfCallBandWth=ncmJapPRICallProfCallBandWth, ncmJapPRICallProfCallAction=ncmJapPRICallProfCallAction, ncmJapPRICaloglinLineIndex=ncmJapPRICaloglinLineIndex, ncmJapPRICallProfTestCallIntvl=ncmJapPRICallProfTestCallIntvl, ncmJapPRICPSetCallProf=ncmJapPRICPSetCallProf, ncmJapPRISecurNumbEntry=ncmJapPRISecurNumbEntry, ncmJapPRICallLogLineEntry=ncmJapPRICallLogLineEntry, ncmJapPRIntvlTstCalSetupSentnFail=ncmJapPRIntvlTstCalSetupSentnFail, ncmJapPRISecOpListype=ncmJapPRISecOpListype, ncmJapPRICPListIndex=ncmJapPRICPListIndex, ncmJapPRISecOpNIDIndex=ncmJapPRISecOpNIDIndex, ncmJapPRICurrTstCalSetupSentnFail=ncmJapPRICurrTstCalSetupSentnFail, ncmJapPRICurrLyr3ProtErr=ncmJapPRICurrLyr3ProtErr, ncmJapPRISecOpCountNum=ncmJapPRISecOpCountNum, ncmJapPRIPortLineIndex=ncmJapPRIPortLineIndex, ncmJapPRISecNumIndex=ncmJapPRISecNumIndex, ncmJapPRICallProfRateAdaptn=ncmJapPRICallProfRateAdaptn, ncmJapPRICurrCallSetupRxnFail=ncmJapPRICurrCallSetupRxnFail, ncmJapPRICallProfExtNumPlan=ncmJapPRICallProfExtNumPlan, ncmJapPRICPSetCallProfResp=ncmJapPRICPSetCallProfResp, ncmJapPRICurrTimestamp=ncmJapPRICurrTimestamp, ncmJapPRIntvlCallSetupRx=ncmJapPRIntvlCallSetupRx, ncmJapPRICurrCRCErrRx=ncmJapPRICurrCRCErrRx, ncmJapPRIntvlCallSetupSentnFail=ncmJapPRIntvlCallSetupSentnFail, ncmJapPRICurrFramerTx=ncmJapPRICurrFramerTx, ncmJapPRICurrSecsInCurrIntvl=ncmJapPRICurrSecsInCurrIntvl, ncmJapPRIPortConfigEntry=ncmJapPRIPortConfigEntry, ncmJapPRICaloglinStatus=ncmJapPRICaloglinStatus, ncmJapPRICallProfExtNumDigit=ncmJapPRICallProfExtNumDigit, ncmJapPRIL2AutoEstablish=ncmJapPRIL2AutoEstablish, ncmJapPRIPortNFASMode=ncmJapPRIPortNFASMode, ncmJapPRICallProfCallRefCount=ncmJapPRICallProfCallRefCount, ncmJapPRICurrDISCSRx=ncmJapPRICurrDISCSRx, ncmJapPRICPListValidCPRefNum=ncmJapPRICPListValidCPRefNum, ncmJapPRICurrentTable=ncmJapPRICurrentTable, ncmJapPRICallProfListTable=ncmJapPRICallProfListTable, ncmJapPRICaloglinLineNum=ncmJapPRICaloglinLineNum, ncmJapPRICallProfListEntry=ncmJapPRICallProfListEntry, ncmJapPRISecNumNumber=ncmJapPRISecNumNumber, ncmJapPRICurrInfoTx=ncmJapPRICurrInfoTx, ncmJapPRICallProfTransferMode=ncmJapPRICallProfTransferMode, ncmJapPRICallProfileTable=ncmJapPRICallProfileTable, ncmJapPRICurrInvalidFrameRx=ncmJapPRICurrInvalidFrameRx, ncmJapPRICallProfNumOwnDigit=ncmJapPRICallProfNumOwnDigit, ncmJapPRIntvlFramerTx=ncmJapPRIntvlFramerTx, ncmJapPRIPortConfigStatus=ncmJapPRIPortConfigStatus, ncmJapPRIntvlIndex=ncmJapPRIntvlIndex, ncmJapPRICPCallActionResp=ncmJapPRICPCallActionResp, ncmJapPRIPortDChanMode=ncmJapPRIPortDChanMode, ncmJapPRICPListNIDIndex=ncmJapPRICPListNIDIndex, ncmJapPRICurrLineIndex=ncmJapPRICurrLineIndex, ncmJapPRIntvlTimestamp=ncmJapPRIntvlTimestamp, ncmJapPRIntvlNIDIndex=ncmJapPRIntvlNIDIndex, ncmJapPRIntvlDISCSTx=ncmJapPRIntvlDISCSTx, ncmJapPRIntvlInfoTx=ncmJapPRIntvlInfoTx, ncmJapPRISecurNumbTable=ncmJapPRISecurNumbTable, ncmJapPRICallProfOwnCallNum=ncmJapPRICallProfOwnCallNum, ncmJapPRICallProfEntry=ncmJapPRICallProfEntry, ncmJapPRICallProfExtNumType=ncmJapPRICallProfExtNumType, ncmJapPRISecurOperEntry=ncmJapPRISecurOperEntry, ncmJapPRIPortSwitchType=ncmJapPRIPortSwitchType, ncmJapPRICaloglinLogLine=ncmJapPRICaloglinLogLine, ncmJapPRICallLogLineTable=ncmJapPRICallLogLineTable, ncmJapPRICurrStatisticReset=ncmJapPRICurrStatisticReset, ncmJapPRICallProfCallStatus=ncmJapPRICallProfCallStatus, ncmJapPRIntvlEndType=ncmJapPRIntvlEndType, ncmJapPRICallProfCallDir=ncmJapPRICallProfCallDir, ncmJapPRICurrentEntry=ncmJapPRICurrentEntry, ncmJapPRICurrCallSetupSent=ncmJapPRICurrCallSetupSent, ncmJapPRISecNumLineIndex=ncmJapPRISecNumLineIndex, ncmJapPRICurrEndType=ncmJapPRICurrEndType, ncmJapPRIPortTimeslotMap=ncmJapPRIPortTimeslotMap, ncmJapPRIntvlFrameAbortRx=ncmJapPRIntvlFrameAbortRx, ncmJapPRICurrInfoRx=ncmJapPRICurrInfoRx, ncmJapPRICurrFrameAbortRx=ncmJapPRICurrFrameAbortRx, ncmJapPRICurrCallSetupRx=ncmJapPRICurrCallSetupRx, ncmJapPRICPListLineIndex=ncmJapPRICPListLineIndex, ncmJapPRIntvlCallSetupSent=ncmJapPRIntvlCallSetupSent, ncmJapPRICallProfMultiRateCnt=ncmJapPRICallProfMultiRateCnt)
