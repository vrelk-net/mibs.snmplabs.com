#
# PySNMP MIB module ASCEND-ADSL-DMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-ADSL-DMT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:25:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
wanTypeAdslDmt, = mibBuilder.importSymbols("ASCEND-WAN-MIB", "wanTypeAdslDmt")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, Unsigned32, ModuleIdentity, Counter64, ObjectIdentity, Bits, TimeTicks, Gauge32, Counter32, IpAddress, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "Unsigned32", "ModuleIdentity", "Counter64", "ObjectIdentity", "Bits", "TimeTicks", "Gauge32", "Counter32", "IpAddress", "MibIdentifier", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adslDmtLineStatusTable = MibTable((1, 3, 6, 1, 4, 1, 529, 4, 10, 1), )
if mibBuilder.loadTexts: adslDmtLineStatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: adslDmtLineStatusTable.setDescription('ADSL DMT status parameters.')
adslDmtLineStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 4, 10, 1, 1), ).setIndexNames((0, "ASCEND-ADSL-DMT-MIB", "adslDmtStatusIfEntryIndex"))
if mibBuilder.loadTexts: adslDmtLineStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: adslDmtLineStatusEntry.setDescription('An interface status entry containing objects to describe the interface.')
adslDmtStatusIfEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 10, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslDmtStatusIfEntryIndex.setStatus('mandatory')
if mibBuilder.loadTexts: adslDmtStatusIfEntryIndex.setDescription('Index into the Status Table via the interface group ifIndex value.')
adslDmtStatusShelfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 10, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslDmtStatusShelfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: adslDmtStatusShelfIndex.setDescription('ADSL DMT module Shelf ID.')
adslDmtStatusSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 10, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslDmtStatusSlotIndex.setStatus('mandatory')
if mibBuilder.loadTexts: adslDmtStatusSlotIndex.setDescription('ADSL DMT module Slot ID.')
adslDmtStatusLineIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 10, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslDmtStatusLineIndex.setStatus('mandatory')
if mibBuilder.loadTexts: adslDmtStatusLineIndex.setDescription('ADSL DMT module line ID.')
adslDmtStatusUnitType = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 10, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("coe", 1), ("cpe", 2), ("other", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslDmtStatusUnitType.setStatus('mandatory')
if mibBuilder.loadTexts: adslDmtStatusUnitType.setDescription('Unit type defines if the unit is operating either as a Central Office Equipment (COE) or Customer Premiss equipment (CPE).')
adslDmtStatusUpRate = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 10, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslDmtStatusUpRate.setStatus('mandatory')
if mibBuilder.loadTexts: adslDmtStatusUpRate.setDescription('Display the current upstream (cpe to coe) rate.')
adslDmtStatusDownRate = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 10, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslDmtStatusDownRate.setStatus('mandatory')
if mibBuilder.loadTexts: adslDmtStatusDownRate.setDescription('Displays the current downstream (coe to cpe) rate.')
adslDmtStatusVendorId = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 10, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslDmtStatusVendorId.setStatus('mandatory')
if mibBuilder.loadTexts: adslDmtStatusVendorId.setDescription('Vendor identification.')
adslDmtStatusFirmWareVer = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 10, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslDmtStatusFirmWareVer.setStatus('mandatory')
if mibBuilder.loadTexts: adslDmtStatusFirmWareVer.setDescription('Major firmware version.')
adslDmtStatusHardWareVer = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 10, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslDmtStatusHardWareVer.setStatus('mandatory')
if mibBuilder.loadTexts: adslDmtStatusHardWareVer.setDescription('Hardware version.')
adslDmtStatusTrellis = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 10, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("no", 1), ("yes", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslDmtStatusTrellis.setStatus('mandatory')
if mibBuilder.loadTexts: adslDmtStatusTrellis.setDescription('Report whether trellis coding is used.')
adslDmtStatusEoc = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 10, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("transaction", 2), ("streaming", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslDmtStatusEoc.setStatus('mandatory')
if mibBuilder.loadTexts: adslDmtStatusEoc.setDescription('Report whether the eoc can support autonomous data streaming mode or only transaction mode.')
adslAtucDMTPhysTable = MibTable((1, 3, 6, 1, 4, 1, 529, 4, 10, 2), )
if mibBuilder.loadTexts: adslAtucDMTPhysTable.setStatus('mandatory')
if mibBuilder.loadTexts: adslAtucDMTPhysTable.setDescription('ADSL DMT status parameters.')
adslAtucDMTPhysEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 4, 10, 2, 1), ).setIndexNames((0, "ASCEND-ADSL-DMT-MIB", "adslAtucDMTIfEntryIndex"))
if mibBuilder.loadTexts: adslAtucDMTPhysEntry.setStatus('mandatory')
if mibBuilder.loadTexts: adslAtucDMTPhysEntry.setDescription('An interface status entry containing objects to describe the interface.')
adslAtucDMTIfEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 10, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucDMTIfEntryIndex.setStatus('mandatory')
if mibBuilder.loadTexts: adslAtucDMTIfEntryIndex.setDescription('Index into the Status Table via the interface group ifIndex value.')
adslAtucDMTShelfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 10, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucDMTShelfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: adslAtucDMTShelfIndex.setDescription('ADSL DMT module Shelf ID.')
adslAtucDMTSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 10, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucDMTSlotIndex.setStatus('mandatory')
if mibBuilder.loadTexts: adslAtucDMTSlotIndex.setDescription('ADSL DMT module Slot ID.')
adslAtucDMTLineIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 10, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucDMTLineIndex.setStatus('mandatory')
if mibBuilder.loadTexts: adslAtucDMTLineIndex.setDescription('ADSL DMT module line ID.')
adslAtucDMTIssue = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 10, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("t1-413-iss1", 1), ("t1-413-iss2", 2), ("t1-413-iss3", 3), ("gdmt-iss1", 4), ("etsi-iss1", 5), ("other", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucDMTIssue.setStatus('mandatory')
if mibBuilder.loadTexts: adslAtucDMTIssue.setDescription('Reports the issue number of the relevant standard that the DMT ADSL transceiver at the ATU-C is currently operating to.')
adslAtucDMTState = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 10, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("other", 1), ("power-up", 2), ("configure", 3), ("idle", 4), ("quiet", 5), ("tone", 6), ("activating", 7), ("training", 8), ("analyzing", 9), ("exchange", 10), ("steady-state", 11), ("not-responding", 12)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucDMTState.setStatus('mandatory')
if mibBuilder.loadTexts: adslAtucDMTState.setDescription('Report current state of ATU-C DMT transceiver.')
adslAtucDMTInterleavePath = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 10, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("as0", 2), ("as1", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucDMTInterleavePath.setStatus('mandatory')
if mibBuilder.loadTexts: adslAtucDMTInterleavePath.setDescription('Report bearer channel of downstream interleaved path.')
adslAtucDMTFastPath = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 10, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("as0", 2), ("as1", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAtucDMTFastPath.setStatus('mandatory')
if mibBuilder.loadTexts: adslAtucDMTFastPath.setDescription('Report bearer channel of downstream fast path.')
adslAturDMTPhysTable = MibTable((1, 3, 6, 1, 4, 1, 529, 4, 10, 3), )
if mibBuilder.loadTexts: adslAturDMTPhysTable.setStatus('mandatory')
if mibBuilder.loadTexts: adslAturDMTPhysTable.setDescription('ADSL DMT status parameters.')
adslAturDMTPhysEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 4, 10, 3, 1), ).setIndexNames((0, "ASCEND-ADSL-DMT-MIB", "adslAturDMTIfEntryIndex"))
if mibBuilder.loadTexts: adslAturDMTPhysEntry.setStatus('mandatory')
if mibBuilder.loadTexts: adslAturDMTPhysEntry.setDescription('An interface status entry containing objects to describe the interface.')
adslAturDMTIfEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 10, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAturDMTIfEntryIndex.setStatus('mandatory')
if mibBuilder.loadTexts: adslAturDMTIfEntryIndex.setDescription('Index into the Status Table via the interface group ifIndex value.')
adslAturDMTShelfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 10, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAturDMTShelfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: adslAturDMTShelfIndex.setDescription('ADSL DMT module Shelf ID.')
adslAturDMTSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 10, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAturDMTSlotIndex.setStatus('mandatory')
if mibBuilder.loadTexts: adslAturDMTSlotIndex.setDescription('ADSL DMT module Slot ID.')
adslAturDMTLineIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 10, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAturDMTLineIndex.setStatus('mandatory')
if mibBuilder.loadTexts: adslAturDMTLineIndex.setDescription('ADSL DMT module line ID.')
adslAturDMTIssue = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 10, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("t1-413-iss1", 1), ("t1-413-iss2", 2), ("t1-413-iss3", 3), ("gdmt-iss1", 4), ("etsi-iss1", 5), ("other", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAturDMTIssue.setStatus('mandatory')
if mibBuilder.loadTexts: adslAturDMTIssue.setDescription('Reports the issue number of the relevant standard that the DMT ADSL transceiver at the ATU-C is currently operating to.')
adslAturDMTState = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 10, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("other", 1), ("activating", 2), ("training", 3), ("analyzing", 4), ("exchange", 5), ("steady-state", 6), ("not-responding", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAturDMTState.setStatus('mandatory')
if mibBuilder.loadTexts: adslAturDMTState.setDescription('Report current state of ATU-C DMT transceiver.')
adslAturDMTInterleavePath = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 10, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("ls0", 2), ("ls1", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAturDMTInterleavePath.setStatus('mandatory')
if mibBuilder.loadTexts: adslAturDMTInterleavePath.setDescription('Report bearer channel of upstream interleaved path.')
adslAturDMTFastPath = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 10, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("ls0", 2), ("ls1", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslAturDMTFastPath.setStatus('mandatory')
if mibBuilder.loadTexts: adslAturDMTFastPath.setDescription('Report bearer channel of upstream fast path.')
adslDmtLineStatisticTable = MibTable((1, 3, 6, 1, 4, 1, 529, 4, 10, 4), )
if mibBuilder.loadTexts: adslDmtLineStatisticTable.setStatus('mandatory')
if mibBuilder.loadTexts: adslDmtLineStatisticTable.setDescription('ADSL DMT statistical parameters.')
adslDmtLineStatisticEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 4, 10, 4, 1), ).setIndexNames((0, "ASCEND-ADSL-DMT-MIB", "adslDmtStatIfEntryIndex"))
if mibBuilder.loadTexts: adslDmtLineStatisticEntry.setStatus('mandatory')
if mibBuilder.loadTexts: adslDmtLineStatisticEntry.setDescription('An interface statistical entry containing objects to describe the interface.')
adslDmtStatIfEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 10, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslDmtStatIfEntryIndex.setStatus('mandatory')
if mibBuilder.loadTexts: adslDmtStatIfEntryIndex.setDescription('Index into the Status Table via the interface group ifIndex value.')
adslDmtStatShelfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 10, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslDmtStatShelfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: adslDmtStatShelfIndex.setDescription('ADSL DMT module Shelf ID.')
adslDmtStatSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 10, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslDmtStatSlotIndex.setStatus('mandatory')
if mibBuilder.loadTexts: adslDmtStatSlotIndex.setDescription('ADSL DMT module Slot ID.')
adslDmtStatLineIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 10, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslDmtStatLineIndex.setStatus('mandatory')
if mibBuilder.loadTexts: adslDmtStatLineIndex.setDescription('ADSL DMT module interface ID.')
adslDmtStatConnUpDays = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 10, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslDmtStatConnUpDays.setStatus('mandatory')
if mibBuilder.loadTexts: adslDmtStatConnUpDays.setDescription('Connection up day count.')
adslDmtStatConnUpHours = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 10, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslDmtStatConnUpHours.setStatus('mandatory')
if mibBuilder.loadTexts: adslDmtStatConnUpHours.setDescription('Connection Up 24 hour count.')
adslDmtStatConnUpMinutes = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 10, 4, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslDmtStatConnUpMinutes.setStatus('mandatory')
if mibBuilder.loadTexts: adslDmtStatConnUpMinutes.setDescription('Connection up minute count.')
adslDmtStatRxSignalPresent = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 10, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslDmtStatRxSignalPresent.setStatus('mandatory')
if mibBuilder.loadTexts: adslDmtStatRxSignalPresent.setDescription('Receive signal present detection.')
adslDmtStatUpDwnCntr = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 10, 4, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslDmtStatUpDwnCntr.setStatus('mandatory')
if mibBuilder.loadTexts: adslDmtStatUpDwnCntr.setDescription('Line Up Down counter value displays the number of times the interface transitions from a down to up state.')
adslDmtStatLineSelfTest = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 4, 10, 4, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("failed", 2), ("passed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adslDmtStatLineSelfTest.setStatus('mandatory')
if mibBuilder.loadTexts: adslDmtStatLineSelfTest.setDescription('Line hardware self test results (Passed or Failed).')
mibBuilder.exportSymbols("ASCEND-ADSL-DMT-MIB", adslAturDMTState=adslAturDMTState, adslDmtStatLineSelfTest=adslDmtStatLineSelfTest, adslDmtStatusUnitType=adslDmtStatusUnitType, adslAturDMTFastPath=adslAturDMTFastPath, adslAtucDMTState=adslAtucDMTState, adslDmtStatusFirmWareVer=adslDmtStatusFirmWareVer, adslDmtStatusSlotIndex=adslDmtStatusSlotIndex, adslAtucDMTLineIndex=adslAtucDMTLineIndex, adslDmtStatusTrellis=adslDmtStatusTrellis, adslDmtStatConnUpHours=adslDmtStatConnUpHours, adslDmtStatusLineIndex=adslDmtStatusLineIndex, adslDmtStatusShelfIndex=adslDmtStatusShelfIndex, adslDmtStatRxSignalPresent=adslDmtStatRxSignalPresent, adslDmtLineStatusTable=adslDmtLineStatusTable, adslAturDMTPhysEntry=adslAturDMTPhysEntry, adslDmtLineStatisticEntry=adslDmtLineStatisticEntry, adslDmtLineStatusEntry=adslDmtLineStatusEntry, adslAturDMTIssue=adslAturDMTIssue, adslAturDMTSlotIndex=adslAturDMTSlotIndex, adslAturDMTShelfIndex=adslAturDMTShelfIndex, adslAtucDMTIssue=adslAtucDMTIssue, adslAtucDMTInterleavePath=adslAtucDMTInterleavePath, adslAtucDMTFastPath=adslAtucDMTFastPath, adslDmtStatusHardWareVer=adslDmtStatusHardWareVer, adslAturDMTLineIndex=adslAturDMTLineIndex, adslDmtStatUpDwnCntr=adslDmtStatUpDwnCntr, adslAturDMTPhysTable=adslAturDMTPhysTable, adslDmtStatusDownRate=adslDmtStatusDownRate, adslAtucDMTShelfIndex=adslAtucDMTShelfIndex, adslAtucDMTPhysEntry=adslAtucDMTPhysEntry, adslDmtStatShelfIndex=adslDmtStatShelfIndex, adslDmtStatConnUpDays=adslDmtStatConnUpDays, adslAtucDMTPhysTable=adslAtucDMTPhysTable, adslAturDMTInterleavePath=adslAturDMTInterleavePath, adslDmtStatusVendorId=adslDmtStatusVendorId, adslDmtStatusEoc=adslDmtStatusEoc, adslDmtStatIfEntryIndex=adslDmtStatIfEntryIndex, adslDmtStatConnUpMinutes=adslDmtStatConnUpMinutes, adslAtucDMTIfEntryIndex=adslAtucDMTIfEntryIndex, adslDmtStatLineIndex=adslDmtStatLineIndex, adslDmtStatusUpRate=adslDmtStatusUpRate, adslAturDMTIfEntryIndex=adslAturDMTIfEntryIndex, adslDmtStatSlotIndex=adslDmtStatSlotIndex, adslAtucDMTSlotIndex=adslAtucDMTSlotIndex, adslDmtStatusIfEntryIndex=adslDmtStatusIfEntryIndex, adslDmtLineStatisticTable=adslDmtLineStatisticTable)