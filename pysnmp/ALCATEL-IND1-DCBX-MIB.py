#
# PySNMP MIB module ALCATEL-IND1-DCBX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALCATEL-IND1-DCBX-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:01:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
softentIND1Dcbx, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "softentIND1Dcbx")
VfcEnableState, = mibBuilder.importSymbols("ALCATEL-IND1-VIRTUAL-FLOW-CONTROL-MIB", "VfcEnableState")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
IEEE8021PriorityValue, = mibBuilder.importSymbols("IEEE8021-TC-MIB", "IEEE8021PriorityValue")
LldpXdot1dcbxAppProtocol, LldpXdot1dcbxTrafficSelectionAlgorithm, LldpXdot1dcbxAppSelector, lldpXdot1dcbxAdminApplicationPriorityAESelector, LldpXdot1dcbxTrafficClassBandwidthValue, lldpXdot1dcbxAdminApplicationPriorityAEProtocol, LldpXdot1dcbxSupportedCapacity, LldpXdot1dcbxTrafficClassValue = mibBuilder.importSymbols("LLDP-EXT-DOT1-V2-MIB", "LldpXdot1dcbxAppProtocol", "LldpXdot1dcbxTrafficSelectionAlgorithm", "LldpXdot1dcbxAppSelector", "lldpXdot1dcbxAdminApplicationPriorityAESelector", "LldpXdot1dcbxTrafficClassBandwidthValue", "lldpXdot1dcbxAdminApplicationPriorityAEProtocol", "LldpXdot1dcbxSupportedCapacity", "LldpXdot1dcbxTrafficClassValue")
lldpV2LocPortIfIndex, = mibBuilder.importSymbols("LLDP-V2-MIB", "lldpV2LocPortIfIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Integer32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, ModuleIdentity, TimeTicks, Counter64, Unsigned32, Counter32, NotificationType, ObjectIdentity, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "ModuleIdentity", "TimeTicks", "Counter64", "Unsigned32", "Counter32", "NotificationType", "ObjectIdentity", "Gauge32", "iso")
TextualConvention, RowStatus, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "TruthValue", "DisplayString")
alcatelIND1DcbxMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1))
alcatelIND1DcbxMIB.setRevisions(('2011-06-28 00:00',))
if mibBuilder.loadTexts: alcatelIND1DcbxMIB.setLastUpdated('201106280000Z')
if mibBuilder.loadTexts: alcatelIND1DcbxMIB.setOrganization('Alcatel-Lucent')
alcatelIND1DcbxMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1))
if mibBuilder.loadTexts: alcatelIND1DcbxMIBObjects.setStatus('current')
alcatelIND1DcbxMIBConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 2))
if mibBuilder.loadTexts: alcatelIND1DcbxMIBConformance.setStatus('current')
alcatelIND1DcbxMIBGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 2, 1))
if mibBuilder.loadTexts: alcatelIND1DcbxMIBGroups.setStatus('current')
alcatelIND1DcbxMIBCompliances = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 2, 2))
if mibBuilder.loadTexts: alcatelIND1DcbxMIBCompliances.setStatus('current')
alaDcbxConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1))
alaDcbxConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 2))
class DcbxTrafficFlow(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("tfLossy", 0), ("tfLossless", 1))

class DcbxPriorityTCMap(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(32, 32)
    fixedLength = 32

class DcbxStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("ok", 0), ("pfcResourcesExhausted", 1), ("pfcTlvMismatch", 2), ("etsTlvMismatch", 3), ("etsPfcTlvMismatch", 4))

class DcbxActionTaken(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("na", 0), ("restEtsAdminCfg", 1), ("restPfcAdminCfg", 2), ("disabledPfc", 3), ("restEtsPfcAdminCfg", 4), ("cfgLocalAdmin", 5), ("cfgLocalRecom", 6), ("cfgRemoteAdmin", 7), ("cfgRemoteRecom", 8))

class DcbxTCsPresent(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 1)
    fixedLength = 1

class DcbxVersion(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("ieee", 0), ("cee", 1), ("auto", 2))

