#
# PySNMP MIB module HP-PROCURVE-420-PRIVATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-PROCURVE-420-PRIVATE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:23:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, NotificationType, Counter64, Unsigned32, Counter32, IpAddress, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, iso, ObjectIdentity, mgmt, Bits, Integer32, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "NotificationType", "Counter64", "Unsigned32", "Counter32", "IpAddress", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "iso", "ObjectIdentity", "mgmt", "Bits", "Integer32", "TimeTicks", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class PhysAddress(OctetString):
    pass

class Guage32(Counter32):
    pass

class MacAddress(OctetString):
    pass

class DisplayString(OctetString):
    pass

class TruthValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 1))
    namedValues = NamedValues(("false", 2), ("true", 1))

hP = MibIdentifier((1, 3, 6, 1, 4, 1, 11))
wireless = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2))
enterprise = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3))
accessPoint = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7))
proCurve = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11))
hPProCuve420 = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37))
enterpriseApSys = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 1))
enterpriseApLineMgnt = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 2))
enterpriseApPortMgnt = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 3))
enterpriseApFileTransferMgt = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 4))
enterpriseApResetMgt = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 5))
enterpriseApIpMgt = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 6))
enterpriseAPdot11 = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7))
swHardwareVer = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swHardwareVer.setStatus('mandatory')
swBootRomVer = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swBootRomVer.setStatus('mandatory')
swOpCodeVer = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swOpCodeVer.setStatus('mandatory')
swCountryCode = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swCountryCode.setStatus('mandatory')
lineTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 2, 1), )
if mibBuilder.loadTexts: lineTable.setStatus('mandatory')
lineEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 2, 1, 1), ).setIndexNames((0, "HP-PROCURVE-420-PRIVATE-MIB", "lineIndex"))
if mibBuilder.loadTexts: lineEntry.setStatus('mandatory')
lineIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 2, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: lineIndex.setStatus('mandatory')
lineDataBits = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lineDataBits.setStatus('mandatory')
lineParity = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(99, 1, 2))).clone(namedValues=NamedValues(("none", 99), ("odd", 1), ("even", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lineParity.setStatus('mandatory')
lineSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lineSpeed.setStatus('mandatory')
lineStopBits = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lineStopBits.setStatus('mandatory')
portTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 3, 1), )
if mibBuilder.loadTexts: portTable.setStatus('mandatory')
portEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 3, 1, 1), ).setIndexNames((0, "HP-PROCURVE-420-PRIVATE-MIB", "portIndex"))
if mibBuilder.loadTexts: portEntry.setStatus('mandatory')
portIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 3, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: portIndex.setStatus('mandatory')
portName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 3, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portName.setStatus('mandatory')
portType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("other", 1), ("hundredBaseTX", 2), ("hundredBaseFX", 3), ("thousandBaseSX", 4), ("thousandBaseLX", 5), ("thousandBaseT", 6), ("thousandBaseGBIC", 7), ("thousandBaseMiniGBIC", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portType.setStatus('mandatory')
portSpeedDpxCfg = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("auto", 1), ("halfDuplex10", 2), ("fullDuplex10", 3), ("halfDuplex100", 4), ("fullDuplex100", 5), ("halfDuplex1000", 6), ("fullDuplex1000", 7))).clone('halfDuplex10')).setMaxAccess("readonly")
if mibBuilder.loadTexts: portSpeedDpxCfg.setStatus('mandatory')
portFlowCtrlCfg = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("backPressure", 3), ("dot3xFlowControl", 4))).clone('enabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: portFlowCtrlCfg.setStatus('mandatory')
portCapabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(99, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))).clone(namedValues=NamedValues(("portCap10half", 99), ("portCap10full", 1), ("portCap100half", 2), ("portCap100full", 3), ("portCap1000half", 4), ("portCap1000full", 5), ("reserved6", 6), ("reserved7", 7), ("reserved8", 8), ("reserved9", 9), ("reserved10", 10), ("reserved11", 11), ("reserved12", 12), ("reserved13", 13), ("portCapSym", 14), ("portCapFlowCtrl", 15)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portCapabilities.setStatus('mandatory')
portAutonegotiation = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portAutonegotiation.setStatus('mandatory')
portSpeedDpxStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("error", 1), ("halfDuplex10", 2), ("fullDuplex10", 3), ("halfDuplex100", 4), ("fullDuplex100", 5), ("halfDuplex1000", 6), ("fullDuplex1000", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portSpeedDpxStatus.setStatus('mandatory')
portFlowCtrlStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 3, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("error", 1), ("backPressure", 2), ("dot3xFlowControl", 3), ("none", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portFlowCtrlStatus.setStatus('mandatory')
transferStart = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("go", 1), ("nogo", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: transferStart.setStatus('mandatory')
transferType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ftp", 1), ("tftp", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: transferType.setStatus('mandatory')
fileType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 4, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("opcode", 1), ("config", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fileType.setStatus('mandatory')
srcFile = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 4, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: srcFile.setStatus('mandatory')
destFile = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 4, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: destFile.setStatus('mandatory')
fileServer = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 4, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fileServer.setStatus('mandatory')
userName = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 4, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: userName.setStatus('mandatory')
password = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 4, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: password.setStatus('mandatory')
restartOpCodeFile = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 5, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: restartOpCodeFile.setStatus('mandatory')
restartControl = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 5, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("running", 1), ("warmBoot", 2), ("coldBoot", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: restartControl.setStatus('mandatory')
netConfigIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 6, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: netConfigIPAddress.setStatus('mandatory')
netConfigSubnetMask = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 6, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: netConfigSubnetMask.setStatus('mandatory')
netDefaultGateway = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 6, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: netDefaultGateway.setStatus('mandatory')
ipHttpState = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 6, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipHttpState.setStatus('mandatory')
ipHttpPort = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 6, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipHttpPort.setStatus('mandatory')
hpdot11StationConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 1), )
if mibBuilder.loadTexts: hpdot11StationConfigTable.setStatus('mandatory')
hpdot11StationConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 1, 1), ).setIndexNames((0, "HP-PROCURVE-420-PRIVATE-MIB", "hpdot11portIndex"))
if mibBuilder.loadTexts: hpdot11StationConfigEntry.setStatus('mandatory')
hpdot11portIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: hpdot11portIndex.setStatus('mandatory')
hpdot11DesiredSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpdot11DesiredSSID.setStatus('mandatory')
hpdot11BeaconPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 1000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpdot11BeaconPeriod.setStatus('mandatory')
hpdot11DTIMPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpdot11DTIMPeriod.setStatus('mandatory')
hpdot11OperationalRateSet = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 108))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpdot11OperationalRateSet.setStatus('mandatory')
hpdot11AuthenticationAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("openSystem", 1), ("sharedKey", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpdot11AuthenticationAlgorithm.setStatus('mandatory')
hpdot11PrivacyTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 2), )
if mibBuilder.loadTexts: hpdot11PrivacyTable.setStatus('mandatory')
hpdot11PrivacyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 2, 1), ).setIndexNames((0, "HP-PROCURVE-420-PRIVATE-MIB", "hpdot11PrivacyportIndex"))
if mibBuilder.loadTexts: hpdot11PrivacyEntry.setStatus('mandatory')
hpdot11PrivacyportIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: hpdot11PrivacyportIndex.setStatus('mandatory')
hpdot11PrivacyInvoked = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpdot11PrivacyInvoked.setStatus('mandatory')
hpdot11WEPDefaultKeyID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpdot11WEPDefaultKeyID.setStatus('mandatory')
hpdot11WEPKeyMappingLength = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpdot11WEPKeyMappingLength.setStatus('mandatory')
hpdot11mac = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 3))
hpdot11OperationTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 3, 1), )
if mibBuilder.loadTexts: hpdot11OperationTable.setStatus('mandatory')
hpdot11OperationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 3, 1, 1), ).setIndexNames((0, "HP-PROCURVE-420-PRIVATE-MIB", "hpdot11OperationIndex"))
if mibBuilder.loadTexts: hpdot11OperationEntry.setStatus('mandatory')
hpdot11OperationIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 3, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: hpdot11OperationIndex.setStatus('mandatory')
hpdot11RTSThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2347))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpdot11RTSThreshold.setStatus('mandatory')
hpdot11FragmentationThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(256, 2346))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpdot11FragmentationThreshold.setStatus('mandatory')
hpdot11phy = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 4))
hpdot11PhyOperationTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 4, 1), )
if mibBuilder.loadTexts: hpdot11PhyOperationTable.setStatus('mandatory')
hpdot11PhyOperationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 4, 1, 1), ).setIndexNames((0, "HP-PROCURVE-420-PRIVATE-MIB", "hpdot11Index"))
if mibBuilder.loadTexts: hpdot11PhyOperationEntry.setStatus('mandatory')
hpdot11Index = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 4, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: hpdot11Index.setStatus('mandatory')
hpdot11CurrentChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 4, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpdot11CurrentChannel.setStatus('mandatory')
hpdot11TurboModeEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(99, 1, 2))).clone(namedValues=NamedValues(("none", 99), ("on", 1), ("off", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpdot11TurboModeEnabled.setStatus('mandatory')
hpdot11PreambleLength = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("short", 1), ("long", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpdot11PreambleLength.setStatus('mandatory')
hpdot11AuthenticationEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 5))
hpdot118021xSupport = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 5, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpdot118021xSupport.setStatus('mandatory')
hpdot118021xRequired = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 5, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpdot118021xRequired.setStatus('mandatory')
hpdot11AuthenticationServerTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 6), )
if mibBuilder.loadTexts: hpdot11AuthenticationServerTable.setStatus('mandatory')
hpdot11AuthenticationServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 6, 1), ).setIndexNames((0, "HP-PROCURVE-420-PRIVATE-MIB", "hpdot11serverIndex"))
if mibBuilder.loadTexts: hpdot11AuthenticationServerEntry.setStatus('mandatory')
hpdot11serverIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 6, 1, 1), Integer32())
if mibBuilder.loadTexts: hpdot11serverIndex.setStatus('mandatory')
hpdot11AuthenticationServer = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 6, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpdot11AuthenticationServer.setStatus('mandatory')
hpdot11AuthenticationPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 6, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1024, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpdot11AuthenticationPort.setStatus('mandatory')
hpdot11AuthenticationKey = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 6, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpdot11AuthenticationKey.setStatus('mandatory')
hpdot11AuthenticationRetransmit = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 6, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpdot11AuthenticationRetransmit.setStatus('mandatory')
hpdot11AuthenticationTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 6, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 60))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpdot11AuthenticationTimeout.setStatus('mandatory')
hpdot11FilterTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 7), )
if mibBuilder.loadTexts: hpdot11FilterTable.setStatus('mandatory')
hpdot11FilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 7, 1), ).setIndexNames((0, "HP-PROCURVE-420-PRIVATE-MIB", "hpdot11FilterIndex"))
if mibBuilder.loadTexts: hpdot11FilterEntry.setStatus('mandatory')
hpdot11FilterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 7, 1, 1), Integer32())
if mibBuilder.loadTexts: hpdot11FilterIndex.setStatus('mandatory')
hpdot11FilterAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 7, 1, 2), PhysAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpdot11FilterAddress.setStatus('mandatory')
hpdot11FilterStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(30, 31))).clone(namedValues=NamedValues(("allowed", 30), ("denied", 31)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpdot11FilterStatus.setStatus('mandatory')
hpdot11smt = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 8))
hpdot11WEPDefaultKeys11g = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 8, 1))
hpdot11WEPDefaultKeys11gTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 8, 1, 1), )
if mibBuilder.loadTexts: hpdot11WEPDefaultKeys11gTable.setStatus('mandatory')
hpdot11WEPDefaultKeys11gEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 8, 1, 1, 1), ).setIndexNames((0, "HP-PROCURVE-420-PRIVATE-MIB", "dot11WEPDefaultKey11gLength"))
if mibBuilder.loadTexts: hpdot11WEPDefaultKeys11gEntry.setStatus('mandatory')
hpdot11WEPDefaultKey11gLength = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 8, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(64, 128, 152))).clone(namedValues=NamedValues(("sixtyFour", 64), ("oneHundredTwentyEight", 128), ("oneHundredFiftyTwo", 152))).clone('oneHundredTwentyEight')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpdot11WEPDefaultKey11gLength.setStatus('mandatory')
hpdot11WEPDefaultKey11gIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 8, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4)))
if mibBuilder.loadTexts: hpdot11WEPDefaultKey11gIndex.setStatus('mandatory')
hpdot11WEPDefaultKey11gValue = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37, 7, 8, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpdot11WEPDefaultKey11gValue.setStatus('mandatory')
mibBuilder.exportSymbols("HP-PROCURVE-420-PRIVATE-MIB", restartControl=restartControl, hpdot11FragmentationThreshold=hpdot11FragmentationThreshold, hpdot11StationConfigEntry=hpdot11StationConfigEntry, hpdot11AuthenticationServerTable=hpdot11AuthenticationServerTable, DisplayString=DisplayString, hpdot11CurrentChannel=hpdot11CurrentChannel, hpdot11WEPDefaultKeys11gEntry=hpdot11WEPDefaultKeys11gEntry, hpdot11WEPDefaultKeys11g=hpdot11WEPDefaultKeys11g, lineStopBits=lineStopBits, portEntry=portEntry, hpdot11AuthenticationServer=hpdot11AuthenticationServer, hpdot11PrivacyInvoked=hpdot11PrivacyInvoked, portSpeedDpxCfg=portSpeedDpxCfg, netConfigSubnetMask=netConfigSubnetMask, hpdot11WEPDefaultKeyID=hpdot11WEPDefaultKeyID, fileServer=fileServer, hpdot11PrivacyEntry=hpdot11PrivacyEntry, enterprise=enterprise, portCapabilities=portCapabilities, hpdot11FilterTable=hpdot11FilterTable, srcFile=srcFile, userName=userName, portSpeedDpxStatus=portSpeedDpxStatus, hpdot11PreambleLength=hpdot11PreambleLength, hpdot11phy=hpdot11phy, swOpCodeVer=swOpCodeVer, transferType=transferType, hpdot11OperationTable=hpdot11OperationTable, portIndex=portIndex, accessPoint=accessPoint, enterpriseApLineMgnt=enterpriseApLineMgnt, hpdot11WEPDefaultKey11gIndex=hpdot11WEPDefaultKey11gIndex, hpdot11PhyOperationTable=hpdot11PhyOperationTable, enterpriseApSys=enterpriseApSys, swHardwareVer=swHardwareVer, MacAddress=MacAddress, PhysAddress=PhysAddress, hPProCuve420=hPProCuve420, hpdot11StationConfigTable=hpdot11StationConfigTable, password=password, restartOpCodeFile=restartOpCodeFile, swBootRomVer=swBootRomVer, hpdot11mac=hpdot11mac, portAutonegotiation=portAutonegotiation, hpdot11DesiredSSID=hpdot11DesiredSSID, portFlowCtrlCfg=portFlowCtrlCfg, hpdot11PrivacyportIndex=hpdot11PrivacyportIndex, destFile=destFile, portType=portType, TruthValue=TruthValue, hpdot118021xSupport=hpdot118021xSupport, hpdot11portIndex=hpdot11portIndex, lineIndex=lineIndex, hpdot11AuthenticationAlgorithm=hpdot11AuthenticationAlgorithm, lineDataBits=lineDataBits, hpdot11WEPDefaultKeys11gTable=hpdot11WEPDefaultKeys11gTable, hpdot11AuthenticationTimeout=hpdot11AuthenticationTimeout, hpdot11AuthenticationServerEntry=hpdot11AuthenticationServerEntry, fileType=fileType, hpdot11RTSThreshold=hpdot11RTSThreshold, wireless=wireless, hpdot11PrivacyTable=hpdot11PrivacyTable, hpdot118021xRequired=hpdot118021xRequired, hpdot11AuthenticationRetransmit=hpdot11AuthenticationRetransmit, Guage32=Guage32, hpdot11serverIndex=hpdot11serverIndex, hpdot11DTIMPeriod=hpdot11DTIMPeriod, transferStart=transferStart, lineTable=lineTable, hpdot11TurboModeEnabled=hpdot11TurboModeEnabled, hpdot11AuthenticationPort=hpdot11AuthenticationPort, portName=portName, hpdot11AuthenticationEntry=hpdot11AuthenticationEntry, proCurve=proCurve, hpdot11FilterAddress=hpdot11FilterAddress, enterpriseApResetMgt=enterpriseApResetMgt, lineEntry=lineEntry, hpdot11WEPKeyMappingLength=hpdot11WEPKeyMappingLength, lineParity=lineParity, hpdot11smt=hpdot11smt, ipHttpPort=ipHttpPort, hpdot11AuthenticationKey=hpdot11AuthenticationKey, hpdot11FilterStatus=hpdot11FilterStatus, hpdot11OperationIndex=hpdot11OperationIndex, hpdot11WEPDefaultKey11gLength=hpdot11WEPDefaultKey11gLength, hpdot11OperationEntry=hpdot11OperationEntry, hpdot11OperationalRateSet=hpdot11OperationalRateSet, ipHttpState=ipHttpState, enterpriseApIpMgt=enterpriseApIpMgt, hpdot11BeaconPeriod=hpdot11BeaconPeriod, hpdot11FilterEntry=hpdot11FilterEntry, portFlowCtrlStatus=portFlowCtrlStatus, enterpriseApFileTransferMgt=enterpriseApFileTransferMgt, netDefaultGateway=netDefaultGateway, hpdot11Index=hpdot11Index, enterpriseApPortMgnt=enterpriseApPortMgnt, portTable=portTable, lineSpeed=lineSpeed, netConfigIPAddress=netConfigIPAddress, hpdot11FilterIndex=hpdot11FilterIndex, hpdot11WEPDefaultKey11gValue=hpdot11WEPDefaultKey11gValue, hP=hP, hpdot11PhyOperationEntry=hpdot11PhyOperationEntry, enterpriseAPdot11=enterpriseAPdot11, swCountryCode=swCountryCode)
