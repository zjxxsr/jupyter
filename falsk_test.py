from flask import Flask
app=Flask(__name__)

@app.route("/")

def ancient_poem():
    sentence="""
    《沁园春 雪》 毛泽东
北国风光，千里冰封，万里雪飘。

望长城内外，惟余莽莽；大河上下，顿失滔滔。

山舞银蛇，原驰蜡象，欲与天公试比高。

须晴日，看红装素裹，分外妖娆。

江山如此多娇，引无数英雄竞折腰。

惜秦皇汉武，略输文采；唐宗宋祖，稍逊风骚。

一代天骄，成吉思汗，只识弯弓射大雕。\t

俱往矣，数风流人物，还看今朝。\t

 

    《沁园春·雪》被南社盟主柳亚子盛赞为千古绝唱。这首词是世人的最爱，每次读来都仿佛又回到了那个战火纷飞的年代，又看到了那个指点江山的伟人，不由地沉醉于那种豪放的风格、磅礴的气势、深远的意境、广阔的胸怀。全词用字遣词，设喻用典，明快有力，挥洒自如，辞义畅达，一泻千里。全词合律入韵，虽属旧体却给读者以面貌一新之感。
    """
    return sentence

app.run()
