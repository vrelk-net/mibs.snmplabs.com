#
# PySNMP MIB module BAY-STACK-ERROR-MESSAGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BAY-STACK-ERROR-MESSAGE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:35:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, NotificationType, Unsigned32, Counter32, Gauge32, ModuleIdentity, Bits, MibIdentifier, TimeTicks, Counter64, iso, ObjectIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "NotificationType", "Unsigned32", "Counter32", "Gauge32", "ModuleIdentity", "Bits", "MibIdentifier", "TimeTicks", "Counter64", "iso", "ObjectIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bayStackMibs, = mibBuilder.importSymbols("SYNOPTICS-ROOT-MIB", "bayStackMibs")
bayStackErrorMessageMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 5, 19))
bayStackErrorMessageMib.setRevisions(('2013-10-11 00:00', '2006-11-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bayStackErrorMessageMib.setRevisionsDescriptions(('Version 2: Added DisplayString to IMPORTS.', 'Version 1: Initial version.',))
if mibBuilder.loadTexts: bayStackErrorMessageMib.setLastUpdated('201310110000Z')
if mibBuilder.loadTexts: bayStackErrorMessageMib.setOrganization('Nortel Networks')
if mibBuilder.loadTexts: bayStackErrorMessageMib.setContactInfo('')
if mibBuilder.loadTexts: bayStackErrorMessageMib.setDescription('General BayStack MIB.')
bsemObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 19, 1))
bsemErrorMessageTable = MibTable((1, 3, 6, 1, 4, 1, 45, 5, 19, 1, 1), )
if mibBuilder.loadTexts: bsemErrorMessageTable.setStatus('current')
if mibBuilder.loadTexts: bsemErrorMessageTable.setDescription('This table contains error messages for failed SNMP Set requests.')
bsemErrorMessageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 5, 19, 1, 1, 1), ).setIndexNames((0, "BAY-STACK-ERROR-MESSAGE-MIB", "bsemErrorMessageAddressType"), (0, "BAY-STACK-ERROR-MESSAGE-MIB", "bsemErrorMessageAddress"), (0, "BAY-STACK-ERROR-MESSAGE-MIB", "bsemErrorMessageRequestId"))
if mibBuilder.loadTexts: bsemErrorMessageEntry.setStatus('current')
if mibBuilder.loadTexts: bsemErrorMessageEntry.setDescription('An error message for a failed SNMP Set request.')
bsemErrorMessageAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 19, 1, 1, 1, 1), InetAddressType())
if mibBuilder.loadTexts: bsemErrorMessageAddressType.setStatus('current')
if mibBuilder.loadTexts: bsemErrorMessageAddressType.setDescription('The type of address contained in bsemErrorMessageAddress.')
bsemErrorMessageAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 19, 1, 1, 1, 2), InetAddress())
if mibBuilder.loadTexts: bsemErrorMessageAddress.setStatus('current')
if mibBuilder.loadTexts: bsemErrorMessageAddress.setDescription('The IP address from which the failed SNMP Set request was received.')
bsemErrorMessageRequestId = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 19, 1, 1, 1, 3), Unsigned32())
if mibBuilder.loadTexts: bsemErrorMessageRequestId.setStatus('current')
if mibBuilder.loadTexts: bsemErrorMessageRequestId.setDescription('The request-id of the Set request PDU that failed.')
bsemErrorMessageString = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 5, 19, 1, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bsemErrorMessageString.setStatus('current')
if mibBuilder.loadTexts: bsemErrorMessageString.setDescription('The error message for the failed Set request.')
mibBuilder.exportSymbols("BAY-STACK-ERROR-MESSAGE-MIB", bsemObjects=bsemObjects, bsemErrorMessageRequestId=bsemErrorMessageRequestId, bsemErrorMessageEntry=bsemErrorMessageEntry, bayStackErrorMessageMib=bayStackErrorMessageMib, bsemErrorMessageString=bsemErrorMessageString, bsemErrorMessageAddress=bsemErrorMessageAddress, PYSNMP_MODULE_ID=bayStackErrorMessageMib, bsemErrorMessageTable=bsemErrorMessageTable, bsemErrorMessageAddressType=bsemErrorMessageAddressType)