#
# PySNMP MIB module PANASAS-EVENTS-MIB-V1 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PANASAS-EVENTS-MIB-V1
# Produced by pysmi-0.3.4 at Wed May  1 14:37:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
panFs, = mibBuilder.importSymbols("PANASAS-PANFS-MIB-V1", "panFs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Gauge32, ObjectIdentity, ModuleIdentity, TimeTicks, iso, IpAddress, Unsigned32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, MibIdentifier, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "ObjectIdentity", "ModuleIdentity", "TimeTicks", "iso", "IpAddress", "Unsigned32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "MibIdentifier", "Bits", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
panEvents = ModuleIdentity((1, 3, 6, 1, 4, 1, 10159, 1, 3, 1))
panEvents.setRevisions(('2011-04-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: panEvents.setRevisionsDescriptions(('1. Changed Panasas, Inc. company contact information.',))
if mibBuilder.loadTexts: panEvents.setLastUpdated('201104070000Z')
if mibBuilder.loadTexts: panEvents.setOrganization('Panasas, Inc')
if mibBuilder.loadTexts: panEvents.setContactInfo('postal: Panasas, Inc 969 W. Maude Avenue Sunnyvale, CA 94085 phone: +1 408 215-6800 email: info@panasas.com')
if mibBuilder.loadTexts: panEvents.setDescription('This file defines the structure of the panasas events mib. The purpose is to maintain a list of the last few notifications generated by the agent.')
panEventTableSize = MibScalar((1, 3, 6, 1, 4, 1, 10159, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: panEventTableSize.setStatus('current')
if mibBuilder.loadTexts: panEventTableSize.setDescription('The number of events in the event table. 0 means there are no events. 1 .. panEventTableSize event indices in the table.')
panEventTable = MibTable((1, 3, 6, 1, 4, 1, 10159, 1, 3, 1, 2), )
if mibBuilder.loadTexts: panEventTable.setStatus('current')
if mibBuilder.loadTexts: panEventTable.setDescription('The event table.')
panEventEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10159, 1, 3, 1, 2, 1), ).setIndexNames((0, "PANASAS-EVENTS-MIB-V1", "panEventIndex"))
if mibBuilder.loadTexts: panEventEntry.setStatus('current')
if mibBuilder.loadTexts: panEventEntry.setDescription('An entry in the Event table.')
panEventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10159, 1, 3, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: panEventIndex.setStatus('current')
if mibBuilder.loadTexts: panEventIndex.setDescription('Index into the Event table.')
panEventCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 10159, 1, 3, 1, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panEventCategory.setStatus('current')
if mibBuilder.loadTexts: panEventCategory.setDescription('Category of the event. (E.g. Error, Warning, Info etc.)')
panEventDate = MibTableColumn((1, 3, 6, 1, 4, 1, 10159, 1, 3, 1, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panEventDate.setStatus('current')
if mibBuilder.loadTexts: panEventDate.setDescription('Date when the event occured.')
panEventTime = MibTableColumn((1, 3, 6, 1, 4, 1, 10159, 1, 3, 1, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panEventTime.setStatus('current')
if mibBuilder.loadTexts: panEventTime.setDescription('Time when the event occured.')
panEventShelfName = MibTableColumn((1, 3, 6, 1, 4, 1, 10159, 1, 3, 1, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panEventShelfName.setStatus('current')
if mibBuilder.loadTexts: panEventShelfName.setDescription('If applicable, shelf where the event occured.')
panEventShelfSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 10159, 1, 3, 1, 2, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panEventShelfSlot.setStatus('current')
if mibBuilder.loadTexts: panEventShelfSlot.setDescription('If applicable, slot where the event occured.')
panEventHwDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 10159, 1, 3, 1, 2, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panEventHwDesc.setStatus('current')
if mibBuilder.loadTexts: panEventHwDesc.setDescription('If applicable, description of the Hw component where the event occured.')
panEventBladeIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 10159, 1, 3, 1, 2, 1, 8), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panEventBladeIPAddr.setStatus('current')
if mibBuilder.loadTexts: panEventBladeIPAddr.setDescription('If applicable, IP Address where the event occured.')
panEventText = MibTableColumn((1, 3, 6, 1, 4, 1, 10159, 1, 3, 1, 2, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panEventText.setStatus('current')
if mibBuilder.loadTexts: panEventText.setDescription('Textual description of the event.')
panEventCode = MibTableColumn((1, 3, 6, 1, 4, 1, 10159, 1, 3, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: panEventCode.setStatus('current')
if mibBuilder.loadTexts: panEventCode.setDescription('The event identification number of this event.')
mibBuilder.exportSymbols("PANASAS-EVENTS-MIB-V1", panEventTableSize=panEventTableSize, panEventEntry=panEventEntry, panEventBladeIPAddr=panEventBladeIPAddr, panEvents=panEvents, panEventDate=panEventDate, panEventText=panEventText, panEventShelfName=panEventShelfName, panEventHwDesc=panEventHwDesc, PYSNMP_MODULE_ID=panEvents, panEventCategory=panEventCategory, panEventTable=panEventTable, panEventShelfSlot=panEventShelfSlot, panEventCode=panEventCode, panEventIndex=panEventIndex, panEventTime=panEventTime)