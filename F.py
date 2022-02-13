import random

def F(listOfNames,N):
  result = []
  for i in range(N):
    randomIndex = (random.randint(0,len(listOfNames)-1))
    randomName = listOfNames[randomIndex]
    result.append(randomName)
  return result
listOfNames = ['Арина','Павел','Стефания','Анастасия','Захар','Александр','Николай','Тимофей','Марсель','Ясмина','София','Вероника','Иван','Матвей','Елизавета','Полина','Михаил','Александра','Эмилия','Мирон']
randomNames = F(listOfNames,100)
print (randomNames)
print(len(randomNames))