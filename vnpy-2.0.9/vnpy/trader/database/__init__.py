import os
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from vnpy.trader.database.database import BaseDatabaseManager
# 原来它调用的是initialize中的init方法，返回的是BaseDatabaseManager对象
# 它的save_tick_data方法是在C:\vnstudio\Lib\site-packages\vnpy\~rader\database\database.py文件中BaseDatabaseManager这个类定义的。
# 然后在上面的import中，将这个类import了进来
if "VNPY_TESTING" not in os.environ:
    from vnpy.trader.setting import get_settings
    from .initialize import init

    settings = get_settings("database.")
    database_manager: "BaseDatabaseManager" = init(settings=settings)
