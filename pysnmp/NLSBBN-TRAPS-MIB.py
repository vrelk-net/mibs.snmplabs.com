#
# PySNMP MIB module NLSBBN-TRAPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NLSBBN-TRAPS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:07:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
gi, nlsbbn, bbnTraps = mibBuilder.importSymbols("NLS-BBNIDENT-MIB", "gi", "nlsbbn", "bbnTraps")
EntryStatus, = mibBuilder.importSymbols("RFC1271-MIB", "EntryStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, ObjectIdentity, Gauge32, iso, Counter64, IpAddress, Bits, TimeTicks, enterprises, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, ModuleIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "Gauge32", "iso", "Counter64", "IpAddress", "Bits", "TimeTicks", "enterprises", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "ModuleIdentity", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bbnTrapElements = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 5, 3, 1))
bbnTrapControl = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 5, 3, 2))
trapIdentifier = MibScalar((1, 3, 6, 1, 4, 1, 1166, 5, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapIdentifier.setStatus('mandatory')
trapNetworkElemModelNumber = MibScalar((1, 3, 6, 1, 4, 1, 1166, 5, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapNetworkElemModelNumber.setStatus('mandatory')
trapNetworkElemSerialNum = MibScalar((1, 3, 6, 1, 4, 1, 1166, 5, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapNetworkElemSerialNum.setStatus('mandatory')
trapPerceivedSeverity = MibScalar((1, 3, 6, 1, 4, 1, 1166, 5, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("cleared", 1), ("indeterminate", 2), ("warning", 3), ("minor", 4), ("major", 5), ("critical", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapPerceivedSeverity.setStatus('mandatory')
trapNetworkElemOperState = MibScalar((1, 3, 6, 1, 4, 1, 1166, 5, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapNetworkElemOperState.setStatus('mandatory')
trapNetworkElemAlarmStatus = MibScalar((1, 3, 6, 1, 4, 1, 1166, 5, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("idle", 1), ("indeterminate", 2), ("warning", 3), ("minor", 4), ("major", 5), ("critical", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapNetworkElemAlarmStatus.setStatus('mandatory')
trapNetworkElemAdminState = MibScalar((1, 3, 6, 1, 4, 1, 1166, 5, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("locked", 1), ("unlocked", 2), ("shuttingDown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapNetworkElemAdminState.setStatus('mandatory')
trapNetworkElemAvailStatus = MibScalar((1, 3, 6, 1, 4, 1, 1166, 5, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("inTest", 1), ("failed", 2), ("powerOff", 3), ("offLine", 4), ("offDuty", 5), ("dependency", 6), ("degraded", 7), ("notInstalled", 8), ("logFull", 9), ("available", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapNetworkElemAvailStatus.setStatus('mandatory')
trapText = MibScalar((1, 3, 6, 1, 4, 1, 1166, 5, 3, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapText.setStatus('mandatory')
trapNETrapLastTrapTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 1166, 5, 3, 1, 10), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapNETrapLastTrapTimeStamp.setStatus('mandatory')
trapChangedObjectId = MibScalar((1, 3, 6, 1, 4, 1, 1166, 5, 3, 1, 11), ObjectIdentifier().clone((1, 3, 6, 1, 4, 1, 1166))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapChangedObjectId.setStatus('mandatory')
trapAdditionalInfoInteger1 = MibScalar((1, 3, 6, 1, 4, 1, 1166, 5, 3, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)).clone(2147483647)).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapAdditionalInfoInteger1.setStatus('mandatory')
trapAdditionalInfoInteger2 = MibScalar((1, 3, 6, 1, 4, 1, 1166, 5, 3, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)).clone(2147483647)).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapAdditionalInfoInteger2.setStatus('mandatory')
trapAdditionalInfoInteger3 = MibScalar((1, 3, 6, 1, 4, 1, 1166, 5, 3, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)).clone(2147483647)).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapAdditionalInfoInteger3.setStatus('mandatory')
trapChangedValueDisplayString = MibScalar((1, 3, 6, 1, 4, 1, 1166, 5, 3, 1, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapChangedValueDisplayString.setStatus('mandatory')
trapChangedValueOID = MibScalar((1, 3, 6, 1, 4, 1, 1166, 5, 3, 1, 16), ObjectIdentifier().clone((1, 3, 6, 1, 4, 1, 1166))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapChangedValueOID.setStatus('mandatory')
trapChangedValueIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 1166, 5, 3, 1, 17), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapChangedValueIpAddress.setStatus('mandatory')
trapChangedValueInteger = MibScalar((1, 3, 6, 1, 4, 1, 1166, 5, 3, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)).clone(2147483647)).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapChangedValueInteger.setStatus('mandatory')
numberOfTrapReceivers = MibScalar((1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numberOfTrapReceivers.setStatus('mandatory')
trapReceiversTable = MibTable((1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 2), )
if mibBuilder.loadTexts: trapReceiversTable.setStatus('mandatory')
trapReceiversTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 2, 1), ).setIndexNames((0, "NLSBBN-TRAPS-MIB", "trapReceiversTableIndex"))
if mibBuilder.loadTexts: trapReceiversTableEntry.setStatus('mandatory')
trapReceiversTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4)))
if mibBuilder.loadTexts: trapReceiversTableIndex.setStatus('mandatory')
trapReceiverAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 2, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapReceiverAddr.setStatus('mandatory')
trapReceiverCommunityString = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 2, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapReceiverCommunityString.setStatus('mandatory')
trapToBeSendQueueSize = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(50, 1000)).clone(50)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapToBeSendQueueSize.setStatus('mandatory')
trapSentQueueSize = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(50, 300)).clone(50)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapSentQueueSize.setStatus('mandatory')
trapThrottlingRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 2, 1, 6), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapThrottlingRate.setStatus('mandatory')
trapLastSent = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapLastSent.setStatus('mandatory')
trapReceiversEntryOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapReceiversEntryOperState.setStatus('mandatory')
trapResendRequest = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 2, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapResendRequest.setStatus('mandatory')
numberOfDiscriminators = MibScalar((1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numberOfDiscriminators.setStatus('mandatory')
trapDiscrimTable = MibTable((1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 4), )
if mibBuilder.loadTexts: trapDiscrimTable.setStatus('mandatory')
trapDiscrimTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 4, 1), ).setIndexNames((0, "NLSBBN-TRAPS-MIB", "trapDiscrimTableIndex"))
if mibBuilder.loadTexts: trapDiscrimTableEntry.setStatus('mandatory')
trapDiscrimTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 20)))
if mibBuilder.loadTexts: trapDiscrimTableIndex.setStatus('mandatory')
trapDiscrimReceiverAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 4, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapDiscrimReceiverAddr.setStatus('mandatory')
trapDiscrimAvailabilityStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(5, 10))).clone(namedValues=NamedValues(("offDuty", 5), ("available", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapDiscrimAvailabilityStatus.setStatus('mandatory')
trapDiscrimWeeklyMask = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 4, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 6))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapDiscrimWeeklyMask.setStatus('mandatory')
trapDiscrimDailyStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 4, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1439))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapDiscrimDailyStartTime.setStatus('mandatory')
trapDiscrimDailyStopTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 4, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1439))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapDiscrimDailyStopTime.setStatus('mandatory')
trapSeverityDiscrim = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("indeterminate", 2), ("warning", 3), ("minor", 4), ("major", 5), ("critical", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapSeverityDiscrim.setStatus('mandatory')
trapDiscrimOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapDiscrimOperationalState.setStatus('mandatory')
trapDiscrimConfigChangeCntl = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 5, 3, 2, 4, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2))).clone('on')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapDiscrimConfigChangeCntl.setStatus('mandatory')
mibBuilder.exportSymbols("NLSBBN-TRAPS-MIB", trapReceiverCommunityString=trapReceiverCommunityString, trapReceiversTableEntry=trapReceiversTableEntry, trapLastSent=trapLastSent, trapReceiverAddr=trapReceiverAddr, trapAdditionalInfoInteger3=trapAdditionalInfoInteger3, trapDiscrimAvailabilityStatus=trapDiscrimAvailabilityStatus, trapNetworkElemOperState=trapNetworkElemOperState, bbnTrapElements=bbnTrapElements, trapResendRequest=trapResendRequest, trapDiscrimTable=trapDiscrimTable, trapNetworkElemSerialNum=trapNetworkElemSerialNum, numberOfDiscriminators=numberOfDiscriminators, trapDiscrimReceiverAddr=trapDiscrimReceiverAddr, trapToBeSendQueueSize=trapToBeSendQueueSize, trapChangedValueOID=trapChangedValueOID, trapPerceivedSeverity=trapPerceivedSeverity, bbnTrapControl=bbnTrapControl, trapSeverityDiscrim=trapSeverityDiscrim, trapDiscrimOperationalState=trapDiscrimOperationalState, trapSentQueueSize=trapSentQueueSize, trapAdditionalInfoInteger1=trapAdditionalInfoInteger1, trapReceiversTableIndex=trapReceiversTableIndex, trapNetworkElemAlarmStatus=trapNetworkElemAlarmStatus, trapNETrapLastTrapTimeStamp=trapNETrapLastTrapTimeStamp, trapChangedObjectId=trapChangedObjectId, trapDiscrimTableIndex=trapDiscrimTableIndex, trapAdditionalInfoInteger2=trapAdditionalInfoInteger2, trapChangedValueInteger=trapChangedValueInteger, trapText=trapText, trapNetworkElemAdminState=trapNetworkElemAdminState, trapReceiversTable=trapReceiversTable, trapDiscrimDailyStopTime=trapDiscrimDailyStopTime, trapIdentifier=trapIdentifier, trapNetworkElemAvailStatus=trapNetworkElemAvailStatus, numberOfTrapReceivers=numberOfTrapReceivers, trapChangedValueDisplayString=trapChangedValueDisplayString, trapDiscrimDailyStartTime=trapDiscrimDailyStartTime, trapDiscrimTableEntry=trapDiscrimTableEntry, trapThrottlingRate=trapThrottlingRate, trapReceiversEntryOperState=trapReceiversEntryOperState, trapChangedValueIpAddress=trapChangedValueIpAddress, trapDiscrimWeeklyMask=trapDiscrimWeeklyMask, trapNetworkElemModelNumber=trapNetworkElemModelNumber, trapDiscrimConfigChangeCntl=trapDiscrimConfigChangeCntl)
