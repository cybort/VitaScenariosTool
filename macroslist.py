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
	'IMG_8E844AE3_oバゼ': 'oバゼットの隠れ家(妹)-(深夜)_sm05', # sm05
	'IMG_D641DBCB_o教会': 'o教会付近の街並(秋)-(深夜)',
	'IMG_3A40273E_i言峰': 'i言峰教会礼拝堂(廃虚)-(月明)',
	'IMG_6E28DAD9_i言峰': 'i言峰教会礼拝堂(廃虚)-(月明)_sm05', # sm05
	'IMG_6E2DDAD7_i言峰': 'i言峰教会礼拝堂(廃虚)-(月明)_sm20', # sm20
	'IMG_8D37F8DA_o言峰': 'o言峰教会前(秋)(灯り無し)-(夜)',
	'IMG_A7F96129_汎用戦': '汎用戦闘バゼット_腕A_a',
	'IMG_8FEFBEFA_汎用戦': '汎用戦闘バゼット_腕B_a',
	'IMG_6C0B1867_汎用戦': '汎用戦闘バゼット_腕B_a(紫)',
	'IMG_0F7D7030_汎用戦': '汎用戦闘バゼット_腕A_a(紫)',
	'IMG_0F7D702E_汎用戦': '汎用戦闘バゼット_腕A_c(紫)',
	'IMG_02FC1CB2_黒セイ': '黒セイバーFD特殊01a(遠)',
	'IMG_DA2A2BB7_キャス': 'キャスター私服01c怒り(中)',
	'IMG_9D7FD2EC_キャス': 'キャスターローブ無し01a(中)',
	'IMG_9D7FD2E9_キャス': 'キャスターローブ無し01b(中)',
	'IMG_FEF13D00_キャス': 'キャスターローブ無し01b(遠)',
	'IMG_9D7FD2EA_キャス': 'キャスターローブ無し01c(中)',
	'IMG_9D7FD2E7_キャス': 'キャスターローブ無し01d(中)',
	'IMG_E02A20D5_キャス': 'キャスターローブ無し01f(中)',
	'IMG_9D7FD2E5_キャス': 'キャスターローブ無し01f(中)',
	'IMG_B18A17DE_キャス': 'キャスターローブ無し01k(近)',
	'IMG_9D7FD2F2_キャス': 'キャスターローブ無し01k(中)',
	'IMG_77E6D2EC_キャス': 'キャスターローブ無し02a(中)',
	'IMG_77E6D2E9_キャス': 'キャスターローブ無し02b(中)',
	'IMG_8BF117D5_キャス': 'キャスターローブ無し02b(近)',
	'IMG_8BF117D6_キャス': 'キャスターローブ無し02c(近)',
	'IMG_77E6D2E7_キャス': 'キャスターローブ無し02d(中)',
	'IMG_77E6D2E8_キャス': 'キャスターローブ無し02e(中)',
	'IMG_77E6D2E6_キャス': 'キャスターローブ無し02g(中)',
	'IMG_77E6D2F3_キャス': 'キャスターローブ無し02h(中)',
	'IMG_77E6D2F4_キャス': 'キャスターローブ無し02i(中)',
	'IMG_77E6D2EF_キャス': 'キャスターローブ無し02l(中)',
	'IMG_AD75D2E9_キャス': 'キャスターローブ無し03b(中)',
	'IMG_956063C2_キャス': 'キャスターローブ無し03b頬(中)',
	'IMG_7E0563C1_キャス': 'キャスターローブ無し03b耳(中)',
	'IMG_AD75D2EA_キャス': 'キャスターローブ無し03c(中)',
	'IMG_95606395_キャス': 'キャスターローブ無し03c頬(中)',
	'IMG_95606380_キャス': 'キャスターローブ無し03d頬(中)',
	'IMG_81276380_キャス': 'キャスターローブ無し03d頬(遠)',
	'IMG_9560633E_キャス': 'キャスターローブ無し03f頬(中)',
	'IMG_AD75D2F3_キャス': 'キャスターローブ無し03h(中)',
	'IMG_0C99E447_カレン': 'カレン修道服無帽01c頬(中)',
	'IMG_D8845CB2_カレン': 'カレン修道服無帽01f頬(中)',
	'IMG_0CDBE447_カレン': 'カレン修道服無帽03c(中)',
	'IMG_CC0FE447_カレン': 'カレン修道服無帽03c頬(近)',
	'IMG_87266CA8_カレン': 'カレン修道服無帽03d頬(近)',
	'IMG_82E7E624_カレン': 'カレン修道服無帽04h頬(中)',
	'IMG_0718AC6A_カレン': 'カレン修道服無帽04n頬(近)',
	'IMG_479CAC6A_カレン': 'カレン修道服無帽04n頬(中)',
	'IMG_C7F26CA8_カレン': 'カレン修道服無帽03d(中)',
	'IMG_8F05FD28_カレン': 'カレン修道服無帽04b(中)_sm05', # sm05
	'IMG_018FF8BB_カレン': 'カレン修道服無帽02h(中)_sm20', # sm20
	#'IMG_981D5CB2_カレン': ''
	#'IMG_E54DCC56_カレン': 'カレン修道服無帽03b頬(近)',
	'IMG_DC78E402_セイバ': 'セイバー私服_箸持ち09a(中)',
	'IMG_2F5262FC_ステン': 'ステンドグラスcenter-(夜)',
	'IMG_FD57CFF5_FD2': 'fd25_01a(アーチャーとギルa)',
	'IMG_FD58CFF5_FD2': 'fd25_01a(アーチャーとギルb)',
	'IMG_6B7988E1_T04': 't04無数に投擲された短剣a',
	'IMG_6B7A88E1_T04': 't04無数に投擲された短剣b',
	'IMG_162573D7_o山門': 'o山門階段(遠景)(秋)-(曇2)',
	'IMG_5B0647F6_o山門': 'o山門階段(アップ)(秋)-(曇2)',
	'IMG_132C47F6_o山門': 'o山門階段(アップ)(秋)-(夕2)',
	'IMG_2FB122C9_o山門': 'o山門階段(遠景)(秋)-(深夜)',
	'IMG_B51FFED4_o山門': 'o山門階段(アップ)(秋)-(深夜)',
	'IMG_370D5AB8_o演劇': 'o演劇06_海上01b-(曇2)',
	'IMG_2E3D4607_o演劇': 'o演劇08_海上の鬼ヶ島-(曇2)',
	'IMG_518FF023_o演劇': 'o演劇09_鬼の城・近景-(真紅)',
	'IMG_36525ADF_o演劇': 'o演劇10_鬼ヶ島内部01-(真紅)',
	'IMG_037CB318_o演劇': 'o演劇11_鬼ヶ島内部02-(深夜)',
	'IMG_D73667AF_o衛宮': 'o衛宮邸付近の街並(秋)-(夕)',
	'IMG_49CA97EC_o衛宮': 'o衛宮邸付近の街並(秋)-(夜)',
	'IMG_FD3C7785_o衛宮': 'o衛宮邸付近の街並(秋)(@)-(夜)',
	'IMG_D431109C_o衛宮': 'o衛宮邸付近の街並(秋)-(深夜)',
	'IMG_7DC9C68B_o遠坂': 'o遠坂邸付近の街並(秋)-(夜)',
	'IMG_F074A852_o冬木': 'o冬木大橋袂の公園1(秋)-(夜)',
	'IMG_C002DF3D_o冬木': 'o冬木大橋袂の公園1(秋)-(深夜)',
	'IMG_CCC7DF3D_o冬木': 'o冬木大橋袂の公園2(秋)-(深夜)',
	'IMG_BBADCA56_o冬木': 'o冬木大橋袂の公園2(秋)-(深夜)_sm06', # sm06
	'IMG_FB74CFC4_o冬樹': 'o冬樹大橋の上(行き)-(深夜)',
	'IMG_FAB26867_o冬樹': 'o冬樹大橋の上(行き)(光点)-(深夜)',
	'IMG_1E6842BB_o冬樹': 'o冬樹大橋の上(帰り)(闇)-(深夜)',
	'IMG_81A2F89C_o冬樹': 'o冬樹大橋の上(帰り)(＠遠)-(深夜)',
	'IMG_D12FF89B_o冬樹': 'o冬樹大橋の上(帰り)(＠近)-(深夜)',
	'IMG_6C8DDE7C_o冬樹': 'o冬樹大橋の上(帰り)(＠近)-(深夜)_sm10', # sm10
	'IMG_B12ECB0E_02汎': '02汎用セイバー01右(決戦)_c',
	'IMG_E9072C3D_02汎': '02汎用セイバー01右(聖剣)_d',
	'IMG_B12ECB0C_02汎': '02汎用セイバー01右(決戦)_e',
	'IMG_3A55DE48_16フ': '16フラガラック(オブジェクトb)',
	'IMG_63B81A53_18ア': '18アヴェスタ発動a(ブラー)',
	'IMG_64151A53_18ア': '18アヴェスタ発動b(ブラー)',
	'IMG_63F61A53_18ア': '18アヴェスタ発動c(ブラー)',
	'IMG_65531A53_18ア': '18アヴェスタ発動d(ブラー)',
	'IMG_C3556587_31絡': '31絡めとられるカリバー',
	'IMG_0B7C49DE_57カ': '57カレン過去回想04祈りと働き',
	'IMG_ED41252C_58ラ': '58ランサー過去回想01旅立ち',
	'IMG_8A9B0663_59ラ': '59ランサー過去回想02影の国',
	'IMG_CE2887EE_60ラ': '60ランサー過去回想03アルスター',
	'IMG_D0C51D78_61ラ': '61ランサー過去回想04英雄の黄昏',
	'IMG_FC5D6E5A_63ア': '63アンリマユ過去回想01生まれた村',
	'IMG_A9A23FA3_65ラ': '65ランサーVSバゼット00',
	'IMG_A9A13FA3_65ラ': '65ランサーvsバゼット01',
	'IMG_A9A43FA3_65ラ': '65ランサーvsバゼット02',
	'IMG_A9A33FA3_65ラ': '65ランサーvsバゼット03',
	'IMG_A99E3FA3_65ラ': '65ランサーvsバゼット04',
	'IMG_A99D3FA3_65ラ': '65ランサーvsバゼット05',
	'IMG_A9A03FA3_65ラ': '65ランサーvsバゼット06',
	'IMG_A99F3FA3_65ラ': '65ランサーvsバゼット07',
	'IMG_A99A3FA3_65ラ': '65ランサーvsバゼット08',
	'IMG_A9993FA3_65ラ': '65ランサーvsバゼット09',
	'IMG_A9A23FA2_65ラ': '65ランサーvsバゼット10',
	'IMG_771BE8C9_43セ': '43セイバー切り＠a(エフェクトb)',
	'IMG_E27065FD_43セ': '43セイバー切り＠(オブジェクトc)',
	'IMG_E27065FF_43セ': '43セイバー切り＠(オブジェクトa)',
	'IMG_7734E90E_43セ': '43セイバー切り＠a(エフェクト)',
	'IMG_DE502B37_43セ': '43セイバー切り＠b(エフェクト無し)',
	'IMG_7350E8C9_43セ': '43セイバー切り＠b(エフェクトb)',
	'IMG_E1832B37_43セ': '43セイバー切り＠a(エフェクト無し)',
	'IMG_C83B23FD_46＠': '46＠化するアヴェンジャー01',
	'IMG_B03181CE_46＠': '46＠化するアヴェンジャー02',
	'IMG_0D8A0D33_46＠': '46＠化するアヴェンジャー03',
	'IMG_F5806B04_46＠': '46＠化するアヴェンジャー04',
	'IMG_276629AB_47＠': '47＠に変じたアヴェンジャー',
	'IMG_862C9359_49カ': '49カレン聖骸布による捕縛(オブジェクト1)',
	'IMG_862C935A_49カ': '49カレン聖骸布による捕縛(オブジェクト2)',
	'IMG_862C935B_49カ': '49カレン聖骸布による捕縛(オブジェクト3)',
	'IMG_862C935C_49カ': '49カレン聖骸布による捕縛(オブジェクト4)',
	'IMG_42CADB86_065': '065_セイバー鎧08a(中)(ブラ)',
	'IMG_C62EDB9E_065': '065_セイバー鎧08a(近)(ブラ)',
	'IMG_3FC4DD14_o言峰': 'o言峰教会前(秋)-(夜)_sm05', # sm05
	'IMG_E3F440A4_アンリ': 'アンリシルエット01a(中)',
	'IMG_A0A9DC89_橋決戦': '橋決戦03(セイバーのみ)',
	'IMG_20C8BE83_橋決戦': '橋決戦03b(アーチャーのみ)',
	'IMG_7E73105B_橋決戦': '橋決戦04(素材・瓦礫Aブラー)',
	'IMG_5CAA105B_橋決戦': '橋決戦04(素材・瓦礫Bブラー)',
	'IMG_DDF0A0D5_橋決戦': '橋決戦05(跳弾・衝撃波なし)',
	'IMG_B5CAE03C_橋決戦': '橋決戦07(素材・ビル窓抜き)',
	'IMG_349F86CE_橋決戦': '橋決戦07(素材・ビル照明あり)',
	'IMG_A169E73C_オブジ': 'オブジェクト_アチャ弾(歪・エフェクト)',
	'IMG_AD323AB1_オブジ': 'オブジェクト_アチャ弾(正球・エフェクト)',
	'IMG_273DDCD4_オブジ': 'オブジェクト_アチャ弾(正球)',
	'IMG_732C743F_キャス': 'キャスターローブ無し01c怒り(遠)',
	'IMG_FEF13D01_キャス': 'キャスターローブ無し01c(遠)',
	'IMG_D9583CFF_キャス': 'キャスターローブ無し02e(遠)',
	'IMG_D9583D01_キャス': 'キャスターローブ無し02c(遠)',
	'IMG_D9583D03_キャス': 'キャスターローブ無し02a(遠)',
	'IMG_D9583D00_キャス': 'キャスターローブ無し02b(遠)',
	'IMG_0EE73D00_キャス': 'キャスターローブ無し03b(遠)',
	'IMG_FEF13D03_キャス': 'キャスターローブ無し01a(遠)',
	'IMG_D9583CFC_キャス': 'キャスターローブ無し02f(遠)',
	'IMG_FEF13D03_キャス': 'キャスターローブ無し01a(遠)',
	'IMG_D9583D06_キャス': 'キャスターローブ無し02l(遠)',
	'IMG_AD75D2E7_キャス': 'キャスターローブ無し03d(中)',
	'IMG_732C9A8A_キャス': 'キャスターローブ無し01c怒り(中)',
	
	'IMG_D15B74A0_70キ': '70キャスター過去回想_魔力の鍋',
	'IMG_F46F50EF_71キ': '71キャスター過去回想_浜辺',
	'IMG_77E6D2EA_キャス': 'キャスターローブ無し02c(中)',
	'IMG_9D7FD2E8_キャス': 'キャスターローブ無し01e(中)',
	'IMG_AD75D2E5_キャス': 'キャスターローブ無し03f(中)',
	'IMG_3874D7DF_o地下': 'o地下洞くつ通路(魔)-(蒼緑)',
	'IMG_0922B462_o地下': 'o地下大空洞全景(過去)-(夜)',
	'IMG_AD75D2EC_キャス': 'キャスターローブ無し03a(中)',
	'IMG_AD75D2E8_キャス': 'キャスターローブ無し03e(中)',
	'IMG_C18017D3_キャス': 'キャスターローブ無し03d(近)',
	'IMG_AEF0DE48_16フ': '16フラガラック(オブジェクトa)',
	'IMG_B129D371_41ア': '41アーチャーが倒されたイメージ',
	'IMG_E57ADEAA_RE0': 'RE01シャーマニック・アンリ',
	'IMG_A730ED07_oアイ': 'oアインツ森内部(逆風b)-(夜)',
	'IMG_C7A660C5_リズハ': 'リズハルバード01ブラーa(遠)',
	'IMG_C7A660A4_リズハ': 'リズハルバード02ブラーa(遠)',
	'IMG_021B0BFA_iアイ': 'iアインツベルン談話室-(夜)',
	'IMG_1E581EFE_o遠坂': 'o遠坂邸付近の街並(秋)-(深夜)',
	'IMG_73F3B205_カレン': 'カレン修道服無帽01a(遠)_sm06', # sm06
	'IMG_6E2BDAD9_i言峰': 'i言峰教会礼拝堂(廃虚)-(月明)_sm06', # sm06
	'IMG_5F5205BF_53バ': '53バゼット過去回想_野営02',
	'IMG_5ACD590D_iバゼ': 'iバゼットの隠れ家_内部-(深夜)_sm06', # sm06
	'IMG_5AC9590C_iバゼ': 'iバゼットの隠れ家_内部-(深夜)_sm12', # sm12
	'IMG_5ACA590D_iバゼ': 'iバゼットの隠れ家_内部-(深夜)',
	'IMG_5504AB1E_士郎ア': '士郎アンリ01a(中)_sm05', # sm05
	'IMG_E726851D_o新都': 'o新都_室内プール(モブ)-(昼)',
	'IMG_47FBF9C8_o新都': 'o新都_室内プール02(モブ)-(昼)',
	'IMG_A265E65F_i新都': 'i新都_ショッピングモールmove',
	'IMG_82D791FF_o新都': 'o新都_室内プール-(昼)',
	'IMG_6E071A20_o新都': 'o新都_室内プール02-(昼)',
	'IMG_6BCD2CE2_o駅前': 'o駅前パーク(秋)-(夕)_sm03', # sm03
	'IMG_6BCE2CE3_o駅前': 'o駅前パーク(秋)-(夕)_sm30', # sm30
	'IMG_CBD81A20_o新都': 'o新都_室内プール02-(昼)_sm03', # sm03
	'IMG_72033334_ライダ': 'ライダー私服04b頬(中)_sm06', # sm06
	'IMG_4456084C_o衛宮': 'o衛宮邸付近の街並(秋)-(昼)',
	'IMG_D66E4B83_o新都': 'o新都_室内プール(モブ)-(昼)',
	'IMG_FB923BD1_セイバ': 'セイバーfd特殊01a頬(中)_sm30', # sm30
	'IMG_D66B4B86_o新都': 'o新都_室内プール(モブ)-(昼)_sm30', # sm30
	'IMG_A4A98120_セイバ': 'セイバーfd特殊05g(近)_sm20', # sm20
	'IMG_5F5897EA_セイバ': 'セイバーfd特殊05g(近)_sm06', # sm06
	'IMG_3AAC28D9_セイバ': 'セイバーfd特殊01l(中)_sm30', # sm30
	'IMG_0737E349_o新都': 'o新都_室内プール02(モブ)-(昼)_sm30', # sm30
	'IMG_A4A88120_セイバ': 'セイバーfd特殊05g(近)_sm30', # sm30
	'IMG_AD1A723F_セイバ': 'セイバー私服01b3(中)_sm06', # sm06
	'IMG_C8C18AE0_セイバ': 'セイバー私服06a腕b(中)_sm06', # sm06
	'IMG_677EA17D_o駅前': 'o駅前パーク(秋)-(昼)_sm06', # sm06
	'IMG_A617962B_o遠坂': 'o遠坂邸付近の街並(秋)-(昼)',
	'IMG_6A100275_凛パジ': '凛パジャマ_髪下ろし02a頬(中)',
	'IMG_6A100296_凛パジ': '凛パジャマ_髪下ろし02b頬(中)',
	'IMG_6A1002B7_凛パジ': '凛パジャマ_髪下ろし02c頬(中)',
	'IMG_5DAC02B7_凛パジ': '凛パジャマ_髪下ろし02c頬(近)',
	'IMG_6A1001E0_凛パジ': '凛パジャマ_髪下ろし02d頬(中)',
	'IMG_5DAC01E0_凛パジ': '凛パジャマ_髪下ろし02d頬(近)',
	'IMG_6A100201_凛パジ': '凛パジャマ_髪下ろし02e頬(中)',
	'IMG_6A100222_凛パジ': '凛パジャマ_髪下ろし02f頬(中)',
	'IMG_6A100243_凛パジ': '凛パジャマ_髪下ろし02g頬(中)',
	'IMG_60DBF5C1_凛パジ': '凛パジャマ_髪下ろし02i頬(中)',
	'IMG_6A1003EE_凛パジ': '凛パジャマ_髪下ろし02j頬(中)',
	'IMG_60DBF5BE_凛パジ': '凛パジャマ_髪下ろし02l頬(中)',
	'IMG_6A1003AC_凛パジ': '凛パジャマ_髪下ろし02h頬(中)',
	'IMG_5DAC03AC_凛パジ': '凛パジャマ_髪下ろし02h頬(近)',
	'IMG_6A1002F9_凛パジ': '凛パジャマ_髪下ろし02m頬(中)',
	'IMG_6A1004A4_凛パジ': '凛パジャマ_髪下ろし02p頬(中)',
	'IMG_60DBF5C9_凛パジ': '凛パジャマ_髪下ろし02q頬(中)',
	'IMG_5DAC02F9_凛パジ': '凛パジャマ_髪下ろし02m頬(近)',
	'IMG_5DAC0222_凛パジ': '凛パジャマ_髪下ろし02f頬(近)',
	'IMG_8BF117D8_キャス': 'キャスターローブ無し02a(近)',
	'IMG_9D7FD2F3_キャス': 'キャスターローブ無し01h(中)',
	'IMG_9D7FD2F4_キャス': 'キャスターローブ無し01i(中)',
	'IMG_9D7FD2F0_キャス': 'キャスターローブ無し01m(中)',
	'IMG_8BF117DB_キャス': 'キャスターローブ無し02l(近)',
	'IMG_8BF117DC_キャス': 'キャスターローブ無し02m(近)',
	'IMG_EE30634C_キャス': 'キャスターローブ無し01g2(中)',
	'IMG_9D7FD2E6_キャス': 'キャスターローブ無し01g(中)',
	'IMG_9D7FD2EF_キャス': 'キャスターローブ無し01l(中)',
	'IMG_AD75D2E6_キャス': 'キャスターローブ無し03g(中)',
	'IMG_77E6D2F1_キャス': 'キャスターローブ無し02j(中)',
	'IMG_77E6D2F2_キャス': 'キャスターローブ無し02k(中)',
	'IMG_B75C63D7_キャス': 'キャスターローブ無し03a頬(近)',
	'IMG_956063D7_キャス': 'キャスターローブ無し03a頬(中)',
	'IMG_EE0F634C_キャス': 'キャスターローブ無し01g3(中)',
	'IMG_732C5BEE_キャス': 'キャスターローブ無し01c怒り(近)',
	'IMG_FEF13CFE_キャス': 'キャスターローブ無し01d(遠)',
	'IMG_D3D4F4FD_ライダ': 'ライダーエプロン04a頬(中)',
	'IMG_72258A82_セイバ': 'セイバー私服06a腕a(中)_sm05', # sm05
	'IMG_72258A82_セイバ': 'セイバー私服06a腕a(中)_sm05', # sm05
	'IMG_A76A51D2_セイバ': 'セイバーfd特殊02_肉まんc(中)',
	'IMG_4A11C66D_セイバ': 'セイバーfd特殊02_肉まんb(中)',
	'IMG_267520F8_セイバ': 'セイバーfd特殊02_肉まんa頬汗(近)',
	'IMG_57806CE0_セイバ': 'セイバーfd特殊02_肉まんb頬(中)',
	'IMG_FFC3DC29_セイバ': 'セイバーfd特殊02_肉まんa頬(中)',
	'IMG_9D90EB16_セイバ': 'セイバーfd特殊02_大判a(中)',
	'IMG_2BD8E2AE_セイバ': 'セイバーfd特殊02_大判a頬(中)',
	'IMG_2BD9A482_セイバ': 'セイバーfd特殊02_大判a頬(近)',
	'IMG_1ADBC99F_セイバ': 'セイバーfd特殊02_大判a頬汗(近)',
	'IMG_3017E2AE_セイバ': 'セイバーfd特殊03_大判a頬(中)',
	'IMG_3018A482_セイバ': 'セイバーfd特殊03_大判a頬(近)',
	'IMG_03BEDC29_セイバ': 'セイバーfd特殊03_肉まんa頬(中)',
	'IMG_4614C66D_セイバ': 'セイバーfd特殊03_肉まんb(中)',
	'IMG_46148769_セイバ': 'セイバーfd特殊03_肉まんb(近)',
	'IMG_A1D1EB16_セイバ': 'セイバーfd特殊03_大判a(中)',
	'IMG_A2B2EB16_セイバ': 'セイバーfd特殊03_大判b(近)',
	'IMG_A16EEB16_セイバ': 'セイバーfd特殊03_大判b(中)',
	'IMG_12D4A852_o冬木': 'o冬木大橋袂の公園1(秋)-(昼)',
	'IMG_94497E75_ランサ': 'ランサーエプロン花屋01g(中)_sm12', # sm12
	'IMG_94497E78_ランサ': 'ランサーエプロン花屋01d(中)_sm12', # sm12
	'IMG_94497E73_ランサ': 'ランサーエプロン花屋01a(中)',
	'IMG_94497E72_ランサ': 'ランサーエプロン花屋01b(中)',
	'IMG_94497E71_ランサ': 'ランサーエプロン花屋01c(中)',
	'IMG_94497E78_ランサ': 'ランサーエプロン花屋01d(中)',
	'IMG_94497E76_ランサ': 'ランサーエプロン花屋01f(中)',
	'IMG_94497E7B_ランサ': 'ランサーエプロン花屋01i(中)',
	'IMG_6EB07E73_ランサ': 'ランサーエプロン花屋02a(中)',
	'IMG_978E53F5_FD3': 'fd39(オブジェクト07・ゲイボルク)',
	'IMG_7A491ABA_iバゼ': 'iバゼットの隠れ家_内部(夢現)-(白)_sm10', # sm10
	'IMG_1F97A852_o冬木': 'o冬木大橋袂の公園2(秋)-(昼)',
	'IMG_6B7B5114_寸劇_': '寸劇_茶髪少年01a(通常_左)',
	'IMG_719CDFFB_寸劇_': '寸劇_茶髪少年01a(通常_中央)',
	'IMG_D67C3FCB_寸劇_': '寸劇_茶髪少年01a(通常_右)',
	'IMG_6E170772_寸劇_': '寸劇_眼鏡少年01a(通常_中央)',
	'IMG_06501F68_寸劇_': '寸劇_眼鏡少年01a(通常_右)',
	'IMG_AF8E8408_寸劇_': '寸劇_絆創膏少年02a(通常_左)',
	'IMG_F1A0DD07_寸劇_': '寸劇_絆創膏少年02a(通常_中央)',
	'IMG_E2E58408_寸劇_': '寸劇_絆創膏少年02a(通常_右)',
	'IMG_639AB9DF_寸劇_': '寸劇_絆創膏少年03a(特殊_弱気)',
	'IMG_BC0F8408_寸劇_': '寸劇_絆創膏少年03a(通常_左)',
	'IMG_FE1FDD07_寸劇_': '寸劇_絆創膏少年03a(通常_中央)',
	'IMG_A70C8408_寸劇_': '寸劇_絆創膏少年04a(通常_左)',
	'IMG_E92EDD07_寸劇_': '寸劇_絆創膏少年04a(通常_中央)',
	'IMG_DA638408_寸劇_': '寸劇_絆創膏少年04a(通常_右)',
	'IMG_0B956A60_寸劇_': '寸劇_セイバー01a(特殊_元気)',
	'IMG_473D87A6_寸劇_': '寸劇_セイバー01a(通常_左)',
	'IMG_C7207CEF_寸劇_': '寸劇_セイバー01a(通常_右)',
	'IMG_473D8B83_寸劇_': '寸劇_セイバー02a(通常_左)',
	'IMG_48DA05C7_寸劇_': '寸劇_セイバー02a(通常_中央)',
	'IMG_C72080CC_寸劇_': '寸劇_セイバー02a(通常_右)',
	'IMG_8940AFA3_寸劇_': '寸劇_セイバー02a(特殊_叫び)',
	'IMG_473D8B64_寸劇_': '寸劇_セイバー03a(通常_左)',
	'IMG_48DA01CA_寸劇_': '寸劇_セイバー03a(通常_中央)',
	'IMG_C72080AD_寸劇_': '寸劇_セイバー03a(通常_右)',
	'IMG_7C813FBC_寸劇_': '寸劇_セイバー03a(特殊_弱気)',
	'IMG_473D8B41_寸劇_': '寸劇_セイバー04a(通常_左)',
	'IMG_48D9FD55_寸劇_': '寸劇_セイバー04a(通常_中央)',
	'IMG_C720808A_寸劇_': '寸劇_セイバー04a(通常_右)',
	'IMG_473D8B22_寸劇_': '寸劇_セイバー05a(通常_左)',
	'IMG_48D9F948_寸劇_': '寸劇_セイバー05a(通常_中央)',
	'IMG_C720806B_寸劇_': '寸劇_セイバー05a(通常_右)',
	'IMG_48D9F723_寸劇_': '寸劇_セイバー06a(通常_中央)',
	'IMG_C7208058_寸劇_': '寸劇_セイバー06a(通常_右)',
	'IMG_B3CDCA61_FD1': 'fd16ex_サッカー寸劇a_sm05', # sm05
	'IMG_EA97DEA9_カレイ': 'カレイドステッキ(リアル)01b',
	'IMG_F7E3FF76_カレイ': 'カレイドステッキ(リアル)01b_sm60', # sm60
	'IMG_3EEAFF71_カレイ': 'カレイドステッキ(リアル)01b_sm15', # sm15
	'IMG_EFD4527D_カレイ': 'カレイドステッキ(マイルド)01b',
	'IMG_1068542E_カレイ': 'カレイドステッキ(マイルド)02',
	'IMG_EFD4527E_カレイ': 'カレイドステッキ(マイルド)01a',
	'IMG_F99E542E_カレイ': 'カレイドステッキ(マイルド)04',
	'IMG_9BCD542E_カレイ': 'カレイドステッキ(マイルド)03',
	'IMG_87B3B369_カレイ': 'カレイドステッキ(あおり)',
	'IMG_9DD4878A_カレイ': 'カレイドステッキ(マイルド)01b_sm10', # sm10
	'IMG_AE5E9438_カレイ': 'カレイドステッキ(マイルド)03_sm10', # sm10
	'IMG_03D99438_カレイ': 'カレイドステッキ(マイルド)04_sm10', # sm10
	'IMG_39C3943B_カレイ': 'カレイドステッキ(マイルド)03_sm03', # sm03
	'IMG_39C39434_カレイ': 'カレイドステッキ(マイルド)03_sm04', # sm04
	'IMG_9DD1878A_カレイ': 'カレイドステッキ(マイルド)01b_sm15', # sm15
	'IMG_27FB5BDD_カレイ': 'カレイドルビー01bステッキ_ラメ(中)',
	'IMG_41E25BDD_カレイ': 'カレイドルビー01aステッキ_ラメ(中)',
	'IMG_E30AD0D4_カレイ': 'カレイドルビー01b_ラメ(近)',
	'IMG_E2D7D0D4_カレイ': 'カレイドルビー01a_ラメ(近)',
	'IMG_2DF7C0CA_カレイ': 'カレイドルビー01b_ラメ(近)_sm04', # sm04
	'IMG_EEACF888_カレイ': 'カレイドルビー01b_ラメ(中)',
	'IMG_56735DA2_カレイ': 'カレイドルビー01cステッキ(中)',
	'IMG_5EF55DA2_カレイ': 'カレイドルビー01eステッキ(中)',
	'IMG_7FC55DA2_カレイ': 'カレイドルビー01dステッキ(遠)',
	'IMG_7FC5610F_カレイ': 'カレイドルビー02dステッキ(遠)',
	'IMG_5AB4610F_カレイ': 'カレイドルビー02dステッキ(中)',
	'IMG_6BD9610F_カレイ': 'カレイドルビー02aステッキ(中)',
	'IMG_5232610F_カレイ': 'カレイドルビー02bステッキ(中)',
	'IMG_5673610F_カレイ': 'カレイドルビー02cステッキ(中)',
	'IMG_74DD5A5D_カレイ': 'カレイドルビー02e_モノクロ(中)',
	'IMG_12109095_10汎': '10汎用バーサーカー03_sm12', # sm12
	'IMG_99D10A68_アーチ': 'アーチャー袖無し(白)01a(遠)',
	'IMG_9A340A68_アーチ': 'アーチャー袖無し(白)01d(遠)',
	'IMG_99F20A68_アーチ': 'アーチャー袖無し(白)01f(遠)',
	'IMG_9A3409C7_アーチ': 'アーチャー袖無し(白)02d(遠)',
	'IMG_9A5509C7_アーチ': 'アーチャー袖無し(白)02e(遠)',
	'IMG_99D10A26_アーチ': 'アーチャー袖無し(白)03a(遠)',
	'IMG_99D10A26_アーチ': 'アーチャー袖無し(白)03a(遠)',
	'IMG_9A340A26_アーチ': 'アーチャー袖無し(白)03d(遠)',
	'IMG_B7CD7A40_アーチ': 'アーチャー袖無し(白)01a(遠)_sm05', # sm05
	'IMG_CC207A40_アーチ': 'アーチャー袖無し(白)01d(遠)_sm05', # sm05
	'IMG_FE8956ED_アーチ': 'アーチャー袖無し05a(遠)_sm03', # sm03
	'IMG_E681B4BE_アーチ': 'アーチャー袖無し05a(遠)_sm20', # sm20
	'IMG_05AE1ABD_iバゼ': 'iバゼットの隠れ家_内部(夢現)-(白)_sm05', # sm05
	'IMG_7370E153_o新都': 'o新都_釣り場(慎二居る)-(昼)',
	'IMG_DC55A5C7_ランサ': 'ランサーギャルソン01a(中)',
	'IMG_9C21A5C7_ランサ': 'ランサーギャルソン01a(近)',
	'IMG_D45AA5C7_ランサ': 'ランサーギャルソン01b(中)',
	'IMG_9426A5C7_ランサ': 'ランサーギャルソン01b(近)',
	'IMG_CC5FA5C7_ランサ': 'ランサーギャルソン01c(中)',
	'IMG_8C2BA5C7_ランサ': 'ランサーギャルソン01c(近)',
	'IMG_043CA5C7_ランサ': 'ランサーギャルソン01d(中)',
	'IMG_FC41A5C7_ランサ': 'ランサーギャルソン01e(中)',
	'IMG_B412A5C7_ランサ': 'ランサーギャルソン01f(近)',
	'IMG_F446A5C7_ランサ': 'ランサーギャルソン01f(中)',
	'IMG_AC17A5C7_ランサ': 'ランサーギャルソン01g(近)',
	'IMG_EC4BA5C7_ランサ': 'ランサーギャルソン01g(中)',
	'IMG_AA86A5C7_ランサ': 'ランサーギャルソン01g(遠)',
	'IMG_6444A5C7_ランサ': 'ランサーギャルソン01h(近)',
	'IMG_9C7DA5C7_ランサ': 'ランサーギャルソン01i(中)',
	'IMG_5C49A5C7_ランサ': 'ランサーギャルソン01i(近)',
	'IMG_5C49A5C7_ランサ': 'ランサーギャルソン01i(近)',
	'IMG_ED2995D1_ランサ': 'ランサーギャルソン03a(中)',
	'IMG_B123115B_ランサ': 'ランサーギャルソン03a2(中)',
	'IMG_DD3395D1_ランサ': 'ランサーギャルソン03c(中)',
	'IMG_9CFF95D1_ランサ': 'ランサーギャルソン03c(近)',
	'IMG_151095D1_ランサ': 'ランサーギャルソン03d(中)',
	'IMG_0D1595D1_ランサ': 'ランサーギャルソン03e(中)',
	'IMG_CCE195D1_ランサ': 'ランサーギャルソン03e(近)',
	'IMG_051A95D1_ランサ': 'ランサーギャルソン03f(中)',
	'IMG_C4E695D1_ランサ': 'ランサーギャルソン03f(近)',
	'IMG_BB5A95D1_ランサ': 'ランサーギャルソン03g(遠)',
	'IMG_BCEB95D1_ランサ': 'ランサーギャルソン03g(近)',
	'IMG_FD1F95D1_ランサ': 'ランサーギャルソン03g(中)',
	'IMG_95A293D6_iファ': 'iファンシー-(アンバー)_sm80', # sm80
	'IMG_944A5870_ランサ': 'ランサーエプロン魚屋01a(中)',
	'IMG_7F86CF8A_ランサ': 'ランサーエプロン魚屋01d(遠)',
	'IMG_BD9C9A67_ランサ': 'ランサーエプロン花屋02a(近)',
	'IMG_53066483_ライダ': 'ライダーエプロン04a(遠)_sm05', # sm05
	'IMG_2A5FE513_キャス': 'キャスター私服01c(中)_sm05', # sm05
	'IMG_21D5F1D6_キャス': 'キャスター私服02a(中)_sm05', # sm05
	'IMG_E336745E_ランサ': 'ランサーエプロン魚屋01g(近)',
	'IMG_E336745B_ランサ': 'ランサーエプロン魚屋01h(近)',
	'IMG_F6C2D73C_RE0': 're07_ペルセウスvsメドゥーサa',
	'IMG_F6C3D73C_RE0': 're07_ペルセウスvsメドゥーサb',
	'IMG_F6C4D73C_RE0': 're07_ペルセウスvsメドゥーサc',
	'IMG_81AD4E96_セイバ': 'セイバー特殊03_タオル無しb(近)',
	'IMG_81AE0F32_セイバ': 'セイバー特殊03_タオル無しb(中)',
	'IMG_DF069A97_セイバ': 'セイバー特殊03_タオル無しa(中)',
	'IMG_DF05D9FB_セイバ': 'セイバー特殊03_タオル無しa(近)',
	'IMG_9961B57C_バゼッ': 'バゼット右手グローブ02a(遠)',
	'IMG_BDF6C8DD_バゼッ': 'バゼット右手グローブ01a(中)',
	'IMG_BDF6C8DC_バゼッ': 'バゼット右手グローブ01b(中)',
	'IMG_960FC8DC_バゼッ': 'バゼット右手グローブ02b(中)',
	'IMG_0E2E98D9_バゼッ': 'バゼット右手グローブ01b(中)_sm03', # sm03
	'IMG_7F5E88FA_o衛宮': 'o衛宮邸外観(秋)-(昼)_sm03', # sm03
	'IMG_7F6388F9_o衛宮': 'o衛宮邸外観(秋)-(昼)_sm14', # sm14
	'IMG_082C9CD3_バゼッ': 'バゼット右手グローブ02a(中)_sm14', # sm14
	'IMG_960FC8DD_バゼッ': 'バゼット右手グローブ02a(中)',
	'IMG_E595BEF2_バゼッ': 'バゼット03腕変えグローブa(中)',
	'IMG_E5B6BEF2_バゼッ': 'バゼット03腕変えグローブb(中)',
	'IMG_E5D7BEF2_バゼッ': 'バゼット03腕変えグローブc(中)',
	'IMG_806BE965_i衛宮': 'i衛宮邸_セイバー部屋_sm05', # sm05
	#'IMG_4811189E_ぬいぐ': 'ぬいぐるみ(後)',
	#'IMG_5065574F_ぬいぐ': 'ぬいぐるみ(後)',
	'IMG_E7DAB5C3_セイバ': 'セイバーfd特殊02_焼き芋a(中)',
	'IMG_A28BCC8D_セイバ': 'セイバーfd特殊02_焼き芋c(中)',
	'IMG_687DA923_セイバ': 'セイバーfd特殊03_焼き芋a頬(中)',
	'IMG_6482A923_セイバ': 'セイバーfd特殊02_焼き芋a頬(中)',
	'IMG_9EFF0E94_セイバ': 'セイバーfd特殊02_焼き芋d頬(中)',
	'IMG_45334128_セイバ': 'セイバーfd特殊02_焼き芋b(中)',
	'IMG_151FFCCA_セイバ': 'セイバーfd特殊02_焼き芋d(中)',
	'IMG_48FF4490_32形': '32形の無い島・石像c(オブジェクト)',
	'IMG_3AE98D71_32形': '32形の無い島・石像b(オブジェクト)',
	'IMG_BAF963C2_キャス': 'キャスターローブ無し02b頬(中)',
	'IMG_77E6D2E5_キャス': 'キャスターローブ無し02f(中)',
	'IMG_9D7FD2F1_キャス': 'キャスターローブ無し01j(中)',
	'IMG_7C6525EA_セイバ': 'セイバー私服_鍋持ち開09a(中)',
	'IMG_7CC825EA_セイバ': 'セイバー私服_鍋持ち開09b(中)',
	'IMG_84B44CD3_i衛宮': 'i衛宮邸_セイバー部屋-(夜)',
	'IMG_D21909C6_i衛宮': 'i衛宮邸客間(凛)-(夜)_sm06',
	'IMG_C339283A_i衛宮': 'i衛宮邸居間(fd)-(夜)_sm10',
	'IMG_F34D6C98_i衛宮': 'i衛宮邸居間(fd)-(夜)_sm06',
	'IMG_33EB3202_i衛宮': 'i衛宮邸居間(fd)(酒盛りa)-(夜)',
	'IMG_B6886F1B_i衛宮': 'i衛宮邸居間(fd)(酒盛りb)-(夜)',
	'IMG_0DDB9D20_i衛宮': 'i衛宮邸居間(fd)(酒盛りc)-(夜)',
	'IMG_6264BEE9_i衛宮': 'i衛宮邸居間(fd)(酒盛りd)-(夜)',
	'IMG_D0864CD4_i衛宮': 'i衛宮邸_ライダー部屋-(夜)',
	'IMG_9E1CFB0B_i衛宮': 'i衛宮邸_ライダー部屋-(夜)_sm06',
	'IMG_404BFB0B_i衛宮': 'i衛宮邸_ライダー部屋-(夜)_sm05',
	'IMG_8D17B0A3_ライダ': 'ライダーのうねる髪(オブジェクトb泡)',
	'IMG_8D17B0A0_ライダ': 'ライダーのうねる髪(オブジェクトa泡)',
	'IMG_2168B3F6_A29': 'a29(fd)_背景のみ(湯気少)',
	'': '',
}

SPECIAL_PARAMETER = { 'target':TARGET, 'page':PAGE, 'rule':RULE, 'pos':POS, 'layer':LAYER, 'nowait':TRUE_FALSE, 'type':NOISE_TYPE, 'base': STORAGES }
