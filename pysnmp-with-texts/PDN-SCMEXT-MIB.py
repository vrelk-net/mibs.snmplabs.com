#
# PySNMP MIB module PDN-SCMEXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-SCMEXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:39:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
pdnAtm, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdnAtm")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ModuleIdentity, Gauge32, Counter64, MibIdentifier, NotificationType, IpAddress, iso, TimeTicks, ObjectIdentity, Unsigned32, Counter32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ModuleIdentity", "Gauge32", "Counter64", "MibIdentifier", "NotificationType", "IpAddress", "iso", "TimeTicks", "ObjectIdentity", "Unsigned32", "Counter32", "Integer32")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
devAtmScm = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 4))
devAtmMaxVciVpiConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 4, 1))
devAtmMaxVciVpiConfigTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 4, 1, 1), )
if mibBuilder.loadTexts: devAtmMaxVciVpiConfigTable.setStatus('mandatory')
if mibBuilder.loadTexts: devAtmMaxVciVpiConfigTable.setDescription('The Paradyne MaxVciVpi-MIB Table .')
devAtmMaxVciVpiConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 4, 1, 1, 1), ).setIndexNames((0, "PDN-SCMEXT-MIB", "devAtmMaxIfIndex"), (0, "PDN-SCMEXT-MIB", "devAtmMaxVpi"))
if mibBuilder.loadTexts: devAtmMaxVciVpiConfigEntry.setStatus('mandatory')
if mibBuilder.loadTexts: devAtmMaxVciVpiConfigEntry.setDescription('An entry in the Paradyne MaxVciVpi-MIB Interface Config Table.')
devAtmMaxIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 4, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devAtmMaxIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: devAtmMaxIfIndex.setDescription('The index value which uniquely identifies the interface for which this entry contains information on interface tests. The interface identified by a particular value of this index is the same interface as identified by the same value of ifIndex from the Interfaces table of MIB II (RFC 1213).')
devAtmMaxVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 4, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devAtmMaxVpi.setStatus('mandatory')
if mibBuilder.loadTexts: devAtmMaxVpi.setDescription('This object is used to specify the vpi of interest.')
devAtmMaxVci = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 4, 1, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devAtmMaxVci.setStatus('mandatory')
if mibBuilder.loadTexts: devAtmMaxVci.setDescription("This object is used to specify the maximum number of vci's that will be allowed for the corresponding vpi.")
devAtmMaxVciVpiRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 4, 1, 1, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devAtmMaxVciVpiRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: devAtmMaxVciVpiRowStatus.setDescription('This object is used to create a new row or modify or delete an existing row in this table.')
devAtmAutoConfigXcon = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 4, 2))
devAtmAutoConfigXconTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 4, 2, 1), )
if mibBuilder.loadTexts: devAtmAutoConfigXconTable.setStatus('mandatory')
if mibBuilder.loadTexts: devAtmAutoConfigXconTable.setDescription('The Paradyne AutoConfigXcon-MIB Table .')
devAtmAutoConfigXconEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 4, 2, 1, 1), ).setIndexNames((0, "PDN-SCMEXT-MIB", "devAtmAutoConfigXconChannel"))
if mibBuilder.loadTexts: devAtmAutoConfigXconEntry.setStatus('mandatory')
if mibBuilder.loadTexts: devAtmAutoConfigXconEntry.setDescription('An entry in the Paradyne AutoConfigXcon-MIB Table.')
devAtmAutoConfigXconChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 4, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devAtmAutoConfigXconChannel.setStatus('mandatory')
if mibBuilder.loadTexts: devAtmAutoConfigXconChannel.setDescription('The index value which uniquely identifies the row in this table as being a unique range of cross connects being automatically generated for the ifindex-devAtmAutoConfigXconIfIndex. ')
devAtmAutoConfigXconIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 4, 2, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devAtmAutoConfigXconIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: devAtmAutoConfigXconIfIndex.setDescription('The index value which uniquely identifies the interface for which this entry contains information on interface tests. The interface identified by a particular value of this index is the same interface as identified by the same value of ifIndex from the Interfaces table of MIB II (RFC 1213).')
devAtmAutoConfigXconVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 4, 2, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devAtmAutoConfigXconVpi.setStatus('mandatory')
if mibBuilder.loadTexts: devAtmAutoConfigXconVpi.setDescription('This object is used to specify the vpi part of the vpi/vci')
devAtmAutoConfigXconVci = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 4, 2, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devAtmAutoConfigXconVci.setStatus('mandatory')
if mibBuilder.loadTexts: devAtmAutoConfigXconVci.setDescription('This object is used to specify the starting vci value.')
devAtmAutoConfigXconTraffic = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 4, 2, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devAtmAutoConfigXconTraffic.setStatus('mandatory')
if mibBuilder.loadTexts: devAtmAutoConfigXconTraffic.setDescription('This object is used to specify the class of service that this connection will be having.')
devAtmAutoConfigXconRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 11, 4, 2, 1, 1, 6), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devAtmAutoConfigXconRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: devAtmAutoConfigXconRowStatus.setDescription('This object is used to create a new row or modify or delete an existing row in this table.')
mibBuilder.exportSymbols("PDN-SCMEXT-MIB", devAtmAutoConfigXconTable=devAtmAutoConfigXconTable, devAtmAutoConfigXconVci=devAtmAutoConfigXconVci, devAtmMaxVci=devAtmMaxVci, devAtmMaxVciVpiConfig=devAtmMaxVciVpiConfig, devAtmAutoConfigXconTraffic=devAtmAutoConfigXconTraffic, devAtmAutoConfigXcon=devAtmAutoConfigXcon, devAtmAutoConfigXconIfIndex=devAtmAutoConfigXconIfIndex, devAtmAutoConfigXconRowStatus=devAtmAutoConfigXconRowStatus, devAtmMaxVpi=devAtmMaxVpi, devAtmAutoConfigXconChannel=devAtmAutoConfigXconChannel, devAtmScm=devAtmScm, devAtmAutoConfigXconVpi=devAtmAutoConfigXconVpi, devAtmMaxVciVpiConfigEntry=devAtmMaxVciVpiConfigEntry, devAtmMaxVciVpiRowStatus=devAtmMaxVciVpiRowStatus, devAtmMaxVciVpiConfigTable=devAtmMaxVciVpiConfigTable, devAtmAutoConfigXconEntry=devAtmAutoConfigXconEntry, devAtmMaxIfIndex=devAtmMaxIfIndex)