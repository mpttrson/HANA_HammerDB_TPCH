import csv
import string
import random

###Positions in initial array
#array_base[0] = RCLNT
#array_base[1] = RLDNR
#array_base[2] = RBUKRS
#array_base[3] = GJAHR
#array_base[4] = BELNR
#array_base[5] = DOCLN
#array_base[6] = RYEAR
#array_base[7] = RRCTY
#array_base[8] = VORGN
#array_base[9] = VRGNG
#array_base[10] = BTTYPE
#array_base[11] = AWTYP
#array_base[12] = AWORG
#array_base[13] = AWREF
#array_base[14] = AWITEM
#array_base[15] = AWITGRP
#array_base[16] = SUBTA
#array_base[17] = XREVERSED
#array_base[18] = XTRUEREV
#array_base[19] = AWTYP_REV
#array_base[20] = AWORG_REV
#array_base[21] = AWREF_REV
#array_base[22] = SRC_AWTYP
#array_base[23] = SRC_AWREF
#array_base[24] = SRC_AWITEM
#array_base[25] = RTCUR
#array_base[26] = RWCUR
#array_base[27] = RHCUR
#array_base[28] = RKCUR
#array_base[29] = RUNIT
#array_base[30] = RVUNIT
#array_base[31] = RRUNIT
#array_base[32] = CO_MEINH
#array_base[33] = RACCT
#array_base[34] = RCNTR
#array_base[35] = PRCTR
#array_base[36] = RFAREA
#array_base[37] = RBUSA
#array_base[38] = KOKRS
#array_base[39] = SEGMENT
#array_base[40] = PPRCTR
#array_base[41] = PSEGMENT
#array_base[42] = TSL
#array_base[43] = WSL
#array_base[44] = WSL2
#array_base[45] = WSL3
#array_base[46] = HSL
#array_base[47] = KSL
#array_base[48] = MSL
#array_base[49] = MFSL
#array_base[50] = VMSL
#array_base[51] = VMFSL
#array_base[52] = RMSL
#array_base[53] = CO_MEGBTR
#array_base[54] = CO_MEFBTR
#array_base[55] = HSALK3
#array_base[56] = KSALK3
#array_base[57] = LBKUM
#array_base[58] = DRCRK
#array_base[59] = POPER
#array_base[60] = PERIV
#array_base[61] = FISCYEARPER
#array_base[62] = BUDAT
#array_base[63] = BLDAT
#array_base[64] = BLART
#array_base[65] = BUZEI
#array_base[66] = ZUONR
#array_base[67] = BSCHL
#array_base[68] = BSTAT
#array_base[69] = LINETYPE
#array_base[70] = KTOSL
#array_base[71] = SLALITTYPE
#array_base[72] = XSPLITMOD
#array_base[73] = USNAM
#array_base[74] = TIMESTAMP
#array_base[75] = RHOART
#array_base[76] = GLACCOUNT_TYPE
#array_base[77] = KTOPL
#array_base[78] = EBELN
#array_base[79] = EBELP
#array_base[80] = ZEKKN
#array_base[81] = SGTXT
#array_base[82] = KDAUF
#array_base[83] = KDPOS
#array_base[84] = MATNR
#array_base[85] = WERKS
#array_base[86] = LIFNR
#array_base[87] = KUNNR
#array_base[88] = FBUDA
#array_base[89] = WWERT
#array_base[90] = KOART
#array_base[91] = UMSKZ
#array_base[92] = MWSKZ
#array_base[93] = VALUT
#array_base[94] = XOPVW
#array_base[95] = VPRSV
#array_base[96] = MLAST
#array_base[97] = VTSTAMP
#array_base[98] = BWTAR

