import streamlit as st
import random

st.set_page_config(page_title="K-Drama Recommender", page_icon="🎬")
st.title("🎎 K-Drama Recommender")
st.write("Choose your favorite genre to explore K-Dramas and meet their iconic leads!")

kdramas = {
    "romantic": [
        {"title": "Crash Landing on You", "desc": "A South Korean heiress accidentally lands in North Korea.", "character": "🧥 Ri Jeong-hyeok: 'I'm calm, loyal, and unexpectedly romantic.'", "url": "https://en.wikipedia.org/wiki/Crash_Landing_on_You"},
        {"title": "Business Proposal", "desc": "She pretends on a blind date... with her boss.", "character": "👔 Kang Tae-moo: 'CEO with a heart I didn’t know I had.'", "url": "https://en.wikipedia.org/wiki/Business_Proposal_(TV_series)"},
        {"title": "Weightlifting Fairy Kim Bok-joo", "desc": "A weightlifter falls in love while chasing dreams.", "character": "🏋️ Kim Bok-joo: 'Strong outside, soft inside.'", "url": "https://en.wikipedia.org/wiki/Weightlifting_Fairy_Kim_Bok-joo"},
        {"title": "Hometown Cha-Cha-Cha", "desc": "A city dentist opens shop in a seaside village.", "character": "🦷 Hong Du-sik: 'Mr. Fix-It with a warm smile.'", "url": "https://en.wikipedia.org/wiki/Hometown_Cha-Cha-Cha"},
        {"title": "Because This is My First Life", "desc": "Two people marry for convenience and discover love.", "character": "🏠 Nam Se-hee: 'Love is... unexpected.'", "url": "https://en.wikipedia.org/wiki/Because_This_Is_My_First_Life"},
    ],
    "action": [
        {"title": "Vincenzo", "desc": "A mafia lawyer returns to Korea to fight corruption.", "character": "💼 Vincenzo Cassano: 'Justice... with style and fire.'", "url": "https://en.wikipedia.org/wiki/Vincenzo_(TV_series)"},
        {"title": "Itaewon Class", "desc": "An ex-con and misfits start a bar to fight back against a food empire.", "character": "🍜 Park Sae-ro-yi: 'I don't kneel to injustice.'", "url": "https://en.wikipedia.org/wiki/Itaewon_Class"},
        {"title": "The Uncanny Counter", "desc": "Demon hunters disguised as noodle shop workers.", "character": "🍜 So Mun: 'Even broken people can fight monsters.'", "url": "https://en.wikipedia.org/wiki/The_Uncanny_Counter"},
        {"title": "Tale of the Nine Tailed", "desc": "A gumiho protects the human world from evil spirits.", "character": "🦊 Lee Yeon: 'Immortal but lonely... until you came.'", "url": "https://en.wikipedia.org/wiki/Tale_of_the_Nine_Tailed"}
    ],
    "melodrama": [
        {"title": "Mr. Sunshine", "desc": "A Korean boy returns as a U.S. officer in turbulent times.", "character": "☀️ Eugene Choi: 'Born in war, shaped by love.'", "url": "https://en.wikipedia.org/wiki/Mr._Sunshine_(South_Korean_TV_series)"},
        {"title": "Moon Lovers: Scarlet Heart Ryeo", "desc": "A modern woman lands in Goryeo era and meets princes.", "character": "🌕 Wang So: 'Love scars, even royals.'", "url": "https://en.wikipedia.org/wiki/Moon_Lovers:_Scarlet_Heart_Ryeo"},
        {"title": "My Mister", "desc": "A man and a struggling young woman find healing.", "character": "👨‍💼 Park Dong-hoon: 'Kindness in silence.'", "url": "https://en.wikipedia.org/wiki/My_Mister"},
        {"title": "Twenty-Five Twenty-One", "desc": "A teen fencer finds love during a financial crisis.", "character": "🏅 Baek Yi-jin: 'From ruins to love.'", "url": "https://en.wikipedia.org/wiki/Twenty-Five_Twenty-One"}
    ],
    "fantasy": [
        {"title": "Alchemy of Souls", "desc": "Soul shifters, magic, and fate collide in Daeho.", "character": "🌀 Jang Uk: 'Even death bows to destiny.'", "url": "https://en.wikipedia.org/wiki/Alchemy_of_Souls"},
        {"title": "Extraordinary You", "desc": "A girl realizes she’s a comic book character.", "character": "📖 Eun Dan-oh: 'I’ll write my own story.'", "url": "https://en.wikipedia.org/wiki/Extraordinary_You"},
        {"title": "The King: Eternal Monarch", "desc": "Parallel universes collide through a mysterious portal.", "character": "👑 Lee Gon: 'Mathematics and monarchy — both rule.'", "url": "https://en.wikipedia.org/wiki/The_King:_Eternal_Monarch"},
        {"title": "Guardian: The Lonely and Great God", "desc": "An immortal goblin seeks to end his cursed life.", "character": "🗡️ Kim Shin: 'I've lived too long to fear anything.'", "url": "https://en.wikipedia.org/wiki/Guardian:_The_Lonely_and_Great_God"},
        {"title": "Doom at Your Service", "desc": "A girl makes a contract with doom itself.", "character": "☄️ Myul Mang: 'To live is to fall in love.'", "url": "https://en.wikipedia.org/wiki/Doom_at_Your_Service"}
    ],
    "school": [
        {"title": "School 2017", "desc": "High school teens struggle with grades and rebellion.", "character": "📝 Ra Eun-ho: 'Dream big, even when scolded.'", "url": "https://en.wikipedia.org/wiki/School_2017"},
        {"title": "Dream High", "desc": "Talented students chase dreams at a music school.", "character": "🎤 Song Sam-dong: 'Dreams are louder than fear.'", "url": "https://en.wikipedia.org/wiki/Dream_High"},
        {"title": "Who Are You: School 2015", "desc": "Twins swap places and uncover dark secrets.", "character": "🧍 Go Eun-byul: 'Truth hides behind the uniform.'", "url": "https://en.wikipedia.org/wiki/Who_Are_You:_School_2015"},
        {"title": "True Beauty", "desc": "A girl uses makeup to transform her social status.", "character": "💄 Lim Ju-kyung: 'Beauty is more than a face.'", "url": "https://en.wikipedia.org/wiki/True_Beauty_(South_Korean_TV_series)"}
    ],
    "medical": [
        {"title": "Hospital Playlist", "desc": "Five doctors bond over music and saving lives.", "character": "🎶 Lee Ik-jun: 'Surgeon by day, singer by night.'", "url": "https://en.wikipedia.org/wiki/Hospital_Playlist"},
        {"title": "Dr. Romantic", "desc": "A genius surgeon hides in a countryside hospital.", "character": "🏥 Kim Sa-bu: 'Patients first, always.'", "url": "https://en.wikipedia.org/wiki/Dr._Romantic"}
    ],
    "historical": [
        {"title": "Love in the Moonlight", "desc": "A girl disguises as a eunuch in the royal palace.", "character": "🌙 Lee Yeong: 'Heart first, crown later.'", "url": "https://en.wikipedia.org/wiki/Love_in_the_Moonlight"}
    ],
    "slice of life": [
        {"title": "Reply 1988", "desc": "Nostalgic life and friendship in a small Seoul neighborhood.", "character": "🎧 Choi Taek: 'Go, baduk. Stay, love.'", "url": "https://en.wikipedia.org/wiki/Reply_1988"},
        {"title": "My Liberation Notes", "desc": "Three siblings seek freedom in a mundane life.", "character": "🧳 Mr. Gu: 'Peace is louder than noise.'", "url": "https://en.wikipedia.org/wiki/My_Liberation_Notes"},
        {"title": "Misaeng: Incomplete Life", "desc": "A former baduk player adjusts to corporate life.", "character": "📁 Jang Geu-rae: 'Play life like a game of Go.'", "url": "https://en.wikipedia.org/wiki/Misaeng:_Incomplete_Life"},
        {"title": "When the Camellia Blooms", "desc": "A single mom runs a bar in a small town.", "character": "🌼 Dong-baek: 'Love blooms from strength.'", "url": "https://en.wikipedia.org/wiki/When_the_Camellia_Blooms"}
    ],
    "supernatural": [
        {"title": "Hotel del Luna", "desc": "A hotel for ghosts run by a cursed woman.", "character": "🌑 Jang Man-wol: 'Every soul has a story.'", "url": "https://en.wikipedia.org/wiki/Hotel_del_Luna"},
        {"title": "Bring It On, Ghost", "desc": "A boy who can see ghosts fights them with a girl spirit.", "character": "👻 Park Bong-pal: 'Boo is just the beginning.'", "url": "https://en.wikipedia.org/wiki/Bring_It_On,_Ghost"},
        {"title": "Master's Sun", "desc": "A woman sees ghosts and finds peace with a CEO.", "character": "☀️ Joo Joong-won: 'You see ghosts, I see you.'", "url": "https://en.wikipedia.org/wiki/Master%27s_Sun"},
        {"title": "Hi Bye, Mama!", "desc": "A mother gets a 49-day chance to return to life.", "character": "🍼 Cha Yu-ri: 'Love beyond death.'", "url": "https://en.wikipedia.org/wiki/Hi_Bye,_Mama!"}
    ],
    "forbidden": [
        {"title": "The World of the Married", "desc": "A wife uncovers her husband’s betrayal.", "character": "💔 Ji Sun-woo: 'Love can ruin or revive.'", "url": "https://en.wikipedia.org/wiki/The_World_of_the_Married"},
        {"title": "Secret Love Affair", "desc": "An elite woman falls for her young piano student.", "character": "🎹 Oh Hye-won: 'Talent breaks walls.'", "url": "https://en.wikipedia.org/wiki/Secret_Love_Affair"},
        {"title": "Temptation of Wife", "desc": "A betrayed woman returns under a new identity.", "character": "💄 Goo Eun-jae: 'Revenge is flawless.'", "url": "https://en.wikipedia.org/wiki/Temptation_of_Wife"},
        {"title": "Nevertheless", "desc": "Two art students dance around temptation.", "character": "🖌️ Park Jae-eon: 'Don't fall for me.'", "url": "https://en.wikipedia.org/wiki/Nevertheless_(TV_series)"}
    ]
}

genre = st.selectbox("Select a genre:", list(kdramas.keys()))

st.subheader(f"Top Picks in {genre.title()} 🎥")

for drama in kdramas[genre]:
    st.markdown(f"### 🎬 [{drama['title']}]({drama['url']})")
    st.write(f"**Plot:** {drama['desc']}")
    st.markdown(f"**🧑 Lead Says:** {drama['character']}")
    st.markdown("---")

if st.button("🎲 Random Pick For Me!"):
    random_genre = random.choice(list(kdramas.keys()))
    random_drama = random.choice(kdramas[random_genre])
    st.success(f"You got a **{random_genre.title()}** drama!")
    st.markdown(f"### 🎬 [{random_drama['title']}]({random_drama['url']})")
    st.write(f"**Plot:** {random_drama['desc']}")
    st.markdown(f"**🧑 Lead Says:** {random_drama['character']}")
    st.markdown("---")