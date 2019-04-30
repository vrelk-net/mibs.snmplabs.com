#
# PySNMP MIB module A3COM-HUAWEI-VOCALLHISTORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-VOCALLHISTORY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:52:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cVoice, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cVoice")
CodecType, = mibBuilder.importSymbols("A3COM-HUAWEI-VO-TYPE-MIB", "CodecType")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, ObjectIdentity, iso, Integer32, Bits, IpAddress, Counter32, ModuleIdentity, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "iso", "Integer32", "Bits", "IpAddress", "Counter32", "ModuleIdentity", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks", "Gauge32")
TextualConvention, DateAndTime, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "TimeStamp", "DisplayString")
h3cVoiceCallHistory = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7))
h3cVoiceCallHistory.setRevisions(('2005-03-15 00:00',))
if mibBuilder.loadTexts: h3cVoiceCallHistory.setLastUpdated('200503150000Z')
if mibBuilder.loadTexts: h3cVoiceCallHistory.setOrganization('Huawei-3COM Technologies Co., Ltd.')
h3cVoCallHistoryObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 1))
h3cVoCallHistoryMaxLen = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoCallHistoryMaxLen.setStatus('current')
h3cVoCallHistoryMaxRetainTime = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cVoCallHistoryMaxRetainTime.setStatus('current')
h3cVoCallHistoryGenericTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 2), )
if mibBuilder.loadTexts: h3cVoCallHistoryGenericTable.setStatus('current')
h3cVoCallHistoryGenericEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 2, 1), ).setIndexNames((0, "A3COM-HUAWEI-VOCALLHISTORY-MIB", "h3cVoCallHisIndex"))
if mibBuilder.loadTexts: h3cVoCallHistoryGenericEntry.setStatus('current')
h3cVoCallHisIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: h3cVoCallHisIndex.setStatus('current')
h3cVoCallHisCallerNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 2, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallHisCallerNumber.setStatus('current')
h3cVoCallHisCalledNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 2, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallHisCalledNumber.setStatus('current')
h3cVoCallHisEncodeType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 2, 1, 4), CodecType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallHisEncodeType.setStatus('current')
h3cVoCallHisChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallHisChannel.setStatus('current')
h3cVoCallHisLocalAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 2, 1, 6), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallHisLocalAddressType.setStatus('current')
h3cVoCallHisLocalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 2, 1, 7), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallHisLocalAddress.setStatus('current')
h3cVoCallHisPeerAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 2, 1, 8), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallHisPeerAddressType.setStatus('current')
h3cVoCallHisPeerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 2, 1, 9), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallHisPeerAddress.setStatus('current')
h3cVoCallHisDisconnectText = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))).clone(namedValues=NamedValues(("normalRelease", 1), ("cardNumberNotExist", 2), ("invalidPassword", 3), ("thisAccountsIsUsing", 4), ("noEnoughBalance", 5), ("theAccountsIsExpired", 6), ("creditLimit", 7), ("userReject", 8), ("serviceInvalid", 9), ("calledLimit", 10), ("maxRedialTimesLimit", 11), ("invalidParameter", 12), ("callerHookOn", 13), ("calledHookOn", 14), ("networkProblem", 15), ("unknownReason", 16)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallHisDisconnectText.setStatus('current')
h3cVoCallHisCallDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 2, 1, 11), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallHisCallDuration.setStatus('current')
h3cVoCallHisVoCallDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 2, 1, 12), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallHisVoCallDuration.setStatus('current')
h3cVoCallHisFaxCallDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 2, 1, 13), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallHisFaxCallDuration.setStatus('current')
h3cVoCallHisImgPages = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 2, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallHisImgPages.setStatus('current')
h3cVoCallHisCallOrigin = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("caller", 1), ("called", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallHisCallOrigin.setStatus('current')
h3cVoCallHistoryVoIPTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 3), )
if mibBuilder.loadTexts: h3cVoCallHistoryVoIPTable.setStatus('current')
h3cVoCallHistoryVoIPEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 3, 1), ).setIndexNames((0, "A3COM-HUAWEI-VOCALLHISTORY-MIB", "h3cVoCallHisVoIPIndex"))
if mibBuilder.loadTexts: h3cVoCallHistoryVoIPEntry.setStatus('current')
h3cVoCallHisVoIPIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: h3cVoCallHisVoIPIndex.setStatus('current')
h3cVoCallHisVoIPSetupTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 3, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallHisVoIPSetupTime.setStatus('current')
h3cVoCallHisVoIPConnTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 3, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallHisVoIPConnTime.setStatus('current')
h3cVoCallHisVoIPDiscTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 3, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallHisVoIPDiscTime.setStatus('current')
h3cVoCallHisVoIPTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallHisVoIPTxPackets.setStatus('current')
h3cVoCallHisVoIPTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallHisVoIPTxBytes.setStatus('current')
h3cVoCallHisVoIPRxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallHisVoIPRxPackets.setStatus('current')
h3cVoCallHisVoIPRxeBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallHisVoIPRxeBytes.setStatus('current')
h3cVoCallHistoryPSTNTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 4), )
if mibBuilder.loadTexts: h3cVoCallHistoryPSTNTable.setStatus('current')
h3cVoCallHistoryPSTNEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 4, 1), ).setIndexNames((0, "A3COM-HUAWEI-VOCALLHISTORY-MIB", "h3cVoCallHisPSTNIndex"))
if mibBuilder.loadTexts: h3cVoCallHistoryPSTNEntry.setStatus('current')
h3cVoCallHisPSTNIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: h3cVoCallHisPSTNIndex.setStatus('current')
h3cVoCallHisPSTNSetupTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 4, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallHisPSTNSetupTime.setStatus('current')
h3cVoCallHisPSTNConnTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 4, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallHisPSTNConnTime.setStatus('current')
h3cVoCallHisPSTNDiscTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 4, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallHisPSTNDiscTime.setStatus('current')
h3cVoCallHisPSTNTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallHisPSTNTxPackets.setStatus('current')
h3cVoCallHisPSTNTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallHisPSTNTxBytes.setStatus('current')
h3cVoCallHisPSTNRxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 4, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallHisPSTNRxPackets.setStatus('current')
h3cVoCallHisPSTNRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 7, 4, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallHisPSTNRxBytes.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-VOCALLHISTORY-MIB", h3cVoCallHisPSTNDiscTime=h3cVoCallHisPSTNDiscTime, h3cVoCallHisCalledNumber=h3cVoCallHisCalledNumber, h3cVoCallHistoryVoIPTable=h3cVoCallHistoryVoIPTable, h3cVoCallHisVoIPConnTime=h3cVoCallHisVoIPConnTime, h3cVoCallHisLocalAddressType=h3cVoCallHisLocalAddressType, h3cVoCallHisVoIPTxPackets=h3cVoCallHisVoIPTxPackets, h3cVoCallHisPSTNIndex=h3cVoCallHisPSTNIndex, h3cVoCallHisPSTNRxBytes=h3cVoCallHisPSTNRxBytes, h3cVoCallHistoryPSTNEntry=h3cVoCallHistoryPSTNEntry, h3cVoCallHisPeerAddressType=h3cVoCallHisPeerAddressType, h3cVoCallHisVoIPRxPackets=h3cVoCallHisVoIPRxPackets, h3cVoCallHistoryPSTNTable=h3cVoCallHistoryPSTNTable, h3cVoCallHisDisconnectText=h3cVoCallHisDisconnectText, h3cVoCallHisPeerAddress=h3cVoCallHisPeerAddress, h3cVoCallHisVoIPDiscTime=h3cVoCallHisVoIPDiscTime, h3cVoiceCallHistory=h3cVoiceCallHistory, h3cVoCallHisPSTNTxPackets=h3cVoCallHisPSTNTxPackets, h3cVoCallHistoryVoIPEntry=h3cVoCallHistoryVoIPEntry, h3cVoCallHistoryObjects=h3cVoCallHistoryObjects, h3cVoCallHisPSTNRxPackets=h3cVoCallHisPSTNRxPackets, h3cVoCallHisVoIPRxeBytes=h3cVoCallHisVoIPRxeBytes, h3cVoCallHisImgPages=h3cVoCallHisImgPages, h3cVoCallHisVoCallDuration=h3cVoCallHisVoCallDuration, h3cVoCallHistoryMaxLen=h3cVoCallHistoryMaxLen, h3cVoCallHisVoIPIndex=h3cVoCallHisVoIPIndex, h3cVoCallHisLocalAddress=h3cVoCallHisLocalAddress, PYSNMP_MODULE_ID=h3cVoiceCallHistory, h3cVoCallHistoryMaxRetainTime=h3cVoCallHistoryMaxRetainTime, h3cVoCallHisPSTNTxBytes=h3cVoCallHisPSTNTxBytes, h3cVoCallHisChannel=h3cVoCallHisChannel, h3cVoCallHisVoIPSetupTime=h3cVoCallHisVoIPSetupTime, h3cVoCallHisFaxCallDuration=h3cVoCallHisFaxCallDuration, h3cVoCallHisCallDuration=h3cVoCallHisCallDuration, h3cVoCallHisPSTNConnTime=h3cVoCallHisPSTNConnTime, h3cVoCallHistoryGenericTable=h3cVoCallHistoryGenericTable, h3cVoCallHistoryGenericEntry=h3cVoCallHistoryGenericEntry, h3cVoCallHisPSTNSetupTime=h3cVoCallHisPSTNSetupTime, h3cVoCallHisIndex=h3cVoCallHisIndex, h3cVoCallHisEncodeType=h3cVoCallHisEncodeType, h3cVoCallHisCallOrigin=h3cVoCallHisCallOrigin, h3cVoCallHisCallerNumber=h3cVoCallHisCallerNumber, h3cVoCallHisVoIPTxBytes=h3cVoCallHisVoIPTxBytes)
