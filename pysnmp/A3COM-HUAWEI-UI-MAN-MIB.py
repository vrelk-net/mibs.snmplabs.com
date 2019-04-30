#
# PySNMP MIB module A3COM-HUAWEI-UI-MAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-UI-MAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:52:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter32, TimeTicks, MibIdentifier, ObjectIdentity, Gauge32, Counter64, ModuleIdentity, Bits, NotificationType, Integer32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter32", "TimeTicks", "MibIdentifier", "ObjectIdentity", "Gauge32", "Counter64", "ModuleIdentity", "Bits", "NotificationType", "Integer32", "Unsigned32")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
h3cUIMgt = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 2))
if mibBuilder.loadTexts: h3cUIMgt.setLastUpdated('200404081405Z')
if mibBuilder.loadTexts: h3cUIMgt.setOrganization('huawei-3com Technologies Co., Ltd.')
h3cUIMgtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 2, 1))
h3cUIBasicInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 2, 1, 1))
h3cUIScalarObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 2, 1, 1, 1))
h3cUITrapBindObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 2, 1, 1, 2))
h3cTerminalUserName = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 2, 1, 1, 2, 1), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cTerminalUserName.setStatus('current')
h3cTerminalSource = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 2, 1, 1, 2, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cTerminalSource.setStatus('current')
h3cTerminalUserAuthFailureReason = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 2, 1, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("exceedRetries", 1), ("authTimeout", 2), ("otherReason", 3)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: h3cTerminalUserAuthFailureReason.setStatus('current')
h3cUINotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 2, 1, 1, 3))
h3cUINotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 2, 1, 1, 3, 0))
h3cLogIn = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 2, 1, 1, 3, 0, 1)).setObjects(("A3COM-HUAWEI-UI-MAN-MIB", "h3cTerminalUserName"), ("A3COM-HUAWEI-UI-MAN-MIB", "h3cTerminalSource"))
if mibBuilder.loadTexts: h3cLogIn.setStatus('current')
h3cLogOut = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 2, 1, 1, 3, 0, 2)).setObjects(("A3COM-HUAWEI-UI-MAN-MIB", "h3cTerminalUserName"), ("A3COM-HUAWEI-UI-MAN-MIB", "h3cTerminalSource"))
if mibBuilder.loadTexts: h3cLogOut.setStatus('current')
h3cLogInAuthenFailure = NotificationType((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 2, 1, 1, 3, 0, 3)).setObjects(("A3COM-HUAWEI-UI-MAN-MIB", "h3cTerminalUserName"), ("A3COM-HUAWEI-UI-MAN-MIB", "h3cTerminalSource"), ("A3COM-HUAWEI-UI-MAN-MIB", "h3cTerminalUserAuthFailureReason"))
if mibBuilder.loadTexts: h3cLogInAuthenFailure.setStatus('current')
h3cVtyMan = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 2, 1, 2))
h3cVtyAccTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 2, 1, 2, 1), )
if mibBuilder.loadTexts: h3cVtyAccTable.setStatus('current')
h3cVtyAccEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 2, 1, 2, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-UI-MAN-MIB", "h3cVtyAccUserIndex"), (0, "A3COM-HUAWEI-UI-MAN-MIB", "h3cVtyAccConnway"))
if mibBuilder.loadTexts: h3cVtyAccEntry.setStatus('current')
h3cVtyAccUserIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 2, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: h3cVtyAccUserIndex.setStatus('current')
h3cVtyAccConnway = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 2, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 11, 12))).clone(namedValues=NamedValues(("inbound", 1), ("outbound", 2), ("linkinbound", 3), ("acl6inbound", 11), ("acl6outbound", 12))))
if mibBuilder.loadTexts: h3cVtyAccConnway.setStatus('current')
h3cVtyAccAclNum = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 2, 1, 2, 1, 1, 3), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVtyAccAclNum.setStatus('current')
h3cVtyAccEntryRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 2, 1, 2, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cVtyAccEntryRowStatus.setStatus('current')
h3cConStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 2, 1, 3))
h3cConStatusTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 2, 1, 3, 1), )
if mibBuilder.loadTexts: h3cConStatusTable.setStatus('current')
h3cConStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 2, 1, 3, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-UI-MAN-MIB", "h3cConUserIndex"))
if mibBuilder.loadTexts: h3cConStatusEntry.setStatus('current')
h3cConUserIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 2, 1, 3, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cConUserIndex.setStatus('current')
h3cConReAuth = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 2, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cConReAuth.setStatus('current')
h3cUIMgtMIBConformance18 = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 2, 2))
h3cUIMgtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 2, 2, 1))
h3cUIMgtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 2, 2, 1, 1)).setObjects(("A3COM-HUAWEI-UI-MAN-MIB", "h3cUIMgtBasicGroup"), ("A3COM-HUAWEI-UI-MAN-MIB", "h3cConStatusGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cUIMgtMIBCompliance = h3cUIMgtMIBCompliance.setStatus('current')
h3cUIMgtManMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 2, 2, 2))
h3cUIMgtBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 2, 2, 2, 1)).setObjects(("A3COM-HUAWEI-UI-MAN-MIB", "h3cVtyAccAclNum"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cUIMgtBasicGroup = h3cUIMgtBasicGroup.setStatus('current')
h3cConStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 2, 2, 2, 2)).setObjects(("A3COM-HUAWEI-UI-MAN-MIB", "h3cConReAuth"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cConStatusGroup = h3cConStatusGroup.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-UI-MAN-MIB", h3cVtyAccTable=h3cVtyAccTable, h3cUIMgt=h3cUIMgt, h3cUIBasicInfo=h3cUIBasicInfo, h3cConStatus=h3cConStatus, h3cTerminalUserAuthFailureReason=h3cTerminalUserAuthFailureReason, h3cUIMgtBasicGroup=h3cUIMgtBasicGroup, h3cConStatusGroup=h3cConStatusGroup, h3cVtyAccEntry=h3cVtyAccEntry, h3cConStatusEntry=h3cConStatusEntry, h3cLogOut=h3cLogOut, h3cVtyMan=h3cVtyMan, h3cConUserIndex=h3cConUserIndex, h3cVtyAccEntryRowStatus=h3cVtyAccEntryRowStatus, h3cTerminalSource=h3cTerminalSource, PYSNMP_MODULE_ID=h3cUIMgt, h3cUIMgtObjects=h3cUIMgtObjects, h3cVtyAccConnway=h3cVtyAccConnway, h3cUIMgtManMIBGroups=h3cUIMgtManMIBGroups, h3cConStatusTable=h3cConStatusTable, h3cUIMgtMIBCompliance=h3cUIMgtMIBCompliance, h3cUIMgtMIBConformance18=h3cUIMgtMIBConformance18, h3cLogIn=h3cLogIn, h3cTerminalUserName=h3cTerminalUserName, h3cConReAuth=h3cConReAuth, h3cLogInAuthenFailure=h3cLogInAuthenFailure, h3cUIMgtMIBCompliances=h3cUIMgtMIBCompliances, h3cUIScalarObjects=h3cUIScalarObjects, h3cUINotificationsPrefix=h3cUINotificationsPrefix, h3cUITrapBindObjects=h3cUITrapBindObjects, h3cVtyAccUserIndex=h3cVtyAccUserIndex, h3cVtyAccAclNum=h3cVtyAccAclNum, h3cUINotifications=h3cUINotifications)
