#
# PySNMP MIB module ChrComIfOpticsOTS-SRC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ChrComIfOpticsOTS-SRC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:19:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
chrComIfifIndex, = mibBuilder.importSymbols("ChrComIfifTable-MIB", "chrComIfifIndex")
chrComIfOptics, = mibBuilder.importSymbols("Chromatis-MIB", "chrComIfOptics")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Counter32, ModuleIdentity, iso, Unsigned32, IpAddress, Bits, Counter64, NotificationType, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter32", "ModuleIdentity", "iso", "Unsigned32", "IpAddress", "Bits", "Counter64", "NotificationType", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
chrComIfOpticsOTS_SRCTable = MibTable((1, 3, 6, 1, 4, 1, 3695, 1, 2, 3, 2), ).setLabel("chrComIfOpticsOTS-SRCTable")
if mibBuilder.loadTexts: chrComIfOpticsOTS_SRCTable.setStatus('current')
chrComIfOpticsOTS_SRCEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3695, 1, 2, 3, 2, 1), ).setLabel("chrComIfOpticsOTS-SRCEntry").setIndexNames((0, "ChrComIfifTable-MIB", "chrComIfifIndex"))
if mibBuilder.loadTexts: chrComIfOpticsOTS_SRCEntry.setStatus('current')
chrComIfOpticsOtsSrcOutPower = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 2, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-501, 300))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComIfOpticsOtsSrcOutPower.setStatus('current')
chrComIfOpticsOtsSrcLOOPThr = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 2, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-501, 300))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chrComIfOpticsOtsSrcLOOPThr.setStatus('current')
chrComIfOpticsOtsSrcSafetyThr = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 2, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-501, 300))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chrComIfOpticsOtsSrcSafetyThr.setStatus('current')
chrComIfOpticsAlarmVector = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 2, 3, 2, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComIfOpticsAlarmVector.setStatus('current')
chrComIfOpticsAlarmSeverityProfileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 2, 3, 2, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chrComIfOpticsAlarmSeverityProfileIndex.setStatus('current')
mibBuilder.exportSymbols("ChrComIfOpticsOTS-SRC-MIB", chrComIfOpticsOTS_SRCEntry=chrComIfOpticsOTS_SRCEntry, chrComIfOpticsOTS_SRCTable=chrComIfOpticsOTS_SRCTable, chrComIfOpticsAlarmSeverityProfileIndex=chrComIfOpticsAlarmSeverityProfileIndex, chrComIfOpticsOtsSrcLOOPThr=chrComIfOpticsOtsSrcLOOPThr, chrComIfOpticsAlarmVector=chrComIfOpticsAlarmVector, chrComIfOpticsOtsSrcOutPower=chrComIfOpticsOtsSrcOutPower, chrComIfOpticsOtsSrcSafetyThr=chrComIfOpticsOtsSrcSafetyThr)
