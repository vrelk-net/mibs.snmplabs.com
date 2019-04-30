#
# PySNMP MIB module PAIRGAIN-AGENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PAIRGAIN-AGENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:27:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
pgainAgent, = mibBuilder.importSymbols("PAIRGAIN-COMMON-HD-MIB", "pgainAgent")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Gauge32, IpAddress, Counter32, Integer32, Unsigned32, NotificationType, iso, TimeTicks, Counter64, MibIdentifier, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Gauge32", "IpAddress", "Counter32", "Integer32", "Unsigned32", "NotificationType", "iso", "TimeTicks", "Counter64", "MibIdentifier", "ModuleIdentity", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

pgAgentSw = MibIdentifier((1, 3, 6, 1, 4, 1, 927, 1, 2, 1))
pgAgentNetProtocol = MibIdentifier((1, 3, 6, 1, 4, 1, 927, 1, 2, 2))
pgSnmpAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 927, 1, 2, 3))
pgAgentHw = MibIdentifier((1, 3, 6, 1, 4, 1, 927, 1, 2, 4))
pgAgentLocImage = MibIdentifier((1, 3, 6, 1, 4, 1, 927, 1, 2, 5))
pgAgentType = MibScalar((1, 3, 6, 1, 4, 1, 927, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("pgCMU", 2), ("pgHMU", 3), ("pgEMU", 4), ("pgDMU", 5), ("pgMBMTiger", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgAgentType.setStatus('mandatory')
pgAgentFwVer = MibScalar((1, 3, 6, 1, 4, 1, 927, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgAgentFwVer.setStatus('mandatory')
pgAgentSwVer = MibScalar((1, 3, 6, 1, 4, 1, 927, 1, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgAgentSwVer.setStatus('mandatory')
pgAgentBootProtocol = MibScalar((1, 3, 6, 1, 4, 1, 927, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("bootp-tftp", 2), ("tftp-only", 3), ("ftp-only", 4), ("proprietary", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgAgentBootProtocol.setStatus('mandatory')
pgAgentBootFile = MibScalar((1, 3, 6, 1, 4, 1, 927, 1, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgAgentBootFile.setStatus('mandatory')
pgAgentAuthTraps = MibScalar((1, 3, 6, 1, 4, 1, 927, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 1))).clone(namedValues=NamedValues(("disable", 2), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgAgentAuthTraps.setStatus('mandatory')
pgAgentTraps = MibScalar((1, 3, 6, 1, 4, 1, 927, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 1))).clone(namedValues=NamedValues(("disable", 2), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgAgentTraps.setStatus('mandatory')
pgAgentMibLevel = MibScalar((1, 3, 6, 1, 4, 1, 927, 1, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgAgentMibLevel.setStatus('mandatory')
pgAgentMySlotId = MibScalar((1, 3, 6, 1, 4, 1, 927, 1, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgAgentMySlotId.setStatus('mandatory')
pgAgentIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 927, 1, 2, 2, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgAgentIpAddr.setStatus('mandatory')
pgAgentNetMask = MibScalar((1, 3, 6, 1, 4, 1, 927, 1, 2, 2, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgAgentNetMask.setStatus('mandatory')
pgAgentDefaultGateway = MibScalar((1, 3, 6, 1, 4, 1, 927, 1, 2, 2, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgAgentDefaultGateway.setStatus('mandatory')
pgAgentBootServerAddr = MibScalar((1, 3, 6, 1, 4, 1, 927, 1, 2, 2, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgAgentBootServerAddr.setStatus('mandatory')
pgAgentTrapReceiverTable = MibTable((1, 3, 6, 1, 4, 1, 927, 1, 2, 3, 1), )
if mibBuilder.loadTexts: pgAgentTrapReceiverTable.setStatus('optional')
pgAgentTrapReceiverEntry = MibTableRow((1, 3, 6, 1, 4, 1, 927, 1, 2, 3, 1, 1), ).setIndexNames((0, "PAIRGAIN-AGENT-MIB", "pgAgentTrapRcvrNetAddress"))
if mibBuilder.loadTexts: pgAgentTrapReceiverEntry.setStatus('optional')
pgAgentTrapRcvrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 2, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("valid", 2), ("invalid", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgAgentTrapRcvrStatus.setStatus('optional')
pgAgentTrapRcvrNetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 2, 3, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgAgentTrapRcvrNetAddress.setStatus('optional')
pgAgentTrapRcvrComm = MibTableColumn((1, 3, 6, 1, 4, 1, 927, 1, 2, 3, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgAgentTrapRcvrComm.setStatus('optional')
pgAgentReset = MibScalar((1, 3, 6, 1, 4, 1, 927, 1, 2, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noReset", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgAgentReset.setStatus('mandatory')
pgAgentRestart = MibScalar((1, 3, 6, 1, 4, 1, 927, 1, 2, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noRestart", 1), ("restart", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgAgentRestart.setStatus('optional')
pgAgentBootMode = MibScalar((1, 3, 6, 1, 4, 1, 927, 1, 2, 4, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("nvram", 1), ("network", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgAgentBootMode.setStatus('mandatory')
pgAgentWriteNvram = MibScalar((1, 3, 6, 1, 4, 1, 927, 1, 2, 4, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noWriteNvram", 1), ("writeNvram", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgAgentWriteNvram.setStatus('mandatory')
pgLocImageValid = MibScalar((1, 3, 6, 1, 4, 1, 927, 1, 2, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("localImageValid", 2), ("localImageInvalid", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgLocImageValid.setStatus('optional')
pgLocImageVersion = MibScalar((1, 3, 6, 1, 4, 1, 927, 1, 2, 5, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgLocImageVersion.setStatus('optional')
pgLocImageLoadMode = MibScalar((1, 3, 6, 1, 4, 1, 927, 1, 2, 5, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("network", 2), ("localBoot", 3), ("localAsBackup", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pgLocImageLoadMode.setStatus('optional')
pgLocImageActualSource = MibScalar((1, 3, 6, 1, 4, 1, 927, 1, 2, 5, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("remoteImage", 2), ("localImage", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pgLocImageActualSource.setStatus('optional')
mibBuilder.exportSymbols("PAIRGAIN-AGENT-MIB", pgAgentWriteNvram=pgAgentWriteNvram, pgAgentBootFile=pgAgentBootFile, pgAgentTrapRcvrNetAddress=pgAgentTrapRcvrNetAddress, DisplayString=DisplayString, pgAgentTrapReceiverTable=pgAgentTrapReceiverTable, pgAgentRestart=pgAgentRestart, pgAgentLocImage=pgAgentLocImage, pgAgentNetMask=pgAgentNetMask, pgAgentTrapRcvrComm=pgAgentTrapRcvrComm, pgAgentBootMode=pgAgentBootMode, pgAgentIpAddr=pgAgentIpAddr, pgAgentAuthTraps=pgAgentAuthTraps, pgAgentFwVer=pgAgentFwVer, pgAgentMySlotId=pgAgentMySlotId, pgAgentReset=pgAgentReset, pgLocImageLoadMode=pgLocImageLoadMode, pgAgentTrapRcvrStatus=pgAgentTrapRcvrStatus, pgLocImageVersion=pgLocImageVersion, pgAgentDefaultGateway=pgAgentDefaultGateway, pgAgentBootProtocol=pgAgentBootProtocol, pgAgentHw=pgAgentHw, pgAgentTraps=pgAgentTraps, pgLocImageValid=pgLocImageValid, pgLocImageActualSource=pgLocImageActualSource, pgAgentSw=pgAgentSw, pgAgentBootServerAddr=pgAgentBootServerAddr, pgAgentTrapReceiverEntry=pgAgentTrapReceiverEntry, pgAgentSwVer=pgAgentSwVer, pgAgentType=pgAgentType, pgSnmpAgent=pgSnmpAgent, pgAgentMibLevel=pgAgentMibLevel, pgAgentNetProtocol=pgAgentNetProtocol)
