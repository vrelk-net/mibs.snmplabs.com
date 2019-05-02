#
# PySNMP MIB module H3C-VOCALLACTIVE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-VOCALLACTIVE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:24:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
CodecType, = mibBuilder.importSymbols("H3C-VO-TYPE-MIB", "CodecType")
h3cVoice, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cVoice")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Unsigned32, Counter64, Counter32, Gauge32, ModuleIdentity, NotificationType, ObjectIdentity, Integer32, TimeTicks, MibIdentifier, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Unsigned32", "Counter64", "Counter32", "Gauge32", "ModuleIdentity", "NotificationType", "ObjectIdentity", "Integer32", "TimeTicks", "MibIdentifier", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
h3cVoiceCallActive = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6))
h3cVoiceCallActive.setRevisions(('2005-03-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: h3cVoiceCallActive.setRevisionsDescriptions(('The initial version of this MIB file.',))
if mibBuilder.loadTexts: h3cVoiceCallActive.setLastUpdated('200503150000Z')
if mibBuilder.loadTexts: h3cVoiceCallActive.setOrganization('Huawei-3COM Technologies Co., Ltd.')
if mibBuilder.loadTexts: h3cVoiceCallActive.setContactInfo('PLAT Team Huawei 3Com Technologies co.,Ltd. Shang-Di Information Industry Base, Hai-Dian District Beijing P.R. China http://www.huawei-3com.com Zip:100085')
if mibBuilder.loadTexts: h3cVoiceCallActive.setDescription('This MIB file is to provide the definition of voice call active record.')
h3cVoCallActiveObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1))
h3cVoCallActiveTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1, 1), )
if mibBuilder.loadTexts: h3cVoCallActiveTable.setStatus('current')
if mibBuilder.loadTexts: h3cVoCallActiveTable.setDescription('The table contains the voice active call information.')
h3cVoCallActiveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1, 1, 1), ).setIndexNames((0, "H3C-VOCALLACTIVE-MIB", "h3cVoCallActiveChannel"))
if mibBuilder.loadTexts: h3cVoCallActiveEntry.setStatus('current')
if mibBuilder.loadTexts: h3cVoCallActiveEntry.setDescription('The entry of h3cVoCallActiveTable.')
h3cVoCallActiveChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cVoCallActiveChannel.setStatus('current')
if mibBuilder.loadTexts: h3cVoCallActiveChannel.setDescription('This object indicates the logic channel number of a call.')
h3cVoCallActiveCallerNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallActiveCallerNumber.setStatus('current')
if mibBuilder.loadTexts: h3cVoCallActiveCallerNumber.setDescription('This object indicates the caller number of a call.')
h3cVoCallActiveCalledNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallActiveCalledNumber.setStatus('current')
if mibBuilder.loadTexts: h3cVoCallActiveCalledNumber.setDescription('This object indicates the called number of a call.')
h3cVoCallActiveEncodeType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1, 1, 1, 4), CodecType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallActiveEncodeType.setStatus('current')
if mibBuilder.loadTexts: h3cVoCallActiveEncodeType.setDescription('This object indicates the encode type of a call.')
h3cVoCallActiveLocalAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1, 1, 1, 5), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallActiveLocalAddressType.setStatus('current')
if mibBuilder.loadTexts: h3cVoCallActiveLocalAddressType.setDescription('This object indicates the local IP address type of a call.')
h3cVoCallActiveLocalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1, 1, 1, 6), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallActiveLocalAddress.setStatus('current')
if mibBuilder.loadTexts: h3cVoCallActiveLocalAddress.setDescription('This object indicates the local IP address of a call.')
h3cVoCallActivePeerAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1, 1, 1, 7), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallActivePeerAddressType.setStatus('current')
if mibBuilder.loadTexts: h3cVoCallActivePeerAddressType.setDescription('This object indicates the peer IP address type of a call.')
h3cVoCallActivePeerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1, 1, 1, 8), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallActivePeerAddress.setStatus('current')
if mibBuilder.loadTexts: h3cVoCallActivePeerAddress.setDescription('This object indicates the peer IP address of a call.')
h3cVoCallActiveCallOrigin = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("caller", 1), ("called", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallActiveCallOrigin.setStatus('current')
if mibBuilder.loadTexts: h3cVoCallActiveCallOrigin.setDescription('This object indicates the direction of a call.')
h3cVoCallActiveIPSigType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("h323", 2), ("sip", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallActiveIPSigType.setStatus('current')
if mibBuilder.loadTexts: h3cVoCallActiveIPSigType.setDescription('This object indicates the ip signal type.')
h3cVoCallActivePSTNSigType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 1), ("fxs", 2), ("fxo", 3), ("em", 4), ("r2", 5), ("dss1", 6), ("dem", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallActivePSTNSigType.setStatus('current')
if mibBuilder.loadTexts: h3cVoCallActivePSTNSigType.setDescription('This object indicates the PSTN(Public Switched Telephone Network) signal type.')
h3cVoCallActiveStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 6, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("idle", 1), ("calling", 2), ("alerting", 3), ("talking", 4), ("release", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cVoCallActiveStatus.setStatus('current')
if mibBuilder.loadTexts: h3cVoCallActiveStatus.setDescription('This object indicates the current progress status of a call.')
mibBuilder.exportSymbols("H3C-VOCALLACTIVE-MIB", h3cVoiceCallActive=h3cVoiceCallActive, h3cVoCallActiveLocalAddress=h3cVoCallActiveLocalAddress, h3cVoCallActivePeerAddress=h3cVoCallActivePeerAddress, h3cVoCallActiveCallOrigin=h3cVoCallActiveCallOrigin, h3cVoCallActiveIPSigType=h3cVoCallActiveIPSigType, h3cVoCallActiveStatus=h3cVoCallActiveStatus, h3cVoCallActiveObjects=h3cVoCallActiveObjects, h3cVoCallActivePeerAddressType=h3cVoCallActivePeerAddressType, h3cVoCallActiveTable=h3cVoCallActiveTable, h3cVoCallActiveChannel=h3cVoCallActiveChannel, h3cVoCallActiveCalledNumber=h3cVoCallActiveCalledNumber, h3cVoCallActiveLocalAddressType=h3cVoCallActiveLocalAddressType, PYSNMP_MODULE_ID=h3cVoiceCallActive, h3cVoCallActiveEntry=h3cVoCallActiveEntry, h3cVoCallActiveCallerNumber=h3cVoCallActiveCallerNumber, h3cVoCallActiveEncodeType=h3cVoCallActiveEncodeType, h3cVoCallActivePSTNSigType=h3cVoCallActivePSTNSigType)