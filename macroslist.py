# Macros Corresponding List
# comes with ABSOLUTELY NO WARRANTY.
# Copyright (C) 2016 Hintay <hintay@me.com>
#
# This file is part of Vita Scenarios Converter.

###########
# Special
###########
IGNORE_MACROS = ['SYNC', 'KMW2', 'HFUL', 'PEND']
# 最后可能有括号
BRACKET_END_MACROS = ['BTXO', 'BIVF', 'MPAU', 'WTVT']
# 最前面无逗号
MACROS_WITHOUT_COMMA = ['KHZE', 'PAGE', 'FCAL', 'NEVL', 'KFCH', 'VPLY', 'WTVT', 'KDLY']

IGNORE_PARAMETERS = ['002', '113', '237', '238', '239']

CLOSE_INLINE_MACRO = ['VPLY', 'TPG0', 'BRET']
###########

MACROS = {
	'BFNT':'@font',
	'BIED':'@interlude_end',
	'BIVF':{'0':'@visibleframe', '1':'@invisibleframe'},
	'BIST':'@interlude_start',
	'BRET':'@return',
	'BTXO':{'0':'@textoff', '1':'@texton'},
	'CFAD':{'0':'@fadein', '2':'@rep'},
	'CHCL':{'0':{'0':'@condoff', '2':'@red', '3':'@green', '4':'@blue', '5':'@nega', '6':'@monocro'}, '1':{'2':'@red', '8':'@sepia'}},
	'CHZB':'@haze_back',
	'CHZS':'@stophaze',
	'CHTC':{'1':'@hearttonecombo'},
	#'COND':'',
	'CTRX':'@transex',
	'CCTO':{'0':'@contrastoff'},
	'CCTR':{'1':'@contrast'},
	'FCAL':'@call', #_FCAL((1166; @call storage=街編・1日目-03.ks
	'HRDW':'@redraw',
	'HFAN':'@hfangry',
	'HFBB':'@hfburstblood',
	'HFCN':'@hfchance',
	'HFFA':'@hfface',
	'HFFC':'@hffacechg',
	'HFFG':'@hffeelgood',
	'HFSG':'@hfsigh',
	'HFST':'@hfstamp',
	'HFSW':'@hfsweat',
	'HFPP':'@hfpop',
	'HFWW':'@hfwww',
	#'HFTF':'@tf',
	#'HFUL':{'2':''}, #_HFUL(2; [hfu]字[hfl] 须特殊处理
	'HSMG':{'0':'@smudge'},
	'HSMO':{'0':'@smudgeoff'},
	'IRIY':'@history enabled=false\n@shortcutkey enabled=false\n@cancelskip',
	'IRIW':'@showiriyacastle',
	'KDSH':'@dash',
	'KDSS':{'0':'@stopdash'},
	'KDSW':'@wdash',
	'KDLY':'@delay',
	'KFCH':'@chgfg',
	'KFG0':'@fg',
	'KFMV':'@movefg', # @monocro
	'KMST':'@stopmove', # @stopsplinemove
	'KMWT':'@wm',
	#'KMW2':'',
	'KMVE':'@move',
	'KMLP':'@loopmove',
	'KSMW':'@wsplinemove',
	'KHZE':'@haze',
	'KFND':'@find',
	'KSMV':'@splinemove',
	'KIMG':'@image',
	'KIME':'@imageex',
	'KWRS':'@resetwait',
	'MPLY':{'0':'@play', '2':'@xchgbgm'},
	'MPAU':{'0':'@playresume', '1':'@playpause'},
	'MSTP':{'0':'@playstop'},
	'NEVL':'@eval', #_NEVL(exp=Scripts.execStorage(HanafudaPlugin.tjs);
	'NCL0':'@cl',
	'NCLF':'@clfg',
	'NCIN':{'0':'@cinesco'},
	'NCTR':'@cltransparent',
	'NCIO':{'0':'@cinesco_off'},
	'NNOB':'@noise_back',
	'NNOI':{'0':'@noise'},
	'NNOS':{'0':'@stopnoise'}, # @noise_off
	'NQUK':{'0':'@quake'},
	'NQUS':'@stopquake',
	'NQUL':'@lquake',
	'NQLS':'@stoplquake',
	'NLYO':'@layopt',
	'NSHK':{'0':'@shock'},
	'NSHW':'@wshock',
	'NLYB':'@backlay',
	'PAGE':'*page',
	#'PEND':'', #_PEND(; 占位符？
	#'QSET':{'0':'@call storage=QuizSystem.ks\n@iscript'},
	#'QADE':'@endscript',
	#'QADS':'.quiz	= %[%s]',
	#'QADD':'quiz:[%s]',
	'SESF':'@sestop',
	'SEPF':{'0':'@se', '2':'@seloop', '0tdeepdaytime':'@setdeepdaytime', '0thscene':'@sethscene'},
	'SEFF':'@fadese',
	'SNOW':{'0':'@snowuninit', '1':{'800':'@snowinit forevisible=false backvisible=true'}}, #@snowopt backvisible=false
	'TCM0':'@cm',
	'TDSP':{'0':'@displayedoff', '1':'@displayedon'},
	'TPG0':'@pg',
	'TWND':{'0':'@setdaytime', '1':'@setnighttime'},
	'TWT0':'@wt',
	#'TRPY':,
	'VPLY':'@say',
	'WTVT':'@waitvoice',
	'WTFT':{'0':'@wait', '0acanskip=false':'@wait acanskip=false'},
	'WTKY':'@l',
	'WNDS':{'0':'@window_start', '1':'@window_end', '2':'@hanafuda_conversation'},
	'MFNR':'@resetfont', # and @rf
	'MVOL':'@fadebgm',
	'MTLK':'@say'
	#'SYNC;:'',
	#'WKST':'',
	#'MVPL':'@playmovie',
	#'MSAD':'', #文本框
}
# @smudge @blur @smudgeoff @bluroff @slideopencombo @slideclosecombo @pasttime 被_CFAD所替代
# @shortcutkey @history 被去除

