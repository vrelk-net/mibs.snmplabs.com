#
# PySNMP MIB module Wellfleet-DS3E3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-DS3E3-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:33:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, ObjectIdentity, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, Gauge32, NotificationType, Unsigned32, Bits, Integer32, iso, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ObjectIdentity", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "Gauge32", "NotificationType", "Unsigned32", "Bits", "Integer32", "iso", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wfDsx3Group, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfDsx3Group")
wfDs3E3ConfigTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 10), )
if mibBuilder.loadTexts: wfDs3E3ConfigTable.setStatus('mandatory')
wfDs3E3ConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 10, 1), ).setIndexNames((0, "Wellfleet-DS3E3-MIB", "wfDs3E3ConfigLineIndex"))
if mibBuilder.loadTexts: wfDs3E3ConfigEntry.setStatus('mandatory')
wfDs3E3ConfigDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 10, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDs3E3ConfigDelete.setStatus('mandatory')
wfDs3E3ConfigDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDs3E3ConfigDisable.setStatus('mandatory')
wfDs3E3ConfigState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 10, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 20))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("los", 3), ("lof", 4), ("raif", 5), ("ais", 6), ("loopback", 7), ("notpresent", 20))).clone('notpresent')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfDs3E3ConfigState.setStatus('mandatory')
wfDs3E3ConfigLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 10, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfDs3E3ConfigLastChange.setStatus('mandatory')
wfDs3E3ConfigLineIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 10, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfDs3E3ConfigLineIndex.setStatus('mandatory')
wfDs3E3ConfigIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 10, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfDs3E3ConfigIfIndex.setStatus('mandatory')
wfDs3E3ConfigLineType = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 10, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("ds3other", 1), ("ds3m23", 2), ("ds3syntran", 3), ("ds3cbitparity", 4), ("ds3clearchannel", 5), ("e3other", 6), ("e3framed", 7), ("e3plcp", 8), ("autodetect", 9))).clone('autodetect')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDs3E3ConfigLineType.setStatus('mandatory')
wfDs3E3ConfigLineCoding = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 10, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("b3zs", 2), ("hdb3", 3))).clone('b3zs')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDs3E3ConfigLineCoding.setStatus('mandatory')
wfDs3E3ConfigLoopbackConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 10, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noloop", 1), ("payloadloop", 2), ("lineloop", 3))).clone('noloop')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDs3E3ConfigLoopbackConfig.setStatus('mandatory')
wfDs3E3ConfigLineStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 10, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8, 16, 32, 64, 128, 256, 512))).clone(namedValues=NamedValues(("noalarm", 1), ("rcrai", 2), ("txrai", 4), ("rcais", 8), ("txais", 16), ("lof", 32), ("los", 64), ("loopback", 128), ("rctestcode", 256), ("otherfailure", 512))).clone('noalarm')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfDs3E3ConfigLineStatus.setStatus('mandatory')
wfDs3E3ConfigPrimaryClockSource = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 10, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("internal", 1), ("external", 2), ("loop", 3))).clone('loop')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDs3E3ConfigPrimaryClockSource.setStatus('mandatory')
wfDs3E3ConfigSecondaryClockSource = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 10, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("internal", 1), ("external", 2), ("loop", 3))).clone('internal')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDs3E3ConfigSecondaryClockSource.setStatus('mandatory')
wfDs3E3ConfigMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 10, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 4608)).clone(4608)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDs3E3ConfigMtu.setStatus('mandatory')
wfDs3E3ConfigLineBuildOut = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 10, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("long", 1), ("short", 2))).clone('short')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDs3E3ConfigLineBuildOut.setStatus('mandatory')
wfDs3E3ConfigCurrentClock = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 10, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("internal", 1), ("external", 2), ("loop", 3))).clone('loop')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfDs3E3ConfigCurrentClock.setStatus('mandatory')
wfDs3E3ConfigExtClockOperational = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 10, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("present", 1), ("notpresent", 2))).clone('notpresent')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfDs3E3ConfigExtClockOperational.setStatus('mandatory')
wfDs3E3ConfigSetupAlarmThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 10, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 10)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDs3E3ConfigSetupAlarmThreshold.setStatus('mandatory')
wfDs3E3ConfigClearAlarmThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 10, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 10)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDs3E3ConfigClearAlarmThreshold.setStatus('mandatory')
wfDs3E3ConfigLoopbackState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 10, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("noloop", 1), ("mgrreqlineloop", 2), ("mgrreqpayloadloop", 3), ("netreqlineloop", 4), ("netreqpayloadloop", 5))).clone('noloop')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfDs3E3ConfigLoopbackState.setStatus('mandatory')
wfDs3E3ConfigSendCode = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 10, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("sendnocode", 1), ("sendlinecode", 2), ("sendpayloadcode", 3), ("sendds1loopcode", 4))).clone('sendnocode')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfDs3E3ConfigSendCode.setStatus('mandatory')
wfDs3E3ActionTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 17), )
if mibBuilder.loadTexts: wfDs3E3ActionTable.setStatus('mandatory')
wfDs3E3ActionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 17, 1), ).setIndexNames((0, "Wellfleet-DS3E3-MIB", "wfDs3E3ActionPortLineNumber"))
if mibBuilder.loadTexts: wfDs3E3ActionEntry.setStatus('mandatory')
wfDs3E3ActionPortLineNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 17, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfDs3E3ActionPortLineNumber.setStatus('mandatory')
wfDs3E3ActionSendFeacLoopCode = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 17, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 21))).clone(namedValues=NamedValues(("lineloop", 1), ("deactivatell", 2), ("payloadloop", 3), ("deactivatepl", 4), ("noaction", 21))).clone('noaction')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDs3E3ActionSendFeacLoopCode.setStatus('mandatory')
wfDs3E3ActionSendFeacDs1LoopUpCode = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 17, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(29))).clone(namedValues=NamedValues(("noaction", 29))).clone('noaction')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDs3E3ActionSendFeacDs1LoopUpCode.setStatus('mandatory')
wfDs3E3ActionSendFeacDs1LoopDownCode = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 17, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(29))).clone(namedValues=NamedValues(("noaction", 29))).clone('noaction')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDs3E3ActionSendFeacDs1LoopDownCode.setStatus('mandatory')
wfDs3E3ActionClearCurrentStats = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 17, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("clrStats", 1), ("noaction", 2))).clone('noaction')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDs3E3ActionClearCurrentStats.setStatus('mandatory')
wfDs3E3ActionClearFarEndCurrentStats = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 17, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("clrStats", 1), ("noaction", 2))).clone('noaction')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDs3E3ActionClearFarEndCurrentStats.setStatus('mandatory')
wfDs3E3ActionClearDayCurrentStats = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 17, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("clrStats", 1), ("noaction", 2))).clone('noaction')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDs3E3ActionClearDayCurrentStats.setStatus('mandatory')
wfDs3E3ActionClearFarEndDayCurrentStats = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 17, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("clrStats", 1), ("noaction", 2))).clone('noaction')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDs3E3ActionClearFarEndDayCurrentStats.setStatus('mandatory')
wfDs3E3ActionClearIntervalStats = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 17, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("clrStats", 1), ("noaction", 2))).clone('noaction')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDs3E3ActionClearIntervalStats.setStatus('mandatory')
wfDs3E3ActionClearFarEndIntervalStats = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 17, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("clrStats", 1), ("noaction", 2))).clone('noaction')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfDs3E3ActionClearFarEndIntervalStats.setStatus('mandatory')
mibBuilder.exportSymbols("Wellfleet-DS3E3-MIB", wfDs3E3ActionTable=wfDs3E3ActionTable, wfDs3E3ConfigLineType=wfDs3E3ConfigLineType, wfDs3E3ConfigLineStatus=wfDs3E3ConfigLineStatus, wfDs3E3ConfigLineBuildOut=wfDs3E3ConfigLineBuildOut, wfDs3E3ActionClearCurrentStats=wfDs3E3ActionClearCurrentStats, wfDs3E3ConfigSecondaryClockSource=wfDs3E3ConfigSecondaryClockSource, wfDs3E3ConfigEntry=wfDs3E3ConfigEntry, wfDs3E3ActionSendFeacLoopCode=wfDs3E3ActionSendFeacLoopCode, wfDs3E3ActionClearFarEndIntervalStats=wfDs3E3ActionClearFarEndIntervalStats, wfDs3E3ActionEntry=wfDs3E3ActionEntry, wfDs3E3ActionClearIntervalStats=wfDs3E3ActionClearIntervalStats, wfDs3E3ConfigLoopbackConfig=wfDs3E3ConfigLoopbackConfig, wfDs3E3ActionClearDayCurrentStats=wfDs3E3ActionClearDayCurrentStats, wfDs3E3ConfigDisable=wfDs3E3ConfigDisable, wfDs3E3ConfigSendCode=wfDs3E3ConfigSendCode, wfDs3E3ConfigSetupAlarmThreshold=wfDs3E3ConfigSetupAlarmThreshold, wfDs3E3ConfigState=wfDs3E3ConfigState, wfDs3E3ConfigLastChange=wfDs3E3ConfigLastChange, wfDs3E3ConfigLineCoding=wfDs3E3ConfigLineCoding, wfDs3E3ConfigClearAlarmThreshold=wfDs3E3ConfigClearAlarmThreshold, wfDs3E3ActionClearFarEndDayCurrentStats=wfDs3E3ActionClearFarEndDayCurrentStats, wfDs3E3ConfigExtClockOperational=wfDs3E3ConfigExtClockOperational, wfDs3E3ConfigPrimaryClockSource=wfDs3E3ConfigPrimaryClockSource, wfDs3E3ConfigLineIndex=wfDs3E3ConfigLineIndex, wfDs3E3ActionSendFeacDs1LoopUpCode=wfDs3E3ActionSendFeacDs1LoopUpCode, wfDs3E3ConfigIfIndex=wfDs3E3ConfigIfIndex, wfDs3E3ConfigLoopbackState=wfDs3E3ConfigLoopbackState, wfDs3E3ActionSendFeacDs1LoopDownCode=wfDs3E3ActionSendFeacDs1LoopDownCode, wfDs3E3ConfigDelete=wfDs3E3ConfigDelete, wfDs3E3ActionClearFarEndCurrentStats=wfDs3E3ActionClearFarEndCurrentStats, wfDs3E3ConfigTable=wfDs3E3ConfigTable, wfDs3E3ConfigCurrentClock=wfDs3E3ConfigCurrentClock, wfDs3E3ConfigMtu=wfDs3E3ConfigMtu, wfDs3E3ActionPortLineNumber=wfDs3E3ActionPortLineNumber)
