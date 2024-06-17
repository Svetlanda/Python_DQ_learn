# HOME TASK 4.3
text = """homEwork:
  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""


lines = text.split('\n')  # Split the lines
additional_sentence_words = []
sentenceFromLastWords = ''
newText = []
result_text = ''


def update_new_sentence(sentence, new_sentence):
    new_sentence += sentence.strip().capitalize()
    new_sentence = new_sentence.replace(' iz ', ' is ')
    return new_sentence


def configure_additional_sentence(sentence):
    last_word = sentence.split(' ')[-1].replace(".", '')
    additional_sentence_words.append(last_word)


def update_new_text(new_line):
    new_line += ". ".join(new_sentences)
    newText.append(new_line)
    return new_line


def update_additional_sentence():
    additional_sentence = " ".join(additional_sentence_words[1:])
    newText[5] = newText[5] + ' ' + additional_sentence.capitalize() + "."


for line in lines:
    sentences = line.split('. ')
    new_line = ''
    new_sentences = []

    for sentence in sentences:
        new_sentence = ''
        if sentence == '':
            new_line = '\n'
            continue

        new_sentence = update_new_sentence(sentence, new_sentence)

        if sentence == sentences[-1]:
            configure_additional_sentence(new_sentence)

        new_sentences.append(new_sentence)

        if line != lines[0]:
            new_line = '\n\xa0 '

    new_line = update_new_text(new_line)

update_additional_sentence()
result_text = ''.join(newText)
spaces_count = result_text.count('\n') + result_text.count(' ')

print(result_text)
print('\n Number of whitespace characters in this text = ', spaces_count)

