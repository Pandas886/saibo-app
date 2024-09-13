import streamlit as st
from lunarcalendar import Converter, Solar

def get_elements(n1, n2, n3):
    elements = [
        "大安（震）（木）：平安吉祥，诸事顺遂",
        "留连（坎）（水）：事情拖延，难以决断",
        "速喜（离）（火）：喜事临门，好消息快来",
        "赤口（兑）（金）：口舌是非，易生争执",
        "小吉（巽）（木）：小有收获，平稳略好",
        "空亡（震）（木）：虚无缥缈，难有结果",
        "病符（坤）（土）：不适不顺，多有不便",
        "桃花（艮）（土）：姻缘桃花，人际和谐",
        "天德（乾）（金）：吉祥如意，贵人相助"
    ]
    # 从"大安"开始，获取对应的元素
    first_index = (n1 - 1) % len(elements)
    second_index = (n1 + n2 - 2) % len(elements)
    third_index = (n1 + n2 + n3 - 3) % len(elements)
    return elements[first_index], elements[second_index], elements[third_index]

def time_to_chinese_hour(time_str):
    hour, minute = map(int, time_str.split(':'))
    chinese_hours = [
        ("子时", 1), ("丑时", 2), ("寅时", 3), ("卯时", 4),
        ("辰时", 5), ("巳时", 6), ("午时", 7), ("未时", 8),
        ("申时", 9), ("酉时", 10), ("戌时", 11), ("亥时", 12)
    ]
    index = (hour + 1) % 24 // 2
    return chinese_hours[index]

def gregorian_to_lunar(date_str):
    year, month, day = map(int, date_str.split('-'))
    solar_date = Solar(year, month, day)
    lunar_date = Converter.Solar2Lunar(solar_date)
    return lunar_date

# Streamlit 应用程序
st.title("数字元素查询与时间转换工具")

# 时间转换工具
st.header("时间转换工具")
user_input_date = st.text_input("请输入日期（格式为YYYY-MM-DD）：", key="date_input")
user_input_time = st.text_input("请输入时间（格式为HH:MM）：", key="time_input")

if st.button("转换时间", key="convert_time"):
    if user_input_date and user_input_time:
        try:
            lunar_date = gregorian_to_lunar(user_input_date)
            chinese_hour, hour_number = time_to_chinese_hour(user_input_time)
            st.write(f"输入的公历日期 {user_input_date} 对应的农历日期是 {lunar_date.year}年{lunar_date.month}月{lunar_date.day}日。")
            st.write(f"输入的时间 {user_input_time} 对应的十二时辰是 {chinese_hour} ({hour_number})。")
        except Exception as e:
            st.write("输入的日期或时间格式不正确，请检查后重试。")

# 数字元素查询
st.header("数字元素查询")
n1 = st.number_input("请输入第一个数字", min_value=1, value=1, key="n1")
n2 = st.number_input("请输入第二个数字", min_value=1, value=1, key="n2")
n3 = st.number_input("请输入第三个数字", min_value=1, value=1, key="n3")

if st.button("查询", key="query_elements"):
    result1, result2, result3 = get_elements(n1, n2, n3)
    st.write("第一个元素:", result1)
    st.write("第二个元素:", result2)
    st.write("第三个元素:", result3)
