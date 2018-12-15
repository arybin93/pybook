import sys
import signal
import asyncio
import aiohttp
import json


loop = asyncio.get_event_loop()
client = aiohttp.ClientSession()

async def get_json(client, url):
    async with client.get(url) as resp:
        assert resp.status == 200
        return await resp.read()

def send_email():
    print('HELLO!')

async def get_reddit_top(subreddit, client):
    data_1 = await get_json(client, 'https://www.reddit.com/r/' + subreddit + '/top.json?sort=top&t=day&limit=5')

    j = json.loads(data_1.decode('utf-8'))
    for i in j['data']['children']:
        score = i['data']['score']
        title = i['data']['title']
        link = i['data']['url']
        result = '{score}: {title} + ({link})'.format(score=score, title=title, link=link)
        print(result)

    print('Done', subreddit + '\n')

    send_email()


def signal_handler(signal, frame):  
    loop.stop()
    client.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

loop = asyncio.get_event_loop()

asyncio.ensure_future(get_reddit_top('python', client))
asyncio.ensure_future(get_reddit_top('programming', client))
loop.run_forever()
