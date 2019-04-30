#
# PySNMP MIB module RUCKUS-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RUCKUS-PRODUCTS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:50:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ruckusProducts, = mibBuilder.importSymbols("RUCKUS-ROOT-MIB", "ruckusProducts")
RuckusCountryCode, = mibBuilder.importSymbols("RUCKUS-TC-MIB", "RuckusCountryCode")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, IpAddress, iso, Counter64, TimeTicks, Bits, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, Counter32, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "IpAddress", "iso", "Counter64", "TimeTicks", "Bits", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "Counter32", "Integer32", "Gauge32")
MacAddress, TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TruthValue", "DisplayString", "TextualConvention")
ruckusProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 25053, 3, 1))
if mibBuilder.loadTexts: ruckusProductsMIB.setLastUpdated('201010150800Z')
if mibBuilder.loadTexts: ruckusProductsMIB.setOrganization('Ruckus Wireless, Inc.')
ruckusWirelessRouterProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 1))
ruckusWirelessAdapterProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 2))
ruckusWirelessMetroProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 3))
ruckusWirelessHotzoneProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4))
ruckusWirelessControllerProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5))
ruckusVF2825 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 1, 1))
ruckusVF2811 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 1, 2))
ruckusVF2821 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 1, 3))
ruckusVF2835 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 1, 4))
ruckusVF7811 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 1, 5))
ruckusVF2111 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 2, 1))
ruckusVF2121 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 2, 2))
ruckusVF7111 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 2, 3))
ruckusMM2225 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 3, 1))
ruckusMM2211 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 3, 2))
ruckusMM2221 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 3, 3))
ruckusZF2925 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 1))
ruckusZF2942 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 2))
ruckusZF7942 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 3))
ruckusZF7962 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 4))
ruckusZF2741 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 5))
ruckusZF7762 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 6))
ruckusZF7762S = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 8))
ruckusZF7762T = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 9))
ruckusZF7762N = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 10))
ruckusZF7343 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 12))
ruckusZF7363 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 13))
ruckusZF7341 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 14))
ruckusZF7731 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 16))
ruckusZF7025 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 20))
ruckusZF7321 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 22))
ruckusZF7321U = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 23))
ruckusZF2741EXT = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 24))
ruckusZF7982 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 25))
ruckusZF7782 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 28))
ruckusZF7782S = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 29))
ruckusZF7782N = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 30))
ruckusZF7782E = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 31))
ruckusZF8800SAC = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 32))
ruckusZF7762AC = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 35))
ruckusZF7762SAC = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 36))
ruckusZF7762TAC = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 37))
ruckusZF7372 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 40))
ruckusZF7372E = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 41))
ruckusZF7352 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 45))
ruckusZF7351 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 48))
ruckusZF7742 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 50))
ruckusZF7055 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 52))
ruckusZF7781M = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 55))
ruckusZF7781CM = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 56))
ruckusZF7781CME = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 57))
ruckusZF7781CMS = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 58))
ruckusZF7781FN = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 60))
ruckusZF7781FNE = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 61))
ruckusZF7781FNS = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 62))
ruckusSC8800SAC = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 65))
ruckusSC8800S = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 66))
ruckusZF7761CM = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7))
ruckusZF7761CMControlLED = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))).clone(namedValues=NamedValues(("ledPerCM", 1), ("ledPerAP", 2), ("ledAlternateMode1Mode2OneHour", 3), ("ledAlternateMode1Mode2Mode6", 4), ("blueActive", 5), ("blueActiveCMOnlineLed", 6), ("ledAllOff", 7), ("heartbeatOffCM", 8), ("heartbeatOffAP", 9), ("softResetAP", 10), ("powerCycleAP", 11), ("factoryResetAP", 12), ("softResetCM", 13), ("powerCycleCM", 14), ("factoryResetCM", 15))).clone('ledPerCM')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZF7761CMControlLED.setStatus('current')
ruckusZF7761CMWanIPAddr = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZF7761CMWanIPAddr.setStatus('current')
ruckusZF7761CMCustomization = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7, 5))
ruckusZF7761CMHTTPService = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7, 5, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZF7761CMHTTPService.setStatus('current')
ruckusZF7761CMTelnetService = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7, 5, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZF7761CMTelnetService.setStatus('current')
ruckusZF7761CMSSHService = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7, 5, 3), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZF7761CMSSHService.setStatus('current')
ruckusZF7761CMUsername = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7, 5, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZF7761CMUsername.setStatus('current')
ruckusZF7761CMPassword = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7, 5, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZF7761CMPassword.setStatus('current')
ruckusZF7761CMLEDMode = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("ledAllOff", 0), ("blueActive", 1), ("blueActiveCMOnlineLed", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZF7761CMLEDMode.setStatus('current')
ruckusZF7761CMHeartbeatMonitorCM = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7, 7), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZF7761CMHeartbeatMonitorCM.setStatus('current')
ruckusZF7761CMHeartbeatMonitorAP = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7, 8), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZF7761CMHeartbeatMonitorAP.setStatus('current')
ruckusZD1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 1))
ruckusZD1100 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 2))
ruckusZD3000 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 3))
ruckusZD5000 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 8))
ruckusZD1000SystemName = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1000SystemName.setStatus('current')
ruckusZD1000SystemIPAddr = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1000SystemIPAddr.setStatus('current')
ruckusZD1000SystemMacAddr = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1000SystemMacAddr.setStatus('current')
ruckusZD1000SystemUptime = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1000SystemUptime.setStatus('current')
ruckusZD1000SystemModel = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1000SystemModel.setStatus('current')
ruckusZD1000SystemLicensedAPs = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1000SystemLicensedAPs.setStatus('current')
ruckusZD1000SystemSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1000SystemSerialNumber.setStatus('current')
ruckusZD1000SystemVersion = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1000SystemVersion.setStatus('current')
ruckusZD1000CountryCode = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 1, 9), RuckusCountryCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1000CountryCode.setStatus('current')
ruckusZD1100SystemName = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 2, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1100SystemName.setStatus('current')
ruckusZD1100SystemIPAddr = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 2, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1100SystemIPAddr.setStatus('current')
ruckusZD1100SystemMacAddr = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 2, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1100SystemMacAddr.setStatus('current')
ruckusZD1100SystemUptime = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 2, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1100SystemUptime.setStatus('current')
ruckusZD1100SystemModel = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 2, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1100SystemModel.setStatus('current')
ruckusZD1100SystemLicensedAPs = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 2, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1100SystemLicensedAPs.setStatus('current')
ruckusZD1100SystemSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 2, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1100SystemSerialNumber.setStatus('current')
ruckusZD1100SystemVersion = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 2, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1100SystemVersion.setStatus('current')
ruckusZD1100CountryCode = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 2, 9), RuckusCountryCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1100CountryCode.setStatus('current')
ruckusZD3000SystemName = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 3, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD3000SystemName.setStatus('current')
ruckusZD3000SystemIPAddr = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 3, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD3000SystemIPAddr.setStatus('current')
ruckusZD3000SystemMacAddr = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 3, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD3000SystemMacAddr.setStatus('current')
ruckusZD3000SystemUptime = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 3, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD3000SystemUptime.setStatus('current')
ruckusZD3000SystemModel = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 3, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD3000SystemModel.setStatus('current')
ruckusZD3000SystemLicensedAPs = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 3, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD3000SystemLicensedAPs.setStatus('current')
ruckusZD3000SystemSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 3, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD3000SystemSerialNumber.setStatus('current')
ruckusZD3000SystemVersion = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 3, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD3000SystemVersion.setStatus('current')
ruckusZD3000CountryCode = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 3, 9), RuckusCountryCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD3000CountryCode.setStatus('current')
ruckusZD5000SystemName = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 8, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD5000SystemName.setStatus('current')
ruckusZD5000SystemIPAddr = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 8, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD5000SystemIPAddr.setStatus('current')
ruckusZD5000SystemMacAddr = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 8, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD5000SystemMacAddr.setStatus('current')
ruckusZD5000SystemUptime = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 8, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD5000SystemUptime.setStatus('current')
ruckusZD5000SystemModel = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 8, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD5000SystemModel.setStatus('current')
ruckusZD5000SystemLicensedAPs = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 8, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD5000SystemLicensedAPs.setStatus('current')
ruckusZD5000SystemSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 8, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD5000SystemSerialNumber.setStatus('current')
ruckusZD5000SystemVersion = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 8, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD5000SystemVersion.setStatus('current')
ruckusZD5000CountryCode = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 8, 9), RuckusCountryCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD5000CountryCode.setStatus('current')
mibBuilder.exportSymbols("RUCKUS-PRODUCTS-MIB", ruckusZD3000=ruckusZD3000, ruckusZD1100CountryCode=ruckusZD1100CountryCode, ruckusZF7982=ruckusZF7982, ruckusZD5000SystemLicensedAPs=ruckusZD5000SystemLicensedAPs, ruckusZD5000SystemSerialNumber=ruckusZD5000SystemSerialNumber, ruckusZF7761CMWanIPAddr=ruckusZF7761CMWanIPAddr, ruckusZF7761CMTelnetService=ruckusZF7761CMTelnetService, ruckusZF7781CMS=ruckusZF7781CMS, ruckusZF7781CME=ruckusZF7781CME, ruckusZF7321U=ruckusZF7321U, ruckusZD1100SystemLicensedAPs=ruckusZD1100SystemLicensedAPs, ruckusZF7761CMControlLED=ruckusZF7761CMControlLED, ruckusZD3000SystemUptime=ruckusZD3000SystemUptime, ruckusZD3000SystemModel=ruckusZD3000SystemModel, ruckusWirelessControllerProducts=ruckusWirelessControllerProducts, ruckusZD1000SystemLicensedAPs=ruckusZD1000SystemLicensedAPs, ruckusZD5000SystemName=ruckusZD5000SystemName, ruckusZF7341=ruckusZF7341, ruckusZD1100=ruckusZD1100, ruckusZF7762T=ruckusZF7762T, ruckusZD1000SystemUptime=ruckusZD1000SystemUptime, ruckusZD3000SystemMacAddr=ruckusZD3000SystemMacAddr, ruckusZD5000=ruckusZD5000, ruckusZD1000SystemSerialNumber=ruckusZD1000SystemSerialNumber, ruckusVF2121=ruckusVF2121, ruckusProductsMIB=ruckusProductsMIB, ruckusWirelessAdapterProducts=ruckusWirelessAdapterProducts, ruckusZF2741EXT=ruckusZF2741EXT, ruckusZD1000SystemModel=ruckusZD1000SystemModel, ruckusZF7742=ruckusZF7742, ruckusZF7782N=ruckusZF7782N, ruckusWirelessRouterProducts=ruckusWirelessRouterProducts, ruckusZF7761CM=ruckusZF7761CM, ruckusZF7761CMHeartbeatMonitorAP=ruckusZF7761CMHeartbeatMonitorAP, ruckusZF7782E=ruckusZF7782E, ruckusZF7942=ruckusZF7942, ruckusZF7781FNE=ruckusZF7781FNE, ruckusZF7321=ruckusZF7321, ruckusZD1100SystemModel=ruckusZD1100SystemModel, ruckusZF7761CMHTTPService=ruckusZF7761CMHTTPService, ruckusZF7762N=ruckusZF7762N, ruckusZF7761CMHeartbeatMonitorCM=ruckusZF7761CMHeartbeatMonitorCM, ruckusWirelessMetroProducts=ruckusWirelessMetroProducts, ruckusZD1000CountryCode=ruckusZD1000CountryCode, ruckusZF7761CMCustomization=ruckusZF7761CMCustomization, ruckusZF2741=ruckusZF2741, ruckusZF7782S=ruckusZF7782S, ruckusZF7781CM=ruckusZF7781CM, ruckusZF7762AC=ruckusZF7762AC, ruckusZF7343=ruckusZF7343, ruckusZD5000SystemUptime=ruckusZD5000SystemUptime, ruckusZF7781FN=ruckusZF7781FN, ruckusMM2221=ruckusMM2221, ruckusZF7762S=ruckusZF7762S, ruckusZD3000SystemVersion=ruckusZD3000SystemVersion, ruckusZD1000SystemName=ruckusZD1000SystemName, ruckusSC8800S=ruckusSC8800S, ruckusVF2821=ruckusVF2821, ruckusZD5000SystemModel=ruckusZD5000SystemModel, ruckusZD3000CountryCode=ruckusZD3000CountryCode, ruckusZD5000SystemVersion=ruckusZD5000SystemVersion, ruckusZD3000SystemIPAddr=ruckusZD3000SystemIPAddr, ruckusZD1100SystemUptime=ruckusZD1100SystemUptime, ruckusZD3000SystemName=ruckusZD3000SystemName, ruckusSC8800SAC=ruckusSC8800SAC, ruckusZD1000=ruckusZD1000, ruckusZD1100SystemName=ruckusZD1100SystemName, ruckusZD5000CountryCode=ruckusZD5000CountryCode, ruckusZD1000SystemMacAddr=ruckusZD1000SystemMacAddr, ruckusZF7351=ruckusZF7351, ruckusVF7811=ruckusVF7811, ruckusVF2825=ruckusVF2825, ruckusZD5000SystemMacAddr=ruckusZD5000SystemMacAddr, ruckusZF7962=ruckusZF7962, ruckusZD1100SystemSerialNumber=ruckusZD1100SystemSerialNumber, ruckusMM2211=ruckusMM2211, ruckusZF7761CMPassword=ruckusZF7761CMPassword, ruckusWirelessHotzoneProducts=ruckusWirelessHotzoneProducts, ruckusZF7762=ruckusZF7762, ruckusZF7352=ruckusZF7352, ruckusZF2942=ruckusZF2942, ruckusVF2111=ruckusVF2111, ruckusZF7731=ruckusZF7731, ruckusZD1000SystemIPAddr=ruckusZD1000SystemIPAddr, ruckusZF2925=ruckusZF2925, ruckusZF7762SAC=ruckusZF7762SAC, ruckusZF7055=ruckusZF7055, ruckusZF7781M=ruckusZF7781M, ruckusVF2835=ruckusVF2835, ruckusZD1100SystemMacAddr=ruckusZD1100SystemMacAddr, ruckusZF7025=ruckusZF7025, ruckusZF8800SAC=ruckusZF8800SAC, ruckusZD3000SystemSerialNumber=ruckusZD3000SystemSerialNumber, ruckusZD1000SystemVersion=ruckusZD1000SystemVersion, ruckusZF7372=ruckusZF7372, ruckusZF7782=ruckusZF7782, ruckusZF7761CMSSHService=ruckusZF7761CMSSHService, ruckusZD3000SystemLicensedAPs=ruckusZD3000SystemLicensedAPs, ruckusZD1100SystemIPAddr=ruckusZD1100SystemIPAddr, PYSNMP_MODULE_ID=ruckusProductsMIB, ruckusMM2225=ruckusMM2225, ruckusZF7372E=ruckusZF7372E, ruckusZF7761CMUsername=ruckusZF7761CMUsername, ruckusZD1100SystemVersion=ruckusZD1100SystemVersion, ruckusVF7111=ruckusVF7111, ruckusZF7363=ruckusZF7363, ruckusZF7762TAC=ruckusZF7762TAC, ruckusZD5000SystemIPAddr=ruckusZD5000SystemIPAddr, ruckusZF7781FNS=ruckusZF7781FNS, ruckusVF2811=ruckusVF2811, ruckusZF7761CMLEDMode=ruckusZF7761CMLEDMode)
