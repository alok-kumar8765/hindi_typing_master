import tkinter as tk
from tkinter import ttk, messagebox
import random
import time


# ============================================================
# HINDI TYPING MASTER
# ============================================================
#
# This version has:
#
# 1. Fixed practice paragraph area
# 2. LARGE typing area that is always visible
# 3. Mangal / Unicode mode
# 4. Kruti Dev mode
# 5. Easy / Medium / Hard
# 6. WPM
# 7. CPM
# 8. Accuracy
# 9. Errors
# 10. Timer
# 11. Correct / wrong highlighting
#
# IMPORTANT:
# Install "Kruti Dev 010" on Windows if you want to use
# Kruti Dev mode.
# ============================================================


# ============================================================
# COLORS
# ============================================================

BG = "#f3f6fa"
WHITE = "#ffffff"
DARK = "#111827"
GRAY = "#64748b"

BLUE = "#2563eb"
BLUE_DARK = "#1d4ed8"

GREEN = "#16a34a"
RED = "#dc2626"

BORDER = "#d1d5db"
LIGHT_BLUE = "#eff6ff"


# ============================================================
# PARAGRAPHS - MANGAL / UNICODE
# ============================================================

MANGAL_PARAGRAPHS = {

    "Easy": [

        """भारत हमारा महान देश है। भारत में अनेक धर्म, भाषाएं और संस्कृतियां
पाई जाती हैं। हमारा देश अपनी विविधता और एकता के लिए पूरी दुनिया में
प्रसिद्ध है। हमें अपने देश से प्रेम करना चाहिए और देश की प्रगति के लिए
ईमानदारी से कार्य करना चाहिए। प्रत्येक नागरिक का कर्तव्य है कि वह देश
के नियमों का पालन करे और समाज के विकास में अपना योगदान दे।""",

        """नियमित अभ्यास सफलता की पहली सीढ़ी है। किसी भी काम को अच्छी तरह सीखने
के लिए धैर्य और मेहनत की आवश्यकता होती है। यदि हम प्रतिदिन थोड़ा समय
अभ्यास के लिए निकालते हैं तो कुछ समय बाद हमारी कार्य क्षमता बढ़ने लगती
है। टाइपिंग सीखने वाले विद्यार्थियों को शुरुआत में गति के बजाय शुद्धता
पर अधिक ध्यान देना चाहिए। धीरे-धीरे अभ्यास करने से गति अपने आप बढ़ती है।"""
    ],

    "Medium": [

        """आज के आधुनिक युग में कंप्यूटर हमारे जीवन का एक महत्वपूर्ण हिस्सा बन
गया है। शिक्षा, बैंकिंग, व्यापार, चिकित्सा, सरकारी कार्यालय और संचार
जैसे अनेक क्षेत्रों में कंप्यूटर का उपयोग किया जाता है। कंप्यूटर पर
काम करने वाले व्यक्ति के लिए तेज और सही टाइपिंग एक महत्वपूर्ण कौशल है।
यदि किसी व्यक्ति की टाइपिंग गति अच्छी है और वह कम गलतियां करता है तो
वह अपने दैनिक कार्य को कम समय में पूरा कर सकता है।""",

        """हिंदी टाइपिंग सीखने के लिए नियमित अभ्यास बहुत आवश्यक है। शुरुआत में
विद्यार्थी को कीबोर्ड की प्रत्येक कुंजी पहचानने में कुछ कठिनाई हो सकती
है। लगातार अभ्यास करने से उंगलियों को सही कुंजियों की आदत हो जाती है।
टाइपिंग करते समय स्क्रीन को ध्यान से देखना चाहिए और बार-बार कीबोर्ड
की ओर नहीं देखना चाहिए। इससे उंगलियों की गति और टाइपिंग की शुद्धता
दोनों में धीरे-धीरे सुधार होता है।""",

        """समय किसी भी व्यक्ति के जीवन की सबसे मूल्यवान संपत्ति है। जो व्यक्ति
समय का सही उपयोग करता है वह अपने लक्ष्य को आसानी से प्राप्त कर सकता है।
विद्यार्थियों को पढ़ाई, अभ्यास, खेल और आराम के लिए उचित समय निर्धारित
करना चाहिए। किसी भी परीक्षा की तैयारी करते समय नियमित अध्ययन के साथ
समय प्रबंधन भी बहुत महत्वपूर्ण होता है। छोटी-छोटी अच्छी आदतें भविष्य
में बड़ी सफलता का कारण बन सकती हैं।"""
    ],

    "Hard": [

        """आधुनिक तकनीकी युग में कंप्यूटर और इंटरनेट ने हमारे जीवन को पूरी तरह
बदल दिया है। आज शिक्षा से लेकर व्यापार, बैंकिंग, प्रशासन, चिकित्सा,
अनुसंधान और संचार तक लगभग प्रत्येक क्षेत्र में डिजिटल तकनीक का प्रयोग
हो रहा है। सरकारी कार्यालयों में विभिन्न प्रकार के दस्तावेज तैयार करने,
आंकड़ों को सुरक्षित रखने और नागरिकों तक आवश्यक सेवाएं पहुंचाने के लिए
कंप्यूटर का उपयोग किया जाता है। ऐसे कार्यों में तेज और शुद्ध टाइपिंग
का विशेष महत्व होता है क्योंकि एक छोटी सी गलती भी महत्वपूर्ण दस्तावेज
में समस्या उत्पन्न कर सकती है।""",

        """प्रतियोगी परीक्षाओं की तैयारी करने वाले विद्यार्थियों के लिए नियमित
अभ्यास अत्यंत आवश्यक है। केवल अधिक समय तक पढ़ना ही पर्याप्त नहीं है,
बल्कि पढ़ाई के लिए सही योजना बनाना और उसका नियमित रूप से पालन करना
भी जरूरी है। यदि विद्यार्थी प्रत्येक दिन निर्धारित समय पर टाइपिंग का
अभ्यास करता है तो कुछ ही सप्ताह में उसकी गति और शुद्धता में उल्लेखनीय
सुधार दिखाई देने लगता है। शुरुआत में गलतियों की संख्या अधिक हो सकती
है, लेकिन गलतियों से सीखकर उन्हें दोबारा न दोहराने का प्रयास करना चाहिए।""",

        """एक कुशल टाइपिस्ट केवल तेज गति से ही नहीं बल्कि उच्च शुद्धता के साथ
टाइप करता है। यदि टाइपिंग की गति बहुत अधिक हो लेकिन गलतियों की संख्या
भी अधिक हो तो वास्तविक कार्य क्षमता कम हो जाती है। इसलिए अभ्यास करते
समय पहले सही अक्षर और सही कुंजी पर ध्यान देना चाहिए। जब शुद्धता अच्छी
हो जाए तब धीरे-धीरे गति बढ़ानी चाहिए। लंबे समय तक नियमित अभ्यास करने
से उंगलियों की गति, ध्यान केंद्रित करने की क्षमता और टाइपिंग का आत्मविश्वास
काफी बेहतर हो जाता है।"""
    ]
}


