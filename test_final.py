from collections import Counter
from math import log10
from scipy.stats import chi2_contingency
import random

lang = [32] + [i for i in range(97,123)] # ascii values of all characters in language
plaintexts_dict1 = []
bigrams = {'th': 116997844, 'he': 100689263, 'in': 87674002, 'er': 77134382, 'an': 69775179, 're': 60923600, 'es': 57070453, 'on': 56915252, 'st': 54018399, 'nt': 50701084, 'en': 48991276, 'at': 48274564, 'ed': 46647960, 'nd': 46194306, 'to': 46115188, 'or': 45725191, 'ea': 43329810, 'ti': 42888666, 'ar': 42353262, 'te': 42295813, 'ng': 38567365, 'al': 38211584, 'it': 37938534, 'as': 37773878, 'is': 37349981, 'ha': 35971841, 'et': 32872552, 'se': 31532272, 'ou': 31112284, 'of': 30540904, 'le': 30383262, 'sa': 30080131, 've': 29320973, 'ro': 29230770, 'ra': 28645577, 'ri': 27634643, 'hi': 27495342, 'ne': 27331675, 'me': 27237733, 'de': 27029835, 'co': 26737101, 'ta': 26147593, 'ec': 25775798, 'si': 25758841, 'll': 24636875, 'so': 23903631, 'na': 23547524, 'li': 23291169, 'la': 23178317, 'el': 23092248, 'ma': 21828378, 'di': 21673998, 'ic': 21468412, 'rt': 21456059, 'ns': 21306421, 'rs': 21237259, 'io': 21210160, 'om': 21066156, 'ch': 20132750, 'ot': 20088048, 'ca': 19930754, 'ce': 19803619, 'ho': 19729026, 'be': 19468489, 'tt': 19367472, 'fo': 18923772, 'ts': 18922522, 'ss': 18915696, 'no': 18894111, 'ee': 18497942, 'em': 18145294, 'ac': 17904683, 'il': 17877600, 'da': 17584055, 'ni': 17452104, 'ur': 17341717, 'wa': 16838794, 'sh': 16773127, 'ei': 16026915, 'am': 15975981, 'tr': 15821226, 'dt': 15759673, 'us': 15699353, 'lo': 15596310, 'pe': 15573318, 'un': 15237699, 'nc': 15214623, 'wi': 15213018, 'ut': 15137169, 'ad': 14877234, 'ew': 14776406, 'ow': 14610429, 'ge': 14425023, 'ep': 14024377, 'ai': 13974919, 'ly': 13742031, 'ol': 13726491, 'ft': 13696078, 'os': 13596265, 'eo': 13524186, 'ef': 13252227, 'pr': 13191182, 'we': 13185116, 'do': 13120322, 'mo': 12950768, 'id': 12896787, 'ie': 12505546, 'mi': 12168944, 'pa': 12068709, 'fi': 11993833, 'po': 11917535, 'ct': 11888752, 'wh': 11852909, 'ir': 11681353, 'ay': 11523416, 'ga': 11239788, 'sc': 10800636, 'ke': 10650670, 'ev': 10574011, 'sp': 10570626, 'im': 10544422, 'op': 10459455, 'ds': 10429887, 'ld': 10245579, 'ul': 10173468, 'oo': 10168856, 'su': 10031005, 'ia': 10002012, 'gh': 9880399, 'pl': 9812226, 'eb': 9738798, 'ig': 9530574, 'vi': 9380037, 'iv': 9129232, 'wo': 9106647, 'yo': 9088497, 'rd': 9025637, 'tw': 8910254, 'ba': 8867461, 'ag': 8809266, 'ry': 8788539, 'ab': 8775582, 'ls': 8675452, 'sw': 8673234, 'ap': 8553911, 'fe': 8529289, 'tu': 8477495, 'ci': 8446084, 'fa': 8357929, 'ht': 8351551, 'fr': 8339376, 'av': 8288885, 'eg': 8286463, 'go': 8188708, 'bo': 8172395, 'bu': 8113271, 'ty': 8008918, 'mp': 7835172, 'oc': 7646952, 'od': 7610214, 'eh': 7559141, 'ys': 7539621, 'ey': 7528342, 'rm': 7377989, 'ov': 7350014, 'gt': 7347990, 'ya': 7239548, 'ck': 7205091, 'gi': 7103140, 'rn': 7064635, 'gr': 6989963, 'rc': 6974063, 'bl': 6941044, 'lt': 6817273, 'yt': 6714151, 'oa': 6554221, 'ye': 6499305, 'ob': 6212512, 'db': 6106719, 'ff': 6085519, 'sf': 6073995, 'rr': 5896212, 'du': 5861311, 'ki': 5814357, 'uc': 5742385, 'if': 5740414, 'af': 5702567, 'dr': 5701879, 'cl': 5683204, 'ex': 5649363, 'sm': 5580755, 'pi': 5559210, 'sb': 5553684, 'cr': 5514347, 'tl': 5403137, 'oi': 5336616, 'ru': 5330557, 'up': 5306948, 'by': 5232074, 'tc': 5196817, 'nn': 5180899, 'ak': 5137311, 'sl': 4965012, 'nf': 4950333, 'ue': 4927837, 'dw': 4906814, 'au': 4884168, 'pp': 4873393, 'ug': 4832325, 'rl': 4803246, 'rg': 4645938, 'br': 4621080, 'cu': 4604045, 'ua': 4589997, 'dh': 4585765, 'rk': 4491400, 'yi': 4461214, 'lu': 4402940, 'um': 4389720, 'bi': 4356462, 'ny': 4343290, 'nw': 4215967, 'qu': 4169424, 'og': 4163126, 'sn': 4157990, 'mb': 4121764, 'va': 4111375, 'df': 4033878, 'dd': 4001275, 'ms': 3922855, 'gs': 3920675, 'aw': 3918960, 'nh': 3915410, 'pu': 3858148, 'hr': 3843001, 'sd': 3842250, 'tb': 3815459, 'pt': 3812475, 'nm': 3796928, 'dc': 3782481, 'gu': 3768430, 'tm': 3759861, 'mu': 3755834, 'nu': 3732602, 'mm': 3730508, 'nl': 3692985, 'eu': 3674130, 'wn': 3649615, 'nb': 3602692, 'rp': 3588188, 'dm': 3544905, 'sr': 3513808, 'ud': 3499535, 'ui': 3481482, 'rf': 3436232, 'ok': 3397570, 'yw': 3379064, 'tf': 3368452, 'ip': 3348621, 'rw': 3348005, 'rb': 3346212, 'oh': 3254659, 'ks': 3227333, 'dp': 3145043, 'fu': 3138900, 'yc': 3128053, 'tp': 3070427, 'mt': 3055946, 'dl': 3050945, 'nk': 3043200, 'cc': 3026492, 'ub': 2990868, 'rh': 2968706, 'np': 2968126, 'ju': 2924815, 'fl': 2890839, 'dn': 2840522, 'ka': 2833038, 'ph': 2825344, 'hu': 2771830, 'jo': 2721345, 'lf': 2702522, 'yb': 2696786, 'rv': 2692445, 'oe': 2616308, 'ib': 2598444, 'ik': 2585124, 'yp': 2581863, 'gl': 2576787, 'lp': 2543957, 'ym': 2516273, 'lb': 2463693, 'hs': 2462026, 'dg': 2442139, 'gn': 2426429, 'ek': 2411639, 'nr': 2393580, 'ps': 2377036, 'td': 2346516, 'lc': 2328063, 'sk': 2321888, 'yf': 2305244, 'yh': 2291273, 'vo': 2253292, 'ah': 2225270, 'dy': 2218040, 'lm': 2216514, 'sy': 2214270, 'nv': 2194534, 'yd': 2122337, 'fs': 2047416, 'sg': 2043770, 'yr': 2021939, 'yl': 2013939, 'ws': 1988727, 'my': 1949129, 'oy': 1932892, 'kn': 1903836, 'iz': 1865802, 'xp': 1840696, 'lw': 1836811, 'tn': 1782119, 'ko': 1758001, 'aa': 1721143, 'ja': 1712763, 'ze': 1709871, 'fc': 1570791, 'gw': 1567991, 'tg': 1530045, 'xt': 1509969, 'fh': 1507604, 'lr': 1505092, 'je': 1487348, 'yn': 1485655, 'gg': 1468286, 'gf': 1465290, 'eq': 1461436, 'hy': 1446451, 'kt': 1443985, 'hc': 1441057, 'bs': 1409672, 'hw': 1403223, 'hn': 1383958, 'cs': 1381608, 'hm': 1353001, 'nj': 1342735, 'hh': 1329998, 'wt': 1301293, 'gc': 1299541, 'lh': 1274048, 'ej': 1256993, 'fm': 1251312, 'dv': 1238565, 'lv': 1238287, 'wr': 1226755, 'gp': 1215204, 'fp': 1199845, 'gb': 1184377, 'gm': 1178511, 'hl': 1169468, 'lk': 1164186, 'cy': 1145316, 'mc': 1101727, 'yg': 1049082, 'xi': 1024736, 'hb': 1014004, 'fw': 1005903, 'gy': 979804, 'hp': 978649, 'mw': 937621, 'pm': 931225, 'za': 929119, 'lg': 926472, 'iw': 922059, 'xa': 904148, 'fb': 888155, 'sv': 882083, 'gd': 879792, 'ix': 879360, 'aj': 870262, 'kl': 846309, 'hf': 834284, 'hd': 828755, 'ae': 815963, 'sq': 800346, 'dj': 799366, 'fy': 789961, 'az': 768359, 'ln': 752316, 'ao': 749566, 'fd': 748027, 'kw': 719633, 'mf': 715087, 'mh': 710864, 'sj': 704442, 'uf': 701892, 'tv': 698150, 'xc': 697995, 'yu': 695512, 'bb': 689158, 'ww': 674610, 'oj': 661082, 'ax': 660826, 'mr': 660619, 'wl': 657782, 'xe': 653947, 'kh': 650095, 'ox': 650078, 'uo': 649906, 'zi': 644035, 'fg': 637758, 'ih': 610683, 'tk': 610333, 'ii': 607124, 'iu': 576683, 'tj': 559473, 'mn': 558397, 'wy': 553647, 'ky': 553296, 'kf': 537342, 'fn': 534362, 'uy': 531960, 'pw': 530411, 'dk': 525744, 'rj': 518157, 'uk': 514873, 'kr': 507020, 'ku': 506618, 'wm': 505687, 'km': 485617, 'md': 481126, 'ml': 478528, 'ez': 465466, 'kb': 457860, 'wc': 448394, 'wd': 432646, 'hg': 429607, 'bt': 428276, 'zo': 424016, 'kc': 420017, 'pf': 418168, 'yv': 411487, 'pc': 400308, 'py': 396147, 'wb': 394820, 'yk': 391953, 'cp': 382923, 'yj': 378679, 'kp': 375653, 'pb': 369336, 'cd': 358435, 'ji': 357577, 'uw': 352732, 'uh': 339341, 'wf': 336213, 'yy': 332973, 'wp': 321746, 'bc': 320380, 'aq': 315068, 'cb': 298053, 'iq': 291635, 'cm': 285942, 'mg': 285133, 'dq': 283314, 'bj': 282608, 'tz': 280007, 'kd': 277982, 'pd': 273162, 'fj': 269865, 'cf': 267630, 'nz': 266461, 'cw': 257253, 'fv': 244685, 'vy': 233082, 'fk': 228905, 'oz': 228556, 'zz': 221275, 'ij': 219128, 'lj': 218362, 'nq': 217422, 'uv': 212051, 'xo': 211173, 'pg': 211133, 'hk': 210385, 'kg': 209266, 'vs': 204093, 'hv': 197539, 'bm': 191807, 'hj': 189906, 'cn': 188046, 'gv': 186777, 'cg': 181590, 'wu': 180884, 'gj': 176947, 'xh': 166599, 'gk': 163830, 'tq': 159111, 'cq': 157546, 'rq': 156933, 'bh': 154489, 'xs': 154347, 'uz': 153736, 'wk': 148964, 'xu': 147533, 'ux': 144814, 'bd': 141752, 'bw': 140189, 'wg': 139890, 'mv': 136314, 'mj': 134263, 'pn': 131645, 'xm': 127492, 'oq': 122677, 'bv': 120081, 'xw': 119322, 'kk': 118811, 'bp': 115161, 'zu': 113538, 'rz': 113432, 'xf': 113031, 'mk': 111041, 'zh': 107639, 'bn': 106125, 'zy': 105871, 'hq': 101241, 'wj': 99435, 'iy': 98361, 'dz': 98038, 'vr': 96416, 'zs': 94993, 'xy': 94329, 'cv': 94224, 'xb': 94041, 'xr': 90046, 'uj': 88168, 'yq': 87953, 'vd': 85611, 'pk': 83017, 'vu': 82830, 'jr': 80471, 'zl': 80039, 'sz': 79840, 'yz': 78281, 'lq': 77148, 'kj': 76816, 'bf': 75352, 'nx': 74844, 'qa': 73527, 'qi': 73387, 'kv': 73184, 'zw': 68865, 'wv': 63930, 'uu': 63043, 'vt': 62912, 'vp': 62577, 'xd': 60101, 'gq': 59750, 'xl': 59585, 'vc': 59024, 'cz': 57914, 'lz': 57314, 'zt': 56955, 'wz': 52836, 'sx': 50975, 'zb': 50652, 'vl': 49032, 'pv': 48105, 'fq': 47504, 'pj': 47043, 'zm': 46034, 'vw': 45608, 'cj': 41526, 'zc': 41037, 'bg': 40516, 'js': 39326, 'xg': 39289, 'rx': 38654, 'hz': 37066, 'xx': 35052, 'vm': 35024, 'xn': 34734, 'qw': 34669, 'jp': 34520, 'vn': 33082, 'zd': 32906, 'zr': 32685, 'fz': 31186, 'xv': 31117, 'zp': 30389, 'vh': 30203, 'vb': 29192, 'zf': 28658, 'gz': 28514, 'tx': 28156, 'vf': 28090, 'dx': 27413, 'qb': 27307, 'bk': 26993, 'zg': 26369, 'vg': 25585, 'jc': 24770, 'zk': 24262, 'zn': 24241, 'uq': 23386, 'jm': 22338, 'vv': 22329, 'jd': 21903, 'mq': 21358, 'jh': 20960, 'qs': 20847, 'jt': 20408, 'jb': 19380, 'fx': 19313, 'pq': 18607, 'mz': 18271, 'yx': 16945, 'qt': 16914, 'wq': 16245, 'jj': 16085, 'jw': 16083, 'lx': 15467, 'gx': 14778, 'jn': 14452, 'zv': 14339, 'mx': 14250, 'jk': 13967, 'kq': 13905, 'xk': 13651, 'jf': 12640, 'qm': 12315, 'qh': 12273, 'jl': 12149, 'jg': 12023, 'vk': 11469, 'vj': 11432, 'kz': 11192, 'qc': 10667, 'xj': 10629, 'pz': 9697, 'ql': 9603, 'qo': 9394, 'jv': 8925, 'qf': 8778, 'qd': 8678, 'bz': 8132, 'hx': 7526, 'zj': 7167, 'px': 6814, 'qp': 6062, 'qe': 6020, 'qr': 5975, 'zq': 5773, 'jy': 5723, 'bq': 5513, 'xq': 5416, 'cx': 5300, 'kx': 5083, 'wx': 4678, 'qy': 4557, 'qv': 4212, 'qn': 3808, 'vx': 3192, 'bx': 3021, 'jz': 2859, 'vz': 2633, 'qg': 2567, 'qq': 2499, 'zx': 2463, 'xz': 2082, 'qk': 2023, 'vq': 1488, 'qj': 1342, 'qx': 765, 'jx': 747, 'jq': 722, 'qz': 280}
bigram_p={}
ss = sum(bigrams.values())
for key in bigrams.keys():
    bigram_p[key] = log10(float(bigrams[key])/ss)
