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
# Name: FakeWallet
# Description: Fun joke - fake crypto wallet. You can change cryptocurrency values ​​using .cfg FakeWallet.
# Author: @hikka_mods
# ---------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------
# meta developer: @hikka_mods
# scope: hikka_only
# scope: hikka_min 1.4.2
# -----------------------------------------------------------------------------------

import logging

from .. import loader, utils

logger = logging.getLogger(__name__)

@loader.tds
class FakeWallet(loader.Module):
    """Fun joke - fake crypto wallet. You can change cryptocurrency values ​​using .cfg FakeWallet."""

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "Toncoin",
                0,
                lambda: self.strings("ton"),
                validator=loader.validators.Integer(),
            ),
            loader.ConfigValue(
                "Tether",
                0,
                lambda: self.strings("tether"),
                validator=loader.validators.Integer(),
            ),
            loader.ConfigValue(
                "Bitcoin",
                0,
                lambda: self.strings("btc"),
                validator=loader.validators.Integer(),
            ),
            loader.ConfigValue(
                "Etherium",
                0,
                lambda: self.strings("ether"),
                validator=loader.validators.Integer(),
            ),
            loader.ConfigValue(
                "Binance",
                0,
                lambda: self.strings("binc"),
                validator=loader.validators.Integer(),
            ),
            loader.ConfigValue(
                "Tron",
                0,
                lambda: self.strings("tron"),
                validator=loader.validators.Integer(),
            ),
            loader.ConfigValue(
                "USDT",
                0,
                lambda: self.strings("usdt"),
                validator=loader.validators.Integer(),
            ),
            loader.ConfigValue(
                "Gram",
                0,
                lambda: self.strings("gram"),
                validator=loader.validators.Integer(),
            ),
            loader.ConfigValue(
                "Litecoin",
                0,
                lambda: self.strings("lite"),
                validator=loader.validators.Integer(),
            ),
        )

    strings = {
        "name": "FakeWallet",
        "crypto": "Enter a value for your cryptovalute",
        "wallet": "<emoji document_id=5438626338560810621>👛</emoji> <b>Wallet</b>\n\n"
        "<emoji document_id=5215276644620586569>☺️</emoji> <a href='https://ton.org'>Toncoin</a>: {} TON\n\n"
        "<emoji document_id=5215699136258524363>☺️</emoji> <a href='https://tether.to'>Tether</a>: {} USDT\n\n"
        "<emoji document_id=5215590800003451651>☺️</emoji> <a href='https://bitcoin.org'>Bitcoin</a>: {} BTC\n\n"
        "<emoji document_id=5217867240044512715>☺️</emoji> <a href='https://etherium.org'>Etherium</a>: {} ETH\n\n"
        "<emoji document_id=5215595550237279768>☺️</emoji> <a href='https://binance.org'>Binance coin</a>: {} BNB\n\n"
        "<emoji document_id=5215437796088499410>☺️</emoji> <a href='https://tron.network'>TRON</a>: {} TRX\n\n"
        "<emoji document_id=5215440441788351459>☺️</emoji> <a href='https://www.centre.io/usdc'>USD Coin</a>: {} USDC\n\n"
        "<emoji document_id=5215267041073711005>☺️</emoji> <a href='https://gramcoin.org'>Gram</a>: {} GRAM\n\n"
        "<emoji document_id=5217877586620729050>☺️</emoji> <a href='https://litecoin.org'>Litecoin</a>: {} LTC",
        "ton": "Enter a value for Toncoin",
        "teth": "Enter a value for Tethcoin",
        "btc": "Enter a value for Bitcoin",
        "ether": "Enter a value for Etherium",
        "binc": "Enter a value for Binance coin",
        "tron": "Enter a value for Tron",
        "usdt": "Enter a value for USDT coin",
        "gram": "Enter a value for Gramcoin",
        "lite": "Enter a value for Litecoin",
        "info": "<b><emoji document_id=5305467350064047192>🫥</emoji><i>Attention!</b>\n\n"
        "<i><emoji document_id=5915991028430542030>☝️</emoji>This module is strictly prohibited from being used for the purposes of <b>scam, fraud and advertising</b>.\n\n"
        "<emoji document_id=5787190061644647815>🗣</emoji>The module is provided solely for entertainment purposes, and any violation of the <b>Rules for using the module</b>, if detected, will be subject <b>to appropriate punishment</i>",
    }

    strings_ru = {
        "wallet": "<emoji document_id=5438626338560810621>👛</emoji> <b>Кошелёк</b>\n\n"
        "<emoji document_id=5215276644620586569>☺️</emoji> <a href='https://ton.org'>Toncoin</a>: {} TON\n\n"
        "<emoji document_id=5215699136258524363>☺️</emoji> <a href='https://tether.to'>Tether</a>: {} USDT\n\n"
        "<emoji document_id=5215590800003451651>☺️</emoji> <a href='https://bitcoin.org'>Bitcoin</a>: {} BTC\n\n"
        "<emoji document_id=5217867240044512715>☺️</emoji> <a href='https://etherium.org'>Etherium</a>: {} ETH\n\n"
        "<emoji document_id=5215595550237279768>☺️</emoji> <a href='https://binance.org'>Binance coin</a>: {} BNB\n\n"
        "<emoji document_id=5215437796088499410>☺️</emoji> <a href='https://tron.network'>TRON</a>: {} TRX\n\n"
        "<emoji document_id=5215440441788351459>☺️</emoji> <a href='https://www.centre.io/usdc'>USD Coin</a>: {} USDC\n\n"
        "<emoji document_id=5215267041073711005>☺️</emoji> <a href='https://gramcoin.org'>Gram</a>: {} GRAM\n\n"
        "<emoji document_id=5217877586620729050>☺️</emoji> <a href='https://litecoin.org'>Litecoin</a>: {} LTC",
        "ton": "Введите количество валюты для Toncoin",
        "teth": "Введите количество валюты для Tethcoin",
        "btc": "Введите количество валюты для Bitcoin",
        "ether": "Введите количество валюты для Etherium",
        "binc": "Введите количество валюты для Binance coin",
        "tron": "Введите количество валюты для Tron",
        "usdt": "Введите количество валюты для USDT coin",
        "gram": "Введите количество валюты для Gramcoin",
        "lite": "Введите количество валюты для Litecoin",
        "info": "<b><emoji document_id=5305467350064047192>🫥</emoji><i> Внимание!</b>\n\n"
        "<i><emoji document_id=5915991028430542030>☝️</emoji> Использование этого модуля в целях <b>скама, обмана и рекламы</b> строго запрещено.\n\n"
        "<emoji document_id=5787190061644647815>🗣</emoji> Модуль предоставлен исключительно в развлекательных целях, и любое нарушение <b>Правил использования модуля</b>, если его обнаружат, будет подлежать соответствующему наказанию.</i>",
    }

    @loader.command(
        ru_doc="Чтобы заполучить поддельный кошелек",
        en_doc="To get a fake wallet",
    )
    @loader.command()
    async def fwalletcmd(self, message):
        ton = self.config["Toncoin"]
        teth = self.config["Tether"]
        btc = self.config["Bitcoin"]
        ether = self.config["Etherium"]
        binc = self.config["Binance"]
        tron = self.config["Tron"]
        usdt = self.config["USDT"]
        gram = self.config["Gram"]
        lite = self.config["Litecoin"]

        await utils.answer(
            message,
            self.strings("wallet").format(
                ton, teth, btc, ether, binc, tron, usdt, gram, lite
            ),
        )

    @loader.command(
        ru_doc="Информация о FakeModule",
        en_doc="Info about FakeModule",
    )
    @loader.command()
    async def fwinfocmd(self, message):
        await utils.answer(message, self.strings("info"))
