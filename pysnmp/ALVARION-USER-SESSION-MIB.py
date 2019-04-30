#
# PySNMP MIB module ALVARION-USER-SESSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALVARION-USER-SESSION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:06:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
alvarionMgmtV2, = mibBuilder.importSymbols("ALVARION-SMI", "alvarionMgmtV2")
AlvarionSSIDOrNone, = mibBuilder.importSymbols("ALVARION-TC", "AlvarionSSIDOrNone")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ObjectIdentity, Bits, Integer32, Counter32, NotificationType, IpAddress, MibIdentifier, Counter64, TimeTicks, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Bits", "Integer32", "Counter32", "NotificationType", "IpAddress", "MibIdentifier", "Counter64", "TimeTicks", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "iso", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
alvarionUserSessionMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36))
if mibBuilder.loadTexts: alvarionUserSessionMIB.setLastUpdated('200710310000Z')
if mibBuilder.loadTexts: alvarionUserSessionMIB.setOrganization('Alvarion Ltd.')
alvarionUserSessionMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1))
coUserSessionInfoGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 1))
coUserSessionStGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2))
coUserSessACUserMaxCount = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessACUserMaxCount.setStatus('current')
coUserSessNonACUserMaxCount = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessNonACUserMaxCount.setStatus('current')
coUserSessACUserCount = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessACUserCount.setStatus('current')
coUserSessNonACUserCount = MibScalar((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessNonACUserCount.setStatus('current')
coUserSessionTable = MibTable((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1), )
if mibBuilder.loadTexts: coUserSessionTable.setStatus('current')
coUserSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1), ).setIndexNames((0, "ALVARION-USER-SESSION-MIB", "coUserSessIndex"))
if mibBuilder.loadTexts: coUserSessionEntry.setStatus('current')
coUserSessIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: coUserSessIndex.setStatus('current')
coUserSessUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 252))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessUserName.setStatus('current')
coUserSessClientIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessClientIpAddress.setStatus('current')
coUserSessSessionDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 4), Counter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessSessionDuration.setStatus('current')
coUserSessIdleTime = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 5), Counter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessIdleTime.setStatus('current')
coUserSessMAPGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessMAPGroupName.setStatus('current')
coUserSessVSCName = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessVSCName.setStatus('current')
coUserSessSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 8), AlvarionSSIDOrNone()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessSSID.setStatus('current')
coUserSessVLAN = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessVLAN.setStatus('current')
coUserSessPHYType = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("unknown", 0), ("ieee802dot11a", 1), ("ieee802dot11b", 2), ("ieee802dot11g", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessPHYType.setStatus('current')
coUserSessAuthType = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ac", 1), ("nonAc", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessAuthType.setStatus('current')
coUserSessCalledStationID = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 252))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessCalledStationID.setStatus('current')
coUserSessCallingStationID = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 252))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessCallingStationID.setStatus('current')
coUserSessRADIUSServerProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessRADIUSServerProfileName.setStatus('current')
coUserSessRADIUSServerIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 15), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessRADIUSServerIpAddress.setStatus('current')
coUserSessBytesSent = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessBytesSent.setStatus('current')
coUserSessBytesReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessBytesReceived.setStatus('current')
coUserSessPacketsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessPacketsSent.setStatus('current')
coUserSessPacketsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 1, 2, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserSessPacketsReceived.setStatus('current')
userSessionMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 2))
userSessionMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 2, 0))
alvarionUserSessionMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 3))
alvarionUserSessionMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 3, 1))
alvarionUserSessionMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 3, 2))
alvarionUserSessionMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 3, 1, 1)).setObjects(("ALVARION-USER-SESSION-MIB", "alvarionUserSessionInfoMIBGroup"), ("ALVARION-USER-SESSION-MIB", "alvarionUserSessionStMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionUserSessionMIBCompliance = alvarionUserSessionMIBCompliance.setStatus('current')
alvarionUserSessionInfoMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 3, 2, 1)).setObjects(("ALVARION-USER-SESSION-MIB", "coUserSessACUserMaxCount"), ("ALVARION-USER-SESSION-MIB", "coUserSessNonACUserMaxCount"), ("ALVARION-USER-SESSION-MIB", "coUserSessACUserCount"), ("ALVARION-USER-SESSION-MIB", "coUserSessNonACUserCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionUserSessionInfoMIBGroup = alvarionUserSessionInfoMIBGroup.setStatus('current')
alvarionUserSessionStMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 36, 3, 2, 2)).setObjects(("ALVARION-USER-SESSION-MIB", "coUserSessUserName"), ("ALVARION-USER-SESSION-MIB", "coUserSessClientIpAddress"), ("ALVARION-USER-SESSION-MIB", "coUserSessSessionDuration"), ("ALVARION-USER-SESSION-MIB", "coUserSessIdleTime"), ("ALVARION-USER-SESSION-MIB", "coUserSessMAPGroupName"), ("ALVARION-USER-SESSION-MIB", "coUserSessVSCName"), ("ALVARION-USER-SESSION-MIB", "coUserSessSSID"), ("ALVARION-USER-SESSION-MIB", "coUserSessVLAN"), ("ALVARION-USER-SESSION-MIB", "coUserSessPHYType"), ("ALVARION-USER-SESSION-MIB", "coUserSessAuthType"), ("ALVARION-USER-SESSION-MIB", "coUserSessCalledStationID"), ("ALVARION-USER-SESSION-MIB", "coUserSessCallingStationID"), ("ALVARION-USER-SESSION-MIB", "coUserSessRADIUSServerProfileName"), ("ALVARION-USER-SESSION-MIB", "coUserSessRADIUSServerIpAddress"), ("ALVARION-USER-SESSION-MIB", "coUserSessBytesSent"), ("ALVARION-USER-SESSION-MIB", "coUserSessBytesReceived"), ("ALVARION-USER-SESSION-MIB", "coUserSessPacketsSent"), ("ALVARION-USER-SESSION-MIB", "coUserSessPacketsReceived"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alvarionUserSessionStMIBGroup = alvarionUserSessionStMIBGroup.setStatus('current')
mibBuilder.exportSymbols("ALVARION-USER-SESSION-MIB", coUserSessionTable=coUserSessionTable, coUserSessionStGroup=coUserSessionStGroup, coUserSessCalledStationID=coUserSessCalledStationID, coUserSessClientIpAddress=coUserSessClientIpAddress, coUserSessPacketsSent=coUserSessPacketsSent, coUserSessACUserCount=coUserSessACUserCount, alvarionUserSessionStMIBGroup=alvarionUserSessionStMIBGroup, coUserSessRADIUSServerProfileName=coUserSessRADIUSServerProfileName, coUserSessIdleTime=coUserSessIdleTime, coUserSessNonACUserCount=coUserSessNonACUserCount, coUserSessRADIUSServerIpAddress=coUserSessRADIUSServerIpAddress, coUserSessBytesReceived=coUserSessBytesReceived, coUserSessCallingStationID=coUserSessCallingStationID, coUserSessAuthType=coUserSessAuthType, PYSNMP_MODULE_ID=alvarionUserSessionMIB, coUserSessVSCName=coUserSessVSCName, alvarionUserSessionMIBCompliance=alvarionUserSessionMIBCompliance, alvarionUserSessionInfoMIBGroup=alvarionUserSessionInfoMIBGroup, coUserSessACUserMaxCount=coUserSessACUserMaxCount, coUserSessBytesSent=coUserSessBytesSent, coUserSessVLAN=coUserSessVLAN, coUserSessSessionDuration=coUserSessSessionDuration, coUserSessPHYType=coUserSessPHYType, coUserSessSSID=coUserSessSSID, userSessionMIBNotificationPrefix=userSessionMIBNotificationPrefix, coUserSessMAPGroupName=coUserSessMAPGroupName, alvarionUserSessionMIBCompliances=alvarionUserSessionMIBCompliances, alvarionUserSessionMIBConformance=alvarionUserSessionMIBConformance, alvarionUserSessionMIB=alvarionUserSessionMIB, userSessionMIBNotifications=userSessionMIBNotifications, coUserSessionEntry=coUserSessionEntry, coUserSessUserName=coUserSessUserName, coUserSessionInfoGroup=coUserSessionInfoGroup, coUserSessIndex=coUserSessIndex, alvarionUserSessionMIBObjects=alvarionUserSessionMIBObjects, coUserSessNonACUserMaxCount=coUserSessNonACUserMaxCount, alvarionUserSessionMIBGroups=alvarionUserSessionMIBGroups, coUserSessPacketsReceived=coUserSessPacketsReceived)