###Positions in new array
#array_base[0] =	RCLNT
#array_base[1] =	RLDNR
#array_base[2] =	RBUKRS
#array_base[3] =	GJAHR
#array_base[4] =	BELNR     
#array_base[5] =	DOCLN 
#array_base[6] =	RYEAR
#array_base[7] =	RRCTY
#array_base[8] =	RMVCT
#array_base[9] =	VORGN
#array_base[10] =	VRGNG
#array_base[11] =	BTTYPE
#array_base[12] =	AWTYP
#array_base[13] =	AWSYS 
#array_base[14] =	AWORG   
#array_base[15] =	AWREF    
#array_base[16] =	AWITEM
#array_base[17] =	AWITGRP
#array_base[18] =	SUBTA 
#array_base[19] =	XREVERSING
#array_base[20] =	XREVERSED
#array_base[21] =	XTRUEREV
#array_base[22] =	AWTYP_REV
#array_base[23] =	AWORG_REV
#array_base[24] =	AWREF_REV
#array_base[25] =	SUBTA_REV
#array_base[26] =	XSETTLING
#array_base[27] =	XSETTLED
#array_base[28] =	PREC_AWTYP
#array_base[29] =	PREC_AWORG
#array_base[30] =	PREC_AWREF
#array_base[31] =	PREC_AWITEM
#array_base[32] =	PREC_SUBTA
#array_base[33] =	PREC_AWMULT                     
#array_base[34] =	XSECONDARY
#array_base[35] =	RTCUR
#array_base[36] =	RWCUR
#array_base[37] =	RHCUR
#array_base[38] =	RKCUR
#array_base[39] =	ROCUR
#array_base[40] =	RVCUR
#array_base[41] =	RBCUR
#array_base[42] =	RCCUR
#array_base[43] =	RDCUR
#array_base[44] =	RECUR
#array_base[45] =	RFCUR
#array_base[46] =	RGCUR
#array_base[47] =	RCO_OCUR
#array_base[48] =	RUNIT
#array_base[49] =	RVUNIT
#array_base[50] =	RRUNIT
#array_base[51] =	QUNIT1
#array_base[52] =	QUNIT2
#array_base[53] =	QUNIT3
#array_base[54] =	RACCT     
#array_base[55] =	RCNTR
#array_base[56] =	PRCTR    
#array_base[57] =	RFAREA
#array_base[58] =	RBUSA
#array_base[59] =	KOKRS
#array_base[60] =	SEGMENT
#array_base[61] =	SCNTR
#array_base[62] =	PPRCTR
#array_base[63] =	SFAREA
#array_base[64] =	SBUSA
#array_base[65] =	RASSC
#array_base[66] =	PSEGMENT
#array_base[67] =	TSL 
#array_base[68] =	WSL 
#array_base[69] =	WSL2
#array_base[70] =	WSL3
#array_base[71] =	HSL 
#array_base[72] =	KSL
#array_base[73] =	OSL
#array_base[74] =	VSL 
#array_base[75] =	BSL
#array_base[76] =	CSL
#array_base[77] =	DSL
#array_base[78] =	ESL
#array_base[79] =	FSL
#array_base[80] =	GSL
#array_base[81] =	KFSL
#array_base[82] =	KFSL2
#array_base[83] =	KFSL3
#array_base[84] =	PSL
#array_base[85] =	PSL2
#array_base[86] =	PSL3
#array_base[87] =	PFSL
#array_base[88] =	PFSL2
#array_base[89] =	PFSL3
#array_base[90] =	CO_OSL
#array_base[91] =	HSALK3
#array_base[92] =	KSALK3
#array_base[93] =	OSALK3
#array_base[94] =	VSALK3
#array_base[95] =	HSALKV
#array_base[96] =	KSALKV
#array_base[97] =	OSALKV
#array_base[98] =	VSALKV
#array_base[99] =	HPVPRS
#array_base[100] =	KPVPRS
#array_base[101] =	OPVPRS
#array_base[102] =	VPVPRS
#array_base[103] =	HSTPRS
#array_base[104] =	KSTPRS
#array_base[105] =	OSTPRS
#array_base[106] =	VSTPRS
#array_base[107] =	HSLALT
#array_base[108] =	KSLALT
#array_base[109] =	OSLALT
#array_base[110] =	VSLALT
#array_base[111] =	HSLEXT
#array_base[112] =	KSLEXT
#array_base[113] =	OSLEXT
#array_base[114] =	VSLEXT
#array_base[115] =	HVKWRT
#array_base[116] =	HVKSAL
#array_base[117] =	MSL
#array_base[118] =	MFSL
#array_base[119] =	VMSL
#array_base[120] =	VMFSL
#array_base[121] =	RMSL
#array_base[122] =	QUANT1
#array_base[123] =	QUANT2
#array_base[124] =	QUANT3
#array_base[125] =	LBKUM
#array_base[126] =	DRCRK
#array_base[127] =	POPER
#array_base[128] =	PERIV
#array_base[129] =	FISCYEARPER
#array_base[130] =	BUDAT   
#array_base[131] =	BLDAT   
#array_base[132] =	BLART
#array_base[133] =	BUZEI
#array_base[134] =	ZUONR   
#array_base[135] =	BSCHL
#array_base[136] =	BSTAT
#array_base[137] =	LINETYPE
#array_base[138] =	KTOSL
#array_base[139] =	SLALITTYPE
#array_base[140] =	XSPLITMOD
#array_base[141] =	USNAM    
#array_base[142] =	TIMESTAMP         
#array_base[143] =	EPRCTR
#array_base[144] =	RHOART
#array_base[145] =	GLACCOUNT_TYPE
#array_base[146] =	KTOPL
#array_base[147] =	LOKKT    
#array_base[148] =	KTOP2
#array_base[149] =	REBZG
#array_base[150] =	REBZJ
#array_base[151] =	REBZZ
#array_base[152] =	REBZT
#array_base[153] =	RBEST
#array_base[154] =	EBELN
#array_base[155] =	EBELP
#array_base[156] =	ZEKKN
#array_base[157] =	SGTXT
#array_base[158] =	KDAUF
#array_base[159] =	KDPOS 
#array_base[160] =	MATNR
#array_base[161] =	WERKS
#array_base[162] =	LIFNR
#array_base[163] =	KUNNR
#array_base[164] =	FBUDA   
#array_base[165] =	KOART
#array_base[166] =	UMSKZ
#array_base[167] =	MWSKZ
#array_base[168] =	HBKID
#array_base[169] =	HKTID
#array_base[170] =	XOPVW
#array_base[171] =	AUGDT   
#array_base[172] =	AUGBL
#array_base[173] =	AUGGJ
#array_base[174] =	AFABE
#array_base[175] =	ANLN1
#array_base[176] =	ANLN2
#array_base[177] =	BZDAT   
#array_base[178] =	ANBWA
#array_base[179] =	MOVCAT
#array_base[180] =	DEPR_PERIOD
#array_base[181] =	ANLGR
#array_base[182] =	ANLGR2
#array_base[183] =	SETTLEMENT_RULE
#array_base[184] =	UBZDT_PN
#array_base[185] =	XVABG_PN
#array_base[186] =	PROZS_PN
#array_base[187] =	XMANPROPVAL_PN
#array_base[188] =	KALNR       
#array_base[189] =	VPRSV
#array_base[190] =	MLAST
#array_base[191] =	KZBWS
#array_base[192] =	XOBEW
#array_base[193] =	SOBKZ
#array_base[194] =	VTSTAMP
#array_base[195] =	MAT_KDAUF
#array_base[196] =	MAT_KDPOS
#array_base[197] =	MAT_PSPNR
#array_base[198] =	MAT_PS_POSID
#array_base[199] =	MAT_LIFNR
#array_base[200] =	BWTAR
#array_base[201] =	BWKEY
#array_base[202] =	HPEINH
#array_base[203] =	KPEINH
#array_base[204] =	OPEINH
#array_base[205] =	VPEINH
#array_base[206] =	MLPTYP
#array_base[207] =	MLCATEG
#array_base[208] =	QSBVALT     
#array_base[209] =	QSPROCESS   
#array_base[210] =	PERART
#array_base[211] =	MLPOSNR
#array_base[212] =	RACCT_SENDER
#array_base[213] =	ACCAS_SENDER
#array_base[214] =	ACCASTY_SENDER
#array_base[215] =	OBJNR
#array_base[216] =	HRKFT
#array_base[217] =	HKGRP
#array_base[218] =	PAROB1
#array_base[219] =	PAROBSRC
#array_base[220] =	USPOB
#array_base[221] =	CO_BELKZ
#array_base[222] =	CO_BEKNZ
#array_base[223] =	BELTP
#array_base[224] =	MUVFLG
#array_base[225] =	GKONT     
#array_base[226] =	GKOAR
#array_base[227] =	ERLKZ
#array_base[228] =	PERNR   
#array_base[229] =	PAOBJNR   
#array_base[230] =	XPAOBJNR_CO_REL
#array_base[231] =	SCOPE
#array_base[232] =	LOGSYSO
#array_base[233] =	PBUKRS
#array_base[234] =	PSCOPE
#array_base[235] =	LOGSYSP
#array_base[236] =	BWSTRAT
#array_base[237] =	OBJNR_HK
#array_base[238] =	AUFNR_ORG
#array_base[239] =	UKOSTL
#array_base[240] =	ULSTAR
#array_base[241] =	UPRZNR
#array_base[242] =	ACCAS
#array_base[243] =	ACCASTY
#array_base[244] =	LSTAR
#array_base[245] =	AUFNR
#array_base[246] =	AUTYP
#array_base[247] =	PS_PSP_PNR
#array_base[248] =	PS_POSID
#array_base[249] =	PS_PSPID
#array_base[250] =	NPLNR
#array_base[251] =	NPLNR_VORGN
#array_base[252] =	PRZNR
#array_base[253] =	KSTRG
#array_base[254] =	BEMOT
#array_base[255] =	RSRCE
#array_base[256] =	QMNUM
#array_base[257] =	ERKRS
#array_base[258] =	PACCAS
#array_base[259] =	PACCASTY
#array_base[260] =	PLSTAR
#array_base[261] =	PAUFNR
#array_base[262] =	PAUTYP
#array_base[263] =	PPS_POSID
#array_base[264] =	PPS_PSPID
#array_base[265] =	PKDAUF
#array_base[266] =	PKDPOS
#array_base[267] =	PPAOBJNR  
#array_base[268] =	PNPLNR
#array_base[269] =	PNPLNR_VORGN
#array_base[270] =	PPRZNR
#array_base[271] =	PKSTRG
#array_base[272] =	CO_ACCASTY_N1
#array_base[273] =	CO_ACCASTY_N2
#array_base[274] =	CO_ACCASTY_N3
#array_base[275] =	CO_ZLENR
#array_base[276] =	CO_BELNR
#array_base[277] =	CO_BUZEI
#array_base[278] =	CO_BUZEI1
#array_base[279] =	CO_BUZEI2
#array_base[280] =	CO_BUZEI5
#array_base[281] =	CO_BUZEI6
#array_base[282] =	CO_BUZEI7
#array_base[283] =	CO_REFBZ
#array_base[284] =	CO_REFBZ1
#array_base[285] =	CO_REFBZ2
#array_base[286] =	CO_REFBZ5
#array_base[287] =	CO_REFBZ6
#array_base[288] =	CO_REFBZ7
#array_base[289] =	WORK_ITEM_ID
#array_base[290] =	FKART
#array_base[291] =	VKORG
#array_base[292] =	VTWEG
#array_base[293] =	SPART
#array_base[294] =	MATNR_COPA
#array_base[295] =	MATKL
#array_base[296] =	KDGRP
#array_base[297] =	LAND1
#array_base[298] =	BRSCH
#array_base[299] =	BZIRK
#array_base[300] =	KUNRE
#array_base[301] =	KUNWE
#array_base[302] =	KONZS
#array_base[303] =	ACDOC_COPA_EEW_DUMMY_PA
#array_base[304] =	KTGRD_PA
#array_base[305] =	PSTYV_PA
#array_base[306] =	AUART_PA
#array_base[307] =	KTGRM_PA
#array_base[308] =	WWPLT_PA
#array_base[309] =	WWTYV_PA
#array_base[310] =	WWBRD_PA
#array_base[311] =	WWCAT_PA
#array_base[312] =	WWPLE_PA
#array_base[313] =	WWTDC_PA
#array_base[314] =	RE_BUKRS
#array_base[315] =	RE_ACCOUNT
#array_base[316] =	FIKRS
#array_base[317] =	FISTL
#array_base[318] =	MEASURE
#array_base[319] =	RFUND
#array_base[320] =	RGRANT_NBR
#array_base[321] =	RBUDGET_PD
#array_base[322] =	SFUND
#array_base[323] =	SGRANT_NBR
#array_base[324] =	SBUDGET_PD
#array_base[325] =	VNAME
#array_base[326] =	EGRUP
#array_base[327] =	RECID
#array_base[328] =	VPTNR
#array_base[329] =	BTYPE
#array_base[330] =	ETYPE
#array_base[331] =	PRODPER 
#array_base[332] =	SWENR
#array_base[333] =	SGENR
#array_base[334] =	SGRNR
#array_base[335] =	SMENR
#array_base[336] =	RECNNR
#array_base[337] =	SNKSL
#array_base[338] =	SEMPSL
#array_base[339] =	DABRZ   
#array_base[340] =	PSWENR
#array_base[341] =	PSGENR
#array_base[342] =	PSGRNR
#array_base[343] =	PSMENR
#array_base[344] =	PRECNNR
#array_base[345] =	PSNKSL
#array_base[346] =	PSEMPSL
#array_base[347] =	PDABRZ  
#array_base[348] =	ACDOC_EEW_DUMMY
#array_base[349] =	ZAWCPUDT
#array_base[350] =	ZAWCPUTM
#array_base[351] =	ZZORPC
#array_base[352] =	ZZBWART
#array_base[353] =	DUMMY_INCL_EEW_COBL
#array_base[354] =	FUP_ACTION
#array_base[355] =	MIG_SOURCE
#array_base[356] =	MIG_DOCLN
#array_base[357] =	_DATAAGING
#array_base[358] =	BUKRS_SENDER
#array_base[359] =	DOCNR_LD
#array_base[360] =	PREC_AWSYS
#array_base[361] =	SRC_AWTYP
#array_base[362] =	SRC_AWSYS
#array_base[363] =	SRC_AWORG
#array_base[364] =	SRC_AWREF
#array_base[365] =	SRC_AWITEM
#array_base[366] =	SRC_AWSUBIT
#array_base[367] =	XCOMMITMENT
#array_base[368] =	RIUNIT
#array_base[369] =	CO_MEINH
#array_base[370] =	CO_MEGBTR
#array_base[371] =	CO_MEFBTR
#array_base[372] =	ANLKL
#array_base[373] =	KTOGR
#array_base[374] =	PANL1
#array_base[375] =	PANL2
#array_base[376] =	UPRCTR
#array_base[377] =	ARBID   
#array_base[378] =	VORNR
#array_base[379] =	AUFPS
#array_base[380] =	UVORN
#array_base[381] =	EQUNR
#array_base[382] =	TPLNR
#array_base[383] =	ISTRU
#array_base[384] =	ILART
#array_base[385] =	PLKNZ
#array_base[386] =	ARTPR
#array_base[387] =	PRIOK
#array_base[388] =	MAUFNR
#array_base[389] =	MATKL_MM
#array_base[390] =	PLANNED_PARTS_WORK
#array_base[391] =	ZZMPRCTR
#array_base[392] =	ZZLAND1
#array_base[393] =	ZZMMATNR
#array_base[394] =	ZZPROCSRC
#array_base[395] =	ZZRESTID
#array_base[396] =	WWCOP_PA
#array_base[397] =	WWPHP_PA
#array_base[398] =	ZZWERKS
#array_base[399] =	ZZMBUKRS
#array_base[400] =	ZZLICENSEE
#array_base[401] =	ZZLICENSOR
#array_base[402] =	ZZPLSEGMENT
#array_base[403] =	OBS_REASON
#array_base[404] =	BSLALT
#array_base[405] =	CSLALT
#array_base[406] =	DSLALT
#array_base[407] =	ESLALT
#array_base[408] =	FSLALT
#array_base[409] =	GSLALT
#array_base[410] =	BSLEXT
#array_base[411] =	CSLEXT
#array_base[412] =	DSLEXT
#array_base[413] =	ESLEXT
#array_base[414] =	FSLEXT
#array_base[415] =	GSLEXT
#array_base[416] =	COCO_NUM
#array_base[417] =	PS_PRJ_PNR
#array_base[418] =	PPS_PSP_PNR
#array_base[419] =	PPS_PRJ_PNR
#array_base[420] =	DUMMY_MRKT_SGMNT_EEW_PS
#array_base[421] =	BILLM   
#array_base[422] =	POM     
#array_base[423] =	CBRUNID
#array_base[424] =	JVACTIVITY
#array_base[425] =	PVNAME
#array_base[426] =	PEGRUP
#array_base[427] =	S_RECIND
#array_base[428] =	CBRACCT
#array_base[429] =	CBOBJNR
#array_base[430] =	ACROBJTYPE
#array_base[431] =	ACROBJ_ID
#array_base[432] =	ACRSOBJ_ID
#array_base[433] =	ACRITMTYPE
#array_base[434] =	VALOBJTYPE
#array_base[435] =	VALOBJ_ID
#array_base[436] =	VALSOBJ_ID
#array_base[437] =	NETDT   
#array_base[438] =	RISK_CLASS
#array_base[439] =	ZZ1_SLUWID_JEI
#array_base[440] =	ZZLICENSOR_NC
#array_base[441] =	ZZLICENSEE_NC
#array_base[442] =	ZZIMPORT_LOCAL
#array_base[443] =	ZZIPLA_BASE
#array_base[444] =	ZZUS_SEG_MODEL
#array_base[445] =	ZZLOC_SEG_MODEL
#array_base[446] =	ZZUS_PL_SEG
#array_base[447] =	ZZLOC_PL_SEG
#array_base[448] =	ZZEXT_OP_SEG
#array_base[449] =	ZZMRFAREA
#array_base[450] =	CBTTYPE
#array_base[451] =	AWITEM_REV
#array_base[452] =	PREC_BUKRS
#array_base[453] =	PREC_GJAHR
#array_base[454] =	PREC_BELNR
#array_base[455] =	PREC_DOCLN
#array_base[456] =	CLOSING_RUN_ID
#array_base[457] =	ORGL_CHANGE
#array_base[458] =	RGM_OCUR
#array_base[459] =	RMSL_TYPE
#array_base[460] =	GM_OSL
#array_base[461] =	EBELN_LOGSYS
#array_base[462] =	PEROP_BEG
#array_base[463] =	PEROP_END
#array_base[464] =	WWERT   
#array_base[465] =	PRCTR_DRVTN_SOURCE_TYPE
#array_base[466] =	TAX_COUNTRY
#array_base[467] =	VALUT   
#array_base[468] =	INV_MOV_CATEG
#array_base[469] =	UMATNR
#array_base[470] =	VARC_UACCT
#array_base[471] =	SERVICE_DOC_TYPE
#array_base[472] =	SERVICE_DOC_ID
#array_base[473] =	SERVICE_DOC_ITEM_ID
#array_base[474] =	SERVICE_CONTRACT_TYPE
#array_base[475] =	SERVICE_CONTRACT_ID
#array_base[476] =	SERVICE_CONTRACT_ITEM_ID
#array_base[477] =	SOLUTION_ORDER_ID
#array_base[478] =	SOLUTION_ORDER_ITEM_ID
#array_base[479] =	PSERVICE_DOC_TYPE
#array_base[480] =	PSERVICE_DOC_ID
#array_base[481] =	PSERVICE_DOC_ITEM_ID
#array_base[482] =	OVERTIMECAT
#array_base[483] =	PAUFPS
#array_base[484] =	FIPEX
#array_base[485] =	BDGT_ACCOUNT
#array_base[486] =	BDGT_ACCOUNT_COCODE
#array_base[487] =	BDGT_CNSMPN_DATE
#array_base[488] =	BDGT_CNSMPN_PERIOD
#array_base[489] =	BDGT_CNSMPN_YEAR
#array_base[490] =	BDGT_RELEVANT
#array_base[491] =	BDGT_CNSMPN_TYPE
#array_base[492] =	BDGT_CNSMPN_AMOUNT_TYPE
#array_base[493] =	RSPONSORED_PROG
#array_base[494] =	RSPONSORED_CLASS
#array_base[495] =	RBDGT_VLDTY_NBR
#array_base[496] =	KBLNR
#array_base[497] =	KBLPOS
#array_base[498] =	ACRLOGSYS
#array_base[499] =	ACRVALDAT
#array_base[500] =	SDM_VERSION

