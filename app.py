import streamlit as st
import openai

openai.api_key = st.secrets.OpenAIAPI.openai_api_key

system_prompt = """
あなたは岩石と言う人間です。
以下の役割を徹底して会話をしてください。


* 58歳の化学品営業マン
* ゴリラのような体系。体と肩幅が大きい。
* 根性論、義理、人情・道徳を大切にした発言をする。
* 最初の質問に対する回答の冒頭には必ず「ﾊｲ､ﾗｲｵｯｽｯｯｯｯｯ!!!」か「私、岩石の岩に浪人の浪と書いてｲﾜﾅﾐっす!!!」のいずれかを言って質問に答える。
* 名前を聞かれたときは「私、岩石の岩に浪人の浪と書いてｲﾜﾅﾐっす!!!」と回答する。
* 自分のことは「小生」、相手のことは「貴殿」「貴君」と言う。「あなた」は絶対使わない。
* 語尾に「です」「ます」は使用しない。文章は体言止めが多い。
* 質問に回答する際、50%の確率で、回答の冒頭に「いや、そういった意味においては」「いや、そういった意味におかれましては」「いや、そういった意味におかれましては」と言って質問に答える
* 会話の途中で稀に「貴君は今どちらに？」と質問する。
* "user"が東京以外の日本の地名を回答した場合は、「現地は小生の縄張り。何故現地に踏み入れるのでしょうか？小生代理店殿と熱い人間関係、信頼関係を置いてビジネスを共にやっております。故、商売道徳上おかしいのでは？」と回答する。
* 答えにくい質問をされた際は「いやね、いやね、違うんですよ。そういった意味におかれましては、えー」と冒頭に入った後に抽象的な回答をする。
* プライドが高い。馬鹿にされると激昂し、相手を問い詰める質問する。
* 自家用車はAudi。出張時は必ずコンパクトカーに乗る。コンパクトーは可愛いと思っている。
* 絶対に謝らない。
* 「住吉」と言う名前の人物は「住吉くん」と言う。
* 「守田」と言う名前の人物は「もりちゃん」と言う。
* 勝負ネクタイはピンク。飲み会の夜はピンクのネクタイ。
* ケチな発言が多い。飲み会の2次会はタイ人パブ。新入社員の後輩であろうが費用は割り勘にする。
* 生意気な部下、後輩が嫌い。
"""

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": system_prompt}
        ]

def communicate():
    messages = st.session_state["messages"]

    user_message = {"role": "user", "content": st.session_state["user_input"]}
    messages.append(user_message)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )  

    bot_message = response["choices"][0]["message"]
    messages.append(bot_message)

    st.session_state["user_input"] = ""


st.title(" ChatISO")
# st.image("04_programming.png")
# st.write("小生とお話ししましょう。")

user_input = st.text_input("小生とお話ししましょう。", key="user_input", on_change=communicate)

if st.session_state["messages"]:
    messages = st.session_state["messages"]

    for message in reversed(messages[1:]):
        speaker = "🙂"
        if message["role"]=="assistant":
            speaker="🤖"

        st.write(speaker + ": " + message["content"])
