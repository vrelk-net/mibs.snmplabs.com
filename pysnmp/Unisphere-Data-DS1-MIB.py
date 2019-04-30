#
# PySNMP MIB module Unisphere-Data-DS1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-DS1-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:23:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
InterfaceIndexOrZero, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "ifIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
IpAddress, ObjectIdentity, Bits, Unsigned32, NotificationType, Integer32, ModuleIdentity, Counter32, Counter64, iso, Gauge32, TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ObjectIdentity", "Bits", "Unsigned32", "NotificationType", "Integer32", "ModuleIdentity", "Counter32", "Counter64", "iso", "Gauge32", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
usDataMibs, = mibBuilder.importSymbols("Unisphere-Data-MIBs", "usDataMibs")
UsdTimeSlotMap, UsdNextIfIndex = mibBuilder.importSymbols("Unisphere-Data-TC", "UsdTimeSlotMap", "UsdNextIfIndex")
usdDs1MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 5))
usdDs1MIB.setRevisions(('2002-05-13 16:01', '2001-07-31 18:25', '2001-04-04 18:05', '1999-06-17 00:00', '1998-11-13 00:00',))
if mibBuilder.loadTexts: usdDs1MIB.setLastUpdated('200205131601Z')
if mibBuilder.loadTexts: usdDs1MIB.setOrganization('Unisphere Networks, Inc.')
usdDs1Objects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1))
usdDsx1ConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1), )
if mibBuilder.loadTexts: usdDsx1ConfigTable.setStatus('current')
usdDsx1ConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: usdDsx1ConfigEntry.setStatus('current')
usdDsx1TimeSlotMap = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 1), UsdTimeSlotMap()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdDsx1TimeSlotMap.setStatus('current')
usdDsx1Ds1ChannelNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 28))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDsx1Ds1ChannelNumber.setStatus('current')
usdDsx1Capabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdDsx1Capabilities.setStatus('current')
usdDsx1Mode = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("t1", 1), ("e1", 2), ("j1", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDsx1Mode.setStatus('current')
usdDsx1LineBuildOutCapabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdDsx1LineBuildOutCapabilities.setStatus('current')
usdDsx1LineBuildOutType = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("shortHaul", 1), ("longHaul", 2), ("notSupported", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDsx1LineBuildOutType.setStatus('current')
usdDsx1LineAttenuation = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("db0", 1), ("dbMinus7Point5", 2), ("dbMinus15", 3), ("dbMinus22Point5", 4), ("notSupported", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDsx1LineAttenuation.setStatus('current')
usdDsx1LineLength = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64000))).setUnits('meters').setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDsx1LineLength.setStatus('current')
usdDsx1LowerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 9), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDsx1LowerIfIndex.setStatus('current')
usdDsx1RowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDsx1RowStatus.setStatus('current')
usdDsx1SendCode = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))).clone(namedValues=NamedValues(("sendInbandLineCode", 1), ("sendBellcoreLineCode", 2), ("sendBellcoreInbandLineCode", 3), ("sendQRSPattern", 4), ("sendAllZerosPattern", 5), ("sendAllOnesPattern", 6), ("sendAltZeroOnePattern", 7), ("sendTwo11Pattern", 8), ("sendTwo15Pattern", 9), ("sendTwo20Pattern", 10), ("sendTwo23Pattern", 11), ("sendUnfrQRSPattern", 12), ("sendUnfrAllZerosPattern", 13), ("sendUnfrAllOnesPattern", 14), ("sendUnfrAltZeroOnePattern", 15), ("sendUnfrTwo11Pattern", 16), ("sendUnfrTwo15Pattern", 17), ("sendUnfrTwo20Pattern", 18), ("sendUnfrTwo23Pattern", 19), ("otherPattern", 20))).clone('otherPattern')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDsx1SendCode.setStatus('current')
usdDsx1YellowAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4))).clone(namedValues=NamedValues(("generate", 1), ("detect", 2), ("none", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDsx1YellowAlarm.setStatus('current')
usdDsx1RemoteLoopback = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDsx1RemoteLoopback.setStatus('current')
usdDsx1FdlCarrier = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDsx1FdlCarrier.setStatus('current')
usdDsx1FdlEic = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDsx1FdlEic.setStatus('current')
usdDsx1FdlLic = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 16), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 11))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDsx1FdlLic.setStatus('current')
usdDsx1FdlFic = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 17), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDsx1FdlFic.setStatus('current')
usdDsx1FdlUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 18), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 6))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDsx1FdlUnit.setStatus('current')
usdDsx1FdlPfi = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 19), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 38))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDsx1FdlPfi.setStatus('current')
usdDsx1FdlPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 20), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDsx1FdlPort.setStatus('current')
usdDsx1FdlGenerator = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 1, 1, 21), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 38))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDsx1FdlGenerator.setStatus('current')
usdDs1NextIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 1, 2), UsdNextIfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdDs1NextIfIndex.setStatus('current')
usdDs1Conformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 4))
usdDs1Compliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 4, 1))
usdDs1Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 4, 2))
usdDs1Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 4, 1, 1)).setObjects(("Unisphere-Data-DS1-MIB", "usdDs1Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs1Compliance = usdDs1Compliance.setStatus('obsolete')
usdDs1Compliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 4, 1, 2)).setObjects(("Unisphere-Data-DS1-MIB", "usdDs1Group1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs1Compliance1 = usdDs1Compliance1.setStatus('obsolete')
usdDs1Compliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 4, 1, 3)).setObjects(("Unisphere-Data-DS1-MIB", "usdDs1Group2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs1Compliance2 = usdDs1Compliance2.setStatus('obsolete')
usdDs1Compliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 4, 1, 4)).setObjects(("Unisphere-Data-DS1-MIB", "usdDs1Group3"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs1Compliance3 = usdDs1Compliance3.setStatus('current')
usdDs1Group = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 4, 2, 1)).setObjects(("Unisphere-Data-DS1-MIB", "usdDsx1TimeSlotMap"), ("Unisphere-Data-DS1-MIB", "usdDsx1Ds1ChannelNumber"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs1Group = usdDs1Group.setStatus('obsolete')
usdDs1Group1 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 4, 2, 2)).setObjects(("Unisphere-Data-DS1-MIB", "usdDsx1TimeSlotMap"), ("Unisphere-Data-DS1-MIB", "usdDsx1Ds1ChannelNumber"), ("Unisphere-Data-DS1-MIB", "usdDsx1Capabilities"), ("Unisphere-Data-DS1-MIB", "usdDsx1Mode"), ("Unisphere-Data-DS1-MIB", "usdDsx1LineBuildOutCapabilities"), ("Unisphere-Data-DS1-MIB", "usdDsx1LineBuildOutType"), ("Unisphere-Data-DS1-MIB", "usdDsx1LineAttenuation"), ("Unisphere-Data-DS1-MIB", "usdDsx1LineLength"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs1Group1 = usdDs1Group1.setStatus('obsolete')
usdDs1Group2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 4, 2, 3)).setObjects(("Unisphere-Data-DS1-MIB", "usdDsx1TimeSlotMap"), ("Unisphere-Data-DS1-MIB", "usdDsx1Ds1ChannelNumber"), ("Unisphere-Data-DS1-MIB", "usdDsx1Capabilities"), ("Unisphere-Data-DS1-MIB", "usdDsx1Mode"), ("Unisphere-Data-DS1-MIB", "usdDsx1LineBuildOutCapabilities"), ("Unisphere-Data-DS1-MIB", "usdDsx1LineBuildOutType"), ("Unisphere-Data-DS1-MIB", "usdDsx1LineAttenuation"), ("Unisphere-Data-DS1-MIB", "usdDsx1LineLength"), ("Unisphere-Data-DS1-MIB", "usdDsx1LowerIfIndex"), ("Unisphere-Data-DS1-MIB", "usdDsx1RowStatus"), ("Unisphere-Data-DS1-MIB", "usdDs1NextIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs1Group2 = usdDs1Group2.setStatus('obsolete')
usdDs1Group3 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 5, 4, 2, 4)).setObjects(("Unisphere-Data-DS1-MIB", "usdDsx1TimeSlotMap"), ("Unisphere-Data-DS1-MIB", "usdDsx1Ds1ChannelNumber"), ("Unisphere-Data-DS1-MIB", "usdDsx1Capabilities"), ("Unisphere-Data-DS1-MIB", "usdDsx1Mode"), ("Unisphere-Data-DS1-MIB", "usdDsx1LineBuildOutCapabilities"), ("Unisphere-Data-DS1-MIB", "usdDsx1LineBuildOutType"), ("Unisphere-Data-DS1-MIB", "usdDsx1LineAttenuation"), ("Unisphere-Data-DS1-MIB", "usdDsx1LineLength"), ("Unisphere-Data-DS1-MIB", "usdDsx1LowerIfIndex"), ("Unisphere-Data-DS1-MIB", "usdDsx1RowStatus"), ("Unisphere-Data-DS1-MIB", "usdDsx1SendCode"), ("Unisphere-Data-DS1-MIB", "usdDsx1YellowAlarm"), ("Unisphere-Data-DS1-MIB", "usdDsx1RemoteLoopback"), ("Unisphere-Data-DS1-MIB", "usdDsx1FdlCarrier"), ("Unisphere-Data-DS1-MIB", "usdDsx1FdlEic"), ("Unisphere-Data-DS1-MIB", "usdDsx1FdlLic"), ("Unisphere-Data-DS1-MIB", "usdDsx1FdlFic"), ("Unisphere-Data-DS1-MIB", "usdDsx1FdlUnit"), ("Unisphere-Data-DS1-MIB", "usdDsx1FdlPfi"), ("Unisphere-Data-DS1-MIB", "usdDsx1FdlPort"), ("Unisphere-Data-DS1-MIB", "usdDsx1FdlGenerator"), ("Unisphere-Data-DS1-MIB", "usdDs1NextIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs1Group3 = usdDs1Group3.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-DS1-MIB", usdDsx1Ds1ChannelNumber=usdDsx1Ds1ChannelNumber, usdDsx1LineAttenuation=usdDsx1LineAttenuation, usdDs1Compliances=usdDs1Compliances, usdDsx1YellowAlarm=usdDsx1YellowAlarm, usdDsx1SendCode=usdDsx1SendCode, usdDs1Group=usdDs1Group, usdDsx1LineBuildOutType=usdDsx1LineBuildOutType, usdDsx1FdlPort=usdDsx1FdlPort, usdDsx1FdlLic=usdDsx1FdlLic, usdDsx1RowStatus=usdDsx1RowStatus, usdDsx1ConfigTable=usdDsx1ConfigTable, usdDsx1RemoteLoopback=usdDsx1RemoteLoopback, usdDsx1ConfigEntry=usdDsx1ConfigEntry, usdDsx1LineLength=usdDsx1LineLength, usdDs1Groups=usdDs1Groups, usdDsx1TimeSlotMap=usdDsx1TimeSlotMap, usdDs1Objects=usdDs1Objects, usdDs1Group1=usdDs1Group1, usdDsx1Mode=usdDsx1Mode, usdDs1Compliance2=usdDs1Compliance2, usdDs1Conformance=usdDs1Conformance, usdDs1Compliance3=usdDs1Compliance3, usdDsx1FdlGenerator=usdDsx1FdlGenerator, usdDs1Compliance=usdDs1Compliance, PYSNMP_MODULE_ID=usdDs1MIB, usdDsx1FdlCarrier=usdDsx1FdlCarrier, usdDsx1FdlEic=usdDsx1FdlEic, usdDsx1LowerIfIndex=usdDsx1LowerIfIndex, usdDs1MIB=usdDs1MIB, usdDsx1FdlFic=usdDsx1FdlFic, usdDs1Group2=usdDs1Group2, usdDsx1LineBuildOutCapabilities=usdDsx1LineBuildOutCapabilities, usdDs1Compliance1=usdDs1Compliance1, usdDs1Group3=usdDs1Group3, usdDsx1FdlPfi=usdDsx1FdlPfi, usdDs1NextIfIndex=usdDs1NextIfIndex, usdDsx1Capabilities=usdDsx1Capabilities, usdDsx1FdlUnit=usdDsx1FdlUnit)
