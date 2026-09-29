# utils/chatbot.py


def get_response(message, context=""):

    msg = message.lower().strip()
    context = context.lower().strip()

    # =========================================================
    # GLOBAL RESPONSES
    # These should work regardless of the current context
    # =========================================================

    # ---------------------------------------------------------
    # User says the problem is solved
    # ---------------------------------------------------------
    resolved_words = [
        "resolved",
        "it is resolved",
        "it's resolved",
        "problem is resolved",
        "issue is resolved",
        "fixed",
        "it is fixed",
        "it's fixed",
        "problem is fixed",
        "issue is fixed",
        "solved",
        "it is solved",
        "it's solved",
        "working now",
        "works now",
        "working fine",
        "problem solved",
        "issue solved",
        "all good",
        "everything is fine"
    ]

    if any(phrase in msg for phrase in resolved_words):

        return (
            "That's great! 🎉\n\n"
            "I'm glad your IT issue has been resolved.\n\n"
            "If you face another IT problem, feel free to ask me. "
            "I'm here to help! 🤖"
        ), ""


    # ---------------------------------------------------------
    # User says no / declines help
    # ---------------------------------------------------------
    if msg in [
        "no",
        "no thanks",
        "no thank you",
        "no, thanks",
        "no, thank you",
        "not now",
        "that's okay",
        "its okay",
        "it's okay",
        "okay thanks",
        "okay thank you"
    ]:

        return (
            "No problem! 😊\n\n"
            "I'm glad I could help.\n\n"
            "If you need IT assistance later, just let me know."
        ), ""


    # ---------------------------------------------------------
    # Thank you
    # ---------------------------------------------------------
    if msg in [
        "thanks",
        "thank you",
        "thank",
        "thx",
        "thanks a lot",
        "thank you so much"
    ]:

        return (
            "You're very welcome! 😊\n\n"
            "I'm happy to help. Feel free to contact me "
            "if you have another IT issue."
        ), context


    # ---------------------------------------------------------
    # Goodbye
    # ---------------------------------------------------------
    if msg in [
        "bye",
        "goodbye",
        "see you",
        "see you later",
        "exit",
        "quit"
    ]:

        return (
            "Goodbye! 👋\n\n"
            "Have a great day! I'm here whenever you need IT support."
        ), ""


    # =========================================================
    # GREETINGS
    # =========================================================

    greetings = [
        "hi",
        "hello",
        "hey",
        "hii",
        "hiii",
        "good morning",
        "good afternoon",
        "good evening"
    ]

    if msg in greetings:

        return (
            "Hello! 👋 I'm your **AI IT Support Assistant**.\n\n"
            "How can I help you today?\n\n"
            "I can assist with:\n\n"
            "🔐 **Password & Login**\n"
            "🌐 **VPN / Network / Wi-Fi**\n"
            "📧 **Email / Outlook**\n"
            "🖨️ **Printer Issues**\n"
            "💻 **Hardware**\n"
            "⚙️ **Software & Applications**"
        ), ""


    # =========================================================
    # PASSWORD RESET CONTEXT
    # =========================================================

    if context == "password_reset":

        # User confirms reset
        if (
            msg in ["yes", "yes please", "yeah", "yep", "sure", "okay"]
            or "reset" in msg
            or "reset it" in msg
            or "reset password" in msg
        ):

            return (
                "Absolutely. 🔐 Let's reset your password.\n\n"
                "### Password Reset Steps\n\n"
                "1. Open your organization's **password reset portal**.\n"
                "2. Select **Forgot Password / Reset Password**.\n"
                "3. Enter your registered username or email ID.\n"
                "4. Complete the identity verification process.\n"
                "5. Create a new password.\n"
                "6. Try logging in with the new password.\n\n"
                "🔒 **Security Tip:** Never share your password or OTP "
                "with anyone.\n\n"
                "If the reset portal is unavailable, contact the "
                "**IT / Access Management Team**."
            ), ""


        # User declines reset
        if (
            msg in ["no", "no thanks", "no thank you"]
            or "don't want" in msg
            or "do not want" in msg
            or "not now" in msg
        ):

            return (
                "No problem! 😊\n\n"
                "I won't start the password reset process.\n\n"
                "If you need help later, just let me know."
            ), ""


        # User says password is forgotten
        if (
            "forgot" in msg
            or "forgotten" in msg
            or "don't remember" in msg
            or "do not remember" in msg
        ):

            return (
                "Since you've forgotten your password, "
                "the **Forgot Password / Reset Password** option "
                "is the appropriate next step. 🔐\n\n"
                "Would you like me to guide you through the reset process?"
            ), "password_reset"


        return (
            "Would you like to **reset your password**? 🔐\n\n"
            "Reply **Yes** if you want the reset steps, or **No** "
            "if you don't need them."
        ), "password_reset"


    # =========================================================
    # LOGIN CONTEXT
    # =========================================================

    if context == "login":

        # Incorrect password
        if (
            "incorrect password" in msg
            or "password is incorrect" in msg
            or "wrong password" in msg
            or "invalid password" in msg
            or "password wrong" in msg
            or "password is wrong" in msg
            or "incorrect" in msg
            or "wrong" in msg
        ):

            return (
                "I see. You're receiving an **incorrect password** "
                "message. 🔐\n\n"
                "Please check:\n\n"
                "1. Caps Lock is not enabled.\n"
                "2. Your username is correct.\n"
                "3. You are entering the correct password.\n\n"
                "If you don't remember your password, I can guide "
                "you through the password reset process.\n\n"
                "**Would you like to reset your password?**"
            ), "password_reset"


        # Account locked
        if (
            "locked" in msg
            or "account lock" in msg
            or "account is locked" in msg
        ):

            return (
                "Your account may be locked. 🔒\n\n"
                "Please avoid repeatedly entering your password.\n\n"
                "Contact the **IT / Access Management Team** to "
                "verify your identity and unlock the account."
            ), ""


        # Authentication error
        if (
            "authentication" in msg
            or "credentials" in msg
            or "authentication failed" in msg
        ):

            return (
                "It looks like you're experiencing an authentication "
                "problem. 🔐\n\n"
                "Please verify your username and password.\n\n"
                "If your credentials are correct but authentication "
                "still fails, contact the **Access Management Team**."
            ), ""


        return (
            "I can help troubleshoot your login problem. 🔐\n\n"
            "Please tell me the exact message displayed on the screen.\n\n"
            "For example:\n"
            "• Incorrect password\n"
            "• Account locked\n"
            "• Invalid credentials\n"
            "• Authentication failed"
        ), "login"


    # =========================================================
    # PASSWORD CONTEXT
    # =========================================================

    if context == "password":

        # Forgot password
        if (
            "forgot" in msg
            or "forgotten" in msg
            or "don't remember" in msg
            or "do not remember" in msg
        ):

            return (
                "No problem. 🔐\n\n"
                "Since you've forgotten your password, "
                "we can use the password reset process.\n\n"
                "Would you like me to guide you through resetting it?"
            ), "password_reset"


        # Unable to login
        if (
            "unable to login" in msg
            or "unable to log in" in msg
            or "can't login" in msg
            or "cannot login" in msg
            or "can't log in" in msg
            or "cannot log in" in msg
            or "unable" in msg
            or "login" in msg
            or "log in" in msg
            or "sign in" in msg
        ):

            return (
                "I understand. Let's troubleshoot your **login problem**. 🔐\n\n"
                "Please check:\n\n"
                "1. Your username is correct.\n"
                "2. Caps Lock is not enabled.\n"
                "3. Your password is entered correctly.\n"
                "4. Connect to the company VPN/network if required.\n\n"
                "If you see an error message, please tell me exactly "
                "what it says."
            ), "login"


        # Incorrect password
        if (
            "incorrect" in msg
            or "wrong password" in msg
            or "password is wrong" in msg
            or "invalid password" in msg
        ):

            return (
                "If you're seeing **Incorrect Password**, please check "
                "Caps Lock and re-enter your credentials.\n\n"
                "If you don't remember your password, I can help you "
                "reset it.\n\n"
                "**Would you like to reset your password?**"
            ), "password_reset"


        # Account locked
        if "locked" in msg or "lock" in msg:

            return (
                "Your account may be locked. 🔒\n\n"
                "Please contact the **IT / Access Management Team** "
                "to unlock your account."
            ), ""


        return (
            "I can help with your **Password & Login issue**. 🔐\n\n"
            "Please tell me which problem you're facing:\n\n"
            "🔑 Forgot password\n"
            "🚫 Unable to login\n"
            "❌ Incorrect password\n"
            "🔒 Account locked"
        ), "password"


    # =========================================================
    # VPN ADVANCED CONTEXT
    # =========================================================

    if context == "vpn_advanced":

        if any(word in msg for word in [
            "still",
            "same",
            "not working",
            "doesn't work",
            "does not work",
            "failed",
            "error",
            "problem",
            "issue",
            "no"
        ]):

            return (
                "I understand. Since the basic and advanced VPN "
                "troubleshooting steps did not resolve the problem, "
                "it should be investigated by the **Network Support Team**. 👨‍💻\n\n"
                "### 📋 Incident Summary\n\n"
                "**Category:** Network / VPN\n\n"
                "**Priority:** High\n\n"
                "**Status:** Escalation Recommended\n\n"
                "Please provide the support team with:\n\n"
                "• VPN error message or error code\n"
                "• Screenshot of the error\n"
                "• Time when the issue occurred\n"
                "• VPN server/location\n\n"
                "This information will help the support team investigate "
                "the issue."
            ), ""


        return (
            "Please let me know whether your VPN is **working now** "
            "or you are **still experiencing the problem**."
        ), "vpn_advanced"


    # =========================================================
    # VPN CONTEXT
    # =========================================================

    if context == "vpn":

        # User already tried troubleshooting
        if any(word in msg for word in [
            "already",
            "tried",
            "done",
            "checked",
            "still",
            "same",
            "not working",
            "doesn't work",
            "does not work",
            "error",
            "failed",
            "unable"
        ]):

            return (
                "No problem. Let's move to **advanced VPN troubleshooting**. 🔧\n\n"
                "Please try:\n\n"
                "1. 🔑 Verify your VPN username and password.\n"
                "2. 🌐 Try another VPN server if available.\n"
                "3. 🔄 Restart your computer.\n"
                "4. 🛡️ Check whether firewall/security software is blocking VPN.\n"
                "5. ⚙️ Make sure your VPN client is updated.\n\n"
                "After trying these steps, tell me whether the VPN "
                "is working or still showing the error."
            ), "vpn_advanced"


        if any(word in msg for word in [
            "yes",
            "working",
            "worked",
            "fixed",
            "solved"
        ]):

            return (
                "Excellent! 🎉\n\n"
                "I'm glad your VPN connection is working now.\n\n"
                "Is there anything else I can help you with?"
            ), ""


        return (
            "Have you already tried checking your internet connection "
            "and restarting the VPN application?"
        ), "vpn"


    # =========================================================
    # PRINTER CONTEXT
    # =========================================================

    if context == "printer":

        if "offline" in msg:

            return (
                "For an **offline printer** 🖨️:\n\n"
                "1. Check that the printer is powered on.\n"
                "2. Check the network or USB connection.\n"
                "3. Open Windows Printer Settings.\n"
                "4. Select the correct printer.\n"
                "5. Restart the printer.\n\n"
                "Try printing a test page."
            ), ""


        if "paper" in msg or "jam" in msg:

            return (
                "For a **paper jam** 🖨️:\n\n"
                "1. Turn off the printer.\n"
                "2. Carefully remove the jammed paper.\n"
                "3. Check the paper tray.\n"
                "4. Restart the printer.\n\n"
                "Then try printing again."
            ), ""


        if "not printing" in msg or "print" in msg:

            return (
                "If the printer is **not printing**:\n\n"
                "1. Check the printer connection.\n"
                "2. Check the print queue.\n"
                "3. Remove stuck print jobs.\n"
                "4. Restart the Print Spooler service.\n"
                "5. Print a test page."
            ), ""


        if "detected" in msg:

            return (
                "If the printer is **not detected**, check the "
                "USB/network connection and update or reinstall "
                "the printer driver."
            ), ""


        return (
            "What problem are you experiencing with the printer?\n\n"
            "🖨️ Offline\n"
            "📄 Paper jam\n"
            "❌ Not printing\n"
            "🔌 Not detected"
        ), "printer"


    # =========================================================
    # FIRST PASSWORD MESSAGE
    # =========================================================

    if (
        "password" in msg
        or "forgot my password" in msg
        or "forgot password" in msg
        or "login" in msg
        or "log in" in msg
        or "sign in" in msg
        or "account locked" in msg
    ):

        # Directly recognize forgotten password
        if (
            "forgot" in msg
            or "forgotten" in msg
        ):

            return (
                "No problem. 🔐\n\n"
                "Since you've forgotten your password, "
                "I can guide you through the password reset process.\n\n"
                "Would you like to reset your password?"
            ), "password_reset"


        return (
            "I can help with your **Password & Login issue**. 🔐\n\n"
            "What problem are you facing?\n\n"
            "🔑 Forgot password\n"
            "🚫 Unable to login\n"
            "❌ Incorrect password\n"
            "🔒 Account locked"
        ), "password"


    # =========================================================
    # FIRST VPN MESSAGE
    # =========================================================

    if "vpn" in msg:

        return (
            "I understand that you're facing a **VPN connection issue**. 🌐\n\n"
            "Let's troubleshoot it step by step.\n\n"
            "**Step 1:** Check whether your internet connection is working.\n\n"
            "**Step 2:** Close and restart the VPN application.\n\n"
            "**Step 3:** Try connecting to the VPN again.\n\n"
            "Have you already tried these steps?"
        ), "vpn"


    # =========================================================
    # PRINTER
    # =========================================================

    if "printer" in msg:

        return (
            "I can help with your **printer issue**. 🖨️\n\n"
            "What problem are you experiencing?\n\n"
            "1. Printer is offline\n"
            "2. Paper jam\n"
            "3. Printer is not printing\n"
            "4. Printer is not detected"
        ), "printer"


    # =========================================================
    # EMAIL / OUTLOOK
    # =========================================================

    if (
        "outlook" in msg
        or "email" in msg
        or "mail" in msg
    ):

        return (
            "I can help with your **Email / Outlook issue**. 📧\n\n"
            "Please try:\n\n"
            "1. Check your internet connection.\n"
            "2. Restart Outlook.\n"
            "3. Check whether Outlook is in Offline Mode.\n"
            "4. Check your mailbox storage.\n\n"
            "If you see a specific error, send me the exact error message."
        ), ""


    # =========================================================
    # NETWORK / WIFI
    # =========================================================

    if (
        "wifi" in msg
        or "wi-fi" in msg
        or "internet" in msg
        or "network" in msg
    ):

        return (
            "Let's troubleshoot your **Network / Internet issue**. 🌐\n\n"
            "Please check:\n\n"
            "1. Wi-Fi is enabled.\n"
            "2. Your device is connected to the correct network.\n"
            "3. Restart the Wi-Fi adapter.\n"
            "4. Restart your router if applicable.\n"
            "5. Try accessing another website.\n\n"
            "If the problem continues, tell me the exact error."
        ), ""


    # =========================================================
    # HARDWARE
    # =========================================================

    if any(word in msg for word in [
        "laptop",
        "keyboard",
        "mouse",
        "screen",
        "hardware",
        "computer"
    ]):

        return (
            "I can help with your **hardware issue**. 💻\n\n"
            "Please provide the device/problem details.\n\n"
            "For example:\n"
            "• Laptop not starting\n"
            "• Keyboard not working\n"
            "• Screen flickering\n"
            "• Mouse not responding"
        ), ""


    # =========================================================
    # SOFTWARE
    # =========================================================

    if any(word in msg for word in [
        "software",
        "application",
        "app",
        "excel",
        "word"
    ]):

        return (
            "I can help with your **software/application issue**. ⚙️\n\n"
            "Please provide:\n\n"
            "• Application name\n"
            "• Error message\n"
            "• What you were trying to do"
        ), ""


    # =========================================================
    # NON-IT QUESTIONS
    # =========================================================

    it_keywords = [
        "vpn",
        "password",
        "login",
        "printer",
        "internet",
        "wifi",
        "network",
        "email",
        "outlook",
        "excel",
        "laptop",
        "keyboard",
        "mouse",
        "screen",
        "hardware",
        "software",
        "application",
        "computer",
        "system",
        "account",
        "access",
        "server",
        "error",
        "issue",
        "problem",
        "windows",
        "pc"
    ]

    if not any(word in msg for word in it_keywords):

        return (
            "I'm your **AI IT Support Assistant**, so I can help only "
            "with IT-related issues. 🤖\n\n"
            "I can assist with:\n\n"
            "🔐 Password & Login\n"
            "🌐 VPN / Network / Wi-Fi\n"
            "📧 Email / Outlook\n"
            "🖨️ Printer\n"
            "💻 Hardware\n"
            "⚙️ Software / Applications\n\n"
            "**Example:**\n"
            "“I forgot my password and cannot log in.”"
        ), context


    # =========================================================
    # DEFAULT
    # =========================================================

    return (
        "I understand that you're experiencing an IT issue. 🔧\n\n"
        "Could you provide more details, such as the device/application "
        "name and the exact error message?"
    ), context