# ============================================================
# KRUTI DEV DATA
# ============================================================

KRUTI_DEV_PARAGRAPHS = {

    "Easy": [

        """Hkkjr ,d egku ns'k gSA Hkkjr esa vusd /keZ] Hkk\"kk,a vkSj laLd`fr;ka
ikbZ tkrh gSaA gekjk ns'k viuh fofo/krk vkSj ,drk ds fy, izfl) gSA
gesa vius ns'k ls izse djuk pkfg, vkSj ns'k dh izxfr ds fy, bZekunkjh
ls dk;Z djuk pkfg,A""",

        """fu;fer vH;kl lQyrk dh igyh lh<+h gSA fdlh Hkh dke dks vPNh rjg
lh[kus ds fy, /kS;Z vkSj esgur dh vko';drk gksrh gSA ;fn ge izfrfnu
FkksM+k le; vH;kl ds fy, fudkyrs gSa rks dqN le; ckn gekjh dk;Z {kerk
c<+us yxrh gSA"""
    ],

    "Medium": [

        """vkt ds vk/qfud ;qx esa dEI;wVj gekjs thou dk ,d egRoiw.kZ fgLlk
cu x;k gSA f'k{kk] cSafdax] O;kikj] fpfdRlk] ljdkjh dk;kZy; vkSj
lapkj tSls vusd {ks=ksa esa dEI;wVj dk mi;ksx fd;k tkrk gSA""",

        """fgUnh Vafix lh[kus ds fy, fu;fer vH;kl cgqr vko';d gSA
'kq:vkr esa fo|kFkhZ dks dhcksMZ dh izR;sd dqath igpkuus esa dqN dfBukbZ
gks ldrh gSA yxkrkj vH;kl djus ls m¡xfy;ksa dks lgh dqath;ksa dh vknr
gks tkrh gSA"""
    ],

    "Hard": [

        """vk/qfud rduhdh ;qx esa dEI;wVj vkSj baVjusV us gekjs thou dks iwjh
rjg cny fn;k gSA vkt f'k{kk ls ysdj O;kikj] cSafdax] iz'kklu] fpfdRlk
vkSj lapkj rd yxHkx izR;sd {ks= esa fMftVy rduhd dk iz;ksx gks jgk gSA""",

        """izfr;ksxh ijh{kkvksa dh rS;kjh djus okys fo|kfFkZ;ksa ds fy, fu;fer
vH;kl vR;ar vko';d gSA dsoy vf/d le; rd i<+uk gh i;kZIr ugha gS]
cfYd i<+kbZ ds fy, lgh ;kstuk cukuk vkSj mldk fu;fer :i ls ikyu
djuk Hkh t:jh gSA"""
    ]
}


