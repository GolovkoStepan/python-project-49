[![Actions Status](https://github.com/GolovkoStepan/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/GolovkoStepan/python-project-49/actions)

## Brain Games

«Игры разума» — набор из пяти консольных игр, построенных по принципу популярных мобильных приложений для прокачки мозга. Каждая игра задает вопросы, на которые нужно дать правильные ответы. После трех правильных ответов считается, что игра пройдена. Неправильные ответы завершают игру и предлагают пройти ее заново.

Игры:
- Калькулятор. Арифметические выражения, которые необходимо вычислить
- Прогрессия. Поиск пропущенных чисел в последовательности чисел
- Определение четного числа
- Определение наибольшего общего делителя
- Определение простого числа

Пример игры:

```bash
brain-progression
Welcome to the Brain Game!
May I have your name? Roman
Hello, Roman!
What number is missing in this progression?
Question: 14 .. 18 20 22 24 26 28
Your answer: 16 # Пользователь вводит ответ
Correct!
Question: 5 6 7 8 9 .. 11 12
Your answer: 10 # Пользователь вводит ответ
Correct!
Question: 12 15 18 21 .. 27 30 33
Your answer: 24 # Пользователь вводит ответ
Correct!
Congratulations, Roman!
```

Варианты запуска:
```bash
brain-games # Приветствие
brain-even # Определение четного числа
brain-calc # Калькулятор
brain-gcd # Определение наибольшего общего делителя
brain-progression # Прогрессия
brain-prime # Определение простого числа
```

Описание команд make:
```bash
make install # Установить зависимости
make build # Собрать пакет
make package-install # Установить пакет локально
make lint # Запуск проверок кода
```
