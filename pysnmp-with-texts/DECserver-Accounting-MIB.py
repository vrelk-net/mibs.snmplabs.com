#
# PySNMP MIB module DECserver-Accounting-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DECserver-Accounting-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:37:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
sysUpTime, = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime")
IpAddress, enterprises, Integer32, NotificationType, MibIdentifier, Unsigned32, TimeTicks, Counter64, ObjectIdentity, Counter32, NotificationType, Bits, ModuleIdentity, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "enterprises", "Integer32", "NotificationType", "MibIdentifier", "Unsigned32", "TimeTicks", "Counter64", "ObjectIdentity", "Counter32", "NotificationType", "Bits", "ModuleIdentity", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
private = MibIdentifier((1, 3, 6, 1, 4, 1, 1))
dec = MibIdentifier((1, 3, 6, 1, 4, 1, 1, 36))
ema = MibIdentifier((1, 3, 6, 1, 4, 1, 1, 36, 2))
mib_extensions_1 = MibIdentifier((1, 3, 6, 1, 4, 1, 1, 36, 2, 18)).setLabel("mib-extensions-1")
decServeraccounting = MibIdentifier((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12))
acctSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 1))
acctConsole = MibScalar((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acctConsole.setStatus('mandatory')
if mibBuilder.loadTexts: acctConsole.setDescription("This object controls whether the managed system displays the accounting events to the server's console port as they occur. The value disable(1) means that it does not. The value enable(2) means that it does. The value of this object persists across power cycles and reboots. Setting takes effect immediately.")
acctAdminLogSize = MibScalar((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("none", 1), ("size4K", 2), ("size8K", 3), ("size16K", 4), ("size32K", 5), ("size64K", 6), ("size128K", 7), ("size256K", 8), ("size512K", 9))).clone('size16K')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acctAdminLogSize.setStatus('mandatory')
if mibBuilder.loadTexts: acctAdminLogSize.setDescription('This object controls the total number of bytes the managed system allocates for all accounting records. The value size4K(1) means the managed system allocates 4K bytes for the accounting table, etc. The value of this object persists across power cycles and reboots of the managed system. Setting it via SNMP has no effect until the managed system again reboots.')
acctOperLogSize = MibScalar((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("none", 1), ("size4K", 2), ("size8K", 3), ("size16K", 4), ("size32K", 5), ("size64K", 6), ("size128K", 7), ("size256K", 8), ("size512K", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acctOperLogSize.setStatus('mandatory')
if mibBuilder.loadTexts: acctOperLogSize.setDescription('This object specifies the total number of bytes the managed system has allocated for all accounting records. The value size4K(1) means the managed system allocated 4K bytes for the accounting table, etc.')
acctThreshold = MibScalar((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("end", 2), ("half", 3), ("quarter", 4), ("eighth", 5))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acctThreshold.setStatus('mandatory')
if mibBuilder.loadTexts: acctThreshold.setDescription('This object controls when the managed system generates an accounting trap. A trap will be generated by the managed system whenever logging another record will take it beyond the specified physical points in the log. For example, the value quarter(4) causes the managed system to generate a trap when logging an entry takes it beyond the 1/4, 1/2, 3/4, or end of the log. The managed system maintains the value of this object across power-cycles and reboots, although setting it changes the behavior of the managed system immediately.')
acctTable = MibTable((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2), )
if mibBuilder.loadTexts: acctTable.setStatus('mandatory')
if mibBuilder.loadTexts: acctTable.setDescription('The list of all accounting records at this managed system.')
acctEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2, 1), ).setIndexNames((0, "DECserver-Accounting-MIB", "acctEntryNonce1"), (0, "DECserver-Accounting-MIB", "acctEntryNonce2"))
if mibBuilder.loadTexts: acctEntry.setStatus('mandatory')
if mibBuilder.loadTexts: acctEntry.setDescription('An accounting record for this managed system. The system automatically creates this record in response to an action which accounting requires to be logged.')
acctEntryNonce1 = MibTableColumn((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acctEntryNonce1.setStatus('mandatory')
if mibBuilder.loadTexts: acctEntryNonce1.setDescription("A number which, in combination with acctNonce2, distinguishes this object's entry from all others.")
acctEntryNonce2 = MibTableColumn((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acctEntryNonce2.setStatus('mandatory')
if mibBuilder.loadTexts: acctEntryNonce2.setDescription("A number which, in combination with acctNonce1, distinguishes this object's entry from all others.")
acctEntryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acctEntryTime.setStatus('mandatory')
if mibBuilder.loadTexts: acctEntryTime.setDescription('The value of the MIB-II sysUpTime object at which the managed system created this accounting log entry.')
acctEntryEvent = MibScalar((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))).clone(namedValues=NamedValues(("other", 1), ("logIn", 2), ("logOut", 3), ("sessionConnect", 4), ("sessionDisconnect", 5), ("kerberosPasswordFail", 6), ("privilegedPasswordFail", 7), ("maintenancePasswordFail", 8), ("loginPasswordFail", 9), ("remotePasswordFail", 10), ("communityFail", 11), ("privilegedPasswordModified", 12), ("maintenacePasswordModified", 13), ("loginPasswordModified", 14), ("remotePasswordModified", 15), ("privilegeLevelModified", 16), ("communityModified", 17)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acctEntryEvent.setStatus('mandatory')
if mibBuilder.loadTexts: acctEntryEvent.setDescription('This object identifies the record type associated with its entry. The value logIn(2) identifies the entry as a log-in record. The value logOut(3) identifies the entry as a log-out record. The value sessionConnect(4) means the entry is a connect attempt record. The value sessionDisconnect(5) means the record is a disconnect record. For all password fail events (6-10), the value identifies the entry as a record flagging a failure to correctly provide the associated password. The value communityFail(11) identifies the record as flagging a failure to provide a valid community in an SNMP request. For all password modify events (12-16), the value identifies the entry as a record flagging a modification to an associated password. The value communityModified(17) indicates that the SNMP community data base at the managed system has been modified. The value other(1) indicates that some other event has occured.')
acctEntryPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acctEntryPort.setStatus('mandatory')
if mibBuilder.loadTexts: acctEntryPort.setDescription('The port to which this entry applies. Its value is -1 when the managed system can associate the record with no port.')
acctEntryUser = MibTableColumn((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acctEntryUser.setStatus('mandatory')
if mibBuilder.loadTexts: acctEntryUser.setDescription('The username associated with the logged-in port. If the managed system can attribute no name to the entry, the value of this object is the NULL string.')
acctEntrySessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acctEntrySessionId.setStatus('mandatory')
if mibBuilder.loadTexts: acctEntrySessionId.setDescription("The id of the session associated with this record. If the managed system associates no session with this accounting record, this object's value is -1.")
acctEntryProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("none", 1), ("lat", 2), ("telnet", 3), ("slip", 4), ("ping", 5), ("mop", 6), ("ppp", 7), ("tn3270", 8), ("autolink", 9), ("snmp-ip", 10), ("other", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acctEntryProtocol.setStatus('mandatory')
if mibBuilder.loadTexts: acctEntryProtocol.setDescription('This object indicates the protocol associated with its entry. Its value is none(1) when the entry is not a connect or disconnect record. The value other(11) applies to other session types than the ones specified above.')
acctEntryAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notApplicable", 1), ("local", 2), ("remote", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acctEntryAccess.setStatus('mandatory')
if mibBuilder.loadTexts: acctEntryAccess.setDescription("This object indicates its entry's access. The value local(2) means the record is associated with a local access log-in or session connect. The value remote(3) indicates the record is associated with a remote access log-in or session connect. The value notApplicable(1) means the entry is not a log-in or session connection record.")
acctEntryPeer = MibTableColumn((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acctEntryPeer.setStatus('mandatory')
if mibBuilder.loadTexts: acctEntryPeer.setDescription('This object identifies the peer associated with the session connect, maintenance password fail or community fail events. The value is the NULL string for entries corresponding to other record types.')
acctEntryReason = MibTableColumn((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("notApplicable", 1), ("normal", 2), ("error", 3), ("other", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acctEntryReason.setStatus('mandatory')
if mibBuilder.loadTexts: acctEntryReason.setDescription('This object indicates the session disconnect reason for its entry. The value notApplicable(1) means that it is not a session disconnect event. The value normal(2) means that the session disconnect occured under normal circumstances. The value error(3) means that an error or some abnormal event occured to disconnect the session. The value other(4) applies to other disconnect reasons.')
acctEntrySentBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acctEntrySentBytes.setStatus('mandatory')
if mibBuilder.loadTexts: acctEntrySentBytes.setDescription("The number of bytes sent when this object's entry represents a session disconnect or logout, and 0 otherwise.")
acctEntryReceivedBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acctEntryReceivedBytes.setStatus('mandatory')
if mibBuilder.loadTexts: acctEntryReceivedBytes.setDescription("The number of bytes received when this object's entry represents a session disconnect or logout, and 0 otherwise.")
acctTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 3))
acctThresholdExceeded = NotificationType((1, 3, 6, 1, 4, 1, 1, 36, 2, 18, 12, 3) + (0,1)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("DECserver-Accounting-MIB", "acctThreshold"))
if mibBuilder.loadTexts: acctThresholdExceeded.setDescription('This trap reports that the managed system has crossed the configured threshold.')
mibBuilder.exportSymbols("DECserver-Accounting-MIB", acctSystem=acctSystem, acctEntryEvent=acctEntryEvent, decServeraccounting=decServeraccounting, acctEntryProtocol=acctEntryProtocol, acctTable=acctTable, acctAdminLogSize=acctAdminLogSize, acctEntryAccess=acctEntryAccess, ema=ema, acctEntryUser=acctEntryUser, acctEntryPort=acctEntryPort, acctOperLogSize=acctOperLogSize, private=private, acctEntryPeer=acctEntryPeer, acctThresholdExceeded=acctThresholdExceeded, acctEntry=acctEntry, acctEntrySessionId=acctEntrySessionId, acctEntryReceivedBytes=acctEntryReceivedBytes, acctEntryNonce2=acctEntryNonce2, acctConsole=acctConsole, acctEntryReason=acctEntryReason, acctEntryNonce1=acctEntryNonce1, acctTraps=acctTraps, acctEntryTime=acctEntryTime, acctEntrySentBytes=acctEntrySentBytes, dec=dec, acctThreshold=acctThreshold, mib_extensions_1=mib_extensions_1)