
import math
class Solution:
    memo={}
    def count(self, coins, N, Sum):

        self.memo={}
        return self.fun(0,Sum,coins)
        
        
    def fun(self,i,sum,given):

        count=0
        if sum==0:
            count=1
        elif sum>0 and i==len(given):
            count=0
        else:
            if given[i]>sum:
                count=0
            elif given[i]==sum:
                count=1
            else:
                times=math.floor(sum/given[i])
                k=0
                temp=0
                while k<=times:
                    temp=temp+self.fun(i+1,sum-k*given[i],given)
                    k+=1
                count=temp
        return count


cl =Solution()
Sum = 7
N = 929
coins=[2,3]
#coins =[1,9,11,23,24,40,62,63,65,82,90,102,107,110,124,131,140,158,162,174,176,179,193,196,213,231,233,238,242,246,259,262,269,270,286,290,297,304,322,324,335,375,392,395,403,423,425,453,456,463,469,483,485,489,496,499,527,537,543,558,567,578,591,595,604,605,607,610,643,654,661,667,683,688,708,716,720,722,727,772,794,809,817,828,832,835,838,851,855,856,865,878,883,888,894,913,914,917,919,928,931,950,958,1002,1023,1024,1055,1063,1068,1069,1071,1074,1084,1098,1100,1102,1126,1127,1143,1155,1156,1168,1175,1183,1185,1199,1214,1217,1228,1230,1243,1251,1253,1257,1274,1304,1326,1329,1343,1355,1369,1398,1431,1436,1440,1448,1467,1491,1494,1512,1515,1521,1535,1546,1547,1550,1558,1567,1590,1591,1592,1607,1613,1617,1628,1635,1636,1648,1657,1658,1723,1732,1734,1738,1741,1742,1747,1748,1770,1779,1783,1796,1797,1801,1802,1805,1837,1844,1850,1852,1866,1882,1885,1905,1911,1913,1917,1926,1936,1939,1958,1970,1972,1973,1985,1986,2005,2009,2016,2017,2026,2030,2046,2051,2055,2063,2064,2075,2089,2090,2095,2096,2112,2121,2131,2140,2147,2149,2159,2177,2192,2223,2236,2237,2240,2241,2242,2247,2260,2271,2282,2284,2306,2335,2341,2343,2353,2379,2385,2409,2415,2420,2425,2430,2436,2440,2442,2475,2481,2482,2493,2496,2522,2523,2533,2534,2536,2542,2550,2571,2597,2608,2614,2624,2630,2635,2639,2652,2654,2656,2672,2689,2709,2713,2716,2717,2722,2739,2741,2745,2753,2759,2763,2773,2778,2783,2784,2795,2798,2804,2830,2857,2859,2872,2874,2884,2921,2922,2924,2935,2961,2962,2971,2972,2985,3001,3012,3013,3017,3020,3038,3044,3069,3075,3079,3094,3108,3112,3113,3122,3143,3161,3169,3172,3175,3178,3186,3195,3216,3223,3258,3277,3289,3309,3369,3372,3381,3385,3393,3411,3419,3426,3459,3461,3464,3470,3482,3486,3495,3501,3504,3519,3551,3556,3563,3577,3583,3584,3635,3639,3641,3660,3661,3671,3686,3707,3720,3722,3730,3732,3739,3755,3758,3767,3774,3776,3784,3794,3802,3806,3825,3834,3835,3847,3852,3879,3883,3890,3891,3892,3917,3930,3937,3946,3948,3987,3991,4007,4009,4017,4034,4081,4084,4100,4120,4129,4135,4140,4156,4163,4199,4200,4208,4210,4218,4236,4240,4244,4260,4287,4288,4295,4298,4312,4317,4319,4322,4323,4327,4331,4333,4336,4337,4345,4350,4360,4361,4369,4374,4382,4391,4394,4408,4412,4424,4430,4432,4436,4452,4460,4470,4496,4511,4512,4545,4568,4574,4592,4611,4626,4647,4651,4653,4690,4707,4743,4784,4796,4802,4809,4878,4887,4895,4914,4915,4920,4931,4965,4985,4995,5013,5019,5026,5036,5051,5056,5086,5091,5109,5128,5161,5176,5177,5189,5203,5232,5242,5292,5293,5313,5332,5336,5373,5376,5382,5387,5397,5405,5417,5429,5442,5444,5455,5457,5460,5462,5476,5477,5481,5488,5496,5523,5542,5548,5552,5556,5559,5591,5600,5604,5634,5643,5650,5653,5674,5712,5729,5731,5737,5765,5766,5786,5790,5815,5818,5827,5830,5837,5847,5868,5869,5880,5890,5902,5905,5920,5933,5938,5944,5948,5957,5963,5967,5983,5993,6020,6028,6034,6049,6059,6079,6082,6098,6099,6174,6219,6221,6222,6228,6229,6232,6259,6273,6292,6312,6315,6316,6320,6339,6342,6345,6387,6391,6396,6415,6435,6447,6453,6455,6456,6459,6470,6494,6517,6531,6537,6541,6557,6558,6567,6568,6585,6617,6620,6632,6636,6638,6644,6663,6669,6676,6693,6700,6706,6755,6757,6771,6776,6792,6797,6840,6858,6863,6868,6872,6877,6890,6898,6908,6912,6925,6930,6946,6976,6985,6992,6998,7019,7023,7030,7031,7032,7037,7055,7066,7082,7093,7096,7098,7101,7107,7108,7119,7134,7135,7136,7138,7140,7156,7181,7185,7200,7202,7207,7211,7221,7224,7229,7232,7233,7243,7244,7269,7271,7285,7300,7304,7310,7318,7328,7331,7340,7362,7364,7385,7390,7393,7394,7398,7416,7429,7440,7475,7504,7505,7520,7526,7562,7566,7576,7577,7594,7603,7617,7630,7632,7633,7653,7672,7673,7674,7684,7685,7690,7696,7711,7746,7747,7774,7775,7782,7817,7823,7825,7855,7862,7870,7878,7892,7900,7908,7910,7919,7927,7947,7953,7979,7995,7996,8041,8043,8048,8049,8079,8082,8085,8090,8091,8096,8108,8112,8133,8140,8142,8161,8174,8184,8215,8235,8250,8269,8270,8274,8275,8282,8309,8325,8331,8363,8375,8382,8383,8426,8446,8474,8481,8522,8540,8542,8559,8560,8567,8587,8600,8618,8620,8641,8664,8668,8673,8680,8708,8710,8730,8736,8737,8754,8784,8794,8799,8806,8810,8820,8839,8870,8874,8886,8899,8900,8917,8937,8979,8986,8995,9013,9015,9016,9018,9019,9044,9052,9058,9059,9077,9081,9090,9094,9103,9128,9158,9161,9164,9192,9205,9233,9243,9248,9267,9278,9314,9315,9316,9319,9323,9343,9366,9372,9421,9423,9435,9458,9475,9480,9489,9490,9494,9499,9503,9512,9520,9528,9546,9561,9574,9581,9590,9592,9595,9597,9604,9621,9626,9629,9634,9661,9663,9666,9667,9678,9682,9704,9705,9716,9719,9723,9736,9738,9740,9744,9756,9766,9777,9808,9814,9819,9829,9832,9840,9853,9875,9882,9889,9900,9921,9942,9958,9961,9964,9994]
print(cl.count(coins,N,Sum))

print(cl.memo)
