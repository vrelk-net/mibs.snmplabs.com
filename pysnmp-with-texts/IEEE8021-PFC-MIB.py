#
# PySNMP MIB module IEEE8021-PFC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IEEE8021-PFC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:52:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ieee802dot1mibs, = mibBuilder.importSymbols("IEEE8021-TC-MIB", "ieee802dot1mibs")
ifGeneralInformationGroup, ifEntry = mibBuilder.importSymbols("IF-MIB", "ifGeneralInformationGroup", "ifEntry")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
systemGroup, = mibBuilder.importSymbols("SNMPv2-MIB", "systemGroup")
Integer32, ModuleIdentity, iso, Counter64, Gauge32, Unsigned32, NotificationType, TimeTicks, ObjectIdentity, Counter32, MibIdentifier, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "iso", "Counter64", "Gauge32", "Unsigned32", "NotificationType", "TimeTicks", "ObjectIdentity", "Counter32", "MibIdentifier", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ieee8021PFCMib = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 21))
ieee8021PFCMib.setRevisions(('2014-12-15 00:00', '2010-02-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ieee8021PFCMib.setRevisionsDescriptions(('Published as part of IEEE Std 802.1Q 2014 revision. Cross references updated and corrected.', 'Included in IEEE P802.1Qbb Copyright (C) IEEE.',))
if mibBuilder.loadTexts: ieee8021PFCMib.setLastUpdated('201412150000Z')
if mibBuilder.loadTexts: ieee8021PFCMib.setOrganization('IEEE 802.1 Working Group')
if mibBuilder.loadTexts: ieee8021PFCMib.setContactInfo('WG-URL: http://grouper.ieee.org/groups/802/1/index.html WG-EMail: stds-802-1@ieee.org Contact: IEEE 802.1 Working Group Chair Postal: IEEE Standards Board 445 Hoes Lane P.O. Box 1331 Piscataway, NJ 08855-1331 USA E-mail: stds-802-1@ieee.org ')
if mibBuilder.loadTexts: ieee8021PFCMib.setDescription('Priority-based Flow Control module for IEEE 802.1Q. Unless otherwise indicated, the references in this MIB module are to IEEE Std 802.1Q-2014. Copyright (C) IEEE (2014). This version of this MIB module is part of IEEE802.1Q; see the draft itself for full legal notices. ')
ieee8021PfcMIBObjects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 21, 1))
ieee8021PfcConformance = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 21, 2))
ieee8021PfcIfTable = MibTable((1, 3, 111, 2, 802, 1, 1, 21, 1, 1), )
if mibBuilder.loadTexts: ieee8021PfcIfTable.setReference('12.23')
if mibBuilder.loadTexts: ieee8021PfcIfTable.setStatus('current')
if mibBuilder.loadTexts: ieee8021PfcIfTable.setDescription('A table of PFC information for all interfaces of a system.')
ieee8021PfcIfEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 21, 1, 1, 1), )
if mibBuilder.loadTexts: ieee8021PfcIfEntry.setReference('12.23')
ifEntry.registerAugmentions(("IEEE8021-PFC-MIB", "ieee8021PfcIfEntry"))
ieee8021PfcIfEntry.setIndexNames(*ifEntry.getIndexNames())
if mibBuilder.loadTexts: ieee8021PfcIfEntry.setStatus('current')
if mibBuilder.loadTexts: ieee8021PfcIfEntry.setDescription('Each entry contains information about the PFC function on a single interface.')
ieee8021PfcLinkDelayAllowance = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 21, 1, 1, 1, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021PfcLinkDelayAllowance.setStatus('current')
if mibBuilder.loadTexts: ieee8021PfcLinkDelayAllowance.setDescription('The allowance made for round-trip propagation delay of the link in bits. The value of this object MUST be retained across reinitializations of the management system.')
ieee8021PfcRequests = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 21, 1, 1, 1, 2), Counter32()).setUnits('Requests').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PfcRequests.setStatus('current')
if mibBuilder.loadTexts: ieee8021PfcRequests.setDescription('A count of the invoked PFC M_CONTROL.request primitives. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.')
ieee8021PfcIndications = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 21, 1, 1, 1, 3), Counter32()).setUnits('Indications').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PfcIndications.setStatus('current')
if mibBuilder.loadTexts: ieee8021PfcIndications.setDescription('A count of the received PFC M_CONTROL.indication primitives. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime.')
ieee8021PfcCompliances = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 21, 2, 1))
ieee8021PfcGroups = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 21, 2, 2))
ieee8021PfcGlobalReqdGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 21, 2, 2, 1)).setObjects(("IEEE8021-PFC-MIB", "ieee8021PfcLinkDelayAllowance"), ("IEEE8021-PFC-MIB", "ieee8021PfcRequests"), ("IEEE8021-PFC-MIB", "ieee8021PfcIndications"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PfcGlobalReqdGroup = ieee8021PfcGlobalReqdGroup.setStatus('current')
if mibBuilder.loadTexts: ieee8021PfcGlobalReqdGroup.setDescription('Objects in the global required group.')
ieee8021PfcCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 21, 2, 1, 1)).setObjects(("SNMPv2-MIB", "systemGroup"), ("IF-MIB", "ifGeneralInformationGroup"), ("IEEE8021-PFC-MIB", "ieee8021PfcGlobalReqdGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021PfcCompliance = ieee8021PfcCompliance.setStatus('current')
if mibBuilder.loadTexts: ieee8021PfcCompliance.setDescription('The compliance statement for support by a system of the IEEE8021-PFC-MIB module.')
mibBuilder.exportSymbols("IEEE8021-PFC-MIB", ieee8021PfcMIBObjects=ieee8021PfcMIBObjects, ieee8021PfcGroups=ieee8021PfcGroups, ieee8021PfcIndications=ieee8021PfcIndications, ieee8021PfcConformance=ieee8021PfcConformance, ieee8021PfcIfEntry=ieee8021PfcIfEntry, ieee8021PfcCompliances=ieee8021PfcCompliances, ieee8021PfcGlobalReqdGroup=ieee8021PfcGlobalReqdGroup, ieee8021PFCMib=ieee8021PFCMib, ieee8021PfcIfTable=ieee8021PfcIfTable, ieee8021PfcRequests=ieee8021PfcRequests, ieee8021PfcLinkDelayAllowance=ieee8021PfcLinkDelayAllowance, PYSNMP_MODULE_ID=ieee8021PFCMib, ieee8021PfcCompliance=ieee8021PfcCompliance)