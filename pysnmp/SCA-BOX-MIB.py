#
# PySNMP MIB module SCA-BOX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SCA-BOX-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:52:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
scanet, = mibBuilder.importSymbols("SCANET-MIB", "scanet")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, MibIdentifier, ModuleIdentity, Integer32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, Unsigned32, NotificationType, Counter32, Gauge32, Bits, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibIdentifier", "ModuleIdentity", "Integer32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "Unsigned32", "NotificationType", "Counter32", "Gauge32", "Bits", "IpAddress", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
box = MibIdentifier((1, 3, 6, 1, 4, 1, 208, 3))
enclosure = MibIdentifier((1, 3, 6, 1, 4, 1, 208, 3, 1))
boards = MibIdentifier((1, 3, 6, 1, 4, 1, 208, 3, 2))
led = MibScalar((1, 3, 6, 1, 4, 1, 208, 3, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: led.setStatus('mandatory')
fan = MibScalar((1, 3, 6, 1, 4, 1, 208, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("fanFailure", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fan.setStatus('mandatory')
power = MibScalar((1, 3, 6, 1, 4, 1, 208, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8, 16, 32))).clone(namedValues=NamedValues(("power1Failure", 1), ("power2Failure", 2), ("power3Failure", 4), ("power4Failure", 8), ("power5Failure", 16), ("power6Failure", 32)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: power.setStatus('mandatory')
slots = MibScalar((1, 3, 6, 1, 4, 1, 208, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 5, 14, 17))).clone(namedValues=NamedValues(("slot-2", 2), ("slot-5", 5), ("slot-14", 14), ("slot-17", 17)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slots.setStatus('mandatory')
slotmap = MibScalar((1, 3, 6, 1, 4, 1, 208, 3, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotmap.setStatus('mandatory')
temperature = MibScalar((1, 3, 6, 1, 4, 1, 208, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("temperatureFailure", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperature.setStatus('mandatory')
fanNo = MibScalar((1, 3, 6, 1, 4, 1, 208, 3, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanNo.setStatus('mandatory')
powerNo = MibScalar((1, 3, 6, 1, 4, 1, 208, 3, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerNo.setStatus('mandatory')
temperatureNo = MibScalar((1, 3, 6, 1, 4, 1, 208, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("yes", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureNo.setStatus('mandatory')
fanPresent = MibScalar((1, 3, 6, 1, 4, 1, 208, 3, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fanPresent.setStatus('mandatory')
powerPresent = MibScalar((1, 3, 6, 1, 4, 1, 208, 3, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: powerPresent.setStatus('mandatory')
temperaturePresent = MibScalar((1, 3, 6, 1, 4, 1, 208, 3, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("yes", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperaturePresent.setStatus('mandatory')
psuFail = MibScalar((1, 3, 6, 1, 4, 1, 208, 3, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("psu1Failure", 1), ("psu2Failure", 2), ("psu3Failure", 3), ("psu4Failure", 4), ("psu5Failure", 5), ("psu6Failure", 6))))
if mibBuilder.loadTexts: psuFail.setStatus('mandatory')
slotmapFail = MibScalar((1, 3, 6, 1, 4, 1, 208, 3, 1, 14), Integer32())
if mibBuilder.loadTexts: slotmapFail.setStatus('mandatory')
brdInfoTable = MibTable((1, 3, 6, 1, 4, 1, 208, 3, 2, 1), )
if mibBuilder.loadTexts: brdInfoTable.setStatus('mandatory')
brdInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 208, 3, 2, 1, 1), ).setIndexNames((0, "SCA-BOX-MIB", "brdNumber1"))
if mibBuilder.loadTexts: brdInfoEntry.setStatus('mandatory')
brdNumber1 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 3, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brdNumber1.setStatus('mandatory')
cardType = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 3, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardType.setStatus('mandatory')
pcbRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 3, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pcbRevision.setStatus('mandatory')
macAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 3, 2, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: macAddress.setStatus('mandatory')
driverSeq = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 3, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: driverSeq.setStatus('mandatory')
product = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 3, 2, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: product.setStatus('mandatory')
serialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 3, 2, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialNumber.setStatus('mandatory')
masterSlave = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 3, 2, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: masterSlave.setStatus('mandatory')
ram = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 3, 2, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ram.setStatus('mandatory')
shram = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 3, 2, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: shram.setStatus('mandatory')
eprom = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 3, 2, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eprom.setStatus('mandatory')
e2prom = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 3, 2, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e2prom.setStatus('mandatory')
flashprom = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 3, 2, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashprom.setStatus('mandatory')
spec0 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 3, 2, 1, 1, 14), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spec0.setStatus('mandatory')
spec1 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 3, 2, 1, 1, 15), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spec1.setStatus('mandatory')
spec2 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 3, 2, 1, 1, 16), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spec2.setStatus('mandatory')
spec3 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 3, 2, 1, 1, 17), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: spec3.setStatus('mandatory')
ipAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 3, 2, 1, 1, 18), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipAddr.setStatus('mandatory')
nsap = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 3, 2, 1, 1, 19), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsap.setStatus('mandatory')
brdStatusTable = MibTable((1, 3, 6, 1, 4, 1, 208, 3, 2, 2), )
if mibBuilder.loadTexts: brdStatusTable.setStatus('mandatory')
brdStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 208, 3, 2, 2, 1), ).setIndexNames((0, "SCA-BOX-MIB", "brdNumber2"))
if mibBuilder.loadTexts: brdStatusEntry.setStatus('mandatory')
brdNumber2 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 3, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brdNumber2.setStatus('mandatory')
brdStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 3, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brdStatus.setStatus('mandatory')
brdLed = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 3, 2, 2, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brdLed.setStatus('mandatory')
brdPlugTable = MibTable((1, 3, 6, 1, 4, 1, 208, 3, 2, 3), )
if mibBuilder.loadTexts: brdPlugTable.setStatus('mandatory')
brdPlugEntry = MibTableRow((1, 3, 6, 1, 4, 1, 208, 3, 2, 3, 1), ).setIndexNames((0, "SCA-BOX-MIB", "brdNumber3"), (0, "SCA-BOX-MIB", "brdPlugNumber"))
if mibBuilder.loadTexts: brdPlugEntry.setStatus('mandatory')
brdNumber3 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 3, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brdNumber3.setStatus('mandatory')
brdPlugNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 3, 2, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brdPlugNumber.setStatus('mandatory')
brdPlugPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 3, 2, 3, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brdPlugPosition.setStatus('mandatory')
brdPlugStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 3, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notAvailable", 1), ("available", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: brdPlugStatus.setStatus('mandatory')
brdPlugType = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 3, 2, 3, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brdPlugType.setStatus('mandatory')
brdPlugPimType = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 3, 2, 3, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 50))).setMaxAccess("readonly")
if mibBuilder.loadTexts: brdPlugPimType.setStatus('mandatory')
brdPlugPimLeds = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 3, 2, 3, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brdPlugPimLeds.setStatus('mandatory')
brdPlugPimOptions = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 3, 2, 3, 1, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brdPlugPimOptions.setStatus('mandatory')
brdOptionTable = MibTable((1, 3, 6, 1, 4, 1, 208, 3, 2, 4), )
if mibBuilder.loadTexts: brdOptionTable.setStatus('mandatory')
brdOptionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 208, 3, 2, 4, 1), ).setIndexNames((0, "SCA-BOX-MIB", "brdNumber4"), (0, "SCA-BOX-MIB", "brdOptionNumber"))
if mibBuilder.loadTexts: brdOptionEntry.setStatus('mandatory')
brdNumber4 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 3, 2, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brdNumber4.setStatus('mandatory')
brdOptionNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 3, 2, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brdOptionNumber.setStatus('mandatory')
brdOptionName = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 3, 2, 4, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brdOptionName.setStatus('mandatory')
brdOptionState = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 3, 2, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notInstalled", 1), ("installed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: brdOptionState.setStatus('mandatory')
brdSwitchSettingTable = MibTable((1, 3, 6, 1, 4, 1, 208, 3, 2, 5), )
if mibBuilder.loadTexts: brdSwitchSettingTable.setStatus('mandatory')
brdSwitchSettingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 208, 3, 2, 5, 1), ).setIndexNames((0, "SCA-BOX-MIB", "brdNumber5"), (0, "SCA-BOX-MIB", "brdSwitchNumber"))
if mibBuilder.loadTexts: brdSwitchSettingEntry.setStatus('mandatory')
brdNumber5 = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 3, 2, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brdNumber5.setStatus('mandatory')
brdSwitchNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 3, 2, 5, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brdSwitchNumber.setStatus('mandatory')
brdSwitchName = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 3, 2, 5, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brdSwitchName.setStatus('mandatory')
brdSwitchSetting = MibTableColumn((1, 3, 6, 1, 4, 1, 208, 3, 2, 5, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: brdSwitchSetting.setStatus('mandatory')
boxPowerFailureEvent = NotificationType((1, 3, 6, 1, 4, 1, 208, 3) + (0,1)).setObjects(("SCA-BOX-MIB", "psuFail"))
boxFanFailureEvent = NotificationType((1, 3, 6, 1, 4, 1, 208, 3) + (0,2))
boxTempFailureEvent = NotificationType((1, 3, 6, 1, 4, 1, 208, 3) + (0,3))
boxModuleInsertedEvent = NotificationType((1, 3, 6, 1, 4, 1, 208, 3) + (0,4)).setObjects(("SCA-BOX-MIB", "slotmapFail"))
boxModuleRemovedEvent = NotificationType((1, 3, 6, 1, 4, 1, 208, 3) + (0,5)).setObjects(("SCA-BOX-MIB", "slotmapFail"))
mibBuilder.exportSymbols("SCA-BOX-MIB", e2prom=e2prom, slotmapFail=slotmapFail, ram=ram, brdSwitchName=brdSwitchName, boxPowerFailureEvent=boxPowerFailureEvent, temperaturePresent=temperaturePresent, serialNumber=serialNumber, powerNo=powerNo, shram=shram, brdPlugPosition=brdPlugPosition, brdPlugPimOptions=brdPlugPimOptions, boxFanFailureEvent=boxFanFailureEvent, brdSwitchSettingTable=brdSwitchSettingTable, powerPresent=powerPresent, brdPlugType=brdPlugType, brdNumber2=brdNumber2, brdNumber5=brdNumber5, brdNumber3=brdNumber3, brdPlugPimLeds=brdPlugPimLeds, brdSwitchNumber=brdSwitchNumber, cardType=cardType, brdStatusEntry=brdStatusEntry, brdPlugNumber=brdPlugNumber, boxTempFailureEvent=boxTempFailureEvent, fan=fan, brdPlugEntry=brdPlugEntry, temperatureNo=temperatureNo, brdOptionName=brdOptionName, brdPlugStatus=brdPlugStatus, brdPlugPimType=brdPlugPimType, fanPresent=fanPresent, product=product, brdStatus=brdStatus, driverSeq=driverSeq, brdSwitchSetting=brdSwitchSetting, slots=slots, enclosure=enclosure, brdOptionNumber=brdOptionNumber, flashprom=flashprom, spec1=spec1, brdOptionState=brdOptionState, boxModuleRemovedEvent=boxModuleRemovedEvent, psuFail=psuFail, led=led, brdStatusTable=brdStatusTable, brdOptionEntry=brdOptionEntry, eprom=eprom, masterSlave=masterSlave, slotmap=slotmap, brdNumber4=brdNumber4, brdOptionTable=brdOptionTable, fanNo=fanNo, brdInfoTable=brdInfoTable, macAddress=macAddress, ipAddr=ipAddr, brdPlugTable=brdPlugTable, boards=boards, box=box, spec3=spec3, boxModuleInsertedEvent=boxModuleInsertedEvent, spec2=spec2, nsap=nsap, power=power, brdNumber1=brdNumber1, spec0=spec0, brdLed=brdLed, temperature=temperature, brdSwitchSettingEntry=brdSwitchSettingEntry, brdInfoEntry=brdInfoEntry, pcbRevision=pcbRevision)
