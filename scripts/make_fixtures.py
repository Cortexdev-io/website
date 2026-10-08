"""Builds the synthetic Beta Invest XLSX fixture (fictitious data only)."""
from pathlib import Path
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Statement"
ws.append(["Beta Invest (fictitious) - Portfolio Statement"])
ws.append(["Account: Cliente Demo 001"])
ws.append(["As of: 2026-10-06"])
ws.append([])
ws.append(["Ticker", "Quantity", "Avg Price (BRL)", "Total Cost (BRL)"])
ws.append(["GAMA11", 300, 105.20, 31560.00])
ws.append(["OMEG4", 1500, 9.35, 14025.00])
ws.append(["BETA4", 200, 33.00, 6600.00])
ws.append(["TOTAL", None, None, 52185.00])
out = Path(__file__).resolve().parent.parent / "fixtures" / "beta_invest.xlsx"
wb.save(out)
print("wrote", out)
