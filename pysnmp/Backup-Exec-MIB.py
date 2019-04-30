#
# PySNMP MIB module Backup-Exec-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Backup-Exec-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:25:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, iso, Integer32, Counter64, ModuleIdentity, NotificationType, Counter32, ObjectIdentity, IpAddress, Bits, MibIdentifier, Gauge32, Unsigned32, NotificationType, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "iso", "Integer32", "Counter64", "ModuleIdentity", "NotificationType", "Counter32", "ObjectIdentity", "IpAddress", "Bits", "MibIdentifier", "Gauge32", "Unsigned32", "NotificationType", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
veritassoftware = MibIdentifier((1, 3, 6, 1, 4, 1, 1302))
backupExecNetWare = MibIdentifier((1, 3, 6, 1, 4, 1, 1302, 1))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 1302, 3))
backupexec = MibIdentifier((1, 3, 6, 1, 4, 1, 1302, 3, 1))
devices = MibIdentifier((1, 3, 6, 1, 4, 1, 1302, 3, 2))
trapvars = MibIdentifier((1, 3, 6, 1, 4, 1, 1302, 3, 3))
beconfig = MibIdentifier((1, 3, 6, 1, 4, 1, 1302, 3, 1, 1))
bejobs = MibIdentifier((1, 3, 6, 1, 4, 1, 1302, 3, 1, 2))
beinfo = MibIdentifier((1, 3, 6, 1, 4, 1, 1302, 3, 1, 3))
bemodules = MibIdentifier((1, 3, 6, 1, 4, 1, 1302, 3, 1, 4))
nonspecifictraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1302, 3, 1, 5))
loader = MibIdentifier((1, 3, 6, 1, 4, 1, 1302, 3, 2, 4))
tape = MibIdentifier((1, 3, 6, 1, 4, 1, 1302, 3, 2, 5))
labs = MibIdentifier((1, 3, 6, 1, 4, 1, 1302, 3, 1, 4, 1))
disasterrecovery = MibIdentifier((1, 3, 6, 1, 4, 1, 1302, 3, 1, 4, 2))
openfileoption = MibIdentifier((1, 3, 6, 1, 4, 1, 1302, 3, 1, 4, 3))
pvldevice = MibIdentifier((1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 1))
pvlmedia = MibIdentifier((1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 2))
catalog = MibIdentifier((1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 3))
tapealert = MibIdentifier((1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 4))
databasemaint = MibIdentifier((1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 5))
softwareupdate = MibIdentifier((1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 6))
install = MibIdentifier((1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 7))
serverName = MibScalar((1, 3, 6, 1, 4, 1, 1302, 3, 3, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serverName.setStatus('mandatory')
appInfo = MibScalar((1, 3, 6, 1, 4, 1, 1302, 3, 3, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appInfo.setStatus('mandatory')
jobName = MibScalar((1, 3, 6, 1, 4, 1, 1302, 3, 3, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jobName.setStatus('mandatory')
operatorName = MibScalar((1, 3, 6, 1, 4, 1, 1302, 3, 3, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: operatorName.setStatus('mandatory')
messageText = MibScalar((1, 3, 6, 1, 4, 1, 1302, 3, 3, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: messageText.setStatus('mandatory')
additionalText = MibScalar((1, 3, 6, 1, 4, 1, 1302, 3, 3, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: additionalText.setStatus('mandatory')
backupExecNTGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 1302, 3, 1, 1, 9))
beNTLoaded = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 1, 1, 9) + (0,1)).setObjects(("Backup-Exec-MIB", "messageText"), ("Backup-Exec-MIB", "serverName"), ("Backup-Exec-MIB", "appInfo"))
beNTUnloaded = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 1, 1, 9) + (0,2)).setObjects(("Backup-Exec-MIB", "messageText"), ("Backup-Exec-MIB", "serverName"), ("Backup-Exec-MIB", "appInfo"))
beNTSystemError = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 1, 1, 9) + (0,3)).setObjects(("Backup-Exec-MIB", "messageText"), ("Backup-Exec-MIB", "serverName"), ("Backup-Exec-MIB", "additionalText"))
beNTGeneralInfo = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 1, 1, 9) + (0,4)).setObjects(("Backup-Exec-MIB", "messageText"), ("Backup-Exec-MIB", "serverName"), ("Backup-Exec-MIB", "additionalText"))
backupExecNTJobs = MibIdentifier((1, 3, 6, 1, 4, 1, 1302, 3, 1, 2, 8))
jobFailure = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 1, 2, 8) + (0,1)).setObjects(("Backup-Exec-MIB", "messageText"), ("Backup-Exec-MIB", "serverName"), ("Backup-Exec-MIB", "jobName"), ("Backup-Exec-MIB", "additionalText"))
jobAborted = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 1, 2, 8) + (0,2)).setObjects(("Backup-Exec-MIB", "messageText"), ("Backup-Exec-MIB", "serverName"), ("Backup-Exec-MIB", "jobName"), ("Backup-Exec-MIB", "operatorName"))
jobSuccess = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 1, 2, 8) + (0,3)).setObjects(("Backup-Exec-MIB", "messageText"), ("Backup-Exec-MIB", "serverName"), ("Backup-Exec-MIB", "jobName"), ("Backup-Exec-MIB", "additionalText"))
jobSuccessExcept = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 1, 2, 8) + (0,4)).setObjects(("Backup-Exec-MIB", "messageText"), ("Backup-Exec-MIB", "serverName"), ("Backup-Exec-MIB", "jobName"), ("Backup-Exec-MIB", "additionalText"))
jobStarted = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 1, 2, 8) + (0,5)).setObjects(("Backup-Exec-MIB", "messageText"), ("Backup-Exec-MIB", "serverName"), ("Backup-Exec-MIB", "jobName"), ("Backup-Exec-MIB", "additionalText"))
jobNoData = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 1, 2, 8) + (0,6)).setObjects(("Backup-Exec-MIB", "messageText"))
jobWarning = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 1, 2, 8) + (0,7)).setObjects(("Backup-Exec-MIB", "messageText"))
beName = MibScalar((1, 3, 6, 1, 4, 1, 1302, 3, 1, 3, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: beName.setStatus('mandatory')
revMajor = MibScalar((1, 3, 6, 1, 4, 1, 1302, 3, 1, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: revMajor.setStatus('mandatory')
revMinor = MibScalar((1, 3, 6, 1, 4, 1, 1302, 3, 1, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: revMinor.setStatus('mandatory')
beBuild = MibScalar((1, 3, 6, 1, 4, 1, 1302, 3, 1, 3, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: beBuild.setStatus('mandatory')
beSerial = MibScalar((1, 3, 6, 1, 4, 1, 1302, 3, 1, 3, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: beSerial.setStatus('mandatory')
backupExecOptLABS = MibIdentifier((1, 3, 6, 1, 4, 1, 1302, 3, 1, 4, 1, 1))
multipleTapesNeeded = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 1, 4, 1, 1) + (0,1)).setObjects(("Backup-Exec-MIB", "messageText"), ("Backup-Exec-MIB", "serverName"), ("Backup-Exec-MIB", "jobName"), ("Backup-Exec-MIB", "additionalText"))
retriedAutomatically = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 1, 4, 1, 1) + (0,2)).setObjects(("Backup-Exec-MIB", "messageText"), ("Backup-Exec-MIB", "serverName"), ("Backup-Exec-MIB", "jobName"), ("Backup-Exec-MIB", "additionalText"))
backupExecOptIDR = MibIdentifier((1, 3, 6, 1, 4, 1, 1302, 3, 1, 4, 2, 1))
copyDRFile = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 1, 4, 2, 1) + (0,1)).setObjects(("Backup-Exec-MIB", "messageText"), ("Backup-Exec-MIB", "serverName"), ("Backup-Exec-MIB", "jobName"), ("Backup-Exec-MIB", "additionalText"))
fullBackupComplete = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 1, 4, 2, 1) + (0,2)).setObjects(("Backup-Exec-MIB", "messageText"), ("Backup-Exec-MIB", "serverName"), ("Backup-Exec-MIB", "jobName"), ("Backup-Exec-MIB", "additionalText"))
backupExecOptOFO = MibIdentifier((1, 3, 6, 1, 4, 1, 1302, 3, 1, 4, 3, 1))
ofoFailed = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 1, 4, 3, 1) + (0,1)).setObjects(("Backup-Exec-MIB", "messageText"), ("Backup-Exec-MIB", "serverName"), ("Backup-Exec-MIB", "jobName"), ("Backup-Exec-MIB", "additionalText"))
ofoCouldNotInit = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 1, 4, 3, 1) + (0,2)).setObjects(("Backup-Exec-MIB", "messageText"), ("Backup-Exec-MIB", "serverName"), ("Backup-Exec-MIB", "jobName"), ("Backup-Exec-MIB", "additionalText"))
backupExecPVLDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 1, 1))
pvlDeviceError = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 1, 1) + (0,1)).setObjects(("Backup-Exec-MIB", "messageText"))
pvlDeviceWarning = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 1, 1) + (0,2)).setObjects(("Backup-Exec-MIB", "messageText"))
pvlDeviceInfo = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 1, 1) + (0,3)).setObjects(("Backup-Exec-MIB", "messageText"))
pvlDeviceAttn = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 1, 1) + (0,4)).setObjects(("Backup-Exec-MIB", "messageText"))
backupExecPVLMedia = MibIdentifier((1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 2, 1))
pvlMediaError = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 2, 1) + (0,1)).setObjects(("Backup-Exec-MIB", "messageText"))
pvlMediaWarning = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 2, 1) + (0,2)).setObjects(("Backup-Exec-MIB", "messageText"))
pvlMediaInfo = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 2, 1) + (0,3)).setObjects(("Backup-Exec-MIB", "messageText"))
pvlMediaAttn = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 2, 1) + (0,4)).setObjects(("Backup-Exec-MIB", "messageText"))
backupExecCatalog = MibIdentifier((1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 3, 1))
catalogFailed = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 3, 1) + (0,1)).setObjects(("Backup-Exec-MIB", "messageText"))
backupExecTapeAlert = MibIdentifier((1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 4, 1))
tapeAlertError = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 4, 1) + (0,1)).setObjects(("Backup-Exec-MIB", "messageText"))
tapeAlertWarning = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 4, 1) + (0,2)).setObjects(("Backup-Exec-MIB", "messageText"))
tapeAlertInfo = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 4, 1) + (0,3)).setObjects(("Backup-Exec-MIB", "messageText"))
backupExecDatabaseMaintenance = MibIdentifier((1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 5, 1))
databaseMaintenanceError = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 5, 1) + (0,1)).setObjects(("Backup-Exec-MIB", "messageText"))
databaseMaintenanceInfo = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 5, 1) + (0,2)).setObjects(("Backup-Exec-MIB", "messageText"))
backupExecSoftwareUpdate = MibIdentifier((1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 6, 1))
softwareUpdateError = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 6, 1) + (0,1)).setObjects(("Backup-Exec-MIB", "messageText"))
softwareUpdateWarning = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 6, 1) + (0,2)).setObjects(("Backup-Exec-MIB", "messageText"))
softwareUpdateInfo = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 6, 1) + (0,3)).setObjects(("Backup-Exec-MIB", "messageText"))
backupExecInstall = MibIdentifier((1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 7, 1))
installWarning = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 7, 1) + (0,1)).setObjects(("Backup-Exec-MIB", "messageText"))
installInfo = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 7, 1) + (0,2)).setObjects(("Backup-Exec-MIB", "messageText"))
backupExecNTLoader = MibIdentifier((1, 3, 6, 1, 4, 1, 1302, 3, 2, 4, 3))
loaderNeedsAttention = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 2, 4, 3) + (0,3)).setObjects(("Backup-Exec-MIB", "messageText"), ("Backup-Exec-MIB", "serverName"), ("Backup-Exec-MIB", "jobName"), ("Backup-Exec-MIB", "additionalText"))
backupExecNTTapeDrive = MibIdentifier((1, 3, 6, 1, 4, 1, 1302, 3, 2, 5, 3))
driveNeedsAttention = NotificationType((1, 3, 6, 1, 4, 1, 1302, 3, 2, 5, 3) + (0,3)).setObjects(("Backup-Exec-MIB", "messageText"), ("Backup-Exec-MIB", "serverName"), ("Backup-Exec-MIB", "jobName"), ("Backup-Exec-MIB", "additionalText"))
messageobject = MibScalar((1, 3, 6, 1, 4, 1, 1302, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: messageobject.setStatus('mandatory')
blockingerrormsg = NotificationType((1, 3, 6, 1, 4, 1, 1302, 1) + (0,1)).setObjects(("Backup-Exec-MIB", "messageobject"))
errormessage = NotificationType((1, 3, 6, 1, 4, 1, 1302, 1) + (0,2)).setObjects(("Backup-Exec-MIB", "messageobject"))
blockingmessage = NotificationType((1, 3, 6, 1, 4, 1, 1302, 1) + (0,3)).setObjects(("Backup-Exec-MIB", "messageobject"))
warningmessage = NotificationType((1, 3, 6, 1, 4, 1, 1302, 1) + (0,4)).setObjects(("Backup-Exec-MIB", "messageobject"))
informationmessage = NotificationType((1, 3, 6, 1, 4, 1, 1302, 1) + (0,5)).setObjects(("Backup-Exec-MIB", "messageobject"))
mibBuilder.exportSymbols("Backup-Exec-MIB", pvlDeviceInfo=pvlDeviceInfo, softwareUpdateInfo=softwareUpdateInfo, veritassoftware=veritassoftware, loaderNeedsAttention=loaderNeedsAttention, nonspecifictraps=nonspecifictraps, loader=loader, jobName=jobName, install=install, backupExecDatabaseMaintenance=backupExecDatabaseMaintenance, tape=tape, ofoFailed=ofoFailed, beNTLoaded=beNTLoaded, serverName=serverName, pvlDeviceError=pvlDeviceError, jobSuccess=jobSuccess, informationmessage=informationmessage, backupExecPVLDevice=backupExecPVLDevice, catalog=catalog, beinfo=beinfo, backupExecNTTapeDrive=backupExecNTTapeDrive, retriedAutomatically=retriedAutomatically, jobWarning=jobWarning, backupexec=backupexec, pvlMediaError=pvlMediaError, softwareUpdateWarning=softwareUpdateWarning, installInfo=installInfo, pvlMediaWarning=pvlMediaWarning, openfileoption=openfileoption, jobNoData=jobNoData, beNTSystemError=beNTSystemError, pvldevice=pvldevice, backupExecNTJobs=backupExecNTJobs, installWarning=installWarning, pvlDeviceAttn=pvlDeviceAttn, jobAborted=jobAborted, labs=labs, fullBackupComplete=fullBackupComplete, databaseMaintenanceInfo=databaseMaintenanceInfo, products=products, backupExecTapeAlert=backupExecTapeAlert, revMinor=revMinor, backupExecOptLABS=backupExecOptLABS, backupExecNTLoader=backupExecNTLoader, pvlMediaAttn=pvlMediaAttn, warningmessage=warningmessage, backupExecOptOFO=backupExecOptOFO, bejobs=bejobs, blockingmessage=blockingmessage, bemodules=bemodules, backupExecNTGeneral=backupExecNTGeneral, additionalText=additionalText, devices=devices, revMajor=revMajor, messageText=messageText, driveNeedsAttention=driveNeedsAttention, backupExecPVLMedia=backupExecPVLMedia, tapeAlertInfo=tapeAlertInfo, ofoCouldNotInit=ofoCouldNotInit, beNTUnloaded=beNTUnloaded, trapvars=trapvars, backupExecInstall=backupExecInstall, jobSuccessExcept=jobSuccessExcept, tapeAlertWarning=tapeAlertWarning, backupExecCatalog=backupExecCatalog, backupExecNetWare=backupExecNetWare, softwareUpdateError=softwareUpdateError, beName=beName, beNTGeneralInfo=beNTGeneralInfo, softwareupdate=softwareupdate, beconfig=beconfig, copyDRFile=copyDRFile, pvlDeviceWarning=pvlDeviceWarning, multipleTapesNeeded=multipleTapesNeeded, catalogFailed=catalogFailed, disasterrecovery=disasterrecovery, backupExecSoftwareUpdate=backupExecSoftwareUpdate, messageobject=messageobject, backupExecOptIDR=backupExecOptIDR, errormessage=errormessage, operatorName=operatorName, beBuild=beBuild, appInfo=appInfo, jobStarted=jobStarted, beSerial=beSerial, tapealert=tapealert, databasemaint=databasemaint, blockingerrormsg=blockingerrormsg, tapeAlertError=tapeAlertError, pvlMediaInfo=pvlMediaInfo, pvlmedia=pvlmedia, jobFailure=jobFailure, databaseMaintenanceError=databaseMaintenanceError)