# ============================================================
# GLOBAL VARIABLES
# ============================================================

current_text = ""
test_running = False
start_time = None
after_id = None


# ============================================================
# MAIN WINDOW
# ============================================================

root = tk.Tk()

root.title("Hindi Typing Master")

root.geometry("1200x800")

root.minsize(950, 700)

root.configure(bg=BG)


# ============================================================
# HEADER
# ============================================================

header = tk.Frame(
    root,
    bg=BG
)

header.pack(
    fill="x",
    pady=(12, 5)
)


tk.Label(
    header,
    text="Hindi Typing Master",
    font=("Arial", 26, "bold"),
    bg=BG,
    fg=DARK
).pack()


tk.Label(
    header,
    text="Mangal & Kruti Dev Typing Practice",
    font=("Arial", 11),
    bg=BG,
    fg=GRAY
).pack(
    pady=(2, 3)
)


# ============================================================
# CONTROL BAR
# ============================================================

control = tk.Frame(
    root,
    bg=WHITE,
    highlightbackground=BORDER,
    highlightthickness=1
)

control.pack(
    fill="x",
    padx=25,
    pady=5
)


tk.Label(
    control,
    text="Mode:",
    font=("Arial", 10, "bold"),
    bg=WHITE,
    fg=DARK
).pack(
    side="left",
    padx=(15, 5),
    pady=10
)


mode_combo = ttk.Combobox(
    control,
    values=[
        "Mangal / Unicode",
        "Kruti Dev"
    ],
    state="readonly",
    width=20
)

mode_combo.set(
    "Mangal / Unicode"
)

mode_combo.pack(
    side="left"
)


tk.Label(
    control,
    text="Difficulty:",
    font=("Arial", 10, "bold"),
    bg=WHITE,
    fg=DARK
).pack(
    side="left",
    padx=(20, 5)
)


difficulty_combo = ttk.Combobox(
    control,
    values=[
        "Easy",
        "Medium",
        "Hard"
    ],
    state="readonly",
    width=12
)

difficulty_combo.set(
    "Medium"
)

difficulty_combo.pack(
    side="left"
)


# START BUTTON

start_button = tk.Button(
    control,
    text="▶ START TEST",
    font=("Arial", 11, "bold"),
    bg=BLUE,
    fg=WHITE,
    activebackground=BLUE_DARK,
    activeforeground=WHITE,
    relief="flat",
    cursor="hand2",
    padx=28,
    pady=9
)

start_button.pack(
    side="right",
    padx=15
)


# ============================================================
# STATISTICS
# ============================================================

stats = tk.Frame(
    root,
    bg=BG
)

stats.pack(
    fill="x",
    padx=25,
    pady=5
)


