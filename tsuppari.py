# coding: utf-8
import sys

src = \
    'あぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢ'\
    'っつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃ'\
    'やゅゆょよらりるれろゎわゐゑをんゔゕゖ'
dst = \
    '亜ぃ慰ぅ宇ぇ餌ぉ悪華蛾鬼戯苦愚怪外孤誤沙座死慈酢頭勢是訴憎駄堕血痔'\
    'っ津づ帝で斗ど那尼奴根乃覇婆波卑微碑父撫腐屁塀餅帆墓歩魔魅夢女喪ゃ'\
    '夜ゅ遊ょ世羅璃流零露ゎ我ゐゑ魚云ゔゕゖ'

while True:
    try:
        s = input('')
        for c in s:
            d = src.find(c)
            if (0 <= d):
                print(dst[d], end = '')
            else:
                print(c, end = '')
        print()
    except EOFError:
        sys.exit(0)


