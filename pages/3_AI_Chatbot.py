import streamlit as st
from utils.chatbot import get_response

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI IT Support Assistant",
    page_icon="🤖",
    layout="wide"
)

# ============================================================
# AVATARS
# ============================================================

BOT_AVATAR = "https://cdn-icons-png.flaticon.com/512/4712/4712109.png"

USER_AVATAR = "https://cdn-icons-png.flaticon.com/512/847/847969.png"

# ============================================================
# HEADER
# ============================================================

st.title("🤖 AI IT Support Assistant")

st.caption(
    "24×7 Virtual Help Desk for IT Incident Management"
)

# ============================================================
# SESSION STATE
# ============================================================

if "chat_history" not in st.session_state:

    st.session_state.chat_history = [
        {
            "role": "assistant",
            "content": (
                "## 👋 Welcome to the IT Help Desk!\n\n"
                "I'm your **AI IT Support Assistant**.\n\n"
                "I can help you with:\n\n"
                "🔐 Password & Login\n\n"
                "🌐 VPN / Network / Wi-Fi\n\n"
                "📧 Email & Outlook\n\n"
                "🖨️ Printer Issues\n\n"
                "💻 Hardware & Software\n\n"
                "**How may I help you today?**"
            )
        }
    ]

# Conversation context
if "context" not in st.session_state:

    st.session_state.context = ""

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("🛠 IT Support Categories")

    st.markdown("""
### 🔐 Access

- Password Reset
- Login Problems
- Account Locked

### 🌐 Network

- VPN
- Wi-Fi
- Internet

### 📧 Software

- Outlook
- Email
- Excel
- Applications

### 💻 Hardware

- Laptop
- Keyboard
- Mouse
- Screen

### 🖨️ Devices

- Printer
""")

    st.divider()

    st.subheader("💡 Try asking")

    st.caption("“My VPN is not connecting.”")
    st.caption("“I forgot my password.”")
    st.caption("“My printer is offline.”")
    st.caption("“Outlook is not opening.”")

    st.divider()

    # Clear conversation
if st.button("🗑️ Clear Conversation", use_container_width=True):

    st.session_state.chat_history = [
        {
            "role": "assistant",
            "content": (
                "## 👋 Welcome to the IT Help Desk!\n\n"
                "I'm your **AI IT Support Assistant**. 🤖\n\n"
                "I can help you with:\n\n"
                "🔐 Password & Login\n\n"
                "🌐 VPN / Network / Wi-Fi\n\n"
                "📧 Email & Outlook\n\n"
                "🖨️ Printer Issues\n\n"
                "💻 Hardware & Software\n\n"
                "**How may I help you today?**"
            )
        }
    ]

    # Reset conversation context
    st.session_state.context = ""

    st.rerun()
# ============================================================
# DISPLAY CHAT
# ============================================================

for chat in st.session_state.chat_history:

    if chat["role"] == "assistant":
        avatar = BOT_AVATAR
    else:
        avatar = USER_AVATAR

    with st.chat_message(
        chat["role"],
        avatar=avatar
    ):

        st.markdown(chat["content"])

# ============================================================
# CHAT INPUT
# ============================================================

user_text = st.chat_input(
    "💬 Type your IT issue here..."
)

if user_text:

    # --------------------------------------------------------
    # Display User Message
    # --------------------------------------------------------

    st.session_state.chat_history.append(
        {
            "role": "user",
            "content": user_text
        }
    )

    # --------------------------------------------------------
    # Get Response
    # --------------------------------------------------------

    reply, new_context = get_response(
        user_text,
        st.session_state.context
    )

    # --------------------------------------------------------
    # Save Context
    # --------------------------------------------------------

    st.session_state.context = new_context

    # --------------------------------------------------------
    # Display Bot Response
    # --------------------------------------------------------

    st.session_state.chat_history.append(
        {
            "role": "assistant",
            "content": reply
        }
    )

    st.rerun()