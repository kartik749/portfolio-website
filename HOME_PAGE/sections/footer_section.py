import streamlit as st

def footer_section():

    st.html("""
    <style>

    .portfolio-footer {

        margin-top: 20px;

        padding: 30px 6%;

        border-top:
            1px solid rgba(255,255,255,0.08);

        text-align: center;

        color: #777777;

        font-size: 13px;

    }

    .footer-name {
        color: #aaaaaa;

        font-weight: 600;

        margin-bottom: 8px;
    }

    </style>


    <div class="portfolio-footer">

        <div class="footer-name">
            Kartik
        </div>

        <div>
            Built with Python & Streamlit
        </div>

    </div>
    """)