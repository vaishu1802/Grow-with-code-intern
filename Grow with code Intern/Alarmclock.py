import datetime
import time
import winsound
def  set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Alarm! Wake up!")
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)  # Play sound (replace "sound.wav" with your preferred alarm sound file)
            break
        time.sleep(1)

# Set the alarm time (format: HH:MM:SS)
alarm_time = "07:00:00"
set_alarm(alarm_time)