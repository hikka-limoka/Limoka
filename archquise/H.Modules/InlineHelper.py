# Proprietary License Agreement

# Copyright (c) 2024-29 CodWiz

# Permission is hereby granted to any person obtaining a copy of this software and associated documentation files (the "Software"), to use the Software for personal and non-commercial purposes, subject to the following conditions:

# 1. The Software may not be modified, altered, or otherwise changed in any way without the explicit written permission of the author.

# 2. Redistribution of the Software, in original or modified form, is strictly prohibited without the explicit written permission of the author.

# 3. The Software is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and non-infringement. In no event shall the author or copyright holder be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the Software or the use or other dealings in the Software.

# 4. Any use of the Software must include the above copyright notice and this permission notice in all copies or substantial portions of the Software.

# 5. By using the Software, you agree to be bound by the terms and conditions of this license.

# For any inquiries or requests for permissions, please contact codwiz@yandex.ru.

# ---------------------------------------------------------------------------------
# Name: InlineHelper
# Description: Basic management of the UB in case only the inline works
# Author: @hikka_mods
# ---------------------------------------------------------------------------------
# meta developer: @hikka_mods
# scope: InlineHelper
# scope: InlineHelper 0.0.1
# ---------------------------------------------------------------------------------

import asyncio
import logging
import shlex
import sys

from .. import loader, main, utils
from ..inline.types import InlineQuery

logger = logging.getLogger(__name__)


