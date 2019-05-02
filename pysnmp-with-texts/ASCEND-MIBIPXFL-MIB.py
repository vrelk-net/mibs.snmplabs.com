#
# PySNMP MIB module ASCEND-MIBIPXFL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBIPXFL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:27:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, ObjectIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, MibIdentifier, Bits, Counter64, IpAddress, TimeTicks, Counter32, Integer32, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ObjectIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "MibIdentifier", "Bits", "Counter64", "IpAddress", "TimeTicks", "Counter32", "Integer32", "iso", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

mibipxsapFilterProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 88))
mibipxsapFilterProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 88, 1), )
if mibBuilder.loadTexts: mibipxsapFilterProfileTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibipxsapFilterProfileTable.setDescription('A list of mibipxsapFilterProfile profile entries.')
mibipxsapFilterProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 88, 1, 1), ).setIndexNames((0, "ASCEND-MIBIPXFL-MIB", "ipxsapFilterProfile-IpxSapFilterName"))
if mibBuilder.loadTexts: mibipxsapFilterProfileEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibipxsapFilterProfileEntry.setDescription('A mibipxsapFilterProfile entry containing objects that maps to the parameters of mibipxsapFilterProfile profile.')
ipxsapFilterProfile_IpxSapFilterName = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 88, 1, 1, 1), DisplayString()).setLabel("ipxsapFilterProfile-IpxSapFilterName").setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxsapFilterProfile_IpxSapFilterName.setStatus('mandatory')
if mibBuilder.loadTexts: ipxsapFilterProfile_IpxSapFilterName.setDescription('The name of this IPX SAP Filter.')
ipxsapFilterProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 88, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("ipxsapFilterProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxsapFilterProfile_Action_o.setStatus('mandatory')
if mibBuilder.loadTexts: ipxsapFilterProfile_Action_o.setDescription('')
mibipxsapFilterProfile_OutputIpxSapFiltersTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 88, 2), ).setLabel("mibipxsapFilterProfile-OutputIpxSapFiltersTable")
if mibBuilder.loadTexts: mibipxsapFilterProfile_OutputIpxSapFiltersTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibipxsapFilterProfile_OutputIpxSapFiltersTable.setDescription('A list of mibipxsapFilterProfile__output_ipx_sap_filters profile entries.')
mibipxsapFilterProfile_OutputIpxSapFiltersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 88, 2, 1), ).setLabel("mibipxsapFilterProfile-OutputIpxSapFiltersEntry").setIndexNames((0, "ASCEND-MIBIPXFL-MIB", "ipxsapFilterProfile-OutputIpxSapFilters-IpxSapFilterName"), (0, "ASCEND-MIBIPXFL-MIB", "ipxsapFilterProfile-OutputIpxSapFilters-Index-o"))
if mibBuilder.loadTexts: mibipxsapFilterProfile_OutputIpxSapFiltersEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibipxsapFilterProfile_OutputIpxSapFiltersEntry.setDescription('A mibipxsapFilterProfile__output_ipx_sap_filters entry containing objects that maps to the parameters of mibipxsapFilterProfile__output_ipx_sap_filters profile.')
ipxsapFilterProfile_OutputIpxSapFilters_IpxSapFilterName = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 88, 2, 1, 1), DisplayString()).setLabel("ipxsapFilterProfile-OutputIpxSapFilters-IpxSapFilterName").setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxsapFilterProfile_OutputIpxSapFilters_IpxSapFilterName.setStatus('mandatory')
if mibBuilder.loadTexts: ipxsapFilterProfile_OutputIpxSapFilters_IpxSapFilterName.setDescription('')
ipxsapFilterProfile_OutputIpxSapFilters_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 88, 2, 1, 2), Integer32()).setLabel("ipxsapFilterProfile-OutputIpxSapFilters-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxsapFilterProfile_OutputIpxSapFilters_Index_o.setStatus('mandatory')
if mibBuilder.loadTexts: ipxsapFilterProfile_OutputIpxSapFilters_Index_o.setDescription('')
ipxsapFilterProfile_OutputIpxSapFilters_ValidFilter = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 88, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("ipxsapFilterProfile-OutputIpxSapFilters-ValidFilter").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxsapFilterProfile_OutputIpxSapFilters_ValidFilter.setStatus('mandatory')
if mibBuilder.loadTexts: ipxsapFilterProfile_OutputIpxSapFilters_ValidFilter.setDescription('When TRUE, this filter entry has been defined and properly initialized. When FALSE, this filter should be skipped when Filter Table is being applied to in/out SAP data.')
ipxsapFilterProfile_OutputIpxSapFilters_TypeFilter = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 88, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("exclude", 1), ("include", 2)))).setLabel("ipxsapFilterProfile-OutputIpxSapFilters-TypeFilter").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxsapFilterProfile_OutputIpxSapFilters_TypeFilter.setStatus('mandatory')
if mibBuilder.loadTexts: ipxsapFilterProfile_OutputIpxSapFilters_TypeFilter.setDescription('Filter may be used to EXCLUDE or, INCLUDE matching SAP fields.')
ipxsapFilterProfile_OutputIpxSapFilters_ServerType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 88, 2, 1, 5), DisplayString()).setLabel("ipxsapFilterProfile-OutputIpxSapFilters-ServerType").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxsapFilterProfile_OutputIpxSapFilters_ServerType.setStatus('mandatory')
if mibBuilder.loadTexts: ipxsapFilterProfile_OutputIpxSapFilters_ServerType.setDescription('Defines the service number to be filtered in/out from SAP data.')
ipxsapFilterProfile_OutputIpxSapFilters_ServerName = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 88, 2, 1, 6), DisplayString()).setLabel("ipxsapFilterProfile-OutputIpxSapFilters-ServerName").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxsapFilterProfile_OutputIpxSapFilters_ServerName.setStatus('mandatory')
if mibBuilder.loadTexts: ipxsapFilterProfile_OutputIpxSapFilters_ServerName.setDescription('Defined the server name to be filtered, Wildcard (* and ?) characters are accepted for partial name matching.')
mibipxsapFilterProfile_InputIpxSapFiltersTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 88, 3), ).setLabel("mibipxsapFilterProfile-InputIpxSapFiltersTable")
if mibBuilder.loadTexts: mibipxsapFilterProfile_InputIpxSapFiltersTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibipxsapFilterProfile_InputIpxSapFiltersTable.setDescription('A list of mibipxsapFilterProfile__input_ipx_sap_filters profile entries.')
mibipxsapFilterProfile_InputIpxSapFiltersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 88, 3, 1), ).setLabel("mibipxsapFilterProfile-InputIpxSapFiltersEntry").setIndexNames((0, "ASCEND-MIBIPXFL-MIB", "ipxsapFilterProfile-InputIpxSapFilters-IpxSapFilterName"), (0, "ASCEND-MIBIPXFL-MIB", "ipxsapFilterProfile-InputIpxSapFilters-Index-o"))
if mibBuilder.loadTexts: mibipxsapFilterProfile_InputIpxSapFiltersEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibipxsapFilterProfile_InputIpxSapFiltersEntry.setDescription('A mibipxsapFilterProfile__input_ipx_sap_filters entry containing objects that maps to the parameters of mibipxsapFilterProfile__input_ipx_sap_filters profile.')
ipxsapFilterProfile_InputIpxSapFilters_IpxSapFilterName = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 88, 3, 1, 1), DisplayString()).setLabel("ipxsapFilterProfile-InputIpxSapFilters-IpxSapFilterName").setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxsapFilterProfile_InputIpxSapFilters_IpxSapFilterName.setStatus('mandatory')
if mibBuilder.loadTexts: ipxsapFilterProfile_InputIpxSapFilters_IpxSapFilterName.setDescription('')
ipxsapFilterProfile_InputIpxSapFilters_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 88, 3, 1, 2), Integer32()).setLabel("ipxsapFilterProfile-InputIpxSapFilters-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: ipxsapFilterProfile_InputIpxSapFilters_Index_o.setStatus('mandatory')
if mibBuilder.loadTexts: ipxsapFilterProfile_InputIpxSapFilters_Index_o.setDescription('')
ipxsapFilterProfile_InputIpxSapFilters_ValidFilter = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 88, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("ipxsapFilterProfile-InputIpxSapFilters-ValidFilter").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxsapFilterProfile_InputIpxSapFilters_ValidFilter.setStatus('mandatory')
if mibBuilder.loadTexts: ipxsapFilterProfile_InputIpxSapFilters_ValidFilter.setDescription('When TRUE, this filter entry has been defined and properly initialized. When FALSE, this filter should be skipped when Filter Table is being applied to in/out SAP data.')
ipxsapFilterProfile_InputIpxSapFilters_TypeFilter = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 88, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("exclude", 1), ("include", 2)))).setLabel("ipxsapFilterProfile-InputIpxSapFilters-TypeFilter").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxsapFilterProfile_InputIpxSapFilters_TypeFilter.setStatus('mandatory')
if mibBuilder.loadTexts: ipxsapFilterProfile_InputIpxSapFilters_TypeFilter.setDescription('Filter may be used to EXCLUDE or, INCLUDE matching SAP fields.')
ipxsapFilterProfile_InputIpxSapFilters_ServerType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 88, 3, 1, 5), DisplayString()).setLabel("ipxsapFilterProfile-InputIpxSapFilters-ServerType").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxsapFilterProfile_InputIpxSapFilters_ServerType.setStatus('mandatory')
if mibBuilder.loadTexts: ipxsapFilterProfile_InputIpxSapFilters_ServerType.setDescription('Defines the service number to be filtered in/out from SAP data.')
ipxsapFilterProfile_InputIpxSapFilters_ServerName = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 88, 3, 1, 6), DisplayString()).setLabel("ipxsapFilterProfile-InputIpxSapFilters-ServerName").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipxsapFilterProfile_InputIpxSapFilters_ServerName.setStatus('mandatory')
if mibBuilder.loadTexts: ipxsapFilterProfile_InputIpxSapFilters_ServerName.setDescription('Defined the server name to be filtered, Wildcard (* and ?) characters are accepted for partial name matching.')
mibBuilder.exportSymbols("ASCEND-MIBIPXFL-MIB", mibipxsapFilterProfileTable=mibipxsapFilterProfileTable, ipxsapFilterProfile_Action_o=ipxsapFilterProfile_Action_o, mibipxsapFilterProfile_InputIpxSapFiltersTable=mibipxsapFilterProfile_InputIpxSapFiltersTable, mibipxsapFilterProfile_InputIpxSapFiltersEntry=mibipxsapFilterProfile_InputIpxSapFiltersEntry, ipxsapFilterProfile_InputIpxSapFilters_ServerName=ipxsapFilterProfile_InputIpxSapFilters_ServerName, ipxsapFilterProfile_InputIpxSapFilters_IpxSapFilterName=ipxsapFilterProfile_InputIpxSapFilters_IpxSapFilterName, ipxsapFilterProfile_OutputIpxSapFilters_Index_o=ipxsapFilterProfile_OutputIpxSapFilters_Index_o, DisplayString=DisplayString, ipxsapFilterProfile_InputIpxSapFilters_ServerType=ipxsapFilterProfile_InputIpxSapFilters_ServerType, ipxsapFilterProfile_IpxSapFilterName=ipxsapFilterProfile_IpxSapFilterName, mibipxsapFilterProfileEntry=mibipxsapFilterProfileEntry, ipxsapFilterProfile_OutputIpxSapFilters_ServerType=ipxsapFilterProfile_OutputIpxSapFilters_ServerType, ipxsapFilterProfile_OutputIpxSapFilters_TypeFilter=ipxsapFilterProfile_OutputIpxSapFilters_TypeFilter, ipxsapFilterProfile_InputIpxSapFilters_TypeFilter=ipxsapFilterProfile_InputIpxSapFilters_TypeFilter, ipxsapFilterProfile_InputIpxSapFilters_ValidFilter=ipxsapFilterProfile_InputIpxSapFilters_ValidFilter, mibipxsapFilterProfile_OutputIpxSapFiltersEntry=mibipxsapFilterProfile_OutputIpxSapFiltersEntry, mibipxsapFilterProfile=mibipxsapFilterProfile, ipxsapFilterProfile_OutputIpxSapFilters_IpxSapFilterName=ipxsapFilterProfile_OutputIpxSapFilters_IpxSapFilterName, ipxsapFilterProfile_OutputIpxSapFilters_ValidFilter=ipxsapFilterProfile_OutputIpxSapFilters_ValidFilter, ipxsapFilterProfile_OutputIpxSapFilters_ServerName=ipxsapFilterProfile_OutputIpxSapFilters_ServerName, mibipxsapFilterProfile_OutputIpxSapFiltersTable=mibipxsapFilterProfile_OutputIpxSapFiltersTable, ipxsapFilterProfile_InputIpxSapFilters_Index_o=ipxsapFilterProfile_InputIpxSapFilters_Index_o)