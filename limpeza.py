
import re

with open("corpus-original.txt", "r", encoding="utf-8") as f:
    texto_original = f.read()

def limpar_corpus(texto):
    texto = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", texto)
    texto = re.sub(r"https?://\S+", "", texto)
    texto = re.sub(r"\s+", " ", texto)
    return texto.strip()

texto_limpo = limpar_corpus(texto_original)

with open("corpus-limpo.txt", "w", encoding="utf-8") as f:
    f.write(texto_limpo)

print("Corpus limpo e salvo com sucesso em 'corpus-limpo.txt'!")