from datetime import datetime
import pytz
import requests
from xml.etree import ElementTree as ET


def get_info(xml_link):
    namespaces = {"media": "http://search.yahoo.com/mrss/"}
    response = requests.get(xml_link)
    root = ET.fromstring(response.content)
    channel = root.find("channel")
    return channel, namespaces


def item_parser(xml_link):
    channel, namespaces = get_info(xml_link)
    count = 0
    for item in channel.iter("item"):
        if count >= 20:
            break
        title = get_text_or_none(item, "title")
        link = get_text_or_none(item, "link")
        published_date = get_text_or_none(item, "pubDate")
        source = get_url_or_none(item, "source", lookup="url")

        item_info = {
            "title": title,
            "link": link,
            "published_date": published_date,
            "source": source,
        }

        yield item_info
        count += 1


def get_text_or_none(parent, arg, namespaces=None):
    result = parent.find(arg, namespaces)
    if result is not None:
        result = result.text
    return result


def get_url_or_none(parent, arg, lookup=None, namespaces=None):
    result = parent.find(arg, namespaces)
    if result is not None:
        result = result.attrib.get(lookup) or result.text
    return result


if __name__ == "__main__":
    xml_link = "https://news.yahoo.com/rss/"
    # xml_link = "https://www.varzesh3.com/rss/all"
    data = item_parser(xml_link)
    for item in data:
        print(item)
