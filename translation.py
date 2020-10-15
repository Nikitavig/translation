from googletrans import Translator
import re

def preprocess_text(text):
	"""
		Функция для обработки текста
		Args:
			test(str): исходный текс
		Return:
			res(str): обработанный текст
	"""


	text = text.lower().replace("ё", "е")
	text = re.sub('\n\n','', text)
	text = re.sub('\t', '', text)
	res = text.strip()
	return res

def translate(text, dest='en'):
	"""
		Функция для перевода текста с одног оязыка на другой
		Args:
			text(str): текст для перевода
			dest(str): язык целевого назначения
		Return:
			res(str): переведенный текст
	"""


	translator = Translator()
	res = []
	for row in re.split(r"\w\. ", text):
		translation = translator.translate(preprocess_text(row), dest=dest).text
		res.append(translation)	
	res = ". ".join(res)
	return res


def main():
	print(translate("Hi", dest='ru'))
	print(translate("What are you dooing?", dest='ru'))


if __name__ == '__main__':
	main()