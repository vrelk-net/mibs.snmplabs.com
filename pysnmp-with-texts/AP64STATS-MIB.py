#
# PySNMP MIB module AP64STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AP64STATS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:23:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ap64Stats, = mibBuilder.importSymbols("APENT-MIB", "ap64Stats")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, ObjectIdentity, IpAddress, Integer32, Counter64, Bits, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, Gauge32, MibIdentifier, ModuleIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ObjectIdentity", "IpAddress", "Integer32", "Counter64", "Bits", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "Gauge32", "MibIdentifier", "ModuleIdentity", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ap64StatsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2467, 1, 44, 1))
if mibBuilder.loadTexts: ap64StatsMib.setLastUpdated('9710092000Z')
if mibBuilder.loadTexts: ap64StatsMib.setOrganization('ArrowPoint Communications Inc.')
if mibBuilder.loadTexts: ap64StatsMib.setContactInfo(' Postal: ArrowPoint Communications Inc. 50 Nagog Park Acton, Massachusetts 01720 Tel: +1 978-206-3000 option 1 E-Mail: support@arrowpoint.com')
if mibBuilder.loadTexts: ap64StatsMib.setDescription('This MIB module contains 64 bit statistical aggregation of the RMON (RFC1757), MIBII (RFC1213) and EtherErrors (RFC1398)')
class PhysAddress(OctetString):
    pass

class OwnerString(DisplayString):
    pass

class EntryStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("valid", 1), ("createRequest", 2), ("underCreation", 3), ("invalid", 4))