@loader.tds
class InlineHelperMod(loader.Module):
    """Basic management of the UB in case only the inline works"""

    strings = {
        "name": "InlineHelper",
        "call_restart": "<emoji document_id=5188311512791393083>🔄</emoji> Restarting...",
        "call_update": "<emoji document_id=5188311512791393083>🔄</emoji> Updating...",
        "res_prefix": "<emoji document_id=5854762571659218443>✅</emoji> Prefix successfully reset to default",
        "restart_inline_handler_title": "🔄 Restart Userbot",
        "restart_inline_handler_description": "Restart your userbot via inline",
        "restart_inline_handler_message": "🔄 Restart",
        "update_inline_handler_title": "🔄 Update Userbot",
        "update_inline_handler_description": "Update your userbot via inline",
        "update_inline_handler_message": "🔄 Update",
        "terminal_inline_handler_title": "💻 Command Executed",
        "terminal_inline_handler_description": "Command executed successfully",
        "terminal_inline_handler_message": "Command <code>{text}</code> executed successfully in terminal",
        "modules_inline_handler_title": "📦 Modules",
        "modules_inline_handler_description": "List all installed modules",
        "modules_inline_handler_result": "📦 All installed modules:\n\n",
        "resetprefix_inline_handler_title": "⚠️ Reset Prefix",
        "resetprefix_inline_handler_description": "Reset your prefix back to default (be careful!)",
        "resetprefix_inline_handler_message": "Are you sure you want to reset your prefix to default dot?",
        "resetprefix_inline_handler_reply_text_yes": "Yes, reset it",
        "resetprefix_inline_handler_reply_text_no": "No, cancel",
        "error_no_module": "<emoji document_id=5854929766146118183>❌</emoji> Module not found: {module}",
        "error_command_failed": "<emoji document_id=5854929766146118183>❌</emoji> Command execution failed: {error}",
        "error_git_failed": "<emoji document_id=5854929766146118183>❌</emoji> Git operation failed: {error}",
    }

    strings_ru = {
        "call_restart": "<emoji document_id=5188311512791393083>🔄</emoji> Перезагружаю...",
        "call_update": "<emoji document_id=5188311512791393083>🔄</emoji> Обновляю...",
        "res_prefix": "<emoji document_id=5854762571659218443>✅</emoji> Префикс успешно сброшен по умолчанию",
        "restart_inline_handler_title": "<emoji document_id=5188311512791393083>🔄</emoji> Перезагрузить юзербота",
        "restart_inline_handler_description": "Перезагрузить юзербота через инлайн",
        "restart_inline_handler_message": "<emoji document_id=5188311512791393083>🔄</emoji> Перезагрузка",
        "update_inline_handler_title": "<emoji document_id=5188311512791393083>🔄</emoji> Обновить юзербота",
        "update_inline_handler_description": "Обновить юзербота через инлайн",
        "update_inline_handler_message": "<emoji document_id=5188311512791393083>🔄</emoji> Обновить",
        "terminal_inline_handler_title": "<emoji document_id=5854762571659218443>💻</emoji> Команда выполнена!",
        "terminal_inline_handler_description": "Команда успешно выполнена.",
        "terminal_inline_handler_message": "Команда <code>{text}</code> была успешно выполнена в терминале",
        "modules_inline_handler_title": "<emoji document_id=5854762571659218443>📦</emoji> Модули",
        "modules_inline_handler_description": "Вывести список установленных модулей",
        "modules_inline_handler_result": "<emoji document_id=5854762571659218443>📦</emoji> Все установленные модули:\n\n",
        "resetprefix_inline_handler_title": "<emoji document_id=5854929766146118183>⚠️</emoji> Сбросить префикс",
        "resetprefix_inline_handler_description": "Сбросить префикс по умолчанию (осторожно!)",
        "resetprefix_inline_handler_message": "Вы действительно хотите сбросить ваш префикс и установить стандартную точку?",
        "resetprefix_inline_handler_reply_text_yes": "Да, сбросить",
        "resetprefix_inline_handler_reply_text_no": "Нет, отменить",
        "error_no_module": "<emoji document_id=5854929766146118183>❌</emoji> Модуль не найден: {module}",
        "error_command_failed": "<emoji document_id=5854929766146118183>❌</emoji> Ошибка выполнения команды: {error}",
        "error_git_failed": "<emoji document_id=5854929766146118183>❌</emoji> Ошибка git операции: {error}",
    }

    def __init__(self):
        self.client = None
        self.db = None
        self._base_dir = utils.get_base_dir()

    async def client_ready(self, client, db):
        self.client = client
        self.db = db

    async def restart(self, call):
        """Restart callback"""
        logger.info("InlineHelper: Restarting userbot...")
        try:
            await call.edit(self.strings["call_restart"])

            await asyncio.create_subprocess_exec(
                [
                    sys.executable,
                    "-c",
                    f"cd {self._base_dir} && git reset --hard HEAD && git pull",
                ],
                cwd=self._base_dir,
            )
            await call.edit(self.strings["call_update"])
            await asyncio.sleep(2)
            await asyncio.create_subprocess_exec(
                [sys.executable, "-c", f"cd {self._base_dir} && git pull"],
                cwd=self._base_dir,
            )
            await call.edit(self.strings["res_prefix"])
        except Exception as e:
            logger.error(f"Restart failed: {e}")
            await call.edit(self.strings["error_git_failed"].format(error=str(e)))

    async def update(self, call):
        """Update callback"""
        logger.info("InlineHelper: Updating userbot...")
        try:
            await call.edit(self.strings["call_update"])

            await asyncio.create_subprocess_exec(
                [
                    sys.executable,
                    "-c",
                    f"cd {self._base_dir} && git reset --hard HEAD && git pull",
                ],
                cwd=self._base_dir,
            )
            await call.edit(self.strings["res_prefix"])
        except Exception as e:
            logger.error(f"Update failed: {e}")
            await call.edit(self.strings["error_git_failed"].format(error=str(e)))

    async def reset_prefix(self, call):
        """Reset prefix callback"""
        try:
            self.db.set(main.__name__, "command_prefix", ".")
            await call.edit(self.strings["res_prefix"])
        except Exception as e:
            logger.error(f"Reset prefix failed: {e}")
            await call.edit(self.strings["error_command_failed"].format(error=str(e)))

    @loader.inline_handler(
        ru_doc="Перезагрузить юзербота",
        en_doc="Reboot the userbot",
    )
    async def restart_inline_handler(self, _: InlineQuery):
        return {
            "title": self.strings("restart_inline_handler_title"),
            "description": self.strings("restart_inline_handler_description"),
            "message": self.strings("restart_inline_handler_message"),
            "reply_markup": [
                {
                    "text": self.strings("restart_inline_handler_reply_text"),
                    "callback": self.restart,
                }
            ],
        }

    @loader.inline_handler(
        ru_doc="Обновить юзербота",
        en_doc="Update the userbot",
    )
    async def update_inline_handler(self, _: InlineQuery):
        return {
            "title": self.strings("update_inline_handler_title"),
            "description": self.strings("update_inline_handler_description"),
            "message": self.strings("update_inline_handler_message"),
            "reply_markup": [
                {
                    "text": self.strings("update_inline_handler_reply_text"),
                    "callback": self.update,
                }
            ],
        }

    @loader.inline_handler(
        ru_doc="Выполнить команду в терминале (лучше сразу подготовить команду и просто вставить)",
        en_doc="Execute the command in the terminal (it is better to prepare the command immediately and just paste it)",
    )
    async def terminal_inline_handler(self, query: InlineQuery):
        """Execute terminal command safely"""
        if not query.args:
            return {
                "title": self.strings["terminal_inline_handler_title"],
                "description": self.strings["terminal_inline_handler_description"],
                "message": self.strings["terminal_inline_handler_message"].format(
                    text="No command provided"
                ),
            }

        command_text = query.args.strip()
        if not command_text:
            return {
                "title": self.strings["terminal_inline_handler_title"],
                "description": self.strings["terminal_inline_handler_description"],
                "message": self.strings["terminal_inline_handler_message"].format(
                    text="No command provided"
                ),
            }

        if any(char in command_text for char in ["&", "|", ";", "`", "$"]):
            return {
                "title": self.strings["terminal_inline_handler_title"],
                "description": self.strings["terminal_inline_handler_description"],
                "message": self.strings["error_command_failed"].format(
                    error="Invalid characters in command"
                ),
            }

        try:
            args = shlex.split(command_text)
            process = await asyncio.create_subprocess_exec(
                args,
                stdin=asyncio.subprocess.PIPE,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                cwd=self._base_dir,
                text=True,
            )

            stdout, stderr = await process.communicate()
            stdout.decode().strip() if stdout else ""
            error = stderr.decode().strip() if stderr else ""

            if error:
                return {
                    "title": self.strings["terminal_inline_handler_title"],
                    "description": self.strings["terminal_inline_handler_description"],
                    "message": self.strings["error_command_failed"].format(error=error),
                }

            return {
                "title": self.strings["terminal_inline_handler_title"],
                "description": self.strings["terminal_inline_handler_description"],
                "message": self.strings["terminal_inline_handler_message"].format(
                    text=command_text
                ),
            }
        except Exception as e:
            return {
                "title": self.strings["terminal_inline_handler_title"],
                "description": self.strings["terminal_inline_handler_description"],
                "message": self.strings["error_command_failed"].format(error=str(e)),
            }

    @loader.inline_handler(
        ru_doc="Вывести список установленных модулей через инлайн",
        en_doc="Display a list of installed modules via the inline",
    )
    async def modules_inline_handler(self, query: InlineQuery):
        """List all installed modules"""
        try:
            result = self.strings["modules_inline_handler_result"]

            for mod in self.allmodules.modules:
                try:
                    name = mod.strings["name"]
                except KeyError:
                    name = mod.__class__.__name__
                result += f"• {name}\n"

        except Exception as e:
            logger.error(f"Error listing modules: {e}")
            result = f"Error listing modules: {str(e)}"

        return {
            "title": self.strings["modules_inline_handler_title"],
            "description": self.strings["modules_inline_handler_description"],
            "message": result,
        }

    @loader.inline_handler(
        ru_doc="Сбросить префикс (осторожнее, сбрасывает ваш префикс на . )",
        en_doc="Reset the prefix (be careful, resets your prefix to . )",
    )
    async def resetprefix_inline_handler(self, _: InlineQuery):
        return {
            "title": self.strings("resetprefix_inline_handler_title"),
            "description": self.strings("resetprefix_inline_handler_description"),
            "message": self.strings("resetprefix_inline_handler_message"),
            "reply_markup": [
                {
                    "text": self.strings("resetprefix_inline_handler_reply_text_yes"),
                    "callback": self.reset_prefix,
                },
                {
                    "text": self.strings("resetprefix_inline_handler_reply_text_no"),
                    "action": "close",
                },
            ],
        }