def make_stat(title, value):

    frame = tk.Frame(
        stats,
        bg=WHITE,
        highlightbackground=BORDER,
        highlightthickness=1
    )

    frame.pack(
        side="left",
        fill="x",
        expand=True,
        padx=3
    )

    tk.Label(
        frame,
        text=title,
        font=("Arial", 8),
        bg=WHITE,
        fg=GRAY
    ).pack(
        pady=(5, 0)
    )

    label = tk.Label(
        frame,
        text=value,
        font=("Arial", 16, "bold"),
        bg=WHITE,
        fg=DARK
    )

    label.pack(
        pady=(0, 5)
    )

    return label


wpm_label = make_stat(
    "WPM",
    "0"
)

cpm_label = make_stat(
    "CPM",
    "0"
)

accuracy_label = make_stat(
    "ACCURACY",
    "100%"
)

errors_label = make_stat(
    "ERRORS",
    "0"
)

time_label = make_stat(
    "TIME",
    "0 sec"
)


# ============================================================
# PRACTICE AREA
# ============================================================
#
# IMPORTANT:
# Fixed height.
# It cannot push the typing box off the screen.
# ============================================================

tk.Label(
    root,
    text="PRACTICE PARAGRAPH",
    font=("Arial", 10, "bold"),
    bg=BG,
    fg=DARK
).pack(
    anchor="w",
    padx=25,
    pady=(8, 3)
)


practice_frame = tk.Frame(
    root,
    bg=WHITE,
    highlightbackground=BORDER,
    highlightthickness=1
)

practice_frame.pack(
    fill="x",
    padx=25,
    pady=(0, 7)
)


practice_scroll = tk.Scrollbar(
    practice_frame
)

practice_scroll.pack(
    side="right",
    fill="y"
)


practice_text = tk.Text(
    practice_frame,

    # FIXED HEIGHT
    height=7,

    wrap="word",

    font=("Nirmala UI", 17),

    bg=WHITE,

    fg=DARK,

    relief="flat",

    padx=15,

    pady=12,

    spacing1=3,

    spacing3=3,

    yscrollcommand=practice_scroll.set
)

practice_text.pack(
    fill="both",
    expand=True
)


practice_scroll.config(
    command=practice_text.yview
)


practice_text.config(
    state="disabled"
)


# Highlight styles

practice_text.tag_configure(
    "correct",
    foreground=GREEN
)

practice_text.tag_configure(
    "wrong",
    foreground=RED,
    underline=True
)

practice_text.tag_configure(
    "remaining",
    foreground=DARK
)


# ============================================================
# TYPING AREA
# ============================================================

typing_title = tk.Label(
    root,
    text="TYPE HERE ↓",
    font=("Arial", 12, "bold"),
    bg=BG,
    fg=BLUE
)

typing_title.pack(
    anchor="w",
    padx=25,
    pady=(4, 3)
)


# BLUE BORDER MAKES IT OBVIOUS

typing_frame = tk.Frame(
    root,
    bg=WHITE,
    highlightbackground=BLUE,
    highlightcolor=BLUE,
    highlightthickness=3
)

typing_frame.pack(
    fill="both",
    expand=True,
    padx=25,
    pady=(0, 6)
)


# ============================================================
# ACTUAL TYPING BOX
# ============================================================

entry = tk.Text(
    typing_frame,

    # LARGE TYPING AREA
    height=6,

    wrap="word",

    # Unicode Hindi font
    font=("Nirmala UI", 19),

    # IMPORTANT:
    # These guarantee visible text.
    bg="#ffffff",
    fg="#111827",

    # Blue cursor
    insertbackground=BLUE,
    insertwidth=3,

    # Selection
    selectbackground="#bfdbfe",
    selectforeground="#111827",

    relief="flat",

    borderwidth=0,

    padx=18,
    pady=15,

    spacing1=4,
    spacing3=4
)

entry.pack(
    fill="both",
    expand=True
)


# ============================================================
# STATUS
# ============================================================

status = tk.Label(
    root,
    text="Press START TEST to begin.",
    font=("Arial", 10, "bold"),
    bg=BG,
    fg=GRAY
)

status.pack(
    pady=3
)


# ============================================================
# BOTTOM BUTTONS
# ============================================================

