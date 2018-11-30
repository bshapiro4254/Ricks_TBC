BLUE="\033[1;36m"
RED="\033[1;31m"
YELLOW="\033[1:32m"
LIGHT_RED="\033[1;31m"
WHITE="\033[1;37m"
GREEN="\033[1;32m"
GREY="\033[1;30m"
BLACK="\033[0;30m"
BLUEBKGD ="\033[0;44m"
GREENBKGD ="\033[0;42m"
GREYBKGD ="\033[0;47m"
WHITEBKGD ="\033[0;39m"
BLACKBKGD ="\033[0;80m"
REDBKGD ="\033[0;41m"
NO_COLOUR="\033[0m"
#.format(BLACK,WHITE,RED,BLUE,GREEN,YELLOW,BLACKBKGD,WHITEBKGD,REDBKGD,BLUEBKGD,GREENBKGD,GREYBKGD)





pickle='''\033[2;3H
\033[3;3HPPPPPPPPPPPP
\033[4;3HPPPP    PPPPP                  KK         LLL  EEEEEEEEE
\033[5;3HPPPP     PPPPP  I   CCCCCCCCCC KK    KKK  LLL  EEEE
\033[6;3HPPPP      PPPP III  CCCC    CC KK   KKK   LLL  EE
\033[7;3HPPPP      PPP   I   CCC      C KK  KKK    LLL  EEEE
\033[8;3HPPPP     PPP        CC         KKKKKK     LLL  EEEEEEE
\033[9;3HPPPPPPPPPPP    III  CC         KKKK       LLL  EEEE
\033[10;3HPPPP          IIIII CC         KKKKK      LLL  EE
\033[11;3HPPP           IIIII CC         KKKKKK     LLL  EEEE
\033[12;3HPPP           IIIII CCC      C KK  KKKK   LLL  EEEEEEEEE
\033[13;3HPPP           IIIII CCCC    CC KK   KKKK  LLLL
\033[14;3HPPP           IIIII CCCC    CC KK   KKKK  LLLLL     LL
\033[15;3HPPP            III  CCCCCCCCCC KK    KKKK LLLLLLLLLLLL
'''.format(BLACK,WHITE,RED,BLUE,GREEN,YELLOW,BLACKBKGD,WHITEBKGD,REDBKGD,BLUEBKGD,GREENBKGD,GREYBKGD)

Rick='''\033[2;80
\033[3;80HRRRRRRRR                                ###
\033[4;80HRRR   RRR                   KK        #####
\033[5;80HRR     RRR    I             KK   KK  #####
\033[6;80HRR     RRR   III CCCCCCCCCC KK  KK   ###  SSSSSSS
\033[7;80HRRR   RRR     I  CCC     CC KKKKK        SS     SS
\033[8;80HRRRRRRRR         CC         KKKK        SS       SS
\033[9;80HRR   RRRR    III CC         KKKKK        SS
\033[10;80HRR     RRR   III CC         KK  KK        SSSSSSSS
\033[11;80HRR      RRR  III CCC     CC KK   KK             SSS
\033[12;80HRR        RR III CCCCCCCCCC KK    KK            SSSS
\033[13;80HRRSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
\033[14;80HRRSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
'''
kosher='''\033[16;1H
\033[17;1HKK    KK                                      RRRRRR
\033[18;1HKK   KK                                       RRR  RRR
\033[19;1HKK  KK                     HH   HH  EEEEEEEE  RR    RRR
\033[20;1HKKKKK      OOOOO    SSSS   HH   HH  EEE   EE  RR    RRR
\033[21;1HKKKK      OOO OOO  SS  SS  HH   HH  EE        RRR  RRR
\033[22;1HKKKKKK    OO   OO SS       HHHHHHH  EEEEEE    RRRRRRR
\033[23;1HKK   KK   O     O  SSSSSS  HHHHHHH  EEEEEE    RR   RRRR
\033[24;1HKK    KK  OO   OO       SS HH   HH  EE        RR     RRR
\033[25;1HKK     KK OOO OOO  SS  SS  HH   HH  EEE   EE  RR      RRR
\033[26;1HKK      KK OOOOO    SSSS   HH   HH  EEEEEEEE  RR        RR
'''.format(BLACK,WHITE,RED,BLUE,GREEN,YELLOW,BLACKBKGD,WHITEBKGD,REDBKGD,BLUEBKGD,GREENBKGD,GREYBKGD)