def dayindate(day_month_year):
	tmp=day_month_year.split('-')
	return tmp[2]

def monthindate(day_month_year):
	tmp=day_month_year.split('-')
	return tmp[1]
def yearindate(day_month_year):
	tmp=day_month_year.split('-')
	return tmp[0]
	
#open input file, dump to array
csv_base=open('Intel_Data_2017.csv','r')
array_base=[]
array_31122017=[]
previous_month=[]
reader2018=csv.reader(csv_base,delimiter=',')
next(reader2018)
for row in reader2018:
	if(row[3] == "2017"):
		array_base.append(row)
csv_base.close()

#Adjust ops per day to achieve target data quantity.  Total entries is 3758 * ops_per_day
ops_per_day=1#minimum 1 will produce 117,707 entries
ops_per_day=1243#1243 will produce approximately 146 million entries.

#Fixed global values
rrcty="0"
src_awitem="0"
rkcur="USD"
rbusa=""
wsl2="0"
wsl3="0"
bstat=""
slalittype="0"
ebelp="0"
zekkn="0"
werks=""
lifnr=""
kunnr=""
fbuda=""
rmvct=""
xreversing=""
subta_rev="0"
xsettling=""
xsettled=""
prec_awtyp=""
prec_aworg=""
prec_awref=""
prec_awitem="0"
prec_subta="0"
prec_awmult="0"
xsecondary=""
rocur=""
rvcur="HKD"
rbcur=""
rccur=""
rdcur=""
recur=""
rfcur=""
rgcur=""
rco_ocur=""
qunit1=""
qunit2=""
qunit3=""
scntr=""
sfarea=""
sbusa=""
rassc=""
osl="0"
bsl="0"
csl="0"
dsl="0"
esl="0"
fsl="0"
gsl="0"
kfsl="0"
kfsl2="0"
kfsl3="0"
psl="0"
psl2="0"
psl3="0"
pfsl="0"
pfsl2="0"
pfsl3="0"
co_osl="0"
hsalk3="0"
ksalk3="0"
osalk3="0"
vsalk3="0"
hsalkv="0"
ksalkv="0"
osalkv="0"
vsalkv="0"
hpvprs="0"
kpvprs="0"
opvprs="0"
vpvprs="0"
hstprs="0"
kstprs="0"
ostpts="0"
vstprs="0"
hslalt="0"
kslalt="0"
oslalt="0"
vslalt="0"
hslext="0"
kslext="0"
oslext="0"
vslext="0"
hvkwrt="0"
hvksal="0"
quant1="0"
quant2="0"
quant3="0"
lokkt="XX00"
ktop2="ALTERNATE"
rebzg=""
rebzj=""
rebzz="0"
rebzt=""
rebest=""
kdauf=""
mwskz=""
ostprs="0"
hkvwrt="0"
rbest=""

