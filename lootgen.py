import subprocess
import sys

# Проверка и установка rich при запуске
try:
    from rich.console import Console
    from rich.table import Table
except ImportError:
    print("Библиотека 'rich' не найдена. Устанавливаем...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "rich"])
    from rich.console import Console
    from rich.table import Table

import random


def simulate_loot(num_chests: int = 10, rare_chance: float = 0.05) -> None:
    console = Console()
    table = Table(title="Loot Simulation")

    table.add_column("Chest", justify="center")
    table.add_column("Loot", justify="left")
    table.add_column("Rarity", justify="center")

    for chest_num in range(1, num_chests + 1):
        if random.random() < rare_chance:
            loot = "Epic Sword"
            rarity = "Rare"
        else:
            loot = "Wooden Shield"
            rarity = "Common"
        table.add_row(str(chest_num), loot, rarity)

    console.print(table)


if __name__ == "__main__":
    simulate_loot(5)
