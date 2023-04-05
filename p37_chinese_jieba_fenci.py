import jieba
import re
content = """
    春姑娘悄悄地从天上来到了人间，她迈着轻盈的脚步，千里迢迢地来到了我们学校。她吹绿了草地，吹艳了花朵。使我们的校园呈现出一片生机勃勃的景象。
    生物园里，各色的花儿开得正艳。红的玫瑰、黄的桂花、粉红的杜鹃……真是“春色满园关不住”。忽然，从墙角飘来一种淡淡的香味，这香味清新脱俗，令人闻了还想闻。我嗅着这股香味走去，啊，原来是墙角处种了一棵水仙。人称水仙是花中的凌波仙子，今日一看，果然不假。你看，它那翠绿的叶子衬托着高贵的花朵，洁白的花蕾中散发出特有的香味，真不愧是花中的仙子啊。
    在生物园外围，嫩绿的福建茶好像一条轻柔的绿丝带，把整个繁花似锦的生物园轻轻地环绕起来。
    操场上，小草在春姑娘温柔的吹拂下，离开了大地母亲温暖的怀抱，好奇地探出头来观看这个新奇的世界。春姑娘把小草那毫无生气的冬装带走了，送给它们一套嫩绿的充满生机的春装。小草高兴地接受了这一件礼物，并且穿上了它，整个操场顿时显得生机勃勃。天空中，三三两两的燕子飞来飞去，好像几位穿着燕尾服的“绅士”在翩翩起舞。
    啊，谢谢你，美丽的春姑娘。谢谢你不辞劳苦，给我们带来了一份厚礼——如诗如画的春天！
"""
content = re.sub(r"[\s。，—…！“”]", "", content)
word_list = jieba.cut(content)
print(list(word_list))