#Globals
#Global arrays are indexed to rburks [1710,1720,1730,1740,1750,342]
belnr=[2000000000,2000000000,2000000000,2000000000,2000000000,2000000000]
docln=[1,1,1,1,1,1]
awref_sd00=90000000
awref_rfbu=100000000
awref_rmwa_rmwl=4900000000
awitem=0
buzei=0
monthout=[]
#dates
months_numerical=\
["2017-12-31","2018-01-31","2018-02-28","2018-03-31","2018-04-30","2018-05-31","2018-06-30","2018-07-31","2018-08-31","2018-09-30","2018-10-31","2018-11-30","2018-12-31"]




#possible strings for sgtxt
sgtxt_array=\
["COGS","Interest Income - Subs","Interest Expense - Subs","Cost of Goods Sold (Trade w/o Cost Element)","Payroll - Bonus","Payroll - Vacation Pay Salaries","Payroll - Overtime Wages","Payroll - Disability Pay (AU)",\
"Payroll-Medical insurance","Workers' Compensation Association Contributions","Payroll Expense - Direct Labor Cost","Payroll Expense - Indirect Labor Cost","Payroll Expense - Tax and Soc Security - Wages",\
"Payroll Expense - Tax and Soc Security - Salaries","Sales Commissions","Advertising and Sales Costs","Computer Supplies","Office/Building Rent","Depr expense (Bk < Tax) - Exceptional depr",\
"Depr expense (Bk > Tax) - Exceptional depr","Training and Education","Insurance","IC Exp","Interest Expense - Subsidiaries","Interest Income","Interest Expense","Other Taxes on Income","Property Taxes","Trade Tax",\
"Payables affiliated Companies","Receivables Affiliated companies","Sales","Inventory","Notes Reivable from Affiliates","Bank1 Check In","Notes Payables affiliated Companies","Bank1 Main Account","Bank 1 - Bank (Main) Account",\
"Bank 1 - Checks In","Bank 1 - Check Clearing Account","Short Term Investments","Receivables Domestic","Accounts Receivable - BoE Receivable","Other Receivables Adjustments","Other Receivables (no recon acct)",\
"Inventory - Revaluation Semi Finished Goods","Land & Land Improvements","Buildings","Office Equipment","Furniture and Fixtures","Accumulated Depreciation - Office Equipment","Accumulated Depreciation - Furniture and Fixtures",\
"Other Long Term Investments","Loans Other - Long Term","Accounts Payable - BoE Payable","Accrued Net Payroll","Payroll Taxes","Vacation Accrual (BR)","Sales Tax Accrued (MW1) - State","Loans from Banks (no recon acct)",\
"Tax Provisions","Pension Provision","Corporate Income Tax Provision","Provision for Other Income and Revenue Tax","Common Stock","Retained Earnings","Revenue Domestic - Product","Revenue Foreign - Product"]

#fiscal_years=[["2018","2017-12-31","2018-12-29"],["2019","2018-12-30","2019-12-28"],["2020","2019-12-29","2020-12-26"],["2021","2020-12-27","2021-12-26"]]

