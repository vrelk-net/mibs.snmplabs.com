#
# PySNMP MIB module H3C-E1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-E1-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:08:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ObjectIdentity, MibIdentifier, NotificationType, IpAddress, TimeTicks, Counter64, Gauge32, Integer32, Counter32, Bits, iso, ModuleIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibIdentifier", "NotificationType", "IpAddress", "TimeTicks", "Counter64", "Gauge32", "Integer32", "Counter32", "Bits", "iso", "ModuleIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
h3cE1 = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 28))
h3cE1.setRevisions(('2010-04-08 18:55', '2009-06-08 17:41', '2004-12-01 14:36',))
if mibBuilder.loadTexts: h3cE1.setLastUpdated('201004081855Z')
if mibBuilder.loadTexts: h3cE1.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
e1InterfaceStatusTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 28, 1), )
if mibBuilder.loadTexts: e1InterfaceStatusTable.setStatus('current')
e1InterfaceStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 28, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: e1InterfaceStatusEntry.setStatus('current')
e1InterfaceInErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 28, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1InterfaceInErrs.setStatus('current')
e1InterfaceInRuntsErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 28, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1InterfaceInRuntsErrs.setStatus('current')
e1InterfaceInGiantsErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 28, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1InterfaceInGiantsErrs.setStatus('current')
e1InterfaceInCrcErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 28, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1InterfaceInCrcErrs.setStatus('current')
e1InterfaceInAlignErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 28, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1InterfaceInAlignErrs.setStatus('current')
e1InterfaceInOverRunsErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 28, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1InterfaceInOverRunsErrs.setStatus('current')
e1InterfaceInDribblesErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 28, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1InterfaceInDribblesErrs.setStatus('current')
e1InterfaceInAbortedSeqErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 28, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1InterfaceInAbortedSeqErrs.setStatus('current')
e1InterfaceInNoBufferErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 28, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1InterfaceInNoBufferErrs.setStatus('current')
e1InterfaceInFramingErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 28, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1InterfaceInFramingErrs.setStatus('current')
e1InterfaceOutputErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 28, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1InterfaceOutputErrs.setStatus('current')
e1InterfaceOutUnderRunErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 28, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1InterfaceOutUnderRunErrs.setStatus('current')
e1InterfaceOutCollisonsErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 28, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1InterfaceOutCollisonsErrs.setStatus('current')
e1InterfaceOutDeferedErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 28, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1InterfaceOutDeferedErrs.setStatus('current')
h3ce1Table = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 28, 2), )
if mibBuilder.loadTexts: h3ce1Table.setStatus('current')
h3ce1Entry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 28, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: h3ce1Entry.setStatus('current')
class H3cE1TimeSlot(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

h3ce1Type = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 28, 2, 1, 1), Bits().clone(namedValues=NamedValues(("voice", 0), ("pos", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3ce1Type.setStatus('current')
h3ce1Clock = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 28, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("slave", 1), ("master", 2))).clone('slave')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3ce1Clock.setStatus('current')
h3ce1FrameFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 28, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("crc4", 1), ("nocrc4", 2))).clone('crc4')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3ce1FrameFormat.setStatus('current')
h3ce1LineCode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 28, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3))).clone(namedValues=NamedValues(("ami", 1), ("hdb3", 3))).clone('hdb3')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3ce1LineCode.setStatus('current')
h3ce1PriSetTimeSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 28, 2, 1, 5), H3cE1TimeSlot()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3ce1PriSetTimeSlot.setStatus('current')
h3ce1DChannelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 28, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3ce1DChannelIndex.setStatus('current')
h3ce1SubScribLineChannelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 28, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3ce1SubScribLineChannelIndex.setStatus('current')
h3ce1FcmChannelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 28, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3ce1FcmChannelIndex.setStatus('current')
h3ce1InterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 28, 3), )
if mibBuilder.loadTexts: h3ce1InterfaceTable.setStatus('current')
h3ce1InterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 28, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: h3ce1InterfaceEntry.setStatus('current')
h3ce1ControllerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 28, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3ce1ControllerIndex.setStatus('current')
h3ce1TimeSlotSetTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 28, 4), )
if mibBuilder.loadTexts: h3ce1TimeSlotSetTable.setStatus('current')
h3ce1TimeSlotSetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 28, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: h3ce1TimeSlotSetEntry.setStatus('current')
h3ce1TimeSlotSetGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 28, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3ce1TimeSlotSetGroupId.setStatus('current')
h3ce1TimeSlotSetSignalType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 28, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("unkown", 1), ("em-delay", 2), ("em-immediate", 3), ("em-wink", 4), ("fxo-ground", 5), ("fxo-loop", 6), ("fxs-ground", 7), ("fxs-loop", 8), ("r2", 9)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3ce1TimeSlotSetSignalType.setStatus('current')
h3ce1TimeSlotSetList = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 28, 4, 1, 3), H3cE1TimeSlot()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3ce1TimeSlotSetList.setStatus('current')
h3ce1TimeSlotSetRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 28, 4, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3ce1TimeSlotSetRowStatus.setStatus('current')
mibBuilder.exportSymbols("H3C-E1-MIB", h3ce1TimeSlotSetRowStatus=h3ce1TimeSlotSetRowStatus, e1InterfaceInRuntsErrs=e1InterfaceInRuntsErrs, h3ce1SubScribLineChannelIndex=h3ce1SubScribLineChannelIndex, h3ce1Table=h3ce1Table, h3ce1TimeSlotSetList=h3ce1TimeSlotSetList, e1InterfaceInNoBufferErrs=e1InterfaceInNoBufferErrs, e1InterfaceOutputErrs=e1InterfaceOutputErrs, h3ce1FcmChannelIndex=h3ce1FcmChannelIndex, h3ce1InterfaceEntry=h3ce1InterfaceEntry, e1InterfaceInGiantsErrs=e1InterfaceInGiantsErrs, H3cE1TimeSlot=H3cE1TimeSlot, h3ce1InterfaceTable=h3ce1InterfaceTable, h3ce1TimeSlotSetTable=h3ce1TimeSlotSetTable, e1InterfaceOutCollisonsErrs=e1InterfaceOutCollisonsErrs, h3ce1Clock=h3ce1Clock, e1InterfaceOutDeferedErrs=e1InterfaceOutDeferedErrs, e1InterfaceInAlignErrs=e1InterfaceInAlignErrs, h3ce1TimeSlotSetSignalType=h3ce1TimeSlotSetSignalType, h3ce1TimeSlotSetEntry=h3ce1TimeSlotSetEntry, e1InterfaceInCrcErrs=e1InterfaceInCrcErrs, h3cE1=h3cE1, e1InterfaceInOverRunsErrs=e1InterfaceInOverRunsErrs, h3ce1Type=h3ce1Type, e1InterfaceInErrs=e1InterfaceInErrs, e1InterfaceInAbortedSeqErrs=e1InterfaceInAbortedSeqErrs, h3ce1TimeSlotSetGroupId=h3ce1TimeSlotSetGroupId, PYSNMP_MODULE_ID=h3cE1, e1InterfaceStatusEntry=e1InterfaceStatusEntry, h3ce1LineCode=h3ce1LineCode, e1InterfaceInFramingErrs=e1InterfaceInFramingErrs, h3ce1PriSetTimeSlot=h3ce1PriSetTimeSlot, h3ce1ControllerIndex=h3ce1ControllerIndex, e1InterfaceOutUnderRunErrs=e1InterfaceOutUnderRunErrs, h3ce1FrameFormat=h3ce1FrameFormat, h3ce1Entry=h3ce1Entry, e1InterfaceStatusTable=e1InterfaceStatusTable, e1InterfaceInDribblesErrs=e1InterfaceInDribblesErrs, h3ce1DChannelIndex=h3ce1DChannelIndex)
