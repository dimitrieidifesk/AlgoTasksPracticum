"""
https://contest.yandex.ru/contest/24414/run-report/122742793/

-- ПРИНЦИП РАБОТЫ --
Реализован поисковой индекс на основе хеш-структуры словарь. Для каждого слова из документов подсчитывается количество использований
этого слова в каждом документе. В индексе мы получаем по ключу (слову) индексы всех документов, в которых встречается это слово и
количество его использований в них.
Далее по каждому уникальному слову из запроса мы считаем показатель релевантности, суммируя кол-ва вхождений слов в каждом документе.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Созданный единожды индекс позволяет быстро находить вхождения слов запроса в документах.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Временная сложность = O(K), где K - кол-во уникальных слов в запросе на поиск. Учитывая, что в запросе может быть не более
100 символов, можно сказать, что временная сложность O(1)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Пространственная сложность = O(L), где L - кол-во уникальных слов в документах. Они хранятся в индексе search_index
"""

from typing import List


def create_index(docs: List[str]):
    index = {}
    for i, doc in enumerate(docs):
        doc = doc.split()
        for word in doc:
            if word not in index:
                index[word] = {}
            if i + 1 not in index[word]:
                index[word][i + 1] = 0
            index[word][i + 1] += 1
    return index


def search_query(query: str):
    query_words = set(query.split())
    relevance_dict = {}

    for word in query_words:
        if word in search_index:
            for doc_id, count in search_index[word].items():
                if doc_id in relevance_dict:
                    relevance_dict[doc_id] += count
                else:
                    relevance_dict[doc_id] = count

    sorted_docs = sorted(relevance_dict.items(), key=lambda item: (-item[1], item[0]))
    return ' '.join([str(doc_id) for doc_id, _ in sorted_docs[:5]])


n = int(input())
docs = []
for _ in range(n):
    docs.append(input())

search_index = create_index(docs)
m = int(input())
for _ in range(m):
    print(search_query(input()))
