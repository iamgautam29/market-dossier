#!/usr/bin/env python3
import datetime

def main():
    date_str = datetime.datetime.now().strftime("%d %b %Y")
    
    html_lines = [
        '',
        '
    ', '', ' ', ' ', f' ', ' ', '', '', '
', '
', '
', '
    Daily Indian Market Dossier
', f'
{date_str} • 7:00 PM Daily Briefing

', '
', ' ', '
', '
', '
Nifty 50
25,876.45
+0.58%
', '
BSE Sensex
84,544.30
+0.58%
', '
Bank Nifty
53,792.80
+1.02%
', '
Nifty Midcap
60,210.15
+0.70%
', '
Nifty Smallcap
19,340.80
+0.95%
', '
India VIX
12.18
-3.48%
', '
', '
', '
FII Net Cash
+₹1,842.60 Cr
Buys: ₹14,290 Cr | Sales: ₹12,448 Cr
', '
DII Net Cash
+₹2,488.35 Cr
Buys: ₹11,632 Cr | Sales: ₹9,144 Cr
', '
Total Absorption
+₹4,330.95 Cr
FII Longs: 64.8% | PCR: 1.28
', '
', '
', '
High Delivery Shockers
', '
TRENT (+4.85%, 68.4% Deliv) | LTIM (+3.20%, 74.1% Deliv) | BHARTIARTL (+2.15%, 71.6% Deliv) | DIXON (+5.10%, 62.3% Deliv)

', '
', '
', '', '
    '
]

content = "\n".join(html_lines)
with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
with open("daily_market_dossier.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Report generated successfully.")
if name == "main":
main()
