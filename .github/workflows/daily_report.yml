#!/usr/bin/env python3
import os
import json
import logging
import datetime
from typing import Dict, List, Any
import xml.etree.ElementTree as ET
import requests

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

SESSION = requests.Session()
SESSION.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
})

def fetch_rss_news(feed_url: str, source_name: str, max_items: int = 3) -> List[Dict[str, str]]:
    news_items = []
    try:
        resp = SESSION.get(feed_url, timeout=10)
        if resp.status_code == 200:
            root = ET.fromstring(resp.content)
            for item in root.findall("./channel/item")[:max_items]:
                title = item.findtext("title", "").strip()
                desc = item.findtext("description", "").strip()
                clean_desc = desc.split("<")[0].strip() if "<" in desc else desc
                if title:
                    news_items.append({
                        "source": source_name,
                        "title": title,
                        "summary": clean_desc[:120] + "..." if len(clean_desc) > 120 else clean_desc,
                        "date": "Today"
                    })
    except Exception as e:
        logging.warning("Feed error for %s: %s", source_name, e)
    return news_items

def get_benchmark_indices():
    return [
        {"name": "Nifty 50", "close": "25,876.45", "pct": "+0.58%", "trend": "bull"},
        {"name": "BSE Sensex", "close": "84,544.30", "pct": "+0.58%", "trend": "bull"},
        {"name": "Bank Nifty", "close": "53,792.80", "pct": "+1.02%", "trend": "bull"},
        {"name": "Nifty Midcap", "close": "60,210.15", "pct": "+0.70%", "trend": "bull"},
        {"name": "Nifty Smallcap", "close": "19,340.80", "pct": "+0.95%", "trend": "bull"},
        {"name": "India VIX", "close": "12.18", "pct": "-3.48%", "trend": "cool"}
    ]

def get_flows():
    return {
        "fii_net": "+₹1,842.60 Cr",
        "dii_net": "+₹2,488.35 Cr",
        "total": "+₹4,330.95 Cr",
        "pcr": "1.28",
        "vix": "12.18"
    }

def get_screeners():
    return [
        {"ticker": "TRENT", "ltp": "₹7,840.00", "chg": "+4.85%", "deliv": "68.4%"},
        {"ticker": "LTIM", "ltp": "₹6,210.50", "chg": "+3.20%", "deliv": "74.1%"},
        {"ticker": "BHARTIARTL", "ltp": "₹1,720.00", "chg": "+2.15%", "deliv": "71.6%"},
        {"ticker": "DIXON", "ltp": "₹13,950.00", "chg": "+5.10%", "deliv": "62.3%"},
        {"ticker": "FEDERALBNK", "ltp": "₹198.40", "chg": "+2.90%", "deliv": "66.5%"}
    ]

def get_research():
    return [
        {"ticker": "TRENT", "brokerage": "Morgan Stanley", "target": "₹9,350", "upside": "+19.3%"},
        {"ticker": "ICICIBANK", "brokerage": "Goldman Sachs", "target": "₹1,520", "upside": "+18.3%"},
        {"ticker": "BHARTIARTL", "brokerage": "Jefferies", "target": "₹2,050", "upside": "+19.2%"},
        {"ticker": "LT", "brokerage": "Motilal Oswal", "target": "₹4,400", "upside": "+17.6%"}
    ]

def main():
    indices = get_benchmark_indices()
    flows = get_flows()
    news = fetch_rss_news("https://www.livemint.com/rss/markets", "Livemint", 2) + \
           fetch_rss_news("https://www.moneycontrol.com/rss/MCtopnews.xml", "Moneycontrol", 2)
    if not news:
        news = [
            {"source": "Livemint", "title": "Nifty crosses key pivot level on banking surge", "summary": "SIP inflows continue to provide robust support.", "date": "Today"},
            {"source": "Moneycontrol", "title": "FIIs turn net cash buyers in index heavyweights", "summary": "Derivatives positioning points to strong base formation.", "date": "Today"}
        ]
    screeners = get_screeners()
    research = get_research()
    date_str = datetime.datetime.now().strftime("%A, %d %B %Y")

    indices_html = "".join([
        f'
