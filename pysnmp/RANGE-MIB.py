#
# PySNMP MIB module RANGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RANGE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:43:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, ModuleIdentity, TimeTicks, IpAddress, MibIdentifier, Bits, NotificationType, Integer32, Counter64, iso, ObjectIdentity, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ModuleIdentity", "TimeTicks", "IpAddress", "MibIdentifier", "Bits", "NotificationType", "Integer32", "Counter64", "iso", "ObjectIdentity", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rangeTestMIB = ModuleIdentity((1, 1, 1))
if mibBuilder.loadTexts: rangeTestMIB.setLastUpdated('9512090000Z')
if mibBuilder.loadTexts: rangeTestMIB.setOrganization('MIB Test Group')
rangeObj = MibIdentifier((1, 1, 2))
obj01 = MibScalar((1, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj01.setStatus('current')
obj02 = MibScalar((1, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj02.setStatus('current')
obj03 = MibScalar((1, 1, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2147483647, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj03.setStatus('current')
obj04 = MibScalar((1, 1, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, -1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj04.setStatus('current')
obj05 = MibScalar((1, 1, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, -2147483648))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj05.setStatus('current')
obj06 = MibScalar((1, 1, 2, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 0))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj06.setStatus('current')
obj07 = MibScalar((1, 1, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(10, 10), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj07.setStatus('current')
obj08 = MibScalar((1, 1, 2, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(10, 10), ValueRangeConstraint(0, 0), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj08.setStatus('current')
obj09 = MibScalar((1, 1, 2, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(10, 10), ValueRangeConstraint(2147483647, 2147483647), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj09.setStatus('current')
obj10 = MibScalar((1, 1, 2, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(2147483647, 2147483647), ValueRangeConstraint(0, 0), ValueRangeConstraint(10, 10), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj10.setStatus('current')
obj11 = MibScalar((1, 1, 2, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(10, 10), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj11.setStatus('current')
obj12 = MibScalar((1, 1, 2, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(10, 10), ValueRangeConstraint(-1, -1), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj12.setStatus('current')
obj13 = MibScalar((1, 1, 2, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-2147483648, -2147483648), ValueRangeConstraint(-1, -1), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj13.setStatus('current')
obj14 = MibScalar((1, 1, 2, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(-2147483648, -2147483648), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj14.setStatus('current')
obj15 = MibScalar((1, 1, 2, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-2147483648, -2147483648), ValueRangeConstraint(-1, -1), ValueRangeConstraint(10, 10), ValueRangeConstraint(0, 0), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj15.setStatus('current')
obj21 = MibScalar((1, 1, 2, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj21.setStatus('current')
obj22 = MibScalar((1, 1, 2, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj22.setStatus('current')
obj23 = MibScalar((1, 1, 2, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj23.setStatus('current')
obj24 = MibScalar((1, 1, 2, 24), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj24.setStatus('current')
obj25 = MibScalar((1, 1, 2, 25), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, -1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj25.setStatus('current')
obj26 = MibScalar((1, 1, 2, 26), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 0))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj26.setStatus('current')
obj27 = MibScalar((1, 1, 2, 27), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-10, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj27.setStatus('current')
obj28 = MibScalar((1, 1, 2, 28), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj28.setStatus('current')
obj31 = MibScalar((1, 1, 2, 31), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 10), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj31.setStatus('current')
obj32 = MibScalar((1, 1, 2, 32), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 10), ValueRangeConstraint(0, 0), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj32.setStatus('current')
obj33 = MibScalar((1, 1, 2, 33), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-2147483648, -1), ValueRangeConstraint(1, 2147483647), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj33.setStatus('current')
obj34 = MibScalar((1, 1, 2, 34), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 2147483647), ValueRangeConstraint(-2147483648, -1), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj34.setStatus('current')
obj35 = MibScalar((1, 1, 2, 35), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-100, -60), ValueRangeConstraint(-40, -5), ValueRangeConstraint(-1, 3), ValueRangeConstraint(5, 10), ValueRangeConstraint(100, 400), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj35.setStatus('current')
obj36 = MibScalar((1, 1, 2, 36), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-200, -200), ValueRangeConstraint(200, 200), ValueRangeConstraint(-199, -199), ValueRangeConstraint(199, 199), ValueRangeConstraint(-198, -198), ValueRangeConstraint(198, 198), ValueRangeConstraint(-197, -197), ValueRangeConstraint(197, 197), ValueRangeConstraint(-196, -196), ValueRangeConstraint(196, 196), ValueRangeConstraint(-195, -195), ValueRangeConstraint(195, 195), ValueRangeConstraint(-194, -194), ValueRangeConstraint(194, 194), ValueRangeConstraint(-193, -193), ValueRangeConstraint(193, 193), ValueRangeConstraint(-192, -192), ValueRangeConstraint(192, 192), ValueRangeConstraint(-191, -191), ValueRangeConstraint(191, 191), ValueRangeConstraint(-190, -190), ValueRangeConstraint(190, 190), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj36.setStatus('current')
obj37 = MibScalar((1, 1, 2, 37), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-200, -190), ValueRangeConstraint(190, 200), ValueRangeConstraint(-170, -160), ValueRangeConstraint(160, 170), ValueRangeConstraint(-150, -140), ValueRangeConstraint(140, 150), ValueRangeConstraint(-120, -100), ValueRangeConstraint(100, 120), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obj37.setStatus('current')
mibBuilder.exportSymbols("RANGE-MIB", obj12=obj12, obj02=obj02, obj05=obj05, obj03=obj03, obj37=obj37, obj31=obj31, obj28=obj28, obj36=obj36, obj01=obj01, PYSNMP_MODULE_ID=rangeTestMIB, obj11=obj11, obj13=obj13, obj04=obj04, obj24=obj24, obj34=obj34, obj07=obj07, obj06=obj06, obj15=obj15, obj22=obj22, obj26=obj26, obj23=obj23, obj08=obj08, obj27=obj27, obj10=obj10, obj09=obj09, obj25=obj25, obj21=obj21, obj14=obj14, obj33=obj33, obj32=obj32, obj35=obj35, rangeObj=rangeObj, rangeTestMIB=rangeTestMIB)
