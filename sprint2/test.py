import aiohttp
import asyncio


async def send_post(session, url, i):
    print(i)
    async with session.post(url, data={
        "account[subdomain]": ["dimitrievdenis"],
        "account[id]": ["31493710"],
        "account[_links][self]": ["https://dimitrievdenis.amocrm.ru"],
        "leads[update][0][id]": ["1761579"],
        "leads[update][0][status_id]": ["69420482"],
        "leads[update][0][price]": ["0"],
        "leads[update][0][responsible_user_id]": ["9138526"],
        "leads[update][0][last_modified]": ["1705059667"],
        "leads[update][0][modified_user_id]": ["9138526"],
        "leads[update][0][created_user_id]": ["9138526"],
        "leads[update][0][date_create]": ["1704912474"],
        "leads[update][0][pipeline_id]": ["8548254"],
        "leads[update][0][tags][0][id]": ["6172"],
        "leads[update][0][tags][0][name]": ["взято"],
        "leads[update][0][tags][1][id]": ["6170"],
        "leads[update][0][tags][1][name]": ["передано"],
        "leads[update][0][account_id]": ["31493710"],
        "leads[update][0][custom_fields][0][id]": ["251032"],
        "leads[update][0][custom_fields][0][name]": ["ID мастера"],
        "leads[update][0][custom_fields][0][values][0][value]": ["1"],
        "leads[update][0][created_at]": ["1704912474"],
        "leads[update][0][updated_at]": ["1705059667"]
    }) as response:
        # Здесь вы можете обработать ответ, если это необходимо (например, распечатать статус)
        return await response.text()


async def main():
    url = "http://95.142.42.93:8001/api/v1/amo/update/"
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(50):
            tasks.append(send_post(session, url, _))
        # Запуск всех задач одновременно
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())

# f = {
#     "jsonrpc": "2.0",
#     "id": 1233123,
#     "method": "get.employees",
#     "params": {
#         "access_token": "80txvo4um49nkh9dji7rgz2beouuba8lgjer0hhn"
#     },
#     "filter": {
#         "field": "id",
#         "operator": "=",
#         "value": 8517943
#     }
# }
#
# print(str(len(f)))
