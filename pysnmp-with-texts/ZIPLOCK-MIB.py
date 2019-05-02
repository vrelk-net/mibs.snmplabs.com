#
# PySNMP MIB module ZIPLOCK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZIPLOCK-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:48:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ctResource, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctResource")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, ObjectIdentity, Counter32, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Unsigned32, Counter64, IpAddress, NotificationType, iso, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "Counter32", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Unsigned32", "Counter64", "IpAddress", "NotificationType", "iso", "Bits", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ctZiplock = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 3))
ctZiplockTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 3, 1), )
if mibBuilder.loadTexts: ctZiplockTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctZiplockTable.setDescription('Table containing Ziplock daughter board information including presence, revision and status')
ctZiplockEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 3, 1, 1), ).setIndexNames((0, "ZIPLOCK-MIB", "ctZiplockNumber"))
if mibBuilder.loadTexts: ctZiplockEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctZiplockEntry.setDescription('Ziplock daughter board information.')
ctZiplockNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctZiplockNumber.setStatus('mandatory')
if mibBuilder.loadTexts: ctZiplockNumber.setDescription('This object provides an index into the Ziplock Table. and represents the Ziplock daughter board number.')
ctZiplockPresence = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctZiplockPresence.setStatus('mandatory')
if mibBuilder.loadTexts: ctZiplockPresence.setDescription('This object indicates the presence of a Ziplock daughter board on the host platform. 1 indicates presence, 2 indicates absence.')
ctZiplockRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 3, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctZiplockRevision.setStatus('mandatory')
if mibBuilder.loadTexts: ctZiplockRevision.setDescription('This object represents the hardware revision of the Ziplock daughter board.')
ctZiplockStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 3, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctZiplockStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ctZiplockStatus.setDescription('This object indicates the status of the Ziplock daughter board. 1=GOOD, 2=BAD, 3=UNKNOWN.')
mibBuilder.exportSymbols("ZIPLOCK-MIB", ctZiplock=ctZiplock, ctZiplockStatus=ctZiplockStatus, ctZiplockRevision=ctZiplockRevision, ctZiplockPresence=ctZiplockPresence, ctZiplockNumber=ctZiplockNumber, ctZiplockEntry=ctZiplockEntry, ctZiplockTable=ctZiplockTable)