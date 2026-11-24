meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD": "Una expresion de risa a un cusualmeteutilizado en jovenes",
            "Aura": "Referencia a la precencia de una persona",
            "Batalla de aura": "Competencia de personas el objetivo es saber quien da mas precencia"  
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    print(word, meme_dict [word])
else:
    print("Si tu no sabes, peor yo")
