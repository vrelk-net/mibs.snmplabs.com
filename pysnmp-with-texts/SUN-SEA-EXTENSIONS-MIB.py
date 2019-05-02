#
# PySNMP MIB module SUN-SEA-EXTENSIONS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SUN-SEA-EXTENSIONS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:12:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, mgmt, IpAddress, enterprises, Gauge32, Counter32, Integer32, Unsigned32, Bits, ObjectIdentity, MibIdentifier, ModuleIdentity, iso, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "mgmt", "IpAddress", "enterprises", "Gauge32", "Counter32", "Integer32", "Unsigned32", "Bits", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "iso", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sunMIB, = mibBuilder.importSymbols("SUN-MIB", "sunMIB")
sunSeaExtensionsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 42, 3))
if mibBuilder.loadTexts: sunSeaExtensionsMIB.setLastUpdated('200309180000Z')
if mibBuilder.loadTexts: sunSeaExtensionsMIB.setOrganization('Sun Microsystems, Inc.')
if mibBuilder.loadTexts: sunSeaExtensionsMIB.setContactInfo('Customer support')
if mibBuilder.loadTexts: sunSeaExtensionsMIB.setDescription('The MIB that describes the sun-specific extensions to mib-2 ')
sunSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 3, 1))
sunInterfaces = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 3, 2))
sunAt = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 3, 3))
sunIp = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 3, 4))
sunIcmp = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 3, 5))
sunTcp = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 3, 6))
sunUdp = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 3, 7))
sunSnmp = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 3, 11))
sunProcesses = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 3, 12))
sunHostPerf = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 3, 13))
agentDescr = MibScalar((1, 3, 6, 1, 4, 1, 42, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentDescr.setStatus('mandatory')
if mibBuilder.loadTexts: agentDescr.setDescription("The SNMP agent's description of itself.")
hostID = MibScalar((1, 3, 6, 1, 4, 1, 42, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostID.setStatus('mandatory')
if mibBuilder.loadTexts: hostID.setDescription('The unique Sun hardware identifier. The value returned is four byte binary string.')
motd = MibScalar((1, 3, 6, 1, 4, 1, 42, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: motd.setStatus('mandatory')
if mibBuilder.loadTexts: motd.setDescription('The first line of /etc/motd.')
unixTime = MibScalar((1, 3, 6, 1, 4, 1, 42, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: unixTime.setStatus('mandatory')
if mibBuilder.loadTexts: unixTime.setDescription('The Unix system time. Measured in seconds since January 1, 1970 GMT.')
sunProcessTable = MibTable((1, 3, 6, 1, 4, 1, 42, 3, 12, 1), ).setMaxAccess("readonly")
if mibBuilder.loadTexts: sunProcessTable.setStatus('mandatory')
psEntry = MibTableRow((1, 3, 6, 1, 4, 1, 42, 3, 12, 1, 1), ).setMaxAccess("readonly").setIndexNames((0, "SUN-SEA-EXTENSIONS-MIB", "psProcessID"))
if mibBuilder.loadTexts: psEntry.setStatus('mandatory')
psProcessID = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 3, 12, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psProcessID.setStatus('mandatory')
if mibBuilder.loadTexts: psProcessID.setDescription('The process identifier for this process.')
psParentProcessID = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 3, 12, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psParentProcessID.setStatus('mandatory')
if mibBuilder.loadTexts: psParentProcessID.setDescription("The process identifier of this process's parent.")
psProcessSize = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 3, 12, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psProcessSize.setStatus('mandatory')
if mibBuilder.loadTexts: psProcessSize.setDescription('The combined size of the data and stack segments (in kilobytes.)')
psProcessCpuTime = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 3, 12, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psProcessCpuTime.setStatus('mandatory')
if mibBuilder.loadTexts: psProcessCpuTime.setDescription('The CPU time (including both user and system time) consumed so far.')
psProcessState = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 3, 12, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psProcessState.setStatus('mandatory')
if mibBuilder.loadTexts: psProcessState.setDescription('The run-state of the process. R - Runnable T - Stopped P - In page wait D - Non-interruptable wait S - Sleeping (less than 20 seconds) I - Idle (more than 20 seconds) Z - Zombie')
psProcessWaitChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 3, 12, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psProcessWaitChannel.setStatus('mandatory')
if mibBuilder.loadTexts: psProcessWaitChannel.setDescription('Reason process is waiting.')
psProcessTTY = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 3, 12, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psProcessTTY.setStatus('mandatory')
if mibBuilder.loadTexts: psProcessTTY.setDescription('Terminal, if any, controlling this process.')
psProcessUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 3, 12, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psProcessUserName.setStatus('mandatory')
if mibBuilder.loadTexts: psProcessUserName.setDescription('Name of the user associated with this process.')
psProcessUserID = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 3, 12, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psProcessUserID.setStatus('mandatory')
if mibBuilder.loadTexts: psProcessUserID.setDescription('Numeric form of the name of the user associated with this process.')
psProcessName = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 3, 12, 1, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psProcessName.setStatus('mandatory')
if mibBuilder.loadTexts: psProcessName.setDescription('Command name used to invoke this process.')
psProcessStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 3, 12, 1, 1, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: psProcessStatus.setStatus('mandatory')
if mibBuilder.loadTexts: psProcessStatus.setDescription('Setting this variable will cause a signal of the set value to be sent to the process.')
rsUserProcessTime = MibScalar((1, 3, 6, 1, 4, 1, 42, 3, 13, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsUserProcessTime.setStatus('mandatory')
if mibBuilder.loadTexts: rsUserProcessTime.setDescription('total number of timeticks used by user processes since the system was last booted.')
rsNiceModeTime = MibScalar((1, 3, 6, 1, 4, 1, 42, 3, 13, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsNiceModeTime.setStatus('mandatory')
if mibBuilder.loadTexts: rsNiceModeTime.setDescription('total number of timeticks used by nice mode since the system was last booted.')
rsSystemProcessTime = MibScalar((1, 3, 6, 1, 4, 1, 42, 3, 13, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsSystemProcessTime.setStatus('mandatory')
if mibBuilder.loadTexts: rsSystemProcessTime.setDescription('total number of timeticks used by system processes since the system was last booted.')
rsIdleModeTime = MibScalar((1, 3, 6, 1, 4, 1, 42, 3, 13, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIdleModeTime.setStatus('mandatory')
if mibBuilder.loadTexts: rsIdleModeTime.setDescription('total number of timeticks used in idle mode since the system was last booted.')
rsDiskXfer1 = MibScalar((1, 3, 6, 1, 4, 1, 42, 3, 13, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsDiskXfer1.setStatus('mandatory')
if mibBuilder.loadTexts: rsDiskXfer1.setDescription('')
rsDiskXfer2 = MibScalar((1, 3, 6, 1, 4, 1, 42, 3, 13, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsDiskXfer2.setStatus('mandatory')
if mibBuilder.loadTexts: rsDiskXfer2.setDescription('')
rsDiskXfer3 = MibScalar((1, 3, 6, 1, 4, 1, 42, 3, 13, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsDiskXfer3.setStatus('mandatory')
if mibBuilder.loadTexts: rsDiskXfer3.setDescription('')
rsDiskXfer4 = MibScalar((1, 3, 6, 1, 4, 1, 42, 3, 13, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsDiskXfer4.setStatus('mandatory')
if mibBuilder.loadTexts: rsDiskXfer4.setDescription('')
rsVPagesIn = MibScalar((1, 3, 6, 1, 4, 1, 42, 3, 13, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsVPagesIn.setStatus('mandatory')
if mibBuilder.loadTexts: rsVPagesIn.setDescription('Number of pages read in from disk.')
rsVPagesOut = MibScalar((1, 3, 6, 1, 4, 1, 42, 3, 13, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsVPagesOut.setStatus('mandatory')
if mibBuilder.loadTexts: rsVPagesOut.setDescription('Number of pages written to disk.')
rsVSwapIn = MibScalar((1, 3, 6, 1, 4, 1, 42, 3, 13, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsVSwapIn.setStatus('mandatory')
if mibBuilder.loadTexts: rsVSwapIn.setDescription('Number of pages swapped in.')
rsVSwapOut = MibScalar((1, 3, 6, 1, 4, 1, 42, 3, 13, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsVSwapOut.setStatus('mandatory')
if mibBuilder.loadTexts: rsVSwapOut.setDescription('Number of pages swapped out.')
rsVIntr = MibScalar((1, 3, 6, 1, 4, 1, 42, 3, 13, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsVIntr.setStatus('mandatory')
if mibBuilder.loadTexts: rsVIntr.setDescription('Number of device interrupts.')
rsIfInPackets = MibScalar((1, 3, 6, 1, 4, 1, 42, 3, 13, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIfInPackets.setStatus('mandatory')
if mibBuilder.loadTexts: rsIfInPackets.setDescription('Number of input packets.')
rsIfOutPackets = MibScalar((1, 3, 6, 1, 4, 1, 42, 3, 13, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIfOutPackets.setStatus('mandatory')
if mibBuilder.loadTexts: rsIfOutPackets.setDescription('Number of output packets.')
rsIfInErrors = MibScalar((1, 3, 6, 1, 4, 1, 42, 3, 13, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIfInErrors.setStatus('mandatory')
if mibBuilder.loadTexts: rsIfInErrors.setDescription('Number of input errors.')
rsIfOutErrors = MibScalar((1, 3, 6, 1, 4, 1, 42, 3, 13, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIfOutErrors.setStatus('mandatory')
if mibBuilder.loadTexts: rsIfOutErrors.setDescription('Number of output errors.')
rsIfCollisions = MibScalar((1, 3, 6, 1, 4, 1, 42, 3, 13, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIfCollisions.setStatus('mandatory')
if mibBuilder.loadTexts: rsIfCollisions.setDescription('Number of output collisions.')
mibBuilder.exportSymbols("SUN-SEA-EXTENSIONS-MIB", rsIdleModeTime=rsIdleModeTime, rsVIntr=rsVIntr, rsIfOutPackets=rsIfOutPackets, rsIfInErrors=rsIfInErrors, psProcessState=psProcessState, rsDiskXfer4=rsDiskXfer4, agentDescr=agentDescr, rsIfOutErrors=rsIfOutErrors, sunSeaExtensionsMIB=sunSeaExtensionsMIB, hostID=hostID, rsDiskXfer3=rsDiskXfer3, psProcessID=psProcessID, sunIp=sunIp, psProcessUserID=psProcessUserID, rsIfInPackets=rsIfInPackets, rsUserProcessTime=rsUserProcessTime, motd=motd, rsVSwapOut=rsVSwapOut, sunUdp=sunUdp, rsSystemProcessTime=rsSystemProcessTime, rsVPagesIn=rsVPagesIn, sunInterfaces=sunInterfaces, sunIcmp=sunIcmp, sunHostPerf=sunHostPerf, psProcessTTY=psProcessTTY, psProcessName=psProcessName, psProcessStatus=psProcessStatus, rsIfCollisions=rsIfCollisions, rsDiskXfer1=rsDiskXfer1, sunTcp=sunTcp, rsVSwapIn=rsVSwapIn, psParentProcessID=psParentProcessID, psProcessUserName=psProcessUserName, rsNiceModeTime=rsNiceModeTime, sunProcessTable=sunProcessTable, psProcessCpuTime=psProcessCpuTime, psProcessWaitChannel=psProcessWaitChannel, psEntry=psEntry, sunProcesses=sunProcesses, sunSnmp=sunSnmp, psProcessSize=psProcessSize, sunAt=sunAt, rsVPagesOut=rsVPagesOut, PYSNMP_MODULE_ID=sunSeaExtensionsMIB, sunSystem=sunSystem, unixTime=unixTime, rsDiskXfer2=rsDiskXfer2)