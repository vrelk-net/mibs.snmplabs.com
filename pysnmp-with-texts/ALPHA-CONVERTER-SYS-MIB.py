#
# PySNMP MIB module ALPHA-CONVERTER-SYS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALPHA-CONVERTER-SYS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:20:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
simple, ScaledNumber = mibBuilder.importSymbols("ALPHA-RESOURCE-MIB", "simple", "ScaledNumber")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Integer32, Gauge32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, NotificationType, TimeTicks, MibIdentifier, Counter64, ModuleIdentity, iso, Bits, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "NotificationType", "TimeTicks", "MibIdentifier", "Counter64", "ModuleIdentity", "iso", "Bits", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
converterSystem = ModuleIdentity((1, 3, 6, 1, 4, 1, 7309, 5, 3, 2))
converterSystem.setRevisions(('2015-07-28 00:00', '2015-07-23 00:00', '2015-06-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: converterSystem.setRevisionsDescriptions((' Updated to follow MIB structure conformance rules. Tested with SimpleWeb: http://www.simpleweb.org Passed highest level of compliance. (level 6) ', 'Fixed MIB syntax warnings.', 'General revision.',))
if mibBuilder.loadTexts: converterSystem.setLastUpdated('201507280000Z')
if mibBuilder.loadTexts: converterSystem.setOrganization('Alpha Technologies Ltd.')
if mibBuilder.loadTexts: converterSystem.setContactInfo('Alpha Technologies Ltd. 7700 Riverfront Gate Burnaby, BC V5J 5M4 Canada Tel: 1-604-436-5900 Fax: 1-604-436-1233')
if mibBuilder.loadTexts: converterSystem.setDescription('This MIB defines the notification block(s) available in system controllers.')
convSysTotalOutputCurrent = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 3, 2, 1), ScaledNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: convSysTotalOutputCurrent.setStatus('current')
if mibBuilder.loadTexts: convSysTotalOutputCurrent.setDescription('Total converter output current in AMPS.')
convSysTotalOutputPower = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 3, 2, 2), ScaledNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: convSysTotalOutputPower.setStatus('current')
if mibBuilder.loadTexts: convSysTotalOutputPower.setDescription('Total converter output power in WATTS.')
convSysTotalCapacityInstalledAmps = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 3, 2, 3), ScaledNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: convSysTotalCapacityInstalledAmps.setStatus('current')
if mibBuilder.loadTexts: convSysTotalCapacityInstalledAmps.setDescription('A converter output current multiplied by the number of converters installed.')
convSysTotalCapacityInstalledPower = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 3, 2, 4), ScaledNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: convSysTotalCapacityInstalledPower.setStatus('current')
if mibBuilder.loadTexts: convSysTotalCapacityInstalledPower.setDescription('A converter output power multiplied by the number of converters installed.')
convSysAverageConverterOutputVoltage = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 3, 2, 5), ScaledNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: convSysAverageConverterOutputVoltage.setStatus('current')
if mibBuilder.loadTexts: convSysAverageConverterOutputVoltage.setDescription('Average converter output voltage.')
convSysAverageConverterInputVoltage = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 3, 2, 6), ScaledNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: convSysAverageConverterInputVoltage.setStatus('current')
if mibBuilder.loadTexts: convSysAverageConverterInputVoltage.setDescription('Average input voltage supplied to the converters.')
convSysSystemVoltage = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 3, 2, 7), ScaledNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: convSysSystemVoltage.setStatus('current')
if mibBuilder.loadTexts: convSysSystemVoltage.setDescription('System voltage.')
convSysTotalLoadCurrent = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 3, 2, 8), ScaledNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: convSysTotalLoadCurrent.setStatus('current')
if mibBuilder.loadTexts: convSysTotalLoadCurrent.setDescription('Total load current.')
convSysSystemNumber = MibScalar((1, 3, 6, 1, 4, 1, 7309, 5, 3, 2, 9), ScaledNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: convSysSystemNumber.setStatus('current')
if mibBuilder.loadTexts: convSysSystemNumber.setDescription('Snmp ID# assigned to the system.')
conformance = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 5, 3, 2, 100))
compliances = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 5, 3, 2, 100, 1))
compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7309, 5, 3, 2, 100, 1, 1)).setObjects(("ALPHA-CONVERTER-SYS-MIB", "converterGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    compliance = compliance.setStatus('current')
if mibBuilder.loadTexts: compliance.setDescription('The compliance statement for systems supporting the Alpha Converter System MIB.')
converterGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 7309, 5, 3, 2, 100, 2))
converterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7309, 5, 3, 2, 100, 2, 1)).setObjects(("ALPHA-CONVERTER-SYS-MIB", "convSysTotalOutputCurrent"), ("ALPHA-CONVERTER-SYS-MIB", "convSysTotalOutputPower"), ("ALPHA-CONVERTER-SYS-MIB", "convSysTotalCapacityInstalledAmps"), ("ALPHA-CONVERTER-SYS-MIB", "convSysTotalCapacityInstalledPower"), ("ALPHA-CONVERTER-SYS-MIB", "convSysAverageConverterOutputVoltage"), ("ALPHA-CONVERTER-SYS-MIB", "convSysAverageConverterInputVoltage"), ("ALPHA-CONVERTER-SYS-MIB", "convSysSystemVoltage"), ("ALPHA-CONVERTER-SYS-MIB", "convSysTotalLoadCurrent"), ("ALPHA-CONVERTER-SYS-MIB", "convSysSystemNumber"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    converterGroup = converterGroup.setStatus('current')
if mibBuilder.loadTexts: converterGroup.setDescription('Alpha converter System data list group.')
mibBuilder.exportSymbols("ALPHA-CONVERTER-SYS-MIB", convSysAverageConverterOutputVoltage=convSysAverageConverterOutputVoltage, convSysTotalOutputCurrent=convSysTotalOutputCurrent, converterGroups=converterGroups, convSysAverageConverterInputVoltage=convSysAverageConverterInputVoltage, convSysTotalOutputPower=convSysTotalOutputPower, convSysTotalCapacityInstalledPower=convSysTotalCapacityInstalledPower, convSysSystemNumber=convSysSystemNumber, PYSNMP_MODULE_ID=converterSystem, compliance=compliance, convSysSystemVoltage=convSysSystemVoltage, convSysTotalLoadCurrent=convSysTotalLoadCurrent, conformance=conformance, converterGroup=converterGroup, converterSystem=converterSystem, convSysTotalCapacityInstalledAmps=convSysTotalCapacityInstalledAmps, compliances=compliances)