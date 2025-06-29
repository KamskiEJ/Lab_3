# Lab 3

Цей проєкт є лабораторною роботою з об'єктно-орієнтованого програмування. Реалізована система дозволяє керувати студентами, викладачами, курсами та оцінками в рамках університету.

## Функціональність

- Додавання студентів, викладачів та курсів
- Реєстрація студентів на курси
- Призначення оцінок студентам
- Розрахунок середнього балу студента або курсу
- Пошук студентів, викладачів та курсів
- Збереження / завантаження даних з файлу (формат `.pkl`)

## Основні класи

- `Person` – базовий клас
- `Student` – студент (наслідує `Person`)
- `Teacher` – викладач (наслідує `Person`)
- `Course` – курс з описом, ідентифікатором та викладачем
- `University` – клас, що зберігає всі об'єкти та керує ними
- `Grade` – оцінка студента за курс
- `Gradebook` – журнал оцінок та аналітика

## Збереження даних

Для серіалізації використовується модуль `pickle`. Створюється файл `university_data.pkl`, який містить стан системи (студенти, курси, оцінки тощо).
