#
# PySNMP MIB module MY-QOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MY-QOS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:06:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
myMgmt, = mibBuilder.importSymbols("MY-SMI", "myMgmt")
ConfigStatus, IfIndex = mibBuilder.importSymbols("MY-TC", "ConfigStatus", "IfIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter32, ObjectIdentity, iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, NotificationType, Unsigned32, ModuleIdentity, Gauge32, Counter64, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "NotificationType", "Unsigned32", "ModuleIdentity", "Gauge32", "Counter64", "Bits", "Integer32")
DisplayString, TruthValue, TextualConvention, MacAddress, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention", "MacAddress", "RowStatus")
myQoSMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18))
myQoSMIB.setRevisions(('2002-03-20 00:00',))
if mibBuilder.loadTexts: myQoSMIB.setLastUpdated('200203200000Z')
if mibBuilder.loadTexts: myQoSMIB.setOrganization('D-Link Crop.')
myQoSPriorityMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 1))
myQoSGlobalStatus = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myQoSGlobalStatus.setStatus('current')
myPriorityTrafficClassNum = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myPriorityTrafficClassNum.setStatus('current')
myPriorityClassNum = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myPriorityClassNum.setStatus('current')
myPriorityDscpMaxValue = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myPriorityDscpMaxValue.setStatus('current')
myTrafficClassTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 1, 5), )
if mibBuilder.loadTexts: myTrafficClassTable.setStatus('current')
myTrafficClassEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 1, 5, 1), ).setIndexNames((0, "MY-QOS-MIB", "myTrafficClassPriority"))
if mibBuilder.loadTexts: myTrafficClassEntry.setStatus('current')
myTrafficClassPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 1, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myTrafficClassPriority.setStatus('current')
myTrafficClass = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 1, 5, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myTrafficClass.setStatus('current')
myPriorityToDscp = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 1, 5, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myPriorityToDscp.setStatus('current')
myDscpClassTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 1, 6), )
if mibBuilder.loadTexts: myDscpClassTable.setStatus('current')
myDscpClassEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 1, 6, 1), ).setIndexNames((0, "MY-QOS-MIB", "myDscpClass"))
if mibBuilder.loadTexts: myDscpClassEntry.setStatus('current')
myDscpClass = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 1, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myDscpClass.setStatus('current')
myDscpTrafficClassPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 1, 6, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myDscpTrafficClassPriority.setStatus('current')
myPriorityTrafficClassOperMode = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("qos-sp", 1), ("qos-wrr", 2), ("qos-drr", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myPriorityTrafficClassOperMode.setStatus('current')
myPriorityBandWidth = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 1, 8), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myPriorityBandWidth.setStatus('current')
myIfPriorityTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 1, 9), )
if mibBuilder.loadTexts: myIfPriorityTable.setStatus('current')
myIfPriorityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 1, 9, 1), ).setIndexNames((0, "MY-QOS-MIB", "myIfPriorityIfIndex"))
if mibBuilder.loadTexts: myIfPriorityEntry.setStatus('current')
myIfPriorityIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 1, 9, 1, 1), IfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myIfPriorityIfIndex.setStatus('current')
myIfPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 1, 9, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myIfPriority.setStatus('current')
myIfPriTrafficClassOperMode = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 1, 9, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("qos-sp", 1), ("qos-wrr", 2), ("qos-drr", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myIfPriTrafficClassOperMode.setStatus('current')
myIfPriorityBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 1, 9, 1, 4), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myIfPriorityBandwidth.setStatus('current')
myIfPriorityQosTrustMode = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 1, 9, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("not-trust", 1), ("trust-cos", 2), ("trust-dscp", 3), ("trust-ip-precedence", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myIfPriorityQosTrustMode.setStatus('current')
myIpPreClassTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 1, 10), )
if mibBuilder.loadTexts: myIpPreClassTable.setStatus('current')
myIpPreClassEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 1, 10, 1), ).setIndexNames((0, "MY-QOS-MIB", "myIpPreClassPriority"))
if mibBuilder.loadTexts: myIpPreClassEntry.setStatus('current')
myIpPreClassPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 1, 10, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myIpPreClassPriority.setStatus('current')
myIpPreToDscp = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 1, 10, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myIpPreToDscp.setStatus('current')
myIfRateLimitTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 1, 11), )
if mibBuilder.loadTexts: myIfRateLimitTable.setStatus('current')
myIfRateLimitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 1, 11, 1), ).setIndexNames((0, "MY-QOS-MIB", "myIfRateLimitIndex"))
if mibBuilder.loadTexts: myIfRateLimitEntry.setStatus('current')
myIfRateLimitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 1, 11, 1, 1), IfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myIfRateLimitIndex.setStatus('current')
myIfRateLimitInMaxBandWidth = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 1, 11, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myIfRateLimitInMaxBandWidth.setStatus('current')
myIfRateLimitInBurstFlowLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 1, 11, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myIfRateLimitInBurstFlowLimit.setStatus('current')
myIfRateLimitOutMaxBandWidth = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 1, 11, 1, 4), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myIfRateLimitOutMaxBandWidth.setStatus('current')
myIfRateLimitOutBurstFlowLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 1, 11, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myIfRateLimitOutBurstFlowLimit.setStatus('current')
myQoSTrafficClassMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 2))
myQoSTrafficClassTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 2, 1), )
if mibBuilder.loadTexts: myQoSTrafficClassTable.setStatus('current')
myQoSTrafficClassEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 2, 1, 1), ).setIndexNames((0, "MY-QOS-MIB", "myQosClassMapName"))
if mibBuilder.loadTexts: myQoSTrafficClassEntry.setStatus('current')
myQosClassMapName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 2, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: myQosClassMapName.setStatus('current')
myQosClassAclName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myQosClassAclName.setStatus('current')
myQosClassMapEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 2, 1, 1, 3), ConfigStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: myQosClassMapEntryStatus.setStatus('current')
myQoSPoliceMapTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 2, 2), )
if mibBuilder.loadTexts: myQoSPoliceMapTable.setStatus('current')
myQoSPoliceMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 2, 2, 1), ).setIndexNames((0, "MY-QOS-MIB", "myQosPoliceMapName"))
if mibBuilder.loadTexts: myQoSPoliceMapEntry.setStatus('current')
myQosPoliceMapName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 2, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: myQosPoliceMapName.setStatus('current')
myQosPoliceMapEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 2, 2, 1, 2), ConfigStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: myQosPoliceMapEntryStatus.setStatus('current')
myQoSPoliceMapConfTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 2, 3), )
if mibBuilder.loadTexts: myQoSPoliceMapConfTable.setStatus('current')
myQoSPoliceMapConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 2, 3, 1), ).setIndexNames((0, "MY-QOS-MIB", "myQoSPoliceCfgPoliceMapName"), (0, "MY-QOS-MIB", "myQoSPoliceCfgClassMapName"))
if mibBuilder.loadTexts: myQoSPoliceMapConfEntry.setStatus('current')
myQoSPoliceCfgPoliceMapName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 2, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: myQoSPoliceCfgPoliceMapName.setStatus('current')
myQoSPoliceCfgClassMapName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 2, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myQoSPoliceCfgClassMapName.setStatus('current')
myQoSPoliceMapConfMaxBandWidth = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 2, 3, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myQoSPoliceMapConfMaxBandWidth.setStatus('current')
myQoSPoliceMapConfBurstFlowLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 2, 3, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myQoSPoliceMapConfBurstFlowLimit.setStatus('current')
myQoSPoliceMapConfExceedAction = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 2, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("discard", 1), ("modify-dscp", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myQoSPoliceMapConfExceedAction.setStatus('current')
myQoSPoliceMapConfExceedDscp = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 2, 3, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myQoSPoliceMapConfExceedDscp.setStatus('current')
myQoSPoliceMapConfNewDscp = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 2, 3, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myQoSPoliceMapConfNewDscp.setStatus('current')
myQoSPoliceMapCfgEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 2, 3, 1, 8), ConfigStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: myQoSPoliceMapCfgEntryStatus.setStatus('current')
myQoSPoliceMapConfMaxHighBandWidth = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 2, 3, 1, 9), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myQoSPoliceMapConfMaxHighBandWidth.setStatus('current')
myQosPoliceIfExtTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 2, 5), )
if mibBuilder.loadTexts: myQosPoliceIfExtTable.setStatus('current')
myQosPoliceIfExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 2, 5, 1), ).setIndexNames((0, "MY-QOS-MIB", "myQosPoliceIfIndex"))
if mibBuilder.loadTexts: myQosPoliceIfExtEntry.setStatus('current')
myQosPoliceIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 2, 5, 1, 1), IfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: myQosPoliceIfIndex.setStatus('current')
myIfInPoliceMapName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 2, 5, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myIfInPoliceMapName.setStatus('current')
myIfOutPoliceMapName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 2, 5, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: myIfOutPoliceMapName.setStatus('current')
myQoSMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 3))
myQoSMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 3, 1))
myQoSMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 3, 2))
myQoSMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 3, 1, 1)).setObjects(("MY-QOS-MIB", "myQoSPriorityMIBGroup"), ("MY-QOS-MIB", "myQoSTrafficClassMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    myQoSMIBCompliance = myQoSMIBCompliance.setStatus('current')
myQoSPriorityMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 3, 2, 1)).setObjects(("MY-QOS-MIB", "myQoSGlobalStatus"), ("MY-QOS-MIB", "myPriorityTrafficClassNum"), ("MY-QOS-MIB", "myPriorityClassNum"), ("MY-QOS-MIB", "myPriorityDscpMaxValue"), ("MY-QOS-MIB", "myTrafficClassPriority"), ("MY-QOS-MIB", "myTrafficClass"), ("MY-QOS-MIB", "myPriorityToDscp"), ("MY-QOS-MIB", "myDscpClass"), ("MY-QOS-MIB", "myDscpTrafficClassPriority"), ("MY-QOS-MIB", "myPriorityTrafficClassOperMode"), ("MY-QOS-MIB", "myPriorityBandWidth"), ("MY-QOS-MIB", "myIfPriorityIfIndex"), ("MY-QOS-MIB", "myIfPriority"), ("MY-QOS-MIB", "myIfPriTrafficClassOperMode"), ("MY-QOS-MIB", "myIfPriorityBandwidth"), ("MY-QOS-MIB", "myIfPriorityQosTrustMode"), ("MY-QOS-MIB", "myIpPreClassPriority"), ("MY-QOS-MIB", "myIpPreToDscp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    myQoSPriorityMIBGroup = myQoSPriorityMIBGroup.setStatus('current')
myQoSTrafficClassMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 18, 3, 2, 2)).setObjects(("MY-QOS-MIB", "myQosClassMapName"), ("MY-QOS-MIB", "myQosClassAclName"), ("MY-QOS-MIB", "myQosClassMapEntryStatus"), ("MY-QOS-MIB", "myQosPoliceMapName"), ("MY-QOS-MIB", "myQosPoliceMapEntryStatus"), ("MY-QOS-MIB", "myQoSPoliceCfgPoliceMapName"), ("MY-QOS-MIB", "myQoSPoliceCfgClassMapName"), ("MY-QOS-MIB", "myQoSPoliceMapConfMaxBandWidth"), ("MY-QOS-MIB", "myQoSPoliceMapConfExceedAction"), ("MY-QOS-MIB", "myQoSPoliceMapConfExceedDscp"), ("MY-QOS-MIB", "myQoSPoliceMapConfNewDscp"), ("MY-QOS-MIB", "myQoSPoliceMapCfgEntryStatus"), ("MY-QOS-MIB", "myQoSPoliceMapConfMaxHighBandWidth"), ("MY-QOS-MIB", "myQosPoliceIfIndex"), ("MY-QOS-MIB", "myIfInPoliceMapName"), ("MY-QOS-MIB", "myIfOutPoliceMapName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    myQoSTrafficClassMIBGroup = myQoSTrafficClassMIBGroup.setStatus('current')
mibBuilder.exportSymbols("MY-QOS-MIB", myIpPreClassTable=myIpPreClassTable, myQosClassMapName=myQosClassMapName, myQoSPoliceMapEntry=myQoSPoliceMapEntry, myTrafficClass=myTrafficClass, myQoSPoliceMapConfNewDscp=myQoSPoliceMapConfNewDscp, myQoSTrafficClassMIBGroup=myQoSTrafficClassMIBGroup, myIfPriority=myIfPriority, myQoSPriorityMIBGroup=myQoSPriorityMIBGroup, myIfRateLimitOutMaxBandWidth=myIfRateLimitOutMaxBandWidth, myQoSPriorityMIBObjects=myQoSPriorityMIBObjects, myQoSPoliceMapTable=myQoSPoliceMapTable, myQoSPoliceMapConfExceedAction=myQoSPoliceMapConfExceedAction, myTrafficClassTable=myTrafficClassTable, myIpPreClassPriority=myIpPreClassPriority, myIfPriorityQosTrustMode=myIfPriorityQosTrustMode, myIfRateLimitEntry=myIfRateLimitEntry, myIfRateLimitIndex=myIfRateLimitIndex, myQosPoliceMapName=myQosPoliceMapName, myDscpTrafficClassPriority=myDscpTrafficClassPriority, myQoSMIBGroups=myQoSMIBGroups, myTrafficClassPriority=myTrafficClassPriority, myIfRateLimitInBurstFlowLimit=myIfRateLimitInBurstFlowLimit, myQoSPoliceMapConfTable=myQoSPoliceMapConfTable, myTrafficClassEntry=myTrafficClassEntry, myQoSPoliceMapConfBurstFlowLimit=myQoSPoliceMapConfBurstFlowLimit, myQoSPoliceCfgClassMapName=myQoSPoliceCfgClassMapName, myPriorityToDscp=myPriorityToDscp, myPriorityClassNum=myPriorityClassNum, myIfPriorityEntry=myIfPriorityEntry, myQosClassMapEntryStatus=myQosClassMapEntryStatus, myQosPoliceIfExtEntry=myQosPoliceIfExtEntry, myQoSPoliceMapConfEntry=myQoSPoliceMapConfEntry, myQosPoliceMapEntryStatus=myQosPoliceMapEntryStatus, myQoSTrafficClassTable=myQoSTrafficClassTable, myQoSPoliceMapConfMaxBandWidth=myQoSPoliceMapConfMaxBandWidth, myQosClassAclName=myQosClassAclName, myIfRateLimitInMaxBandWidth=myIfRateLimitInMaxBandWidth, myIfPriTrafficClassOperMode=myIfPriTrafficClassOperMode, myIfRateLimitTable=myIfRateLimitTable, myQosPoliceIfIndex=myQosPoliceIfIndex, myPriorityBandWidth=myPriorityBandWidth, myPriorityTrafficClassNum=myPriorityTrafficClassNum, myQoSMIB=myQoSMIB, PYSNMP_MODULE_ID=myQoSMIB, myPriorityDscpMaxValue=myPriorityDscpMaxValue, myDscpClassEntry=myDscpClassEntry, myDscpClass=myDscpClass, myIfPriorityTable=myIfPriorityTable, myIpPreClassEntry=myIpPreClassEntry, myQoSPoliceCfgPoliceMapName=myQoSPoliceCfgPoliceMapName, myIfPriorityBandwidth=myIfPriorityBandwidth, myQoSTrafficClassEntry=myQoSTrafficClassEntry, myQoSPoliceMapConfExceedDscp=myQoSPoliceMapConfExceedDscp, myIfOutPoliceMapName=myIfOutPoliceMapName, myQoSMIBCompliance=myQoSMIBCompliance, myQoSMIBCompliances=myQoSMIBCompliances, myQosPoliceIfExtTable=myQosPoliceIfExtTable, myPriorityTrafficClassOperMode=myPriorityTrafficClassOperMode, myQoSMIBConformance=myQoSMIBConformance, myQoSTrafficClassMIBObjects=myQoSTrafficClassMIBObjects, myQoSPoliceMapConfMaxHighBandWidth=myQoSPoliceMapConfMaxHighBandWidth, myIfPriorityIfIndex=myIfPriorityIfIndex, myDscpClassTable=myDscpClassTable, myIfInPoliceMapName=myIfInPoliceMapName, myIfRateLimitOutBurstFlowLimit=myIfRateLimitOutBurstFlowLimit, myIpPreToDscp=myIpPreToDscp, myQoSPoliceMapCfgEntryStatus=myQoSPoliceMapCfgEntryStatus, myQoSGlobalStatus=myQoSGlobalStatus)
