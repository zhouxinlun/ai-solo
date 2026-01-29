#!/usr/bin/env python3
import iterm2
import sys
import asyncio

async def main(connection):
    if len(sys.argv) < 3:
        print("Usage: python notify_role.py <TargetName> <Command>")
        return

    target_name = sys.argv[1]
    command_text = sys.argv[2]

    app = await iterm2.async_get_app(connection)
    
    target_session = None

    # 1. 寻找目标 Session
    for window in app.terminal_windows:
        for tab in window.tabs:
            for session in tab.sessions:
                if target_name.lower() in session.name.lower():
                    target_session = session
                    break
            if target_session: break
        if target_session: break

    # 2. 执行命令（分步发送）
    if target_session:
        # 第一步：只发送命令文本（不带回车）
        clean_command = command_text.rstrip()
        await target_session.async_send_text(clean_command)
        
        # 【关键修复】
        # 暂停 0.05 秒。这给 Shell 一点时间去处理刚才输入的字符，
        # 让它退出“粘贴模式”或“补全模式”。
        await asyncio.sleep(0.05)
        
        # 第二步：单独发送回车键 (Hex 0x0D)
        # 这样 Shell 会认为是你手动按下了 Enter
        await target_session.async_send_text("\r")
        
        print(f"Executed in {target_session.name}: {clean_command}")
    else:
        print(f"Error: Could not find session named '{target_name}'")

iterm2.run_until_complete(main, retry=True)