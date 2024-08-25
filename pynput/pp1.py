from pynput import keyboard


def on_press(key):
    try:
        print(f'Натиснуто клавішу: {key.char}')
    except AttributeError:
        print(f'Натиснуто спеціальну клавішу: {key}')


def on_release(key):
    print(f'Відпущенv  клавішу: {key}')
    if key == keyboard.Key.esc:
        # Зупиняє слухача клавіатури
        return False


# Створення об'єкта слухача клавіатури
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
