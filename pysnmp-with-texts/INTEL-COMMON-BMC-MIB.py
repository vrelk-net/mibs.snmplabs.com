#
# PySNMP MIB module INTEL-COMMON-BMC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/INTEL-COMMON-BMC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:54:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, TimeTicks, ModuleIdentity, NotificationType, Counter64, NotificationType, MibIdentifier, Gauge32, enterprises, Bits, Integer32, IpAddress, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "TimeTicks", "ModuleIdentity", "NotificationType", "Counter64", "NotificationType", "MibIdentifier", "Gauge32", "enterprises", "Bits", "Integer32", "IpAddress", "iso", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
wired_for_management = MibIdentifier((1, 3, 6, 1, 4, 1, 3183)).setLabel("wired-for-management")
pet = MibIdentifier((1, 3, 6, 1, 4, 1, 3183, 1))
pet_events = MibIdentifier((1, 3, 6, 1, 4, 1, 3183, 1, 1)).setLabel("pet-events")
tempUpperNonCriticalGoingHigh = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,65799))
if mibBuilder.loadTexts: tempUpperNonCriticalGoingHigh.setDescription('Temperature sensor crossed upper non-critical threshold, going high.')
tempUpperCriticalGoingHigh = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,65801))
if mibBuilder.loadTexts: tempUpperCriticalGoingHigh.setDescription('Temperature sensor crossed upper critical threshold, going high.')
voltageLowerNonCriticalGoingLow = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,131328))
if mibBuilder.loadTexts: voltageLowerNonCriticalGoingLow.setDescription('Voltage sensor crossed lower non-critical threshold, going low.')
voltageLowerCriticalGoingLow = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,131330))
if mibBuilder.loadTexts: voltageLowerCriticalGoingLow.setDescription('Voltage sensor crossed lower critical threshold, going low.')
voltageUpperNonCriticalGoingHigh = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,131335))
if mibBuilder.loadTexts: voltageUpperNonCriticalGoingHigh.setDescription('Voltage sensor crossed upper non-critical threshold, going high.')
voltageUpperCriticalGoingHigh = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,131337))
if mibBuilder.loadTexts: voltageUpperCriticalGoingHigh.setDescription('Voltage sensor crossed upper critical threshold, going high.')
fanFailureLowerNonCriticalGoingLow = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,262400))
if mibBuilder.loadTexts: fanFailureLowerNonCriticalGoingLow.setDescription('Fan sensor crossed lower non-critical threshold, going low.')
fanFailureLowerCriticalGoingLow = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,262402))
if mibBuilder.loadTexts: fanFailureLowerCriticalGoingLow.setDescription('Fan sensor crossed lower critical threshold, going low.')
chassisIntrusionEvent = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,356096))
if mibBuilder.loadTexts: chassisIntrusionEvent.setDescription('A Chassis Intrusion assertion event.')
chassisIntrusionEventLANLeashLost = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,356100))
if mibBuilder.loadTexts: chassisIntrusionEventLANLeashLost.setDescription('A Chassis Intrusion LAN leash lost assertion event.')
powerSupplyPresence = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,552704))
if mibBuilder.loadTexts: powerSupplyPresence.setDescription('Power supply presence event.')
powerSupplyFailure = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,552705))
if mibBuilder.loadTexts: powerSupplyFailure.setDescription('Power supply failure event.')
powerSupplyPredictiveFailure = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,552706))
if mibBuilder.loadTexts: powerSupplyPredictiveFailure.setDescription('Power supply predictive failure asserted event.')
powerSupplyACLost = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,552707))
if mibBuilder.loadTexts: powerSupplyACLost.setDescription('Power supply A/C lost event.')
powerSupplyConfigurationError = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,552710))
if mibBuilder.loadTexts: powerSupplyConfigurationError.setDescription('Power supply configuration error event.')
uncorrectableECCError = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,814849))
if mibBuilder.loadTexts: uncorrectableECCError.setDescription('Uncorrectable ECC error event.')
postError = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,1011456))
if mibBuilder.loadTexts: postError.setDescription('Power On Self Test (POST) error event.')
thermalTripError = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,487169))
if mibBuilder.loadTexts: thermalTripError.setDescription('Thermal Trip error event.')
cpuPresence = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,487175))
if mibBuilder.loadTexts: cpuPresence.setDescription('Processor Presence')
procDisabledError = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,459521))
if mibBuilder.loadTexts: procDisabledError.setDescription('CATERR Event Detected.')
fatalNMIError = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,1273600))
if mibBuilder.loadTexts: fatalNMIError.setDescription('Front Panel NMI Assertion event.')
timerExpired = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,2322176))
if mibBuilder.loadTexts: timerExpired.setDescription('Timer expired event.')
hardReset = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,2322177))
if mibBuilder.loadTexts: hardReset.setDescription('Hard reset event.')
powerDown = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,2322178))
if mibBuilder.loadTexts: powerDown.setDescription('Power down event.')
powerReset = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,2322179))
if mibBuilder.loadTexts: powerReset.setDescription('Power Reset event')
timerInterrupt = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,2322184))
if mibBuilder.loadTexts: timerInterrupt.setDescription('Timer Interrupt event.')
oemSystemBootEvent = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,1208065))
if mibBuilder.loadTexts: oemSystemBootEvent.setDescription('OEM System Boot event.')
selLogAreaReset = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,1076994))
if mibBuilder.loadTexts: selLogAreaReset.setDescription('Log area reset / cleared')
smiTimeoutError = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,258817))
if mibBuilder.loadTexts: smiTimeoutError.setDescription('SMI Timeout Assertion event.')
drivePresence = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,880384))
if mibBuilder.loadTexts: drivePresence.setDescription('Drive Presence event.')
driveFault = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,880385))
if mibBuilder.loadTexts: driveFault.setDescription('Drive Fault event.')
drivePredictiveFailure = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,880386))
if mibBuilder.loadTexts: drivePredictiveFailure.setDescription('Drive Predictive Failure event.')
driveRebuild = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,880391))
if mibBuilder.loadTexts: driveRebuild.setDescription('Drive Rebuild event.')
powerOffPowerUnit = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,618240))
if mibBuilder.loadTexts: powerOffPowerUnit.setDescription('Power Unit Power Off event.')
acLostPowerUnit = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,618244))
if mibBuilder.loadTexts: acLostPowerUnit.setDescription('Power Unit AC Lost event.')
softPowerControlPowerUnit = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,618245))
if mibBuilder.loadTexts: softPowerControlPowerUnit.setDescription('Power Unit Soft Power Control Failure event.')
powerUnitFailure = NotificationType((1, 3, 6, 1, 4, 1, 3183, 1, 1) + (0,618246))
if mibBuilder.loadTexts: powerUnitFailure.setDescription('Power Unit Failure event.')
mibBuilder.exportSymbols("INTEL-COMMON-BMC-MIB", powerDown=powerDown, timerInterrupt=timerInterrupt, voltageLowerNonCriticalGoingLow=voltageLowerNonCriticalGoingLow, powerOffPowerUnit=powerOffPowerUnit, postError=postError, thermalTripError=thermalTripError, selLogAreaReset=selLogAreaReset, procDisabledError=procDisabledError, oemSystemBootEvent=oemSystemBootEvent, voltageLowerCriticalGoingLow=voltageLowerCriticalGoingLow, chassisIntrusionEventLANLeashLost=chassisIntrusionEventLANLeashLost, fanFailureLowerNonCriticalGoingLow=fanFailureLowerNonCriticalGoingLow, pet_events=pet_events, chassisIntrusionEvent=chassisIntrusionEvent, smiTimeoutError=smiTimeoutError, powerSupplyPredictiveFailure=powerSupplyPredictiveFailure, fatalNMIError=fatalNMIError, voltageUpperCriticalGoingHigh=voltageUpperCriticalGoingHigh, powerSupplyACLost=powerSupplyACLost, wired_for_management=wired_for_management, pet=pet, powerSupplyConfigurationError=powerSupplyConfigurationError, driveFault=driveFault, fanFailureLowerCriticalGoingLow=fanFailureLowerCriticalGoingLow, drivePredictiveFailure=drivePredictiveFailure, cpuPresence=cpuPresence, driveRebuild=driveRebuild, acLostPowerUnit=acLostPowerUnit, powerUnitFailure=powerUnitFailure, timerExpired=timerExpired, powerSupplyFailure=powerSupplyFailure, powerReset=powerReset, softPowerControlPowerUnit=softPowerControlPowerUnit, tempUpperNonCriticalGoingHigh=tempUpperNonCriticalGoingHigh, hardReset=hardReset, drivePresence=drivePresence, powerSupplyPresence=powerSupplyPresence, uncorrectableECCError=uncorrectableECCError, tempUpperCriticalGoingHigh=tempUpperCriticalGoingHigh, voltageUpperNonCriticalGoingHigh=voltageUpperNonCriticalGoingHigh)