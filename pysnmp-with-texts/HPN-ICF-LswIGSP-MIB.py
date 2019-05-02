#
# PySNMP MIB module HPN-ICF-LswIGSP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-LswIGSP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:39:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
hpnicflswCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicflswCommon")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter64, Gauge32, ModuleIdentity, TimeTicks, Unsigned32, NotificationType, Integer32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter32, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "Gauge32", "ModuleIdentity", "TimeTicks", "Unsigned32", "NotificationType", "Integer32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter32", "MibIdentifier", "iso")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
hpnicfLswIgmpsnoopingMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7))
hpnicfLswIgmpsnoopingMib.setRevisions(('2001-06-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpnicfLswIgmpsnoopingMib.setRevisionsDescriptions(('',))
if mibBuilder.loadTexts: hpnicfLswIgmpsnoopingMib.setLastUpdated('200106290000Z')
if mibBuilder.loadTexts: hpnicfLswIgmpsnoopingMib.setOrganization('')
if mibBuilder.loadTexts: hpnicfLswIgmpsnoopingMib.setContactInfo('')
if mibBuilder.loadTexts: hpnicfLswIgmpsnoopingMib.setDescription('')
class EnabledStatus(TextualConvention, Integer32):
    description = 'A simple status value for the object.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

hpnicfLswIgmpsnoopingMibObject = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1))
hpnicfIgmpSnoopingStatus = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfIgmpSnoopingStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfIgmpSnoopingStatus.setDescription('Configure to enable IGMP Snooping.')
hpnicfIgmpSnoopingRouterPortAge = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)).clone(105)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfIgmpSnoopingRouterPortAge.setStatus('current')
if mibBuilder.loadTexts: hpnicfIgmpSnoopingRouterPortAge.setDescription('Configure the aging time of the router port.')
hpnicfIgmpSnoopingResponseTime = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 25)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfIgmpSnoopingResponseTime.setStatus('current')
if mibBuilder.loadTexts: hpnicfIgmpSnoopingResponseTime.setDescription('Configure the maximum query response time.')
hpnicfIgmpSnoopingHostTime = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(200, 1000)).clone(260)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfIgmpSnoopingHostTime.setStatus('current')
if mibBuilder.loadTexts: hpnicfIgmpSnoopingHostTime.setDescription('Configure the aging time of the multicast group port.')
hpnicfIgmpSnoopingGroupLimitTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 5), )
if mibBuilder.loadTexts: hpnicfIgmpSnoopingGroupLimitTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfIgmpSnoopingGroupLimitTable.setDescription('The table lists the maximum group number that one interface could do IGMP Snooping.')
hpnicfIgmpSnoopingGroupLimitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 5, 1), ).setIndexNames((0, "HPN-ICF-LswIGSP-MIB", "hpnicfIgmpSnoopingGroupIfIndex"))
if mibBuilder.loadTexts: hpnicfIgmpSnoopingGroupLimitEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfIgmpSnoopingGroupLimitEntry.setDescription('An entry (conceptual row) representing the maximum group number on an interface which IGMP Snooping operation is enabled.')
hpnicfIgmpSnoopingGroupIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 5, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hpnicfIgmpSnoopingGroupIfIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfIgmpSnoopingGroupIfIndex.setDescription('The ifIndex value of the port on which IGMP snooping is enabled.')
hpnicfIgmpSnoopingGroupLimitNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 5, 1, 2), Unsigned32().clone(4294967295)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfIgmpSnoopingGroupLimitNumber.setStatus('current')
if mibBuilder.loadTexts: hpnicfIgmpSnoopingGroupLimitNumber.setDescription('The maxmum group number of IGMP Snooping on a port.')
hpnicfIgmpSnoopingFastLeaveTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 6), )
if mibBuilder.loadTexts: hpnicfIgmpSnoopingFastLeaveTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfIgmpSnoopingFastLeaveTable.setDescription('The table specifies the fast leave status on those ports that do IGMP Snooping.')
hpnicfIgmpSnoopingFastLeaveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 6, 1), ).setIndexNames((0, "HPN-ICF-LswIGSP-MIB", "hpnicfIgmpSnoopingFastLeaveIfIndex"))
if mibBuilder.loadTexts: hpnicfIgmpSnoopingFastLeaveEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfIgmpSnoopingFastLeaveEntry.setDescription('An entry specifies the fast leave status on those ports that do IGMP Snooping.')
hpnicfIgmpSnoopingFastLeaveIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 6, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hpnicfIgmpSnoopingFastLeaveIfIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfIgmpSnoopingFastLeaveIfIndex.setDescription('The ifIndex value of the port on which IGMP snooping is enabled.')
hpnicfIgmpSnoopingFastLeaveStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 6, 1, 2), EnabledStatus().clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfIgmpSnoopingFastLeaveStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfIgmpSnoopingFastLeaveStatus.setDescription('The fast leave status of the port on which IGMP Snooping is enabled.')
hpnicfIgmpSnoopingGroupPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 7), )
if mibBuilder.loadTexts: hpnicfIgmpSnoopingGroupPolicyTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfIgmpSnoopingGroupPolicyTable.setDescription('This is a table specifies the group policy parameter and Vlan ID of the IGMP Snooping port.')
hpnicfIgmpSnoopingGroupPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 7, 1), ).setIndexNames((0, "HPN-ICF-LswIGSP-MIB", "hpnicfIgmpSnoopingGroupPolicyIfIndex"), (0, "HPN-ICF-LswIGSP-MIB", "hpnicfIgmpSnoopingGroupPolicyVlanID"))
if mibBuilder.loadTexts: hpnicfIgmpSnoopingGroupPolicyEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfIgmpSnoopingGroupPolicyEntry.setDescription('An entry representing the group policy parameter and Vlan ID of a port on which IGMP Snooping operation is enabled.')
hpnicfIgmpSnoopingGroupPolicyIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 7, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hpnicfIgmpSnoopingGroupPolicyIfIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfIgmpSnoopingGroupPolicyIfIndex.setDescription('The ifIndex value of the port on which IGMP Snooping is enabled.')
hpnicfIgmpSnoopingGroupPolicyVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 7, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)))
if mibBuilder.loadTexts: hpnicfIgmpSnoopingGroupPolicyVlanID.setStatus('current')
if mibBuilder.loadTexts: hpnicfIgmpSnoopingGroupPolicyVlanID.setDescription('The Vlan ID which the IGMP Snooping port is attached to.')
hpnicfIgmpSnoopingGroupPolicyParameter = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 7, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2000, 2999))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfIgmpSnoopingGroupPolicyParameter.setStatus('current')
if mibBuilder.loadTexts: hpnicfIgmpSnoopingGroupPolicyParameter.setDescription('The ACL Number which is used as the group policy parameter of the IGMP Snooping port.')
hpnicfIgmpSnoopingGroupPolicyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 7, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfIgmpSnoopingGroupPolicyStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfIgmpSnoopingGroupPolicyStatus.setDescription('This object is used to create or delete a row and represent the current status of this row. Now support three state:CreateAndGo,Active,Destroy.')
hpnicfIgmpSnoopingNonFloodingStatus = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 8), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfIgmpSnoopingNonFloodingStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfIgmpSnoopingNonFloodingStatus.setDescription('Configure to disable multicast flooding when no member exists in the destinated group. To use this function,IGMP snooping must be enabled.')
hpnicfIgmpSnoopingVlanStatusTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 9), )
if mibBuilder.loadTexts: hpnicfIgmpSnoopingVlanStatusTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfIgmpSnoopingVlanStatusTable.setDescription('The table used to enable or disable IGMP snooping on the specified VLAN.')
hpnicfIgmpSnoopingVlanStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 9, 1), ).setIndexNames((0, "HPN-ICF-LswIGSP-MIB", "hpnicfIgmpSnoopingVlanID"))
if mibBuilder.loadTexts: hpnicfIgmpSnoopingVlanStatusEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfIgmpSnoopingVlanStatusEntry.setDescription('An entry representing the IGMP snooping status on the specified VLAN.')
hpnicfIgmpSnoopingVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 9, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)))
if mibBuilder.loadTexts: hpnicfIgmpSnoopingVlanID.setStatus('current')
if mibBuilder.loadTexts: hpnicfIgmpSnoopingVlanID.setDescription('An index uniquely identifies on which VLAN IGMP snooping is enabled or disabled. ')
hpnicfIgmpSnoopingVlanEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 9, 1, 2), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfIgmpSnoopingVlanEnabled.setStatus('current')
if mibBuilder.loadTexts: hpnicfIgmpSnoopingVlanEnabled.setDescription('Indicating whether IGMP snooping is enabled on this VLAN.')
hpnicfIgmpSnoopingStatsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 10))
hpnicfRecvIGMPGQueryNum = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 10, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfRecvIGMPGQueryNum.setStatus('current')
if mibBuilder.loadTexts: hpnicfRecvIGMPGQueryNum.setDescription('The statistics of IGMP general query packets received on the device.')
hpnicfRecvIGMPSQueryNum = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 10, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfRecvIGMPSQueryNum.setStatus('current')
if mibBuilder.loadTexts: hpnicfRecvIGMPSQueryNum.setDescription('The statistics of IGMP specific query packets received on the device.')
hpnicfRecvIGMPV1ReportNum = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 10, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfRecvIGMPV1ReportNum.setStatus('current')
if mibBuilder.loadTexts: hpnicfRecvIGMPV1ReportNum.setDescription('The statistics of IGMP V1 report packets received on the device.')
hpnicfRecvIGMPV2ReportNum = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 10, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfRecvIGMPV2ReportNum.setStatus('current')
if mibBuilder.loadTexts: hpnicfRecvIGMPV2ReportNum.setDescription('The statistics of IGMP V2 report packets received on the device.')
hpnicfRecvIGMPLeaveNum = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 10, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfRecvIGMPLeaveNum.setStatus('current')
if mibBuilder.loadTexts: hpnicfRecvIGMPLeaveNum.setDescription('The statistics of IGMP leave packets received on the device.')
hpnicfRecvErrorIGMPPacketNum = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 10, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfRecvErrorIGMPPacketNum.setStatus('current')
if mibBuilder.loadTexts: hpnicfRecvErrorIGMPPacketNum.setDescription('The statistics of error IGMP packets received on the device.')
hpnicfSentIGMPSQueryNum = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 10, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfSentIGMPSQueryNum.setStatus('current')
if mibBuilder.loadTexts: hpnicfSentIGMPSQueryNum.setDescription('The statistics of IGMP specific query packets sent from the device.')
hpnicfIgmpSnoopingClearStats = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 7, 1, 10, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("clear", 1), ("counting", 2))).clone('counting')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfIgmpSnoopingClearStats.setStatus('current')
if mibBuilder.loadTexts: hpnicfIgmpSnoopingClearStats.setDescription('The configuration to clear the statistics of IGMP packets.')
mibBuilder.exportSymbols("HPN-ICF-LswIGSP-MIB", hpnicfIgmpSnoopingFastLeaveIfIndex=hpnicfIgmpSnoopingFastLeaveIfIndex, hpnicfIgmpSnoopingFastLeaveTable=hpnicfIgmpSnoopingFastLeaveTable, hpnicfIgmpSnoopingGroupIfIndex=hpnicfIgmpSnoopingGroupIfIndex, hpnicfRecvIGMPSQueryNum=hpnicfRecvIGMPSQueryNum, hpnicfLswIgmpsnoopingMibObject=hpnicfLswIgmpsnoopingMibObject, hpnicfIgmpSnoopingGroupLimitTable=hpnicfIgmpSnoopingGroupLimitTable, hpnicfIgmpSnoopingHostTime=hpnicfIgmpSnoopingHostTime, hpnicfIgmpSnoopingVlanID=hpnicfIgmpSnoopingVlanID, hpnicfIgmpSnoopingGroupPolicyTable=hpnicfIgmpSnoopingGroupPolicyTable, hpnicfRecvIGMPV2ReportNum=hpnicfRecvIGMPV2ReportNum, PYSNMP_MODULE_ID=hpnicfLswIgmpsnoopingMib, hpnicfIgmpSnoopingFastLeaveStatus=hpnicfIgmpSnoopingFastLeaveStatus, hpnicfRecvErrorIGMPPacketNum=hpnicfRecvErrorIGMPPacketNum, hpnicfRecvIGMPGQueryNum=hpnicfRecvIGMPGQueryNum, hpnicfIgmpSnoopingStatus=hpnicfIgmpSnoopingStatus, hpnicfIgmpSnoopingVlanEnabled=hpnicfIgmpSnoopingVlanEnabled, hpnicfIgmpSnoopingNonFloodingStatus=hpnicfIgmpSnoopingNonFloodingStatus, hpnicfIgmpSnoopingRouterPortAge=hpnicfIgmpSnoopingRouterPortAge, hpnicfIgmpSnoopingGroupPolicyParameter=hpnicfIgmpSnoopingGroupPolicyParameter, hpnicfIgmpSnoopingGroupPolicyStatus=hpnicfIgmpSnoopingGroupPolicyStatus, hpnicfIgmpSnoopingVlanStatusTable=hpnicfIgmpSnoopingVlanStatusTable, hpnicfIgmpSnoopingStatsObjects=hpnicfIgmpSnoopingStatsObjects, hpnicfRecvIGMPLeaveNum=hpnicfRecvIGMPLeaveNum, hpnicfIgmpSnoopingFastLeaveEntry=hpnicfIgmpSnoopingFastLeaveEntry, EnabledStatus=EnabledStatus, hpnicfIgmpSnoopingResponseTime=hpnicfIgmpSnoopingResponseTime, hpnicfIgmpSnoopingGroupPolicyVlanID=hpnicfIgmpSnoopingGroupPolicyVlanID, hpnicfIgmpSnoopingGroupLimitEntry=hpnicfIgmpSnoopingGroupLimitEntry, hpnicfIgmpSnoopingGroupPolicyEntry=hpnicfIgmpSnoopingGroupPolicyEntry, hpnicfRecvIGMPV1ReportNum=hpnicfRecvIGMPV1ReportNum, hpnicfIgmpSnoopingClearStats=hpnicfIgmpSnoopingClearStats, hpnicfIgmpSnoopingVlanStatusEntry=hpnicfIgmpSnoopingVlanStatusEntry, hpnicfIgmpSnoopingGroupLimitNumber=hpnicfIgmpSnoopingGroupLimitNumber, hpnicfLswIgmpsnoopingMib=hpnicfLswIgmpsnoopingMib, hpnicfIgmpSnoopingGroupPolicyIfIndex=hpnicfIgmpSnoopingGroupPolicyIfIndex, hpnicfSentIGMPSQueryNum=hpnicfSentIGMPSQueryNum)