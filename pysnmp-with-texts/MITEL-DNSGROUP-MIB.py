#
# PySNMP MIB module MITEL-DNSGROUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MITEL-DNSGROUP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:13:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, IpAddress, iso, enterprises, NotificationType, Bits, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, Counter64, ModuleIdentity, Gauge32, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "iso", "enterprises", "NotificationType", "Bits", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "Counter64", "ModuleIdentity", "Gauge32", "MibIdentifier", "Unsigned32")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
mitelIpGrpDnsGroup = ModuleIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3))
mitelIpGrpDnsGroup.setRevisions(('2003-03-21 03:18', '1999-03-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mitelIpGrpDnsGroup.setRevisionsDescriptions(('Translate to SMIv2', 'DNS MIB Version 1.0',))
if mibBuilder.loadTexts: mitelIpGrpDnsGroup.setLastUpdated('200303210318Z')
if mibBuilder.loadTexts: mitelIpGrpDnsGroup.setOrganization('MITEL Corporation')
if mibBuilder.loadTexts: mitelIpGrpDnsGroup.setContactInfo('Standards Group, Postal: MITEL Corporation 350 Legget Drive, PO Box 13089 Kanata, Ontario Canada K2K 1X3 Tel: +1 613 592 2122 Fax: +1 613 592 4784 E-mail: std@mitel.com')
if mibBuilder.loadTexts: mitelIpGrpDnsGroup.setDescription('The MITEL DNS MIB module.')
mitel = MibIdentifier((1, 3, 6, 1, 4, 1, 1027))
mitelProprietary = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4))
mitelPropIpNetworking = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8))
mitelIpNetRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1))
mitelRouterIpGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1))
mitelDnsGrpDomainName = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelDnsGrpDomainName.setStatus('current')
if mibBuilder.loadTexts: mitelDnsGrpDomainName.setDescription('The Domain Name for this device.')
mitelDnsGrpPrimaryDns = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelDnsGrpPrimaryDns.setStatus('current')
if mibBuilder.loadTexts: mitelDnsGrpPrimaryDns.setDescription('Address of Primary DNS Server.')
mitelDnsGrpSecondaryDns = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelDnsGrpSecondaryDns.setStatus('current')
if mibBuilder.loadTexts: mitelDnsGrpSecondaryDns.setDescription('Address of Secondary DNS Server.')
mitelDnsGrpQueryOrder = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("local-first", 1), ("dns-first", 2), ("dns-only", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelDnsGrpQueryOrder.setStatus('current')
if mibBuilder.loadTexts: mitelDnsGrpQueryOrder.setDescription('Order which DNS is queried.')
mitelDnsGrpAnswerTtl = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelDnsGrpAnswerTtl.setStatus('current')
if mibBuilder.loadTexts: mitelDnsGrpAnswerTtl.setDescription('Answer TTL to return in locally generated responses.')
mitelDnsGrpDnsPort = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelDnsGrpDnsPort.setStatus('current')
if mibBuilder.loadTexts: mitelDnsGrpDnsPort.setDescription('Port to listen for DNS requests on.')
mitelDnsGrpFilterEnabled = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelDnsGrpFilterEnabled.setStatus('current')
if mibBuilder.loadTexts: mitelDnsGrpFilterEnabled.setDescription('DNS Security Filtering Status. If Enabled, filter DNS quries that are not from localhost.')
mitelDnsGrpDnsStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3, 9))
mitelDnsStatsQueryTotal = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3, 9, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelDnsStatsQueryTotal.setStatus('current')
if mibBuilder.loadTexts: mitelDnsStatsQueryTotal.setDescription('Total DNS query count.')
mitelDnsStatsQueryFiltered = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3, 9, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelDnsStatsQueryFiltered.setStatus('current')
if mibBuilder.loadTexts: mitelDnsStatsQueryFiltered.setDescription('The number of queries filtered and rejected.')
mitelDnsStatsQueryLocal = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3, 9, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelDnsStatsQueryLocal.setStatus('current')
if mibBuilder.loadTexts: mitelDnsStatsQueryLocal.setDescription('The number of queries processed locally.')
mitelDnsStatsQueryLocalFail = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3, 9, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelDnsStatsQueryLocalFail.setStatus('current')
if mibBuilder.loadTexts: mitelDnsStatsQueryLocalFail.setDescription('The number of failed queries processed locally.')
mitelDnsStatsQueryExternal = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3, 9, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelDnsStatsQueryExternal.setStatus('current')
if mibBuilder.loadTexts: mitelDnsStatsQueryExternal.setDescription('The number of queries forwarded to an external DNS.')
mitelDnsStatsQueryExternalFail = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3, 9, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelDnsStatsQueryExternalFail.setStatus('current')
if mibBuilder.loadTexts: mitelDnsStatsQueryExternalFail.setDescription('The number of queries forwarded to an external DNS that failed.')
mitelDnsStatsQueryInvalid = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3, 9, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelDnsStatsQueryInvalid.setStatus('current')
if mibBuilder.loadTexts: mitelDnsStatsQueryInvalid.setDescription('The number of invalid queries.')
mitelDnsGrpDnsHostTable = MibTable((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3, 10), )
if mibBuilder.loadTexts: mitelDnsGrpDnsHostTable.setStatus('current')
if mibBuilder.loadTexts: mitelDnsGrpDnsHostTable.setDescription('This table contains a list of IP addresses and their associated Host Names.')
mitelDnsGrpDnsHostEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3, 10, 1), ).setIndexNames((0, "MITEL-DNSGROUP-MIB", "mitelDnsHostTableIpAddress"), (0, "MITEL-DNSGROUP-MIB", "mitelDnsHostTableHostName"))
if mibBuilder.loadTexts: mitelDnsGrpDnsHostEntry.setStatus('current')
if mibBuilder.loadTexts: mitelDnsGrpDnsHostEntry.setDescription('DNS information')
mitelDnsHostTableIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3, 10, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelDnsHostTableIpAddress.setStatus('current')
if mibBuilder.loadTexts: mitelDnsHostTableIpAddress.setDescription('The IP address to be associated with mitelDnsHostTableHostName')
mitelDnsHostTableHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3, 10, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelDnsHostTableHostName.setStatus('current')
if mibBuilder.loadTexts: mitelDnsHostTableHostName.setDescription("The entry's Host Name")
mitelDnsHostTableRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 1, 3, 10, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mitelDnsHostTableRowStatus.setStatus('current')
if mibBuilder.loadTexts: mitelDnsHostTableRowStatus.setDescription('The current status of this entry')
mibBuilder.exportSymbols("MITEL-DNSGROUP-MIB", mitelRouterIpGroup=mitelRouterIpGroup, mitelDnsStatsQueryExternal=mitelDnsStatsQueryExternal, mitelDnsGrpDomainName=mitelDnsGrpDomainName, mitelDnsGrpPrimaryDns=mitelDnsGrpPrimaryDns, mitelDnsStatsQueryFiltered=mitelDnsStatsQueryFiltered, mitelPropIpNetworking=mitelPropIpNetworking, mitelDnsGrpAnswerTtl=mitelDnsGrpAnswerTtl, mitelDnsHostTableIpAddress=mitelDnsHostTableIpAddress, mitelProprietary=mitelProprietary, mitelDnsHostTableRowStatus=mitelDnsHostTableRowStatus, mitelDnsStatsQueryTotal=mitelDnsStatsQueryTotal, mitelDnsGrpDnsPort=mitelDnsGrpDnsPort, mitelDnsGrpQueryOrder=mitelDnsGrpQueryOrder, mitelDnsGrpSecondaryDns=mitelDnsGrpSecondaryDns, mitelDnsStatsQueryLocal=mitelDnsStatsQueryLocal, mitelDnsGrpDnsStatistics=mitelDnsGrpDnsStatistics, mitelDnsStatsQueryLocalFail=mitelDnsStatsQueryLocalFail, mitelDnsStatsQueryInvalid=mitelDnsStatsQueryInvalid, PYSNMP_MODULE_ID=mitelIpGrpDnsGroup, mitelDnsGrpDnsHostTable=mitelDnsGrpDnsHostTable, mitelDnsStatsQueryExternalFail=mitelDnsStatsQueryExternalFail, mitelIpNetRouter=mitelIpNetRouter, mitelDnsGrpDnsHostEntry=mitelDnsGrpDnsHostEntry, mitelDnsHostTableHostName=mitelDnsHostTableHostName, mitelDnsGrpFilterEnabled=mitelDnsGrpFilterEnabled, mitel=mitel, mitelIpGrpDnsGroup=mitelIpGrpDnsGroup)