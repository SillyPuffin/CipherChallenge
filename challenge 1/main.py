#basics
alpha = "abcdefghijklmnopqrstuvwxyz"
text = "AHKLE XRMHP XKLXT LMAHK LEXRL NKKXR XGZET GWFRW XTKFK LEHOX ETVXB PTLNG LNKXA HPMHT WWKXL LRHNL HBAHI XMATM MABLE XMMXK YBGWL RHNTG WYBGW LRHNP XEEBT FPKBM BGZUX VTNLX BWHGH MDGHP PAHXE LXMHM NKGMH TGWBY BZNKX MATMR HNFBZ AMUXT UEXMH AXEIB TFLHK KRYHK MAXMK HNUEX BFTRA TOXVT NLXWU RVRIA XKBGZ MABLE XMMXK UNMBP TLGHM LNKXM ATMRH NPHNE WKXTW TFXLL TZXLX GMBGF RATGW GHMDG HPBGZ GHMAB GZTUH NMFXB MLXXF XWFHK XEBDX ERRHN PHNEW FTDXM AXXYY HKMBY MAXFX LLTZX PTLAT KWXKM HKXTW BYGHM TGWBT FPKHG ZTUHN MRHNK BGMXK XLMLB GVHWX LTGWV RIAXK LMAXG IXKAT ILBMP HGMFT MMXKP AXMAX KRHNK XTWBM HKGHM BTFTW XMXVM BOXBG MAXLF TEEMH PGHYX KBGGX PRHKD TGWBG TKXVX GMBGO XLMBZ TMBHG BVTFX NIHGT LMKTG ZXGXL LMATM BVTGG HMNGI BVDBP TLTLD XWMHB GOXLM BZTMX TUKXT DBGTM TEHVT EPTKX AHNLX MAXAT LIATW UXXGK XFHOX WTGWV ENFLB ERKXI ETVXW TEXKM BGZMA XHPGX KUNMG HMABG ZLXXF XWMHU XFBLL BGZTG WMAXL ABIIB GZVKT MXLKX FTBGX WLXTE XWUXA BGWMA XFBYH NGWTU NEEXM VTKKR BGZTG NGNLN TEBGL VKBIM BHGTG WATOX BGVEN WXWTL DXMVA BMBLF BZAMR NGNLN TEYHK TVTLX MHUXF TKDXW BGMAB LPTRT GWMAX EXMMX KLFTD XGHLX GLXMH FXBTF AHIBG ZMATM RHNPB EEUXT UEXMH AXEIB GMXKI KXMMA XFPBM AENVD MATMF BZAML AXWLH FXEBZ AMHGF RBGOX LMBZT MBHGZ BOXGM AXUNE EXMPT LYHNG WPBMA TLABI FXGMU HNGWY HKXGZ ETGWM AXKXF TRTEL HUXKX TLHGY HKRHN MHUXP HKKBX WUNMB FHLML BGVXK XERAH IXGHM BYRHN ATOXK XTWMA BLYTK MAXGI EXTLX NGWXK LMTGW AHPFN VABTI IKXVB TMXRH NKTLL BLMTG VXBEH HDYHK PTKWP BMALH FXXTZ XKGXL LMHRH NKKXI ERPBM AFRZK TMBMN WXFBL LDTMX PTKGX" 


def common(text):
    let_dict = {}
    for letter in text:
        if letter != " ":
            if letter in list(let_dict.keys()):
                let_dict[letter] += 1
            else:
                let_dict[letter] = 1

    max = 0
    mletter = ""
    for letter in let_dict:
        if let_dict[letter] > max:
            mletter = letter
            max = let_dict[letter]
    
    # print(let_dict)

    return mletter


def find_shift(first,second):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    firstindex = alpha.index(first)
    secondindex = alpha.index(second)
    return secondindex - firstindex

#x is porobably eee

eindex = alpha.index("e")

new_text = ""
dif = find_shift("x","e")
spacecount = 0
print(dif)
for letter in text:
    if letter != " ":
        new_text += alpha[(alpha.index(letter.lower())+dif)%26]
    if letter == " ":
        spacecount += 1
for i in range(spacecount):
    new_text += " "
print(new_text)
print(len(text),len(new_text))