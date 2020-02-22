def count(word, choisedCharacter):
	numberOf = 0
	for character in word:
		if character == choisedCharacter:
			numberOf = numberOf +1
	print('찾고자 하는 문자의 개수는 :' , numberOf)
	

word = input('word 입력:')
chara = input('문자 입력:')
count(word, chara)