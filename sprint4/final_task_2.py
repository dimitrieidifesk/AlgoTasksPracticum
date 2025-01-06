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

Построение индекса:
O(K * 2L)
K - кол-во документов
L - кол-во слов в документе. 2L т.к. мы делим документ на слова O(L), затем проходимся по каждому слову в документе.
Обработка запросов:
O(Q * 2W * S * N * logN)
Q - кол-во запросов
W - кол-во слов в данном запросе. 2W, т.к. мы делим запрос на уникальные слова, затем проходимся по этому списку слов.
S - кол-во документов с данным словом в индексе
N - кол-во документов, удовлетворяющих поисковому запросу
Общая временная сложность программы:
O(K * 2L) + O(Q * 2W * S * N * logN)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Пространственная сложность = O(L), где L - кол-во уникальных слов в документах. Они хранятся в индексе search_index

Построение индекса:
В худшем случае в индексе нам придется сохранить O(K * L) ключ-значений (id документа, кол-во вхождений слова)
K - кол-во документов
L - кол-во уникальных слов в 1 документе

Обработка запросов:
O(W * N)
W - кол-во слов в запросе (query_words)
N - кол-во документов, удовлетворяющих поисковому запросу (relevance_dict)
Общая пространственная сложность программы:
O(K * L) + O(W * N)

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
