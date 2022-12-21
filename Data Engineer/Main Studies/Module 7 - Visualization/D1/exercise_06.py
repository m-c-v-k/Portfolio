# Imporing necessary libraries
import matplotlib.pyplot as plt

# 6.a
landerMedaljer = {
    "lander": ["SWE", "ITA", "NOR", "FIN", "GER", "CHI",
               "ESP", "ESP", "SWE", "FIN"],
    "medaljer": ["Guld", "Silver", "Brons", "Brons", "Guld", "Silver", "Guld", "Guld"],
}

plt.hist(landerMedaljer['medaljer'], color='#ff0000')
plt.title('Medal histostory')
plt.xlabel('Medal count')
plt.ylabel('Medal type')
plt.show()

# 6.b
plt.hist(landerMedaljer['lander'], color='#ff0000')
plt.show()
