# AgentBox

**AgentBox** 是一个基于 Python 的轻量级 CLI 工具，用于快速检测和安装常见开发环境组件，例如 Git、Node.js 等。

项目使用 **argparse** 构建命令行接口，并使用 **uv** 进行依赖与环境管理。

---

## ✨ 特性

* 简洁易用的 CLI 设计
* 支持系统环境检测
* 支持自动安装常见开发工具
* 跨平台支持（Windows / macOS / Linux）
* 基于 Python `argparse` 构建
* 使用 `uv` 进行依赖管理

---

## 📦 安装

### 方式一：开发模式安装（推荐）

```bash
uv pip install -e .
```

安装后即可使用全局命令：

```bash
agentbox
```

---

### 方式二：直接运行

```bash
python -m agentbox
```

---

## 🚀 使用方法

### 查看帮助

```bash
agentbox --help
```

或

```bash
agentbox -h
```

---

### 查看版本

```bash
agentbox --version
```

输出示例：

```
agentbox 0.1.0
```

---

### 环境检测

检测系统是否安装 `git` 和 `npm`：

```bash
agentbox doctor
```

示例输出：

```
🔎 正在检测系统环境...

✔ git 已安装
  版本: git version 2.44.0

✔ npm 已安装
  版本: 10.8.2
```

---

### 安装 Node.js

```bash
agentbox install node
```

---

### 安装 Git

```bash
agentbox install git
```

---

## 📂 项目结构

```
agentbox/
│
├─ pyproject.toml
├─ README.md
│
├─ agentbox/
│  ├─ __init__.py
│  ├─ __main__.py
│  ├─ cli.py
│  ├─ version.py
│  │
│  ├─ commands/
│  │  ├─ doctor.py
│  │  └─ install.py
│  │
│  └─ utils/
│
└─ tests/
   └─ test_cli.py
```

---

## 🧪 运行测试

项目使用 **pytest** 进行测试。

安装测试依赖：

```bash
uv add --dev pytest
```

运行测试：

```bash
uv run pytest
```

---

## 🛠 开发

克隆项目：

```bash
git clone https://github.com/yourname/agentbox.git
cd agentbox
```

创建开发环境：

```bash
uv sync
```

开发模式安装：

```bash
uv pip install -e .
```

---

## 📌 技术栈

* Python 3.9+
* argparse
* uv
* pytest

---

## 📄 License

MIT License

---

## ⭐ 贡献

欢迎提交 Issue 或 Pull Request 来改进本项目。
