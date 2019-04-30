#
# PySNMP MIB module GEN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GEN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:08:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, enterprises, IpAddress, ObjectIdentity, NotificationType, Counter32, ModuleIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, iso, Gauge32, Unsigned32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "enterprises", "IpAddress", "ObjectIdentity", "NotificationType", "Counter32", "ModuleIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "iso", "Gauge32", "Unsigned32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
lannet = MibIdentifier((1, 3, 6, 1, 4, 1, 81))
madge = MibIdentifier((1, 3, 6, 1, 4, 1, 494))
lntOID = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 17))
deviceMgr = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 20))
probe = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 22))
lBoxOID = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 17, 1))
lUnknownBoxOID = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 17, 1, 1))
lLET18BoxOID = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 17, 1, 2))
lLET3BoxOID = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 17, 1, 3))
lLET36BoxOID = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 17, 1, 4))
lLET18EBoxOID = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 17, 1, 5))
lLERT40BoxOID = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 17, 1, 6))
lLET10BoxOID = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 17, 1, 7))
lFDX100BoxOID = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 17, 1, 8))
lSTACKBoxOID = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 17, 1, 9))
lLET20BoxOID = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 17, 1, 10))
lLET36_01_02BoxOID = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 17, 1, 11)).setLabel("lLET36-01-02BoxOID")
visageBoxOID = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 17, 1, 12))
visage16155BoxOID = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 17, 1, 13))
letM770BoxOID = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 17, 1, 14))
m770BoxOID = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 17, 1, 15))
m770AtmOID = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 17, 1, 16))
cajunP330OID = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 17, 1, 17))
cajunP130OID = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 17, 1, 18))
cajunP360OID = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 17, 1, 19))
smartDevicesOID = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 17, 2))
unknownDeviceOID = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 17, 2, 1))
lsaOID = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 17, 2, 2))
iasOID = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 17, 2, 3))
collage530OID = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 17, 2, 4))
eaxOID = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 17, 2, 5))
lsfOID = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 17, 2, 6))
lsa2OID = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 17, 2, 7))
mmlsOID = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 17, 2, 8))
visage26OID = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 17, 2, 9))
lbt155plusOID = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 17, 2, 10))
cajunP120OID = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 17, 2, 11))
visage26PlusOID = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 17, 2, 12))
cajunP333ROID = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 17, 2, 13))
cajunP122OID = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 17, 2, 14))
cajunP330AtmOID = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 17, 2, 15))
mibBuilder.exportSymbols("GEN-MIB", cajunP330OID=cajunP330OID, unknownDeviceOID=unknownDeviceOID, lFDX100BoxOID=lFDX100BoxOID, m770AtmOID=m770AtmOID, smartDevicesOID=smartDevicesOID, visage26OID=visage26OID, lLET36_01_02BoxOID=lLET36_01_02BoxOID, lntOID=lntOID, iasOID=iasOID, mmlsOID=mmlsOID, lLET10BoxOID=lLET10BoxOID, visage16155BoxOID=visage16155BoxOID, lLET3BoxOID=lLET3BoxOID, cajunP130OID=cajunP130OID, cajunP333ROID=cajunP333ROID, collage530OID=collage530OID, lLET36BoxOID=lLET36BoxOID, cajunP120OID=cajunP120OID, lsa2OID=lsa2OID, cajunP360OID=cajunP360OID, lbt155plusOID=lbt155plusOID, cajunP122OID=cajunP122OID, letM770BoxOID=letM770BoxOID, lLERT40BoxOID=lLERT40BoxOID, visageBoxOID=visageBoxOID, lLET18BoxOID=lLET18BoxOID, probe=probe, lUnknownBoxOID=lUnknownBoxOID, lsaOID=lsaOID, lBoxOID=lBoxOID, madge=madge, lSTACKBoxOID=lSTACKBoxOID, eaxOID=eaxOID, visage26PlusOID=visage26PlusOID, lLET18EBoxOID=lLET18EBoxOID, cajunP330AtmOID=cajunP330AtmOID, lsfOID=lsfOID, m770BoxOID=m770BoxOID, lannet=lannet, deviceMgr=deviceMgr, lLET20BoxOID=lLET20BoxOID)
