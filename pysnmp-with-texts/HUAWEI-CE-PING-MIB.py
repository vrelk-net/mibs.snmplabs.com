#
# PySNMP MIB module HUAWEI-CE-PING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-CE-PING-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:43:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, MibIdentifier, Integer32, Bits, mib_2, Counter32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Gauge32, IpAddress, Unsigned32, NotificationType, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibIdentifier", "Integer32", "Bits", "mib-2", "Counter32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Gauge32", "IpAddress", "Unsigned32", "NotificationType", "TimeTicks", "iso")
TextualConvention, RowStatus, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "MacAddress", "DisplayString")
hwCePing = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 175))
if mibBuilder.loadTexts: hwCePing.setLastUpdated('200810161855Z')
if mibBuilder.loadTexts: hwCePing.setOrganization('Huawei Technologies Co., Ltd.')
if mibBuilder.loadTexts: hwCePing.setContactInfo('R&D BeiJing, Huawei Technologies co.,Ltd. Huawei Bld.,NO.3 Xinxi Rd., Shang-Di Information Industry Base, Hai-Dian District Beijing P.R. China Zip:100085 Http://www.huawei.com E-mail:support@huawei.com')
if mibBuilder.loadTexts: hwCePing.setDescription('HUAWEI VPLS quality detect funcion.')
hwCePingTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 175, 1), )
if mibBuilder.loadTexts: hwCePingTable.setStatus('current')
if mibBuilder.loadTexts: hwCePingTable.setDescription('The table of Ce Ping.')
hwCePingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 175, 1, 1), ).setIndexNames((0, "HUAWEI-CE-PING-MIB", "hwCePingIndex"))
if mibBuilder.loadTexts: hwCePingEntry.setStatus('current')
if mibBuilder.loadTexts: hwCePingEntry.setDescription('The entry of hwCePingTable.')
hwCePingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 175, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: hwCePingIndex.setStatus('current')
if mibBuilder.loadTexts: hwCePingIndex.setDescription('The index of hwCePingTable,it is always 1.')
hwCePingTargetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 175, 1, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwCePingTargetAddress.setStatus('current')
if mibBuilder.loadTexts: hwCePingTargetAddress.setDescription('Specifies the IP address to be used as the destination.')
hwCePingSourceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 175, 1, 1, 3), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwCePingSourceAddress.setStatus('current')
if mibBuilder.loadTexts: hwCePingSourceAddress.setDescription('Specify an unused IP address in the same network that is associated with the VPLS.')
hwCePingVsiName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 175, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwCePingVsiName.setStatus('current')
if mibBuilder.loadTexts: hwCePingVsiName.setDescription('The VSI name that is uesd by the operation.')
hwCePingInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 175, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwCePingInterval.setStatus('current')
if mibBuilder.loadTexts: hwCePingInterval.setDescription('This value represents the inter-packet delay between packets and is in seconds.')
hwCePingCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 175, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwCePingCount.setStatus('current')
if mibBuilder.loadTexts: hwCePingCount.setDescription('This value represents the number of packets that need to be transmitted.')
hwCePingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 175, 1, 1, 51), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwCePingRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwCePingRowStatus.setDescription('The operating state of the row.')
hwCePingResultTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 175, 2), )
if mibBuilder.loadTexts: hwCePingResultTable.setStatus('current')
if mibBuilder.loadTexts: hwCePingResultTable.setDescription('The table of CE Ping result.')
hwCePingResultEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 175, 2, 1), ).setIndexNames((0, "HUAWEI-CE-PING-MIB", "hwCePingIndex"))
if mibBuilder.loadTexts: hwCePingResultEntry.setStatus('current')
if mibBuilder.loadTexts: hwCePingResultEntry.setDescription('The entry of hwCePingResultTable.')
hwCePingResultOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 175, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("sucessful", 1), ("inProcess", 2), ("timeout", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwCePingResultOperStatus.setStatus('current')
if mibBuilder.loadTexts: hwCePingResultOperStatus.setDescription('Reflects the operational state of a hwCePingEntry: sucessful(1) - Test is sucessful. inProcess(2) - Test is in process. timeout(3) - Test is timeout.')
hwCePingResultMac = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 175, 2, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwCePingResultMac.setStatus('current')
if mibBuilder.loadTexts: hwCePingResultMac.setDescription('The Mac that is detected by the test.')
hwCePingGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 175, 3))
hwCePingCtrlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 175, 3, 1)).setObjects(("HUAWEI-CE-PING-MIB", "hwCePingTargetAddress"), ("HUAWEI-CE-PING-MIB", "hwCePingSourceAddress"), ("HUAWEI-CE-PING-MIB", "hwCePingVsiName"), ("HUAWEI-CE-PING-MIB", "hwCePingInterval"), ("HUAWEI-CE-PING-MIB", "hwCePingCount"), ("HUAWEI-CE-PING-MIB", "hwCePingRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwCePingCtrlGroup = hwCePingCtrlGroup.setStatus('current')
if mibBuilder.loadTexts: hwCePingCtrlGroup.setDescription('Description.')
hwCePingResultGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 175, 3, 2)).setObjects(("HUAWEI-CE-PING-MIB", "hwCePingResultOperStatus"), ("HUAWEI-CE-PING-MIB", "hwCePingResultMac"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwCePingResultGroup = hwCePingResultGroup.setStatus('current')
if mibBuilder.loadTexts: hwCePingResultGroup.setDescription('Description.')
mibBuilder.exportSymbols("HUAWEI-CE-PING-MIB", hwCePingGroup=hwCePingGroup, hwCePingIndex=hwCePingIndex, hwCePingResultGroup=hwCePingResultGroup, PYSNMP_MODULE_ID=hwCePing, hwCePingRowStatus=hwCePingRowStatus, hwCePingCount=hwCePingCount, hwCePingResultMac=hwCePingResultMac, hwCePingSourceAddress=hwCePingSourceAddress, hwCePing=hwCePing, hwCePingTable=hwCePingTable, hwCePingResultOperStatus=hwCePingResultOperStatus, hwCePingTargetAddress=hwCePingTargetAddress, hwCePingEntry=hwCePingEntry, hwCePingResultTable=hwCePingResultTable, hwCePingInterval=hwCePingInterval, hwCePingResultEntry=hwCePingResultEntry, hwCePingCtrlGroup=hwCePingCtrlGroup, hwCePingVsiName=hwCePingVsiName)