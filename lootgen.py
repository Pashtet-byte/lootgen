import random
from rich.console import Console
from rich.table import Table

def simulate_loot(num_chests: int = 10, rare_chance: float = 0.05) -> None:
    console = Console()
    table = Table(title="LootGen: Симуляция лута")
    table.add_column("Сундук #", justify="right")
    table.add_column("Предмет")
    table.add_column("Редкость")

    for i in range(1, num_chests + 1):
        if random.random() < rare_chance:
            item = "Редкий самоцвет"
            rarity = "Редкий"
        else:
            item = random.choice(["Меч", "Щит", "Зелье"])
            rarity = "Обычный"
        table.add_row(str(i), item, rarity)

    console.print(table)

if __name__ == "__main__":
    simulate_loot(5)