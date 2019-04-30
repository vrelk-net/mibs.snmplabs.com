#
# PySNMP MIB module COSINE-GLOBAL-REG (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/COSINE-GLOBAL-REG
# Produced by pysmi-0.3.4 at Mon Apr 29 18:11:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, ObjectIdentity, iso, Integer32, Counter64, Gauge32, TimeTicks, enterprises, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, Bits, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ObjectIdentity", "iso", "Integer32", "Counter64", "Gauge32", "TimeTicks", "enterprises", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "Bits", "MibIdentifier", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
csRoot = ObjectIdentity((1, 3, 6, 1, 4, 1, 3085))
if mibBuilder.loadTexts: csRoot.setStatus('current')
csReg = ObjectIdentity((1, 3, 6, 1, 4, 1, 3085, 1))
if mibBuilder.loadTexts: csReg.setStatus('current')
csModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 3085, 1, 1))
if mibBuilder.loadTexts: csModules.setStatus('current')
csGeneric = ObjectIdentity((1, 3, 6, 1, 4, 1, 3085, 2))
if mibBuilder.loadTexts: csGeneric.setStatus('current')
csProduct = ObjectIdentity((1, 3, 6, 1, 4, 1, 3085, 3))
if mibBuilder.loadTexts: csProduct.setStatus('current')
csOrionMIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 3085, 3, 1))
if mibBuilder.loadTexts: csOrionMIB.setStatus('current')
csInVisionMIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 3085, 3, 2))
if mibBuilder.loadTexts: csInVisionMIB.setStatus('current')
csCaps = ObjectIdentity((1, 3, 6, 1, 4, 1, 3085, 4))
if mibBuilder.loadTexts: csCaps.setStatus('current')
csReqs = ObjectIdentity((1, 3, 6, 1, 4, 1, 3085, 5))
if mibBuilder.loadTexts: csReqs.setStatus('current')
csExpr = ObjectIdentity((1, 3, 6, 1, 4, 1, 3085, 6))
if mibBuilder.loadTexts: csExpr.setStatus('current')
cosineGlobalRegMod = ModuleIdentity((1, 3, 6, 1, 4, 1, 3085, 1, 1, 1))
cosineGlobalRegMod.setRevisions(('1998-03-24 13:55',))
if mibBuilder.loadTexts: cosineGlobalRegMod.setLastUpdated('9803241355Z')
if mibBuilder.loadTexts: cosineGlobalRegMod.setOrganization('Cosine Communication Co.')
mibBuilder.exportSymbols("COSINE-GLOBAL-REG", PYSNMP_MODULE_ID=cosineGlobalRegMod, csInVisionMIB=csInVisionMIB, csCaps=csCaps, csRoot=csRoot, csModules=csModules, csOrionMIB=csOrionMIB, csReg=csReg, csProduct=csProduct, cosineGlobalRegMod=cosineGlobalRegMod, csGeneric=csGeneric, csReqs=csReqs, csExpr=csExpr)