# LootGen

## Описание
Консольная утилита для симуляции вероятности выпадения редких предметов (лута) из сундуков. Критически важна для баланса игры.

## Технологии
- **Python 3.12**
- **rich** — красивый вывод таблиц
- **ruff** — линтер
- **Git + GitHub** — контроль версий
- **GitHub Actions** — CI/CD

## Версия
Проект настроен с CI и линтингом

## Развертывание (одной командой после клона)

```bash
git clone https://github.com/Pashtet-byte/lootgen.git
cd lootgen

python -m venv venv
# Linux/Mac:
source venv/bin/activate
# Windows:
# venv\Scripts\activate

pip install -r requirements.txt
python lootgen.py
