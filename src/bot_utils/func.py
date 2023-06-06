import aiohttp
from data.config import TONCENTER_KEY

async def get_info_by_contract(contract):
    result = []

    payload = {
    "method": "runGetMethod",
    "params": {"address": contract,
    "method": "get_balances",
    "stack": []},
    "id": "1",
    "jsonrpc": "2.0",
    }


    async with aiohttp.ClientSession() as session:
        r = await session.post(url="https://toncenter.com/api/v2/jsonRPC",
                        json=payload,
                        headers={"X-API-Key": TONCENTER_KEY})
        
        request_json = await r.json()


    for i in request_json["result"]["stack"]:
        print(i)
        if i[1] != '0x0':
            result.append(float(int(i[1], 16)) / 1e9)

    return result

async def get_lp_holders_by_contract(contract, limit=20):
    holders = None
    result = {}

    async with aiohttp.ClientSession() as session:
        r = await session.get(url=f"https://tonobserver.com/api/v2/get_by_owner/jetton_master/{contract}")
        tmp = await r.json()
        for i in tmp["result"]:
            if i["info"]["jettonMaster"]["jettonContent"]["onchain"]["known"]["symbol"] == "LP":
                r = await session.get(url=f"https://tonobserver.com/api/v2/jetton_top_holders/{i['address']}",
                                      params={"limit": limit + 1})
                
                holders = await r.json()

    if holders != None:
        for i in holders["result"][1:]:
            if int(i["info"]["jettonWallet"]["balance"]) > 0:
                result[i["info"]["jettonWallet"]["ownerAddress"]] = int(i["info"]["jettonWallet"]["balance"]) / 1e9
        return result