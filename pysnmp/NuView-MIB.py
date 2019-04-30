#
# PySNMP MIB module NuView-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NuView-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:22:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, NotificationType, NotificationType, TimeTicks, Integer32, ModuleIdentity, Bits, enterprises, Counter32, MibIdentifier, Unsigned32, IpAddress, Counter64, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "NotificationType", "NotificationType", "TimeTicks", "Integer32", "ModuleIdentity", "Bits", "enterprises", "Counter32", "MibIdentifier", "Unsigned32", "IpAddress", "Counter64", "Gauge32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
NuView = MibIdentifier((1, 3, 6, 1, 4, 1, 2427))
ClusterX = MibIdentifier((1, 3, 6, 1, 4, 1, 2427, 2))
clxMibStats = MibIdentifier((1, 3, 6, 1, 4, 1, 2427, 2, 1))
clxTrapData = MibIdentifier((1, 3, 6, 1, 4, 1, 2427, 2, 2))
clxMibStatsMajRev = MibScalar((1, 3, 6, 1, 4, 1, 2427, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clxMibStatsMajRev.setStatus('mandatory')
clxMibStatsMinRev = MibScalar((1, 3, 6, 1, 4, 1, 2427, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clxMibStatsMinRev.setStatus('mandatory')
clxMibStatsVendorName = MibScalar((1, 3, 6, 1, 4, 1, 2427, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clxMibStatsVendorName.setStatus('mandatory')
clxTrapDataString01 = MibScalar((1, 3, 6, 1, 4, 1, 2427, 2, 2, 1), DisplayString())
if mibBuilder.loadTexts: clxTrapDataString01.setStatus('mandatory')
clxTrapDataNodeName = MibScalar((1, 3, 6, 1, 4, 1, 2427, 2, 2, 2), DisplayString())
if mibBuilder.loadTexts: clxTrapDataNodeName.setStatus('mandatory')
clxTrapDataClusterName = MibScalar((1, 3, 6, 1, 4, 1, 2427, 2, 2, 3), DisplayString())
if mibBuilder.loadTexts: clxTrapDataClusterName.setStatus('mandatory')
clxTrapDataResourceName = MibScalar((1, 3, 6, 1, 4, 1, 2427, 2, 2, 4), DisplayString())
if mibBuilder.loadTexts: clxTrapDataResourceName.setStatus('mandatory')
clxTrapDataResourceType = MibScalar((1, 3, 6, 1, 4, 1, 2427, 2, 2, 5), DisplayString())
if mibBuilder.loadTexts: clxTrapDataResourceType.setStatus('mandatory')
clxTrapDataSeverityValue = MibScalar((1, 3, 6, 1, 4, 1, 2427, 2, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("info", 0), ("warning", 1), ("error", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: clxTrapDataSeverityValue.setStatus('mandatory')
clxTrapDataNetwork = MibScalar((1, 3, 6, 1, 4, 1, 2427, 2, 2, 7), DisplayString())
if mibBuilder.loadTexts: clxTrapDataNetwork.setStatus('mandatory')
clxTrapEventDate = MibScalar((1, 3, 6, 1, 4, 1, 2427, 2, 2, 8), DisplayString())
if mibBuilder.loadTexts: clxTrapEventDate.setStatus('mandatory')
clxTrapEventTime = MibScalar((1, 3, 6, 1, 4, 1, 2427, 2, 2, 9), DisplayString())
if mibBuilder.loadTexts: clxTrapEventTime.setStatus('mandatory')
clxTrapEventSource = MibScalar((1, 3, 6, 1, 4, 1, 2427, 2, 2, 10), DisplayString())
if mibBuilder.loadTexts: clxTrapEventSource.setStatus('mandatory')
clxTrapEventCategory = MibScalar((1, 3, 6, 1, 4, 1, 2427, 2, 2, 11), DisplayString())
if mibBuilder.loadTexts: clxTrapEventCategory.setStatus('mandatory')
clxTrapEventID = MibScalar((1, 3, 6, 1, 4, 1, 2427, 2, 2, 12), DisplayString())
if mibBuilder.loadTexts: clxTrapEventID.setStatus('mandatory')
clxTrapEventUser = MibScalar((1, 3, 6, 1, 4, 1, 2427, 2, 2, 13), DisplayString())
if mibBuilder.loadTexts: clxTrapEventUser.setStatus('mandatory')
clxTrapEventComputer = MibScalar((1, 3, 6, 1, 4, 1, 2427, 2, 2, 14), DisplayString())
if mibBuilder.loadTexts: clxTrapEventComputer.setStatus('mandatory')
clxTrapDataNetworkName = MibScalar((1, 3, 6, 1, 4, 1, 2427, 2, 2, 15), DisplayString())
if mibBuilder.loadTexts: clxTrapDataNetworkName.setStatus('mandatory')
NuViewTrapStr = NotificationType((1, 3, 6, 1, 4, 1, 2427) + (0,1)).setObjects(("NuView-MIB", "clxTrapDataString01"))
ClusterXTrapStr = NotificationType((1, 3, 6, 1, 4, 1, 2427, 2) + (0,1)).setObjects(("NuView-MIB", "clxTrapDataString01"))
ClusterXTrapNodeFail = NotificationType((1, 3, 6, 1, 4, 1, 2427, 2) + (0,2)).setObjects(("NuView-MIB", "clxTrapDataClusterName"), ("NuView-MIB", "clxTrapDataNodeName"))
ClusterXTrapClusterFail = NotificationType((1, 3, 6, 1, 4, 1, 2427, 2) + (0,3)).setObjects(("NuView-MIB", "clxTrapDataClusterName"))
ClusterXTrapResourceFail = NotificationType((1, 3, 6, 1, 4, 1, 2427, 2) + (0,4)).setObjects(("NuView-MIB", "clxTrapDataClusterName"), ("NuView-MIB", "clxTrapDataNodeName"), ("NuView-MIB", "clxTrapDataResourceName"))
ClusterXTrapNodeJoins = NotificationType((1, 3, 6, 1, 4, 1, 2427, 2) + (0,5)).setObjects(("NuView-MIB", "clxTrapDataClusterName"), ("NuView-MIB", "clxTrapDataNodeName"))
ClusterXTrapNetworkFail = NotificationType((1, 3, 6, 1, 4, 1, 2427, 2) + (0,6)).setObjects(("NuView-MIB", "clxTrapDataClusterName"), ("NuView-MIB", "clxTrapDataNetworkName"))
ClusterXTrapNormalClusterServiceLog = NotificationType((1, 3, 6, 1, 4, 1, 2427, 2) + (0,7)).setObjects(("NuView-MIB", "clxTrapEventDate"), ("NuView-MIB", "clxTrapEventTime"), ("NuView-MIB", "clxTrapEventSource"), ("NuView-MIB", "clxTrapEventCategory"), ("NuView-MIB", "clxTrapEventID"), ("NuView-MIB", "clxTrapEventUser"), ("NuView-MIB", "clxTrapEventComputer"))
ClusterXTrapWarningClusterServiceLog = NotificationType((1, 3, 6, 1, 4, 1, 2427, 2) + (0,8)).setObjects(("NuView-MIB", "clxTrapEventDate"), ("NuView-MIB", "clxTrapEventTime"), ("NuView-MIB", "clxTrapEventSource"), ("NuView-MIB", "clxTrapEventCategory"), ("NuView-MIB", "clxTrapEventID"), ("NuView-MIB", "clxTrapEventUser"), ("NuView-MIB", "clxTrapEventComputer"))
ClusterXTrapCriticalClusterServiceLog = NotificationType((1, 3, 6, 1, 4, 1, 2427, 2) + (0,9)).setObjects(("NuView-MIB", "clxTrapEventDate"), ("NuView-MIB", "clxTrapEventTime"), ("NuView-MIB", "clxTrapEventSource"), ("NuView-MIB", "clxTrapEventCategory"), ("NuView-MIB", "clxTrapEventID"), ("NuView-MIB", "clxTrapEventUser"), ("NuView-MIB", "clxTrapEventComputer"))
mibBuilder.exportSymbols("NuView-MIB", clxTrapDataNetworkName=clxTrapDataNetworkName, clxTrapEventCategory=clxTrapEventCategory, ClusterXTrapStr=ClusterXTrapStr, NuViewTrapStr=NuViewTrapStr, ClusterXTrapNodeFail=ClusterXTrapNodeFail, clxTrapData=clxTrapData, ClusterXTrapResourceFail=ClusterXTrapResourceFail, ClusterX=ClusterX, clxMibStats=clxMibStats, ClusterXTrapClusterFail=ClusterXTrapClusterFail, ClusterXTrapNodeJoins=ClusterXTrapNodeJoins, ClusterXTrapNormalClusterServiceLog=ClusterXTrapNormalClusterServiceLog, clxTrapEventUser=clxTrapEventUser, clxTrapDataResourceType=clxTrapDataResourceType, clxMibStatsMinRev=clxMibStatsMinRev, clxTrapEventID=clxTrapEventID, clxTrapEventComputer=clxTrapEventComputer, NuView=NuView, clxMibStatsMajRev=clxMibStatsMajRev, ClusterXTrapCriticalClusterServiceLog=ClusterXTrapCriticalClusterServiceLog, clxTrapDataNetwork=clxTrapDataNetwork, ClusterXTrapWarningClusterServiceLog=ClusterXTrapWarningClusterServiceLog, clxTrapEventSource=clxTrapEventSource, clxTrapDataString01=clxTrapDataString01, clxTrapEventDate=clxTrapEventDate, ClusterXTrapNetworkFail=ClusterXTrapNetworkFail, clxTrapDataClusterName=clxTrapDataClusterName, clxTrapDataNodeName=clxTrapDataNodeName, clxTrapDataResourceName=clxTrapDataResourceName, clxTrapEventTime=clxTrapEventTime, clxTrapDataSeverityValue=clxTrapDataSeverityValue, clxMibStatsVendorName=clxMibStatsVendorName)