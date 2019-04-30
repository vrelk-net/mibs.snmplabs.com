#
# PySNMP MIB module OPTIX-SONET-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/OPTIX-SONET-TC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:26:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
optixCommon, = mibBuilder.importSymbols("OPTIX-OID-MIB", "optixCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Bits, Counter32, Unsigned32, Counter64, ModuleIdentity, NotificationType, ObjectIdentity, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "Counter32", "Unsigned32", "Counter64", "ModuleIdentity", "NotificationType", "ObjectIdentity", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Integer32", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
optixsonetTCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 99))
optixsonetTCMIB.setRevisions(('2006-02-25 00:00',))
if mibBuilder.loadTexts: optixsonetTCMIB.setLastUpdated('200602250000Z')
if mibBuilder.loadTexts: optixsonetTCMIB.setOrganization('Huawei Technologies Co.,Ltd.')
class AlarmEventType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(3, 6, 37, 69, 87, 100, 101, 111, 120, 185, 186, 187, 188, 189, 192, 193, 198, 200, 212, 213, 223, 232, 240, 270, 272, 273, 274, 275, 276, 277, 278, 279, 280, 282, 283, 284, 285, 286, 287, 288, 289, 323, 324, 325, 326, 327, 335, 433, 439, 440, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 570, 573, 574, 575, 591, 604, 606, 32768, 32769, 32774, 32776, 32777, 32778, 32779, 32791, 32792, 32794, 32798, 32802, 32803, 32804, 32807, 32808, 32814, 32815, 32816, 32817, 32818, 32819, 32820, 32821, 32822, 32823, 32824, 32825, 32826, 32827, 32828, 32829, 32830, 32831, 32832, 32833, 32834, 32835, 32836, 32837, 32838, 32839, 32840, 32841, 32842, 32843, 32844, 32845, 32846, 32847, 32848, 32849, 32876, 32877, 32878, 32879, 32880, 32881, 32882, 32883, 32884, 32886, 32887, 32889, 32890, 32891, 32892, 32899, 32900, 32901, 32903, 32904, 32905, 32906, 32907, 32908, 32909, 32910, 32911, 32912, 32913, 32915, 32916, 32917, 32918, 32919, 32920, 32921, 32922, 32923, 32924, 32925, 32926, 32927, 32928, 33156, 33161, 33170, 33171, 33172, 33174, 33175, 33176, 33177, 33280, 33281, 33282, 33283, 33284, 33286, 33287, 33289, 33298, 33301, 33304, 33305, 33312, 33314, 33315, 33316, 33330, 33331, 33332, 33333, 33335, 33336, 33337, 33345, 33347, 33348, 33349, 33350, 33351, 33361, 33363, 33364, 33365, 33368, 33370, 33372, 33373, 33374, 33375, 33377, 36923, 36924, 36925, 36926, 36927, 36928, 36930, 36936), SingleValueConstraint(36937, 36938, 36939, 36940, 36941, 36942, 36943, 36944, 36945, 36946, 36947, 36948, 36949, 36950, 36951, 36952, 36953, 36954, 36955, 36956, 36957, 36958, 36959, 36960, 36961, 36966, 36967, 36968, 36969, 36970, 36971, 36972, 36973, 36974, 36975, 36976, 36977, 40960, 40973, 40974, 40979, 40980, 40981, 40982, 63604, 63605, 63607, 63629, 63630, 65409, 65410, 65411, 40970, 40971, 40972, 40983, 40984, 36978, 36979, 36980, 36981, 36985, 36986, 40961, 12300, 40985, 40986, 12769, 12288, 12298, 12299, 12291, 12292, 12293, 12294, 12767, 12823, 12824, 12825, 12826))
    namedValues = NamedValues(("almLoc", 3), ("almFileLost", 6), ("almReiL", 37), ("almBcmPumHigh", 69), ("almTimS", 87), ("almSyncAllLos", 100), ("almSyncBad", 101), ("almSyncLos", 111), ("almPs", 120), ("almDbmsError", 185), ("almLosMut", 186), ("almLosChan", 187), ("almChanAdd", 188), ("almTd", 189), ("almClcPumHigh", 192), ("almS1SynChange", 193), ("almProtectMode", 198), ("almSecuAlm", 200), ("almFecLof", 212), ("almFecOof", 213), ("almRateOver", 223), ("almCfgbdFail", 232), ("almLoopback", 240), ("almClcModHigh", 270), ("almOtuLof", 272), ("almOtuOom", 273), ("almSmTim", 274), ("almPmTim", 275), ("almSmBdi", 276), ("almPmBdi", 277), ("almSmBei", 278), ("almPmBei", 279), ("almSmIae", 280), ("almSmBipExc", 282), ("almPmBipExc", 283), ("almSmBipSd", 284), ("almPmBipSd", 285), ("almOtuAis", 286), ("almOduAis", 287), ("almOduOci", 288), ("almOduLck", 289), ("almSumInpwrHigh", 323), ("almSumInpwrLow", 324), ("almSumOutpwrHigh", 325), ("almSumOutpwrLow", 326), ("almGainLow", 327), ("almBeffecExc", 335), ("almDgeAdjFail", 433), ("almWavelenLockFail", 439), ("almHscUnavail", 440), ("envEnvAircompr", 502), ("envEnvAircond", 503), ("envEnvAirdryr", 504), ("envEnvBatdschrg", 505), ("envEnvBattery", 506), ("envEnvClfan", 507), ("envEnvCpmajor", 508), ("envEnvCpminor", 509), ("envEnvEngine", 510), ("envEnvEngoprg", 511), ("envEnvExplgs", 512), ("envEnvFirdetr", 513), ("envEnvFire", 514), ("envEnvFlood", 515), ("envEnvFuse", 516), ("envEnvGen", 517), ("envEnvHiair", 518), ("envEnvHihum", 519), ("envEnvHitemp", 520), ("envEnvHiwtr", 521), ("envEnvIntruder", 522), ("envEnvLwbatvg", 523), ("envEnvLwfuel", 524), ("envEnvLwhum", 525), ("envEnvLwpres", 526), ("envEnvLwtemp", 527), ("envEnvLwwtr", 528), ("envEnvMisc", 529), ("envEnvOpendr", 530), ("envEnvPower", 531), ("envEnvPump", 532), ("envEnvPwr48", 536), ("envEnvRect", 537), ("envEnvRecthi", 538), ("envEnvRectlo", 539), ("envEnvSmoke", 540), ("envEnvToxicgas", 541), ("envEnvVentn", 542), ("envContAircond", 543), ("envContEngine", 544), ("envContFan", 545), ("envContGen", 546), ("envContHeat", 547), ("envContLight", 548), ("envContMisc", 549), ("envContSpklr", 550), ("almEsconCderr", 570), ("almCommitTimeout", 573), ("almSwdlNepkgcheck", 574), ("almSwdlChgmngMismatch", 575), ("almDbsyncFail", 591), ("almClientMm", 604), ("almLaserModuleMismatch", 606), ("almEqptNsa", 32768), ("almEqptSa", 32769), ("almApsb", 32774), ("almFeprlf", 32776), ("almApscm", 32777), ("almApsmm", 32778), ("almApstm", 32779), ("almHldoverSync", 32791), ("almFreerunSync", 32792), ("almFstsync", 32794), ("almManualSsmSet", 32798), ("almFanRmv", 32802), ("almSingleFanFail", 32803), ("almMultiFanFail", 32804), ("almMea", 32807), ("almRmv", 32808), ("almTf", 32814), ("almSfS", 32815), ("almInPwrHigh", 32816), ("almInPwrLow", 32817), ("almSfL", 32818), ("almSdL", 32819), ("almLsrEol", 32820), ("almOutPwrHigh", 32821), ("almOutPwrLow", 32822), ("almSdS", 32823), ("almAisL", 32824), ("almRfiL", 32825), ("almAisP", 32826), ("almLopP", 32827), ("almTimP", 32828), ("almUneqP", 32829), ("almSfP", 32830), ("almSdP", 32831), ("almRfiP", 32832), ("almAls", 32833), ("almLpbkfacility", 32834), ("almLpbkterm", 32835), ("almPlmP", 32836), ("almErfiPPld", 32837), ("almErfiPSer", 32838), ("almErfiPConn", 32839), ("almPdiP", 32840), ("almPwrFail", 32841), ("almLopV", 32842), ("almAisV", 32843), ("almPlmV", 32844), ("almUneqV", 32845), ("almRfiV", 32846), ("almErfiVSer", 32847), ("almErfiVConn", 32848), ("almErfiVPld", 32849), ("almIntfRmv", 32876), ("almSyncSsmChange", 32877), ("almTimingModeChange", 32878), ("almLow", 32879), ("almLp", 32880), ("almFrcd", 32881), ("almMan", 32882), ("almExer", 32883), ("almWtr", 32884), ("almSwtoidle", 32886), ("almSwFail", 32887), ("almSyncSw", 32889), ("almChanFail", 32890), ("almPwraFail", 32891), ("almPwrbFail", 32892), ("almIntfMea", 32899), ("almIntfFail", 32900), ("almAic", 32901), ("almDbmsCfgDamage", 32903), ("almDefkbyte", 32904), ("almIncnaps", 32905), ("almImaps", 32906), ("almEtsql", 32907), ("almTplalm", 32908), ("almSqlalm", 32909), ("almNodeidMm", 32910), ("almXconMm", 32911), ("almRingmMm", 32912), ("almSqlmMm", 32913), ("almLpS", 32915), ("almLowR", 32916), ("almLowS", 32917), ("almFrcdR", 32918), ("almFrcdS", 32919), ("almManR", 32920), ("almManS", 32921), ("almExerR", 32922), ("almExerS", 32923), ("almLpAllS", 32924), ("almRingswitch", 32925), ("almSpanswtich", 32926), ("almSwtopassthru", 32927), ("almLsql", 32928), ("almDbmsCfgBackupFailed", 33156), ("almFanFail", 33161), ("almInvalidEqpt", 33170), ("almLapdbvHigh", 33171), ("almLapdbvLow", 33172), ("almLbcHigh", 33174), ("almLbcLow", 33175), ("almLccHigh", 33176), ("almLccLow", 33177), ("almLinkErr", 33280), ("almLoa", 33281), ("almLof", 33282), ("almLomP", 33283), ("almLos", 33284), ("almLtempHigh", 33286), ("almLtempLow", 33287), ("almNebdDataMea", 33289), ("almNoLsrPara", 33298), ("almReffail", 33301), ("almSdV", 33304), ("almSfV", 33305), ("almSqmP", 33312), ("almSvMea", 33314), ("almTempHi", 33315), ("almAis", 33316), ("almInhlpbk", 33330), ("almLockout", 33331), ("almLaserShut", 33332), ("almLpbkallds1feac", 33333), ("almLpbkcrs", 33335), ("almLpbkds1feac", 33336), ("almLpbkds3feac", 33337), ("almLpbkfacilityP", 33345), ("almLpbktermP", 33347), ("almPrimarychnChange", 33348), ("almRai", 33349), ("almSsmDql", 33350), ("almSsmLos", 33351), ("almTsa", 33361), ("almNormal", 33363), ("almWkswbk", 33364), ("almWkswpr", 33365), ("almAteRmv", 33368), ("almPowerRmv", 33370), ("almOof", 33372), ("almExerSuccess", 33373), ("almExerFail", 33374), ("almUpgradeIp", 33375), ("almChassisMea", 33377), ("almLaserNotExist", 36923), ("almLcasBwReduced", 36924), ("almGfpLof", 36925), ("almFanOpen", 36926), ("almFanClose", 36927), ("almLevelMea", 36928), ("almTCvL", 36930), ("almDccFail", 36936)) + NamedValues(("almLanLoc", 36937), ("almTCvcpP", 36938), ("almTCvP", 36939), ("almTCvpP", 36940), ("almTCvS", 36941), ("almTCvV", 36942), ("almTEscpP", 36943), ("almTEsL", 36944), ("almTEsP", 36945), ("almTEspP", 36946), ("almTEsS", 36947), ("almTEsV", 36948), ("almTPjcsPdet", 36949), ("almTPjcsVdet", 36950), ("almTSescpP", 36951), ("almTSesL", 36952), ("almTSesP", 36953), ("almTSespP", 36954), ("almTSesS", 36955), ("almTSesV", 36956), ("almTUascpP", 36957), ("almTUasL", 36958), ("almTUasP", 36959), ("almTUaspP", 36960), ("almTUasV", 36961), ("almBitsAis", 36966), ("almBitsLof", 36967), ("almBitsLos", 36968), ("almBitsCvover", 36969), ("almBlsrSfR", 36970), ("almBlsrSfS", 36971), ("almBlsrSdR", 36972), ("almBlsrSdS", 36973), ("almIsolateNode", 36974), ("almSf", 36975), ("almSd", 36976), ("almAutosw", 36977), ("almLpbkfac2ni", 40960), ("almStateChange", 40973), ("almMtMode", 40974), ("almRmvToMt", 40979), ("almRstFromMt", 40980), ("almLpbk", 40981), ("almRlsLpbk", 40982), ("almRemcSf", 63604), ("almRemcSD", 63605), ("almPowerSwitch", 63607), ("almPortOffline", 63629), ("almDataLost", 63630), ("almSqmV", 65409), ("almLomV", 65410), ("almFcsErr", 65411), ("almRevertiveModeMismatch", 40970), ("almRingIDMismatch", 40971), ("almIncorrectFiberConnection", 40972), ("almSyncNotSyncnronized", 40983), ("almPowerExceed", 40984), ("almLcasPlct", 36978), ("almLcasPlcr", 36979), ("almLcasTlct", 36980), ("almLcasTlcr", 36981), ("almLcasFopt", 36985), ("almLcasFopr", 36986), ("almGfpCsf", 40961), ("almLptRfi", 12300), ("almPartialUnprotected", 40985), ("almFanMea", 40986), ("almLagPortFail", 12769), ("almDlagProtFail", 12288), ("almCcLoss", 12298), ("almMpConflict", 12299), ("almOamRemoteLoop", 12291), ("almOamRemoteSD", 12292), ("almOamRemoteSF", 12293), ("almOamFail", 12294), ("almOamSelfLoop", 12767), ("almEthCfmMismerge", 12823), ("almEthCfmUnexperi", 12824), ("almEthCfmLoc", 12825), ("almEthCfmRdi", 12826))

class AlmDataNtfcnCdeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("cr", 1), ("mj", 2), ("mn", 3), ("na", 4), ("nr", 5))

class AlmDataSrvEffType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("nsa", 1), ("sa", 2))

class DirectionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("all", 0), ("rcv", 1), ("trmt", 2))

class LocationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("all", 0), ("nend", 1), ("fend", 2))

class MOD2Type(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65))
    namedValues = NamedValues(("mod2All", 0), ("mod2Ds1", 1), ("mod2E100", 2), ("mod2E1000", 3), ("mod2Ec1", 4), ("mod2Oc3", 5), ("mod2Oc12", 6), ("mod2Oc48", 7), ("mod2Oc192", 8), ("mod2Sts1", 9), ("mod2Sts3c", 10), ("mod2Sts6c", 11), ("mod2Sts9c", 12), ("mod2Sts12c", 13), ("mod2Sts15c", 14), ("mod2Sts24c", 15), ("mod2Sts48c", 16), ("mod2Sts192c", 17), ("mod2T1", 18), ("mod2T3", 19), ("mod2M13", 20), ("mod2Vt1", 21), ("mod2Vt2", 22), ("mod2Env", 23), ("mod2Sync", 24), ("mod2Bits", 25), ("mod2Eqpt", 26), ("mod2Ds3", 27), ("mod2Stm1", 28), ("mod2Stm4", 29), ("mod2Stm16", 30), ("mod2Stm64", 31), ("mod2Vc3", 32), ("mod2Vc4", 33), ("mod2Vc12", 34), ("mod2Vc16c", 35), ("mod2Vc4c", 36), ("mod2E1", 37), ("mod2E3", 38), ("mod2E1t1", 39), ("mod2E3t3", 40), ("mod2Hardware", 41), ("mod2Syncall", 42), ("mod2Syncne", 43), ("mod2Syncfac", 44), ("mod2Cont", 45), ("mod2Ochl", 46), ("mod2Pg", 47), ("mod2Feth", 48), ("mod2Geth", 49), ("mod2Fe", 50), ("mod2Ge", 51), ("mod2Vctrunk", 52), ("mod2Och", 53), ("mod2Wdm", 54), ("mod2Client", 55), ("mod2Eth", 56), ("mod2Osc", 57), ("mod2Mca", 58), ("mod2Variable", 59), ("mod2Xgeth", 60), ("mod2Fc", 61), ("mod2Dcc", 62), ("mod2Lan", 63), ("mod2EQPT", 64), ("mod2Butt", 65))

