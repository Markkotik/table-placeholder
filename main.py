import pandas as pd

import config

# Создание пустой таблицы
df = pd.DataFrame(index=config.planets, columns=config.columns)


# Итерация по таблице для заполнения примерными данными
for planet in planets:
    for column in columns:
        prompt = create_prompt(planet, column)
        print(prompt)  # Здесь будет ваш API запрос к GPT-4
        # Пример заполнения: df.loc[planet, column] = "Пример трактовки от GPT-4"
