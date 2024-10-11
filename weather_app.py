import streamlit as st
import requests
import json
import pandas as pd

# 设置应用程序标题
st.title("实时天气数据")

# 获取天气数据
@st.cache
def get_weather_data():
    result = requests.get('https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en')
    return result.json()

# 获取数据
weather_data = get_weather_data()

# 将 JSON 数据保存到文件
with open('weather.json', 'w') as f:
    output_json = json.dumps(weather_data, indent=4, sort_keys=True)
    f.write(output_json)

# 创建一个 DataFrame 来存储温度数据
temperature_data = {
    "Place": [item['place'] for item in weather_data["temperature"]["data"]],
    "Temperature (°C)": [item['value'] for item in weather_data["temperature"]["data"]]
}

df_temperature = pd.DataFrame(temperature_data)

# 在侧边栏中创建一个选择框
selected_place = st.sidebar.selectbox("选择地点", df_temperature['Place'])

# 显示所选地点的温度数据
st.header(f"{selected_place} 的温度数据")
selected_temperature = df_temperature[df_temperature['Place'] == selected_place]['Temperature (°C)'].values[0]
st.write(f"Temperature: {selected_temperature}°C")