import subprocess
import sys


def run_cli(args):
    """
    运行 CLI 命令并返回结果
    """
    cmd = [sys.executable, "-m", "agentbox"] + args

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )

    return result


def test_help():
    """测试 --help"""
    result = run_cli(["--help"])

    assert result.returncode == 0
    assert "AgentBox CLI" in result.stdout
    assert "doctor" in result.stdout
    assert "install" in result.stdout


def test_version():
    """测试版本输出"""
    result = run_cli(["--version"])

    assert result.returncode == 0
    assert "0.1.0" in result.stdout


def test_doctor_command():
    """测试 doctor 子命令"""
    result = run_cli(["doctor"])

    assert result.returncode == 0
    assert "检测系统环境" in result.stdout or "git" in result.stdout


def test_install_help():
    """测试 install 帮助"""
    result = run_cli(["install", "--help"])

    assert result.returncode == 0
    assert "node" in result.stdout
    assert "git" in result.stdout