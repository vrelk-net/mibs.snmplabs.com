#
# PySNMP MIB module RTM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RTM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:18:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
stratacom, = mibBuilder.importSymbols("CISCOWAN-SMI", "stratacom")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Counter32, IpAddress, ModuleIdentity, Unsigned32, MibIdentifier, NotificationType, Integer32, TimeTicks, Bits, iso, Gauge32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Counter32", "IpAddress", "ModuleIdentity", "Unsigned32", "MibIdentifier", "NotificationType", "Integer32", "TimeTicks", "Bits", "iso", "Gauge32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rtm = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 120))
trapsConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 120, 1))
trapConfigTable = MibTable((1, 3, 6, 1, 4, 1, 351, 120, 1, 1), )
if mibBuilder.loadTexts: trapConfigTable.setStatus('mandatory')
if mibBuilder.loadTexts: trapConfigTable.setDescription('The trap configuration table. This table is used for registering SNMP managers with the system. The system will send traps only to the registered SNMP mangers.')
trapConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 120, 1, 1, 1), ).setIndexNames((0, "RTM-MIB", "managerIPaddress"))
if mibBuilder.loadTexts: trapConfigEntry.setStatus('mandatory')
if mibBuilder.loadTexts: trapConfigEntry.setDescription('An entry for each of the SNMP Manager registered. Each SNMP Manager is identified by its IP Address specified in managerIPAddress object.')
managerIPaddress = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 120, 1, 1, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: managerIPaddress.setStatus('mandatory')
if mibBuilder.loadTexts: managerIPaddress.setDescription('A unique index value representing the SNMP manager.')
managerPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 120, 1, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: managerPortNumber.setStatus('mandatory')
if mibBuilder.loadTexts: managerPortNumber.setDescription('The UDP Port number on which the manager receives traps from a system.')
managerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 120, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("addRow", 1), ("delRow", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: managerRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: managerRowStatus.setDescription("This object is used for adding(registering) and deleting(de-registering) SNMP managers in the system. By setting this object to 'addRow' snmp manager will be registered with the system. By setting this object to 'delRow' snmp manager will be registered with the system. In some systems, the SNMP Manager will be de-registered automatically by the agent (to allow other SNMP managers to register), if manager is idle for long time( This time is called aging interval time). In order to avoid Managers being de-registered automatically it is expected that the SNMP Managers keep sending keep-alive requests(SNMP GET on this object) to the system for predefined interval(Choosen by SNMP Manager). The keep-alive requests need to be sent few minutes before the aging interval expires. The aging value of the Registered Managers are in the order of minutes(system dependent or user configured). The value supported for the aging value is system dependent. The system might support aging value per manager basis or per node basis (applicable to all the registered managers). ")
readingTrapsFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 120, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("false", 1), ("true", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: readingTrapsFlag.setStatus('mandatory')
if mibBuilder.loadTexts: readingTrapsFlag.setDescription("An entry for the state of the manager. The value 'false' indicates that SNMP manager is not in the middle of uploading traps(via trapUploadTable). The value 'true' indicates that SNMP manager is in the middle of uploading traps(via trapUploadTable). When the value is 'true' the system will not send traps to the corresponding manager identified by managerIPAddress object.")
nextTrapSeqNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 120, 1, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nextTrapSeqNum.setStatus('mandatory')
if mibBuilder.loadTexts: nextTrapSeqNum.setDescription('Set by the manager to indicate the first trap(identified by this sequence number) it is interested in uploading. The agent increments this value when readingTrapsFlag is set to true(1) and SNMP Get is performed on trapUploadTable. The trapUploadTable entries returned depends upon this value. If there are no traps in the system with the the sequence number, the agent will set the value for this object to the head of FIFO(Saved traps) and return an error response.')
managerNumOfValidEntries = MibScalar((1, 3, 6, 1, 4, 1, 351, 120, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: managerNumOfValidEntries.setStatus('mandatory')
if mibBuilder.loadTexts: managerNumOfValidEntries.setDescription('The number of entries in trapConfigTable.')
lastSequenceNumber = MibScalar((1, 3, 6, 1, 4, 1, 351, 120, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastSequenceNumber.setStatus('mandatory')
if mibBuilder.loadTexts: lastSequenceNumber.setDescription('The sequence number of the last trap generated by the system. This object is used in each of the RTM Compliant trap definitions. The manager can figure out whether any trap is lost(missing) by comparing the lastSequenceNumber values received in last 2 traps.')
trapUploadTable = MibTable((1, 3, 6, 1, 4, 1, 351, 120, 1, 4), )
if mibBuilder.loadTexts: trapUploadTable.setStatus('mandatory')
if mibBuilder.loadTexts: trapUploadTable.setDescription('The trapUploadTable is used by the manager to retrieve missing(lost) traps using robust trap mechanism. The manager does a Get request on this table.')
trapUploadEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 120, 1, 4, 1), ).setIndexNames((0, "RTM-MIB", "trapManagerIPaddress"))
if mibBuilder.loadTexts: trapUploadEntry.setStatus('mandatory')
if mibBuilder.loadTexts: trapUploadEntry.setDescription('Manager does a Get request on the elements of this entry to upload missing traps.')
trapManagerIPaddress = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 120, 1, 4, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapManagerIPaddress.setStatus('mandatory')
if mibBuilder.loadTexts: trapManagerIPaddress.setDescription('IP address of the manager used as an index to the table. The value of this object must match with the value in the managerIPaddress object.')
trapSequenceNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 120, 1, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapSequenceNum.setStatus('mandatory')
if mibBuilder.loadTexts: trapSequenceNum.setDescription('The sequence number associated with the trap. This sequence number has to match with the value in lastSequenceNumber object embedded in trapPduString.')
trapPduString = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 120, 1, 4, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapPduString.setStatus('mandatory')
if mibBuilder.loadTexts: trapPduString.setDescription('Trap description string. This contains the Trap PDU that is stored in the system.')
endOfQueueFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 120, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("false", 1), ("true", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: endOfQueueFlag.setStatus('mandatory')
if mibBuilder.loadTexts: endOfQueueFlag.setDescription("Flag indicating the last trap saved in the system's FIFO queue.")
recoverTrapTable = MibTable((1, 3, 6, 1, 4, 1, 351, 120, 1, 5), )
if mibBuilder.loadTexts: recoverTrapTable.setStatus('mandatory')
if mibBuilder.loadTexts: recoverTrapTable.setDescription('A table containing information about the traps sent from the system/switch. The total number of traps stored in the switch is implementation specific. It is expected that systems supporting RTM Mechanism save atleast least 500 traps , so that NMS applications can recover the traps if they determined it to be lost.')
recoverTrapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 120, 1, 5, 1), ).setIndexNames((0, "RTM-MIB", "recoverTrapSequenceNum"))
if mibBuilder.loadTexts: recoverTrapEntry.setStatus('mandatory')
if mibBuilder.loadTexts: recoverTrapEntry.setDescription('The entry for each of the traps stored in the switch.')
recoverTrapSequenceNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 120, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: recoverTrapSequenceNum.setStatus('mandatory')
if mibBuilder.loadTexts: recoverTrapSequenceNum.setDescription("The sequence number associated with the trap. The system tries to find a matching entry in the list of traps stored. If there is a match, an valid entry returned with value for 'recoverTrapPduString' object.")
recoverTrapPduString = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 120, 1, 5, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readonly")
if mibBuilder.loadTexts: recoverTrapPduString.setStatus('mandatory')
if mibBuilder.loadTexts: recoverTrapPduString.setDescription('Trap description string. This contains the Trap PDU that is stored in the system.')
mibBuilder.exportSymbols("RTM-MIB", trapPduString=trapPduString, trapConfigEntry=trapConfigEntry, endOfQueueFlag=endOfQueueFlag, trapUploadTable=trapUploadTable, rtm=rtm, managerPortNumber=managerPortNumber, trapUploadEntry=trapUploadEntry, trapConfigTable=trapConfigTable, trapSequenceNum=trapSequenceNum, managerNumOfValidEntries=managerNumOfValidEntries, recoverTrapEntry=recoverTrapEntry, managerIPaddress=managerIPaddress, recoverTrapTable=recoverTrapTable, trapsConfig=trapsConfig, trapManagerIPaddress=trapManagerIPaddress, readingTrapsFlag=readingTrapsFlag, recoverTrapPduString=recoverTrapPduString, lastSequenceNumber=lastSequenceNumber, managerRowStatus=managerRowStatus, nextTrapSeqNum=nextTrapSeqNum, recoverTrapSequenceNum=recoverTrapSequenceNum)