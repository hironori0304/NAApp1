import streamlit as st

# タイトル
st.title('栄養評価アプリ')

# 入力欄
height = st.number_input('身長 (cm)', min_value=0.0, format="%.2f")
current_weight = st.number_input('現在の体重 (kg)', min_value=0.0, format="%.2f")
usual_weight = st.number_input('平常時体重 (kg)', min_value=0.0, format="%.2f")

# 期間選択
period = st.selectbox('期間を選択', ('1週間', '1カ月', '3カ月', '6カ月'))

# 体重変化率の基準値
period_thresholds = {
    '1週間': (1, 2),
    '1カ月': (5, 5),
    '3カ月': (7.5, 7.5),
    '6カ月': (10, 10)
}

# 計算ボタン
if st.button('計算'):
    if height > 0 and current_weight > 0 and usual_weight > 0:
        # 身長をメートルに変換
        height_m = height / 100
        
        # BMI計算
        bmi = current_weight / (height_m ** 2)
        
        # BMI判定
        if bmi < 18.5:
            bmi_category = "やせ"
        elif 18.5 <= bmi < 25:
            bmi_category = "ふつう"
        else:
            bmi_category = "肥満"
        
        # 理想体重計算
        ideal_weight = 22 * (height_m ** 2)
        
        # %理想体重計算
        percent_ideal_weight = (current_weight / ideal_weight) * 100
        
        # 平常時体重比計算
        percent_usual_weight = (current_weight / usual_weight) * 100
        
        # 体重変化量計算
        weight_change = usual_weight - current_weight
        
        # 体重変化率計算
        weight_change_rate = (weight_change / usual_weight) * 100
        
        # 体重変化の評価
        significant_loss, severe_loss = period_thresholds[period]
        if weight_change_rate >= severe_loss:
            weight_loss_evaluation = "高度な体重減少"
        elif weight_change_rate >= significant_loss:
            weight_loss_evaluation = "有意な体重減少"
        else:
            weight_loss_evaluation = "通常の範囲内の体重減少"
        
        # 結果表示
        st.write(f'BMI: {bmi:.2f}')
        st.write(f'BMIの評価: {bmi_category}')
        st.write(f'理想体重: {ideal_weight:.2f} kg')
        st.write(f'%理想体重: {percent_ideal_weight:.2f} %')
        st.write(f'平常時体重比: {percent_usual_weight:.2f} %')
        st.write(f'体重変化量: {weight_change:.2f} kg')
        st.write(f'体重変化率: {weight_change_rate:.2f} %')
        st.write(f'体重変化の評価: {weight_loss_evaluation}')
        

    else:
        st.write('すべての値を正しく入力してください。')
else:
    # 初期表示項目
    st.write('BMI: ')
    st.write('BMIの評価: ')
    st.write('理想体重: ')
    st.write('%理想体重: ')
    st.write('平常時体重比: ')
    st.write('体重変化量: ')
    st.write('体重変化率: ')
    st.write('体重変化の評価: ')


    # 計算式表示
    st.write("計算式:")
    st.write("BMI = 現在の体重 (kg) / (身長 (m) ^ 2)")
    st.write("理想体重 = 22 * (身長 (m) ^ 2)")
    st.write("%理想体重 = (現在の体重 (kg) / 理想体重 (kg)) * 100")
    st.write("平常時体重比 = (現在の体重 (kg) / 平常時体重 (kg)) * 100")
    st.write("体重変化量 = 平常時体重 (kg) - 現在の体重 (kg)")
    st.write("体重変化率 = (体重変化量 (kg) / 平常時体重 (kg)) * 100")
