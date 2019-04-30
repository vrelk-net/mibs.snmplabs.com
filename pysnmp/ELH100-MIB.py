#
# PySNMP MIB module ELH100-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELH100-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:45:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity, Counter32, Counter64, Bits, TimeTicks, ModuleIdentity, Unsigned32, enterprises, NotificationType, MibIdentifier, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity", "Counter32", "Counter64", "Bits", "TimeTicks", "ModuleIdentity", "Unsigned32", "enterprises", "NotificationType", "MibIdentifier", "IpAddress", "Integer32")
DisplayString, TextualConvention, PhysAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "PhysAddress")
cabletron = MibIdentifier((1, 3, 6, 1, 4, 1, 52))
cabletronOEM = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 259))
cabletronRepeaters = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 259, 10))
cabletronELH100 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 259, 10, 3))
cabletronELH100Common = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1))
cabletronELH100BasicCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2))
cabletronELH100PerfMonCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 3))
cabletronELH100SwitchCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4))
cabletronELH100BackupCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 5))
cabletronELH100SecurityCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 6))
elh100System = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 1))
elh100MajorVer = MibScalar((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: elh100MajorVer.setStatus('mandatory')
elh100MinorVer = MibScalar((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: elh100MinorVer.setStatus('mandatory')
elh100HardwareVer = MibScalar((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: elh100HardwareVer.setStatus('mandatory')
elh100CommunityMgt = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 2))
elh100CommunityTable = MibTable((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 2, 3), )
if mibBuilder.loadTexts: elh100CommunityTable.setStatus('mandatory')
elh100CommunityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 2, 3, 1), ).setIndexNames((0, "ELH100-MIB", "elh100CommunityIndex"))
if mibBuilder.loadTexts: elh100CommunityEntry.setStatus('mandatory')
elh100CommunityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: elh100CommunityIndex.setStatus('mandatory')
elh100CommunityRowCreation = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elh100CommunityRowCreation.setStatus('mandatory')
elh100CommunityString = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 2, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elh100CommunityString.setStatus('mandatory')
elh100CommunityStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("invalid", 1), ("readOnly", 2), ("readWrite", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elh100CommunityStatus.setStatus('mandatory')
elh100TrapManagerMgt = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 3))
elh100TrapManagerTable = MibTable((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 3, 2), )
if mibBuilder.loadTexts: elh100TrapManagerTable.setStatus('mandatory')
elh100TrapMgtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 3, 2, 1), ).setIndexNames((0, "ELH100-MIB", "elh100TrapMgtIndex"))
if mibBuilder.loadTexts: elh100TrapMgtEntry.setStatus('mandatory')
elh100TrapMgtIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: elh100TrapMgtIndex.setStatus('mandatory')
elh100TrapMgtRowCreation = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elh100TrapMgtRowCreation.setStatus('mandatory')
elh100TrapMgtCommunityString = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 3, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elh100TrapMgtCommunityString.setStatus('mandatory')
elh100TrapMgtIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 3, 2, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elh100TrapMgtIpAddress.setStatus('mandatory')
elh100DownloadMgt = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 4))
elh100DownloadServerIP = MibScalar((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 4, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elh100DownloadServerIP.setStatus('mandatory')
elh100DownloadFilename = MibScalar((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 4, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elh100DownloadFilename.setStatus('mandatory')
elh100DownloadMode = MibScalar((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 4, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("permanent", 1), ("temporary", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elh100DownloadMode.setStatus('mandatory')
elh100DownloadAction = MibScalar((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 4, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("run", 1), ("noRun", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elh100DownloadAction.setStatus('mandatory')
elh100Restart = MibScalar((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: elh100Restart.setStatus('mandatory')
cabletronELH100StackInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 1))
stackInusedIP = MibScalar((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stackInusedIP.setStatus('mandatory')
stackInusedNetMask = MibScalar((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stackInusedNetMask.setStatus('mandatory')
stackInusedGateway = MibScalar((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stackInusedGateway.setStatus('mandatory')
stackBootpIP = MibScalar((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stackBootpIP.setStatus('mandatory')
stackTemporalIP = MibScalar((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stackTemporalIP.setStatus('mandatory')
stackTemporalNetMask = MibScalar((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stackTemporalNetMask.setStatus('mandatory')
stackTemporalGateway = MibScalar((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 1, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stackTemporalGateway.setStatus('mandatory')
stackBootpEnable = MibScalar((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable-bootp", 1), ("enable-bootp", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stackBootpEnable.setStatus('mandatory')
ipInformationReset = MibScalar((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noReset", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipInformationReset.setStatus('mandatory')
stackHealthMonitor = MibScalar((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(256, 256)).setFixedLength(256)).setMaxAccess("readonly")
if mibBuilder.loadTexts: stackHealthMonitor.setStatus('mandatory')
cabletronELH100AgentInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 2))
nicAttachSegment = MibScalar((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 2, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nicAttachSegment.setStatus('mandatory')
serialNumberTable = MibTable((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 2, 2), )
if mibBuilder.loadTexts: serialNumberTable.setStatus('mandatory')
serialNumberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 2, 2, 1), ).setIndexNames((0, "ELH100-MIB", "sNIndex"))
if mibBuilder.loadTexts: serialNumberEntry.setStatus('mandatory')
sNIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sNIndex.setStatus('mandatory')
serialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 2, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialNumber.setStatus('mandatory')
sNCurrentUnitID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 2, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sNCurrentUnitID.setStatus('mandatory')
telnetMaxSessions = MibScalar((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: telnetMaxSessions.setStatus('mandatory')
telnetAutoLogoutEnable = MibScalar((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: telnetAutoLogoutEnable.setStatus('mandatory')
telnetAutoLogoutTimeout = MibScalar((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 99))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: telnetAutoLogoutTimeout.setStatus('mandatory')
vT100RefreshInterval = MibScalar((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(5, 30, 60, 120, 180, 300))).clone(namedValues=NamedValues(("seconds5", 5), ("seconds30", 30), ("seconds60", 60), ("seconds120", 120), ("seconds180", 180), ("seconds300", 300)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vT100RefreshInterval.setStatus('mandatory')
cabletronELH100gGroupInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 3))
groupTable = MibTable((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 3, 1), )
if mibBuilder.loadTexts: groupTable.setStatus('mandatory')
groupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 3, 1, 1), ).setIndexNames((0, "ELH100-MIB", "groupID"))
if mibBuilder.loadTexts: groupEntry.setStatus('mandatory')
groupID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: groupID.setStatus('mandatory')
groupType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("notPresent", 1), ("unknown", 2), ("elh100-12tx", 3), ("elh100-24tx", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: groupType.setStatus('mandatory')
groupCounterReset = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noReset", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: groupCounterReset.setStatus('mandatory')
mgmtModuleStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notPresent", 1), ("active", 2), ("standby", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgmtModuleStatus.setStatus('mandatory')
mgmtModuleDatabaseVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 3, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mgmtModuleDatabaseVersion.setStatus('mandatory')
switchModuleType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("notPresent", 1), ("unknown", 2), ("internalSwitch10-100", 3), ("mediaTX-10-100", 4), ("mediaFX-SC", 5), ("mediaFX-ST", 6), ("switchMediaTX-10-100", 7), ("switchMediaFX-SC", 8), ("switchMediaFX-ST", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchModuleType.setStatus('mandatory')
switchModuleActive = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("active", 1), ("notActive", 2), ("notApplicable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchModuleActive.setStatus('mandatory')
backplaneTable = MibTable((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 3, 2), )
if mibBuilder.loadTexts: backplaneTable.setStatus('mandatory')
backplaneEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 3, 2, 1), ).setIndexNames((0, "ELH100-MIB", "backplaneGroupID"), (0, "ELH100-MIB", "backplaneSegmentID"))
if mibBuilder.loadTexts: backplaneEntry.setStatus('mandatory')
backplaneGroupID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: backplaneGroupID.setStatus('mandatory')
backplaneSegmentID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(10, 100))).clone(namedValues=NamedValues(("tenMbps", 10), ("oneHundredMbps", 100)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: backplaneSegmentID.setStatus('mandatory')
backplaneIsolated = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("isolated", 1), ("attached", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backplaneIsolated.setStatus('mandatory')
cabletronELH100PortInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 4))
portTable = MibTable((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 4, 1), )
if mibBuilder.loadTexts: portTable.setStatus('mandatory')
portEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 4, 1, 1), ).setIndexNames((0, "ELH100-MIB", "portGroupID"), (0, "ELH100-MIB", "portID"))
if mibBuilder.loadTexts: portEntry.setStatus('mandatory')
portGroupID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portGroupID.setStatus('mandatory')
portID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 4, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portID.setStatus('mandatory')
portLinkSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 10, 100))).clone(namedValues=NamedValues(("noLink", 1), ("tenMbps", 10), ("oneHundredMbps", 100)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portLinkSpeed.setStatus('mandatory')
portSpeedConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 2, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 10, 100))).clone(namedValues=NamedValues(("autoNegotiate", 1), ("tenMbps", 10), ("oneHundredMbps", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portSpeedConfig.setStatus('mandatory')
cabletronELH100PerfMonAgentInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 3, 1))
perfMonAgentCRCErrors = MibScalar((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: perfMonAgentCRCErrors.setStatus('mandatory')
perfMonAgentAlignmentErrors = MibScalar((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: perfMonAgentAlignmentErrors.setStatus('mandatory')
perfMonAgentCollisions = MibScalar((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: perfMonAgentCollisions.setStatus('mandatory')
perfMonAgentTotalPortIsolates = MibScalar((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: perfMonAgentTotalPortIsolates.setStatus('mandatory')
perfMonAgentSymbolErrors = MibScalar((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: perfMonAgentSymbolErrors.setStatus('mandatory')
cabletronELH100SwitchInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 1))
switchPortTable = MibTable((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 1, 1), )
if mibBuilder.loadTexts: switchPortTable.setStatus('mandatory')
switchPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 1, 1, 1), ).setIndexNames((0, "ELH100-MIB", "switchPortGroupID"), (0, "ELH100-MIB", "switchPortID"))
if mibBuilder.loadTexts: switchPortEntry.setStatus('mandatory')
switchPortGroupID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchPortGroupID.setStatus('mandatory')
switchPortID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchPortID.setStatus('mandatory')
switchPortAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("notApplicable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: switchPortAdminStatus.setStatus('mandatory')
switchPortSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 10, 100))).clone(namedValues=NamedValues(("noLink", 1), ("tenMbps", 10), ("oneHundredMbps", 100)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchPortSpeed.setStatus('mandatory')
switchPortDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("halfDuplex", 1), ("fullDuplex", 2), ("notApplicable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchPortDuplex.setStatus('mandatory')
switchPortLink = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("link", 1), ("noLink", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchPortLink.setStatus('mandatory')
cabletronELH100SwitchStatsInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 2))
switchPortStatsTable = MibTable((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 2, 1), )
if mibBuilder.loadTexts: switchPortStatsTable.setStatus('mandatory')
switchPortStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 2, 1, 1), ).setIndexNames((0, "ELH100-MIB", "switchPortStatsGroupID"), (0, "ELH100-MIB", "switchPortStatsID"))
if mibBuilder.loadTexts: switchPortStatsEntry.setStatus('mandatory')
switchPortStatsGroupID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchPortStatsGroupID.setStatus('mandatory')
switchPortStatsID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchPortStatsID.setStatus('mandatory')
switchPortReadableFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchPortReadableFrames.setStatus('mandatory')
switchPortReadableOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchPortReadableOctets.setStatus('mandatory')
switchPortFCSErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchPortFCSErrors.setStatus('mandatory')
switchPortAlignmentErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchPortAlignmentErrors.setStatus('mandatory')
switchPortFramesTooLong = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchPortFramesTooLong.setStatus('mandatory')
switchPortShortEvents = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchPortShortEvents.setStatus('mandatory')
switchPortRunts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchPortRunts.setStatus('mandatory')
switchPortCollisions = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 2, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchPortCollisions.setStatus('mandatory')
switchPortLateEvents = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 2, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchPortLateEvents.setStatus('mandatory')
switchPortVeryLongEvents = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 2, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchPortVeryLongEvents.setStatus('mandatory')
switchPortDataRateMismatches = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 2, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchPortDataRateMismatches.setStatus('mandatory')
switchPortAutoPartitions = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 2, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchPortAutoPartitions.setStatus('mandatory')
switchPortBroadcastPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 2, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchPortBroadcastPackets.setStatus('mandatory')
switchPortMulticastPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 2, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchPortMulticastPackets.setStatus('mandatory')
switchPortIsolates = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 4, 2, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: switchPortIsolates.setStatus('mandatory')
cabletronELH100BackupInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 5, 1))
backupPortTable = MibTable((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 5, 1, 1), )
if mibBuilder.loadTexts: backupPortTable.setStatus('mandatory')
backupPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 5, 1, 1, 1), ).setIndexNames((0, "ELH100-MIB", "backupIndex"))
if mibBuilder.loadTexts: backupPortEntry.setStatus('mandatory')
backupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 5, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 72))).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupIndex.setStatus('mandatory')
backupPriPortGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 5, 1, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupPriPortGroup.setStatus('mandatory')
backupPriPortPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 5, 1, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupPriPortPort.setStatus('mandatory')
backupSecPortGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 5, 1, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupSecPortGroup.setStatus('mandatory')
backupSecPortPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 5, 1, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupSecPortPort.setStatus('mandatory')
backupPortAction = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 5, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("inactive", 1), ("active", 2), ("standby", 3), ("backup", 4), ("invalid", 5), ("delete", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: backupPortAction.setStatus('mandatory')
cabletronELH100SecurityInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 6, 1))
securityTable = MibTable((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 6, 1, 1), )
if mibBuilder.loadTexts: securityTable.setStatus('mandatory')
securityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 6, 1, 1, 1), ).setIndexNames((0, "ELH100-MIB", "securityGroupID"), (0, "ELH100-MIB", "securityPortID"))
if mibBuilder.loadTexts: securityEntry.setStatus('mandatory')
securityGroupID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 6, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: securityGroupID.setStatus('mandatory')
securityPortID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 6, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: securityPortID.setStatus('mandatory')
securityAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 6, 1, 1, 1, 3), PhysAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: securityAddr.setStatus('mandatory')
securityAutoLearnAction = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 6, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("inactive", 1), ("active", 2), ("learned", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: securityAutoLearnAction.setStatus('mandatory')
securityEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 259, 10, 3, 6, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inactive", 1), ("warningAndDisable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: securityEnable.setStatus('mandatory')
mibBuilder.exportSymbols("ELH100-MIB", elh100System=elh100System, telnetMaxSessions=telnetMaxSessions, elh100TrapMgtIpAddress=elh100TrapMgtIpAddress, portSpeedConfig=portSpeedConfig, securityEnable=securityEnable, telnetAutoLogoutEnable=telnetAutoLogoutEnable, switchPortEntry=switchPortEntry, elh100CommunityString=elh100CommunityString, groupTable=groupTable, groupType=groupType, elh100TrapMgtIndex=elh100TrapMgtIndex, switchPortTable=switchPortTable, cabletronELH100BackupInfo=cabletronELH100BackupInfo, switchPortReadableOctets=switchPortReadableOctets, perfMonAgentTotalPortIsolates=perfMonAgentTotalPortIsolates, cabletronELH100SecurityInfo=cabletronELH100SecurityInfo, switchPortStatsEntry=switchPortStatsEntry, elh100DownloadAction=elh100DownloadAction, cabletronELH100AgentInfo=cabletronELH100AgentInfo, switchPortMulticastPackets=switchPortMulticastPackets, elh100DownloadMgt=elh100DownloadMgt, backplaneGroupID=backplaneGroupID, cabletronELH100SwitchCapability=cabletronELH100SwitchCapability, elh100CommunityMgt=elh100CommunityMgt, elh100CommunityIndex=elh100CommunityIndex, cabletron=cabletron, stackBootpIP=stackBootpIP, switchPortDataRateMismatches=switchPortDataRateMismatches, switchPortID=switchPortID, cabletronELH100StackInfo=cabletronELH100StackInfo, securityAutoLearnAction=securityAutoLearnAction, switchPortAdminStatus=switchPortAdminStatus, cabletronELH100PerfMonCapability=cabletronELH100PerfMonCapability, switchPortReadableFrames=switchPortReadableFrames, cabletronELH100PortInfo=cabletronELH100PortInfo, groupCounterReset=groupCounterReset, backupSecPortGroup=backupSecPortGroup, switchPortIsolates=switchPortIsolates, portID=portID, cabletronELH100SwitchInfo=cabletronELH100SwitchInfo, switchPortFCSErrors=switchPortFCSErrors, stackInusedNetMask=stackInusedNetMask, switchPortShortEvents=switchPortShortEvents, stackInusedGateway=stackInusedGateway, switchPortAutoPartitions=switchPortAutoPartitions, elh100MinorVer=elh100MinorVer, elh100HardwareVer=elh100HardwareVer, switchModuleType=switchModuleType, switchPortLateEvents=switchPortLateEvents, backplaneEntry=backplaneEntry, cabletronELH100SecurityCapability=cabletronELH100SecurityCapability, mgmtModuleDatabaseVersion=mgmtModuleDatabaseVersion, portTable=portTable, switchPortGroupID=switchPortGroupID, perfMonAgentCollisions=perfMonAgentCollisions, backupPriPortPort=backupPriPortPort, switchPortSpeed=switchPortSpeed, elh100TrapMgtEntry=elh100TrapMgtEntry, switchPortDuplex=switchPortDuplex, elh100CommunityTable=elh100CommunityTable, switchPortVeryLongEvents=switchPortVeryLongEvents, backupPortEntry=backupPortEntry, elh100CommunityStatus=elh100CommunityStatus, elh100DownloadServerIP=elh100DownloadServerIP, sNIndex=sNIndex, elh100TrapManagerMgt=elh100TrapManagerMgt, mgmtModuleStatus=mgmtModuleStatus, stackBootpEnable=stackBootpEnable, securityPortID=securityPortID, nicAttachSegment=nicAttachSegment, cabletronRepeaters=cabletronRepeaters, cabletronELH100gGroupInfo=cabletronELH100gGroupInfo, backplaneTable=backplaneTable, perfMonAgentCRCErrors=perfMonAgentCRCErrors, backplaneIsolated=backplaneIsolated, elh100CommunityEntry=elh100CommunityEntry, groupEntry=groupEntry, cabletronOEM=cabletronOEM, perfMonAgentSymbolErrors=perfMonAgentSymbolErrors, switchPortStatsTable=switchPortStatsTable, elh100Restart=elh100Restart, switchPortStatsID=switchPortStatsID, switchPortLink=switchPortLink, perfMonAgentAlignmentErrors=perfMonAgentAlignmentErrors, portLinkSpeed=portLinkSpeed, backupPriPortGroup=backupPriPortGroup, backupSecPortPort=backupSecPortPort, serialNumberEntry=serialNumberEntry, elh100TrapMgtCommunityString=elh100TrapMgtCommunityString, switchPortStatsGroupID=switchPortStatsGroupID, securityTable=securityTable, stackTemporalGateway=stackTemporalGateway, stackHealthMonitor=stackHealthMonitor, cabletronELH100SwitchStatsInfo=cabletronELH100SwitchStatsInfo, backplaneSegmentID=backplaneSegmentID, groupID=groupID, elh100CommunityRowCreation=elh100CommunityRowCreation, backupIndex=backupIndex, switchPortFramesTooLong=switchPortFramesTooLong, vT100RefreshInterval=vT100RefreshInterval, backupPortAction=backupPortAction, securityAddr=securityAddr, securityEntry=securityEntry, cabletronELH100PerfMonAgentInfo=cabletronELH100PerfMonAgentInfo, ipInformationReset=ipInformationReset, telnetAutoLogoutTimeout=telnetAutoLogoutTimeout, elh100TrapMgtRowCreation=elh100TrapMgtRowCreation, switchPortBroadcastPackets=switchPortBroadcastPackets, switchPortRunts=switchPortRunts, elh100TrapManagerTable=elh100TrapManagerTable, stackTemporalIP=stackTemporalIP, switchPortCollisions=switchPortCollisions, sNCurrentUnitID=sNCurrentUnitID, elh100MajorVer=elh100MajorVer, serialNumber=serialNumber, cabletronELH100BackupCapability=cabletronELH100BackupCapability, cabletronELH100Common=cabletronELH100Common, elh100DownloadFilename=elh100DownloadFilename, serialNumberTable=serialNumberTable, switchModuleActive=switchModuleActive, switchPortAlignmentErrors=switchPortAlignmentErrors, backupPortTable=backupPortTable, cabletronELH100BasicCapability=cabletronELH100BasicCapability, securityGroupID=securityGroupID, stackTemporalNetMask=stackTemporalNetMask, elh100DownloadMode=elh100DownloadMode, cabletronELH100=cabletronELH100, portEntry=portEntry, stackInusedIP=stackInusedIP, portGroupID=portGroupID)
