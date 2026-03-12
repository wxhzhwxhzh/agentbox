import argparse
from agentbox.version import VERSION
from agentbox.commands import doctor, install


def build_parser():
    parser = argparse.ArgumentParser(
        prog="agentbox",
        description="AgentBox CLI 工具，用于检测和安装开发环境",
        epilog="示例:\n"
               "  agentbox doctor\n"
               "  agentbox install node\n"
               "  agentbox install git",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f"%(prog)s {VERSION}",
        help="显示版本号"
    )

    subparsers = parser.add_subparsers(dest="command")

    # doctor
    doctor_parser = subparsers.add_parser(
        "doctor",
        help="检测系统环境（git/npm）"
    )
    doctor_parser.set_defaults(func=doctor.run)

    # install
    install_parser = subparsers.add_parser(
        "install",
        help="安装开发工具"
    )

    install_parser.add_argument(
        "target",
        choices=["node", "git"],
        help="要安装的软件（node / git）"
    )

    install_parser.set_defaults(func=install.run)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if not hasattr(args, "func"):
        parser.print_help()
        return

    try:
        args.func(args)
    except Exception as e:
        print(f"\n❌ 执行失败: {e}")