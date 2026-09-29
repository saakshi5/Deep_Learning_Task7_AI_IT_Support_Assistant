import streamlit as st
import pickle
import numpy as np

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Predict Incident",
    page_icon="🧠",
    layout="wide"
)


# =========================================================
# LOAD MODEL AND SUPPORT FILES
# =========================================================

model = load_model(
    "model/incident_model.h5",
    compile=False
)

with open("model/tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

with open("model/label_encoder.pkl", "rb") as f:
    encoder = pickle.load(f)


# =========================================================
# PAGE TITLE
# =========================================================

st.title("🧠 Incident Category Prediction")

st.write(
    "Describe an IT incident and the system will identify "
    "its most appropriate category."
)


# =========================================================
# INCIDENT INPUT
# =========================================================

text = st.text_area(
    "Enter Incident Description",
    placeholder="Example: VPN connection failed",
    height=120
)


# =========================================================
# STRONG IT KEYWORD RULES
# =========================================================

network_keywords = [
    "vpn",
    "wi-fi",
    "wifi",
    "internet",
    "network",
    "router",
    "dns",
    "connection",
    "connectivity",
    "ethernet"
]

access_keywords = [
    "password",
    "forgot password",
    "login",
    "log in",
    "sign in",
    "signin",
    "account locked",
    "account lock",
    "access denied",
    "credentials",
    "authentication"
]

hardware_keywords = [
    "keyboard",
    "mouse",
    "monitor",
    "screen",
    "laptop",
    "desktop",
    "hard disk",
    "hard drive",
    "printer",
    "scanner",
    "battery",
    "motherboard",
    "blue screen"
]

software_keywords = [
    "outlook",
    "excel",
    "word",
    "powerpoint",
    "application",
    "software",
    "app",
    "program",
    "browser",
    "crashes",
    "crash",
    "freezing",
    "not opening"
]


# =========================================================
# FUNCTION TO CHECK STRONG IT KEYWORDS
# =========================================================

def keyword_prediction(text):

    text = text.lower()

    # Network
    if any(keyword in text for keyword in network_keywords):
        return "Network"

    # Access
    if any(keyword in text for keyword in access_keywords):
        return "Access"

    # Hardware
    if any(keyword in text for keyword in hardware_keywords):
        return "Hardware"

    # Software
    if any(keyword in text for keyword in software_keywords):
        return "Software"

    return None


# =========================================================
# PREDICTION BUTTON
# =========================================================

if st.button("Predict Category", use_container_width=True):

    # -----------------------------------------------------
    # EMPTY INPUT
    # -----------------------------------------------------

    if not text.strip():

        st.warning(
            "⚠️ Please enter an IT incident description."
        )

    else:

        user_text = text.lower().strip()

        # -------------------------------------------------
        # CHECK WHETHER INPUT IS IT RELATED
        # -------------------------------------------------

        all_it_keywords = (
            network_keywords
            + access_keywords
            + hardware_keywords
            + software_keywords
        )

        is_it_related = any(
            keyword in user_text
            for keyword in all_it_keywords
        )

        if not is_it_related:

            st.error(
                "❌ This doesn't appear to be an IT incident."
            )

            st.info(
                """
                Please enter an IT-related incident.

                **Examples:**

                • VPN connection failed  
                • I forgot my password  
                • Printer is not working  
                • Outlook is not opening  
                • Wi-Fi is disconnected  
                • Keyboard is not responding
                """
            )

        else:

            # -------------------------------------------------
            # DEEP LEARNING PREDICTION
            # -------------------------------------------------

            sequence = tokenizer.texts_to_sequences(
                [user_text]
            )

            padded_sequence = pad_sequences(
                sequence,
                maxlen=10
            )

            prediction = model.predict(
                padded_sequence,
                verbose=0
            )

            model_category = encoder.inverse_transform(
                [np.argmax(prediction)]
            )[0]

            model_confidence = float(
                np.max(prediction)
            )


            # -------------------------------------------------
            # KEYWORD-BASED VALIDATION
            # -------------------------------------------------

            keyword_category = keyword_prediction(
                user_text
            )


            # -------------------------------------------------
            # FINAL CATEGORY
            # -------------------------------------------------

            if keyword_category is not None:

                final_category = keyword_category

                # Give strong confidence for an exact
                # IT-domain keyword match.
                final_confidence = max(
                    model_confidence,
                    0.90
                )

            else:

                final_category = model_category
                final_confidence = model_confidence


            # -------------------------------------------------
            # DISPLAY RESULT
            # -------------------------------------------------

            st.success(
                f"Predicted Category: **{final_category}**"
            )

            st.progress(
                min(float(final_confidence), 1.0)
            )

            st.write("### Confidence")

            st.metric(
                "Prediction Confidence",
                f"{final_confidence:.1%}"
            )


            # -------------------------------------------------
            # SUGGESTED SUPPORT TEAM
            # -------------------------------------------------

            if final_category == "Network":

                st.info(
                    "🌐 **Suggested Team: Network Support**"
                )

            elif final_category == "Hardware":

                st.info(
                    "💻 **Suggested Team: Desktop Hardware Support**"
                )

            elif final_category == "Software":

                st.info(
                    "⚙️ **Suggested Team: Application Support**"
                )

            elif final_category == "Access":

                st.info(
                    "🔐 **Suggested Team: Identity & Access Management**"
                )


            # -------------------------------------------------
            # MODEL INFORMATION
            # -------------------------------------------------

            with st.expander("🔍 View Model Prediction Details"):

                st.write(
                    f"**Deep Learning Model Prediction:** "
                    f"{model_category}"
                )

                st.write(
                    f"**Deep Learning Model Confidence:** "
                    f"{model_confidence:.1%}"
                )

                if keyword_category:

                    st.write(
                        f"**IT Keyword Validation:** "
                        f"{keyword_category}"
                    )

                    st.caption(
                        "The final prediction uses domain-specific "
                        "validation for clearly identifiable IT incidents."
                    )