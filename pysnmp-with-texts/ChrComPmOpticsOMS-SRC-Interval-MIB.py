#
# PySNMP MIB module ChrComPmOpticsOMS-SRC-Interval-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ChrComPmOpticsOMS-SRC-Interval-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:35:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
chrComIfifIndex, = mibBuilder.importSymbols("ChrComIfifTable-MIB", "chrComIfifIndex")
TruthValue, = mibBuilder.importSymbols("ChrTyp-MIB", "TruthValue")
chrComPmOptics, = mibBuilder.importSymbols("Chromatis-MIB", "chrComPmOptics")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, ObjectIdentity, Unsigned32, Counter64, Bits, NotificationType, Integer32, Counter32, IpAddress, ModuleIdentity, MibIdentifier, iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "Unsigned32", "Counter64", "Bits", "NotificationType", "Integer32", "Counter32", "IpAddress", "ModuleIdentity", "MibIdentifier", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
chrComPmOpticsOMS_SRC_IntervalTable = MibTable((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 11), ).setLabel("chrComPmOpticsOMS-SRC-IntervalTable")
if mibBuilder.loadTexts: chrComPmOpticsOMS_SRC_IntervalTable.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsOMS_SRC_IntervalTable.setDescription('')
chrComPmOpticsOMS_SRC_IntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 11, 1), ).setLabel("chrComPmOpticsOMS-SRC-IntervalEntry").setIndexNames((0, "ChrComIfifTable-MIB", "chrComIfifIndex"), (0, "ChrComPmOpticsOMS-SRC-Interval-MIB", "chrComPmOpticsIntervalNumber"))
if mibBuilder.loadTexts: chrComPmOpticsOMS_SRC_IntervalEntry.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsOMS_SRC_IntervalEntry.setDescription('')
chrComPmOpticsIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 11, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsIntervalNumber.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsIntervalNumber.setDescription('')
chrComPmOpticsSuspectedIntrvl = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 11, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsSuspectedIntrvl.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsSuspectedIntrvl.setDescription('a flag marking the validity of the entry data')
chrComPmOpticsElapsedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 11, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsElapsedTime.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsElapsedTime.setDescription('measurment duration, in 0.01 seconds')
chrComPmOpticsSuppressedIntrvls = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 11, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsSuppressedIntrvls.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsSuppressedIntrvls.setDescription('invalid for first version. indicates how many all-zero periods have passed.')
chrComPmOpticsORS = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 11, 1, 5), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsORS.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsORS.setDescription('')
chrComPmOpticsSES = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 11, 1, 6), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsSES.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsSES.setDescription('')
chrComPmOpticsUAS = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 11, 1, 7), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsUAS.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsUAS.setDescription('')
chrComPmOpticsMean = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 11, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsMean.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsMean.setDescription('')
chrComPmOpticsMax = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 11, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsMax.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsMax.setDescription('')
chrComPmOpticsMin = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 11, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsMin.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsMin.setDescription('')
chrComPmOpticsSD = MibTableColumn((1, 3, 6, 1, 4, 1, 3695, 1, 10, 1, 11, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComPmOpticsSD.setStatus('current')
if mibBuilder.loadTexts: chrComPmOpticsSD.setDescription('')
mibBuilder.exportSymbols("ChrComPmOpticsOMS-SRC-Interval-MIB", chrComPmOpticsMax=chrComPmOpticsMax, chrComPmOpticsORS=chrComPmOpticsORS, chrComPmOpticsMean=chrComPmOpticsMean, chrComPmOpticsSuppressedIntrvls=chrComPmOpticsSuppressedIntrvls, chrComPmOpticsElapsedTime=chrComPmOpticsElapsedTime, chrComPmOpticsSES=chrComPmOpticsSES, chrComPmOpticsUAS=chrComPmOpticsUAS, chrComPmOpticsOMS_SRC_IntervalEntry=chrComPmOpticsOMS_SRC_IntervalEntry, chrComPmOpticsSD=chrComPmOpticsSD, chrComPmOpticsMin=chrComPmOpticsMin, chrComPmOpticsOMS_SRC_IntervalTable=chrComPmOpticsOMS_SRC_IntervalTable, chrComPmOpticsIntervalNumber=chrComPmOpticsIntervalNumber, chrComPmOpticsSuspectedIntrvl=chrComPmOpticsSuspectedIntrvl)