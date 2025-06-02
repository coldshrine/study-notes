import matplotlib.pyplot as plt
import seaborn as sns
import textwrap

plt.rcParams['font.family'] = 'Arial'
sns.set_style("whitegrid", {'grid.linestyle': ':', 'grid.alpha': 0.4})
cool_palette = sns.color_palette("cool_r")

data = {
    "Человеческие чувства и состояния": 91,
    "Качественная характеристика человека": 83,
    "Действия и поступки человека": 77,
    "Качественная характеристика предметов и явлений действительности": 33,
    "Характеристика умственных и интеллектуальных способностей человека": 32,
    "Манера речевого общения": 22,
    "Отношение человека к окружающей среде и другим людям": 20,
    "Манера осуществления зрительного восприятия": 17,
    "Отношения власти, зависимости, подчинения": 15,
    "Указание на мастерство, умение": 13,
    "Черты характера человека": 12
}

max_line_length = 28
sorted_data = sorted(data.items(), key=lambda x: -x[1])
categories = [textwrap.fill(name, max_line_length) for name, _ in sorted_data]
values = [value for _, value in sorted_data]

fig, ax = plt.subplots(figsize=(10, 7))
fig.patch.set_facecolor('white')

bars = ax.barh(
    categories,
    values,
    color=cool_palette,
    height=0.6,
    edgecolor='white',
    linewidth=0.7
)

ax.set_xticks([])
ax.invert_yaxis()

plt.yticks(
    ticks=range(len(categories)),
    labels=categories,
    ha='left',
    position=(-0.05, 0),
    fontsize=11,
    linespacing=1.4
)

for i, (bar, value) in enumerate(zip(bars, values)):
    ax.text(
        bar.get_width() + 1,
        i,
        str(value),
        va='center',
        ha='left',
        fontsize=10,
        fontweight='bold',
        color='#333333'
    )

plt.margins(y=0.03)
ax.set_xlim(right=max(values)*1.15)
plt.subplots_adjust(left=0.35, right=0.85)

ax.xaxis.grid(True, linestyle=':', alpha=0.3)
ax.yaxis.grid(False)
sns.despine(left=True, bottom=True, right=True, top=True)

plt.title('Распределение категорий качественных наречий', 
          pad=20, fontsize=14, fontweight='bold', loc='left')

plt.tight_layout()
plt.show()