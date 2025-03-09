import streamlit as st
import random
import time
import requests

st.title("Money Making Machine")

def generate_money():
    return random.randint(1, 1000)  # Fixed typo and added return statement

st.subheader("Instant Cash Generator")
if st.button("Generate Money"):
    st.write("Counting your money...")
    time.sleep(5)
    amount = generate_money()
    st.success(f"You made ${amount}!")

def fetch_side_hustle():
    try:
        response = requests.get("http://127.0.0.1:8000/side_hustles?apiKey=12345")
        if response.status_code == 200:
            hustles = response.json()  # Fixed assignment operator
            return hustles["side_hustle"]
        else:
            return "Freelancing"
    except Exception as e:
        st.error(f"Something went wrong! Error: {e}")
        return "Something went wrong!"

st.subheader("Side Hustle Ideas")
if st.button("Get Side Hustle Idea"):
    hustle_idea = fetch_side_hustle()
    st.sucess(hustle_idea)

import streamlit as st
import requests

def fetch_money_quotes():
    try:
        response = requests.get("http://127.0.0.1:8000/money_quotes?apiKey=12345")  # Fixed typo in requests.get()
        if response.status_code == 200:
            quotes = response.json()
            return quotes.get("money_quotes", "No quote found")  # Added safe .get() handling
        else:
            return "Money is the root of all evil"  # Fixed typo
    except Exception as e:
        st.error(f"Something went wrong! Error: {e}")
        return "Something went wrong!"

st.subheader("Money Making Motivations")
if st.button("Get Money Quotes"):
    money_idea = fetch_money_quotes()
    st.success(money_idea)  


