#!/bin/bash
echo "Создаем структуру файлов"
sudo python3 main_acl.py

echo "Запуск тестов"
python3 main_acl.py

