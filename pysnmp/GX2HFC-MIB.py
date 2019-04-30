#
# PySNMP MIB module GX2HFC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GX2HFC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:07:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
motproxies, gi = mibBuilder.importSymbols("NLS-BBNIDENT-MIB", "motproxies", "gi")
trapNetworkElemAlarmStatus, trapNetworkElemAdminState, trapNetworkElemAvailStatus, trapText, trapNETrapLastTrapTimeStamp, trapChangedValueInteger, trapIdentifier, trapNetworkElemModelNumber, trapNetworkElemOperState, trapNetworkElemSerialNum, trapPerceivedSeverity, trapChangedObjectId = mibBuilder.importSymbols("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus", "trapNetworkElemAdminState", "trapNetworkElemAvailStatus", "trapText", "trapNETrapLastTrapTimeStamp", "trapChangedValueInteger", "trapIdentifier", "trapNetworkElemModelNumber", "trapNetworkElemOperState", "trapNetworkElemSerialNum", "trapPerceivedSeverity", "trapChangedObjectId")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysUpTime, = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime")
MibIdentifier, ObjectIdentity, Gauge32, iso, Counter64, IpAddress, Bits, TimeTicks, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, ModuleIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "Gauge32", "iso", "Counter64", "IpAddress", "Bits", "TimeTicks", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "ModuleIdentity", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hfc = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 6, 1))
hfcCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 6, 1, 1))
hfcDevices = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 6, 1, 2))
gx2 = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 1))
hfcUnknownType = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 2))
gx2Cm = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 3))
gx2Lm = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 4))
gx2Lmc = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 5))
gx2Rx200 = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 6))
gx2Psdc = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 7))
gx2Rsw200 = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 8))
gx2Rx1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 9))
gx2Lm870C = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 10))
gx2EDFA = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 11))
gx2Em870 = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 12))
gx2Drr3x = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 13))
gx2Drr4x = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 14))
gx2Osw10b = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 15))
gx2Dm870 = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 16))
gx2OA100BD = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 17))
gx2Rsw1000b = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 18))
gx2Dm200 = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 19))
gx2CEB = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 20))
gx2Drr2x = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 21))
gx2Rfa1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 22))
gx2Liteps = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 23))
gx2Em870x2 = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 24))
gx2Drt4x = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 25))
gx2Drt2x = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 26))
gx2LmE = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27))
gx2Dm1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 28))
gx2Rx200BX4 = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 29))
gx2Em1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 30))
gx2Lm1000s = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 31))
gx2Rx085BX4 = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 32))
gx2Ea1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 33))
gx2Dm2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 34))
gx2DualDrr2x = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 35))
gx2Gs1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 36))
hfcCommonTable = MibTable((1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1), )
if mibBuilder.loadTexts: hfcCommonTable.setStatus('mandatory')
hfcCommonTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1), ).setIndexNames((0, "GX2HFC-MIB", "hfcCommonTableIndex"))
if mibBuilder.loadTexts: hfcCommonTableEntry.setStatus('mandatory')
hfcCommonTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hfcCommonTableIndex.setStatus('mandatory')
hfcUnitName = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hfcUnitName.setStatus('mandatory')
hfcUnitTypeDescriptorPointer = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hfcUnitTypeDescriptorPointer.setStatus('mandatory')
hfcUnitHwVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hfcUnitHwVersion.setStatus('mandatory')
hfcUnitFwVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hfcUnitFwVersion.setStatus('mandatory')
hfcUnitModelNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hfcUnitModelNumber.setStatus('mandatory')
hfcUnitLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hfcUnitLocation.setStatus('mandatory')
hfcUnitSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hfcUnitSerialNumber.setStatus('mandatory')
hfcUnitAdministrativeState = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("readOnly", 1), ("operatorAccess", 2), ("factoryAccess", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hfcUnitAdministrativeState.setStatus('mandatory')
hfcUnitOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hfcUnitOperationalState.setStatus('mandatory')
hfcUnitAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("ok", 1), ("undetermined", 2), ("warning", 3), ("minor", 4), ("major", 5), ("critical", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hfcUnitAlarmStatus.setStatus('mandatory')
hfcUnitAvailabilityStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("inTest", 1), ("failed", 2), ("powerOff", 3), ("offLine", 4), ("offDuty", 5), ("dependency", 6), ("degraded", 7), ("notInstalled", 8), ("logFull", 9), ("available", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hfcUnitAvailabilityStatus.setStatus('mandatory')
hfcLogicalRfNetworkDescriptor = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 13), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hfcLogicalRfNetworkDescriptor.setStatus('mandatory')
hfcUnitDetected = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hfcUnitDetected.setStatus('mandatory')
hfcNELastTrapTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 15), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hfcNELastTrapTimeStamp.setStatus('mandatory')
hfcPhysicalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 16), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hfcPhysicalAddress.setStatus('mandatory')
hfcDateCode = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 17), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hfcDateCode.setStatus('mandatory')
hfcNeighbor1IPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 18), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hfcNeighbor1IPAddress.setStatus('mandatory')
hfcNeighbor2IPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 19), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hfcNeighbor2IPAddress.setStatus('mandatory')
hfcfinshedGoodsPartNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 20), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hfcfinshedGoodsPartNumber.setStatus('mandatory')
hfcManufactureLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 21), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hfcManufactureLocation.setStatus('mandatory')
hfcDeviceSlotLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 22), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hfcDeviceSlotLocation.setStatus('mandatory')
hfcBelongsTo = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 23), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hfcBelongsTo.setStatus('mandatory')
hfcModuleType = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 24), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hfcModuleType.setStatus('mandatory')
hfcDevicePositionData = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hfcDevicePositionData.setStatus('mandatory')
hfcExtendableSlotData = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 26), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hfcExtendableSlotData.setStatus('mandatory')
hfcActualModelNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 1166, 6, 1, 1, 1, 1, 27), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hfcActualModelNumber.setStatus('mandatory')
trapHfcNewNEFound = NotificationType((1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 1) + (0,1)).setObjects(("NLSBBN-TRAPS-MIB", "trapIdentifier"), ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"), ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"), ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"), ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"), ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"), ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"), ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"), ("NLSBBN-TRAPS-MIB", "trapText"), ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"), ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"), ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
trapHfcNewNELost = NotificationType((1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 1) + (0,2)).setObjects(("NLSBBN-TRAPS-MIB", "trapIdentifier"), ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"), ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"), ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"), ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"), ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"), ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"), ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"), ("NLSBBN-TRAPS-MIB", "trapText"), ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"), ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"), ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
trapToBeSendQueueOverflow = NotificationType((1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 1) + (0,3)).setObjects(("NLSBBN-TRAPS-MIB", "trapIdentifier"), ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"), ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"), ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"), ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"), ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"), ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"), ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"), ("NLSBBN-TRAPS-MIB", "trapText"), ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
trapHfcNameChange = NotificationType((1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 1) + (0,4)).setObjects(("NLSBBN-TRAPS-MIB", "trapIdentifier"), ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"), ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"), ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"), ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"), ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"), ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"), ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"), ("NLSBBN-TRAPS-MIB", "trapText"), ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"), ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"), ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
mibBuilder.exportSymbols("GX2HFC-MIB", gx2Lm870C=gx2Lm870C, hfcCommonTableEntry=hfcCommonTableEntry, hfc=hfc, trapHfcNewNEFound=trapHfcNewNEFound, gx2Cm=gx2Cm, gx2Drt2x=gx2Drt2x, gx2Ea1000=gx2Ea1000, gx2Dm2000=gx2Dm2000, hfcUnknownType=hfcUnknownType, hfcUnitTypeDescriptorPointer=hfcUnitTypeDescriptorPointer, gx2Lm=gx2Lm, hfcUnitAlarmStatus=hfcUnitAlarmStatus, hfcModuleType=hfcModuleType, hfcUnitDetected=hfcUnitDetected, gx2Lmc=gx2Lmc, hfcUnitAdministrativeState=hfcUnitAdministrativeState, gx2Em1000=gx2Em1000, gx2Rfa1000=gx2Rfa1000, gx2=gx2, gx2Rsw1000b=gx2Rsw1000b, hfcUnitModelNumber=hfcUnitModelNumber, hfcPhysicalAddress=hfcPhysicalAddress, hfcDateCode=hfcDateCode, hfcNeighbor2IPAddress=hfcNeighbor2IPAddress, hfcManufactureLocation=hfcManufactureLocation, hfcNELastTrapTimeStamp=hfcNELastTrapTimeStamp, gx2Rx200=gx2Rx200, hfcDevicePositionData=hfcDevicePositionData, gx2Em870=gx2Em870, gx2Rsw200=gx2Rsw200, gx2Rx1000=gx2Rx1000, gx2Lm1000s=gx2Lm1000s, gx2Drr3x=gx2Drr3x, gx2OA100BD=gx2OA100BD, hfcCommonTable=hfcCommonTable, hfcActualModelNumber=hfcActualModelNumber, gx2Liteps=gx2Liteps, hfcUnitLocation=hfcUnitLocation, trapToBeSendQueueOverflow=trapToBeSendQueueOverflow, gx2CEB=gx2CEB, hfcLogicalRfNetworkDescriptor=hfcLogicalRfNetworkDescriptor, hfcUnitFwVersion=hfcUnitFwVersion, hfcCommonTableIndex=hfcCommonTableIndex, gx2Drr2x=gx2Drr2x, hfcfinshedGoodsPartNumber=hfcfinshedGoodsPartNumber, trapHfcNewNELost=trapHfcNewNELost, gx2Drt4x=gx2Drt4x, gx2Dm200=gx2Dm200, gx2Osw10b=gx2Osw10b, gx2Rx085BX4=gx2Rx085BX4, hfcUnitSerialNumber=hfcUnitSerialNumber, gx2EDFA=gx2EDFA, hfcBelongsTo=hfcBelongsTo, gx2Gs1000=gx2Gs1000, gx2Rx200BX4=gx2Rx200BX4, hfcDevices=hfcDevices, hfcCommon=hfcCommon, gx2LmE=gx2LmE, gx2Dm1000=gx2Dm1000, hfcUnitOperationalState=hfcUnitOperationalState, gx2DualDrr2x=gx2DualDrr2x, gx2Dm870=gx2Dm870, hfcExtendableSlotData=hfcExtendableSlotData, hfcDeviceSlotLocation=hfcDeviceSlotLocation, gx2Em870x2=gx2Em870x2, gx2Psdc=gx2Psdc, hfcNeighbor1IPAddress=hfcNeighbor1IPAddress, hfcUnitName=hfcUnitName, trapHfcNameChange=trapHfcNameChange, hfcUnitAvailabilityStatus=hfcUnitAvailabilityStatus, gx2Drr4x=gx2Drr4x, hfcUnitHwVersion=hfcUnitHwVersion)