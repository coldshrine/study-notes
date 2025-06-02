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

# Считаем сумму по каждой категории
df["Сумма"] = df[["ФРАН", "АНГЛ", "БЕЛ"]].sum(axis=1)

# Создаем колонку с названием категории и суммой
df["Категория с суммой"] = df.apply(
    lambda row: f"{row['Категория']} ({row['Сумма']})", axis=1
)

# Сортируем по убыванию суммы
df = df.sort_values("Сумма", ascending=False)

palette = {
    "ФРАН": "#c69ff5",
    "АНГЛ": "#b185d8",
    "БЕЛ": "#986fc2"
}

fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(18, 8), sharey=True)
languages = ["ФРАН", "АНГЛ", "БЕЛ"]

for i, lang in enumerate(languages):
    sns.barplot(
        x=lang,
        y="Категория с суммой",
        data=df,
        ax=axes[i],
        color=palette[lang]
    )
    axes[i].set_title(lang, fontsize=14, fontweight='bold')
    axes[i].set_xlabel("Значение", fontsize=10)
    axes[i].bar_label(axes[i].containers[0], fmt='%d', padding=3, fontsize=9)

    # Убираем рамки
    for spine in axes[i].spines.values():
        spine.set_visible(False)

# Показываем категории только на первом графике:
axes[0].set_ylabel("Категории", fontsize=10)
axes[0].tick_params(labelsize=9)

# Скрываем метки оси Y у правых графиков, чтобы не дублировать
for ax in axes[1:]:
    ax.tick_params(left=False, labelleft=False)

plt.tight_layout(rect=[0, 0, 1, 0.95])
fig.suptitle("Распределение категорий по языкам", fontsize=16, fontweight='bold')
plt.show()