class PerformanceEventType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(32770, 32784, 32785, 32786, 32789, 32799, 32800, 32801, 32852, 32992, 32993, 32994, 33000, 33001, 33002, 33008, 33009, 33010, 33011, 33012, 33013, 33014, 33015, 33016, 33056, 33057, 33058, 33059, 33060, 33061, 33064, 33065, 33088, 33089, 33090, 33091, 33092, 33093, 33094, 33095, 36864, 36865, 36866, 36867, 36868, 36869, 36870, 36871, 36872, 36873, 36874, 36875, 36876, 36877, 36878, 36879, 36880, 36881, 36882, 36883, 36884, 36885, 36886, 36887, 45065))
    namedValues = NamedValues(("pmSesS", 32770), ("pmCvL", 32784), ("pmEsL", 32785), ("pmSesL", 32786), ("pmUasL", 32789), ("pmPsd", 32799), ("pmCvP", 32800), ("pmEsP", 32801), ("pmPjcsVDet", 32852), ("pmBdtempcur", 32992), ("pmBdtempmax", 32993), ("pmBdtempmin", 32994), ("pmPmutempcur", 33000), ("pmPmutempmax", 33001), ("pmPmutempmin", 33002), ("pmLbccur", 33008), ("pmLbcmax", 33009), ("pmLbcmin", 33010), ("pmOptcur", 33011), ("pmOptmax", 33012), ("pmOptmin", 33013), ("pmOprcur", 33014), ("pmOprmax", 33015), ("pmOprmin", 33016), ("pmCvpP", 33056), ("pmCvcpP", 33057), ("pmEspP", 33058), ("pmEscpP", 33059), ("pmSespP", 33060), ("pmSescpP", 33061), ("pmUaspP", 33064), ("pmUascpP", 33065), ("pmPscProtect", 33088), ("pmPsdProtect", 33089), ("pmPscSpan", 33090), ("pmPsdSpan", 33091), ("pmPscRing", 33092), ("pmPsdRing", 33093), ("pmPscWork", 33094), ("pmPsdWork", 33095), ("pmLcccur", 36864), ("pmLccmax", 36865), ("pmLccmin", 36866), ("pmLtempcur", 36867), ("pmLtempmax", 36868), ("pmLtempmin", 36869), ("pmLapdbvcur", 36870), ("pmLapdbvmax", 36871), ("pmLapdbvmin", 36872), ("pmPlbccur", 36873), ("pmPlbcmax", 36874), ("pmPlbcmin", 36875), ("pmPlwccur", 36876), ("pmPlwcmax", 36877), ("pmPlwcmin", 36878), ("pmCvS", 36879), ("pmEsS", 36880), ("pmSesP", 36881), ("pmUasP", 36882), ("pmCvV", 36883), ("pmEsV", 36884), ("pmSesV", 36885), ("pmUasV", 36886), ("pmPsc", 36887), ("pmPjcsPDet", 45065))

class ValidflagType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("invalid", 0), ("valid", 1))

mibBuilder.exportSymbols("OPTIX-SONET-TC-MIB", DirectionType=DirectionType, LocationType=LocationType, AlarmEventType=AlarmEventType, PYSNMP_MODULE_ID=optixsonetTCMIB, AlmDataSrvEffType=AlmDataSrvEffType, ValidflagType=ValidflagType, AlmDataNtfcnCdeType=AlmDataNtfcnCdeType, PerformanceEventType=PerformanceEventType, optixsonetTCMIB=optixsonetTCMIB, MOD2Type=MOD2Type)
