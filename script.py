name: Daily Python Script Run

on:
  schedule:
    # 每天美国东部时间22:30执行 (UTC时间：02:30)
    - cron: '30 2 * * *'  # UTC 时间 02:30 等价于美东时间 10:30 PM

  # 手动触发器
  workflow_dispatch:

jobs:
  run-script:
    runs-on: ubuntu-latest

    steps:
      # 检出仓库代码
      - name: Checkout repository
        uses: actions/checkout@v3

      # 设置 Python 环境
      - name: Set up Python
        uses: actions/setup-python@v3
        with:
          python-version: '3.8'

      # 安装依赖（如果有 requirements.txt）
      - name: Install dependencies
        run: |
          pip install -r requirements.txt  # 如果有 requirements.txt 文件

      # 运行 Python 脚本
      - name: Run Python script
        run: |
          python script.py  # 根目录下的 Python 脚本

      # 提交更新后的文件并推送到 GitHub 仓库
      - name: Commit and push changes
        uses: EndBug/add-and-commit@v7
        with:
          message: "Automated update of processed_index and merged_output"
          author_name: "GitHub Actions"
          author_email: "actions@github.com"
          add: 'assets/script/processed_index.txt, merged_output.txt'