score_floor = log10(0.01/ss)

# Convert character to index in lang
def ind(character):
    if character == ' ': return 0
    else: return ord(character) - 96

# Calculate Digram frequency
def calc_freq_bigram(input_str):
    freq = Counter(input_str[i:i+2] for i in range(len(input_str)-1))
    freq_s = sorted(list(freq.values()), reverse=True)
    return freq_s

# Calculate Plaintext frequencies from dictionary 1
def read_dict1():
    with open('plaintext_dictionary_test1.txt', 'r') as f:
        for line in f.readlines():
            if len(line) < 30: continue
            #perform frequency analysis
            plaintexts_dict1.append({
                'text': line.strip(),
                'freq': calc_freq_bigram(line.strip()),
            })

# Calc Chi-Squared statistic to get closest plaintext match for Test 1
def get_chi2_match(ct):
    fr_ct = calc_freq_bigram(ct)
    chi_tests_stat=[]
    for plain in plaintexts_dict1: # Calc chi-squared per plaintext
        fr_pt = plain['freq']
        stat, p, dof, exp = chi2_contingency([fr_ct[:15], fr_pt[:15]])
        chi_tests_stat.append(stat)
    min_stat = min(chi_tests_stat) # lower stat means greater affinity
    match_stat = chi_tests_stat.index(min_stat)
    stat_val_adjusted = min_stat * (500/len(ct))
    return match_stat, stat_val_adjusted # return matched plaintext index and chi-squared stat value adjusted according to ciphertext length

