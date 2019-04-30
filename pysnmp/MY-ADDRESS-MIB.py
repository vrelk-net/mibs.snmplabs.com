#
# PySNMP MIB module MY-ADDRESS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MY-ADDRESS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:06:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
myMgmt, = mibBuilder.importSymbols("MY-SMI", "myMgmt")
ConfigStatus, IfIndex = mibBuilder.importSymbols("MY-TC", "ConfigStatus", "IfIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, iso, TimeTicks, MibIdentifier, Integer32, Counter32, Bits, ObjectIdentity, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "iso", "TimeTicks", "MibIdentifier", "Integer32", "Counter32", "Bits", "ObjectIdentity", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32")
TextualConvention, RowStatus, TruthValue, TimeStamp, DisplayString, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "TruthValue", "TimeStamp", "DisplayString", "MacAddress")
myAddressMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22))
myAddressMIB.setRevisions(('2002-03-20 00:00',))
if mibBuilder.loadTexts: myAddressMIB.setLastUpdated('200203200000Z')
if mibBuilder.loadTexts: myAddressMIB.setOrganization('D-Link Crop.')
myAddressMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1))
myAddressManagementObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 1))
myAddressNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 2))
myDynamicAddressCurrentNum = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myDynamicAddressCurrentNum.setStatus('current')
myStaticAddressCurrentNum = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myStaticAddressCurrentNum.setStatus('current')
myFilterAddressCurrentNum = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myFilterAddressCurrentNum.setStatus('current')
myAddressAvailableNum = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myAddressAvailableNum.setStatus('current')
myMacAddressTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 1, 5), )
if mibBuilder.loadTexts: myMacAddressTable.setStatus('current')
myMacAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 1, 5, 1), ).setIndexNames((0, "MY-ADDRESS-MIB", "myMacAddressFdbId"), (0, "MY-ADDRESS-MIB", "myMacAddress"))
if mibBuilder.loadTexts: myMacAddressEntry.setStatus('current')
myMacAddressFdbId = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 1, 5, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myMacAddressFdbId.setStatus('current')
myMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 1, 5, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myMacAddress.setStatus('current')
myMacAddressPort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 1, 5, 1, 3), IfIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myMacAddressPort.setStatus('current')
myMacAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("dynamic", 1), ("static", 2), ("filter", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myMacAddressType.setStatus('current')
myMacAddressStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 1, 5, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: myMacAddressStatus.setStatus('current')
myMacNotiGlobalEnabled = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 2, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myMacNotiGlobalEnabled.setStatus('current')
myMacNotificationInterval = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 2, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myMacNotificationInterval.setStatus('current')
myMacNotiHisTableMaxLength = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 2, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 200)).clone(50)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myMacNotiHisTableMaxLength.setStatus('current')
myMacNotiHisTableCurrentLength = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 2, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myMacNotiHisTableCurrentLength.setStatus('current')
myMacNotiHisTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 2, 5), )
if mibBuilder.loadTexts: myMacNotiHisTable.setStatus('current')
myMacNotiHisEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 2, 5, 1), ).setIndexNames((0, "MY-ADDRESS-MIB", "myMacNotiHisIndex"))
if mibBuilder.loadTexts: myMacNotiHisEntry.setStatus('current')
myMacNotiHisIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 2, 5, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: myMacNotiHisIndex.setStatus('current')
myMacNotiHisMacChangedMsg = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 2, 5, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 254))).setMaxAccess("readonly")
if mibBuilder.loadTexts: myMacNotiHisMacChangedMsg.setStatus('current')
myMacNotiHisTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 2, 5, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myMacNotiHisTimestamp.setStatus('current')
myMacNotiIfCfgTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 2, 6), )
if mibBuilder.loadTexts: myMacNotiIfCfgTable.setStatus('current')
myMacNotiIfCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 2, 6, 1), ).setIndexNames((0, "MY-ADDRESS-MIB", "myMacNotiIfIndex"))
if mibBuilder.loadTexts: myMacNotiIfCfgEntry.setStatus('current')
myMacNotiIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 2, 6, 1, 1), IfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myMacNotiIfIndex.setStatus('current')
myIfMacAddrLearntEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 2, 6, 1, 2), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myIfMacAddrLearntEnable.setStatus('current')
myIfMacAddrRemovedEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 1, 2, 6, 1, 3), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myIfMacAddrRemovedEnable.setStatus('current')
myAddressTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 2))
macChangedNotification = NotificationType((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 2, 1)).setObjects(("MY-ADDRESS-MIB", "myMacNotiHisMacChangedMsg"))
if mibBuilder.loadTexts: macChangedNotification.setStatus('current')
myAddressMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 3))
myAddressMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 3, 1))
myAddressMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 3, 2))
myAddressMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 3, 1, 1)).setObjects(("MY-ADDRESS-MIB", "myMacAddressMIBGroup"), ("MY-ADDRESS-MIB", "myAddressNotificationMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    myAddressMIBCompliance = myAddressMIBCompliance.setStatus('current')
myMacAddressMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 3, 2, 1)).setObjects(("MY-ADDRESS-MIB", "myDynamicAddressCurrentNum"), ("MY-ADDRESS-MIB", "myStaticAddressCurrentNum"), ("MY-ADDRESS-MIB", "myFilterAddressCurrentNum"), ("MY-ADDRESS-MIB", "myAddressAvailableNum"), ("MY-ADDRESS-MIB", "myMacAddressFdbId"), ("MY-ADDRESS-MIB", "myMacAddress"), ("MY-ADDRESS-MIB", "myMacAddressPort"), ("MY-ADDRESS-MIB", "myMacAddressType"), ("MY-ADDRESS-MIB", "myMacAddressStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    myMacAddressMIBGroup = myMacAddressMIBGroup.setStatus('current')
myAddressNotificationMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 22, 3, 2, 2)).setObjects(("MY-ADDRESS-MIB", "myMacNotiGlobalEnabled"), ("MY-ADDRESS-MIB", "myMacNotificationInterval"), ("MY-ADDRESS-MIB", "myMacNotiHisTableMaxLength"), ("MY-ADDRESS-MIB", "myMacNotiHisTableCurrentLength"), ("MY-ADDRESS-MIB", "myMacNotiHisIndex"), ("MY-ADDRESS-MIB", "myMacNotiHisMacChangedMsg"), ("MY-ADDRESS-MIB", "myMacNotiHisTimestamp"), ("MY-ADDRESS-MIB", "myMacNotiIfIndex"), ("MY-ADDRESS-MIB", "myIfMacAddrLearntEnable"), ("MY-ADDRESS-MIB", "myIfMacAddrRemovedEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    myAddressNotificationMIBGroup = myAddressNotificationMIBGroup.setStatus('current')
mibBuilder.exportSymbols("MY-ADDRESS-MIB", myMacNotiHisTableCurrentLength=myMacNotiHisTableCurrentLength, myAddressMIBCompliances=myAddressMIBCompliances, myAddressNotificationObjects=myAddressNotificationObjects, myMacNotiIfIndex=myMacNotiIfIndex, myAddressMIBConformance=myAddressMIBConformance, myMacNotiHisIndex=myMacNotiHisIndex, macChangedNotification=macChangedNotification, myMacNotiHisTable=myMacNotiHisTable, myMacNotiHisTimestamp=myMacNotiHisTimestamp, myStaticAddressCurrentNum=myStaticAddressCurrentNum, myAddressTraps=myAddressTraps, myDynamicAddressCurrentNum=myDynamicAddressCurrentNum, myAddressManagementObjects=myAddressManagementObjects, myAddressMIB=myAddressMIB, myMacNotiHisMacChangedMsg=myMacNotiHisMacChangedMsg, myMacNotificationInterval=myMacNotificationInterval, myAddressAvailableNum=myAddressAvailableNum, PYSNMP_MODULE_ID=myAddressMIB, myMacAddress=myMacAddress, myMacAddressTable=myMacAddressTable, myAddressMIBObjects=myAddressMIBObjects, myMacNotiIfCfgTable=myMacNotiIfCfgTable, myMacNotiHisTableMaxLength=myMacNotiHisTableMaxLength, myMacNotiIfCfgEntry=myMacNotiIfCfgEntry, myMacAddressMIBGroup=myMacAddressMIBGroup, myAddressMIBCompliance=myAddressMIBCompliance, myFilterAddressCurrentNum=myFilterAddressCurrentNum, myIfMacAddrLearntEnable=myIfMacAddrLearntEnable, myMacAddressPort=myMacAddressPort, myMacNotiHisEntry=myMacNotiHisEntry, myAddressMIBGroups=myAddressMIBGroups, myMacAddressType=myMacAddressType, myMacAddressFdbId=myMacAddressFdbId, myAddressNotificationMIBGroup=myAddressNotificationMIBGroup, myMacAddressEntry=myMacAddressEntry, myIfMacAddrRemovedEnable=myIfMacAddrRemovedEnable, myMacNotiGlobalEnabled=myMacNotiGlobalEnabled, myMacAddressStatus=myMacAddressStatus)