# _WKST(G054,1;  _WKST(G011,1; 变量+1
# _QJMP(_D990,quiz14_correct,quiz14_incorrect; @quiz success=*page11 failed=*page12
# _HFTF(0,`026:クイズタイガー編クリア,`235:1; @eval exp="tf['クイズタイガー編クリア']=true"

# 以`开头
PARAMETERS = {
	#'002':'haverule', # 2=on 0=none ?
	'003':'time',
	'004':'vague',
	'005':'storage', # bg for @rep?
	'008':'canskip',
	'010':'page',
	'012':'layer', # -2=&no -1=base 255=all
	'013':'left',
	'014':'top',
	'015':'opacity',
	'017':'accel',
	'018':'cx',
	'019':'cy',
	'020':'imag',
	'021':'mag',
	'023':'range', #_HSMG
	'024':'level',
	#'026':'tf', #_HFTF ??
	'032':'pos',
	'033':'index',
	'034':'noclear',
	'035':'fliplr',
	'036':'flipud',
	'037':'poss',
	'039':'indexes',
	'040':'opacities',
	'041':'vmax',
	'042':'count',
	'043':'delay',
	'044':'type',
	'045':'nowait',
	'046':'textoff',
	'047':'irot',
	'048':'mx',
	'049':'my',
	'050':'rot',
	'051':'face',
	'067':'hmax',
	'068':'upper',
	'069':'lower',
	'074':'volume',
	'075':'target',
	'076':'hidefg',
	'086':'color',
	'087':'storages',
	'089':'center',
	'090':'upperpow',
	'091':'lowerpow',
	'092':'centerpow',
	#'094':'id', #_SYNC starttag
	'096':'lwaves',
	'098':'base',
	'099':'px',
	'100':'py',
	'101':'deg',
	'111':'overlap',
	#'113':'', #_KDSH @dash
	'114':'monocro',
	'115':'both', #_KFMV @movefg
	'116':'mover', #_KMLP @loopmove
	'117':'frame',
	'118':'decel',
	'119':'spread', #_KMVE @move
	'121':'intime',
	'122':'waves',
	'124':'standard',
	'128':'edgecolor',
	'131':'italic',
	#'139':'bg', #? _KDSH @dash _COND
	'141':'indexs',
	'164':'rule',
	'170':'spline',
	'171':'affine',
	'172':'path',
	'216':'last',
	'217':'lv2off',
	'218':'fliplrs',
	'219':'flipuds',
	'220':'avoid',
	'221':'force',
	'222':'layers',
	'223':'lefts',
	'224':'tops',
	'227':'colors',
	'228':'monos',
	'229':'mono',
	'230':'noquake',
	'231':'bluroff',
	'232':'chara',
	'233':'question',
	'234':'alters',
	#'235':'result',
	'236':'nospline',
	#'237':'', #@loopmove
	#'238':'', #@chgfg
	#'239':'', #@loopmove
}

TARGET = {
	'1':'bg',
	'2':'fg',
	'3':'all',
}

PAGE = {
	'0':'back',
	'1':'fore'
}

CALL = {
	'(1013':'カレン-01.ks',
	'(1166':'街編・1日目-03.ks',
	'(1179':'街編・1日目-24.ks'
}

