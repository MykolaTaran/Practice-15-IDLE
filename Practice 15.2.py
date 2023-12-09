import pandas as pd

import matplotlib.pyplot as plt

import matplotlib.dates as mdates

data_comp = pd.read_csv("comptagevelo20152.csv", encoding = "latin1")

plt.figure(figsize = (15, 10))
fig, ax = plt.subplots(figsize=(15, 10))
plt.plot(data_comp["Date"], data_comp["Berri1"], label = "Berri1")
plt.plot(data_comp["Date"], data_comp["Boyer"], label = "Boyer")
plt.plot(data_comp["Date"], data_comp["BrÃ©beuf"], label = "BrÃ©beuf")
plt.plot(data_comp["Date"], data_comp["CSC (CÃ´te Sainte-Catherine)"], label = "CSC (CÃ´te Sainte-Catherine)")
plt.plot(data_comp["Date"], data_comp["Maisonneuve_2"], label = "Maisonneuve_2")
plt.plot(data_comp["Date"], data_comp["Maisonneuve_3"], label = "Maisonneuve_3")
plt.plot(data_comp["Date"], data_comp["Notre-Dame"], label = "Notre-Dame")
plt.plot(data_comp["Date"], data_comp["Parc"], label = "Parc")
plt.plot(data_comp["Date"], data_comp["PierDup"], label = "PierDup")
plt.plot(data_comp["Date"], data_comp["Pont_Jacques_Cartier"], label = "Pont_Jacques_Cartier")
plt.plot(data_comp["Date"], data_comp["Rachel / HÃ´tel de Ville"], label = "Rachel / HÃ´tel de Ville")
plt.plot(data_comp["Date"], data_comp["Rachel / Papineau"], label = "Rachel / Papineau")
plt.plot(data_comp["Date"], data_comp["RenÃ©-LÃ©vesque"], label = "RenÃ©-LÃ©vesque")
plt.plot(data_comp["Date"], data_comp["Saint-Antoine"], label = "Saint-Antoine")
plt.plot(data_comp["Date"], data_comp["Saint-Urbain"], label = "Saint-Urbain")
plt.plot(data_comp["Date"], data_comp["Totem_Laurier"], label = "Totem_Laurier")
plt.plot(data_comp["Date"], data_comp["University"], label = "University")
plt.plot(data_comp["Date"], data_comp["Viger"], label = "Viger")
plt.xlabel("Date")
plt.ylabel("")
xfmt = mdates.DateFormatter("%b")
months = mdates.MonthLocator()
ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(xfmt)
plt.legend()
plt.show()