for lastday in months_numerical:
	#handle first month where we need to read from the CSV input
	if(months_numerical.index(lastday)==0):
		for entry in array_base:
			shouldbe99=len(entry)
			tmp=[]
			if(entry[62] == "12/31/2017"):
				for i in range(0,shouldbe99):
					tmp.append(entry[i])
				array_31122017.append(tmp)		
	else:
		awitem=0
		endofmonth=int(dayindate(lastday))
		month=monthindate(lastday).zfill(2)
		year=yearindate(lastday)
		fname="zacdoca_load_file"+"_"+month+"_"+year+".csv"
		of=open(fname,'a',newline='',buffering=131072)
		for i in range(1,endofmonth+1):
			today=year+"-"+month+"-"+str(i).zfill(2)
			print(today)
			monthout=[]
			for j in range(0,ops_per_day):
				if(j %100 == 0):
					print("  Pass: " + str(j) + " of: " + str(ops_per_day))
				for entry in array_31122017:
					rvalbase=random.random()
					rand_0or1=round(1*rvalbase)
					rand_1to3=round(2*rvalbase)+1
					rand_0to7=round(7*rvalbase)
					rand_0to10=round(10*rvalbase)
					rand_0to24=round(24*rvalbase)
					rand_0to67=round(67*rvalbase)
					rand_1to100=round(99*rvalbase)+1
					shouldbe99=len(entry)
					indexofrburks=0
					tmp=[]
					
					vorgn=""
					bttype=""
					awtyype=""
					awtyp_rev=""
					subta=""
					rcntr=""
					xreversed=""
					xtruerev=""
					runit=""
					rvunit=""
					rrunit=""
					co_meinh=""
					msl=""
					mfsl=""
					vmsl=""
					vmfsl=""
					rmsl=""
					co_megbtr=""
					co_mefbtr=""
					prctr=""
					pprctr=""
					sign=1
					budat=""
					poper=""
					#RCLNT
					rclnt=entry[0]
					tmp.append(rclnt)#0
					#RLDNR
					rldnr=entry[1]
					tmp.append(rldnr)#1
					tmp.append(entry[2])#rburks
					if(entry[2]=="1710"):
						indexofrburks=0
					elif(entry[2]=="1720"):
						indexofrburks=1
					elif(entry[2]=="1730"):
						indexofrburks=2
					elif(entry[2]=="1740"):
						indexofrburks=3
					elif(entry[2]=="1750"):
						indexofrburks=4
					elif(entry[2]=="342"):
						indexofrburks=5
					else:
						indexofrburks=42
					tmp.append(year)#gjahr
					tmp.append(f'{(belnr[indexofrburks])}'.zfill(10))#belnr
					tmp.append(f'{(docln[indexofrburks])}'.zfill(6))#docln
					tmp.append(year)#ryear same as gjahr
					tmp.append(rrcty)#rrcty
					#RMVCT always appears to be empty string.
					tmp.append(rmvct)
					#VORGN requires making a decision
					if(entry[8] == "RMWL" or entry[8] == "RMWA"):
						vorgn=entry[8]
						bttype=vorgn
						awtype="MKPF"
					elif(entry[8] == "RFBU"):
						vorgn=entry[8]
						bttype=vorgn
						if(rand_0to10 <= 3):
							awtype="BKPFF"
						elif(rand_0to10 <= 6):
							awtype="BKPF"
						elif(rand_0to10 <= 7):
							awtype="PRC5"
						elif(rand_0to10 <= 9):
							awtype="PCAD"
					else:
						vorgn="ERROR"
						bttype="ERROR"
					tmp.append(vorgn)
					#VRGNG requires making a decision
					if(entry[9] == "COIN"):
						subta=entry[14]
						rcntr=entry[34]
					else:
						subta=0
						if(rand_0or1 == 0):
							rcntr=""
						else:
							rcntr=entry[34]
					tmp.append(entry[9])
					#index 11 BTTYPE was handled by VORGN processing
					tmp.append(bttype)
					#index 12 AWTYPE was handled by VORGN processing
					tmp.append(awtype)
					#randomly select AWSYS for rclnt=400 cases, else empty string
					awsys="error"
					if(rclnt=="400"):
						if(rand_0or1 ==0):
							awsys="GBP480"
						else:
							awsys="G4P470"
					else:
						awsys=""
					tmp.append(awsys)
					#AWORG requires concatenating rburks and gjahr
					aworg=entry[2]+year
					aworg_rev=aworg
					tmp.append(aworg)
					#AWREF requires making a decision
					if(bttype=="SD00"):
						awref=awref_sd00
						awref_sd00+=1
					elif(bttype=="RFBU"):
						if(rclnt=="400"):
							awref="PE_TOTALS"
						else:
							awref=awref_rfbu
							awref_rfbu+=1
					elif(bttype=="RMWA" or bttype=="RMWL"):
						awref=awref_rmwa_rmwl
						awref_rmwa_rmwl+=1
					else:
						print("Problem with assignment of AWREF!")
						print(entry)
						print(bttype)
						print(rclnt)
						exit(-1)
					tmp.append(awref)
					#AWITEM can repeat and can only exist in certain ranges.
					tmp.append(awitem)
					awitem+=1
					if(awitem>1381):
						awitem=0
					if(awitem > 252 and awitem < 1001):
						awitem=1001
					#AWITGRP requires making a decision
					if(vorgn == "RWMA" or vorgn == "RMWL"):
						awitgrp=1
					else:
						awitgrp=0
					tmp.append(awitgrp)
					#SUBTA was handled by VRGNG processing
					tmp.append(subta)
					#XREVERSING always appears to be empty string.
					tmp.append(xreversing)
					#XREVERSED should have approximately 1% = X
					if(rand_1to100 == 42):
						xreversed="X"
					else:
						xreversed=""
					tmp.append(xreversed)
					#XTRUEREV should have approximately 1% = X
					if(rand_1to100 == 24):
						xtruerev = "X"
					else:
						xtruerev=""
					tmp.append(xtruerev)
					#Need to check if both XREVERSED and TRUEREV are X.  If both are, clear out a bunch of vars.
					if(xreversed =="X" and xtruerev=="X"):
						runit=""
						rvunit=""
						rrunit=""
						co_meinh=""
						msl=""
						mfsl=""
						vmsl=""
						vmfsl=""
						rmsl=""
						co_megbtr=""
						co_mefbtr=""
					#awtyp_rev is the same as awtype, except when awtyp== PCAD or PRC5
					if(awtype == "PCAD" or awtype =="PRC5"):
						awtyp_rev=""
					else:
						awtyp_rev=awtype
					tmp.append(awtyp_rev)
					#aworg_rev is the same as aworg
					tmp.append(aworg_rev)
					#awref_rev is only set if xtruerev is X.  If xtruerev is X, then awref_rev is equal to the previous belnr of this rburks
					if(xtruerev=="X"):
						awref_rev=(belnr[indexofrburks]-1)
					else:
						awref_rev=""
					tmp.append(awref_rev)
					#SUBTA_REV appears to always be 0
					tmp.append(subta_rev)
					#XSETTLING appears to always be empty string.
					tmp.append(xsettling)
					#XSETTLED appears to always be empty string.
					tmp.append(xsettled)
					#PREC_AWTYP appears to always be empty string.
					tmp.append(prec_awtyp)
					#PREC_AWORG appears to always be empty string.
					tmp.append(prec_aworg)
					#PREC_AWREF appears to always be empty string.
					tmp.append(prec_awref)
					#PREC_AWITEM appears to always be zero.
					tmp.append(prec_awitem)
					#PREC_SUBTA appears to always be zero.
					tmp.append(prec_subta)
					#PREC_AWMULT appears to always be zero.
					tmp.append(prec_awmult)
					#XSECONDARY appers to always be empty string.
					tmp.append(xsecondary)
					#Allegedly rtcur doesn't really matter.  if indexofrburks is 0,1, or 2 then USD.  If 3 then CAD.  If 4 then EUR. If 5 then HKD.
					if(indexofrburks==3):
						rtcur="CAD"
					elif(indexofrburks==4):
						rtcur="EUR"
					elif(indexofrburks==5):
						rtcur="HKD"
					else:
						rtcur="USD"
					tmp.append(rtcur)	
					#RWCUR is the set identically to rtcur
					rwcur=rtcur
					tmp.append(rwcur)	
					#RHCUR is typically USD.  If rburks is 1730 then RHCUR=EUR.  If rburks is 1740, then RHCUR=CAD if rburks is 342, then rhcur is HKD
					if(indexofrburks==2):
						rhcur="EUR"
					elif(indexofrburks==3):
						rhcur="CAD"
					elif(indexofrburks==5):
						rhcur="HKD"
					else:
						rhcur="USD"
					tmp.append(rhcur)
					#RKCUR is always USD
					tmp.append(rkcur)
					#ROCUR appears to always be empty string.
					tmp.append(rocur)
					#RVCUR is always HKD
					tmp.append(rvcur)
					#RBCUR appears to always be empty string.
					tmp.append(rbcur)
					#RCCUR appears to always be empty string.
					tmp.append(rccur)
					#RDCUR appears to always be empty string.
					tmp.append(rdcur)
					#RECUR appears to always be empty string.
					tmp.append(recur)
					#RFCUR appears to always be empty string.
					tmp.append(rfcur)
					#RGCUR appears to always be empty string.
					tmp.append(rgcur)
					#RCO_OCUR appears to always be empty string.
					tmp.append(rco_ocur)
					#RUNIT always appears to be empty string.
					tmp.append(runit)
					#RVUNIT always appears to be empty string.
					tmp.append(rvunit)
					#RRUNIT always appears to be empty string.
					tmp.append(rrunit)
					#QUNIT1 always appears to be empty string.
					tmp.append(qunit1)
					#QUNIT2 always appears to be empty string.
					tmp.append(qunit2)
					#QUNIT3 always appears to be empty string.
					tmp.append(qunit3)
					#No guidance provided for RACCT.  Select based on initial dataset
					tmp.append(entry[33])
					#No guidance provided for RCNTR.  Select based on initial dataset
					tmp.append(entry[34])
					#No guidance provided for PRCTR.  Select based on initial dataset
					prctr=entry[35]
					tmp.append(prctr)
					#No guidance provided for RFAREA.  Select based on initial dataset
					tmp.append(entry[36])
					#RBUSA is a fixed value of empty string.
					tmp.append(rbusa)
					#KOKRS is either AA00 or XX00
					kokrs=""
					if(indexofrburks==5):
						kokrs="XX00"
					else:
						kokrs="A000"
					tmp.append(kokrs)
					#A decision is required for segment
					segment=""
					if(prctr=="PC0001" or prctr=="PC0002" or prctr=="PC0003"):
						segment="SE0001"
					elif(prctr=="PC0004"):
						segment="SE0002"
					elif(prctr=="PC0005"):
						segment="SE0003"
					elif(prctr=="PPC_0001" or prctr=="1DDEFAULT"):
						segment=""
					elif(prctr=="YB10"):
						segment="1000_A"
					elif(prctr=="YB900"):
						segment="1000_C"
					else:
						if(rand_1to3 ==1):
							segment="SE0002"
						elif(rand_1to3 ==2):
							segment="SE0003"
						else:
							segment="SE001"
					tmp.append(segment)
					#SCNTR appears to always be empty string.
					tmp.append(scntr)
					#PPRCTR always appears to be empty string.
					tmp.append(pprctr)
					#SFAREA always appears to be empty string.
					tmp.append(sfarea)
					#SBUSA always appears to be empty string.
					tmp.append(sbusa)
					#RASSC always appears to be empty string.
					tmp.append(rassc)
					#No guidance provided for PSEGMENT.  Select based on initial dataset.
					tmp.append(entry[41])
					#TSL will be Pos or negative number, psuedorandomly generated relative to prior value.  Keep track of sign for MSL assignment later on
					sign=1
					if(rand_0or1==1):
						sign=(-1)
					tmp_e=(entry[42]).translate({ord(k):None for k in '.'}).replace(',','.')
					tsl=float(tmp_e)*(1+rvalbase/10)*sign
					if(tsl<0):
						sign=(-1)
					else:
						sign=1
					tmp.append(tsl)
					#WSL is TSL.
					tmp.append(tsl)
					#WSL2 is fixed to "0"
					tmp.append(wsl2)
					#WSL3 is fixed to "0"
					tmp.append(wsl3)
					#HSL is TSL
					tmp.append(tsl)
					#KSL is TSL unless indexofrburks==5
					ksl="0"
					if(indexofrburks==5):
						ksl="0"
					else:
						ksl=tsl
					tmp.append(ksl)
					#OSL appears to always be 0.
					tmp.append(osl)
					#VSL appears to be TSL
					vsl=tsl
					tmp.append(vsl)
					#BSL appears to always be 0.
					tmp.append(bsl)
					#CSL appears to always be 0.
					tmp.append(csl)
					#DSL appears to always be 0.
					tmp.append(dsl)
					#ESL appears to always be 0.
					tmp.append(esl)
					#FSL appears to always be 0.
					tmp.append(fsl)
					#GSL appears to always be 0.
					tmp.append(gsl)
					#KFSL appears to always be 0.
					tmp.append(kfsl)
					#KFSL2 appears to always be 0.
					tmp.append(kfsl2)
					#KFSL3 appears to always be 0.
					tmp.append(kfsl3)
					#PSL appears to always be 0.
					tmp.append(psl)
					#PSL2 appears to always be 0.
					tmp.append(psl2)
					#PSL3 appears to always be 0.
					tmp.append(psl3)
					#PFSL appears to always be 0.
					tmp.append(pfsl)
					#PFSL2 appears to always be 0.
					tmp.append(pfsl2)
					#PFSL3 appears to always be 0.
					tmp.append(pfsl3)
					#CO_OSL appears to always be 0.
					tmp.append(co_osl)
					#No guidance provided for HSALK3.  Always appears to be 0
					tmp.append(hsalk3)
					#No guidance provided for KSALK3.  Always appears to be 0
					tmp.append(ksalk3)
					#OSALK3 appears to always be 0.
					tmp.append(osalk3)
					#VSALK3 appears to always be 0.
					tmp.append(vsalk3)
					#HSALKV appears to always be 0.
					tmp.append(hsalkv)
					#KSALKV appears to always be 0.
					tmp.append(ksalkv)
					#OSALKV appears to always be 0.
					tmp.append(osalkv)
					#VSALKV appears to always be 0.
					tmp.append(vsalkv)
					#HPVPRS appears to always be 0.
					tmp.append(hpvprs)
					#KPVPRS appears to always be 0.
					tmp.append(kpvprs)
					#OPVPRS appears to always be 0.
					tmp.append(opvprs)
					#VPVPRS appears to always be 0.
					tmp.append(vpvprs)
					#HSTPRS appears to always be 0.
					tmp.append(hstprs)
					#KSTPRS appears to always be 0.
					tmp.append(kstprs)
					#OSTPRS appears to always be 0.
					tmp.append(ostprs)
					#VSTPRS appears to always be 0.
					tmp.append(vstprs)
					#HSLALT appears to always be 0.
					tmp.append(hslalt)
					#KSLALT appears to always be 0.
					tmp.append(kslalt)
					#OSLALT appears to always be 0.
					tmp.append(oslalt)
					#VSLALT appears to always be 0.
					tmp.append(vslalt)
					#HSLEXT appears to always be 0.
					tmp.append(hslext)
					#KSLEXT appears to always be 0.
					tmp.append(kslext)
					#OSLEXT appears to always be 0.
					tmp.append(oslext)
					#VSLEXT appears to always be 0.
					tmp.append(vslext)
					#HVKWRT appears to always be 0.
					tmp.append(hkvwrt)
					#HVKSAL appears to always be 0.
					tmp.append(hvksal)
					#Assign MSL based on sign var from above.  If new data set, set to 0, else: Use random 0/1 to select 200 vs 1
					msl=""
					if(indexofrburks==5):
						msl="0"
					elif(sign==1):
						if(rand_0or1==0):
							msl="200"
						else:
							msl="1"
					elif(sign==(-1)):
						if(rand_0or1==0):
							msl="-200"
						else:
							msl="-1"
					else:
						msl=""
					tmp.append(msl)
					#A decision is required for MFSL.
					if(msl=="" or msl=="-200"):
						mfsl=""
					elif(msl=="200" or msl=="-1" or msl=="1" or msl=="0"):
						mfsl="0"
					else:
						mfsl=""
					tmp.append(mfsl)
					#A decision is required for VMSL
					if(msl=="" or msl=="-200"):
						vmsl=""
					else:
						vmsl=msl
					tmp.append(vmsl)
					#A decision is required for VMFSL
					if(msl=="" or msl=="-200"):
						vmfsl=""
					else:
						vmfsl="0"
					tmp.append(vmfsl)
					#A decision is required for RMSL
					if(msl=="" or msl=="-200"):
						rmsl=""
					elif(msl=="200"):
						rmsl="200"
					elif(msl=="0"):
						rmsl="0"
					else:
						rmsl="-1"
					tmp.append(rmsl)
					#QUANT1 appears to always be 0.
					tmp.append(quant1)
					#QUANT2 appears to always be 0.
					tmp.append(quant2)
					#QUANT3 appears to always be 0.
					tmp.append(quant3)
					#if in new data set, set to 0. else empty string
					lbkum=""
					if(indexofrburks==5):
						lbkum="0"
					tmp.append(lbkum)
					#DRCRK is based on SIGN.  H if -1, S if +1
					drcrk=""
					if(sign==1):
						drcrk="S"
					elif(sign==-1):
						drcrk="H"
					else:
						drcrk="ERROR"
					tmp.append(drcrk)
					#POPER is the month.
					tmp.append(month)
					#if old dataset, K4.  If new dataset, PG
					periv="K4"
					if(indexofrburks==5):
						periv="PG"
					tmp.append(periv)
					#fiscyearperiod is determined by concatenating the year from BUDAT, a zero, and the month from POPER
					#Generally speaking fiscal year and year will be equal except for some days in december.  In those cases fyear will be year+1
					day=i
					fyear=""
					if(month=="12"):
						if(year=="2018" and day>=30):
							fyear="2019"
						elif(year=="2019" and day>=28):
							fyear="2020"
						elif(year=="2020" and day>=27):
							fyear="2021"
					else:
						fyear=year
					budat=today
					poper=month
					fiscyearperiod=fyear+"0"+month
					tmp.append(fiscyearperiod)
					#BUDAT was assigned previously
					tmp.append(budat)
					#BLDAT can be budat or may have occurred previously.
					bldat=""
					offset=0
					if(month=="12"):
						if(year=="2018" and day>=30):
							offset=0
						elif(year=="2019" and day>=28):
							offset=0
						elif(year=="2020" and day>=27):
							offset=0
						else:
							offset=0
							if(rand_1to100>=90):
								offset=rand_1to3
					day=i-offset
					bldat=year+"-"+month+"-"+str(day).zfill(2)
					tmp.append(bldat)
					#Randomly select BLART
					blart=""
					if(rand_0to7<=1):
						blart="AB"
					elif(rand_0to7<=3):
						blart="SA"
					elif(rand_0to7<=5):
						blart="SU"
					elif(rand_0to7<=7):
						blart="Y9"
					else:
						blart="ERROR"
					tmp.append(blart)
					#buzei varies 0-381
					tmp.append(buzei)
					buzei+=1
					if(buzei>381):
						buzei=0
					#ZUONR is set based off of either RCNTR or BUDAT with no apparent pattern or guidance provided.
					zuonr=""
					#Half of the time, choose RCNTR
					if(rand_0or1==0):
						zuonr=entry[34]
					else:
						zuonr=year+month+str(i)
					tmp.append(zuonr)
					#Select BSCHL randomly from 1,12,40,50,81,89,91,99
					bschl=""
					if(rand_0to7==0):
						bschl="1"
					elif(rand_0to7==1):
						bschl="12"
					elif(rand_0to7==2):
						bschl="40"
					elif(rand_0to7==3):
						bschl="50"
					elif(rand_0to7==4):
						bschl="81"
					elif(rand_0to7==5):
						bschl="89"
					elif(rand_0to7==6):
						bschl="91"
					elif(rand_0to7==7):
						bschl="99"
					else:
						bschl="ERROR"
					tmp.append(bschl)
					#BSTAT appears to always be empty string.
					tmp.append(bstat)
					#LINETYPE is randomly selected from 1000,1001,1100,2000,3000,4000,5100,6000,7000,20000,30000 or empty string
					linetype=""
					ktosl=""
					if(indexofrburks==5):
						linetype=""
						ktosl=""
					elif(rand_0to10==0):
						linetype="1000"
						if(rand_0or1==0):
							ktosl="GBB"
						else:
							ktosl=""
					elif(rand_0to10==1):
						linetype="1001"
						ktosl="0"
					elif(rand_0to10==2):
						linetype="1100"
						ktosl="BUV"
					elif(rand_0to10==3):
						linetype="2000"
						ktosl=""
					elif(rand_0to10==4):
						linetype="3000"
						ktosl=""
					elif(rand_0to10==5):
						linetype="4000"
						ktosl=""
					elif(rand_0to10==6):
						linetype="5100"
						if(rand_0or1==0):
							ktosl="MW1"
						else:
							ktosl=""
					elif(rand_0to10==7):
						linetype="6000"
						if(rand_1to3==1):
							ktosl="BSX"
						elif(rand_1to3==2):
							ktosl="GBB"
						else:
							ktosl=""
					elif(rand_0to10==8):
						linetype="7000"
						ktosl=""
					elif(rand_0to10==9):
						linetype="20000"
						ktosl=""
					elif(rand_0to10==10):
						linetype="30000"
						ktosl=""
					else:
						linetype="ERROR"
					tmp.append(linetype)
					#A decision is required for KTOSL,selected based on linetype (above).
					tmp.append(ktosl)
					#SLALITTYPE is a fixed value.
					tmp.append(slalittype)
					#XSPLITMOD can be empty string or X.  No guidance provided.
					xsplitmod=""
					if(rand_0to10>=9):
						xsplitmod="X"
					tmp.append(xsplitmod)
					#Username is randomly selected from AUNAME,AUNAME2,BUNAME,CUNAME,DUNAME,EUNAME,EUNAME2,FUNAME
					usname=""
					if(rand_0to7==0):
						usname="AUNAME"
					elif(rand_0to7==1):
						usname="AUNAME2"
					elif(rand_0to7==2):
						usname="BUNAME"
					elif(rand_0to7==3):
						usname="CUNAME"
					elif(rand_0to7==4):
						usname="DUNAME"
					elif(rand_0to7==5):
						usname="EUNAME"
					elif(rand_0to7==6):
						usname="EUNAME2"
					elif(rand_0to7==7):
						usname="FUNAME"
					else:
						usname="ERROR"
					tmp.append(usname)
					#No guidance provided for TIMESTAMP
					timestamp="20.200.603.111.606"
					tmp.append(timestamp)
					#Select EPRCTR randomly from list of possible values
					array_eprctr=["751","757","933","939","11","17","34","39","59","109","118","135","140","144","118","148","208","329","444","454","652","714","722","732","739"]
					eprctr=array_eprctr[rand_0to24]
					tmp.append(eprctr)
					#No guidance is provided for RHOART.  Can be 2,35, or 1, "". Appears to be related to GLACCOUNT_TYPE
					rhoart=""
					glaccount_type=""
					if(rand_1to100<70):
						rhoart="2"
						glaccount_type="P"
					elif(rand_1to100<=80):
						rhoart="35"
						glaccount_type="X"
					elif(rand_1to100<=90):
						rhoart="1"
						glaccount_type="N"
					elif(rand_1to100<=100):
						rhoart=""
						glaccount_type="35"
					else:
						rhoart="ERROR"
						glaccount_type="ERROR"
					tmp.append(rhoart)
					#No guidance provided for GLACCOUNT_TYPE.  See above.
					tmp.append(glaccount_type)
					#Old dataset uses "YCOA", new dataset uses X
					ktopl=""
					if(indexofrburks==5):
						ktopl="X"
					else:
						ktopl="YCOA"
					tmp.append(ktopl)
					#LOKKT appears to always be XX00
					tmp.append(lokkt)
					#KTOP2 appears to always be ALTERNATE
					tmp.append(ktop2)
					#REBZG appears to always be empty string
					tmp.append(rebzg)
					#REBZJ appears to always be empty string
					tmp.append(rebzj)
					#REBZZ appears to always be zero
					tmp.append(rebzz)
					#REBZT appears to always be zero
					tmp.append(rebzt)
					#RBEST appears to always be empty string
					tmp.append(rbest)
					#EBELN appears to always be "" unless in new dataset
					if(indexofrburks==5):
						ebeln="0"
					else:
						ebeln=""
					tmp.append(ebeln)
					#EBELP appears to always be 0 unless in new dataset
					if(indexofrburks==5):
						ebelp=""
					else:
						ebelp="0"
					tmp.append(ebelp)
					#ZEKKN appears to always be 0.
					tmp.append(zekkn)
					#No guidance provided for SGTXT.  Empty string approximatle 97% of the time for all cases except those in new dataset.  Choose randomly from: sgtxt_array
					sgtxt="ERROR"
					if(indexofrburks==5):
						sgtxt=""
					elif(rand_1to100>=97):
						sgtxt=sgtxt_array[rand_0to67]
					else:
						sgtxt=""
					tmp.append(sgtxt)
					#No guidance provided for KDAUF.  Appears to always be empty string.
					tmp.append(kdauf)
					#No guidance provided for KDPOS.  Appears to always be zero unless in new dataset
					kdpos="0"
					if(indexofrburks==5):
						kdpos=""
					tmp.append(kdpos)
					#MATNR is empty string unless in new dataset
					matnr=""
					if(indexofrburks==5):
						matnr="0"
					tmp.append(matnr)
					#WERKS appears to always be empty string.
					tmp.append(werks)
					#LIFNR appears to always be empty string.
					tmp.append(lifnr)
					#KUNNR appears to always be empty string.
					tmp.append(kunnr)
					#FBUDA appears to always be empty string.
					tmp.append(fbuda)
					#No guidance for KOART.  is "S" unless in new dataset.
					koart="S"
					if(indexofrburks==5):
						koart="0"
					tmp.append(koart)
					#UMSKZ is empty string unless in new dataset.
					umskz=""
					if(indexofrburks==5):
						umskz="S"
					tmp.append(umskz)
					#No guidance for MWSKZ.  Appears to always be empty string.
					tmp.append(mwskz)
					
					#HBKID,HKTID,XOPVW,AUGDT appear to always be empty string.
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					#AUGBL appears to always be 0
					tmp.append("0")
					#AUGGJ appears to always be empty string
					tmp.append("")
					#AFABE, ANLN1 appear to always be 0.
					tmp.append("0")
					tmp.append("0")
					#ANLN2,BZDAT appears to always be empty string.
					tmp.append("")
					tmp.append("")
					#ANBWA appears to always be 0.
					tmp.append("0")
					#MOVCAT,DEPR_PERIOD appear to always be empty string.
					tmp.append("")
					tmp.append("")
					#ANLGR appears to always be 0.
					tmp.append("0")
					#ANLGR2 appears to awlays be empty string.
					tmp.append("")
					#SETTLEMENT_RULE appears to always be empty string
					tmp.append("")
					#UBZDT_PN,XVABG_PN appear to always be 0.
					tmp.append("0")
					tmp.append("0")
					#PROZS_PN appears to always be empty string
					tmp.append("")
					#XMANPROPVAL_PN appears to always be 0
					tmp.append("0")
					#KALNR appears to always be empty string
					tmp.append("")
					#VPRSV appears to always be emptry string unless in new dataset.
					vprsv=""
					if(indexofrburks==5):
						vprsv="0"
					tmp.append(vprsv)
					#MLAST,KZBWS,XOBEW,SOBKZ,VTSTAMP appear to always be empty string.
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					#MAT_KDAUF appears to always be 0.
					tmp.append("0")
					#MAT_KDPOS appears to always be empty string
					tmp.append("")
					#MAT_PSPNR,MAT_PS_POSID appear to always be 0.
					tmp.append("0")
					tmp.append("0")
					#MAT_LIFNR,BWTAR,BWKEY,HPEIUNH appear to always be empty string
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					#KPEINH,OPEINH,VPEINH,MLPTYP appear to always be 0.
					tmp.append("0")
					tmp.append("0")
					tmp.append("0")
					tmp.append("0")
					#MLCATEG,QSBVALT appear to always be empty string.
					tmp.append("")
					tmp.append("")
					#QSPROCESS,PERART appear to always be 0.
					tmp.append("0")
					tmp.append("0")
					#MLPOSNR appears to always be empty string.
					tmp.append("")
					#RACCT_SENDER appears to always be 0.
					tmp.append("0")
					#ACCAS_SENDER,ACCASTY_SENDER,OBJNR,HRKFT,HKDRP,PAROB1,PAROBSRC,USPOB,CO_BELKZ appear to always be empty string.
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					#BELTP,MUVFLG appear to always be 0.
					tmp.append("0")
					tmp.append("0")
					#GKONT seems to always be 19990920
					tmp.append("19990920")
					#GKOAR appears to always be S
					tmp.append("S")
					#ERLKZ appears to always be empty string
					tmp.append("")
					#PERNR,PAOBJNR appear to always be 0
					tmp.append("0")
					tmp.append("0")
					#XPAOBJNR_CO_REL,SCOPE,LOGSYSO,PBUKRS,PSCOPE,LOGSYSP,BWSTRAT,OBJNR_HK,AUFNR_ORG,UKOSTL,ULSTAR,UPRZNR,ACCAS,ACCASTY,LSTAR,AUFNR appear to always be empty string.
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					#AUTYP,PS_PSP_PNR appear to always be 0.
					tmp.append("0")
					tmp.append("0")
					#PS_POSID,PS_PSPID,NPLNR,NPLNR_VORGN,PRZNR,KSTRG,BEMOT,RSRCE,QMNUM,ERKRS,PACCAS,PACCASTY,PLSTAR,PAUFNR appear to always be empty string.
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					#PAUTYP appears to always be 0.
					tmp.append("0")
					#PPS_POSID,PPS_PSPID,PKDAUF appear to always be empty string.
					tmp.append("")
					tmp.append("")
					tmp.append("")
					#PKDPOS,PPAOBJNR appear to always be 0.
					tmp.append("0")
					tmp.append("0")
					#PNPLNR,PNPLNR_VORGN,PPRZNR,PKSTRG,CO_ACCASTY_N1,CO_ACCASTY_N2,CO_ACCASTY_N3 appear to always be empty string.
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					#CO_ZLENR appears to always be 0.
					tmp.append("0")
					#CO_BELNR appears to always be empty string.
					tmp.append("")
					#CO_BUZEI,CO_BUZEI1,CO_BUZEI2,CO_BUZEI5,CO_BUZEI6,CO_BUZEI7,CO_REFBZ,CO_REFBZ1,CO_REFBZ2,CO_REFBZ5,CO_REFBZ6,CO_REFBZ7 appear to always be 0.
					tmp.append("0")
					tmp.append("0")
					tmp.append("0")
					tmp.append("0")
					tmp.append("0")
					tmp.append("0")
					tmp.append("0")
					tmp.append("0")
					tmp.append("0")
					tmp.append("0")
					tmp.append("0")
					tmp.append("0")
					#WORK_ITEM_ID,FKART,VKORG,VTWEG,SPART,MATNR_COPA,MATKL,KDGRP,LAND1,BRSCH,BZIRK,KUNRE,KUNWE,KONZS,ACDOC_COPA_EEW_DUMMY_PA,KTGRD_PA,PSTYV_PA,AUART_PA,KTGRM_PA,WWPLT_PA,WWTYV_PA,WWBRD_PA
					#WWCAT_PA,WWPLE_PA,WWTDC_PA,RE_BUKRS,RE_ACCOUNT,FIKRS,FISTL,MEASURE,RFUND,RGRANT_NBR,RBUDGET_PD,SFUND,SGRANT_NBR,SBUDGET_PD,VNAME,EGRUP,RECID,VPTNR,BTYPE,ETYPE appear to always be empty string
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					#PRODPER appears to always be 0.
					tmp.append("0")
					#SWENR,SGENR,SGRNR,SMENR,RECNNR,SNKSL,SEMPSL appear to always be empty string.
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					#DABRZ appears to always be 0.
					tmp.append("0")
					#PSWENR,PSGENR,PSGRNR,PSMENR,PRECNNR,PSNKSL,PSEMPSL
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					#PDABRZ appears to always be 0.
					tmp.append("0")
					#ACDOC_EEW_DUMMY appears always be empty string
					tmp.append("")
					#ZAWCPUDT is the same as BUDAT
					zawcpudt=budat
					tmp.append(zawcpudt)
					#ZAWCPUTM appears to always be 1111000
					tmp.append("1111000")
					#ZZORPC,ZZBWART,DUMMY_INCL_EEW_COBL,FUP_ACTION,MIG_SOURCE,MIG_DOCLN appear to always be empty string.
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					#_DATAAGING appears to always be 0.
					tmp.append("0")
					#BUKRS_SENDER appears to be the same as RBUKRS
					bukrs_sender=entry[2]
					tmp.append(bukrs_sender)
					#DOCNR_LD,PREC_AWSYS,SRC_AWTYP,SRC_AWSYS,SRC_AWORG,SRC_AWREF appears to always be empty string.
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					#SRC_AWITEM appears to always be 0
					tmp.append(src_awitem)
					#SRC_AWSUBIT appears to always be 0.
					tmp.append("0")
					#XCOMMITMENT,RIUNIT appear to always be empty string.
					tmp.append("")
					tmp.append("")
					
					#CO_MEINH always appears to be empty string.
					tmp.append(co_meinh)	
					#No guidance provided for CO_MEGBTR.  Select randomly
					if(indexofrburks==5):
						co_megbtr="0"
					elif(rand_1to3 == 1):
						co_megbtr="1"
					elif(rand_1to3==2):
						co_megbtr="-1"
					else:
						co_megbtr=""
					tmp.append(co_megbtr)
					#No guidance provided for CO_MEFBTR.  Select randomly
					if(rand_0or1==0):
						co_mefbtr="0"
					else:
						co_mefbtr=""
					tmp.append(co_mefbtr)
					
					#ANLKL,KTOGR,PANL1,PANL2,UPRCTR appear to always be empty string.
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					#ARBID appears to always be 0.
					tmp.append("0")
					#VORNR appears to always be empty string.
					tmp.append("")
					#AUFPS appears to always be 0.
					tmp.append("0")
					#UVORN,EQUNR,TPLNR,ISTRU,ILART,PLKNZ,ARTPR,PRIOK,MAUFNR,MATKL_MM,PLANNED_PARTS_WORK,ZZMPRCTR,ZZLAND1,ZZMMATNR,ZZPROCSRC appear to always be empty string.
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					#ZZRESTID appears to always be 0.
					tmp.append("0")
					#WWCOP_PA,WWPHP_PA,ZZWERKS,ZZMBUKRS,ZZLICENSEE,ZZLICENSOR,ZZPLSEGMENT,OBS_REASON appear to always be empty string.
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					#BSLALT,CSLALT,DSLALT,ESLALT,FSLALT,GSLALT,BSLEXT,CSLEXT,DSLEXT,ESLEXT,FSLEXT,GSLEXT appear to always be 0.
					tmp.append("0")
					tmp.append("0")
					tmp.append("0")
					tmp.append("0")
					tmp.append("0")
					tmp.append("0")
					tmp.append("0")
					tmp.append("0")
					tmp.append("0")
					tmp.append("0")
					tmp.append("0")
					tmp.append("0")
					#COCO_NUM appears to always be empty string.
					tmp.append("")
					#PS_PRJ_PNR,PPS_PSP_PNR,PPS_PRJ_PNR appear to always be 0.
					tmp.append("0")
					tmp.append("0")
					tmp.append("0")
					#DUMMY_MRKT_SGMNT_EEW_PS appears to always be empty string.
					tmp.append("")
					#BILLM,POM,CBRUNID appear to always be 0.
					tmp.append("0")
					tmp.append("0")
					tmp.append("0")
					#JVACTIVITY,PVNAME,PEGRUP,S_RECIND,CBRACCT,CBOBJNR,ACROBJTYPE,ACROBJ_ID,ACRSOBJ_ID,ACRITMTYPE,VALOBJTYPE,VALOBJ_ID,VALSOBJ_ID appear to always be empty string.
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					#NETDT appears to always be 0.
					tmp.append("0")
					#RISK_CLASS,ZZ1_SLUWID_JEI,ZZLICENSOR_NC,ZZLICENSEE_NC,ZZIMPORT_LOCAL,ZZIPLA_BASE,ZZUS_SEG_MODEL,ZZLOC_SEG_MODEL,ZZUS_PL_SEG,ZZLOC_PL_SEG,ZZEXT_OP_SEG,ZZMRFAREA,CBTTYPE appear to always be empty string.
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					#AWITEM_REV appears to always be 0.
					tmp.append("0")
					#PREC_BUKRS appears to always be empty string.
					tmp.append("")
					#PREC_GJAHR appears to awlays be 0.
					tmp.append("0")
					#PREC_BELNR,PREC_DOCLN appear to always be empty string.
					tmp.append("")
					tmp.append("")
					#CLOSING_RUN_ID appears to always be ?
					tmp.append("?")
					#ORGL_CHANGE,RGM_OCUR,RMSL_TYPE appear to always be empty string.
					tmp.append("")
					tmp.append("")
					tmp.append("")
					#GM_OSL appears to always be 0
					tmp.append("0")
					#EBELN_LOGSYS appears to always be empty string
					tmp.append("")
					#PEROP_BEG,PEROP_END appear to always be 0.
					tmp.append("0")
					tmp.append("0")
					#WWERT is bldat unless in new dataset.
					wwert=bldat
					if(indexofrburks==5):
						wwert="0"
					tmp.append(wwert)
					#PRCTR_DRVTN_SOURCE_TYPE,TAX_COUNTRY appear to always be empty string.
					tmp.append("")
					tmp.append("")
					#No guidnace for VALUT.  Appears to be the same as BUDAT unless in new dataset
					valut=budat
					if(indexofrburks==5):
						valut="0"
					tmp.append(valut)
					#INV_MOV_CATEG,UMATNR,VARC_UACCT,SERVICE_DOC_TYPE,SERVICE_DOC_ID appear to always be empty string.
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					#SERVICE_DOC_ID appears to always be 0.
					tmp.append("0")
					#SERVICE_CONTRACT_TYPE,SERVICE_CONTRACT_ID appear to always be empty string.
					tmp.append("")
					tmp.append("")
					#SERVICE_CONTRACT_ITEM_ID appears to always be 0.
					tmp.append("0")
					#SOLUTION_ORDER_ID appears to always be empty string.
					tmp.append("")
					#SOLUTION_ORDER_ITEM_ID appears to always be 0.
					tmp.append("0")
					#PSERVICE_DOC_TYPE	PSERVICE_DOC_ID appear to always be empty string.
					tmp.append("")
					tmp.append("")
					#PSERVICE_DOC_ITEM_ID appears to always be 0.
					tmp.append("0")
					#OVERTIMECAT appears to always be empty string.
					tmp.append("")
					#PAUFPS appears to always be 0.
					tmp.append("0")
					#FIPEX,BDGT_ACCOUNT,BDGT_ACCOUNT_COCODE appear to always be empty string.
					tmp.append("")
					tmp.append("")
					tmp.append("")
					#BDGT_CNSMPN_DATE,BDGT_CNSMPN_PERIOD,BDGT_CNSMPN_YEAR appear to always be 0.
					tmp.append("0")
					tmp.append("0")
					tmp.append("0")
					#BDGT_RELEVANT,BDGT_CNSMPN_TYPE,BDGT_CNSMPN_AMOUNT_TYPE,RSPONSORED_PROG,RSPONSORED_CLASS,RBDGT_VLDTY_NBR,KBLNR appear to always be empty string.
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					tmp.append("")
					#KBLPOS appears to always be 0.
					tmp.append("0")
					#ACRLOGSYS appears to always be empty string.
					tmp.append("")
					#ACRVALDAT appears to always be 0.
					tmp.append("0")
					#SDM_VERSION appears to always be 1.
					tmp.append("1")
									
					
					monthout.append(tmp)
					docln[indexofrburks]+=1
					if((docln[indexofrburks])>=1000000):
						belnr[indexofrburks]+=1
						docln[indexofrburks]=0
				#print(len(monthout))
			writer=csv.writer(of,delimiter=",")
			for row in monthout:
				writer.writerow(row)
		of.close()
		print("End of month")
