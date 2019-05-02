#
# PySNMP MIB module NMS-EPON-LLID (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NMS-EPON-LLID
# Produced by pysmi-0.3.4 at Wed May  1 14:21:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
nmsEPONGroup, = mibBuilder.importSymbols("NMS-SMI", "nmsEPONGroup")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, iso, IpAddress, Bits, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, NotificationType, MibIdentifier, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "IpAddress", "Bits", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "NotificationType", "MibIdentifier", "Counter32", "ModuleIdentity")
RowStatus, TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString", "TruthValue")
nmsEponLlid = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9))
nmseponllidTable = MibTable((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1), )
if mibBuilder.loadTexts: nmseponllidTable.setStatus('mandatory')
if mibBuilder.loadTexts: nmseponllidTable.setDescription('A list of epon ONU and LLID table entries.')
nmsEponLlidEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1), ).setIndexNames((0, "NMS-EPON-LLID", "llidIfIndex"))
if mibBuilder.loadTexts: nmsEponLlidEntry.setStatus('mandatory')
if mibBuilder.loadTexts: nmsEponLlidEntry.setDescription('A collection of additional objects in the epon ONU and LLID table.')
llidIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llidIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: llidIfIndex.setDescription('LLID interface id, unique in system.')
llidToEponPortDiid = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llidToEponPortDiid.setStatus('mandatory')
if mibBuilder.loadTexts: llidToEponPortDiid.setDescription('EPON port DIID that LLID belongs to.')
llidsequenceNo = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llidsequenceNo.setStatus('mandatory')
if mibBuilder.loadTexts: llidsequenceNo.setDescription('LLID squence number,unique in system.')
llidEncrypStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llidEncrypStatus.setStatus('mandatory')
if mibBuilder.loadTexts: llidEncrypStatus.setDescription('LLID encryption status.')
llidCtcOamExtStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llidCtcOamExtStatus.setStatus('mandatory')
if mibBuilder.loadTexts: llidCtcOamExtStatus.setDescription('CTC OAM version negotiation resultCTC OAM extended status.')
llidCtcOamExtOui = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llidCtcOamExtOui.setStatus('mandatory')
if mibBuilder.loadTexts: llidCtcOamExtOui.setDescription('CTC OAM version negotiation resultCTC OAM extended OUI.')
llidCtcOamExtVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llidCtcOamExtVersion.setStatus('mandatory')
if mibBuilder.loadTexts: llidCtcOamExtVersion.setDescription('CTC OAM version negotiation resultCTC OAM extended version.')
llidIfPIR = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llidIfPIR.setStatus('mandatory')
if mibBuilder.loadTexts: llidIfPIR.setDescription('LLID port peak bandwidth.Notes:dba mode=1,2(12144/cycle-size(ms) to MIN(1000000,1000000/cycle-size(ms) ), dba mode =3,4(512 to1000000).')
llidIfCIR = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 955000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llidIfCIR.setStatus('mandatory')
if mibBuilder.loadTexts: llidIfCIR.setDescription('LLID port assurance bandwidth. Note:CIR<=PIR.')
llidIfFIR = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 955000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llidIfFIR.setStatus('mandatory')
if mibBuilder.loadTexts: llidIfFIR.setDescription('LLID port fixed bandwidth. Note:FIR<=CIR.')
llidIfConfigRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: llidIfConfigRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: llidIfConfigRowStatus.setDescription('LLID port configuration row status.')
llidIfDynamicMacLearningStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llidIfDynamicMacLearningStatus.setStatus('mandatory')
if mibBuilder.loadTexts: llidIfDynamicMacLearningStatus.setDescription('LLID port dynamic MAC address learning status.')
llidIfDynamicMacLearningLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 13), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llidIfDynamicMacLearningLimit.setStatus('mandatory')
if mibBuilder.loadTexts: llidIfDynamicMacLearningLimit.setDescription('LLID port dynamic MAC address learning limition.')
llidIfDynamicMacLearningNumberLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1023))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llidIfDynamicMacLearningNumberLimit.setStatus('mandatory')
if mibBuilder.loadTexts: llidIfDynamicMacLearningNumberLimit.setDescription('LLID port dynamic MAC address learning number limition.')
llidIfQosPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 15), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llidIfQosPolicy.setStatus('mandatory')
if mibBuilder.loadTexts: llidIfQosPolicy.setDescription('LLID interface qos policy name.')
llidIfACL = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 16), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llidIfACL.setStatus('mandatory')
if mibBuilder.loadTexts: llidIfACL.setDescription('LLID interface ACL.')
llidDownStreamPir = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llidDownStreamPir.setStatus('mandatory')
if mibBuilder.loadTexts: llidDownStreamPir.setDescription('LLID port down-stream peak bandwidth. Notes:dba mode=1,2(12144/cycle-size(ms) to MIN(1000000,1000000/cycle-size(ms) ), dba mode =3,4(512 to1000000).')
llidDownStreamCir = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 955000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llidDownStreamCir.setStatus('mandatory')
if mibBuilder.loadTexts: llidDownStreamCir.setDescription('LLID port down-stream assurance bandwidth. Note:CIR<=PIR.')
llidDownStreamFir = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 955000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llidDownStreamFir.setStatus('mandatory')
if mibBuilder.loadTexts: llidDownStreamFir.setDescription('LLID port down-stream fixed bandwidth. Note:FIR<=CIR.')
llidDownStreamIfRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 9, 1, 1, 20), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: llidDownStreamIfRowstatus.setStatus('mandatory')
if mibBuilder.loadTexts: llidDownStreamIfRowstatus.setDescription('LLID port down-stream configuration row status.That effects to llidDownStreamPir, llidDownStreamCir, llidDownStreamFir.')
mibBuilder.exportSymbols("NMS-EPON-LLID", llidIfDynamicMacLearningStatus=llidIfDynamicMacLearningStatus, llidsequenceNo=llidsequenceNo, nmseponllidTable=nmseponllidTable, nmsEponLlidEntry=nmsEponLlidEntry, llidIfConfigRowStatus=llidIfConfigRowStatus, llidCtcOamExtOui=llidCtcOamExtOui, llidDownStreamPir=llidDownStreamPir, llidIfDynamicMacLearningLimit=llidIfDynamicMacLearningLimit, llidIfQosPolicy=llidIfQosPolicy, llidCtcOamExtVersion=llidCtcOamExtVersion, llidIfPIR=llidIfPIR, llidEncrypStatus=llidEncrypStatus, llidIfACL=llidIfACL, llidIfCIR=llidIfCIR, nmsEponLlid=nmsEponLlid, llidDownStreamCir=llidDownStreamCir, llidIfDynamicMacLearningNumberLimit=llidIfDynamicMacLearningNumberLimit, llidDownStreamIfRowstatus=llidDownStreamIfRowstatus, llidIfIndex=llidIfIndex, llidCtcOamExtStatus=llidCtcOamExtStatus, llidIfFIR=llidIfFIR, llidToEponPortDiid=llidToEponPortDiid, llidDownStreamFir=llidDownStreamFir)