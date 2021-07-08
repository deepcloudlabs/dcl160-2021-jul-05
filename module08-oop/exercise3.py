import asyncio
import json

import websockets

# 'price': '32508.27000000', 'quantity': '0.02127200', 'bid': 6773072785, 'ask': 6773072724
volumes = {}


async def consumer_handler(frames):
    async for frame in frames:
        trade = json.loads(frame)
        price = float(trade["p"])
        quantity = float(trade["q"])
        volume = price * quantity
        bid = trade["b"]
        ask = trade["a"]
        if bid not in volumes:
            volumes[bid] = {"id": bid, "sell": 0.0, "buy": 0.0, "count": 0}
        if ask not in volumes:
            volumes[ask] = {"id": bid, "sell": 0.0, "buy": 0.0, "count": 0}
        volumes[bid]["buy"] += volume
        volumes[bid]["count"] += 1
        volumes[ask]["sell"] += volume
        volumes[ask]["count"] += 1
        if len(volumes.values()) % 50 == 0:
            sorted_volumes = sorted(volumes.values(), key=lambda volume: volume["sell"] + volume["buy"], reverse=True)
            with open("volumes.json", mode='w') as json_file:
                json.dump(sorted_volumes, json_file)
            print("volumes are written to the file.")


async def connect():
    async with websockets.connect("wss://stream.binance.com:9443/ws/btcusdt@trade") as ws:
        await consumer_handler(ws)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(connect())
    loop.run_forever()
