def getAnswer(question, rightAnswer):
  count = 2
  print(question)
  answer = input().lower().strip()
  while (rightAnswer != answer):
    if count == 0:
      return "???????????"
    print('неверно, попыток:', count)
    answer = input().lower().strip()
    count -= 1
  print('принято')
  return answer


msg = getAnswer("первый этап", 'кроманьонец')

print(msg)

# msg = 2

# def getAnswer(a):
#   print(msg)
# getAnswer(msg)