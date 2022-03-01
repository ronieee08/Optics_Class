"""
Simple script to download raw WorldView data over RailRoad Valley
"""

from pystac_client import Client
from cirruslib.transfer import download_item_assets


headers = {"x-api-key": "22OKUqSLMF1aAmDgXqO553otqDmaewNs9xE1brgq"}
wv_nitf_url = 'https://api.smart-stac.com/'
wv_nitf_collection = ['worldview-nitf']

rr_valley_bbox = [
    -115.806884765625,
    38.28131307922966,
    -115.66680908203125,
    38.363195134453846
  ]

wv_catalog = Client.open(wv_nitf_url, headers=headers)

wv_search = wv_catalog.search(collections=wv_nitf_collection,
                           bbox=rr_valley_bbox, max_items=100000)

print('Number of items found {}'.format(wv_search.matched()))

wv_items = list(wv_search.get_items())

download_path = r'path/to/download'

for wv_item in wv_items:
    print(f'Downloading {wv_item.id}')
    download_item_assets(wv_item.to_dict(), path=download_path)





ajkbvgiuegqiohfoiwegdfiugqweidugfhlokqwebndolfboihwerd