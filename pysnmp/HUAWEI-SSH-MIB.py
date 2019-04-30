#
# PySNMP MIB module HUAWEI-SSH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-SSH-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:36:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32, Gauge32, IpAddress, MibIdentifier, TimeTicks, Counter64, Integer32, iso, ModuleIdentity, Bits, NotificationType, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32", "Gauge32", "IpAddress", "MibIdentifier", "TimeTicks", "Counter64", "Integer32", "iso", "ModuleIdentity", "Bits", "NotificationType", "ObjectIdentity")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
hwSSH = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118))
hwSSH.setRevisions(('2014-09-26 00:00', '2014-06-30 00:00', '2014-05-06 00:00', '2010-11-09 00:00', '2010-08-25 00:00', '2010-06-17 00:00', '2010-04-18 00:00', '2010-03-03 00:00', '2010-01-29 00:00', '2006-09-05 00:00',))
if mibBuilder.loadTexts: hwSSH.setLastUpdated('201409260000Z')
if mibBuilder.loadTexts: hwSSH.setOrganization('Huawei Technologies Co.,Ltd.')
hwSSHServer = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1))
hwStelnetServerEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwStelnetServerEnable.setStatus('current')
hwSftpServerEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwSftpServerEnable.setStatus('current')
hwSSHServerComp1x = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwSSHServerComp1x.setStatus('current')
hwSSHServerTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 120))).setUnits('second').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwSSHServerTimeOut.setStatus('current')
hwSSHServerRetry = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 5))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwSSHServerRetry.setStatus('current')
hwSSHServerPort = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(22, 22), ValueRangeConstraint(1025, 65535), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwSSHServerPort.setStatus('current')
hwSSHServerKeyTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 24))).setUnits('hour').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwSSHServerKeyTimeOut.setStatus('current')
hwSSHServerAlarmEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwSSHServerAlarmEnable.setStatus('current')
hwSftpMaxUserNum = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwSftpMaxUserNum.setStatus('current')
hwSftpOnLineUserNum = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSftpOnLineUserNum.setStatus('current')
hwSSHUserTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 11), )
if mibBuilder.loadTexts: hwSSHUserTable.setStatus('current')
hwSSHUserEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 11, 1), ).setIndexNames((0, "HUAWEI-SSH-MIB", "hwSSHUserIndex"))
if mibBuilder.loadTexts: hwSSHUserEntry.setStatus('current')
hwSSHUserIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 11, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 200)))
if mibBuilder.loadTexts: hwSSHUserIndex.setStatus('current')
hwSSHUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 11, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSSHUserName.setStatus('current')
hwSSHUserAssignKey = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 11, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSSHUserAssignKey.setStatus('current')
hwSSHUserAuthType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 11, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("authNULL", 1), ("authPASSWORD", 2), ("authRSA", 3), ("authRSAorPASSWORD", 4), ("authRSAandPASSWORD", 5), ("authDSA", 6), ("authDSAandPASSWORD", 7), ("authAny", 8), ("authECC", 9), ("authECCandPASSWORD", 10))).clone('authPASSWORD')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSSHUserAuthType.setStatus('current')
hwSSHUserServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 11, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("servicetypeNULL", 1), ("servicetypeSTELNET", 2), ("servicetypeSFTP", 3), ("servicetypeALL", 4), ("servicetypeSNetConf", 5), ("servicetypeSftpSNetConf", 6), ("servicetypeSTelnetSftp", 7), ("servicetypeSTelnetSNetConf", 8))).clone('servicetypeNULL')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSSHUserServiceType.setStatus('current')
hwSSHUserSftpDirectory = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 11, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSSHUserSftpDirectory.setStatus('current')
hwSSHUserAuthorizationCMD = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 11, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("authorizationNULL", 1), ("authorizationAAA", 2))).clone('authorizationNULL')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSSHUserAuthorizationCMD.setStatus('current')
hwSSHUserRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 11, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSSHUserRowStatus.setStatus('current')
hwSSHUserAssignKeyType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 11, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("keyTypeNULL", 0), ("keyTypeRSA", 1), ("keyTypeDSA", 2), ("keyTypeECC", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSSHUserAssignKeyType.setStatus('current')
hwSSHServerSessionTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 12), )
if mibBuilder.loadTexts: hwSSHServerSessionTable.setStatus('current')
hwSSHServerSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 12, 1), ).setIndexNames((0, "HUAWEI-SSH-MIB", "hwSSHSessionIndex"))
if mibBuilder.loadTexts: hwSSHServerSessionEntry.setStatus('current')
hwSSHSessionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 12, 1, 1), Integer32())
if mibBuilder.loadTexts: hwSSHSessionIndex.setStatus('current')
hwSSHSessionUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 12, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSSHSessionUserName.setStatus('current')
hwSSHSessionConnectType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 12, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21))).clone(namedValues=NamedValues(("none", 0), ("vty0", 1), ("vty1", 2), ("vty2", 3), ("vty3", 4), ("vty4", 5), ("vty5", 6), ("vty6", 7), ("vty7", 8), ("vty8", 9), ("vty9", 10), ("vty10", 11), ("vty11", 12), ("vty12", 13), ("vty13", 14), ("vty14", 15), ("vty15", 16), ("vty16", 17), ("vty17", 18), ("vty18", 19), ("vty19", 20), ("vty20", 21)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSSHSessionConnectType.setStatus('current')
hwSSHSessionVer = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 12, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSSHSessionVer.setStatus('current')
hwSSHSessionState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 12, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("started", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSSHSessionState.setStatus('current')
hwSSHSessionRetry = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 12, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSSHSessionRetry.setStatus('current')
hwSSHSessionCtosCipher = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 12, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSSHSessionCtosCipher.setStatus('current')
hwSSHSessionStocCipher = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 12, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSSHSessionStocCipher.setStatus('current')
hwSSHSessionCtosHmac = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 12, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSSHSessionCtosHmac.setStatus('current')
hwSSHSessionStocHmac = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 12, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSSHSessionStocHmac.setStatus('current')
hwSSHSessionKex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 12, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSSHSessionKex.setStatus('current')
hwSSHSessionAuthType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 12, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSSHSessionAuthType.setStatus('current')
hwSSHSessionServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 12, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSSHSessionServiceType.setStatus('current')
hwSSHSessionKeyType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 12, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("keyTypeRSA", 1), ("keyTypeDSA", 2), ("keyTypeECC", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSSHSessionKeyType.setStatus('current')
hwSSHSessionConnectionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 12, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSSHSessionConnectionIndex.setStatus('current')
hwSSHSessionCtosCompress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 12, 1, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSSHSessionCtosCompress.setStatus('current')
hwSSHSessionStocCompress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 12, 1, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSSHSessionStocCompress.setStatus('current')
hwRSAPublicKeyTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 13), )
if mibBuilder.loadTexts: hwRSAPublicKeyTable.setStatus('current')
hwRSAPublicKeyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 13, 1), ).setIndexNames((0, "HUAWEI-SSH-MIB", "hwRSAPublicKeyName"))
if mibBuilder.loadTexts: hwRSAPublicKeyEntry.setStatus('current')
hwRSAPublicKeyName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 13, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 30)))
if mibBuilder.loadTexts: hwRSAPublicKeyName.setStatus('current')
hwRSAPublicKeyCode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 13, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 2048))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwRSAPublicKeyCode.setStatus('current')
hwRSAPublicKeyRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 13, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwRSAPublicKeyRowStatus.setStatus('current')
hwRSAPublicKeyFingerprint = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 13, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 60))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwRSAPublicKeyFingerprint.setStatus('current')
hwSNetConfMaxUserNum = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwSNetConfMaxUserNum.setStatus('current')
hwSNetConfServerEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwSNetConfServerEnable.setStatus('current')
hwSSHKeepAliveEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwSSHKeepAliveEnable.setStatus('current')
hwSCPServerEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwSCPServerEnable.setStatus('current')
hwSCPMaxUserNum = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 5))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwSCPMaxUserNum.setStatus('current')
hwSSHClient = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 2))
hwSSHFirstTimeAuthEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwSSHFirstTimeAuthEnable.setStatus('current')
hwSSHServerInfoTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 2, 2), )
if mibBuilder.loadTexts: hwSSHServerInfoTable.setStatus('current')
hwSSHServerInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 2, 2, 1), ).setIndexNames((0, "HUAWEI-SSH-MIB", "hwSSHServerIndex"))
if mibBuilder.loadTexts: hwSSHServerInfoEntry.setStatus('current')
hwSSHServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 20)))
if mibBuilder.loadTexts: hwSSHServerIndex.setStatus('current')
hwSSHServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 2, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSSHServerName.setStatus('current')
hwSSHServerAssignKey = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 2, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSSHServerAssignKey.setStatus('current')
hwSSHServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 2, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSSHServerRowStatus.setStatus('current')
hwSSHServerAssignDSAKey = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 2, 2, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSSHServerAssignDSAKey.setStatus('current')
hwSSHServerAssignECCKey = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 2, 2, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwSSHServerAssignECCKey.setStatus('current')
hwSSHKeepAliveInterval = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwSSHKeepAliveInterval.setStatus('current')
hwSSHKeepAliveMaxCount = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwSSHKeepAliveMaxCount.setStatus('current')
hwSSHNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 3))
hwSSHSftpUserNumExceedMax = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 3, 1)).setObjects(("HUAWEI-SSH-MIB", "hwSftpOnLineUserNum"), ("HUAWEI-SSH-MIB", "hwSftpMaxUserNum"))
if mibBuilder.loadTexts: hwSSHSftpUserNumExceedMax.setStatus('current')
hwSSHMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 4))
hwSSHMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 4, 1))
hwSSHMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 4, 1, 1)).setObjects(("HUAWEI-SSH-MIB", "hwSSHServerGroup"), ("HUAWEI-SSH-MIB", "hwSSHUserGroup"), ("HUAWEI-SSH-MIB", "hwSSHServerSessionGroup"), ("HUAWEI-SSH-MIB", "hwSSHClientGroup"), ("HUAWEI-SSH-MIB", "hwSSHServerInfoGroup"), ("HUAWEI-SSH-MIB", "hwSSHNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSSHMIBCompliance = hwSSHMIBCompliance.setStatus('current')
hwSSHMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 4, 2))
hwSSHServerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 4, 2, 1)).setObjects(("HUAWEI-SSH-MIB", "hwStelnetServerEnable"), ("HUAWEI-SSH-MIB", "hwSftpServerEnable"), ("HUAWEI-SSH-MIB", "hwSSHServerComp1x"), ("HUAWEI-SSH-MIB", "hwSSHServerTimeOut"), ("HUAWEI-SSH-MIB", "hwSSHServerRetry"), ("HUAWEI-SSH-MIB", "hwSSHServerPort"), ("HUAWEI-SSH-MIB", "hwSSHServerKeyTimeOut"), ("HUAWEI-SSH-MIB", "hwSSHServerAlarmEnable"), ("HUAWEI-SSH-MIB", "hwSftpMaxUserNum"), ("HUAWEI-SSH-MIB", "hwSftpOnLineUserNum"), ("HUAWEI-SSH-MIB", "hwSNetConfMaxUserNum"), ("HUAWEI-SSH-MIB", "hwSNetConfServerEnable"), ("HUAWEI-SSH-MIB", "hwSSHKeepAliveEnable"), ("HUAWEI-SSH-MIB", "hwSCPServerEnable"), ("HUAWEI-SSH-MIB", "hwSCPMaxUserNum"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSSHServerGroup = hwSSHServerGroup.setStatus('current')
hwSSHUserGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 4, 2, 2)).setObjects(("HUAWEI-SSH-MIB", "hwSSHUserName"), ("HUAWEI-SSH-MIB", "hwSSHUserAssignKey"), ("HUAWEI-SSH-MIB", "hwSSHUserAuthType"), ("HUAWEI-SSH-MIB", "hwSSHUserServiceType"), ("HUAWEI-SSH-MIB", "hwSSHUserSftpDirectory"), ("HUAWEI-SSH-MIB", "hwSSHUserAuthorizationCMD"), ("HUAWEI-SSH-MIB", "hwSSHUserRowStatus"), ("HUAWEI-SSH-MIB", "hwSSHUserAssignKeyType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSSHUserGroup = hwSSHUserGroup.setStatus('current')
hwSSHServerSessionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 4, 2, 3)).setObjects(("HUAWEI-SSH-MIB", "hwSSHSessionUserName"), ("HUAWEI-SSH-MIB", "hwSSHSessionConnectType"), ("HUAWEI-SSH-MIB", "hwSSHSessionVer"), ("HUAWEI-SSH-MIB", "hwSSHSessionState"), ("HUAWEI-SSH-MIB", "hwSSHSessionRetry"), ("HUAWEI-SSH-MIB", "hwSSHSessionCtosCipher"), ("HUAWEI-SSH-MIB", "hwSSHSessionStocCipher"), ("HUAWEI-SSH-MIB", "hwSSHSessionCtosHmac"), ("HUAWEI-SSH-MIB", "hwSSHSessionStocHmac"), ("HUAWEI-SSH-MIB", "hwSSHSessionKex"), ("HUAWEI-SSH-MIB", "hwSSHSessionAuthType"), ("HUAWEI-SSH-MIB", "hwSSHSessionServiceType"), ("HUAWEI-SSH-MIB", "hwSSHSessionKeyType"), ("HUAWEI-SSH-MIB", "hwSSHSessionConnectionIndex"), ("HUAWEI-SSH-MIB", "hwSSHSessionCtosCompress"), ("HUAWEI-SSH-MIB", "hwSSHSessionStocCompress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSSHServerSessionGroup = hwSSHServerSessionGroup.setStatus('current')
hwSSHClientGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 4, 2, 4)).setObjects(("HUAWEI-SSH-MIB", "hwSSHFirstTimeAuthEnable"), ("HUAWEI-SSH-MIB", "hwSSHKeepAliveInterval"), ("HUAWEI-SSH-MIB", "hwSSHKeepAliveMaxCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSSHClientGroup = hwSSHClientGroup.setStatus('current')
hwSSHServerInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 4, 2, 5)).setObjects(("HUAWEI-SSH-MIB", "hwSSHServerName"), ("HUAWEI-SSH-MIB", "hwSSHServerAssignKey"), ("HUAWEI-SSH-MIB", "hwSSHServerRowStatus"), ("HUAWEI-SSH-MIB", "hwSSHServerAssignDSAKey"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSSHServerInfoGroup = hwSSHServerInfoGroup.setStatus('current')
hwSSHNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 4, 2, 6)).setObjects(("HUAWEI-SSH-MIB", "hwSSHSftpUserNumExceedMax"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwSSHNotificationGroup = hwSSHNotificationGroup.setStatus('current')
hwRSALocalKeyTable = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 5))
hwRSALocalHostPublicKeyCode = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 5, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 2048))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwRSALocalHostPublicKeyCode.setStatus('current')
hwRSALocalHostPublicKeyFingerprint = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 5, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 60))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwRSALocalHostPublicKeyFingerprint.setStatus('current')
hwRSALocalServerPublicKeyCode = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 5, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 2048))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwRSALocalServerPublicKeyCode.setStatus('current')
hwRSALocalServerPublicKeyFingerprint = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 118, 5, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 60))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwRSALocalServerPublicKeyFingerprint.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-SSH-MIB", hwRSAPublicKeyEntry=hwRSAPublicKeyEntry, hwSSHSessionConnectType=hwSSHSessionConnectType, hwSCPServerEnable=hwSCPServerEnable, hwRSALocalHostPublicKeyCode=hwRSALocalHostPublicKeyCode, hwSSHServerPort=hwSSHServerPort, hwSSHSessionCtosCipher=hwSSHSessionCtosCipher, hwSSHSessionVer=hwSSHSessionVer, hwRSAPublicKeyTable=hwRSAPublicKeyTable, hwSSHServerInfoTable=hwSSHServerInfoTable, hwSftpServerEnable=hwSftpServerEnable, hwSSHUserTable=hwSSHUserTable, hwSSHUserIndex=hwSSHUserIndex, hwRSAPublicKeyCode=hwRSAPublicKeyCode, hwSSHKeepAliveEnable=hwSSHKeepAliveEnable, hwSSHSessionStocHmac=hwSSHSessionStocHmac, hwSSHServerAlarmEnable=hwSSHServerAlarmEnable, hwRSALocalKeyTable=hwRSALocalKeyTable, hwSSHSessionState=hwSSHSessionState, hwSSHSftpUserNumExceedMax=hwSSHSftpUserNumExceedMax, hwRSAPublicKeyName=hwRSAPublicKeyName, hwSSHSessionKex=hwSSHSessionKex, hwSSHServerRetry=hwSSHServerRetry, hwSSHServerTimeOut=hwSSHServerTimeOut, hwRSALocalHostPublicKeyFingerprint=hwRSALocalHostPublicKeyFingerprint, hwSSHUserEntry=hwSSHUserEntry, hwSSHUserGroup=hwSSHUserGroup, hwSSHSessionServiceType=hwSSHSessionServiceType, hwSSHMIBCompliance=hwSSHMIBCompliance, hwSSHSessionAuthType=hwSSHSessionAuthType, hwSSHUserServiceType=hwSSHUserServiceType, hwSSHSessionKeyType=hwSSHSessionKeyType, hwSSHMIBCompliances=hwSSHMIBCompliances, hwSSHFirstTimeAuthEnable=hwSSHFirstTimeAuthEnable, hwSSHServerKeyTimeOut=hwSSHServerKeyTimeOut, hwRSALocalServerPublicKeyFingerprint=hwRSALocalServerPublicKeyFingerprint, hwSftpMaxUserNum=hwSftpMaxUserNum, hwSSHKeepAliveInterval=hwSSHKeepAliveInterval, hwSSHSessionStocCipher=hwSSHSessionStocCipher, hwRSALocalServerPublicKeyCode=hwRSALocalServerPublicKeyCode, hwSftpOnLineUserNum=hwSftpOnLineUserNum, hwSSHNotifications=hwSSHNotifications, hwSSHUserName=hwSSHUserName, hwSSHSessionRetry=hwSSHSessionRetry, hwSSHServerSessionEntry=hwSSHServerSessionEntry, hwSSHUserAuthorizationCMD=hwSSHUserAuthorizationCMD, hwSSH=hwSSH, hwSSHServerGroup=hwSSHServerGroup, hwSSHMIBConformance=hwSSHMIBConformance, hwSSHServerAssignKey=hwSSHServerAssignKey, hwSSHSessionStocCompress=hwSSHSessionStocCompress, hwStelnetServerEnable=hwStelnetServerEnable, hwSSHSessionCtosHmac=hwSSHSessionCtosHmac, hwSSHKeepAliveMaxCount=hwSSHKeepAliveMaxCount, hwSSHServerInfoGroup=hwSSHServerInfoGroup, hwSSHServerComp1x=hwSSHServerComp1x, hwSSHServerSessionTable=hwSSHServerSessionTable, hwRSAPublicKeyFingerprint=hwRSAPublicKeyFingerprint, hwSNetConfServerEnable=hwSNetConfServerEnable, hwSSHUserSftpDirectory=hwSSHUserSftpDirectory, hwSSHSessionIndex=hwSSHSessionIndex, hwSSHSessionUserName=hwSSHSessionUserName, hwSSHServerIndex=hwSSHServerIndex, hwSSHSessionConnectionIndex=hwSSHSessionConnectionIndex, hwSSHClientGroup=hwSSHClientGroup, hwSSHServerSessionGroup=hwSSHServerSessionGroup, hwSSHServerInfoEntry=hwSSHServerInfoEntry, hwSNetConfMaxUserNum=hwSNetConfMaxUserNum, PYSNMP_MODULE_ID=hwSSH, hwSSHClient=hwSSHClient, hwSSHServerAssignDSAKey=hwSSHServerAssignDSAKey, hwSSHUserRowStatus=hwSSHUserRowStatus, hwSSHServer=hwSSHServer, hwSSHServerRowStatus=hwSSHServerRowStatus, hwRSAPublicKeyRowStatus=hwRSAPublicKeyRowStatus, hwSSHServerAssignECCKey=hwSSHServerAssignECCKey, hwSSHSessionCtosCompress=hwSSHSessionCtosCompress, hwSSHServerName=hwSSHServerName, hwSSHUserAssignKeyType=hwSSHUserAssignKeyType, hwSSHMIBGroups=hwSSHMIBGroups, hwSSHUserAuthType=hwSSHUserAuthType, hwSCPMaxUserNum=hwSCPMaxUserNum, hwSSHNotificationGroup=hwSSHNotificationGroup, hwSSHUserAssignKey=hwSSHUserAssignKey)