# Compute fitness score of text based on bigrams in english
def bigram_score(text):
    score=0
    for i in range(len(text) - 1):
        if text[i:i+2] in bigram_p: score += bigram_p.get(text[i:i+2])
        else: score += score_floor
    return score

# Decipher ciphertext based on given key
def decipher(ct, key):
    pt=[]
    for c in ct:
        pt.append(chr(key[ind(c)]))
    return ''.join(pt)


#### Main ####
read_dict1()
input_ct = input("Enter the ciphertext: ")


#### Test 1 ####
match1, test1val = get_chi2_match(input_ct)
print("Plaintext guess for Test 1:\n", plaintexts_dict1[match1]['text'], sep='')


#### Test 2 ####
print("\n Processing Test 2...")
maxscore = -99e9
parentscore = maxscore
parentkey = lang[:]
maxkey = parentkey[:]
for _ in range(4):
    random.shuffle(parentkey)
    deciphered = decipher(input_ct, parentkey)
    parentscore = bigram_score(deciphered)
    iterc=0
    while iterc < 1000:
        iterc += 1
        a = random.randint(0,26)
        b = random.randint(0,26)
        child = parentkey[:]
        child[a], child[b] = child[b], child[a] # swap 2 random chars
        deciphered = decipher(input_ct, child)
        score = bigram_score(deciphered)
        if score > parentscore:
            parentscore, parentkey = score, child[:]
            iterc = 0
    if parentscore > maxscore:
        maxscore, maxkey = parentscore, parentkey[:]

test2_pt = decipher(input_ct, maxkey)
print("Plaintext guess for Test 2:\n", test2_pt, sep='')
maxkey = [chr(k) for k in maxkey]
print("Key guessed:",''.join(maxkey))