# Desktop Pet 桌面宠物

一个使用 Python Tkinter 编写的轻量级桌面宠物，无需第三方依赖，适合初学者作为第一个 GitHub 项目。

## 功能

- 透明置顶窗口
- 鼠标拖拽移动
- 点击互动
- 随机说话
- 右键菜单：喂食、玩耍、睡觉/唤醒、隐藏、退出
- 纯 Python，无需安装额外库

## 运行方式

确保电脑已安装 Python 3.9+。

```bash
python desktop_pet.py
```

## 打包成 Windows exe

```bash
pip install pyinstaller
pyinstaller --onefile --windowed desktop_pet.py
```

打包完成后，程序在：

```bash
dist/desktop_pet.exe
```

## 后续可优化方向

- 替换成 PNG/GIF 宠物素材
- 增加随机走动
- 增加番茄钟提醒
- 增加工作陪伴语音
- 增加开机自启动
- 增加托盘菜单
