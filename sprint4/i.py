# from collections import defaultdict
#
#
# def find_anagrams(n, strings):
#     anagrams = defaultdict(list)
#
#     for index in range(n):
#         sorted_str = ''.join(sorted(strings[index]))
#         anagrams[sorted_str].append(index)
#
#     result = list(anagrams.values())
#
#     for group in result:
#         group.sort()
#     result.sort(key=lambda x: x[0] if x else float('inf'))
#
#     for group in result:
#         print(' '.join(map(str, group)))
#
#
# n = int(input())
# strings = input().split()
# find_anagrams(n, strings)
from datetime import datetime, timedelta; import requests; case_list_resp = requests.get('https://deztroy.nau.team:8443/api/v2/projects/corebo00000000000p3ukh0ci1032ltk/cases-batch/list?state=adjourned,new&modifiedAfter={}Z'.format((datetime.utcnow() - timedelta(days=1)).isoformat()), headers={'Username': 'dimitriev', 'X-API-Key': 'uMED9nZ.ykSihv3iUigqyvheP2vdmMhO90npuj4P', 'Content-Type': 'application/json'})

print(case_list_resp.json())
