import shutil
import subprocess


def check_tool(name, version_cmd):

    path = shutil.which(name)

    if not path:
        return False, None

    try:
        result = subprocess.run(
            version_cmd,
            capture_output=True,
            text=True
        )

        version = result.stdout.strip() or result.stderr.strip()
        return True, version

    except Exception:
        return True, "版本获取失败"


def run(args):

    print("🔎 正在检测系统环境...\n")

    tools = {
        "git": ["git", "--version"],
        "node": ["node", "--version"],
    }

    for tool, cmd in tools.items():

        ok, version = check_tool(tool, cmd)

        if ok:
            print(f"✔ {tool} 已安装")
            print(f"  版本: {version}\n")
        else:
            print(f"✘ {tool} 未安装\n")