buttons = tk.Frame(
    root,
    bg=BG
)

buttons.pack(
    pady=(2, 8)
)


new_button = tk.Button(
    buttons,
    text="↻ NEW TEST",
    font=("Arial", 10, "bold"),
    bg="#e2e8f0",
    fg=DARK,
    relief="flat",
    cursor="hand2",
    padx=25,
    pady=8
)

new_button.pack(
    side="left",
    padx=5
)


reset_button = tk.Button(
    buttons,
    text="RESET",
    font=("Arial", 10, "bold"),
    bg="#fee2e2",
    fg="#991b1b",
    relief="flat",
    cursor="hand2",
    padx=25,
    pady=8
)

reset_button.pack(
    side="left",
    padx=5
)


# ============================================================
# FUNCTIONS
# ============================================================

def get_dataset():

    if mode_combo.get() == "Mangal / Unicode":

        return MANGAL_PARAGRAPHS

    return KRUTI_DEV_PARAGRAPHS


def get_font():

    if mode_combo.get() == "Mangal / Unicode":

        return (
            "Nirmala UI",
            19
        )

    return (
        "Kruti Dev 010",
        19
    )


def update_fonts():

    font = get_font()

    practice_text.configure(
        font=font
    )

    entry.configure(
        font=font
    )


def cancel_timer():

    global after_id

    if after_id is not None:

        try:
            root.after_cancel(
                after_id
            )
        except:
            pass

        after_id = None


def start_test():

    global current_text
    global test_running
    global start_time

    cancel_timer()

    update_fonts()

    dataset = get_dataset()

    level = difficulty_combo.get()

    current_text = random.choice(
        dataset[level]
    ).strip()

    # Display paragraph

    practice_text.config(
        state="normal"
    )

    practice_text.delete(
        "1.0",
        tk.END
    )

    practice_text.insert(
        "1.0",
        current_text
    )

    practice_text.config(
        state="disabled"
    )

    # Scroll paragraph to top

    practice_text.yview_moveto(
        0
    )

    # CLEAR TYPING BOX

    entry.delete(
        "1.0",
        tk.END
    )

    # Reset statistics

    wpm_label.config(
        text="0"
    )

    cpm_label.config(
        text="0"
    )

    accuracy_label.config(
        text="100%"
    )

    errors_label.config(
        text="0"
    )

    time_label.config(
        text="0 sec"
    )

    status.config(
        text="Type the paragraph above...",
        fg=BLUE
    )

    # Start

    start_time = time.time()

    test_running = True

    # THIS IS IMPORTANT:
    # Put cursor directly into typing box.

    entry.focus_set()

    update_stats()


def calculate_stats(typed):

    correct = 0
    errors = 0

    length = min(
        len(typed),
        len(current_text)
    )

    for i in range(length):

        if typed[i] == current_text[i]:

            correct += 1

        else:

            errors += 1

    if len(typed) == 0:

        accuracy = 100

    else:

        accuracy = (
            correct /
            len(typed)
        ) * 100

    return correct, errors, accuracy


def update_highlight(typed):

    practice_text.config(
        state="normal"
    )

    practice_text.delete(
        "1.0",
        tk.END
    )

    for i, char in enumerate(
        current_text
    ):

        if i < len(typed):

            if typed[i] == char:

                practice_text.insert(
                    tk.END,
                    char,
                    "correct"
                )

            else:

                practice_text.insert(
                    tk.END,
                    char,
                    "wrong"
                )

        else:

            practice_text.insert(
                tk.END,
                char,
                "remaining"
            )

    practice_text.config(
        state="disabled"
    )


