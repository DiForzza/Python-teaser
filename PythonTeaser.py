import speech_recognition as sr
import pyttsx3

tts = pyttsx3.init()
rate = tts.getProperty('rate')  # Скорость произношения
tts.setProperty('rate', rate - 80)
volume = tts.getProperty('volume')  # Громкость голоса
tts.setProperty('volume', volume + 0.8)
voices = tts.getProperty('voices')
# Задать голос по умолчанию
tts.setProperty('voice', 'ru')
for voice in voices:
    if voice.name == 'Aleksandr':
        # if voice.name == 'Anna':
        tts.setProperty('voice', voice.id)

def record_volume():
    r = sr.Recognizer()
    with sr.Microphone(device_index = 1) as source:
        print('Настраиваюсь.')
        r.adjust_for_ambient_noise(source, duration=0.5) #настройка посторонних шумов
        print('Слушаю...')
        audio = r.listen(source)
    print('Услышала.')
    try:
        query = r.recognize_google(audio, language = 'ru-RU')
        text = query.lower()
        print(f'Вы сказали: {text}')
        tts.say(f'сам {text}')
        tts.runAndWait()
    except:
        print('Error')

while True:
    record_volume()