class RemoteDcbxVersion(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("ieee", 0), ("cee", 1), ("auto", 2), ("unknown", 3))

alaDcbxDCProfileTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 1), )
if mibBuilder.loadTexts: alaDcbxDCProfileTable.setStatus('current')
alaDcbxDCProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 1, 1), ).setIndexNames((0, "ALCATEL-IND1-DCBX-MIB", "alaDcbxDCPId"))
if mibBuilder.loadTexts: alaDcbxDCProfileEntry.setStatus('current')
alaDcbxDCPId = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 128)))
if mibBuilder.loadTexts: alaDcbxDCPId.setStatus('current')
alaDcbxDCPName = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaDcbxDCPName.setStatus('current')
alaDcbxDCPETSTrafficClassesSupported = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 1, 1, 3), LldpXdot1dcbxSupportedCapacity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaDcbxDCPETSTrafficClassesSupported.setStatus('current')
alaDcbxDCPPFCCap = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 1, 1, 4), LldpXdot1dcbxSupportedCapacity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaDcbxDCPPFCCap.setStatus('current')
alaDcbxDCPPriorityTCMap = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 1, 1, 5), DcbxPriorityTCMap()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaDcbxDCPPriorityTCMap.setStatus('current')
alaDcbxDCPTemplateDCPId = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaDcbxDCPTemplateDCPId.setStatus('current')
alaDcbxDCPTemplateDCPName = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 1, 1, 7), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaDcbxDCPTemplateDCPName.setStatus('current')
alaDcbxDCPTCsPresent = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 1, 1, 8), DcbxTCsPresent()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaDcbxDCPTCsPresent.setStatus('current')
alaDcbxDCP8023xPauseReady = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 1, 1, 9), VfcEnableState().clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaDcbxDCP8023xPauseReady.setStatus('current')
alaDcbxDCPRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 1, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaDcbxDCPRowStatus.setStatus('current')
alaDcbxDCPTrafficClassTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 2), )
if mibBuilder.loadTexts: alaDcbxDCPTrafficClassTable.setStatus('current')
alaDcbxDCPTCEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 2, 1), ).setIndexNames((0, "ALCATEL-IND1-DCBX-MIB", "alaDcbxDCPTCDCPId"), (0, "ALCATEL-IND1-DCBX-MIB", "alaDcbxDCPTCTrafficClass"))
if mibBuilder.loadTexts: alaDcbxDCPTCEntry.setStatus('current')
alaDcbxDCPTCDCPId = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 128)))
if mibBuilder.loadTexts: alaDcbxDCPTCDCPId.setStatus('current')
alaDcbxDCPTCTrafficClass = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 2, 1, 2), LldpXdot1dcbxTrafficClassValue())
if mibBuilder.loadTexts: alaDcbxDCPTCTrafficClass.setStatus('current')
alaDcbxDCPTCDCPName = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 2, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDcbxDCPTCDCPName.setStatus('current')
alaDcbxDCPTCMaximumBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 2, 1, 4), LldpXdot1dcbxTrafficClassBandwidthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDcbxDCPTCMaximumBandwidth.setStatus('current')
alaDcbxDCPTCMinimumBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 2, 1, 5), LldpXdot1dcbxTrafficClassBandwidthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDcbxDCPTCMinimumBandwidth.setStatus('current')
alaDcbxDCPTCPFCLinkDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 2, 1, 6), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(10, 100), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDcbxDCPTCPFCLinkDelay.setStatus('current')
alaDcbxDCPTCPFCLinkDelayUserModified = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 2, 1, 7), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaDcbxDCPTCPFCLinkDelayUserModified.setStatus('current')
alaDcbxDCPTCPFCTrafficFlow = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 2, 1, 8), DcbxTrafficFlow()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDcbxDCPTCPFCTrafficFlow.setStatus('current')
alaDcbxDCPTCPriorityMap = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 2, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaDcbxDCPTCPriorityMap.setStatus('current')
alaDcbxDCPTCTrafficScheduler = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 2, 1, 10), LldpXdot1dcbxTrafficSelectionAlgorithm()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaDcbxDCPTCTrafficScheduler.setStatus('current')
alaDcbxDCPTCRecommendedBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 2, 1, 11), LldpXdot1dcbxTrafficClassBandwidthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDcbxDCPTCRecommendedBandwidth.setStatus('current')
alaDcbxDCPTCRecommendedTrafficScheduler = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 2, 1, 12), LldpXdot1dcbxTrafficSelectionAlgorithm()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaDcbxDCPTCRecommendedTrafficScheduler.setStatus('current')
alaDcbxPortInstanceTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 3), )
if mibBuilder.loadTexts: alaDcbxPortInstanceTable.setStatus('current')
alaDcbxPortInstanceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 3, 1), ).setIndexNames((0, "ALCATEL-IND1-DCBX-MIB", "alaDcbxPIIfIndex"))
if mibBuilder.loadTexts: alaDcbxPortInstanceEntry.setStatus('current')
alaDcbxPIIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: alaDcbxPIIfIndex.setStatus('current')
alaDcbxPIDCBXAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 3, 1, 2), VfcEnableState().clone('enabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaDcbxPIDCBXAdmin.setStatus('current')
alaDcbxPIDCBXOper = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 3, 1, 3), VfcEnableState().clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaDcbxPIDCBXOper.setStatus('current')
alaDcbxPIAdminDCPId = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 3, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaDcbxPIAdminDCPId.setStatus('current')
alaDcbxPIAdminDCPName = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 3, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaDcbxPIAdminDCPName.setStatus('current')
alaDcbxPILocalModified = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 3, 1, 6), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaDcbxPILocalModified.setStatus('current')
alaDcbxPIPFCDefense = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 3, 1, 7), VfcEnableState().clone('enabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaDcbxPIPFCDefense.setStatus('current')
alaDcbxPIPFCStatsClear = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 3, 1, 8), VfcEnableState().clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaDcbxPIPFCStatsClear.setStatus('current')
alaDcbxPIStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 3, 1, 9), DcbxStatus().clone('ok')).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaDcbxPIStatus.setStatus('current')
alaDcbxPIActionTaken = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 3, 1, 10), DcbxActionTaken().clone('na')).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaDcbxPIActionTaken.setStatus('current')
alaDcbxPIRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 3, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaDcbxPIRowStatus.setStatus('current')
alaDcbxPIDCBXVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 3, 1, 12), DcbxVersion()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaDcbxPIDCBXVersion.setStatus('current')
alaDcbxPIDCBXOperVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 3, 1, 13), DcbxVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaDcbxPIDCBXOperVersion.setStatus('current')
alaDcbxPIDCBXRemoteOperVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 3, 1, 14), RemoteDcbxVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaDcbxPIDCBXRemoteOperVersion.setStatus('current')
alaDcbxPIPriorityTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 4), )
if mibBuilder.loadTexts: alaDcbxPIPriorityTable.setStatus('current')
alaDcbxPIPrioEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 4, 1), ).setIndexNames((0, "ALCATEL-IND1-DCBX-MIB", "alaDcbxPIPrioIfIndex"), (0, "ALCATEL-IND1-DCBX-MIB", "alaDcbxPIPrioPriority"))
if mibBuilder.loadTexts: alaDcbxPIPrioEntry.setStatus('current')
alaDcbxPIPrioIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 4, 1, 1), Unsigned32())
if mibBuilder.loadTexts: alaDcbxPIPrioIfIndex.setStatus('current')
alaDcbxPIPrioPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 4, 1, 2), IEEE8021PriorityValue())
if mibBuilder.loadTexts: alaDcbxPIPrioPriority.setStatus('current')
alaDcbxPIPrioTC = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 4, 1, 3), LldpXdot1dcbxTrafficClassValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaDcbxPIPrioTC.setStatus('current')
alaDcbxPIPrioPFCPacketsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 4, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaDcbxPIPrioPFCPacketsReceived.setStatus('current')
alaDcbxPIPrioPFCPacketsTransmitted = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 4, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaDcbxPIPrioPFCPacketsTransmitted.setStatus('current')
alaDcbxPfcLLPrioritiesUsed = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaDcbxPfcLLPrioritiesUsed.setStatus('deprecated')
alaDcbxPfcLLPrioritiesReserved = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaDcbxPfcLLPrioritiesReserved.setStatus('deprecated')
alaDcbxPfcLLPrioritiesAvailable = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaDcbxPfcLLPrioritiesAvailable.setStatus('deprecated')
alaDcbxPfcUsageTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 8), )
if mibBuilder.loadTexts: alaDcbxPfcUsageTable.setStatus('current')
alaDcbxPfcUsageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 8, 1), ).setIndexNames((0, "ALCATEL-IND1-DCBX-MIB", "alaDcbxPfcUsageChassisId"))
if mibBuilder.loadTexts: alaDcbxPfcUsageEntry.setStatus('current')
alaDcbxPfcUsageChassisId = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 8, 1, 1), Unsigned32())
if mibBuilder.loadTexts: alaDcbxPfcUsageChassisId.setStatus('current')
alaDcbxPfcUsagePrioritiesUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 8, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaDcbxPfcUsagePrioritiesUsed.setStatus('current')
alaDcbxPfcUsagePrioritiesReserved = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 8, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaDcbxPfcUsagePrioritiesReserved.setStatus('current')
alaDcbxPfcUsagePrioritiesAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 8, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaDcbxPfcUsagePrioritiesAvailable.setStatus('current')
alaXdot1dcbxAdminApplicationPriorityAppTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 9), )
if mibBuilder.loadTexts: alaXdot1dcbxAdminApplicationPriorityAppTable.setStatus('current')
alaXdot1dcbxAdminApplicationPriorityAppEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 9, 1), ).setIndexNames((0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"), (0, "LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxAdminApplicationPriorityAESelector"), (0, "LLDP-EXT-DOT1-V2-MIB", "lldpXdot1dcbxAdminApplicationPriorityAEProtocol"))
if mibBuilder.loadTexts: alaXdot1dcbxAdminApplicationPriorityAppEntry.setStatus('current')
alaXdot1dcbxAdminApplicationPriorityAEPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 9, 1, 1), IEEE8021PriorityValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaXdot1dcbxAdminApplicationPriorityAEPriority.setStatus('current')
alaXdot1dcbxAdminApplicationPriorityAppRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 1, 1, 9, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaXdot1dcbxAdminApplicationPriorityAppRowStatus.setStatus('current')
alcatelIND1DcbxMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-DCBX-MIB", "alaDcbxDCProfileGroup"), ("ALCATEL-IND1-DCBX-MIB", "alaDcbxDCPTrafficClassGroup"), ("ALCATEL-IND1-DCBX-MIB", "alaDcbxPortInstanceGroup"), ("ALCATEL-IND1-DCBX-MIB", "alaDcbxPortInstancePriorityGroup"), ("ALCATEL-IND1-DCBX-MIB", "alaDcbxPfcUsageGroup"), ("ALCATEL-IND1-DCBX-MIB", "alaDcbxPfcUsageNewGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alcatelIND1DcbxMIBCompliance = alcatelIND1DcbxMIBCompliance.setStatus('current')
alaDcbxDCProfileGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-DCBX-MIB", "alaDcbxDCPName"), ("ALCATEL-IND1-DCBX-MIB", "alaDcbxDCPETSTrafficClassesSupported"), ("ALCATEL-IND1-DCBX-MIB", "alaDcbxDCPPFCCap"), ("ALCATEL-IND1-DCBX-MIB", "alaDcbxDCPPriorityTCMap"), ("ALCATEL-IND1-DCBX-MIB", "alaDcbxDCPTemplateDCPId"), ("ALCATEL-IND1-DCBX-MIB", "alaDcbxDCPTemplateDCPName"), ("ALCATEL-IND1-DCBX-MIB", "alaDcbxDCPTCsPresent"), ("ALCATEL-IND1-DCBX-MIB", "alaDcbxDCP8023xPauseReady"), ("ALCATEL-IND1-DCBX-MIB", "alaDcbxDCPRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaDcbxDCProfileGroup = alaDcbxDCProfileGroup.setStatus('current')
alaDcbxDCPTrafficClassGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 2, 1, 2)).setObjects(("ALCATEL-IND1-DCBX-MIB", "alaDcbxDCPTCDCPName"), ("ALCATEL-IND1-DCBX-MIB", "alaDcbxDCPTCMaximumBandwidth"), ("ALCATEL-IND1-DCBX-MIB", "alaDcbxDCPTCMinimumBandwidth"), ("ALCATEL-IND1-DCBX-MIB", "alaDcbxDCPTCPFCLinkDelay"), ("ALCATEL-IND1-DCBX-MIB", "alaDcbxDCPTCPFCLinkDelayUserModified"), ("ALCATEL-IND1-DCBX-MIB", "alaDcbxDCPTCPFCTrafficFlow"), ("ALCATEL-IND1-DCBX-MIB", "alaDcbxDCPTCPriorityMap"), ("ALCATEL-IND1-DCBX-MIB", "alaDcbxDCPTCTrafficScheduler"), ("ALCATEL-IND1-DCBX-MIB", "alaDcbxDCPTCRecommendedBandwidth"), ("ALCATEL-IND1-DCBX-MIB", "alaDcbxDCPTCRecommendedTrafficScheduler"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaDcbxDCPTrafficClassGroup = alaDcbxDCPTrafficClassGroup.setStatus('current')
alaDcbxPortInstanceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 2, 1, 3)).setObjects(("ALCATEL-IND1-DCBX-MIB", "alaDcbxPIDCBXAdmin"), ("ALCATEL-IND1-DCBX-MIB", "alaDcbxPIDCBXOper"), ("ALCATEL-IND1-DCBX-MIB", "alaDcbxPIAdminDCPId"), ("ALCATEL-IND1-DCBX-MIB", "alaDcbxPIAdminDCPName"), ("ALCATEL-IND1-DCBX-MIB", "alaDcbxPILocalModified"), ("ALCATEL-IND1-DCBX-MIB", "alaDcbxPIPFCDefense"), ("ALCATEL-IND1-DCBX-MIB", "alaDcbxPIPFCStatsClear"), ("ALCATEL-IND1-DCBX-MIB", "alaDcbxPIStatus"), ("ALCATEL-IND1-DCBX-MIB", "alaDcbxPIActionTaken"), ("ALCATEL-IND1-DCBX-MIB", "alaDcbxPIRowStatus"), ("ALCATEL-IND1-DCBX-MIB", "alaDcbxPIDCBXVersion"), ("ALCATEL-IND1-DCBX-MIB", "alaDcbxPIDCBXOperVersion"), ("ALCATEL-IND1-DCBX-MIB", "alaDcbxPIDCBXRemoteOperVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaDcbxPortInstanceGroup = alaDcbxPortInstanceGroup.setStatus('current')
alaDcbxPortInstancePriorityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 2, 1, 4)).setObjects(("ALCATEL-IND1-DCBX-MIB", "alaDcbxPIPrioTC"), ("ALCATEL-IND1-DCBX-MIB", "alaDcbxPIPrioPFCPacketsReceived"), ("ALCATEL-IND1-DCBX-MIB", "alaDcbxPIPrioPFCPacketsTransmitted"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaDcbxPortInstancePriorityGroup = alaDcbxPortInstancePriorityGroup.setStatus('current')
alaDcbxPfcUsageGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 2, 1, 5)).setObjects(("ALCATEL-IND1-DCBX-MIB", "alaDcbxPfcLLPrioritiesUsed"), ("ALCATEL-IND1-DCBX-MIB", "alaDcbxPfcLLPrioritiesReserved"), ("ALCATEL-IND1-DCBX-MIB", "alaDcbxPfcLLPrioritiesAvailable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaDcbxPfcUsageGroup = alaDcbxPfcUsageGroup.setStatus('current')
alaDcbxPfcUsageNewGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 2, 1, 6)).setObjects(("ALCATEL-IND1-DCBX-MIB", "alaDcbxPfcUsagePrioritiesUsed"), ("ALCATEL-IND1-DCBX-MIB", "alaDcbxPfcUsagePrioritiesReserved"), ("ALCATEL-IND1-DCBX-MIB", "alaDcbxPfcUsagePrioritiesAvailable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaDcbxPfcUsageNewGroup = alaDcbxPfcUsageNewGroup.setStatus('current')
alaXdot1dcbxAdminApplicationPriorityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 72, 1, 2, 1, 7)).setObjects(("ALCATEL-IND1-DCBX-MIB", "alaXdot1dcbxAdminApplicationPriorityAEPriority"), ("ALCATEL-IND1-DCBX-MIB", "alaXdot1dcbxAdminApplicationPriorityAppRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaXdot1dcbxAdminApplicationPriorityGroup = alaXdot1dcbxAdminApplicationPriorityGroup.setStatus('current')
mibBuilder.exportSymbols("ALCATEL-IND1-DCBX-MIB", alcatelIND1DcbxMIBConformance=alcatelIND1DcbxMIBConformance, alaDcbxPfcUsagePrioritiesUsed=alaDcbxPfcUsagePrioritiesUsed, alaDcbxConfig=alaDcbxConfig, alaDcbxDCPRowStatus=alaDcbxDCPRowStatus, alaDcbxPIIfIndex=alaDcbxPIIfIndex, DcbxTrafficFlow=DcbxTrafficFlow, alaDcbxDCPTrafficClassGroup=alaDcbxDCPTrafficClassGroup, DcbxPriorityTCMap=DcbxPriorityTCMap, alcatelIND1DcbxMIBCompliances=alcatelIND1DcbxMIBCompliances, alaDcbxDCPTCRecommendedTrafficScheduler=alaDcbxDCPTCRecommendedTrafficScheduler, alaDcbxDCPTCRecommendedBandwidth=alaDcbxDCPTCRecommendedBandwidth, alaDcbxPortInstanceTable=alaDcbxPortInstanceTable, PYSNMP_MODULE_ID=alcatelIND1DcbxMIB, alaDcbxPIStatus=alaDcbxPIStatus, alaXdot1dcbxAdminApplicationPriorityGroup=alaXdot1dcbxAdminApplicationPriorityGroup, alaDcbxPfcUsageGroup=alaDcbxPfcUsageGroup, alaDcbxPIDCBXOper=alaDcbxPIDCBXOper, alaDcbxPortInstanceGroup=alaDcbxPortInstanceGroup, alcatelIND1DcbxMIBCompliance=alcatelIND1DcbxMIBCompliance, alcatelIND1DcbxMIBGroups=alcatelIND1DcbxMIBGroups, alaDcbxPortInstancePriorityGroup=alaDcbxPortInstancePriorityGroup, RemoteDcbxVersion=RemoteDcbxVersion, alaDcbxPIPrioPFCPacketsTransmitted=alaDcbxPIPrioPFCPacketsTransmitted, alaDcbxPfcLLPrioritiesUsed=alaDcbxPfcLLPrioritiesUsed, alaDcbxPfcUsagePrioritiesAvailable=alaDcbxPfcUsagePrioritiesAvailable, alcatelIND1DcbxMIBObjects=alcatelIND1DcbxMIBObjects, alaDcbxDCPTemplateDCPId=alaDcbxDCPTemplateDCPId, alaDcbxPfcLLPrioritiesReserved=alaDcbxPfcLLPrioritiesReserved, alaDcbxDCPTCEntry=alaDcbxDCPTCEntry, alaDcbxDCPPFCCap=alaDcbxDCPPFCCap, alaDcbxDCPTCsPresent=alaDcbxDCPTCsPresent, alaDcbxPfcUsageTable=alaDcbxPfcUsageTable, alaDcbxPIPFCStatsClear=alaDcbxPIPFCStatsClear, alaDcbxDCPTCDCPId=alaDcbxDCPTCDCPId, alaDcbxDCPTCPFCTrafficFlow=alaDcbxDCPTCPFCTrafficFlow, alaDcbxPfcUsageChassisId=alaDcbxPfcUsageChassisId, alaDcbxDCPId=alaDcbxDCPId, alaDcbxPfcUsageNewGroup=alaDcbxPfcUsageNewGroup, alaDcbxDCPTCTrafficClass=alaDcbxDCPTCTrafficClass, alaDcbxDCPTCPFCLinkDelay=alaDcbxDCPTCPFCLinkDelay, alaDcbxConformance=alaDcbxConformance, alaXdot1dcbxAdminApplicationPriorityAppRowStatus=alaXdot1dcbxAdminApplicationPriorityAppRowStatus, DcbxStatus=DcbxStatus, alaDcbxPIDCBXRemoteOperVersion=alaDcbxPIDCBXRemoteOperVersion, DcbxTCsPresent=DcbxTCsPresent, alaDcbxPIPrioTC=alaDcbxPIPrioTC, alaDcbxDCPTCPriorityMap=alaDcbxDCPTCPriorityMap, alaDcbxDCPTCTrafficScheduler=alaDcbxDCPTCTrafficScheduler, alaDcbxPIDCBXOperVersion=alaDcbxPIDCBXOperVersion, alaDcbxDCP8023xPauseReady=alaDcbxDCP8023xPauseReady, alaDcbxDCPTCMinimumBandwidth=alaDcbxDCPTCMinimumBandwidth, alaDcbxDCPTrafficClassTable=alaDcbxDCPTrafficClassTable, alaDcbxPfcUsagePrioritiesReserved=alaDcbxPfcUsagePrioritiesReserved, alaXdot1dcbxAdminApplicationPriorityAEPriority=alaXdot1dcbxAdminApplicationPriorityAEPriority, alaDcbxPIPrioPFCPacketsReceived=alaDcbxPIPrioPFCPacketsReceived, alaXdot1dcbxAdminApplicationPriorityAppTable=alaXdot1dcbxAdminApplicationPriorityAppTable, alaDcbxPIPrioEntry=alaDcbxPIPrioEntry, alaDcbxDCPTemplateDCPName=alaDcbxDCPTemplateDCPName, alaDcbxPfcUsageEntry=alaDcbxPfcUsageEntry, alaDcbxPILocalModified=alaDcbxPILocalModified, alaDcbxPIDCBXVersion=alaDcbxPIDCBXVersion, alaDcbxDCProfileGroup=alaDcbxDCProfileGroup, alcatelIND1DcbxMIB=alcatelIND1DcbxMIB, DcbxActionTaken=DcbxActionTaken, alaDcbxDCProfileEntry=alaDcbxDCProfileEntry, alaDcbxPIDCBXAdmin=alaDcbxPIDCBXAdmin, alaDcbxDCPETSTrafficClassesSupported=alaDcbxDCPETSTrafficClassesSupported, DcbxVersion=DcbxVersion, alaDcbxPIPrioPriority=alaDcbxPIPrioPriority, alaDcbxPIPFCDefense=alaDcbxPIPFCDefense, alaDcbxPIPriorityTable=alaDcbxPIPriorityTable, alaDcbxPIAdminDCPId=alaDcbxPIAdminDCPId, alaXdot1dcbxAdminApplicationPriorityAppEntry=alaXdot1dcbxAdminApplicationPriorityAppEntry, alaDcbxPIPrioIfIndex=alaDcbxPIPrioIfIndex, alaDcbxDCPTCMaximumBandwidth=alaDcbxDCPTCMaximumBandwidth, alaDcbxDCPPriorityTCMap=alaDcbxDCPPriorityTCMap, alaDcbxPIActionTaken=alaDcbxPIActionTaken, alaDcbxPIAdminDCPName=alaDcbxPIAdminDCPName, alaDcbxPortInstanceEntry=alaDcbxPortInstanceEntry, alaDcbxDCPName=alaDcbxDCPName, alaDcbxDCPTCPFCLinkDelayUserModified=alaDcbxDCPTCPFCLinkDelayUserModified, alaDcbxDCPTCDCPName=alaDcbxDCPTCDCPName, alaDcbxPIRowStatus=alaDcbxPIRowStatus, alaDcbxDCProfileTable=alaDcbxDCProfileTable, alaDcbxPfcLLPrioritiesAvailable=alaDcbxPfcLLPrioritiesAvailable)
