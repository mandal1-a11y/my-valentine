import streamlit as st
import os

# 1. Page Configuration
st.set_page_config(page_title="My Valentine ❤️", page_icon="💖")

# 2. CSS Styling
st.markdown("""
    <style>
    .stApp { background: linear-gradient(to bottom, #ff99aa, #ff4d6d); }
    .stButton>button { 
        background-color: #ff0054 !important; color: white !important; 
        border-radius: 25px !important; border: 2px solid white !important;
        font-weight: bold !important;
    }
    .poem-box {
        background-color: rgba(255, 255, 255, 0.2);
        padding: 25px;
        border-radius: 15px;
        border: 1px solid white;
        text-align: center;
        font-style: italic;
    }
    h1, h2, h3, p, li { color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. Media Function (Compatible Version - Fixes the TypeError)
def play_media(file_path):
    if os.path.exists(file_path):
        # Removed 'key' argument to avoid the TypeError on older Streamlit versions
        st.audio(file_path, format="audio/mp4", autoplay=True)
    else:
        st.info(f"🎵 Note: {file_path} not found in sidebar!")

# 4. State Management
if 'auth' not in st.session_state: st.session_state.auth = False
if 'step' not in st.session_state: st.session_state.step = 'welcome'

# --- SCREEN 1: PASSWORD ---
if not st.session_state.auth:
    st.title("🔒 Private Access")
    pwd = st.text_input("Whats your favorite color :", type="password")
    if st.button("Unlock"):
        if pwd == "boobies":
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("Access denied, Try again Love ❤ !")

# --- AUTHORIZED CONTENT (Runs only after login) ---
else:
    # DYNAMIC MUSIC SELECTION
    if st.session_state.step == 'memory':
        play_media("memory_lane.m4a")
    elif st.session_state.step == 'vday':
        play_media("v_day.m4a")
    else:
        play_media("song.m4a")

    # STEP 1: WELCOME
    if st.session_state.step == 'welcome':
        st.title("Hello my Handsome, Beautifull, Princess Baby! ❤️")
        if os.path.exists("us.jpg"):
            st.image("us.jpg")
        if st.button("Start the Journey 🌹"):
            st.session_state.step = 'rose'
            st.rerun()

    # STEP 2: ROSE DAY
    elif st.session_state.step == 'rose':
        st.header("Feb 7: Rose Day 💐")
        st.image("https://images.unsplash.com/photo-1582794543139-8ac9cb0f7b11?q=80&w=500")
        st.subheader("For You:")
        st.write("A virtual bouquet of roses. You're my favorite flower babyyyyy. I LOVE YOU VERY VERY MUCHHHHHHHH, MUAHHHHHHH")
        if st.button("Next: Propose Day 💍"):
            st.session_state.step = 'propose'
            st.rerun()

    # STEP 3: PROPOSE DAY
    elif st.session_state.step == 'propose':
        st.header("Feb 8: Propose Day ✨")
        if os.path.exists("proposal.png"):
            st.image("proposal.png")
        st.write("I'd choose you every single time. Will you be mine?")
        if st.button("Next: Memory Lane 📸"):
            st.session_state.step = 'memory'
            st.rerun()

    # STEP 4: MEMORY LANE (10 Photos)
    elif st.session_state.step == 'memory':
        st.header("Our Memory Lane 📸")
        st.write("Every moment with you is a treasure I keep in my heart.")
        
        cols = st.columns(2)
        for i in range(1, 11):
            with cols[i % 2]:
                img_name = f"mem{i}.jpg"
                if os.path.exists(img_name):
                    st.image(img_name, use_container_width=True)
                else:
                    st.write(f"📷 Photo {i}")

        st.write("---")
        if st.button("Next: Hug Day 🤗"):
            st.session_state.step = 'hug'
            st.rerun()

    # STEP 5: HUG DAY
    elif st.session_state.step == 'hug':
        st.header("Feb 12: Hug Day 🤗")
        if os.path.exists("hug.jpg"):
            st.image("hug.jpg")
        st.write("Counting down to the next real hug. I want you to know that your hugs are the safest place for me. I crave it when I have good or bad day, I crave it when am sleeping or walking, i crave it randomlyyyy")
        if st.button("Next: Kiss Day 💋"):
            st.session_state.step = 'kiss'
            st.rerun()

    # STEP 6: KISS DAY
    elif st.session_state.step == 'kiss':
        st.header("Feb 13: Kiss Day 💋")
        if os.path.exists("kiss.jpg"):
            st.image("kiss.jpg")
        st.write("A thousand kisses sent your way until I finally get to kiss you as long as I want!")
        if st.button("The Big Finale! ❤️"):
            st.session_state.step = 'vday'
            st.rerun()

    # STEP 7: VALENTINE'S DAY FINALE
    elif st.session_state.step == 'vday':
        st.balloons()
        # This adds the flower background image back specifically for this page
        st.markdown("""
            <style>
            .stApp {
                background: url("https://images.unsplash.com/photo-1490750967868-88aa4486c946?q=80&w=2070") no-repeat center center fixed !important;
                background-size: cover !important;
            }
            .poem-box {
                background-color: rgba(0, 0, 0, 0.4) !important; /* Making it a bit darker so text is easier to read over flowers */
                padding: 25px;
                border-radius: 15px;
                border: 1px solid white;
                text-align: center;
                font-style: italic;
            }
            </style>
            """, unsafe_allow_html=True)
        st.title("Happy Valentine's Day! 💖")
        st.markdown("""
         <div class="poem-box">
             <p>Miles apart, but close at heart,</p>
             <p>From the very day we got our start.</p>
             <p>Through every call and every screen,</p>
             <p>You're the best man I've ever seen.</p>
             <br>
             <p>No distance can dull the light we share,</p>
             <p>Because I find you everywhere.</p>
             <p>In every thought and every prayer,</p>
             <p>I love you more than I can swear.</p>
         </div>
         """, unsafe_allow_html=True)
        st.write("")
        st.write("Forever yours, bbg Asmita")
        if st.button("Back to Start"):
            st.session_state.step = 'welcome'
