def getAnswer(question, rightAnswer):
  count = 2
  print(question)
  answer = input().lower().strip()
  rightAnswer = rightAnswer.lower().strip()
  while (rightAnswer != answer):
    if count == 0:
      return ">>>не указан<<<"
    print('неверно, попыток:', count)
    answer = input().lower().strip()
    count -= 1
  print('принято')
  return answer


stage1 = getAnswer("укажите первый этап эволюции человека", "Dryopithecus")
stage2 = getAnswer("укажите второй этап эволюции человека", "Ramapithecus")
stage3 = getAnswer("укажите третий этап эволюции человека", "Australopithecus")
stage4 = getAnswer("укажите четвертый этап эволюции человека", "Homo Erectus")
stage5 = getAnswer("укажите пятый этап эволюции человека", "Homo Sapiens Neanderthalensis")    
stage6 = getAnswer("укажите шастой этап эволюции человека", "Homo Sapiens Sapiens")    

print( stage1, stage2, stage3, stage4, stage5, stage6, sep=' => ')
