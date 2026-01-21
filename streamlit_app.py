import streamlit as st

st.set_page_config(page_title="相性分析アプリ", layout="centered")
st.title("💖 相性分析アプリ（15問・分析型）")

st.write("シチュエーションごとに、あなたの理想と相手の行動を比較します。")

# 質問データ（質問ごとに選択肢が違う）
questions = [
    {"text": "落ち込んだとき、どうしてほしい？",
     "choices": ["話を聞いてほしい", "励ましてほしい", "そっとしてほしい"]},

    {"text": "忙しいときの関わり方は？",
     "choices": ["応援してほしい", "干渉しないでほしい", "様子を見てほしい"]},

    {"text": "連絡の頻度はどれくらいが理想？",
     "choices": ["毎日", "数日に1回", "必要なときだけ"]},

    {"text": "ケンカしたときはどうしたい？",
     "choices": ["すぐ話し合う", "時間を置く", "自然に元に戻したい"]},

    {"text": "不安なときの対応は？",
     "choices": ["言葉で安心させてほしい", "行動で示してほしい", "そっと支えてほしい"]},

    {"text": "嬉しいことがあったときは？",
     "choices": ["一緒に喜びたい", "報告できれば十分", "特に何もしなくていい"]},

    {"text": "体調が悪いときは？",
     "choices": ["看病してほしい", "気遣いの連絡がほしい", "一人で休みたい"]},

    {"text": "意見が合わないときは？",
     "choices": ["話し合って決めたい", "相手に合わせる", "一度距離を置く"]},

    {"text": "将来の話について",
     "choices": ["よく話したい", "必要になったら話す", "あまり話したくない"]},

    {"text": "記念日の考え方は？",
     "choices": ["大切にしたい", "できれば祝いたい", "特にこだわらない"]},

    {"text": "一人の時間について",
     "choices": ["とても大事", "ほどほどに欲しい", "あまり必要ない"]},

    {"text": "相手の友人関係について",
     "choices": ["積極的に関わりたい", "必要なときだけ", "あまり関わらない"]},

    {"text": "問題が起きたときの対応",
     "choices": ["一緒に解決したい", "自分で考えたい", "時間に任せたい"]},

    {"text": "感情表現について",
     "choices": ["はっきり伝えてほしい", "控えめでいい", "行動で示してほしい"]},

    {"text": "愛情表現の仕方は？",
     "choices": ["言葉", "行動", "一緒に過ごす時間"]}
]

# 入力：自分
st.subheader("① あなたの理想")
my_answers = []
for i, q in enumerate(questions):
    a = st.selectbox(q["text"], q["choices"], key=f"my_{i}")
    my_answers.append(a)

# 入力：相手
st.subheader("② 相手の行動")
partner_answers = []
for i, q in enumerate(questions):
    a = st.selectbox(f"相手はどうしそう？（{q['text']}）", q["choices"], key=f"pt_{i}")
    partner_answers.append(a)

# 分析
if st.button("相性を分析する"):
    match = 0
    detail = []

    for q, my, pt in zip(questions, my_answers, partner_answers):
        if my == pt:
            match += 1
            detail.append(f"✔ {q['text']}：一致")
        else:
            detail.append(f"✖ {q['text']}：不一致")

    percent = int(match / len(questions) * 100)

    st.subheader("🔍 相性分析結果")
    st.write(f"一致率：**{percent}%**")

    if percent >= 80:
        st.success("価値観がとても近く、安定した相性です 💖")
    elif percent >= 60:
        st.info("違いはあるものの、話し合いで調整できる相性です 🙂")
    else:
        st.warning("価値観のズレが大きいかもしれません 🤔")

    st.subheader("📊 質問ごとの分析")
    for d in detail:
        st.write(d)