def update_stats():

    global after_id

    if not test_running:

        return

    typed = entry.get(
        "1.0",
        tk.END
    ).rstrip("\n")

    # Prevent typing beyond paragraph

    if len(typed) > len(current_text):

        typed = typed[
            :len(current_text)
        ]

        entry.delete(
            "1.0",
            tk.END
        )

        entry.insert(
            "1.0",
            typed
        )

    elapsed = (
        time.time()
        -
        start_time
    )

    if elapsed <= 0:

        elapsed = 0.01

    correct, errors, accuracy = calculate_stats(
        typed
    )

    characters = len(typed)

    # Standard WPM
    wpm = int(
        (
            characters /
            5 /
            elapsed
        ) * 60
    )

    # CPM
    cpm = int(
        (
            characters /
            elapsed
        ) * 60
    )

    wpm_label.config(
        text=str(wpm)
    )

    cpm_label.config(
        text=str(cpm)
    )

    accuracy_label.config(
        text=f"{accuracy:.0f}%"
    )

    errors_label.config(
        text=str(errors)
    )

    time_label.config(
        text=f"{int(elapsed)} sec"
    )

    update_highlight(
        typed
    )

    # Complete

    if typed == current_text:

        finish_test()

        return

    after_id = root.after(
        150,
        update_stats
    )


def finish_test():

    global test_running

    test_running = False

    cancel_timer()

    typed = entry.get(
        "1.0",
        tk.END
    ).rstrip("\n")

    elapsed = (
        time.time()
        -
        start_time
    )

    if elapsed <= 0:

        elapsed = 0.01

    correct, errors, accuracy = calculate_stats(
        typed
    )

    characters = len(typed)

    wpm = int(
        (
            characters /
            5 /
            elapsed
        ) * 60
    )

    cpm = int(
        (
            characters /
            elapsed
        ) * 60
    )

    wpm_label.config(
        text=str(wpm)
    )

    cpm_label.config(
        text=str(cpm)
    )

    accuracy_label.config(
        text=f"{accuracy:.0f}%"
    )

    errors_label.config(
        text=str(errors)
    )

    time_label.config(
        text=f"{int(elapsed)} sec"
    )

    status.config(
        text=(
            f"✓ TEST COMPLETE   "
            f"WPM: {wpm}   |   "
            f"CPM: {cpm}   |   "
            f"Accuracy: {accuracy:.0f}%"
        ),
        fg=GREEN
    )


def new_test():

    start_test()


def reset_test():

    global test_running
    global current_text

    test_running = False

    cancel_timer()

    current_text = ""

    entry.delete(
        "1.0",
        tk.END
    )

    practice_text.config(
        state="normal"
    )

    practice_text.delete(
        "1.0",
        tk.END
    )

    practice_text.insert(
        "1.0",
        "Press START TEST to begin your typing practice."
    )

    practice_text.config(
        state="disabled"
    )

    wpm_label.config(
        text="0"
    )

    cpm_label.config(
        text="0"
    )

    accuracy_label.config(
        text="100%"
    )

    errors_label.config(
        text="0"
    )

    time_label.config(
        text="0 sec"
    )

    status.config(
        text="Press START TEST to begin.",
        fg=GRAY
    )

    # Return cursor to typing box

    entry.focus_set()


# ============================================================
# MODE CHANGE
# ============================================================

def mode_changed(event=None):

    if test_running:

        answer = messagebox.askyesno(
            "Change Mode",
            "Changing mode will stop the current test.\n\nContinue?"
        )

        if not answer:

            return

        reset_test()

    update_fonts()


mode_combo.bind(
    "<<ComboboxSelected>>",
    mode_changed
)


# ============================================================
# DIFFICULTY CHANGE
# ============================================================

def difficulty_changed(event=None):

    if test_running:

        answer = messagebox.askyesno(
            "Change Difficulty",
            "Start a new test with this difficulty?"
        )

        if answer:

            start_test()


difficulty_combo.bind(
    "<<ComboboxSelected>>",
    difficulty_changed
)


# ============================================================
# BUTTON COMMANDS
# ============================================================

start_button.config(
    command=start_test
)

new_button.config(
    command=new_test
)

reset_button.config(
    command=reset_test
)


# ============================================================
# KEYBOARD SHORTCUTS
# ============================================================

root.bind(
    "<F5>",
    lambda event: start_test()
)

root.bind(
    "<Escape>",
    lambda event: reset_test()
)


# ============================================================
# INITIAL SCREEN
# ============================================================

practice_text.config(
    state="normal"
)

practice_text.insert(
    "1.0",
    "Press START TEST to begin your typing practice."
)

practice_text.config(
    state="disabled"
)


update_fonts()


# ============================================================
# START APPLICATION
# ============================================================

root.mainloop()
