#
# PySNMP MIB module NOKIA-IPSO-LBCLUSTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NOKIA-IPSO-LBCLUSTER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:13:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ipsoProducts, = mibBuilder.importSymbols("NOKIA-IPSO-REGISTRATION-MIB", "ipsoProducts")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Integer32, ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32, Bits, iso, Gauge32, ModuleIdentity, TimeTicks, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Integer32", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32", "Bits", "iso", "Gauge32", "ModuleIdentity", "TimeTicks", "Counter64", "Counter32")
TimeStamp, MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "MacAddress", "TextualConvention", "DisplayString")
ipsoLBClusterMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 94, 1, 21, 5))
ipsoLBClusterMIB.setRevisions(('1901-05-14 00:00',))
if mibBuilder.loadTexts: ipsoLBClusterMIB.setLastUpdated('0105140000Z')
if mibBuilder.loadTexts: ipsoLBClusterMIB.setOrganization('Nokia IPRG')
ipsoLBClusterInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1))
ipsoLBClusterNodeSpecificInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2))
ipsoLBClusterNotificationGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 3))
ipsoLBNumClusters = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipsoLBNumClusters.setStatus('current')
ipsoLBClusterInfoTable = MibTable((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 2), ).setIndexNames((0, "NOKIA-IPSO-LBCLUSTER-MIB", "ClusterIndex"))
if mibBuilder.loadTexts: ipsoLBClusterInfoTable.setStatus('current')
ipsoLBClusterInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 2, 1), )
if mibBuilder.loadTexts: ipsoLBClusterInfoEntry.setStatus('current')
clusterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterIndex.setStatus('current')
clusterID = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterID.setStatus('current')
clusterNumMembers = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterNumMembers.setStatus('current')
clusterNumInterfaces = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterNumInterfaces.setStatus('current')
clusterUpTimeAtJoin = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 2, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterUpTimeAtJoin.setStatus('current')
systemUpTimeAtJoin = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 2, 1, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemUpTimeAtJoin.setStatus('current')
clusterTotalBuckets = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterTotalBuckets.setStatus('current')
clusterBucketsAssigned = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterBucketsAssigned.setStatus('current')
ipsoLBClusterAddressTable = MibTable((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 3), ).setIndexNames((0, "NOKIA-IPSO-LBCLUSTER-MIB", "ClusterIndex"), (0, "NOKIA-IPSO-LBCLUSTER-MIB", "ClusterAddress"))
if mibBuilder.loadTexts: ipsoLBClusterAddressTable.setStatus('current')
ipsoLBClusterAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 3, 1), )
if mibBuilder.loadTexts: ipsoLBClusterAddressEntry.setStatus('current')
clusterIndex2 = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterIndex2.setStatus('current')
clusterAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 3, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterAddress.setStatus('current')
clusterMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 3, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterMACAddress.setStatus('current')
ipsoLBClusterMemberTable = MibTable((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 4), ).setIndexNames((0, "NOKIA-IPSO-LBCLUSTER-MIB", "ClusterIndex"), (0, "NOKIA-IPSO-LBCLUSTER-MIB", "MemberID"))
if mibBuilder.loadTexts: ipsoLBClusterMemberTable.setStatus('current')
ipsoLBClusterMemberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 4, 1), )
if mibBuilder.loadTexts: ipsoLBClusterMemberEntry.setStatus('current')
clusterIndex3 = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterIndex3.setStatus('current')
memberID = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memberID.setStatus('current')
memberPercentageBucketsAssigned = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memberPercentageBucketsAssigned.setStatus('current')
memberRating = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 4, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memberRating.setStatus('current')
memberPrimaryAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 1, 4, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memberPrimaryAddress.setStatus('current')
ipsoLBClusterNodeSpecificTable = MibTable((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 1), ).setIndexNames((0, "NOKIA-IPSO-LBCLUSTER-MIB", "ClusterIndex"))
if mibBuilder.loadTexts: ipsoLBClusterNodeSpecificTable.setStatus('current')
ipsoLBClusterNodeSpecificEntry = MibTableRow((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 1, 1), )
if mibBuilder.loadTexts: ipsoLBClusterNodeSpecificEntry.setStatus('current')
clusterIndex4 = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterIndex4.setStatus('current')
memberID2 = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memberID2.setStatus('current')
percentageBucketsAssigned = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: percentageBucketsAssigned.setStatus('current')
memberMode = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("uninitialized", 1), ("initialized", 2), ("joining", 3), ("becomingmaster", 4), ("master", 5), ("member", 6), ("unknown", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: memberMode.setStatus('current')
memberRating2 = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memberRating2.setStatus('current')
memberPrimaryAddress2 = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 1, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memberPrimaryAddress2.setStatus('current')
ipsoLBClusterNodeSpecificInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 2), ).setIndexNames((0, "NOKIA-IPSO-LBCLUSTER-MIB", "ClusterIndex"), (0, "NOKIA-IPSO-LBCLUSTER-MIB", "ifIndex"))
if mibBuilder.loadTexts: ipsoLBClusterNodeSpecificInterfaceTable.setStatus('current')
ipsoLBClusterNodeSpecificInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 2, 1), )
if mibBuilder.loadTexts: ipsoLBClusterNodeSpecificInterfaceEntry.setStatus('current')
clusterIndex5 = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterIndex5.setStatus('current')
memberID3 = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memberID3.setStatus('current')
ifIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 2, 1, 3), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifIndex.setStatus('current')
clusterIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterIPAddress.setStatus('current')
clusterNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 2, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterNetMask.setStatus('current')
clusterBroadcastAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 2, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clusterBroadcastAddress.setStatus('current')
realIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 2, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: realIPAddress.setStatus('current')
masterIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 2, 2, 1, 8), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: masterIPAddress.setStatus('current')
ipsoLBMemberJoinRejectReason = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 3, 0), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fewinterface", 1), ("illegallicence", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ipsoLBMemberJoinRejectReason.setStatus('current')
ipsoLBClusterNewMasterReason = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("oldMasterHelloTimeout", 1), ("iamBetterMaster", 2), ("initalizedAsMaster", 3), ("unknown", 4)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ipsoLBClusterNewMasterReason.setStatus('current')
ipsoLBClusterMemberJoin = NotificationType((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 3, 2)).setObjects(("NOKIA-IPSO-LBCLUSTER-MIB", "clusterID"), ("NOKIA-IPSO-LBCLUSTER-MIB", "memberID"), ("NOKIA-IPSO-LBCLUSTER-MIB", "ipsoMemberIPAddress"))
if mibBuilder.loadTexts: ipsoLBClusterMemberJoin.setStatus('current')
ipsoLBClusterMemberLeft = NotificationType((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 3, 3)).setObjects(("NOKIA-IPSO-LBCLUSTER-MIB", "clusterID"), ("NOKIA-IPSO-LBCLUSTER-MIB", "memberID"), ("NOKIA-IPSO-LBCLUSTER-MIB", "ipsoMemberIPAddress"))
if mibBuilder.loadTexts: ipsoLBClusterMemberLeft.setStatus('current')
ipsoLBClusterNewMaster = NotificationType((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 3, 4)).setObjects(("NOKIA-IPSO-LBCLUSTER-MIB", "clusterID"), ("NOKIA-IPSO-LBCLUSTER-MIB", "ipsoLBClusterNewMasterReason"))
if mibBuilder.loadTexts: ipsoLBClusterNewMaster.setStatus('current')
ipsoLBJoinReject = NotificationType((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 3, 5)).setObjects(("NOKIA-IPSO-LBCLUSTER-MIB", "clusterID"), ("NOKIA-IPSO-LBCLUSTER-MIB", "ipsoMemberIPAddress"), ("NOKIA-IPSO-LBCLUSTER-MIB", "ipsoMemberRejectErcode"), ("NOKIA-IPSO-LBCLUSTER-MIB", "ipsoMemberRejectWrongIntf"), ("NOKIA-IPSO-LBCLUSTER-MIB", "ipsoMemberRejectprimaryintf"), ("NOKIA-IPSO-LBCLUSTER-MIB", "ipsoMemberRejectCip"), ("NOKIA-IPSO-LBCLUSTER-MIB", "ipsoMemberRejectHash"))
if mibBuilder.loadTexts: ipsoLBJoinReject.setStatus('current')
ipsoMemberRejectErcode = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 3, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(55, 22, 65, 61, 6))).clone(namedValues=NamedValues(("internalerroronmaster", 55), ("numberofmembersclustercansupportexceeded", 22), ("nodeunreachableononeoftheselectedinterfaces", 65), ("protocolversionmismatch", 61), ("configurationmismatch", 6)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ipsoMemberRejectErcode.setStatus('current')
ipsoMemberRejectWrongIntf = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 3, 7), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ipsoMemberRejectWrongIntf.setStatus('current')
ipsoMemberRejectprimaryintf = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 3, 8), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ipsoMemberRejectprimaryintf.setStatus('current')
ipsoMemberRejectCip = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 3, 9), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ipsoMemberRejectCip.setStatus('current')
ipsoMemberRejectHash = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 3, 10), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ipsoMemberRejectHash.setStatus('current')
ipsoMemberIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 21, 5, 3, 11), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: ipsoMemberIPAddress.setStatus('current')
mibBuilder.exportSymbols("NOKIA-IPSO-LBCLUSTER-MIB", clusterBucketsAssigned=clusterBucketsAssigned, ipsoLBClusterNodeSpecificTable=ipsoLBClusterNodeSpecificTable, clusterIndex5=clusterIndex5, memberID2=memberID2, PYSNMP_MODULE_ID=ipsoLBClusterMIB, memberPrimaryAddress2=memberPrimaryAddress2, ipsoMemberRejectCip=ipsoMemberRejectCip, clusterIndex2=clusterIndex2, clusterBroadcastAddress=clusterBroadcastAddress, ipsoLBClusterMemberEntry=ipsoLBClusterMemberEntry, percentageBucketsAssigned=percentageBucketsAssigned, clusterIndex3=clusterIndex3, ipsoLBClusterNewMasterReason=ipsoLBClusterNewMasterReason, clusterIPAddress=clusterIPAddress, ipsoMemberIPAddress=ipsoMemberIPAddress, ipsoLBClusterInfoTable=ipsoLBClusterInfoTable, clusterNumInterfaces=clusterNumInterfaces, ipsoLBClusterNotificationGroup=ipsoLBClusterNotificationGroup, ipsoLBClusterMIB=ipsoLBClusterMIB, ipsoLBClusterNodeSpecificInfo=ipsoLBClusterNodeSpecificInfo, clusterMACAddress=clusterMACAddress, memberRating=memberRating, ipsoLBClusterNodeSpecificInterfaceEntry=ipsoLBClusterNodeSpecificInterfaceEntry, ipsoMemberRejectErcode=ipsoMemberRejectErcode, ipsoLBClusterNewMaster=ipsoLBClusterNewMaster, ipsoLBJoinReject=ipsoLBJoinReject, ipsoMemberRejectHash=ipsoMemberRejectHash, clusterNumMembers=clusterNumMembers, ipsoLBNumClusters=ipsoLBNumClusters, ipsoLBClusterAddressEntry=ipsoLBClusterAddressEntry, ipsoMemberRejectprimaryintf=ipsoMemberRejectprimaryintf, ipsoLBMemberJoinRejectReason=ipsoLBMemberJoinRejectReason, clusterTotalBuckets=clusterTotalBuckets, clusterNetMask=clusterNetMask, ipsoLBClusterNodeSpecificEntry=ipsoLBClusterNodeSpecificEntry, ipsoLBClusterInfoEntry=ipsoLBClusterInfoEntry, memberID3=memberID3, ipsoLBClusterNodeSpecificInterfaceTable=ipsoLBClusterNodeSpecificInterfaceTable, clusterUpTimeAtJoin=clusterUpTimeAtJoin, ifIndex=ifIndex, memberPercentageBucketsAssigned=memberPercentageBucketsAssigned, ipsoLBClusterMemberLeft=ipsoLBClusterMemberLeft, ipsoLBClusterInfo=ipsoLBClusterInfo, ipsoLBClusterMemberTable=ipsoLBClusterMemberTable, clusterIndex4=clusterIndex4, realIPAddress=realIPAddress, ipsoLBClusterMemberJoin=ipsoLBClusterMemberJoin, memberMode=memberMode, memberRating2=memberRating2, systemUpTimeAtJoin=systemUpTimeAtJoin, ipsoMemberRejectWrongIntf=ipsoMemberRejectWrongIntf, clusterID=clusterID, masterIPAddress=masterIPAddress, ipsoLBClusterAddressTable=ipsoLBClusterAddressTable, memberID=memberID, memberPrimaryAddress=memberPrimaryAddress, clusterIndex=clusterIndex, clusterAddress=clusterAddress)