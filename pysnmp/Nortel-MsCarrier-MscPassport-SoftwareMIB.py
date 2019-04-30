#
# PySNMP MIB module Nortel-MsCarrier-MscPassport-SoftwareMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-MsCarrier-MscPassport-SoftwareMIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:21:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
RowStatus, DisplayString, Unsigned32, StorageType = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB", "RowStatus", "DisplayString", "Unsigned32", "StorageType")
Link, NonReplicated, AsciiStringIndex, AsciiString = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-TextualConventionsMIB", "Link", "NonReplicated", "AsciiStringIndex", "AsciiString")
mscPassportMIBs, mscComponents = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB", "mscPassportMIBs", "mscComponents")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, Counter32, TimeTicks, Bits, IpAddress, MibIdentifier, ModuleIdentity, Gauge32, ObjectIdentity, Unsigned32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "Counter32", "TimeTicks", "Bits", "IpAddress", "MibIdentifier", "ModuleIdentity", "Gauge32", "ObjectIdentity", "Unsigned32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
softwareMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 17))
mscSw = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14))
mscSwRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 1), )
if mibBuilder.loadTexts: mscSwRowStatusTable.setStatus('mandatory')
mscSwRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwIndex"))
if mibBuilder.loadTexts: mscSwRowStatusEntry.setStatus('mandatory')
mscSwRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscSwRowStatus.setStatus('mandatory')
mscSwComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscSwComponentName.setStatus('mandatory')
mscSwStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscSwStorageType.setStatus('mandatory')
mscSwIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: mscSwIndex.setStatus('mandatory')
mscSwOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 11), )
if mibBuilder.loadTexts: mscSwOperTable.setStatus('mandatory')
mscSwOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 11, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwIndex"))
if mibBuilder.loadTexts: mscSwOperEntry.setStatus('mandatory')
mscSwTidyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 11, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("inactive", 0), ("inProgress", 1), ("querying", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscSwTidyStatus.setStatus('mandatory')
mscSwAvBeingTidied = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 11, 1, 421), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(1, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscSwAvBeingTidied.setStatus('mandatory')
mscSwAvlTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 256), )
if mibBuilder.loadTexts: mscSwAvlTable.setStatus('mandatory')
mscSwAvlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 256, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwIndex"), (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwAvlValue"))
if mibBuilder.loadTexts: mscSwAvlEntry.setStatus('mandatory')
mscSwAvlValue = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 256, 1, 1), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(1, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscSwAvlValue.setStatus('mandatory')
mscSwAvlRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 256, 1, 2), RowStatus()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: mscSwAvlRowStatus.setStatus('mandatory')
mscSwAvListToTidyTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 422), )
if mibBuilder.loadTexts: mscSwAvListToTidyTable.setStatus('mandatory')
mscSwAvListToTidyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 422, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwIndex"), (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwAvListToTidyValue"))
if mibBuilder.loadTexts: mscSwAvListToTidyEntry.setStatus('mandatory')
mscSwAvListToTidyValue = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 422, 1, 1), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(1, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscSwAvListToTidyValue.setStatus('mandatory')
mscSwAvListTidiedTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 423), )
if mibBuilder.loadTexts: mscSwAvListTidiedTable.setStatus('mandatory')
mscSwAvListTidiedEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 423, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwIndex"), (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwAvListTidiedValue"))
if mibBuilder.loadTexts: mscSwAvListTidiedEntry.setStatus('mandatory')
mscSwAvListTidiedValue = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 423, 1, 1), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(1, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscSwAvListTidiedValue.setStatus('mandatory')
mscSwPatlTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 436), )
if mibBuilder.loadTexts: mscSwPatlTable.setStatus('mandatory')
mscSwPatlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 436, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwIndex"), (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwPatlValue"))
if mibBuilder.loadTexts: mscSwPatlEntry.setStatus('mandatory')
mscSwPatlValue = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 436, 1, 1), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(1, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscSwPatlValue.setStatus('mandatory')
mscSwPatlRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 436, 1, 2), RowStatus()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: mscSwPatlRowStatus.setStatus('mandatory')
mscSwDld = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 2))
mscSwDldRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 2, 1), )
if mibBuilder.loadTexts: mscSwDldRowStatusTable.setStatus('mandatory')
mscSwDldRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 2, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwIndex"), (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwDldIndex"))
if mibBuilder.loadTexts: mscSwDldRowStatusEntry.setStatus('mandatory')
mscSwDldRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 2, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscSwDldRowStatus.setStatus('mandatory')
mscSwDldComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscSwDldComponentName.setStatus('mandatory')
mscSwDldStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 2, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscSwDldStorageType.setStatus('mandatory')
mscSwDldIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 2, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: mscSwDldIndex.setStatus('mandatory')
mscSwDldOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 2, 10), )
if mibBuilder.loadTexts: mscSwDldOperTable.setStatus('mandatory')
mscSwDldOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 2, 10, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwIndex"), (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwDldIndex"))
if mibBuilder.loadTexts: mscSwDldOperEntry.setStatus('mandatory')
mscSwDldAvBeingDownloaded = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 2, 10, 1, 1), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscSwDldAvBeingDownloaded.setStatus('mandatory')
mscSwDldStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 2, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("inactive", 0), ("inProgress", 1), ("stopping", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscSwDldStatus.setStatus('mandatory')
mscSwDldFilesToTransfer = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 2, 10, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscSwDldFilesToTransfer.setStatus('mandatory')
mscSwDldProcessorTargets = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 2, 10, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscSwDldProcessorTargets.setStatus('mandatory')
mscSwDldDldListTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 2, 260), )
if mibBuilder.loadTexts: mscSwDldDldListTable.setStatus('mandatory')
mscSwDldDldListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 2, 260, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwIndex"), (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwDldIndex"), (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwDldDldListValue"))
if mibBuilder.loadTexts: mscSwDldDldListEntry.setStatus('mandatory')
mscSwDldDldListValue = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 2, 260, 1, 1), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(1, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscSwDldDldListValue.setStatus('mandatory')
mscSwDldDldListRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 2, 260, 1, 2), RowStatus()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: mscSwDldDldListRowStatus.setStatus('mandatory')
mscSwDldDownloadedAvListTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 2, 261), )
if mibBuilder.loadTexts: mscSwDldDownloadedAvListTable.setStatus('mandatory')
mscSwDldDownloadedAvListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 2, 261, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwIndex"), (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwDldIndex"), (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwDldDownloadedAvListValue"))
if mibBuilder.loadTexts: mscSwDldDownloadedAvListEntry.setStatus('mandatory')
mscSwDldDownloadedAvListValue = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 2, 261, 1, 1), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(1, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscSwDldDownloadedAvListValue.setStatus('mandatory')
mscSwAv = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3))
mscSwAvRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 1), )
if mibBuilder.loadTexts: mscSwAvRowStatusTable.setStatus('mandatory')
mscSwAvRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwIndex"), (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwAvIndex"))
if mibBuilder.loadTexts: mscSwAvRowStatusEntry.setStatus('mandatory')
mscSwAvRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscSwAvRowStatus.setStatus('mandatory')
mscSwAvComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscSwAvComponentName.setStatus('mandatory')
mscSwAvStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscSwAvStorageType.setStatus('mandatory')
mscSwAvIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 1, 1, 10), AsciiStringIndex().subtype(subtypeSpec=ValueSizeConstraint(1, 30)))
if mibBuilder.loadTexts: mscSwAvIndex.setStatus('mandatory')
mscSwAvOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 10), )
if mibBuilder.loadTexts: mscSwAvOperTable.setStatus('mandatory')
mscSwAvOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 10, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwIndex"), (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwAvIndex"))
if mibBuilder.loadTexts: mscSwAvOperEntry.setStatus('mandatory')
mscSwAvProcessorTargets = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 10, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscSwAvProcessorTargets.setStatus('mandatory')
mscSwAvCompatibleAvListTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 259), )
if mibBuilder.loadTexts: mscSwAvCompatibleAvListTable.setStatus('mandatory')
mscSwAvCompatibleAvListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 259, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwIndex"), (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwAvIndex"), (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwAvCompatibleAvListValue"))
if mibBuilder.loadTexts: mscSwAvCompatibleAvListEntry.setStatus('mandatory')
mscSwAvCompatibleAvListValue = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 259, 1, 1), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(1, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscSwAvCompatibleAvListValue.setStatus('mandatory')
mscSwAvFeat = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 2))
mscSwAvFeatRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 2, 1), )
if mibBuilder.loadTexts: mscSwAvFeatRowStatusTable.setStatus('mandatory')
mscSwAvFeatRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 2, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwIndex"), (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwAvIndex"), (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwAvFeatIndex"))
if mibBuilder.loadTexts: mscSwAvFeatRowStatusEntry.setStatus('mandatory')
mscSwAvFeatRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 2, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscSwAvFeatRowStatus.setStatus('mandatory')
mscSwAvFeatComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscSwAvFeatComponentName.setStatus('mandatory')
mscSwAvFeatStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 2, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscSwAvFeatStorageType.setStatus('mandatory')
mscSwAvFeatIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 2, 1, 1, 10), AsciiStringIndex().subtype(subtypeSpec=ValueSizeConstraint(1, 25)))
if mibBuilder.loadTexts: mscSwAvFeatIndex.setStatus('mandatory')
mscSwAvPatch = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 3))
mscSwAvPatchRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 3, 1), )
if mibBuilder.loadTexts: mscSwAvPatchRowStatusTable.setStatus('mandatory')
mscSwAvPatchRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 3, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwIndex"), (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwAvIndex"), (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwAvPatchIndex"))
if mibBuilder.loadTexts: mscSwAvPatchRowStatusEntry.setStatus('mandatory')
mscSwAvPatchRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 3, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscSwAvPatchRowStatus.setStatus('mandatory')
mscSwAvPatchComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 3, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscSwAvPatchComponentName.setStatus('mandatory')
mscSwAvPatchStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 3, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscSwAvPatchStorageType.setStatus('mandatory')
mscSwAvPatchIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 3, 1, 1, 10), AsciiStringIndex().subtype(subtypeSpec=ValueSizeConstraint(1, 30)))
if mibBuilder.loadTexts: mscSwAvPatchIndex.setStatus('mandatory')
mscSwAvPatchOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 3, 10), )
if mibBuilder.loadTexts: mscSwAvPatchOperTable.setStatus('mandatory')
mscSwAvPatchOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 3, 10, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwIndex"), (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwAvIndex"), (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwAvPatchIndex"))
if mibBuilder.loadTexts: mscSwAvPatchOperEntry.setStatus('mandatory')
mscSwAvPatchDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 3, 3, 10, 1, 1), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscSwAvPatchDescription.setStatus('mandatory')
mscSwLpt = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 4))
mscSwLptRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 4, 1), )
if mibBuilder.loadTexts: mscSwLptRowStatusTable.setStatus('mandatory')
mscSwLptRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 4, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwIndex"), (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwLptIndex"))
if mibBuilder.loadTexts: mscSwLptRowStatusEntry.setStatus('mandatory')
mscSwLptRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 4, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscSwLptRowStatus.setStatus('mandatory')
mscSwLptComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 4, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscSwLptComponentName.setStatus('mandatory')
mscSwLptStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 4, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscSwLptStorageType.setStatus('mandatory')
mscSwLptIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 4, 1, 1, 10), AsciiStringIndex().subtype(subtypeSpec=ValueSizeConstraint(1, 25)))
if mibBuilder.loadTexts: mscSwLptIndex.setStatus('mandatory')
mscSwLptProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 4, 10), )
if mibBuilder.loadTexts: mscSwLptProvTable.setStatus('mandatory')
mscSwLptProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 4, 10, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwIndex"), (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwLptIndex"))
if mibBuilder.loadTexts: mscSwLptProvEntry.setStatus('mandatory')
mscSwLptCommentText = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 4, 10, 1, 1), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscSwLptCommentText.setStatus('mandatory')
mscSwLptSystemConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 4, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0))).clone(namedValues=NamedValues(("default", 0))).clone('default')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscSwLptSystemConfig.setStatus('mandatory')
mscSwLptFlTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 4, 257), )
if mibBuilder.loadTexts: mscSwLptFlTable.setStatus('mandatory')
mscSwLptFlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 4, 257, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwIndex"), (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwLptIndex"), (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwLptFlValue"))
if mibBuilder.loadTexts: mscSwLptFlEntry.setStatus('mandatory')
mscSwLptFlValue = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 4, 257, 1, 1), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(1, 25))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscSwLptFlValue.setStatus('mandatory')
mscSwLptFlRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 4, 257, 1, 2), RowStatus()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: mscSwLptFlRowStatus.setStatus('mandatory')
mscSwLptLogicalProcessorsTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 4, 258), )
if mibBuilder.loadTexts: mscSwLptLogicalProcessorsTable.setStatus('mandatory')
mscSwLptLogicalProcessorsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 4, 258, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwIndex"), (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwLptIndex"), (0, "Nortel-MsCarrier-MscPassport-SoftwareMIB", "mscSwLptLogicalProcessorsValue"))
if mibBuilder.loadTexts: mscSwLptLogicalProcessorsEntry.setStatus('mandatory')
mscSwLptLogicalProcessorsValue = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 14, 4, 258, 1, 1), Link()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscSwLptLogicalProcessorsValue.setStatus('mandatory')
softwareGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 17, 1))
softwareGroupCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 17, 1, 1))
softwareGroupCA02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 17, 1, 1, 3))
softwareGroupCA02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 17, 1, 1, 3, 2))
softwareCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 17, 3))
softwareCapabilitiesCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 17, 3, 1))
softwareCapabilitiesCA02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 17, 3, 1, 3))
softwareCapabilitiesCA02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 17, 3, 1, 3, 2))
mibBuilder.exportSymbols("Nortel-MsCarrier-MscPassport-SoftwareMIB", mscSwLptIndex=mscSwLptIndex, mscSwDldStatus=mscSwDldStatus, mscSwAvStorageType=mscSwAvStorageType, mscSwLptStorageType=mscSwLptStorageType, mscSwLptFlEntry=mscSwLptFlEntry, mscSwAvFeat=mscSwAvFeat, mscSwDldStorageType=mscSwDldStorageType, mscSwAvOperEntry=mscSwAvOperEntry, mscSw=mscSw, mscSwAvRowStatus=mscSwAvRowStatus, mscSwIndex=mscSwIndex, mscSwLptFlTable=mscSwLptFlTable, mscSwDldRowStatus=mscSwDldRowStatus, mscSwAvRowStatusEntry=mscSwAvRowStatusEntry, mscSwAvPatchRowStatus=mscSwAvPatchRowStatus, mscSwDldDownloadedAvListTable=mscSwDldDownloadedAvListTable, mscSwPatlValue=mscSwPatlValue, mscSwAvlValue=mscSwAvlValue, mscSwDldOperEntry=mscSwDldOperEntry, mscSwLptFlRowStatus=mscSwLptFlRowStatus, softwareGroupCA02A=softwareGroupCA02A, mscSwAvCompatibleAvListEntry=mscSwAvCompatibleAvListEntry, mscSwDldDldListRowStatus=mscSwDldDldListRowStatus, mscSwAvFeatStorageType=mscSwAvFeatStorageType, mscSwAvListToTidyTable=mscSwAvListToTidyTable, mscSwAvComponentName=mscSwAvComponentName, mscSwAvFeatIndex=mscSwAvFeatIndex, mscSwAvPatchOperEntry=mscSwAvPatchOperEntry, mscSwComponentName=mscSwComponentName, mscSwAvListTidiedEntry=mscSwAvListTidiedEntry, mscSwDld=mscSwDld, softwareMIB=softwareMIB, mscSwAvPatchRowStatusTable=mscSwAvPatchRowStatusTable, mscSwAvBeingTidied=mscSwAvBeingTidied, mscSwAvPatch=mscSwAvPatch, mscSwLptSystemConfig=mscSwLptSystemConfig, mscSwDldDldListEntry=mscSwDldDldListEntry, softwareCapabilities=softwareCapabilities, mscSwLptRowStatusTable=mscSwLptRowStatusTable, mscSwLptComponentName=mscSwLptComponentName, mscSwAv=mscSwAv, mscSwDldDldListValue=mscSwDldDldListValue, mscSwPatlTable=mscSwPatlTable, mscSwRowStatus=mscSwRowStatus, mscSwDldDownloadedAvListValue=mscSwDldDownloadedAvListValue, mscSwLptProvEntry=mscSwLptProvEntry, mscSwAvPatchRowStatusEntry=mscSwAvPatchRowStatusEntry, mscSwDldDldListTable=mscSwDldDldListTable, mscSwAvPatchComponentName=mscSwAvPatchComponentName, mscSwAvListToTidyValue=mscSwAvListToTidyValue, mscSwPatlRowStatus=mscSwPatlRowStatus, mscSwDldFilesToTransfer=mscSwDldFilesToTransfer, mscSwAvListTidiedTable=mscSwAvListTidiedTable, mscSwOperTable=mscSwOperTable, mscSwAvCompatibleAvListTable=mscSwAvCompatibleAvListTable, mscSwStorageType=mscSwStorageType, mscSwLptLogicalProcessorsValue=mscSwLptLogicalProcessorsValue, mscSwAvFeatRowStatusEntry=mscSwAvFeatRowStatusEntry, mscSwAvFeatRowStatus=mscSwAvFeatRowStatus, mscSwLptRowStatus=mscSwLptRowStatus, mscSwLpt=mscSwLpt, mscSwDldComponentName=mscSwDldComponentName, mscSwLptFlValue=mscSwLptFlValue, softwareCapabilitiesCA02=softwareCapabilitiesCA02, mscSwDldDownloadedAvListEntry=mscSwDldDownloadedAvListEntry, mscSwAvPatchStorageType=mscSwAvPatchStorageType, softwareCapabilitiesCA=softwareCapabilitiesCA, mscSwAvPatchIndex=mscSwAvPatchIndex, mscSwLptProvTable=mscSwLptProvTable, mscSwPatlEntry=mscSwPatlEntry, mscSwAvlRowStatus=mscSwAvlRowStatus, mscSwDldProcessorTargets=mscSwDldProcessorTargets, mscSwRowStatusTable=mscSwRowStatusTable, mscSwAvCompatibleAvListValue=mscSwAvCompatibleAvListValue, mscSwRowStatusEntry=mscSwRowStatusEntry, softwareGroupCA02=softwareGroupCA02, mscSwAvOperTable=mscSwAvOperTable, softwareGroupCA=softwareGroupCA, mscSwAvRowStatusTable=mscSwAvRowStatusTable, mscSwAvProcessorTargets=mscSwAvProcessorTargets, mscSwDldIndex=mscSwDldIndex, mscSwTidyStatus=mscSwTidyStatus, mscSwLptLogicalProcessorsEntry=mscSwLptLogicalProcessorsEntry, mscSwLptLogicalProcessorsTable=mscSwLptLogicalProcessorsTable, mscSwAvIndex=mscSwAvIndex, softwareGroup=softwareGroup, mscSwDldOperTable=mscSwDldOperTable, mscSwAvlEntry=mscSwAvlEntry, mscSwDldRowStatusTable=mscSwDldRowStatusTable, mscSwOperEntry=mscSwOperEntry, mscSwAvPatchDescription=mscSwAvPatchDescription, mscSwAvListTidiedValue=mscSwAvListTidiedValue, mscSwLptCommentText=mscSwLptCommentText, mscSwAvlTable=mscSwAvlTable, mscSwLptRowStatusEntry=mscSwLptRowStatusEntry, mscSwDldAvBeingDownloaded=mscSwDldAvBeingDownloaded, softwareCapabilitiesCA02A=softwareCapabilitiesCA02A, mscSwAvListToTidyEntry=mscSwAvListToTidyEntry, mscSwAvFeatRowStatusTable=mscSwAvFeatRowStatusTable, mscSwAvFeatComponentName=mscSwAvFeatComponentName, mscSwAvPatchOperTable=mscSwAvPatchOperTable, mscSwDldRowStatusEntry=mscSwDldRowStatusEntry)
