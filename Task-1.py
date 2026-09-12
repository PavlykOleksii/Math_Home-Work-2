import matplotlib.pyplot as plt
from matplotlib_venn import venn3

rock_fans = {101, 102, 103, 105, 107, 109, 110, 112, 115, 118}
pop_fans = {102, 104, 105, 106, 108, 110, 111, 113, 115, 117}
jazz_fans = {103, 105, 108, 110, 112, 114, 115, 116, 119, 120}

print(f"\nID слухачів які слухали рок: {rock_fans} їх кількість: {len(rock_fans)}\nID слухачів які слухали поп: {pop_fans} їх кількість: {len(pop_fans)}\nID слухачів які слухали джаз: {jazz_fans} їх кількість: {len(jazz_fans)}")

all_fans = rock_fans | pop_fans | jazz_fans

print(f"\nID слухачів які слухали хоча б один із трьох жанрів: {all_fans}\nїх кількість: {len(all_fans)}")

all_genres = rock_fans & pop_fans & jazz_fans
print(f"\nID слухачів які слухали всі жанри: {all_genres}\nїх кількість: {len(all_genres)}")

only_rock_fans = rock_fans - (pop_fans | jazz_fans)
print(f"\nID слухачів які слухали тільки рок: {only_rock_fans}\nїх кількість: {len(only_rock_fans)}")

two_genres = ((rock_fans & pop_fans) - jazz_fans) | ((rock_fans & jazz_fans) - pop_fans) | ((pop_fans & jazz_fans) - rock_fans)
print(f"\nID слухачів які слухали тільки 2 жанри: {two_genres}\nїх кількість: {len(two_genres)}")

venn3(
    subsets=(rock_fans, pop_fans, jazz_fans),
    set_labels=("Рок", "Поп", "Джаз")
)

plt.title("Перетин аудиторій музичних жанрів")
plt.show()