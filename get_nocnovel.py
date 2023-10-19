# ノクターンノベルス(https://noc.syosetu.com)をテキスト保存する。
# ↓こちらのスクリプトを改修したものです。
# word2vecとノクターンノベルスを用いてドスケベ単語を学習させた話
# https://note.com/happaeight/n/n3b60ccd6cd54
# pip install requests
# pip install BeautifulSoup4
import os, re, time
import requests
from urllib import request
from bs4 import BeautifulSoup

def nocScraping(novelID, limit=0):
	# set UA
	header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0"}

	# set cookie
	cookie = {"over18": "yes"}

	# 親URLをセット
	chapterlistUrl = "https://novel18.syosetu.com/" + str(novelID) + "/"
	responseCL	= requests.get(url=chapterlistUrl, headers=header, cookies=cookie)
	chapterlistHtml = responseCL.content
	soupCL = BeautifulSoup(chapterlistHtml, "html.parser")
	sublist = soupCL.find_all("dl", attrs={"class", "novel_sublist2"})
	#print(len(sublist))

	novelDirPass = "data/" + novelID
	count = 1

	if(limit == 0):
		countlimit = len(sublist) + 1
	else:
		countlimit = limit + 1

	while(count < countlimit):
		# set url
		url = "https://novel18.syosetu.com/" + str(novelID) + "/" + str(count) + "/"
		#print(url)

		# get html
		response  = requests.get(url=url, headers=header, cookies=cookie)
		html = response.content
		#print(html)

		# set BeautifulSoup
		soup = BeautifulSoup(html, "html.parser")

		# scraping
		mainText = soup.find("div", attrs={"id": "novel_honbun"})
		#mainText = soup.find("div", attrs={"id":"novel_ex"})
		#print(mainText)

		try:
			mainTextLines = mainText.find_all("p")
		except AttributeError:
			pass

		allText = ""
		for mainTextLine in mainTextLines:
			text = str(mainTextLine)
			text = re.sub("<p.*\">", "", text)
			text = re.sub("</p>", "", text)
			text = text.replace("<br/>", "")
			text = re.sub('<ruby><rb>(.*?)</rb><rp>(.*?)</rp><rt>(.*?)</rt><rp>(.*?)</rp></ruby>', '\\1\\2\\3\\4', text)
			text = re.sub('\(・\)', '', text)
			text = re.sub('（・）', '', text)

			# 漢数字のゼロ「〇」→丸印「○」
			text = text.replace("〇", "○")
			text = text.replace("●", "○")

			text = text.replace("お○ん○ん", "おちんちん")
			text = text.replace("お○○○○", "おちんちん")
			text = text.replace("おち○ちん", "おちんちん")
			text = text.replace("お○○ちん", "おちんちん")
			text = text.replace("おちん○ん", "おちんちん")
			text = text.replace("お○んちん", "おちんちん")
			text = text.replace("オ○ンチン", "オチンチン")
			text = text.replace("チ○チン", "ちんちん")
			text = text.replace("ち○ぽ", "ちんぽ")
			text = text.replace("ち○○", "ちんぽ")
			text = text.replace("チ○ポ", "チンポ")
			text = text.replace("チ○ボ", "チンポ")
			text = text.replace("ヂ○ポ", "ヂンポ")
			text = text.replace("ヂ○ボ", "ヂンボ")
			text = text.replace("チ゛○ポ", "ヂンポ")
			text = text.replace("ヂィ○ポ", "ヂンポ")
			text = text.replace("チ○フォ", "チンフォ")
			text = text.replace("ひぃ○ふぉ", "ひぃんふぉ")
			text = text.replace("チン○", "チンポ")
			text = text.replace("ひ○ぽ", "ひんぽ")
			text = text.replace("チ○コ", "チンコ")
			text = text.replace("ち○こ", "ちんこ")
			text = text.replace("オ○ンコ", "オチンコ")
			text = text.replace("オ○ンポ", "オチンポ")
			text = text.replace("お○んぽ", "おちんぽ")
			text = text.replace("ペ○ス", "ペニス")
			text = text.replace("キ○タマ", "キンタマ")
			text = text.replace("キン○マ", "キンタマ")
			text = text.replace("ヤリ○ン", "ヤリチン")
			text = text.replace("お○んこ", "おまんこ")
			text = text.replace("おま○こ", "おまんこ")
			text = text.replace("お○○こ", "おまんこ")
			text = text.replace("オマ○コ", "オマンコ")
			text = text.replace("マ○コ", "マンコ")
			text = text.replace("○ンコ", "マンコ")
			text = text.replace("マン○", "マンコ")
			text = text.replace("まん○", "まんこ")
			text = text.replace("ま○こ", "まんこ")
			text = text.replace("ま○○こ", "まんこ")
			text = text.replace("ま○○", "まんこ")
			text = text.replace("レ○プ", "レイプ")
			text = text.replace("ク○トリス", "クリトリス")
			text = text.replace("クリ○リス", "クリトリス")
			text = text.replace("中○生", "中学生")
			text = text.replace("女子○生", "女子高生")
			text = text.replace("○ックス", "セックス")
			text = text.replace("セッ○ス", "セックス")
			text = text.replace("セ○○ス", "セックス")
			text = text.replace("ロ○コン", "ロリコン")
			text = text.replace("ク○ニ", "クンニ")
			text = text.replace("フェ○チオ", "フェラチオ")
			text = text.replace("ホ○", "ホモ")
			text = text.replace("イン○", "インポ")
			text = text.replace("バイ○グラ", "バイアグラ")
			text = text.replace("ウー○ナイザー", "ウーマナイザー")
			text = text.replace("ピ○クローター", "ピンクローター")
			text = text.replace("飛○○子", "飛びっ子")
			text = text.replace("TE○GA", "TENGA")
			text = text.replace("TEN○A", "TENGA")
			text = text.replace("T○NGA", "TENGA")
			text = text.replace("援○", "援交")
			text = text.replace("カ○ピス", "カルピス")
			text = text.replace("カル○ス", "カルピス")
			text = text.replace("チ○カス", "チンカス")
			text = text.replace("う○ち", "うんち")
			text = text.replace("ウ○チ", "ウンチ")
			text = text.replace("○棒", "肉棒")
			text = text.replace("キチ○イ", "キチガイ")
			text = text.replace("ガ○ジ", "ガイジ")
			text = text.replace("ゴキ○リ", "ゴキブリ")
			text = text.replace("秋○原", "秋葉原")
			text = text.replace("ポケ○ン", "ポケモン")
			text = text.replace("ポ○モン", "ポケモン")
			text = text.replace("○○モンバトル", "ポケモンバトル")
			text = text.replace("変態○面", "変態仮面")
			text = text.replace("ウル○○マン", "ウルトラマン")
			text = text.replace("怪獣ツインテー○", "怪獣ツインテール")
			text = text.replace("アポ○チョコ", "アポロチョコ")
			text = text.replace("仮○ライダー", "仮面ライダー")
			text = text.replace("ラ○ュタ", "ラピュタ")
			text = text.replace("デスト○イドモン○ター", "デストロイドモンスター")
			text = text.replace("ＧＮア○マー", "ＧＮアーマー")
			text = text.replace("ハ○ヒ", "ハルヒ")
			text = text.replace("キ○スク", "キヨスク")
			text = text.replace("マ○クラ", "マイクラ")
			text = text.replace("鬼○の刃", "鬼滅の刃")
			text = text.replace("冨○義勇", "冨岡義勇")
			text = text.replace("グラ○ル", "グラブル")
			text = text.replace("グ○ブル", "グラブル")
			text = text.replace("との○ラ", "とのフラ")
			text = text.replace("と○フラ", "とのフラ")
			text = text.replace("i○ad", "iPad")
			text = text.replace("ド○クエ", "ドラクエ")
			text = text.replace("ド○○エ", "ドラクエ")
			text = text.replace("ドラ○エ", "ドラクエ")
			text = text.replace("ス○イム", "スライム")
			text = text.replace("シー○キン", "シーチキン")
			text = text.replace("紀○国屋", "紀伊国屋")
			text = text.replace("ペ○", "ペペ")
			text = text.replace("暗殺教室の奥○", "暗殺教室の奥田")
			text = text.replace("ジョ○ョ", "ジョジョ")
			text = text.replace("スレイ○ーズ", "スレイヤーズ")
			text = text.replace("○スタード", "バスタード")
			text = text.replace("六○世界TRPG", "六門世界TRPG")
			text = text.replace("ト○コ", "トルコ")
			text = text.replace("サ○エさん", "サザエさん")
			text = text.replace("あたり前○のクラッカー", "あたり前田のクラッカー")
			text = text.replace("シ○ン○ン", "シェンロン")
			text = text.replace("ちょ○切り", "ちょん切り")
			text = text.replace("川口春○", "川口春奈")
			text = text.replace("○谷美玲", "桐谷美玲")
			text = text.replace("ＳＡＳＵＫ○", "ＳＡＳＵＫＥ")
			text = text.replace("○分クッキング", "３分クッキング")
			text = text.replace("ガッ○ャン", "ガッチャン")
			text = text.replace("ＴＯＬ○ＶＥる", "ToLOVEる")
			text = text.replace("ゴ○ジェット", "ゴキジェット")
			text = text.replace("ベギ○マ", "ベギラマ")
			text = text.replace("ベギ○ゴン", "ベギラゴン")
			text = text.replace("超サ○ヤ人", "超サイヤ人")
			text = text.replace("ペ○シマン", "ペプシマン")
			text = text.replace("ガン○ム", "ガンダム")
			text = text.replace("ガ○ダム", "ガンダム")
			text = text.replace("ガ○ガル", "ガンガル")
			text = text.replace("シティー○ンター", "シティーハンター")
			text = text.replace("シ○ィハ○ター", "シティハンター")
			text = text.replace("○ィズニーランド", "ディズニーランド")
			text = text.replace("ディ○ニーランド", "ディズニーランド")
			text = text.replace("嵐○", "嵐山")
			text = text.replace("金閣○", "金閣寺")
			text = text.replace("白川○", "白川通")
			text = text.replace("東○道", "東名道")
			text = text.replace("○ールドスクエア", "ワールドスクエア")
			text = text.replace("キングアンドプリン○", "キングアンドプリンス")
			text = text.replace("ＴＯＯ○Ｈ", "ＴＯＯＴＨ")
			text = text.replace("○ッグカメラ", "ビッグカメラ")
			text = text.replace("スナド○", "スナドラ")
			text = text.replace("羽○国際線", "羽田国際線")
			text = text.replace("○イキキ", "ワイキキ")
			text = text.replace("ホノル○", "ホノルル")
			text = text.replace("ハワ○島", "ハワイ島")
			text = text.replace("マウナケ○火山", "マウナケア火山")
			text = text.replace("コ○コーヒー", "コナコーヒー")
			text = text.replace("奥多○", "奥多摩")
			text = text.replace("秩○", "秩父")
			text = text.replace("○能市", "飯能市")
			text = text.replace("オア○島", "オアフ島")
			text = text.replace("○マゾンプライム", "アマゾンプライム")
			text = text.replace("○イゼリア", "サイゼリア")
			text = text.replace("○ノアール", "ルノアール")
			text = text.replace("○急イン", "東急イン")
			text = text.replace("○阪", "大阪")
			text = text.replace("ボ○ノーク・サマーン", "ボリノーク・サマーン")
			text = text.replace("ボリ○―ク・サマーン", "ボリノーク・サマーン")
			text = text.replace("北○の拳", "北斗の拳")
			text = text.replace("ど○で○ドア", "どこでもドア")
			text = text.replace("第○勧業銀行", "第一勧業銀行")
			text = text.replace("第○勧銀", "第一勧銀")
			text = text.replace("○菱銀行", "三菱銀行")
			text = text.replace("ショ○カー", "ショッカー")
			text = text.replace("シ○ッカー", "ショッカー")
			text = text.replace("ユ○○ロ", "ユニクロ")
			text = text.replace("ユニ○ロ", "ユニクロ")
			text = text.replace("し○○ら", "しまむら")
			text = text.replace("ドロ○ボー", "ドロンボー")
			text = text.replace("ボ○ッキー", "ボヤッキー")
			text = text.replace("ド○ンジョ", "ドロンジョ")
			text = text.replace("ト○ズラー", "トンズラー")
			text = text.replace("鉄腕ア○ム", "鉄腕アトム")
			text = text.replace("ド○ペ", "ドクペ")
			text = text.replace("ゴ○ウブラック", "ゴクウブラック")
			text = text.replace("童○", "童貞")
			text = text.replace("ファ○ネル", "ファンネル")
			text = text.replace("メ○ヘラ", "メンヘラ")
			text = text.replace("エ○ズ", "エイズ")
			text = text.replace("峰不○子", "峰不二子")
			text = text.replace("ど○○もドア", "どこでもドア")
			text = text.replace("ちびま○子ちゃん", "ちびまる子ちゃん")
			text = text.replace("ハ○プロ", "ハロプロ")
			text = text.replace("ド○ゴンボール", "ドラゴンボール")
			text = text.replace("ス○ムダンク", "スラムダンク")
			text = text.replace("ワ○ピース", "ワンピース")
			text = text.replace("遊○王", "遊戯王")
			text = text.replace("ナ○ト", "ナルト")
			text = text.replace("テ○プリ", "テニプリ")
			text = text.replace("サ○ケくん", "サスケくん")
			text = text.replace("リ○ーマ", "リョーマ")
			text = text.replace("ヤ○ハ", "ヤマハ")
			text = text.replace("Ｍ○―１０", "ＭＴ―１０")
			text = text.replace("中○の頃", "中学の頃")
			text = text.replace("四次元ポ○ット", "四次元ポケット")
			text = text.replace("○○ノート", "デスノート")
			text = text.replace("ル○ンダイブ", "ルパンダイブ")
			text = text.replace("ド○えもん", "ドラえもん")
			text = text.replace("G○Pro", "GoPro")
			text = text.replace("LI○E", "LINE")
			text = text.replace("L○NE", "LINE")
			text = text.replace("よ○じや", "よーじや")
			text = text.replace("○学校", "小学校")
			text = text.replace("ルー○ス", "ルーカス")
			text = text.replace("○ッポラ", "コッポラ")
			text = text.replace("フ○ーラ", "フローラ")
			text = text.replace("と○る○○の禁書○○", "とある魔術の禁書目録")
			text = text.replace("すれ○がい通信", "すれちがい通信")
			text = text.replace("綾○", "綾鷹")
			text = text.replace("○鷹", "綾鷹")
			text = text.replace("ス○ード", "スペード")
			text = text.replace("大阪梅○駅", "大阪梅田駅")
			text = text.replace("す○ざ○まい", "すしざんまい")
			text = text.replace("カニ○リズム", "カニバリズム")
			text = text.replace("ネ○フ", "ネルフ")
			text = text.replace("碇○ンドウ", "碇ゲンドウ")
			text = text.replace("や○ま作戦", "やしま作戦")
			text = text.replace("める○ちゃん", "めるもちゃん")
			text = text.replace("ハマ○", "ハマー")
			text = text.replace("Amaz○n", "Amazon")
			text = text.replace("アク○リアス", "アクエリアス")
			text = text.replace("ポカ○スエット", "ポカリスエット")
			text = text.replace("○曜サ○ペンス", "火曜サスペンス")
			text = text.replace("○曜スペシャル", "水曜スペシャル")
			text = text.replace("クラ○ン", "クラウン")
			text = text.replace("ラ○ワゴン", "ラブワゴン")

			# 丸印「○」
			if re.search('○', text):
				ng.write(text + "\n")

			if(text != ""):
				allText = allText + text + "\n"

		allText = re.sub("\n\n", "\n", allText)
		allText = re.sub("　", "", allText)
		print(allText)

		os.makedirs(novelDirPass, exist_ok=True)
		newFilePass = novelDirPass + "/" + novelID + "_" + str(count) + ".txt"
		if not os.path.isfile(newFilePass):
			with open(newFilePass, mode="w", encoding="UTF-8") as f:
				f.write(allText)

		count = count +1


def getNcode(limit):
	response = requests.get(
		"https://api.syosetu.com/novel18api/api", 
		params={
			"out"     : "json", 
			"nocgenre": 1, 
			"sasie"   : 0, 
			"type"    : "re", 
			"ispickup": 1, 
			"lim"     : limit, 
			"of"      : "n"
		})

	#print(response.json()[1]["ncode"])
	ncodelist=[]
	count = 1
	while(count < limit+1):
		ncodelist.append(response.json()[count]["ncode"])
		count = count + 1
	#print(ncodelist)
	return ncodelist

# 取得作品数, 取得話数リミット
def getNovelText(number, limit=0):
	ncodelist = getNcode(number)
	#count = 1
	#while(count < number + 1):
	count = 0
	while(count < number):
		nocScraping(ncodelist[count].lower(), limit)
		count = count + 1
		time.sleep(1.5)

if __name__ == "__main__":
	ng = open("ng_list.txt", mode="w", encoding="UTF-8")
	getNovelText(500, 20)
	ng.close()
