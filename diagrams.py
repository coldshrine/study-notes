import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Данные
categories = [
    "Человеческие чувства и состояния",
    "Качественная характеристика человека",
    "Действия и поступки человека",
    "Качественная характеристика предметов и явлений действительности",
    "Характеристика умственных и интеллектуальных способностей человека",
    "Манера речевого общения",
    "Отношение человека к окружающей среде и другим людям",
    "Манера осуществления зрительного восприятия"
]

fran = [34, 29, 26, 6, 10, 9, 6, 11]
angl = [20, 31, 17, 5, 11, 7, 5, 4]
bel = [37, 23, 34, 21, 11, 7, 9, 2]

# Создание датафрейма
df = pd.DataFrame({
    "Категория": categories,
    "ФРАН": fran,
    "АНГЛ": angl,
    "БЕЛ": bel
})

# Сортировка по убыванию общей суммы
df["Сумма"] = df[["ФРАН", "АНГЛ", "БЕЛ"]].sum(axis=1)
df = df.sort_values("Сумма", ascending=False).drop(columns="Сумма")

# Цвета для каждого языка
palette = {
    "ФРАН": "#c69ff5",
    "АНГЛ": "#b185d8",
    "БЕЛ": "#986fc2"
}

# Настройка графика
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(16, 7), sharey=True)
languages = ["ФРАН", "АНГЛ", "БЕЛ"]

for i, lang in enumerate(languages):
    sns.barplot(
        x=lang,
        y="Категория",
        data=df,
        ax=axes[i],
        color=palette[lang]
    )
    axes[i].set_title(lang, fontsize=14, fontweight='bold')
    axes[i].set_xlabel("Значение", fontsize=10)
    axes[i].bar_label(axes[i].containers[0], fmt='%d', padding=3, fontsize=9)
    
    # Отображаем названия категорий у всех графиков
    axes[i].set_ylabel("Категория", fontsize=10)
    axes[i].tick_params(labelsize=9)

fig.suptitle("Распределение категорий по языкам", fontsize=16, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()