
# Password Recovery Code Cracker

This script is designed to brute force 4-digit recovery codes for a password reset endpoint in a legal and authorized environment. It supports high concurrency, customizable headers, and real-time progress tracking.

## Features

- High-speed brute force with concurrency (up to 100 simultaneous requests).
- Real-time progress tracking using a dynamic progress bar.
- Customizable HTTP headers, including `X-Forwarded-For` for bypassing IP restrictions.
- Fully asynchronous, leveraging Python's `aiohttp` library for optimal performance.

---

## How It Works

1. Sends POST requests to the target password reset endpoint.
2. Iterates through all possible 4-digit recovery codes (0000–9999).
3. Detects and stops upon finding a valid recovery code.
4. Outputs the progress and results in the terminal.

---

## Requirements

- **Python**: Version 3.7 or higher.
- **Dependencies**: Install them with `pip`:
  ```bash
  pip install aiohttp tqdm
  ```

---

## Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/password-recovery-cracker.git
   cd password-recovery-cracker
   ```

2. **Edit the script**:
   - Replace `session_cookie` with your actual `PHPSESSID` value.
   - Update the target URL (`url`) if needed.

3. **Run the script**:
   ```bash
   python Hammer-q1.py
   ```

---

## Example Output

```plaintext
[INFO] 脚本开始运行
破解进度:  45%|███████████████▌              | 4500/10000 [00:10<00:12, 450codes/s]
[+] 找到有效验证码: 3121
[INFO] 脚本运行完成
```

---

## Notes

- **Legal Disclaimer**: This script is for educational and ethical penetration testing purposes only. Ensure you have proper authorization before using this tool.
- For large-scale tasks, adjust concurrency (`100 tasks at a time`) in the script.

---

## Contribution

Feel free to contribute to this project by submitting issues or pull requests. Suggestions for performance optimization are welcome.

---