RULE = {
	'001':'crystal_bt',
	'002':'l2r_half',
	'003':'l2r_ss',
	'004':'mosaic_lt_rb',
	'005':'pageleft',
	'006':'pageright',
	'007':'r2l_half',
	'008':'r2l_sfs',
	'009':'r2l_ss',
	'010':'sparm',
	'011':'trans000',
	'012':'カーテン左から',
	'013':'カーテン上から',
	'014':'シャッター下から',
	'015':'シャッター左から',
	'016':'シャッター上から',
	'022':'モザイク',
	'027':'やや細かい縦ブラインド(中央から左右へ)',
	'028':'右から左へ',
	'029':'右渦巻き',
	'030':'右下から左上へ',
	'031':'右上から左下へ',
	'032':'円形(外から中へ)',
	'033':'円形(中から外へ)',
	'036':'下から上へ',
	'037':'左から右へ',
	'038':'左下から右上へ',
	'039':'左回り',
	'041':'左上から右下へ',
	'048':'斜めチェッカー',
	'052':'上から下へ',
	'053':'走る感じ(右から)',
	'054':'走る感じ(下から)',
	'055':'走る感じ(上から)',
	'056':'走る感じ',
	'058':'短冊(下から)',
	'059':'短冊(上から)',
	'060':'短冊細(右から)',
	'061':'短冊細(左から)',
	'062':'虫食い',
	'063':'波',
	'064':'放射状(時計回り)',
	'066':'koyama02r',
	'067':'カレン割',
	'070':'crystal_bt_r',
	'071':'forfd05',
	'072':'forfd05_2',
	'073':'forfd逆月07',
	'074':'forRider01',
	'075':'koyama01r',
	'076':'koyama02r2',
	'078':'中央から左右へ',
	'079':'左回り連続2',
}

POS = {
	'-1':'all',
	'1':'l',
	'2':'r',
	'3':'lc',
	'4':'rc',
	'5':'c',
	'1ower':'lower', #替换文本
}

LAYER = {
	'-2':'&no',
	'-1':'base',
	'1':'base',
	'255':'all'
}

BGM = {
	'0':'bgm01',
	'1':'bgm03',
	'2':'bgm04',
	'3':'bgm05',
	'4':'bgm06',
	'5':'bgm07',
	'6':'bgm08',
	'7':'bgm09',
	'8':'bgm10',
	'9':'bgm11',
	'10':'bgm13',
	'11':'bgm14',
	'12':'bgm15',
	'13':'bgm16',
	'14':'bgm17',
	'15':'bgm18',
	'16':'bgm19',
	'17':'bgm20',
	'18':'bgm21',
	'19':'bgm22',
	'20':'bgm23',
	'21':'bgm24',
	'22':'bgm25',
	'23':'bgm26',
	'24':'bgm27',
	'25':'bgm28',
	'26':'bgm29',
	'27':'bgm33',
	'28':'bgm34',
	'29':'bgm35',
	'30':'bgm38',
	'31':'bgm39',
	'32':'bgm40',
	'33':'bgm41',
	'34':'bgm42',
	'35':'bgm43',
	'36':'bgm44',
	'37':'bgm45',
	'38':'bgm46',
	'39':'bgm48',
	'40':'bgm49',
	'41':'bgm101',
	'42':'bgm102',
	'43':'bgm103',
	'44':'bgm104',
	'45':'bgm105',
	'46':'bgm106',
	'47':'bgm107',
	'48':'bgm108',
	'49':'bgm109',
	'50':'bgm110a',
	'51':'bgm110b',
	'52':'bgm111',
	'53':'bgm112',
	'54':'bgm113',
	'55':'bgm114',
	'56':'bgm115',
	'57':'bgm116',
	'58':'bgm117',
	'59':'bgm118',
	'60':'bgm119',
	'61':'bgm120',
	'62':'bgm121',
	'63':'bgm122',
	'64':'bgm123',
	'65':'bgm124',
	'66':'bgm126',
	'67':'bgm127',
	'68':'bgm128',
	'69':'bgm129',
	'70':'bgm130',
	'71':'bgm131',
	'72':'bgm132',
	'73':'bgm133',
	'74':'bgm134',
	'75':'bgm135',
	'76':'bgm135b',
	'77':'bgm136',
	'78':'bgm137',
	'79':'bgm138',
	'80':'bgm139',
	'81':'bgm140',
	'82':'bgm141',
	'83':'bgm142',
	'84':'bgm143',
	'85':'bgm144',
	'86':'bgm145',
	'87':'demo01',
	'88':'demo02',
	'89':'demo03',
	'90':'demo04',
	'91':'hfbgm01',
	'92':'hfbgm02',
	'93':'hfbgm03',
	'94':'hfbgm04',
	'95':'hfbgm05',
	'96':'hfbgm06',
	'97':'hfbgm07',
	'98':'iriya01',
	'99':'iriya02',
	'100':'iriya03',
	'101':'iriya04',
	'102':'iriya05',
	'103':'iriya06',
	'104':'iriya07',
	'105':'iriya08',
	'106':'iriya09',
	'107':'iriya10',
	'108':'ステータス',
}
'''
	# Capsule Servant
	'109':'',
	'110':'',
	'111':'',
	'112':'',
	'113':'',
	'114':'',
	'115':'',
	'116':'',
	'117':'',
	'118':'',
	'119':'',
	'120':'',
	'121':'',
	'123':'',
	'124':'',
	'125':'',
	'126':'',
}
'''

