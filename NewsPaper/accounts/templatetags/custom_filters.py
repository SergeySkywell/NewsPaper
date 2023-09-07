from django import template

register = template.Library()

bad_words = [
    'Lorem',
    'suscipit',
    'massa',
    'ipsum',
    'efficitur',
    'vehicula'
]

@register.filter()
def censor(sentence):
    sentence_words = sentence.split()
    for i, word in enumerate(sentence_words):
        if word in bad_words:
            sentence_words[i] = word[0] + '***'
    return ' '.join(sentence_words)