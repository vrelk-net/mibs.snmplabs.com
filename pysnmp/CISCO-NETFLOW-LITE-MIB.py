#
# PySNMP MIB module CISCO-NETFLOW-LITE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-NETFLOW-LITE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:51:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
Layer2Cos, CiscoVrfName = mibBuilder.importSymbols("CISCO-TC", "Layer2Cos", "CiscoVrfName")
Dscp, = mibBuilder.importSymbols("DIFFSERV-DSCP-TC", "Dscp")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddressType, InetAddress, InetPortNumber = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress", "InetPortNumber")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity, iso, Bits, Integer32, Counter64, TimeTicks, NotificationType, Gauge32, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity", "iso", "Bits", "Integer32", "Counter64", "TimeTicks", "NotificationType", "Gauge32", "MibIdentifier", "Unsigned32")
DisplayString, StorageType, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "StorageType", "TextualConvention", "RowStatus")
ciscoNetflowLiteMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 776))
ciscoNetflowLiteMIB.setRevisions(('2011-09-14 00:00',))
if mibBuilder.loadTexts: ciscoNetflowLiteMIB.setLastUpdated('201109140000Z')
if mibBuilder.loadTexts: ciscoNetflowLiteMIB.setOrganization('Cisco Systems, Inc.')
ciscoNetflowLiteMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 776, 0))
ciscoNetflowLiteMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 776, 1))
ciscoNetflowLiteMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 776, 2))
cnlExporter = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 1))
cnlSampler = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 2))
cnlMonitor = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 3))
cnlMaxExporterAllowed = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnlMaxExporterAllowed.setStatus('current')
cnlExporterTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 1, 2), )
if mibBuilder.loadTexts: cnlExporterTable.setStatus('current')
cnlExporterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 1, 2, 1), ).setIndexNames((1, "CISCO-NETFLOW-LITE-MIB", "cnlExporterName"))
if mibBuilder.loadTexts: cnlExporterEntry.setStatus('current')
cnlExporterName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 1, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: cnlExporterName.setStatus('current')
cnlExportAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 1, 2, 1, 2), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cnlExportAddrType.setStatus('current')
cnlExportDestinationAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 1, 2, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cnlExportDestinationAddr.setStatus('current')
cnlExportDestinationUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 1, 2, 1, 4), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cnlExportDestinationUdpPort.setStatus('current')
cnlExportDestinationUdpLoadShare = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 1, 2, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cnlExportDestinationUdpLoadShare.setStatus('current')
cnlExportSourceAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 1, 2, 1, 6), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cnlExportSourceAddr.setStatus('current')
cnlExportSourceUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 1, 2, 1, 7), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cnlExportSourceUdpPort.setStatus('current')
cnlExportVrf = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 1, 2, 1, 8), CiscoVrfName()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cnlExportVrf.setStatus('current')
cnlExportTtl = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 1, 2, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 254)).clone(254)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cnlExportTtl.setStatus('current')
cnlExportCos = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 1, 2, 1, 10), Layer2Cos()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cnlExportCos.setStatus('current')
cnlExportDscp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 1, 2, 1, 11), Dscp()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cnlExportDscp.setStatus('current')
cnlExportTemplateTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 1, 2, 1, 12), Unsigned32().clone(1800)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cnlExportTemplateTimeout.setStatus('current')
cnlExportSamplerTableTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 1, 2, 1, 13), Unsigned32().clone(1800)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cnlExportSamplerTableTimeout.setStatus('current')
cnlExportInterfaceTableTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 1, 2, 1, 14), Unsigned32().clone(1800)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cnlExportInterfaceTableTimeout.setStatus('current')
cnlExportProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 1, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ipFix", 1), ("netflowV9", 2))).clone('netflowV9')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cnlExportProtocol.setStatus('current')
cnlPacketExported = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 1, 2, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnlPacketExported.setStatus('current')
cnlExporterStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 1, 2, 1, 17), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cnlExporterStorageType.setStatus('current')
cnlExporterRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 1, 2, 1, 18), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cnlExporterRowStatus.setStatus('current')
cnlMaxSamplerAllowed = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 2, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnlMaxSamplerAllowed.setStatus('current')
cnlSamplerTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 2, 2), )
if mibBuilder.loadTexts: cnlSamplerTable.setStatus('current')
cnlSamplerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 2, 2, 1), ).setIndexNames((1, "CISCO-NETFLOW-LITE-MIB", "cnlSamplerName"))
if mibBuilder.loadTexts: cnlSamplerEntry.setStatus('current')
cnlSamplerName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 2, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: cnlSamplerName.setStatus('current')
cnlSamplerPacketRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 2, 2, 1, 2), Unsigned32().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cnlSamplerPacketRate.setStatus('current')
cnlSamplerPacketSectionSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 2, 2, 1, 3), Unsigned32().clone(64)).setUnits('bytes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cnlSamplerPacketSectionSize.setStatus('current')
cnlSamplerPacketOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 2, 2, 1, 4), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cnlSamplerPacketOffset.setStatus('current')
cnlSamplerStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 2, 2, 1, 5), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cnlSamplerStorageType.setStatus('current')
cnlSamplerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 2, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cnlSamplerRowStatus.setStatus('current')
cnlIfMonitorTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 3, 1), )
if mibBuilder.loadTexts: cnlIfMonitorTable.setStatus('current')
cnlIfMonitorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (1, "CISCO-NETFLOW-LITE-MIB", "cnlIfMonitorSessionName"))
if mibBuilder.loadTexts: cnlIfMonitorEntry.setStatus('current')
cnlIfMonitorSessionName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 3, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: cnlIfMonitorSessionName.setStatus('current')
cnlIfMonitorActiveStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnlIfMonitorActiveStatus.setStatus('current')
cnlIfSamplerName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 3, 1, 1, 3), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cnlIfSamplerName.setStatus('current')
cnlIfExporterName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 3, 1, 1, 4), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cnlIfExporterName.setStatus('current')
cnlIfAveragePacketSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 3, 1, 1, 5), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cnlIfAveragePacketSize.setStatus('current')
cnlIfAveragePacketSizeObserved = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 3, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnlIfAveragePacketSizeObserved.setStatus('current')
cnlIfAveragePacketSizeUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 3, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnlIfAveragePacketSizeUsed.setStatus('current')
cnlIfMonitorPktsObserved = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 3, 1, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnlIfMonitorPktsObserved.setStatus('current')
cnlIfMonitorPktsExported = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 3, 1, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnlIfMonitorPktsExported.setStatus('current')
cnlIfMonitorPktsDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 3, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnlIfMonitorPktsDropped.setStatus('current')
cnlIfMonitorStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 3, 1, 1, 11), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cnlIfMonitorStorageType.setStatus('current')
cnlIfMonitorRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 3, 1, 1, 12), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cnlIfMonitorRowStatus.setStatus('current')
ciscoNetflowLiteMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 776, 2, 1))
ciscoNetflowLiteMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 776, 2, 2))
ciscoNetflowLiteMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 776, 2, 1, 1)).setObjects(("CISCO-NETFLOW-LITE-MIB", "cnlExporterInfoGroup"), ("CISCO-NETFLOW-LITE-MIB", "cnlSamplerInfoGroup"), ("CISCO-NETFLOW-LITE-MIB", "cnlIfMonitorInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNetflowLiteMIBCompliance = ciscoNetflowLiteMIBCompliance.setStatus('current')
cnlExporterInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 776, 2, 2, 1)).setObjects(("CISCO-NETFLOW-LITE-MIB", "cnlMaxExporterAllowed"), ("CISCO-NETFLOW-LITE-MIB", "cnlExportAddrType"), ("CISCO-NETFLOW-LITE-MIB", "cnlExportDestinationAddr"), ("CISCO-NETFLOW-LITE-MIB", "cnlExportDestinationUdpPort"), ("CISCO-NETFLOW-LITE-MIB", "cnlExportDestinationUdpLoadShare"), ("CISCO-NETFLOW-LITE-MIB", "cnlExportSourceAddr"), ("CISCO-NETFLOW-LITE-MIB", "cnlExportSourceUdpPort"), ("CISCO-NETFLOW-LITE-MIB", "cnlExportVrf"), ("CISCO-NETFLOW-LITE-MIB", "cnlExportTtl"), ("CISCO-NETFLOW-LITE-MIB", "cnlExportCos"), ("CISCO-NETFLOW-LITE-MIB", "cnlExportDscp"), ("CISCO-NETFLOW-LITE-MIB", "cnlExportTemplateTimeout"), ("CISCO-NETFLOW-LITE-MIB", "cnlExportSamplerTableTimeout"), ("CISCO-NETFLOW-LITE-MIB", "cnlExportInterfaceTableTimeout"), ("CISCO-NETFLOW-LITE-MIB", "cnlExportProtocol"), ("CISCO-NETFLOW-LITE-MIB", "cnlPacketExported"), ("CISCO-NETFLOW-LITE-MIB", "cnlExporterStorageType"), ("CISCO-NETFLOW-LITE-MIB", "cnlExporterRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cnlExporterInfoGroup = cnlExporterInfoGroup.setStatus('current')
cnlSamplerInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 776, 2, 2, 2)).setObjects(("CISCO-NETFLOW-LITE-MIB", "cnlMaxSamplerAllowed"), ("CISCO-NETFLOW-LITE-MIB", "cnlSamplerPacketRate"), ("CISCO-NETFLOW-LITE-MIB", "cnlSamplerPacketSectionSize"), ("CISCO-NETFLOW-LITE-MIB", "cnlSamplerPacketOffset"), ("CISCO-NETFLOW-LITE-MIB", "cnlSamplerStorageType"), ("CISCO-NETFLOW-LITE-MIB", "cnlSamplerRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cnlSamplerInfoGroup = cnlSamplerInfoGroup.setStatus('current')
cnlIfMonitorInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 776, 2, 2, 3)).setObjects(("CISCO-NETFLOW-LITE-MIB", "cnlIfMonitorActiveStatus"), ("CISCO-NETFLOW-LITE-MIB", "cnlIfSamplerName"), ("CISCO-NETFLOW-LITE-MIB", "cnlIfExporterName"), ("CISCO-NETFLOW-LITE-MIB", "cnlIfAveragePacketSize"), ("CISCO-NETFLOW-LITE-MIB", "cnlIfAveragePacketSizeObserved"), ("CISCO-NETFLOW-LITE-MIB", "cnlIfAveragePacketSizeUsed"), ("CISCO-NETFLOW-LITE-MIB", "cnlIfMonitorPktsObserved"), ("CISCO-NETFLOW-LITE-MIB", "cnlIfMonitorPktsExported"), ("CISCO-NETFLOW-LITE-MIB", "cnlIfMonitorPktsDropped"), ("CISCO-NETFLOW-LITE-MIB", "cnlIfMonitorStorageType"), ("CISCO-NETFLOW-LITE-MIB", "cnlIfMonitorRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cnlIfMonitorInfoGroup = cnlIfMonitorInfoGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-NETFLOW-LITE-MIB", cnlSampler=cnlSampler, cnlIfMonitorActiveStatus=cnlIfMonitorActiveStatus, cnlExportInterfaceTableTimeout=cnlExportInterfaceTableTimeout, cnlIfMonitorEntry=cnlIfMonitorEntry, ciscoNetflowLiteMIBCompliance=ciscoNetflowLiteMIBCompliance, cnlExportSamplerTableTimeout=cnlExportSamplerTableTimeout, cnlMaxSamplerAllowed=cnlMaxSamplerAllowed, cnlExporterEntry=cnlExporterEntry, PYSNMP_MODULE_ID=ciscoNetflowLiteMIB, ciscoNetflowLiteMIBConform=ciscoNetflowLiteMIBConform, cnlExportTemplateTimeout=cnlExportTemplateTimeout, cnlIfAveragePacketSizeObserved=cnlIfAveragePacketSizeObserved, cnlExportDscp=cnlExportDscp, cnlExportDestinationUdpLoadShare=cnlExportDestinationUdpLoadShare, cnlExporterStorageType=cnlExporterStorageType, cnlIfMonitorTable=cnlIfMonitorTable, cnlSamplerTable=cnlSamplerTable, ciscoNetflowLiteMIBGroups=ciscoNetflowLiteMIBGroups, cnlExporterRowStatus=cnlExporterRowStatus, cnlExporterInfoGroup=cnlExporterInfoGroup, cnlIfMonitorInfoGroup=cnlIfMonitorInfoGroup, cnlExportVrf=cnlExportVrf, ciscoNetflowLiteMIBCompliances=ciscoNetflowLiteMIBCompliances, cnlExportSourceUdpPort=cnlExportSourceUdpPort, cnlExportAddrType=cnlExportAddrType, cnlIfAveragePacketSize=cnlIfAveragePacketSize, cnlSamplerPacketRate=cnlSamplerPacketRate, cnlIfExporterName=cnlIfExporterName, cnlExportDestinationUdpPort=cnlExportDestinationUdpPort, cnlExportProtocol=cnlExportProtocol, ciscoNetflowLiteMIBObjects=ciscoNetflowLiteMIBObjects, cnlIfMonitorStorageType=cnlIfMonitorStorageType, cnlExportCos=cnlExportCos, cnlSamplerPacketOffset=cnlSamplerPacketOffset, ciscoNetflowLiteMIB=ciscoNetflowLiteMIB, cnlExporter=cnlExporter, cnlExportDestinationAddr=cnlExportDestinationAddr, cnlSamplerStorageType=cnlSamplerStorageType, cnlMaxExporterAllowed=cnlMaxExporterAllowed, cnlSamplerPacketSectionSize=cnlSamplerPacketSectionSize, cnlPacketExported=cnlPacketExported, cnlExportSourceAddr=cnlExportSourceAddr, cnlIfMonitorPktsObserved=cnlIfMonitorPktsObserved, cnlSamplerInfoGroup=cnlSamplerInfoGroup, cnlExporterTable=cnlExporterTable, cnlSamplerName=cnlSamplerName, cnlMonitor=cnlMonitor, cnlIfSamplerName=cnlIfSamplerName, cnlSamplerEntry=cnlSamplerEntry, cnlExportTtl=cnlExportTtl, cnlIfMonitorRowStatus=cnlIfMonitorRowStatus, cnlExporterName=cnlExporterName, ciscoNetflowLiteMIBNotifs=ciscoNetflowLiteMIBNotifs, cnlIfAveragePacketSizeUsed=cnlIfAveragePacketSizeUsed, cnlIfMonitorSessionName=cnlIfMonitorSessionName, cnlIfMonitorPktsDropped=cnlIfMonitorPktsDropped, cnlSamplerRowStatus=cnlSamplerRowStatus, cnlIfMonitorPktsExported=cnlIfMonitorPktsExported)
