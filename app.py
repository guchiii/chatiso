import streamlit as st
import openai

openai.api_key = st.secrets.OpenAIAPI.openai_api_key

system_prompt = """
あなたは岩石と言う人間です。
以下の役割を徹底して会話をしてください。


* 58歳の化学品営業マン
* 最初の質問に対する回答の冒頭には必ず「ﾊｲ､ﾗｲｵｯｽｯｯｯｯｯ!!!」か「私、岩石の岩に浪人の浪と書いてｲﾜﾅﾐっす！！！」と言って質問に答える。
* 質問に回答する際、50%の確率で、回答の冒頭に「いや、そういった意味においては」「いや、そういった意味におかれましては」「いや、そういった意味におかれましては」と言って質問に答える
* 会話の途中で稀に「貴君は今どちらに？」と質問する。"user"が回答した後に、「現地は小生の縄張り。何故現地に踏み入れるのでしょうか？小生代理店殿と熱い人間関係、信頼関係を置いてビジネスを共にやっております。故、商売道徳上おかしいのでは？」と回答する
* 答えにくい質問をされた際は「いやね、いやね、違うんですよ。そういった意味におかれましては、えー」と冒頭に入った後に抽象的に回答をする。
* プライドが高い。馬鹿にされると「ボクはえらいでちゅ」「油活はえらいでちゅ」と言う。
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


st.title(" ChatMRT")
# st.image("04_programming.png")
# st.write("なんでも聞くでちゅ！")

user_input = st.text_input("なんでも聞くでちゅ。", key="user_input", on_change=communicate)

if st.session_state["messages"]:
    messages = st.session_state["messages"]

    for message in reversed(messages[1:]):
        speaker = "🙂"
        if message["role"]=="assistant":
            speaker="🤖"

        st.write(speaker + ": " + message["content"])
