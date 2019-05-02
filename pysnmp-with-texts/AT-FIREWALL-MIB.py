#
# PySNMP MIB module AT-FIREWALL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AT-FIREWALL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:29:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
DisplayStringUnsized, modules = mibBuilder.importSymbols("AT-SMI-MIB", "DisplayStringUnsized", "modules")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Gauge32, ObjectIdentity, Counter32, Bits, Counter64, Integer32, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ModuleIdentity, iso, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Gauge32", "ObjectIdentity", "Counter32", "Bits", "Counter64", "Integer32", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ModuleIdentity", "iso", "IpAddress")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
firewall = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 77))
firewall.setRevisions(('2006-06-28 12:22',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: firewall.setRevisionsDescriptions(('Initial Revision',))
if mibBuilder.loadTexts: firewall.setLastUpdated('200606281222Z')
if mibBuilder.loadTexts: firewall.setOrganization('Allied Telesis, Inc')
if mibBuilder.loadTexts: firewall.setContactInfo('http://www.alliedtelesis.com')
if mibBuilder.loadTexts: firewall.setDescription('This MIB file contains definitions of managed objects for the FIREWALL module. ')
firewallTrapMessage = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 77, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: firewallTrapMessage.setStatus('current')
if mibBuilder.loadTexts: firewallTrapMessage.setDescription('The last message sent in a firewall TRAP. This variable is really just a placeholder for the object sent in the firewall TRAP, but can be read independently if required. Note however that a new TRAP will cause this variable to be overwritten.')
firewallTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 77, 0))
firewallAttackTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 77, 0, 1)).setObjects(("AT-FIREWALL-MIB", "firewallTrapMessage"))
if mibBuilder.loadTexts: firewallAttackTrap.setStatus('current')
if mibBuilder.loadTexts: firewallAttackTrap.setDescription('A firewall trap is generated when the firewall detects an intrusion or attack and notifies the router manager. Firewall trap notifications are enabled with the command ENABLE FIREWALL NOTIFY=SNMP.')
firewallSessionsStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 77, 2))
totalNumberOfSessions = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 77, 2, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: totalNumberOfSessions.setStatus('mandatory')
if mibBuilder.loadTexts: totalNumberOfSessions.setDescription('The total number of sessions going through the firewall. It will be the sum of the number of sessions on all individual nodes.')
numberOfSessionsPerNodeCountingStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 77, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: numberOfSessionsPerNodeCountingStatus.setStatus('mandatory')
if mibBuilder.loadTexts: numberOfSessionsPerNodeCountingStatus.setDescription('The status of counting the number of sessions per node, ie, when this particular ferture is on, the status will be enabled, other wise it will be disabled, which is the default status.')
numberOfSessionsPerNodeTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 77, 2, 3), )
if mibBuilder.loadTexts: numberOfSessionsPerNodeTable.setStatus('current')
if mibBuilder.loadTexts: numberOfSessionsPerNodeTable.setDescription('This is a table of nodes in the network with their corresponding ip address and number of sessions')
numberOfSessionsPerNodeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 77, 2, 3, 1), ).setIndexNames((0, "AT-FIREWALL-MIB", "nodeIpAddress"))
if mibBuilder.loadTexts: numberOfSessionsPerNodeEntry.setStatus('current')
if mibBuilder.loadTexts: numberOfSessionsPerNodeEntry.setDescription('An entry includes the information about a node and numbers of sessions belongs to it.')
nodeIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 77, 2, 3, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nodeIpAddress.setStatus('current')
if mibBuilder.loadTexts: nodeIpAddress.setDescription('The ip address of each node that has firewall limit rules attached and needs to be monitored')
numberOfSessionsPerNode = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 77, 2, 3, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numberOfSessionsPerNode.setStatus('current')
if mibBuilder.loadTexts: numberOfSessionsPerNode.setDescription('Number of active sessions created by the corresponding node')
mibBuilder.exportSymbols("AT-FIREWALL-MIB", numberOfSessionsPerNodeTable=numberOfSessionsPerNodeTable, numberOfSessionsPerNode=numberOfSessionsPerNode, firewallAttackTrap=firewallAttackTrap, firewall=firewall, PYSNMP_MODULE_ID=firewall, firewallSessionsStatistics=firewallSessionsStatistics, totalNumberOfSessions=totalNumberOfSessions, numberOfSessionsPerNodeCountingStatus=numberOfSessionsPerNodeCountingStatus, nodeIpAddress=nodeIpAddress, firewallTraps=firewallTraps, numberOfSessionsPerNodeEntry=numberOfSessionsPerNodeEntry, firewallTrapMessage=firewallTrapMessage)