ap64dot3StatsTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 44, 2), )
if mibBuilder.loadTexts: ap64dot3StatsTable.setStatus('current')
if mibBuilder.loadTexts: ap64dot3StatsTable.setDescription('Statistics for a collection of ethernet-like interfaces attached to a particular system.')
ap64dot3StatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 44, 2, 1), ).setIndexNames((0, "AP64STATS-MIB", "ap64dot3StatsIndex"))
if mibBuilder.loadTexts: ap64dot3StatsEntry.setStatus('current')
if mibBuilder.loadTexts: ap64dot3StatsEntry.setDescription('Statistics for a particular interface to an ethernet-like medium.')
ap64dot3StatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64dot3StatsIndex.setStatus('current')
if mibBuilder.loadTexts: ap64dot3StatsIndex.setDescription('An index value that uniquely identifies an interface to an ethernet-like medium. The interface identified by a particular value of this index is the same interface as identified by the same value of ifIndex.')
ap64dot3StatsAlignmentErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 2, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64dot3StatsAlignmentErrors.setReference('IEEE 802.3 Layer Management')
if mibBuilder.loadTexts: ap64dot3StatsAlignmentErrors.setStatus('current')
if mibBuilder.loadTexts: ap64dot3StatsAlignmentErrors.setDescription('A count of frames received on a particular interface that are not an integral number of octets in length and do not pass the FCS check. The count represented by an instance of this object is incremented when the alignmentError status is returned by the MAC service to the LLC (or other MAC user). Received frames for which multiple error conditions obtain are, according to the conventions of IEEE 802.3 Layer Management, counted exclusively according to the error status presented to the LLC.')
ap64dot3StatsFCSErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 2, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64dot3StatsFCSErrors.setReference('IEEE 802.3 Layer Management')
if mibBuilder.loadTexts: ap64dot3StatsFCSErrors.setStatus('current')
if mibBuilder.loadTexts: ap64dot3StatsFCSErrors.setDescription('A count of frames received on a particular interface that are an integral number of octets in length but do not pass the FCS check. The count represented by an instance of this object is incremented when the frameCheckError status is returned by the MAC service to the LLC (or other MAC user). Received frames for which multiple error conditions obtain are, according to the conventions of IEEE 802.3 Layer Management, counted exclusively according to the error status presented to the LLC.')
ap64dot3StatsSingleCollisionFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64dot3StatsSingleCollisionFrames.setReference('IEEE 802.3 Layer Management')
if mibBuilder.loadTexts: ap64dot3StatsSingleCollisionFrames.setStatus('current')
if mibBuilder.loadTexts: ap64dot3StatsSingleCollisionFrames.setDescription('A count of successfully transmitted frames on a particular interface for which transmission is inhibited by exactly one collision. A frame that is counted by an instance of this object is also counted by the corresponding instance of either the ifOutUcastPkts or ifOutNUcastPkts object and is not counted by the corresponding instance of the ap64dot3StatsMultipleCollisionFrames object.')
ap64dot3StatsMultipleCollisionFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64dot3StatsMultipleCollisionFrames.setReference('IEEE 802.3 Layer Management')
if mibBuilder.loadTexts: ap64dot3StatsMultipleCollisionFrames.setStatus('current')
if mibBuilder.loadTexts: ap64dot3StatsMultipleCollisionFrames.setDescription('A count of successfully transmitted frames on a particular interface for which transmission is inhibited by more than one collision. A frame that is counted by an instance of this object is also counted by the corresponding instance of either the ifOutUcastPkts or ifOutNUcastPkts object and is not counted by the corresponding instance of the ap64dot3StatsSingleCollisionFrames object.')
ap64dot3StatsSQETestErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64dot3StatsSQETestErrors.setReference('ANSI/IEEE Std 802.3-1985 Carrier Sense Multiple Access with Collision Detection Access Method and Physical Layer Specifications')
if mibBuilder.loadTexts: ap64dot3StatsSQETestErrors.setStatus('current')
if mibBuilder.loadTexts: ap64dot3StatsSQETestErrors.setDescription('A count of times that the SQE TEST ERROR message is generated by the PLS sublayer for a particular interface. The SQE TEST ERROR message is defined in section 7.2.2.2.4 of ANSI/IEEE 802.3-1985 and its generation is described in section 7.2.4.6 of the same document.')
ap64dot3StatsDeferredTransmissions = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 2, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64dot3StatsDeferredTransmissions.setReference('IEEE 802.3 Layer Management')
if mibBuilder.loadTexts: ap64dot3StatsDeferredTransmissions.setStatus('current')
if mibBuilder.loadTexts: ap64dot3StatsDeferredTransmissions.setDescription('A count of frames for which the first transmission attempt on a particular interface is delayed because the medium is busy. The count represented by an instance of this object does not include frames involved in collisions.')
ap64dot3StatsLateCollisions = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 2, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64dot3StatsLateCollisions.setReference('IEEE 802.3 Layer Management')
if mibBuilder.loadTexts: ap64dot3StatsLateCollisions.setStatus('current')
if mibBuilder.loadTexts: ap64dot3StatsLateCollisions.setDescription('The number of times that a collision is detected on a particular interface later than 512 bit-times into the transmission of a packet. Five hundred and twelve bit-times corresponds to 51.2 microseconds on a 10 Mbit/s system. A (late) collision included in a count represented by an instance of this object is also considered as a (generic) collision for purposes of other collision-related statistics.')
ap64dot3StatsExcessiveCollisions = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 2, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64dot3StatsExcessiveCollisions.setReference('IEEE 802.3 Layer Management')
if mibBuilder.loadTexts: ap64dot3StatsExcessiveCollisions.setStatus('current')
if mibBuilder.loadTexts: ap64dot3StatsExcessiveCollisions.setDescription('A count of frames for which transmission on a particular interface fails due to excessive collisions.')
ap64dot3StatsInternalMacTransmitErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 2, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64dot3StatsInternalMacTransmitErrors.setReference('IEEE 802.3 Layer Management')
if mibBuilder.loadTexts: ap64dot3StatsInternalMacTransmitErrors.setStatus('current')
if mibBuilder.loadTexts: ap64dot3StatsInternalMacTransmitErrors.setDescription('A count of frames for which transmission on a particular interface fails due to an internal MAC sublayer transmit error. A frame is only counted by an instance of this object if it is not counted by the corresponding instance of either the ap64dot3StatsLateCollisions object, the ap64dot3StatsExcessiveCollisions object, or the ap64dot3StatsCarrierSenseErrors object. The precise meaning of the count represented by an instance of this object is implementation- specific. In particular, an instance of this object may represent a count of transmission errors on a particular interface that are not otherwise counted.')
ap64dot3StatsCarrierSenseErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 2, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64dot3StatsCarrierSenseErrors.setReference('IEEE 802.3 Layer Management')
if mibBuilder.loadTexts: ap64dot3StatsCarrierSenseErrors.setStatus('current')
if mibBuilder.loadTexts: ap64dot3StatsCarrierSenseErrors.setDescription('The number of times that the carrier sense condition was lost or never asserted when attempting to transmit a frame on a particular interface. The count represented by an instance of this object is incremented at most once per transmission attempt, even if the carrier sense condition fluctuates during a transmission attempt.')
ap64dot3StatsFrameTooLongs = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 2, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64dot3StatsFrameTooLongs.setReference('IEEE 802.3 Layer Management')
if mibBuilder.loadTexts: ap64dot3StatsFrameTooLongs.setStatus('current')
if mibBuilder.loadTexts: ap64dot3StatsFrameTooLongs.setDescription('A count of frames received on a particular interface that exceed the maximum permitted frame size. The count represented by an instance of this object is incremented when the frameTooLong status is returned by the MAC service to the LLC (or other MAC user). Received frames for which multiple error conditions obtain are, according to the conventions of IEEE 802.3 Layer Management, counted exclusively according to the error status presented to the LLC.')
ap64dot3StatsInternalMacReceiveErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 2, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64dot3StatsInternalMacReceiveErrors.setReference('IEEE 802.3 Layer Management')
if mibBuilder.loadTexts: ap64dot3StatsInternalMacReceiveErrors.setStatus('current')
if mibBuilder.loadTexts: ap64dot3StatsInternalMacReceiveErrors.setDescription('A count of frames for which reception on a particular interface fails due to an internal MAC sublayer receive error. A frame is only counted by an instance of this object if it is not counted by the corresponding instance of either the ap64dot3StatsFrameTooLongs object, the ap64dot3StatsAlignmentErrors object, or the ap64dot3StatsFCSErrors object. The precise meaning of the count represented by an instance of this object is implementation- specific. In particular, an instance of this object may represent a count of receive errors on a particular interface that are not otherwise counted.')
ap64ifTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3), )
if mibBuilder.loadTexts: ap64ifTable.setStatus('current')
if mibBuilder.loadTexts: ap64ifTable.setDescription('A list of interface entries. The number of entries is given by the value of ifNumber.')
ap64ifEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1), ).setIndexNames((0, "AP64STATS-MIB", "ap64ifIndex"))
if mibBuilder.loadTexts: ap64ifEntry.setStatus('current')
if mibBuilder.loadTexts: ap64ifEntry.setDescription('An interface entry containing objects at the subnetwork layer and below for a particular interface.')
ap64ifIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64ifIndex.setStatus('current')
if mibBuilder.loadTexts: ap64ifIndex.setDescription("A unique value for each interface. Its value ranges between 1 and the value of ifNumber. The value for each interface must remain constant at least from one re-initialization of the entity's network management system to the next re- initialization.")
ap64ifDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64ifDescr.setStatus('current')
if mibBuilder.loadTexts: ap64ifDescr.setDescription('A textual string containing information about the interface. This string should include the name of the manufacturer, the product name and the version of the hardware interface.')
ap64ifType = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32))).clone(namedValues=NamedValues(("other", 1), ("regular1822", 2), ("hdh1822", 3), ("ddn-x25", 4), ("rfc877-x25", 5), ("ethernet-csmacd", 6), ("iso88023-csmacd", 7), ("iso88024-tokenBus", 8), ("iso88025-tokenRing", 9), ("iso88026-man", 10), ("starLan", 11), ("proteon-10Mbit", 12), ("proteon-80Mbit", 13), ("hyperchannel", 14), ("fddi", 15), ("lapb", 16), ("sdlc", 17), ("ds1", 18), ("e1", 19), ("basicISDN", 20), ("primaryISDN", 21), ("propPointToPointSerial", 22), ("ppp", 23), ("softwareLoopback", 24), ("eon", 25), ("ethernet-3Mbit", 26), ("nsip", 27), ("slip", 28), ("ultra", 29), ("ds3", 30), ("sip", 31), ("frame-relay", 32)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64ifType.setStatus('current')
if mibBuilder.loadTexts: ap64ifType.setDescription("The type of interface, distinguished according to the physical/link protocol(s) immediately `below' the network layer in the protocol stack.")
ap64ifMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64ifMtu.setStatus('current')
if mibBuilder.loadTexts: ap64ifMtu.setDescription('The size of the largest datagram which can be sent/received on the interface, specified in octets. For interfaces that are used for transmitting network datagrams, this is the size of the largest network datagram that can be sent on the interface.')
ap64ifSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64ifSpeed.setStatus('current')
if mibBuilder.loadTexts: ap64ifSpeed.setDescription("An estimate of the interface's current bandwidth in bits per second. For interfaces which do not vary in bandwidth or for those where no accurate estimation can be made, this object should contain the nominal bandwidth.")
ap64ifPhysAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 6), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64ifPhysAddress.setStatus('current')
if mibBuilder.loadTexts: ap64ifPhysAddress.setDescription("The interface's address at the protocol layer immediately `below' the network layer in the protocol stack. For interfaces which do not have such an address (e.g., a serial line), this object should contain an octet string of zero length.")
ap64ifAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64ifAdminStatus.setStatus('current')
if mibBuilder.loadTexts: ap64ifAdminStatus.setDescription('The desired state of the interface. The testing(3) state indicates that no operational packets can be passed.')
ap64ifOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64ifOperStatus.setStatus('current')
if mibBuilder.loadTexts: ap64ifOperStatus.setDescription('The current operational state of the interface. The testing(3) state indicates that no operational packets can be passed.')
ap64ifLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 9), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64ifLastChange.setStatus('current')
if mibBuilder.loadTexts: ap64ifLastChange.setDescription('The value of sysUpTime at the time the interface entered its current operational state. If the current state was entered prior to the last re- initialization of the local network management subsystem, then this object contains a zero value.')
ap64ifInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64ifInOctets.setStatus('current')
if mibBuilder.loadTexts: ap64ifInOctets.setDescription('The total number of octets received on the interface, including framing characters.')
ap64ifInUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64ifInUcastPkts.setStatus('current')
if mibBuilder.loadTexts: ap64ifInUcastPkts.setDescription('The number of subnetwork-unicast packets delivered to a higher-layer protocol.')
ap64ifInNUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64ifInNUcastPkts.setStatus('current')
if mibBuilder.loadTexts: ap64ifInNUcastPkts.setDescription('The number of non-unicast (i.e., subnetwork- broadcast or subnetwork-multicast) packets delivered to a higher-layer protocol.')
ap64ifInDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64ifInDiscards.setStatus('current')
if mibBuilder.loadTexts: ap64ifInDiscards.setDescription('The number of inbound packets which were chosen to be discarded even though no errors had been detected to prevent their being deliverable to a higher-layer protocol. One possible reason for discarding such a packet could be to free up buffer space.')
ap64ifInErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64ifInErrors.setStatus('current')
if mibBuilder.loadTexts: ap64ifInErrors.setDescription('The number of inbound packets that contained errors preventing them from being deliverable to a higher-layer protocol.')
ap64ifInUnknownProtos = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64ifInUnknownProtos.setStatus('current')
if mibBuilder.loadTexts: ap64ifInUnknownProtos.setDescription('The number of packets received via the interface which were discarded because of an unknown or unsupported protocol.')
ap64ifOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64ifOutOctets.setStatus('current')
if mibBuilder.loadTexts: ap64ifOutOctets.setDescription('The total number of octets transmitted out of the interface, including framing characters.')
ap64ifOutUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64ifOutUcastPkts.setStatus('current')
if mibBuilder.loadTexts: ap64ifOutUcastPkts.setDescription('The total number of packets that higher-level protocols requested be transmitted to a subnetwork-unicast address, including those that were discarded or not sent.')
ap64ifOutNUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64ifOutNUcastPkts.setStatus('current')
if mibBuilder.loadTexts: ap64ifOutNUcastPkts.setDescription('The total number of packets that higher-level protocols requested be transmitted to a non- unicast (i.e., a subnetwork-broadcast or subnetwork-multicast) address, including those that were discarded or not sent.')
ap64ifOutDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64ifOutDiscards.setStatus('current')
if mibBuilder.loadTexts: ap64ifOutDiscards.setDescription('The number of outbound packets which were chosen to be discarded even though no errors had been detected to prevent their being transmitted. One possible reason for discarding such a packet could be to free up buffer space.')
ap64ifOutErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 20), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64ifOutErrors.setStatus('current')
if mibBuilder.loadTexts: ap64ifOutErrors.setDescription('The number of outbound packets that could not be transmitted because of errors.')
ap64ifOutQLen = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 21), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64ifOutQLen.setStatus('current')
if mibBuilder.loadTexts: ap64ifOutQLen.setDescription('The length of the output packet queue (in packets).')
ap64ifSpecific = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 3, 1, 22), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64ifSpecific.setStatus('current')
if mibBuilder.loadTexts: ap64ifSpecific.setDescription('A reference to MIB definitions specific to the particular media being used to realize the interface. For example, if the interface is realized by an ethernet, then the value of this object refers to a document defining objects specific to ethernet. If this information is not present, its value should be set to the OBJECT IDENTIFIER { 0 0 }, which is a syntatically valid object identifier, and any conformant implementation of ASN.1 and BER must be able to generate and recognize this value.')
ap64etherStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4), )
if mibBuilder.loadTexts: ap64etherStatsTable.setStatus('current')
if mibBuilder.loadTexts: ap64etherStatsTable.setDescription('A list of Ethernet statistics entries.')
ap64etherStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1), ).setIndexNames((0, "AP64STATS-MIB", "ap64etherStatsIndex"))
if mibBuilder.loadTexts: ap64etherStatsEntry.setStatus('current')
if mibBuilder.loadTexts: ap64etherStatsEntry.setDescription('A collection of statistics kept for a particular Ethernet interface. As an example, an instance of the etherStatsPkts object might be named etherStatsPkts.1')
ap64etherStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64etherStatsIndex.setStatus('current')
if mibBuilder.loadTexts: ap64etherStatsIndex.setDescription('The value of this object uniquely identifies this etherStats entry.')
ap64etherStatsDataSource = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64etherStatsDataSource.setStatus('current')
if mibBuilder.loadTexts: ap64etherStatsDataSource.setDescription('This object identifies the source of the data that this etherStats entry is configured to analyze. This source can be any ethernet interface on this device. In order to identify a particular interface, this object shall identify the instance of the ifIndex object, defined in RFC 1213 and RFC 1573 [4,6], for the desired interface. For example, if an entry were to receive data from interface #1, this object would be set to ifIndex.1. The statistics in this group reflect all packets on the local network segment attached to the identified interface. An agent may or may not be able to tell if fundamental changes to the media of the interface have occurred and necessitate an invalidation of this entry. For example, a hot-pluggable ethernet card could be pulled out and replaced by a token-ring card. In such a case, if the agent has such knowledge of the change, it is recommended that it invalidate this entry. This object may not be modified if the associated etherStatsStatus object is equal to valid(1).')
ap64etherStatsDropEvents = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64etherStatsDropEvents.setStatus('current')
if mibBuilder.loadTexts: ap64etherStatsDropEvents.setDescription('The total number of events in which packets were dropped by the probe due to lack of resources. Note that this number is not necessarily the number of packets dropped; it is just the number of times this condition has been detected.')
ap64etherStatsOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64etherStatsOctets.setStatus('current')
if mibBuilder.loadTexts: ap64etherStatsOctets.setDescription('The total number of octets of data (including those in bad packets) received on the network (excluding framing bits but including FCS octets). This object can be used as a reasonable estimate of ethernet utilization. If greater precision is desired, the etherStatsPkts and etherStatsOctets objects should be sampled before and after a common interval. The differences in the sampled values are Pkts and Octets, respectively, and the number of seconds in the interval is Interval. These values are used to calculate the Utilization as follows: Pkts * (9.6 + 6.4) + (Octets * .8) Utilization = ------------------------------------- Interval * 10,000 The result of this equation is the value Utilization which is the percent utilization of the ethernet segment on a scale of 0 to 100 percent.')
ap64etherStatsPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64etherStatsPkts.setStatus('current')
if mibBuilder.loadTexts: ap64etherStatsPkts.setDescription('The total number of packets (including bad packets, broadcast packets, and multicast packets) received.')
ap64etherStatsBroadcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64etherStatsBroadcastPkts.setStatus('current')
if mibBuilder.loadTexts: ap64etherStatsBroadcastPkts.setDescription('The total number of good packets received that were directed to the broadcast address. Note that this does not include multicast packets.')
ap64etherStatsMulticastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64etherStatsMulticastPkts.setStatus('current')
if mibBuilder.loadTexts: ap64etherStatsMulticastPkts.setDescription('The total number of good packets received that were directed to a multicast address. Note that this number does not include packets directed to the broadcast address.')
ap64etherStatsCRCAlignErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64etherStatsCRCAlignErrors.setStatus('current')
if mibBuilder.loadTexts: ap64etherStatsCRCAlignErrors.setDescription('The total number of packets received that had a length (excluding framing bits, but including FCS octets) of between 64 and 1518 octets, inclusive, but but had either a bad Frame Check Sequence (FCS) with an integral number of octets (FCS Error) or a bad FCS with a non-integral number of octets (Alignment Error).')
ap64etherStatsUndersizePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64etherStatsUndersizePkts.setStatus('current')
if mibBuilder.loadTexts: ap64etherStatsUndersizePkts.setDescription('The total number of packets received that were less than 64 octets long (excluding framing bits, but including FCS octets) and were otherwise well formed.')
ap64etherStatsOversizePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64etherStatsOversizePkts.setStatus('current')
if mibBuilder.loadTexts: ap64etherStatsOversizePkts.setDescription('The total number of packets received that were longer than 1518 octets (excluding framing bits, but including FCS octets) and were otherwise well formed.')
ap64etherStatsFragments = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64etherStatsFragments.setStatus('current')
if mibBuilder.loadTexts: ap64etherStatsFragments.setDescription('The total number of packets received that were less than 64 octets in length (excluding framing bits but including FCS octets) and had either a bad Frame Check Sequence (FCS) with an integral number of octets (FCS Error) or a bad FCS with a non-integral number of octets (Alignment Error). Note that it is entirely normal for ap64etherStatsFragments to increment. This is because it counts both runts (which are normal occurrences due to collisions) and noise hits.')
ap64etherStatsJabbers = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64etherStatsJabbers.setStatus('current')
if mibBuilder.loadTexts: ap64etherStatsJabbers.setDescription('The total number of packets received that were longer than 1518 octets (excluding framing bits, but including FCS octets), and had either a bad Frame Check Sequence (FCS) with an integral number of octets (FCS Error) or a bad FCS with a non-integral number of octets (Alignment Error). Note that this definition of jabber is different than the definition in IEEE-802.3 section 8.2.1.5 (10BASE5) and section 10.3.1.4 (10BASE2). These documents define jabber as the condition where any packet exceeds 20 ms. The allowed range to detect jabber is between 20 ms and 150 ms.')
ap64etherStatsCollisions = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64etherStatsCollisions.setStatus('current')
if mibBuilder.loadTexts: ap64etherStatsCollisions.setDescription('The best estimate of the total number of collisions on this Ap64ethernet segment. The value returned will depend on the location of the RMON probe. Section 8.2.1.3 (10BASE-5) and section 10.3.1.3 (10BASE-2) of IEEE standard 802.3 states that a station must detect a collision, in the receive mode, if three or more stations are transmitting simultaneously. A repeater port must detect a collision when two or more stations are transmitting simultaneously. Thus a probe placed on a repeater port could record more collisions than a probe connected to a station on the same segment would. Probe location plays a much smaller role when considering 10BASE-T. 14.2.1.4 (10BASE-T) of IEEE standard 802.3 defines a collision as the simultaneous presence of signals on the DO and RD circuits (transmitting and receiving at the same time). A 10BASE-T station can only detect collisions when it is transmitting. Thus probes placed on a station and a repeater, should report the same number of collisions. Note also that an RMON probe inside a repeater should ideally report collisions between the repeater and one or more other hosts (transmit collisions as defined by IEEE 802.3k) plus receiver collisions observed on any coax segments to which the repeater is connected.')
ap64etherStatsPkts64Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64etherStatsPkts64Octets.setStatus('current')
if mibBuilder.loadTexts: ap64etherStatsPkts64Octets.setDescription('The total number of packets (including bad packets) received that were 64 octets in length (excluding framing bits but including FCS octets).')
ap64etherStatsPkts65to127Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64etherStatsPkts65to127Octets.setStatus('current')
if mibBuilder.loadTexts: ap64etherStatsPkts65to127Octets.setDescription('The total number of packets (including bad packets) received that were between 65 and 127 octets in length inclusive (excluding framing bits but including FCS octets).')
ap64etherStatsPkts128to255Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64etherStatsPkts128to255Octets.setStatus('current')
if mibBuilder.loadTexts: ap64etherStatsPkts128to255Octets.setDescription('The total number of packets (including bad packets) received that were between 128 and 255 octets in length inclusive (excluding framing bits but including FCS octets).')
ap64etherStatsPkts256to511Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64etherStatsPkts256to511Octets.setStatus('current')
if mibBuilder.loadTexts: ap64etherStatsPkts256to511Octets.setDescription('The total number of packets (including bad packets) received that were between 256 and 511 octets in length inclusive (excluding framing bits but including FCS octets).')
ap64etherStatsPkts512to1023Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64etherStatsPkts512to1023Octets.setStatus('current')
if mibBuilder.loadTexts: ap64etherStatsPkts512to1023Octets.setDescription('The total number of packets (including bad packets) received that were between 512 and 1023 octets in length inclusive (excluding framing bits but including FCS octets).')
ap64etherStatsPkts1024to1518Octets = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64etherStatsPkts1024to1518Octets.setStatus('current')
if mibBuilder.loadTexts: ap64etherStatsPkts1024to1518Octets.setDescription('The total number of packets (including bad packets) received that were between 1024 and 1518 octets in length inclusive (excluding framing bits but including FCS octets).')
ap64etherStatsOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 20), OwnerString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64etherStatsOwner.setStatus('current')
if mibBuilder.loadTexts: ap64etherStatsOwner.setDescription('The entity that configured this entry and is therefore using the resources assigned to it.')
ap64etherStatsStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2467, 1, 44, 4, 1, 21), EntryStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ap64etherStatsStatus.setStatus('current')
if mibBuilder.loadTexts: ap64etherStatsStatus.setDescription('The status of this ap64etherStats entry.')
mibBuilder.exportSymbols("AP64STATS-MIB", ap64dot3StatsSQETestErrors=ap64dot3StatsSQETestErrors, ap64dot3StatsExcessiveCollisions=ap64dot3StatsExcessiveCollisions, ap64ifTable=ap64ifTable, ap64ifMtu=ap64ifMtu, ap64ifInNUcastPkts=ap64ifInNUcastPkts, ap64ifOutNUcastPkts=ap64ifOutNUcastPkts, OwnerString=OwnerString, ap64ifOperStatus=ap64ifOperStatus, ap64ifInErrors=ap64ifInErrors, ap64etherStatsOwner=ap64etherStatsOwner, ap64dot3StatsLateCollisions=ap64dot3StatsLateCollisions, ap64dot3StatsCarrierSenseErrors=ap64dot3StatsCarrierSenseErrors, ap64ifInUcastPkts=ap64ifInUcastPkts, ap64dot3StatsIndex=ap64dot3StatsIndex, ap64etherStatsDropEvents=ap64etherStatsDropEvents, ap64ifPhysAddress=ap64ifPhysAddress, ap64etherStatsStatus=ap64etherStatsStatus, ap64StatsMib=ap64StatsMib, ap64etherStatsPkts=ap64etherStatsPkts, ap64etherStatsPkts512to1023Octets=ap64etherStatsPkts512to1023Octets, EntryStatus=EntryStatus, ap64etherStatsOctets=ap64etherStatsOctets, ap64etherStatsJabbers=ap64etherStatsJabbers, ap64etherStatsIndex=ap64etherStatsIndex, ap64ifInOctets=ap64ifInOctets, ap64ifOutOctets=ap64ifOutOctets, ap64etherStatsPkts1024to1518Octets=ap64etherStatsPkts1024to1518Octets, ap64ifIndex=ap64ifIndex, ap64ifInDiscards=ap64ifInDiscards, ap64dot3StatsTable=ap64dot3StatsTable, PYSNMP_MODULE_ID=ap64StatsMib, ap64ifInUnknownProtos=ap64ifInUnknownProtos, ap64ifOutQLen=ap64ifOutQLen, ap64etherStatsPkts64Octets=ap64etherStatsPkts64Octets, ap64ifEntry=ap64ifEntry, ap64etherStatsPkts65to127Octets=ap64etherStatsPkts65to127Octets, ap64dot3StatsDeferredTransmissions=ap64dot3StatsDeferredTransmissions, ap64etherStatsPkts128to255Octets=ap64etherStatsPkts128to255Octets, ap64etherStatsMulticastPkts=ap64etherStatsMulticastPkts, ap64dot3StatsFCSErrors=ap64dot3StatsFCSErrors, ap64ifOutErrors=ap64ifOutErrors, ap64ifLastChange=ap64ifLastChange, ap64ifType=ap64ifType, ap64etherStatsDataSource=ap64etherStatsDataSource, ap64etherStatsCollisions=ap64etherStatsCollisions, ap64etherStatsPkts256to511Octets=ap64etherStatsPkts256to511Octets, ap64etherStatsEntry=ap64etherStatsEntry, ap64ifDescr=ap64ifDescr, ap64etherStatsBroadcastPkts=ap64etherStatsBroadcastPkts, ap64dot3StatsFrameTooLongs=ap64dot3StatsFrameTooLongs, ap64etherStatsFragments=ap64etherStatsFragments, ap64ifSpecific=ap64ifSpecific, ap64etherStatsCRCAlignErrors=ap64etherStatsCRCAlignErrors, ap64etherStatsOversizePkts=ap64etherStatsOversizePkts, ap64etherStatsTable=ap64etherStatsTable, ap64dot3StatsSingleCollisionFrames=ap64dot3StatsSingleCollisionFrames, ap64dot3StatsInternalMacReceiveErrors=ap64dot3StatsInternalMacReceiveErrors, ap64ifOutDiscards=ap64ifOutDiscards, ap64dot3StatsInternalMacTransmitErrors=ap64dot3StatsInternalMacTransmitErrors, ap64dot3StatsEntry=ap64dot3StatsEntry, PhysAddress=PhysAddress, ap64etherStatsUndersizePkts=ap64etherStatsUndersizePkts, ap64dot3StatsAlignmentErrors=ap64dot3StatsAlignmentErrors, ap64ifSpeed=ap64ifSpeed, ap64ifOutUcastPkts=ap64ifOutUcastPkts, ap64dot3StatsMultipleCollisionFrames=ap64dot3StatsMultipleCollisionFrames, ap64ifAdminStatus=ap64ifAdminStatus)