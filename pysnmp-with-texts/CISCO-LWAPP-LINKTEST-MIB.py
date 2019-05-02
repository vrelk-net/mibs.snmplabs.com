#
# PySNMP MIB module CISCO-LWAPP-LINKTEST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-LWAPP-LINKTEST-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:05:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter32, Counter64, Bits, iso, ObjectIdentity, ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Integer32, TimeTicks, IpAddress, NotificationType, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "Bits", "iso", "ObjectIdentity", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Integer32", "TimeTicks", "IpAddress", "NotificationType", "MibIdentifier")
MacAddress, TruthValue, DisplayString, TimeInterval, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TruthValue", "DisplayString", "TimeInterval", "TextualConvention", "RowStatus")
ciscoLwappLinkTestMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 516))
ciscoLwappLinkTestMIB.setRevisions(('2006-04-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoLwappLinkTestMIB.setRevisionsDescriptions(('Initial version of this MIB module. ',))
if mibBuilder.loadTexts: ciscoLwappLinkTestMIB.setLastUpdated('200604060000Z')
if mibBuilder.loadTexts: ciscoLwappLinkTestMIB.setOrganization('Cisco Systems Inc.')
if mibBuilder.loadTexts: ciscoLwappLinkTestMIB.setContactInfo(' Cisco Systems, Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS Email: cs-wnbu-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoLwappLinkTestMIB.setDescription("This MIB is intended to be implemented on all those devices operating as Central controllers, that terminate the Light Weight Access Point Protocol tunnel from Cisco Light-weight LWAPP Access Points. Link Test is performed to learn the radio link quality between AP and Client. CCX linktest is performed for CCX clients. With CCX linktest radio link can be measured in both direction i.e. AP->Client(downLink) and Client->AP(uplink). When client does not support CCX or CCX linktest fails,ping is done between AP and Client. In ping test, only uplink (client->AP) quality can be measured. The relationship between the controller and the LWAPP APs is depicted as follows. +......+ +......+ +......+ +......+ + + + + + + + + + CC + + CC + + CC + + CC + + + + + + + + + +......+ +......+ +......+ +......+ .. . . . .. . . . . . . . . . . . . . . . . . . . . . . . +......+ +......+ +......+ +......+ +......+ + + + + + + + + + + + AP + + AP + + AP + + AP + + AP + + + + + + + + + + + +......+ +......+ +......+ +......+ +......+ . . . . . . . . . . . . . . . . . . . . . . . . +......+ +......+ +......+ +......+ +......+ + + + + + + + + + + + MN + + MN + + MN + + MN + + MN + + + + + + + + + + + +......+ +......+ +......+ +......+ +......+ The LWAPP tunnel exists between the controller and the APs. The MNs communicate with the APs through the protocol defined by the 802.11 standard. LWAPP APs, upon bootup, discover and join one of the controllers and forward all the 802.11 frames to them encapsulated inside LWAPP frames. GLOSSARY Access Point ( AP ) An entity that contains an 802.11 medium access control ( MAC ) and physical layer ( PHY ) interface and provides access to the distribution services via the wireless medium for associated clients. LWAPP APs encapsulate all the 802.11 frames in LWAPP frames and sends them to the controller to which it is logically connected. Central Controller ( CC ) The central entity that terminates the LWAPP protocol tunnel from the LWAPP APs. Throughout this MIB, this entity also referred to as 'controller'. Cisco Compatible eXtensions (CCX) Wireless LAN Access Points (APs) manufactured by Cisco Systems have features and capabilities beyond those in related standards (e.g., IEEE 802.11 suite of standards, Wi-Fi recommendations by WECA, 802.1X security suite, etc). A number of features provide higher performance. For example, Cisco AP transmits a specific Information Element, which the clients adapt to for enhanced performance. Similarly, a number of features are implemented by means of proprietary Information Elements, which Cisco clients use in specific ways to carry out tasks above and beyond the standard.Other examples of feature categories are roaming and power saving. Light Weight Access Point Protocol ( LWAPP ) This is a generic protocol that defines the communication between the Access Points and the Central controller. Mobile Node ( MN ) A roaming 802.11 wireless device in a wireless network associated with an access point. Mobile Node and client are used interchangeably. Received Signal Strength Indicator ( RSSI ) A measure of the strength of the signal as observed by the entity that received it, expressed in 'dbm'. Signal-Noise Ratio ( SNR ) A measure of the quality of the signal relative to the strength of noise expressed in 'dB'. REFERENCE [1] Wireless LAN Medium Access Control ( MAC ) and Physical Layer ( PHY ) Specifications. [2] Draft-obara-capwap-lwapp-00.txt, IETF Light Weight Access Point Protocol ")
ciscoLwappLinkTestMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 516, 0))
ciscoLwappLinkTestMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 516, 1))
ciscoLwappLinkTestMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 516, 2))
ciscoLwappLinkTestConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 1))
ciscoLwappLinkTestRun = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2))
ciscoLwappLinkTestStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 3))
cLLtResponder = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLLtResponder.setStatus('current')
if mibBuilder.loadTexts: cLLtResponder.setDescription("This object is used to control the AP's response to the linktests initiated by the client. When set to 'true', the AP is expected to respond to the linktests performed by the client. The AP won't respond to the linktests initiated by the client, when this object is set to 'false'. ")
cLLtPacketSize = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 1500)).clone(50)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLLtPacketSize.setStatus('current')
if mibBuilder.loadTexts: cLLtPacketSize.setDescription('This object indicates the number of bytes to be sent by the AP to the client in one linktest packet. ')
cLLtNumberOfPackets = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLLtNumberOfPackets.setStatus('current')
if mibBuilder.loadTexts: cLLtNumberOfPackets.setDescription('This object indicates the number of linktest packets sent by the AP to the client. ')
cLLtTestPurgeTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(15, 1800)).clone(15)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cLLtTestPurgeTime.setStatus('current')
if mibBuilder.loadTexts: cLLtTestPurgeTime.setDescription('This object indicates the duration for which the results of a particular run of linktest is available in cLLtClientLtResultsTable from the time of completion of that run of linktest. At the expiry of this time after the completion of the linktest, the entries corresponding to the linktest and the corresponding results are removed from cLLtClientLinkTestTable and cLLtClientLtResultsTable respectively. ')
cLLtClientLinkTestTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 1), )
if mibBuilder.loadTexts: cLLtClientLinkTestTable.setStatus('current')
if mibBuilder.loadTexts: cLLtClientLinkTestTable.setDescription("This table is used to initiate linktests between an AP and one of its associated clients. CCX linktests are done on clients that support CCX. For all non-CCX clients, ping test is done. Note that ping test is also done when the CCX linktests fail. With CCX LinkTest support, the controller can test the link quality in downstream (direction of traffic from AP to client) direction by issuing LinkTest requests towards the client and let client record in the response packet the RF parameters like received signal strength, signal-to-noise etc., of the received request packet. With ping test only those RF parameters that are seen by the AP are measured. User initiates one run of linktest by adding a row to this table through explicit management action from the network manager. A row is created by specifying cLLtClientLtIndex, cLLtClientLtMacAddress and setting the RowStatus object to 'createAndGo'. This indicates the the request made to start the linktest on the client identified by cLLtClientLtMacAddress. cLLtClientLtIndex identifies the particular instance of the test. The added row is deleted by setting the corresponding instance of the RowStatus object to 'destroy'. In case if the agent finds that the time duration represented by cLLtTestPurgeTime has elapsed since the completion of the linktest, it proceeds to delete the row automatically, if the row exists at that point of time. The results of the linktest identified by cLLtClientLtIndex can be obtained from the queries to cLLtClientLtResultsTable. ")
cLLtClientLinkTestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtIndex"))
if mibBuilder.loadTexts: cLLtClientLinkTestEntry.setStatus('current')
if mibBuilder.loadTexts: cLLtClientLinkTestEntry.setDescription('Each entry in this table represents one instance of the linktest initiated by the user through a network manager. ')
cLLtClientLtIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 32)))
if mibBuilder.loadTexts: cLLtClientLtIndex.setStatus('current')
if mibBuilder.loadTexts: cLLtClientLtIndex.setDescription('This object uniquely identifies one particular run of the linktest initiated between the client identified by cLLtClientLtMacAddress and the AP it is currently associated with. ')
cLLtClientLtMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 1, 1, 2), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLLtClientLtMacAddress.setStatus('current')
if mibBuilder.loadTexts: cLLtClientLtMacAddress.setDescription("This object represents the mac address of the client involved in the particular run of linktest. This object must be set to a valid value when setting cLLtClientRowStatus to 'createAndGo' to initiate a run of linktest. ")
cLLtClientLtRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cLLtClientLtRowStatus.setStatus('current')
if mibBuilder.loadTexts: cLLtClientLtRowStatus.setDescription('This object is the status column used for creating and deleting instances of the columnar objects in this table. ')
cLLtClientLTResultsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2), )
if mibBuilder.loadTexts: cLLtClientLTResultsTable.setStatus('current')
if mibBuilder.loadTexts: cLLtClientLTResultsTable.setDescription('This table populates the results of the linktests initiated by the user through the cLLtClientLinkTestTable. This table has a sparse dependent relationship with cLLtClientLinkTestTable. There exists a row in this table corresponding to the row for each row in cLLtClientLinkTestTable identified by cLLtClientLtIndex. A row is added to this table when user, through the network manager, adds a row to cLLtClientLinkTestTable and initiates one run of linktest. A row is deleted by the agent when the corresponding row of cLLtClientLinkTestTable is deleted. The manager is expected to poll cLLtClientLtStatus to check the status of the linktest. Depending on the status read through this object cLLtClientLtStatus, the appropriate columns for CCX or ping tests are read and linktest statistics are gathered. ')
cLLtClientLTResultsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1), ).setIndexNames((0, "CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtIndex"))
if mibBuilder.loadTexts: cLLtClientLTResultsEntry.setStatus('current')
if mibBuilder.loadTexts: cLLtClientLTResultsEntry.setDescription('Each entry in this table represents the results of the linktest identified by cLLtClientLtIndex. ')
cLLtClientLtPacketsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 1), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLLtClientLtPacketsSent.setStatus('current')
if mibBuilder.loadTexts: cLLtClientLtPacketsSent.setDescription('The number of packets sent to the target client specified by cLLtClientLtMacAddress by the AP it is associated to. ')
cLLtClientLtPacketsRx = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 2), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLLtClientLtPacketsRx.setStatus('current')
if mibBuilder.loadTexts: cLLtClientLtPacketsRx.setDescription('The number of packets sent by the client specified by cLLtClientLtMacAddress to the AP it is associated to. ')
cLLtClientLtTotalPacketsLost = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 3), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLLtClientLtTotalPacketsLost.setStatus('current')
if mibBuilder.loadTexts: cLLtClientLtTotalPacketsLost.setDescription('The total number of packets lost during the linktest in both the upstream and downstream directions. ')
cLLtClientLtApToClientPktsLost = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 4), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLLtClientLtApToClientPktsLost.setStatus('current')
if mibBuilder.loadTexts: cLLtClientLtApToClientPktsLost.setDescription('The number of packets lost during the linktest in the downstream (direction of traffic from AP to client) direction. ')
cLLtClientLtClientToApPktsLost = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 5), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLLtClientLtClientToApPktsLost.setStatus('current')
if mibBuilder.loadTexts: cLLtClientLtClientToApPktsLost.setDescription('The number of packets lost during the linktest in the upstream (direction of traffic from client to AP) direction. ')
cLLtClientLtMinRoundTripTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 6), TimeInterval()).setUnits('hundredths-seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLLtClientLtMinRoundTripTime.setStatus('current')
if mibBuilder.loadTexts: cLLtClientLtMinRoundTripTime.setDescription('The minimum round trip time observed on the linktest packet between the AP and the client. ')
cLLtClientLtMaxRoundTripTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 7), TimeInterval()).setUnits('hundredths-seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLLtClientLtMaxRoundTripTime.setStatus('current')
if mibBuilder.loadTexts: cLLtClientLtMaxRoundTripTime.setDescription('The maximum round trip time observed on the linktest packet between the AP and the client. ')
cLLtClientLtAvgRoundTripTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 8), TimeInterval()).setUnits('hundredths-seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLLtClientLtAvgRoundTripTime.setStatus('current')
if mibBuilder.loadTexts: cLLtClientLtAvgRoundTripTime.setDescription('The average round trip time observed on the linktest packet between the AP and the client. ')
cLLtClientLtUplinkMinRSSI = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 9), Integer32()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLLtClientLtUplinkMinRSSI.setStatus('current')
if mibBuilder.loadTexts: cLLtClientLtUplinkMinRSSI.setDescription('The minimum RSSI value as observed at the AP. ')
cLLtClientLtUplinkMaxRSSI = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 10), Integer32()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLLtClientLtUplinkMaxRSSI.setStatus('current')
if mibBuilder.loadTexts: cLLtClientLtUplinkMaxRSSI.setDescription('The maximum RSSI value as observed at the AP. ')
cLLtClientLtUplinkAvgRSSI = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 11), Integer32()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLLtClientLtUplinkAvgRSSI.setStatus('current')
if mibBuilder.loadTexts: cLLtClientLtUplinkAvgRSSI.setDescription('The average RSSI value as observed at the AP. ')
cLLtClientLtDownlinkMinRSSI = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 12), Integer32()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLLtClientLtDownlinkMinRSSI.setStatus('current')
if mibBuilder.loadTexts: cLLtClientLtDownlinkMinRSSI.setDescription('The minimum RSSI value as observed at the client. ')
cLLtClientLtDownlinkMaxRSSI = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 13), Integer32()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLLtClientLtDownlinkMaxRSSI.setStatus('current')
if mibBuilder.loadTexts: cLLtClientLtDownlinkMaxRSSI.setDescription('The maximum RSSI value as observed at the client. ')
cLLtClientLtDownlinkAvgRSSI = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 14), Integer32()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLLtClientLtDownlinkAvgRSSI.setStatus('current')
if mibBuilder.loadTexts: cLLtClientLtDownlinkAvgRSSI.setDescription('The average RSSI value as observed at the client. ')
cLLtClientLtUplinkMinSNR = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 15), Integer32()).setUnits('dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLLtClientLtUplinkMinSNR.setStatus('current')
if mibBuilder.loadTexts: cLLtClientLtUplinkMinSNR.setDescription('The minimum SNR value as observed at the AP. ')
cLLtClientLtUplinkMaxSNR = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 16), Integer32()).setUnits('dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLLtClientLtUplinkMaxSNR.setStatus('current')
if mibBuilder.loadTexts: cLLtClientLtUplinkMaxSNR.setDescription('The maximum SNR value as observed at the AP. ')
cLLtClientLtUplinkAvgSNR = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 17), Integer32()).setUnits('dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLLtClientLtUplinkAvgSNR.setStatus('current')
if mibBuilder.loadTexts: cLLtClientLtUplinkAvgSNR.setDescription('The average SNR value as observed at the AP. ')
cLLtClientLtDownlinkMinSNR = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 18), Integer32()).setUnits('dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLLtClientLtDownlinkMinSNR.setStatus('current')
if mibBuilder.loadTexts: cLLtClientLtDownlinkMinSNR.setDescription('The minimum SNR value as observed at the client. ')
cLLtClientLtDownlinkMaxSNR = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 19), Integer32()).setUnits('dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLLtClientLtDownlinkMaxSNR.setStatus('current')
if mibBuilder.loadTexts: cLLtClientLtDownlinkMaxSNR.setDescription('The maximum SNR value as observed at the client. ')
cLLtClientLtDownlinkAvgSNR = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 20), Integer32()).setUnits('dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLLtClientLtDownlinkAvgSNR.setStatus('current')
if mibBuilder.loadTexts: cLLtClientLtDownlinkAvgSNR.setDescription('The average SNR value as observed at the client. ')
cLLtClientLtTotalTxRetriesAP = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 21), Counter32()).setUnits('retries').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLLtClientLtTotalTxRetriesAP.setStatus('current')
if mibBuilder.loadTexts: cLLtClientLtTotalTxRetriesAP.setDescription('The total number of linktest packet transmission retries as observed at the AP. ')
cLLtClientLtMaxTxRetriesAP = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 22), Counter32()).setUnits('retries').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLLtClientLtMaxTxRetriesAP.setStatus('current')
if mibBuilder.loadTexts: cLLtClientLtMaxTxRetriesAP.setDescription('The maximum number of linktest packet transmission retries observed at the AP. ')
cLLtClientLtTotalTxRetriesClient = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 23), Counter32()).setUnits('retries').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLLtClientLtTotalTxRetriesClient.setStatus('current')
if mibBuilder.loadTexts: cLLtClientLtTotalTxRetriesClient.setDescription('The total number of linktest packet transmission retries at the client. ')
cLLtClientLtMaxTxRetriesClient = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 24), Counter32()).setUnits('retries').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLLtClientLtMaxTxRetriesClient.setStatus('current')
if mibBuilder.loadTexts: cLLtClientLtMaxTxRetriesClient.setDescription('The maximum number of linktest packet transmission retries observed at the client. ')
cLLtClientLtStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 2, 2, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("cLLtClientLtStatusFailed", 0), ("cLLtClientLtStatusCcxInProgress", 1), ("cLLtClientLtStatusPngInProgress", 2), ("cLLtClientLtStatusPingSuccess", 3), ("cLLtClientLtStatusCcxLtSuccess", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLLtClientLtStatus.setStatus('current')
if mibBuilder.loadTexts: cLLtClientLtStatus.setDescription("This object indicates the status of the linktest this particular entry corresponds to. The semantics as follows. 'cLLtClientLtStatusFailed' - This value indicates that this particular linktest has failed. 'cLLtClientLtCcxStatusInProgress' - This value indicates that the CCX linktest is in progress. 'cLLtClientLtPngStatusInProgress' - This value indicates that the Ping-based linktest is in progress. 'cLLtClientLtStatusPingSuccess' - This value indicates that ping-based linktest between AP and client has succeeded. Only the following columns of this table should be considered for collecting data from the ping responses. cLLtClientLtPacketsSent, cLLtClientLtPacketsRx, cLLtClientLtUplinkAvgRSSI, cLLtClientLtUplinkAvgSNR cLLtClientLtStatusCcxLtSuccess - This value indicates that CCX linktest done to test the link between the client and the AP is successful. All the columns of this table are applicable and valid for collecting data from the CCX responses. ")
cLLtClientLtDataRateTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 3, 1), )
if mibBuilder.loadTexts: cLLtClientLtDataRateTable.setStatus('current')
if mibBuilder.loadTexts: cLLtClientLtDataRateTable.setDescription('This table provides the results of CCX Link tests classified on different data rates between AP and clients. A row is added to this table automatically by the agent corresponding to one linktest identified by cLLtClientLtIndex and deleted when the corresponding row in cLLtClientLinkTestTable is deleted. ')
cLLtClientLtDataRateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 3, 1, 1), ).setIndexNames((0, "CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtIndex"), (0, "CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtDataRate"))
if mibBuilder.loadTexts: cLLtClientLtDataRateEntry.setStatus('current')
if mibBuilder.loadTexts: cLLtClientLtDataRateEntry.setDescription('Each entry represents a conceptual row and populates the number of packets sent in the linktest identified by cLLtClientLtIndex. The statistics of the linktest are classified based on the respective data rates identified by cLLtClientLtDataRate. ')
cLLtClientLtDataRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 3, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255)))
if mibBuilder.loadTexts: cLLtClientLtDataRate.setStatus('current')
if mibBuilder.loadTexts: cLLtClientLtDataRate.setDescription('This object identifies the rate at which packets are transmitted. The rates are defined in Mbps with the following being the possible values. Rates - 1,2,5.5,6,9,11,12,18,24,36,48,54,108. ')
cLLtClientLtRateDownlinkPktsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 3, 1, 1, 2), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLLtClientLtRateDownlinkPktsSent.setStatus('current')
if mibBuilder.loadTexts: cLLtClientLtRateDownlinkPktsSent.setDescription('The number of packets sent by the AP at the rate identified by cLLtClientLtDataRate. ')
cLLtClientLtRateUplinkPktsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 516, 1, 3, 1, 1, 3), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cLLtClientLtRateUplinkPktsSent.setStatus('current')
if mibBuilder.loadTexts: cLLtClientLtRateUplinkPktsSent.setDescription('The number of packets sent by the client at the rate identified by cLLtClientLtDataRate. ')
ciscoLwappLinkTestMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 516, 2, 1))
ciscoLwappLinkTestMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 516, 2, 2))
ciscoLwappLinkTestMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 516, 2, 1, 1)).setObjects(("CISCO-LWAPP-LINKTEST-MIB", "cLLinkTestConfigGroup"), ("CISCO-LWAPP-LINKTEST-MIB", "cLLinkTestRunsGroup"), ("CISCO-LWAPP-LINKTEST-MIB", "cLLinkTestStatusGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLwappLinkTestMIBCompliance = ciscoLwappLinkTestMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoLwappLinkTestMIBCompliance.setDescription('The compliance statement for the SNMP entities that implement the ciscoLwappLinkTestMIB module.')
cLLinkTestConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 516, 2, 2, 1)).setObjects(("CISCO-LWAPP-LINKTEST-MIB", "cLLtResponder"), ("CISCO-LWAPP-LINKTEST-MIB", "cLLtPacketSize"), ("CISCO-LWAPP-LINKTEST-MIB", "cLLtNumberOfPackets"), ("CISCO-LWAPP-LINKTEST-MIB", "cLLtTestPurgeTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cLLinkTestConfigGroup = cLLinkTestConfigGroup.setStatus('current')
if mibBuilder.loadTexts: cLLinkTestConfigGroup.setDescription('This collection of objects represent the linktest parameters for use during the various of the tests. ')
cLLinkTestRunsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 516, 2, 2, 2)).setObjects(("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtMacAddress"), ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtPacketsSent"), ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtPacketsRx"), ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtTotalPacketsLost"), ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtApToClientPktsLost"), ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtClientToApPktsLost"), ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtMinRoundTripTime"), ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtMaxRoundTripTime"), ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtAvgRoundTripTime"), ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtUplinkMinRSSI"), ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtUplinkMaxRSSI"), ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtUplinkAvgRSSI"), ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtDownlinkMinRSSI"), ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtDownlinkMaxRSSI"), ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtDownlinkAvgRSSI"), ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtUplinkMinSNR"), ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtUplinkMaxSNR"), ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtUplinkAvgSNR"), ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtDownlinkMinSNR"), ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtDownlinkMaxSNR"), ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtDownlinkAvgSNR"), ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtTotalTxRetriesAP"), ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtMaxTxRetriesAP"), ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtTotalTxRetriesClient"), ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtMaxTxRetriesClient"), ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtStatus"), ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cLLinkTestRunsGroup = cLLinkTestRunsGroup.setStatus('current')
if mibBuilder.loadTexts: cLLinkTestRunsGroup.setDescription('This collection of objects is used to initiate linktests and retrieve the results of the respective runs of the tests. ')
cLLinkTestStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 516, 2, 2, 3)).setObjects(("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtRateDownlinkPktsSent"), ("CISCO-LWAPP-LINKTEST-MIB", "cLLtClientLtRateUplinkPktsSent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cLLinkTestStatusGroup = cLLinkTestStatusGroup.setStatus('current')
if mibBuilder.loadTexts: cLLinkTestStatusGroup.setDescription('This collection of objects provide information about the linktest results. ')
mibBuilder.exportSymbols("CISCO-LWAPP-LINKTEST-MIB", ciscoLwappLinkTestMIBCompliances=ciscoLwappLinkTestMIBCompliances, cLLtClientLtTotalTxRetriesClient=cLLtClientLtTotalTxRetriesClient, cLLtClientLtUplinkMinSNR=cLLtClientLtUplinkMinSNR, cLLtClientLinkTestTable=cLLtClientLinkTestTable, cLLtClientLtRateUplinkPktsSent=cLLtClientLtRateUplinkPktsSent, cLLtClientLTResultsTable=cLLtClientLTResultsTable, PYSNMP_MODULE_ID=ciscoLwappLinkTestMIB, cLLtResponder=cLLtResponder, cLLtClientLTResultsEntry=cLLtClientLTResultsEntry, cLLtClientLtUplinkAvgRSSI=cLLtClientLtUplinkAvgRSSI, cLLtClientLtUplinkMaxSNR=cLLtClientLtUplinkMaxSNR, cLLtNumberOfPackets=cLLtNumberOfPackets, cLLtClientLtUplinkAvgSNR=cLLtClientLtUplinkAvgSNR, cLLtClientLtDataRateTable=cLLtClientLtDataRateTable, ciscoLwappLinkTestRun=ciscoLwappLinkTestRun, cLLtClientLtUplinkMinRSSI=cLLtClientLtUplinkMinRSSI, cLLtClientLtPacketsRx=cLLtClientLtPacketsRx, cLLtClientLtDownlinkAvgSNR=cLLtClientLtDownlinkAvgSNR, cLLtClientLtClientToApPktsLost=cLLtClientLtClientToApPktsLost, cLLtClientLtDataRateEntry=cLLtClientLtDataRateEntry, cLLtClientLtRateDownlinkPktsSent=cLLtClientLtRateDownlinkPktsSent, cLLtClientLtMacAddress=cLLtClientLtMacAddress, cLLtClientLtMaxRoundTripTime=cLLtClientLtMaxRoundTripTime, cLLtClientLtMinRoundTripTime=cLLtClientLtMinRoundTripTime, cLLtClientLtPacketsSent=cLLtClientLtPacketsSent, cLLtClientLtAvgRoundTripTime=cLLtClientLtAvgRoundTripTime, cLLtClientLtDownlinkAvgRSSI=cLLtClientLtDownlinkAvgRSSI, cLLtClientLtMaxTxRetriesClient=cLLtClientLtMaxTxRetriesClient, cLLtClientLtDataRate=cLLtClientLtDataRate, cLLtClientLtApToClientPktsLost=cLLtClientLtApToClientPktsLost, cLLtPacketSize=cLLtPacketSize, cLLtClientLtDownlinkMinRSSI=cLLtClientLtDownlinkMinRSSI, ciscoLwappLinkTestStatus=ciscoLwappLinkTestStatus, cLLtClientLtDownlinkMaxRSSI=cLLtClientLtDownlinkMaxRSSI, cLLtClientLtIndex=cLLtClientLtIndex, cLLtClientLtDownlinkMinSNR=cLLtClientLtDownlinkMinSNR, cLLinkTestRunsGroup=cLLinkTestRunsGroup, ciscoLwappLinkTestMIBNotifs=ciscoLwappLinkTestMIBNotifs, ciscoLwappLinkTestConfig=ciscoLwappLinkTestConfig, cLLtClientLtUplinkMaxRSSI=cLLtClientLtUplinkMaxRSSI, ciscoLwappLinkTestMIBCompliance=ciscoLwappLinkTestMIBCompliance, cLLtClientLinkTestEntry=cLLtClientLinkTestEntry, ciscoLwappLinkTestMIBObjects=ciscoLwappLinkTestMIBObjects, cLLtTestPurgeTime=cLLtTestPurgeTime, cLLtClientLtRowStatus=cLLtClientLtRowStatus, cLLtClientLtDownlinkMaxSNR=cLLtClientLtDownlinkMaxSNR, cLLtClientLtMaxTxRetriesAP=cLLtClientLtMaxTxRetriesAP, cLLinkTestStatusGroup=cLLinkTestStatusGroup, ciscoLwappLinkTestMIB=ciscoLwappLinkTestMIB, cLLinkTestConfigGroup=cLLinkTestConfigGroup, cLLtClientLtTotalPacketsLost=cLLtClientLtTotalPacketsLost, ciscoLwappLinkTestMIBGroups=ciscoLwappLinkTestMIBGroups, cLLtClientLtTotalTxRetriesAP=cLLtClientLtTotalTxRetriesAP, cLLtClientLtStatus=cLLtClientLtStatus, ciscoLwappLinkTestMIBConform=ciscoLwappLinkTestMIBConform)