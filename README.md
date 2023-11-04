# Keylogger with Discord Webhook Integration

This is a simple keylogger script that logs keystrokes and sends them to a specified Discord webhook. Please note that the use of keyloggers without the explicit consent of the user is unethical and potentially illegal. This script is provided for educational purposes only, and it should only be used responsibly and with the necessary permissions.

## Prerequisites

Before using this keylogger script, you need to have the following dependencies installed:

- [pynput](https://pypi.org/project/pynput/): A Python library to monitor and control input devices.
- [dhooks](https://pypi.org/project/dhooks/): A Python library for Discord webhook integration.

You can install these dependencies using pip:

```bash
pip install pynput dhooks
```

## Usage

- Open the script and replace the `WEBHOOK_URL` variable with the URL of the Discord webhook to which you want to send the keylogs.
  
- Optionally, you can adjust the `TIME_INTERVAL` variable to set the delay (in seconds) between each report to the webhook. The default is 10 seconds.

- Run the script, and it will start logging keystrokes and sending them to the specified Discord webhook.

## Important Considerations

- The use of keyloggers without consent is a violation of privacy and may be illegal in many jurisdictions. Always obtain explicit permission from users before using this script.

- Be responsible when using this script, and ensure that you comply with all applicable laws and ethical standards.

- This script is intended for educational purposes only and should not be used for malicious activities.

- Use the script in a controlled environment, such as on your own computer, for legitimate and lawful purposes.

## Disclaimer

The author and maintainers of this script are not responsible for any misuse or unlawful activities conducted using this keylogger. Use it responsibly and in accordance with the law.
