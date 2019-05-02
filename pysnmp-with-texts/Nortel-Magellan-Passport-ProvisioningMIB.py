#
# PySNMP MIB module Nortel-Magellan-Passport-ProvisioningMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-Magellan-Passport-ProvisioningMIB
# Produced by pysmi-0.3.4 at Wed May  1 14:28:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
RowPointer, RowStatus, Unsigned32, DisplayString, StorageType = mibBuilder.importSymbols("Nortel-Magellan-Passport-StandardTextualConventionsMIB", "RowPointer", "RowStatus", "Unsigned32", "DisplayString", "StorageType")
EnterpriseDateAndTime, NonReplicated, AsciiStringIndex, AsciiString = mibBuilder.importSymbols("Nortel-Magellan-Passport-TextualConventionsMIB", "EnterpriseDateAndTime", "NonReplicated", "AsciiStringIndex", "AsciiString")
passportMIBs, components = mibBuilder.importSymbols("Nortel-Magellan-Passport-UsefulDefinitionsMIB", "passportMIBs", "components")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Unsigned32, Integer32, ObjectIdentity, Counter64, MibIdentifier, Counter32, ModuleIdentity, IpAddress, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "Integer32", "ObjectIdentity", "Counter64", "MibIdentifier", "Counter32", "ModuleIdentity", "IpAddress", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
provisioningMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 19))
prov = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11))
provRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 1), )
if mibBuilder.loadTexts: provRowStatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: provRowStatusTable.setDescription('This entry controls the addition and deletion of prov components.')
provRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 1, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-ProvisioningMIB", "provIndex"))
if mibBuilder.loadTexts: provRowStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: provRowStatusEntry.setDescription('A single entry in the table represents a single prov component.')
provRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: provRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: provRowStatus.setDescription('This variable is used as the basis for SNMP naming of prov components. These components cannot be added nor deleted.')
provComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: provComponentName.setStatus('mandatory')
if mibBuilder.loadTexts: provComponentName.setDescription("This variable provides the component's string name for use with the ASCII Console Interface")
provStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: provStorageType.setStatus('mandatory')
if mibBuilder.loadTexts: provStorageType.setDescription('This variable represents the storage type value for the prov tables.')
provIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: provIndex.setStatus('mandatory')
if mibBuilder.loadTexts: provIndex.setDescription('This variable represents the index for the prov tables.')
provStateTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 10), )
if mibBuilder.loadTexts: provStateTable.setStatus('mandatory')
if mibBuilder.loadTexts: provStateTable.setDescription('This group contains the three OSI State attributes. The descriptions generically indicate what each state attribute implies about the component. Note that not all the values and state combinations described here are supported by every component which uses this group. For component-specific information and the valid state combinations, refer to NTP 241-7001-150, Passport Operations and Maintenance Guide.')
provStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 10, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-ProvisioningMIB", "provIndex"))
if mibBuilder.loadTexts: provStateEntry.setStatus('mandatory')
if mibBuilder.loadTexts: provStateEntry.setDescription('An entry in the provStateTable.')
provAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 10, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("locked", 0), ("unlocked", 1), ("shuttingDown", 2))).clone('unlocked')).setMaxAccess("readonly")
if mibBuilder.loadTexts: provAdminState.setStatus('mandatory')
if mibBuilder.loadTexts: provAdminState.setDescription('This attribute indicates the OSI Administrative State of the component. The value locked indicates that the component is administratively prohibited from providing services for its users. A Lock or Lock - force command has been previously issued for this component. When the value is locked, the value of usageState must be idle. The value shuttingDown indicates that the component is administratively permitted to provide service to its existing users only. A Lock command was issued against the component and it is in the process of shutting down. The value unlocked indicates that the component is administratively permitted to provide services for its users. To enter this state, issue an Unlock command to this component.')
provOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: provOperationalState.setStatus('mandatory')
if mibBuilder.loadTexts: provOperationalState.setDescription('This attribute indicates the OSI Operational State of the component. The value enabled indicates that the component is available for operation. Note that if adminState is locked, it would still not be providing service. The value disabled indicates that the component is not available for operation. For example, something is wrong with the component itself, or with another component on which this one depends. If the value is disabled, the usageState must be idle.')
provUsageState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 10, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("idle", 0), ("active", 1), ("busy", 2))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: provUsageState.setStatus('mandatory')
if mibBuilder.loadTexts: provUsageState.setDescription('This attribute indicates the OSI Usage State of the component. The value idle indicates that the component is not currently in use. The value active indicates that the component is in use and has spare capacity to provide for additional users. The value busy indicates that the component is in use and has no spare operating capacity for additional users at this time.')
provOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 11), )
if mibBuilder.loadTexts: provOperTable.setStatus('mandatory')
if mibBuilder.loadTexts: provOperTable.setDescription('This group contains the operational attributes for the ProvisioningSystem component.')
provOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 11, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-ProvisioningMIB", "provIndex"))
if mibBuilder.loadTexts: provOperEntry.setStatus('mandatory')
if mibBuilder.loadTexts: provOperEntry.setDescription('An entry in the provOperTable.')
provProvisioningActivity = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 11, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 21))).clone(namedValues=NamedValues(("initialLoading", 0), ("none", 2), ("activation", 3), ("initialActivation", 4), ("rollingBack", 5), ("saving", 6), ("loadingOrApplying", 7), ("semanticChecking", 8), ("waitingForConfirm", 9), ("clearing", 11), ("copying", 12), ("committing", 13), ("deleting", 14), ("confirming", 15), ("adding", 21)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: provProvisioningActivity.setStatus('mandatory')
if mibBuilder.loadTexts: provProvisioningActivity.setDescription('This attribute describes the type of provisioning activity that the ProvisioningSystem component is performing.')
provActivityProgress = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 11, 1, 2), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: provActivityProgress.setStatus('mandatory')
if mibBuilder.loadTexts: provActivityProgress.setDescription('This attribute indicates the status relating to a long-running command handled by the ProvisioningSystem. It is usually expressed as a percentage of the number of elements (for example, components) processed with respect to the total set of elements that need to be processed for that activity. Note that, one cannot assume that the percentage implies how much time the task may still take. The time to complete the activity is dependent on many things which are beyond the control of the ProvisioningSystem itself.')
provCommittedFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 11, 1, 3), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: provCommittedFileName.setStatus('mandatory')
if mibBuilder.loadTexts: provCommittedFileName.setDescription('This attribute contains the name of the committed file. This is the file that will be used to obtain the provisioning data if the module restarts. Immediately after system power-up, this attribute contains the name of the file used during initial loading.')
provCurrentViewFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 11, 1, 4), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: provCurrentViewFileName.setStatus('mandatory')
if mibBuilder.loadTexts: provCurrentViewFileName.setDescription('This attribute contains the name of the provisioning file that contains the current view provisioning data. After system power-up, this attribute contains the name of the file used during initial loading. If the current view data has not been saved, this attribute is empty.')
provLastUsedFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 11, 1, 5), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(1, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: provLastUsedFileName.setStatus('mandatory')
if mibBuilder.loadTexts: provLastUsedFileName.setDescription('This attribute contains the last saved, loaded or committed file name. Immediately after system power-up, this attribute contains the name of the file used during initial loading.')
provProvisioningSession = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 11, 1, 6), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: provProvisioningSession.setStatus('mandatory')
if mibBuilder.loadTexts: provProvisioningSession.setDescription('This attribute contains the component name of the operator session which is currently in provisioning mode. For example, NMIS Telnet Session/2 If no session is in provisioning mode, this attribute will be empty.')
provProvisioningUser = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 11, 1, 7), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: provProvisioningUser.setStatus('mandatory')
if mibBuilder.loadTexts: provProvisioningUser.setDescription('This attribute contains the userid of the operator who is currently provisioning the module. If no session is in provisioning mode, this attribute will be empty.')
provCheckRequired = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 11, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: provCheckRequired.setStatus('mandatory')
if mibBuilder.loadTexts: provCheckRequired.setDescription('This attribute indicates whether semantic checking is required before activating the edit view.')
provNextFileSequenceNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 11, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 999))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: provNextFileSequenceNumber.setStatus('obsolete')
if mibBuilder.loadTexts: provNextFileSequenceNumber.setDescription('This attribute is no longer supported.')
provConfirmRequired = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 11, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: provConfirmRequired.setStatus('mandatory')
if mibBuilder.loadTexts: provConfirmRequired.setDescription('This attribute indicates whether the operator must enter a Confirm Prov command in order to keep a newly activated current view in effect. If an activation is not confirmed within 20 minutes of its completion, the module will restart using the committed provisioning data.')
provProvisioningDirectory = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 11, 1, 11), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: provProvisioningDirectory.setStatus('obsolete')
if mibBuilder.loadTexts: provProvisioningDirectory.setDescription('This attribute indicates the name of the provisioning directory.')
provEditViewName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 11, 1, 12), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: provEditViewName.setStatus('mandatory')
if mibBuilder.loadTexts: provEditViewName.setDescription('This attribute indicates the name of the provisioning view that represents the edit view provisioning data. If the edit view data has not been saved, this attribute is empty.')
provEditViewAddedComponents = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 11, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: provEditViewAddedComponents.setStatus('mandatory')
if mibBuilder.loadTexts: provEditViewAddedComponents.setDescription('This attribute indicates the number of provisioning components that have been added to the edit view with respect to the current view.')
provEditViewDeletedComponents = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 11, 1, 14), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: provEditViewDeletedComponents.setStatus('mandatory')
if mibBuilder.loadTexts: provEditViewDeletedComponents.setDescription('This attribute indicates the number of provisioned components that have been deleted from the edit view with respect to the current view.')
provEditViewChangedComponents = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 11, 1, 15), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: provEditViewChangedComponents.setStatus('mandatory')
if mibBuilder.loadTexts: provEditViewChangedComponents.setDescription('This attribute indicates the number of provisioned components whose attributes differ between the edit and current views.')
provStandbyCpActivity = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 11, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 6))).clone(namedValues=NamedValues(("none", 0), ("loadingProvisioningData", 1), ("savingCommitFormatProvisioningData", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: provStandbyCpActivity.setStatus('mandatory')
if mibBuilder.loadTexts: provStandbyCpActivity.setDescription('This attribute descibes the type of provisionin activity, which ProvisioningSystem is performing on standby CP.')
provStandbyCpActivityProgress = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 11, 1, 17), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: provStandbyCpActivityProgress.setStatus('mandatory')
if mibBuilder.loadTexts: provStandbyCpActivityProgress.setDescription('This attribute indicates status of a provisioning activity, which ProvisioningSystem is performing on standby CP.')
provView = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 2))
provViewRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 2, 1), )
if mibBuilder.loadTexts: provViewRowStatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: provViewRowStatusTable.setDescription('*** THIS TABLE CURRENTLY NOT IMPLEMENTED *** This entry controls the addition and deletion of provView components.')
provViewRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 2, 1, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-ProvisioningMIB", "provIndex"), (0, "Nortel-Magellan-Passport-ProvisioningMIB", "provViewIndex"))
if mibBuilder.loadTexts: provViewRowStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: provViewRowStatusEntry.setDescription('A single entry in the table represents a single provView component.')
provViewRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 2, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: provViewRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: provViewRowStatus.setDescription('This variable is used as the basis for SNMP naming of provView components. These components cannot be added nor deleted.')
provViewComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: provViewComponentName.setStatus('mandatory')
if mibBuilder.loadTexts: provViewComponentName.setDescription("This variable provides the component's string name for use with the ASCII Console Interface")
provViewStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 2, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: provViewStorageType.setStatus('mandatory')
if mibBuilder.loadTexts: provViewStorageType.setDescription('This variable represents the storage type value for the provView tables.')
provViewIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 2, 1, 1, 10), AsciiStringIndex().subtype(subtypeSpec=ValueSizeConstraint(1, 40)))
if mibBuilder.loadTexts: provViewIndex.setStatus('mandatory')
if mibBuilder.loadTexts: provViewIndex.setDescription('This variable represents the index for the provView tables.')
provViewOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 2, 100), )
if mibBuilder.loadTexts: provViewOperTable.setStatus('mandatory')
if mibBuilder.loadTexts: provViewOperTable.setDescription('*** THIS TABLE CURRENTLY NOT IMPLEMENTED *** This group contains the operational attributes for the View component.')
provViewOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 2, 100, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-ProvisioningMIB", "provIndex"), (0, "Nortel-Magellan-Passport-ProvisioningMIB", "provViewIndex"))
if mibBuilder.loadTexts: provViewOperEntry.setStatus('mandatory')
if mibBuilder.loadTexts: provViewOperEntry.setDescription('An entry in the provViewOperTable.')
provViewUser = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 2, 100, 1, 1), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: provViewUser.setStatus('mandatory')
if mibBuilder.loadTexts: provViewUser.setDescription('This attribute indicates the userid of the operator who first saved this view. It may be empty if unknown or if the view has not been saved.')
provViewCheckState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 2, 100, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("failed", 0), ("unknown", 1), ("partial", 2), ("softwareChanged", 3), ("full", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: provViewCheckState.setStatus('mandatory')
if mibBuilder.loadTexts: provViewCheckState.setDescription('This attribute indicates the semantic check state of the view when it was saved. The values are described in worst to best order. The failed state indicates that the view has failed a semantic check and cannot be activated. The unknown state indicates that semantic checks have not been run and the view cannot be activated. The partial state indicates that the view has passed incomplete checks, that is Check -changed Prov has succeeded. This is also the best state value for a partial view. Thew view cannot be activated until it has been fully checked. The softwareChanged state indicates that the view has passed complete checks, but by software other than that to be activated, that is, either the application versions have changed, or features have been added. After activation, the new software may detect semantic errors. After correcting these errors, if any, the view will need to be re-saved or re-committed as appropriate. The full state indicates that the view has passed complete checks, that is, it has been fully verified. It can be activated.')
provViewComponents = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 2, 100, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 999999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: provViewComponents.setStatus('mandatory')
if mibBuilder.loadTexts: provViewComponents.setDescription('This attributes indicates the number of provisioned components that have been (or could be) saved.')
provViewFormats = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 2, 100, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: provViewFormats.setStatus('mandatory')
if mibBuilder.loadTexts: provViewFormats.setDescription('This attribute indicates the formats of the saved information. Each serves a different purpose. The ascii format is readable by operators and can be easily parsed and generated by scripts. NMS makes use of this format. Note that the syntax is subject to change without notice. This format is generated via Save -ascii Prov. A view with an ascii format can be loaded and activated. The commit format is generated via Commit Prov and allows for fast activation, that is, a shorter service outage time. The system will never leave a view with only this format, as it cannot be loaded. The delta format contains the changes made between the current view and the edit view. It is, therefore, much smaller and faster to Load or Save than the other formats. A view containing this format can be loaded or have the changes applied to the edit view. This provides a mechanism to propagate a set of changes from one view to another. A view containing only this format can be activated if this would not require a system reload. To generate this format, issue Save Prov without the -ascii or portable options. The part format is generated via Save component() Prov. The part format can be loaded. The syntax of this format is subject to change without notice. The portable format is a compact representation that can be quickly loaded. It can be transported from one Passport to another, or to an NMS. It is generated via Save -portable Prov. The portable format can be loaded and activated. Description of bits: ascii(0) commit(1) delta(2) part(3) portable(4)')
provViewBaseView = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 2, 100, 1, 5), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readonly")
if mibBuilder.loadTexts: provViewBaseView.setStatus('mandatory')
if mibBuilder.loadTexts: provViewBaseView.setDescription("This attribute indicates the name of the view upon which this view's changes are based (even if the delta format does not exists). In other words, it indicates the name of the current view that existed at the time that this view was saved. This may not be the name of the current view that is running now. This attribute is empty when the view is unsaved or if the current view was saved.")
provViewVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 2, 100, 1, 6), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: provViewVersion.setStatus('mandatory')
if mibBuilder.loadTexts: provViewVersion.setDescription('This attribute represents the version of base software that saved this view. It is empty if unknown.')
provViewCreationDate = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 11, 2, 100, 1, 7), EnterpriseDateAndTime().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(19, 19), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: provViewCreationDate.setStatus('mandatory')
if mibBuilder.loadTexts: provViewCreationDate.setDescription('This attribute indicates the creation date of this view.')
provisioningGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 19, 1))
provisioningGroupBE = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 19, 1, 5))
provisioningGroupBE00 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 19, 1, 5, 1))
provisioningGroupBE00A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 19, 1, 5, 1, 2))
provisioningCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 19, 3))
provisioningCapabilitiesBE = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 19, 3, 5))
provisioningCapabilitiesBE00 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 19, 3, 5, 1))
provisioningCapabilitiesBE00A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 19, 3, 5, 1, 2))
mibBuilder.exportSymbols("Nortel-Magellan-Passport-ProvisioningMIB", provViewVersion=provViewVersion, provViewRowStatus=provViewRowStatus, provViewCreationDate=provViewCreationDate, provStateTable=provStateTable, provStateEntry=provStateEntry, provViewUser=provViewUser, provisioningCapabilities=provisioningCapabilities, provisioningCapabilitiesBE00A=provisioningCapabilitiesBE00A, provisioningMIB=provisioningMIB, provRowStatusEntry=provRowStatusEntry, provisioningGroupBE=provisioningGroupBE, provOperEntry=provOperEntry, provComponentName=provComponentName, provisioningCapabilitiesBE=provisioningCapabilitiesBE, provisioningCapabilitiesBE00=provisioningCapabilitiesBE00, provStorageType=provStorageType, prov=prov, provActivityProgress=provActivityProgress, provViewRowStatusTable=provViewRowStatusTable, provLastUsedFileName=provLastUsedFileName, provRowStatusTable=provRowStatusTable, provProvisioningUser=provProvisioningUser, provIndex=provIndex, provEditViewDeletedComponents=provEditViewDeletedComponents, provViewComponents=provViewComponents, provViewIndex=provViewIndex, provViewOperTable=provViewOperTable, provCurrentViewFileName=provCurrentViewFileName, provViewStorageType=provViewStorageType, provCommittedFileName=provCommittedFileName, provConfirmRequired=provConfirmRequired, provEditViewAddedComponents=provEditViewAddedComponents, provView=provView, provViewOperEntry=provViewOperEntry, provViewBaseView=provViewBaseView, provCheckRequired=provCheckRequired, provStandbyCpActivityProgress=provStandbyCpActivityProgress, provProvisioningSession=provProvisioningSession, provOperTable=provOperTable, provEditViewName=provEditViewName, provViewCheckState=provViewCheckState, provAdminState=provAdminState, provRowStatus=provRowStatus, provStandbyCpActivity=provStandbyCpActivity, provViewRowStatusEntry=provViewRowStatusEntry, provisioningGroup=provisioningGroup, provUsageState=provUsageState, provisioningGroupBE00=provisioningGroupBE00, provEditViewChangedComponents=provEditViewChangedComponents, provViewComponentName=provViewComponentName, provProvisioningActivity=provProvisioningActivity, provisioningGroupBE00A=provisioningGroupBE00A, provNextFileSequenceNumber=provNextFileSequenceNumber, provViewFormats=provViewFormats, provOperationalState=provOperationalState, provProvisioningDirectory=provProvisioningDirectory)