import tkinter as tk
import data_dict

data = data_dict.data

# Функция для поиска данных в словаре
def search():
    search_key = entry.get().lower()  # Получаем введенное пользователем слово для поиска
    result.delete(1.0, tk.END)  # Очищаем текстовое поле от предыдущих результатов
    if search_key in data:
        description = data[search_key]  # Находим описание слова
        result.insert(tk.END, str(*description.keys()))
        result.insert(tk.END, *description.values()) # Выводим описание в текстовое поле
    else:
        result.insert(tk.END, 'Слово не найдено в словаре.\nСкорее всего это правильный глагол или слово написано с ошибкой.')  # Выводим сообщение, если слово не найдено

# Создаем графический интерфейс
root = tk.Tk()
root.title("Irregular verbs")

# Создаем и размещаем элементы интерфейса
label = tk.Label(root, text="Введите глагол в базовой форме:")
label.pack()

entry = tk.Entry(root)
entry.pack()

search_button = tk.Button(root, text="Поиск", command=search)
search_button.pack()

result = tk.Text(root, height=5, width=45)
result.pack()

# Запускаем основной цикл программы
root.mainloop()