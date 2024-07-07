import streamlit as st
import datetime as dtime


with st.form(key='profile_form'):
    #　テキストボックス
    name = st.text_input('名前')
    address = st.text_input("住所")

    #　セレクトボックス
    age_category = st.radio('年齢層', ('子供（18才未満）',
                                '大人（18才以上）'))

    #複数選択
    hobby = st.multiselect('趣味',('スポーツ','読書',
                            'プログラミング','アニメ・映画','釣り','料理'))

    #
    mail_subscribe = st.checkbox('メールマガジンを購読する')
    #
    height = st.slider('身長', min_value=110, max_value=210)
    #日付
    start_date = st.date_input('開始日', dtime.date(2024,7,7))			#	import datetime as dtimeを最初に書いておかないとエラーを吐くので注意

    #カラーピッカー
    color = st.color_picker('テーマカラー', '#00f900')

    #　ボタン
    submit_btn = st.form_submit_button('送信')                          #	ボタンが押されている場合はT、押されてなければFが戻り値として返ってくる
    cancel_btn = st.form_submit_button('キャンセル')
    
    if submit_btn:
        st.text(f'ようこそ！{name}さん！{address}に書籍を送りました')
        st.text(f'年齢層: {age_category}')
        st.text(f'趣味：{", ".join(hobby)}')
