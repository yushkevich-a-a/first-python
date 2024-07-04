countRightAnswer = 0

def getAnswer(question, rightAnswer):
  global countRightAnswer
  count = 2
  print(question)
  answer = input().lower().strip()
  rightAnswer = rightAnswer.lower().strip()
  while (rightAnswer != answer):
    if count == 0:
      return ("x" * len(rightAnswer))
    print('неверно, попыток:', count)
    answer = input().lower().strip()
    count -= 1
  print('Верно')
  countRightAnswer += 1
  return answer




stage1 = getAnswer("укажите первый этап эволюции человека", "Dryopithecus")
stage2 = getAnswer("укажите второй этап эволюции человека", "Ramapithecus")
stage3 = getAnswer("укажите третий этап эволюции человека", "Australopithecus")
stage4 = getAnswer("укажите четвертый этап эволюции человека", "Homo Erectus")
stage5 = getAnswer("укажите пятый этап эволюции человека", "Homo Sapiens Neanderthalensis")    
stage6 = getAnswer("укажите шастой этап эволюции человека", "Homo Sapiens Sapiens")    


print( stage1, stage2, stage3, stage4, stage5, stage6, sep=' => ')
# результат  при правильном указании периодов: dryopithecus => ramapithecus => australopithecus => homo erectus => homo sapiens neanderthalensis => homo sapiens sapiens

print("правильно указанных периодов:", countRightAnswer, "из 6")
