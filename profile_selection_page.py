import streamlit as st
from pathlib import Path
import base64
def profile_selection():

    # Load profile image

    image_path = Path("assets/kartik photo 1.jpg")

    if image_path.exists():

        image_bytes = image_path.read_bytes()

        image_base64 = base64.b64encode(
            image_bytes
        ).decode("utf-8")

    else:
        image_base64 = None


    # Profile Selection UI

    if image_base64:

        st.html(f"""
        <style>

        .profile-screen {{
            min-height: 75vh;

            display: flex;
            flex-direction: column;

            align-items: center;
            justify-content: center;

            text-align: center;
        }}


        .profile-title {{
            font-size: 52px;

            font-weight: 600;

            letter-spacing: 3px;

            color: white;

            margin-bottom: 55px;
        }}


        .profile-card {{
            width: 210px;

            text-align: center;

            cursor: pointer;

            transition: transform 0.3s ease;
        }}


        .profile-image {{
            width: 190px;
            height: 190px;

            margin: auto;

            border-radius: 8px;

            object-fit: cover;

            border: 3px solid transparent;

            display: block;

            transition:
                transform 0.3s ease,
                border 0.3s ease,
                box-shadow 0.3s ease;
        }}


        .profile-card:hover {{
            transform: scale(1.05);
        }}


        .profile-card:hover .profile-image {{
            border: 3px solid white;

            box-shadow:
                0 0 25px rgba(255, 255, 255, 0.15);
        }}


        .profile-name {{
            margin-top: 18px;

            font-size: 24px;

            font-weight: 500;

            color: #b8b8b8;

            transition: color 0.3s ease;
        }}


        .profile-card:hover .profile-name {{
            color: white;
        }}

        </style>


        <div class="profile-screen">

            <div class="profile-title">
                WHO'S HERE?
            </div>


            <div class="profile-card">

                <img
                    class="profile-image"
                    src="data:image/jpeg;base64,{image_base64}"
                >

                <div class="profile-name">
                    Kartik
                </div>

            </div>

        </div>
        """)

    else:

        # Fallback if image doesn't exist

        st.html("""
        <style>

        .profile-screen {
            min-height: 75vh;

            display: flex;
            flex-direction: column;

            align-items: center;
            justify-content: center;

            text-align: center;
        }

        .profile-title {
            font-size: 52px;
            font-weight: 600;
            letter-spacing: 3px;
            color: white;
            margin-bottom: 55px;
        }

        .profile-image {
            width: 190px;
            height: 190px;

            margin: auto;

            border-radius: 8px;

            background:
                linear-gradient(
                    135deg,
                    #333333,
                    #18181c
                );

            display: flex;

            align-items: center;
            justify-content: center;

            font-size: 85px;
        }

        .profile-name {
            margin-top: 18px;

            font-size: 24px;

            font-weight: 500;

            color: #b8b8b8;
        }

        </style>


        <div class="profile-screen">

            <div class="profile-title">
                WHO'S HERE?
            </div>

            <div class="profile-image">
                👤
            </div>

            <div class="profile-name">
                Kartik
            </div>

        </div>
        """)

        st.warning(
            "Profile image not found. "
            "Place kartik.jpg inside the assets folder."
        )

    # Continue Button

    st.write("")
    st.write("")

    left, center, right = st.columns([2, 1, 2])

    with center:

        if st.button(
            "Continue",
            use_container_width=True
        ):

            st.session_state.entered = True

            st.rerun()