TRUE_FALSE = {
	'0':'false',
	'1':'true'
}

NOISE_TYPE = {
	'1':'ltDodge'
}

SAY_NAME = {
	'RIN': '凛',
	'SHI': '士郎',
	'BZK': '二人',
}

STORAGES = {
	'IMG_670A352B_iバゼ': 'iバゼットの隠れ家_内部(夢現)-(白)',
	'IMG_EF60BDD8_iバゼ': 'iバゼットの隠れ家_内部(夢現)(血痕)-(白)',
	'IMG_C7931E16_iバゼ': 'iバゼットの隠れ家_内部-(深夜)',
	'IMG_FDFEA332_oバゼ': 'oバゼットの隠れ家(姉)-(深夜)',
	'IMG_9F1C24C2_oバゼ': 'oバゼットの隠れ家(妹)-(深夜)',
	'IMG_72F65F4F_oバゼ': 'oバゼットの隠れ家(妹)-(昼)',
	'IMG_D641DBCB_o教会': 'o教会付近の街並(秋)-(深夜)',
	'IMG_0B7C49DE_57カ': '57カレン過去回想04祈りと働き',
	'IMG_ED41252C_58ラ': '58ランサー過去回想01旅立ち',
	'IMG_8A9B0663_59ラ': '59ランサー過去回想02影の国',
	'IMG_CE2887EE_60ラ': '60ランサー過去回想03アルスター',
	'IMG_D0C51D78_61ラ': '61ランサー過去回想04英雄の黄昏',
	'IMG_FC5D6E5A_63ア': '63アンリマユ過去回想01生まれた村',
	'IMG_3A40273E_i言峰': 'i言峰教会礼拝堂(廃虚)-(月明)',
	'IMG_8D37F8DA_o言峰': 'o言峰教会前(秋)(灯り無し)-(夜)',
	'IMG_A7F96129_汎用戦': '汎用戦闘バゼット_腕A_a',
	'IMG_8FEFBEFA_汎用戦': '汎用戦闘バゼット_腕B_a',
	'IMG_6C0B1867_汎用戦': '汎用戦闘バゼット_腕B_a(紫)',
	'IMG_0F7D7030_汎用戦': '汎用戦闘バゼット_腕A_a(紫)',
	'IMG_0F7D702E_汎用戦': '汎用戦闘バゼット_腕A_c(紫)',
	'IMG_02FC1CB2_黒セイ': '黒セイバーFD特殊01a(遠)',
	'IMG_9D7FD2E9_キャス': 'キャスターローブ無し01b(中)',
	'IMG_77E6D2EC_キャス': 'キャスターローブ無し02a(中)',
	'IMG_0C99E447_カレン': 'カレン修道服無帽01c頬(中)',
	'IMG_D8845CB2_カレン': 'カレン修道服無帽01f頬(中)',
	'IMG_0CDBE447_カレン': 'カレン修道服無帽03c(中)',
	'IMG_CC0FE447_カレン': 'カレン修道服無帽03c頬(近)',
	'IMG_87266CA8_カレン': 'カレン修道服無帽03d頬(近)',
	'IMG_82E7E624_カレン': 'カレン修道服無帽04h頬(中)',
	'IMG_0718AC6A_カレン': 'カレン修道服無帽04n頬(近)',
	'IMG_479CAC6A_カレン': 'カレン修道服無帽04n頬(中)',
	'IMG_C7F26CA8_カレン': 'カレン修道服無帽03d(中)',
	#'IMG_981D5CB2_カレン': ''
	#'IMG_E54DCC56_カレン': 'カレン修道服無帽03b頬(近)',
	'IMG_DC78E402_セイバ': 'セイバー私服_箸持ち09a(中)',
	'IMG_2F5262FC_ステン': 'ステンドグラスcenter-(夜)',
}

SPECIAL_PARAMETER = { 'target':TARGET, 'page':PAGE, 'rule':RULE, 'pos':POS, 'layer':LAYER, 'nowait':TRUE_FALSE, 'type':NOISE_TYPE, 'storage': STORAGES }
