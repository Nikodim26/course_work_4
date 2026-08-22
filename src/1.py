# Запись в файл
with open(self.path, "w", encoding="utf-8") as f:
    json.dump(aeroplanes_list, f, indent=4, ensure_ascii=False)

logger.info(f'Создана запись данных самолетов в заданном "квадрате" в файл')