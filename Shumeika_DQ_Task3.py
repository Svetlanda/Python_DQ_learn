# HOME TASK 3
text = """homEwork:
  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

lines = text.split('\n')  # Split the lines
additionalSentenceWords = []
sentenceFromLastWords = ''
newText = []
resultText = ''

for line in lines:
    sentences = line.split('. ')
    newLine = ''
    newSentences = []

    for sentence in sentences:
        newSentence = ''
        if sentence == '':
            newLine = '\n'
            continue

        newSentence += sentence.strip().capitalize()
        newSentence = newSentence.replace(' iz ', ' is ')

        if sentence == sentences[-1]:
            lastWord = newSentence.split(' ')[-1].replace(".", '')
            additionalSentenceWords.append(lastWord)

        newSentences.append(newSentence)

        if line != lines[0]:
            newLine = '\n\xa0 '

    newLine += ". ".join(newSentences)
    newText.append(newLine)

additionalSentence = " ".join(additionalSentenceWords[1:])
newText[5] = newText[5] + ' ' + additionalSentence.capitalize() + "."

resultText = ''.join(newText)
spacesCount = resultText.count('\n') + resultText.count(' ')

#  to compare with initial text, comment 50 line  where additional Sentence added
#  spacesCountInitial = text.count('\n') + text.count(' ')

print(resultText)
print('\n Number of whitespace characters in this text = ', spacesCount)