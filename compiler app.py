from gtts import gTTS

txt = input("Enter a text to transfer to audio : ")
langue = input("Which language you wrote with (en/ar/fr/es) : ")
fn = input("Name your audio file : ")

res = gTTS(text=txt,lang=langue)
res.save(fn+".mp3")