# Импорт библиотек
import pandas as pd
import bar_chart_race as bcr
import matplotlib.pyplot as plt


# Загрузка данных из CSV-файла
df = pd.read_csv('Arzte.csv', dtype={'Годы': str}).fillna(0) # Заменить пропущенные значения на 0


# Установка столбца 'year' в качестве индекса DataFrame
df = df.set_index('Годы')


# Размеры окна графика (в дюймах)
fig_width, fig_height = 9, 16


# Путь к файлу для сохранения видео
output_file_path = 'arzte_race.mp4'

# Создание фигуры и оси с заданными размерами
fig, ax = plt.subplots(figsize=(fig_width, fig_height))


# Создание bar chart race с определенными параметрами
bcr.bar_chart_race(
    df=df,  
    title='Барлық мамандықтағы дәрігерлер саны                     \nЧисленность врачей всех специальностей                       ',  
    orientation='h',  
    sort='desc',  
    n_bars=15,  
    steps_per_period=40,  
    period_length=2200,  
    filename=output_file_path,  
    figsize=(fig_width, fig_height),  
    cmap='Pastel1',  
    bar_kwargs={'alpha': 1},  
    filter_column_colors=True,
    title_size = 30,
    bar_label_size = 20,
    tick_label_size = 20
)