casino='''\033[19;75H
\033[20;75H   CCCCCCCC
\033[21;75H  CCCCCCCCCC    SSSSSSS    I  NN     NN     OOOOO
\033[22;75H CCC    AA CC  SS     SS  III NNN    NN    OO   OO
\033[23;75HCCC    AAAA C SS       S   I  NNNN   NN   OO     OO
\033[24;75HCC    AA^^AA   SS             NN NN  NN  OO       OO
\033[25;75HCC    AA  AA    SSSSSSS    I  NN  NN NN  OO       OO
\033[26;75HCC    AAAAAA          SS  III NN   NNNN  OO       OO
\033[27;75HCCC   AA^^AA           SS III NN    NNN   OO     OO
\033[28;75HCCCC  AA  AA   SS     SS  III NN     NN    OO   OO
\033[29;75HCCCCC AA  AA    SSSSSSS    I  NN      N     OOOOO
\033[30;75H  CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
\033[31;75H    CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
'''.format(BLACK,WHITE,RED,BLUE,GREEN,YELLOW,BLACKBKGD,WHITEBKGD,REDBKGD,BLUEBKGD,GREENBKGD,GREYBKGD)

picklerick='''\033[10;20H
\033[11;20H                   _____
\033[12;20H                   |A A|
\033[13;20H                ___| H |
\033[14;20H                |Q Q|_A|
\033[15;20H              __| D |___
\033[16;20H              |**|**|**|                                            ____
\033[17;20H              |**|**|**|                                            \9 9\__
\033[18;20H              |**|**|**|                                             \ \K K\
\033[19;20H              |__|**|__|               _________________             _\9\ S \_
\033[20;20H                 |**|               _/                  \__          \__\**\__\
\033[21;20H                 |**|            __/  _             _      \___       \__\**\__\
\033[22;20H                 |**|           /     \\____   ____//         \\       \__\**\__\
\033[23;20H                 |**|          ||      ____ \_/ _____         ||        \__\**\__\
\033[24;20H                 |**|          |      /     \ /     \         ||            \**\
\033[26;20H                 \**\        //      |  ** | |  ** |         ||             \**\
\033[27;20H                  \**\       ||      |  ** | |  ** |         ||              \**\
\033[28;20H                   \**\    __||      |     | |     |         |__              \**\
\033[29;20H                    \**\  /==\\      \_____/ \_____/        //==\              \**\
\033[30;20H                     \**\/====\\                           //====\______________\**\
\033[31;20H                      \|========>                       <========|******************\
\033[32;20H                         \====//   /^^\           /^^\     \\====/====================+
\033[33;20H                          \__/||   \***\_________/***/     ||\__/
\033[34;20H                            //||    |***************|      ///||
\033[35;20H                           ||_^_     \*************/       _^_||
\033[36;20H                          <<+|=|+>>>>  |@@|@@|@@@|     <<<<+|=|+>>
\033[37;20H                           |//|\\\    \+++++++++++/      ///|\\|
\033[38;20H                           |\\_///      \@/\@/\@@/       \\\_//|
\033[39;20H                           |||          \@/   \@@/           |||
\033[40;20H                           |||                               |||
\033[41;20H                           |||                               |||
\033[42;20H                           ||_^_                           _^_||
\033[43;20H                           |//|\\\                       ///|\\|
\033[44;20H                          <<+|=|+>>>>                 <<<<+|=|+>>
\033[45;20H                           |\\_///                       \\\_//|
'''.format(BLACK,WHITE,RED,BLUE,GREEN,YELLOW,BLACKBKGD,WHITEBKGD,REDBKGD,BLUEBKGD,GREENBKGD,GREYBKGD)
print picklerick
print pickle
print Rick
print kosher
print casino
