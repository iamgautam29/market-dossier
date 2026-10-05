#!/usr/bin/env python3
import datetime

def generate_html():
    now_str = datetime.datetime.now().strftime("%A, %d %B %Y")
    
    html = f"""


  
  
  Daily Indian Market Dossier
    Daily Indian Market Dossier{now_str} • 7:00 PM Daily BriefingPrint / PDFNifty 5025,876.45+0.58%BSE Sensex84,544.30+0.58%Bank Nifty53,792.80+1.02%Nifty Midcap60,210.15+0.70%Nifty Smallcap19,340.80+0.95%India VIX12.18-3.48%FII Net Cash+₹1,842.60 CrBuys: ₹14,290 Cr | Sales: ₹12,448 CrDII Net Cash+₹2,488.35 CrBuys: ₹11,632 Cr | Sales: ₹9,144 CrTotal Institutional Absorption+₹4,330.95 CrFII Longs: 64.8% | PCR: 1.28Livemint & Moneycontrol IntelligenceLivemint • TodayNifty crosses key pivot level on strong banking accumulationSustained mutual fund inflows cushion against foreign rate volatility.Moneycontrol • TodayFIIs turn net cash buyers in index heavyweightsDerivatives open interest clustering points to a strong base at 25,800.High Delivery Volume ShockersStockLTPChgDeliveryTRENT₹7,840.00+4.85%68.4%LTIM₹6,210.50+3.20%74.1%BHARTIARTL₹1,720.00+2.15%71.6%DIXON₹13,950.00+5.10%62.3%Institutional Research UpgradesTRENTMorgan Stanley • Target: ₹9,350+19.3%ICICIBANKGoldman Sachs • Target: ₹1,520+18.3%BHARTIARTLJefferies • Target: ₹2,050+19.2%"""with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
with open("daily_market_dossier.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Report generated successfully.")
if name == "main":generate_html()
