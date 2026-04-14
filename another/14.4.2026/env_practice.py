# 💬 Создайте переменную окружения MY_NAME
# $Env:MY_NAME = "Wade Wilson"
#
# 💬 Используйте её с другими программами, например
# echo "Hello $Env:MY_NAME"

import os

name = os.getenv("MY_NAME", "World")
print(f"Hello {name} from Python")