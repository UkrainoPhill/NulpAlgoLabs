lab1 -  Варіант 2
        Напишіть функцію, яка приймає невпорядкований масив цілих чисел і повертає діапазон індексів (початковий і кінцевий) найменшого підмасиву, який потрібно відсортувати для досягнення повного впорядкування всього       масиву.

        Наприклад, для вхідного масиву 1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19

        Результат: (3, 9)

        Підмасив, який потрібно відсортувати для впорядкування всього масиву, починається з індексу 3 (значення 7) і закінчується на індексі 9 (значення 7). У випадку, якщо вхідний масив відсортований, слд повернути кортеж      (-1, -1)

        Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку unittest та перевірити сценарії коли: вхідний масив посортований, вхідний масив необхідно сортувати весь, масив містить лише 1       елемент.