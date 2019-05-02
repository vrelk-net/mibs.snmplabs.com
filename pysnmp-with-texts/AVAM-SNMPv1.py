#
# PySNMP MIB module AVAM-SNMPv1 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AVAM-SNMPv1
# Produced by pysmi-0.3.4 at Wed May  1 11:32:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
DateAndTime, = mibBuilder.importSymbols("HOST-RESOURCES-MIB", "DateAndTime")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, ModuleIdentity, ObjectIdentity, Gauge32, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, MibIdentifier, Counter64, NotificationType, NotificationType, Unsigned32, IpAddress, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ModuleIdentity", "ObjectIdentity", "Gauge32", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "MibIdentifier", "Counter64", "NotificationType", "NotificationType", "Unsigned32", "IpAddress", "enterprises")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
availant = MibIdentifier((1, 3, 6, 1, 4, 1, 5910))
avProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 5910, 1))
avamMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 5910, 1, 3))
avamVisObj = MibIdentifier((1, 3, 6, 1, 4, 1, 5910, 1, 3, 1))
avamNotify = MibIdentifier((1, 3, 6, 1, 4, 1, 5910, 1, 3, 2))
avVersionString = MibScalar((1, 3, 6, 1, 4, 1, 5910, 1, 3, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avVersionString.setStatus('mandatory')
if mibBuilder.loadTexts: avVersionString.setDescription('The version of the Availant Manager SNMP agent.')
avEventDateTime = MibScalar((1, 3, 6, 1, 4, 1, 5910, 1, 3, 2, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avEventDateTime.setStatus('mandatory')
if mibBuilder.loadTexts: avEventDateTime.setDescription('The date and time when the Event occurred, shown as GMT.')
avEventAgent = MibScalar((1, 3, 6, 1, 4, 1, 5910, 1, 3, 2, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avEventAgent.setStatus('mandatory')
if mibBuilder.loadTexts: avEventAgent.setDescription('The Agent that signaled the Event.')
avHostURL = MibScalar((1, 3, 6, 1, 4, 1, 5910, 1, 3, 2, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avHostURL.setStatus('mandatory')
if mibBuilder.loadTexts: avHostURL.setDescription('A URL to Availant Manager on the host where the Event occurred.')
avEventNotify = NotificationType((1, 3, 6, 1, 4, 1, 5910, 1, 3) + (0,1)).setObjects(("AVAM-SNMPv1", "avEventDateTime"), ("AVAM-SNMPv1", "avEventAgent"), ("AVAM-SNMPv1", "avHostURL"))
if mibBuilder.loadTexts: avEventNotify.setDescription('Notification when an Availant Manager Event has occurred.')
mibBuilder.exportSymbols("AVAM-SNMPv1", avVersionString=avVersionString, avEventNotify=avEventNotify, avHostURL=avHostURL, avProducts=avProducts, avamNotify=avamNotify, avamVisObj=avamVisObj, avEventDateTime=avEventDateTime, availant=availant, avamMIB=avamMIB, avEventAgent=avEventAgent)