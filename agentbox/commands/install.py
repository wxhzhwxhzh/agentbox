import platform
import subprocess


def install_node():

    system = platform.system()

    print("📦 开始安装 Node.js...")

    if system == "Windows":
        cmd = ["winget", "install", "-e", "--id", "OpenJS.NodeJS"]

    elif system == "Darwin":
        cmd = ["brew", "install", "node"]

    elif system == "Linux":
        cmd = ["sudo", "apt", "install", "-y", "nodejs", "npm"]

    else:
        raise RuntimeError("当前系统不支持自动安装")

    subprocess.run(cmd)


def install_git():

    system = platform.system()

    print("📦 开始安装 Git...")

    if system == "Windows":
        cmd = ["winget", "install", "--id", "Git.Git"]

    elif system == "Darwin":
        cmd = ["brew", "install", "git"]

    elif system == "Linux":
        cmd = ["sudo", "apt", "install", "-y", "git"]

    else:
        raise RuntimeError("当前系统不支持自动安装")

    subprocess.run(cmd)


def run(args):

    try:

        if args.target == "node":
            install_node()

        elif args.target == "git":
            install_git()

        print("\n✔ 安装命令执行完成")

    except Exception as e:

        print("\n❌ 安装失败")
        print(e)