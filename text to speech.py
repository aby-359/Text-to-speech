from gtts import gTTS
import os
text="Hey Iam Aby Nice meeting you"
output=gTTS(text=text,lang="en",slow=False)
output.save("audio3.mp3")
os.system("start audio3.mp3")




































