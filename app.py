import streamlit as st
import streamlit as st
import requests
from PIL import Image
from streamlit_lottie import st_lottie


# code by Adewole Olumide 16/02/2023

# pip install streamlit - for framework
# pip install streamlit-lottie for gifs
# pip install requests - requests library
# pip install pillow - for images
# find more emojis here https://www.webfx.com/tools/emoji-cheat-sheet/
# animation files from lottiefiles.com
# get forms from formsubmit.co
# pip install pipreqs for deployment


# request animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# load assets
lottie_coding = load_lottieurl(
    "https://assets2.lottiefiles.com/packages/lf20_zvmuqszh.json"
)
lottie_rate = load_lottieurl(
    "https://assets7.lottiefiles.com/packages/lf20_6pyKbDVStk.json"
)
lottie_fast = load_lottieurl(
    "https://assets2.lottiefiles.com/packages/lf20_g1wiidwh.json"
)
first_img = Image.open("images/bankcomparision.jpeg")
second_img = Image.open("images/exchange.png")

st.set_page_config(page_title="Sendr", page_icon=":moneybag:", layout="wide")


def intro():
    import streamlit as st
    from urllib.error import URLError

    st.markdown(f"# {list(page_names_to_funcs.keys())[0]}")

    with st.container():
        col1, col2 = st.columns((1, 2))
        with col1:
            st.subheader("The Fastest way to Send Money:rocket:")
            st.write(
                """Send and receive money globally with Sendr, the world's trusted currency authority.
                Convert your airtime to cash in minutes and withraw your cash to your local bank."""
            )
        with col2:
            st_lottie(lottie_coding, height=350, key="Money")

    with st.container():
        st.write("---")
        st.subheader("How to send money with Sendr")
        st.write("##")

        col1, col2, col3 = st.columns(3)
    st.write("##")
    with col1:
        st.subheader("1. Create an Account")
        with st.expander("Learn More"):
            st.write(
                """It takes just a few minutes, and all you need is an email address."""
            )

    with col2:
        st.subheader("2. Enter Your Details")
        with st.expander("Learn More"):
            st.write(
                """Add recipient (you'll need their address, bank account/IBAN, swift/BIC) and payment information."""
            )

    with col3:
        st.subheader("3. Confirm and Send")
        with st.expander("Learn More"):
            st.write(
                """Check the currencies and amount are correct, get the expected delivery date, and send your money transfer."""
            )
    st.button("Get Started")

    st.write("##")
    st.write("##")
    st.write("Bank Comparision")

    col1, col2 = st.columns((2))
    with col1:
        st.subheader("What you could save using Sendr vs. your bank")
        st.write(
            """Transfer £20,000 to EUR and your recipients could get up to €554 more. 
        You'll get our most competitive rates with no hidden fees."""
        )
        st.button("Sign in and Send ")

    with col2:
        st.image(first_img)

    st.write("##")
    st.write(
        """The comparison savings are based on a single transfer of GBP£20,000 to EUR and shows how much Sendr would send to the recipient, 
    and how much the comparator would send to the recipient. The difference between these two amounts is highlighted as the “saving”. 
    Our savings comparisons are derived from pricing data provided by an independent third party ‘DQM GRC’. 
    The comparison savings provided are true only for the example given and may not include all fees and charges. 
    Savings are calculated by comparing the exchange rate (including margin and fees) between Sendr and the comparator at the same date and time. 
    Different currency exchange amounts, currencies, dates, times, and other factors may result in different comparison savings. 
    These results may not be indicative of actual savings and should be used only as a guide. The rate comparison chart is updated quarterly."""
    )

    with st.container():
        st.write("---")
        st.subheader("Why send money with Sendr?")
        st.write("##")

        col1, col2, col3, col4 = st.columns((2, 1, 2, 1))
        with col1:
            st.subheader(
                "You'll get great rates for your transfer:chart_with_upwards_trend:"
            )
            st.write(
                """Our rates are consistently some of the best in the business and trusted by millions."""
            )
        with col2:
            st_lottie(lottie_rate, height=200, key="Great Rates")

        st.write("##")

        with col3:
            st.subheader("We're Fast:zap:")
            st.write(
                """With some transfers taking only minutes, you can get your money where it needs to be — quickly"""
            )

        with col4:
            st_lottie(lottie_fast, height=200, key="Fast Transfer")
        st.write("##")


def converter():
    import streamlit as st
    from urllib.error import URLError

    st.markdown(f"# {list(page_names_to_funcs.keys())[1]}")
        # Store the initial value of widgets in session state
    with st.container():
        currency = st.text_input(
            "Enter a Denomination: Dollars or Naira 👇",
        )
        def conversion(currency):
                if currency == "Dollars":
                    dollar = int(st.number_input("Please type in Dollar value: "))
                    rate = 720
                    value = (dollar * rate)
                    st.write(dollar, "Dollars to Naira is equivalent to", value, "Naira")
                elif currency == "Naira":
                    naira = int(st.number_input("Please type in Naira value: "))
                    rate = 720
                    value = (naira / rate)
                    st.write(naira, "Naira to Dollars is equivalent to", value, "Dollars")
                else:
                    st.write("Please type in a value.")

        if currency:
            st.write(conversion(currency))

@st.cache_data
def sendMoney():
    import streamlit as st

    st.markdown(f"# {list(page_names_to_funcs.keys())[2]}")


@st.cache_data
def contact():
    import streamlit as st

    st.markdown(f"# {list(page_names_to_funcs.keys())[3]}")


page_names_to_funcs = {
    "International Money Transfer": intro,
    "Converter": converter,
    "Send Money": sendMoney,
    "Contact Us": contact,
}

demo_name = st.sidebar.selectbox("© Sendr 2023 | Menu", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
