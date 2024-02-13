from sys import *


def split_into_articles(filename: str):
    with open(filename, 'r') as f:
        paragraphs = [p.strip() for p in f.read().split("\nArticle") if p.strip()]
        articles = [f"Article {i}:{paragraph}" for i, paragraph in enumerate(paragraphs, start = 0)]
        return articles


                
def read_constitution(command: str, searching_text: str):
    if command.lower() != "find":
        raise ValueError("The command doesn't exist!")
    if searching_text is None or searching_text == "":
        raise ValueError("The searching text must be a Value string.")
    searching_text = searching_text.strip().lower().split()
    return command, searching_text
    

# command, searching_text = read_constitution(argv[1], argv[2])
# print(command, searching_text)
      

def search_for_articles(searching_text: list, constitution):
    output = []
    for word in searching_text:
        for article in constitution:
            if word in article.strip().split():
                output.append(article)
    return output


command, searching_text = read_constitution(argv[1], argv[2])
constitution = split_into_articles('constitution.txt')
output = search_for_articles(searching_text, constitution)
print(output)