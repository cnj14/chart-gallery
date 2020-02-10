# three_charts.py
import matplotlib.pyplot as plt 
import numpy as np 

#
# CHART 1 (PIE)
#

pie_data = [
    {"company": "Company X", "market_share": 0.55},
    {"company": "Company Y", "market_share": 0.30},
    {"company": "Company Z", "market_share": 0.15}
]
comps = []
shares = []

for x in pie_data:
    comps.append(x["company"])
    shares.append(x["market_share"])


print("----------------")
print("GENERATING PIE CHART...")
# print(pie_data)

fig1, ax1 = plt.subplots()
ax1.pie(shares, labels=comps, autopct='%1.1f%%', startangle=90)
ax1.axis("equal")
plt.show()

#
# CHART 2 (LINE)
#

line_data = [
    {"date": "2019-01-01", "stock_price_usd": 100.00},
    {"date": "2019-01-02", "stock_price_usd": 101.01},
    {"date": "2019-01-03", "stock_price_usd": 120.20},
    {"date": "2019-01-04", "stock_price_usd": 107.07},
    {"date": "2019-01-05", "stock_price_usd": 142.42},
    {"date": "2019-01-06", "stock_price_usd": 135.35},
    {"date": "2019-01-07", "stock_price_usd": 160.60},
    {"date": "2019-01-08", "stock_price_usd": 162.62},
]
dates = []
prices = []

print("----------------")
print("GENERATING LINE GRAPH...")
# print(line_data)

for y in line_data:
    dates.append(y["date"])
    prices.append(y["stock_price_usd"])
for p in prices:
    p = "${0:.2f}".format(p)
fig2, ax = plt.subplots()
ax.plot(dates, prices)
fig2.autofmt_xdate()
plt.xlabel("Date")
plt.ylabel("Stock Price")
plt.show()


#
# CHART 3 (HORIZONTAL BAR)
#

print("----------------")
print("GENERATING BAR CHART...")


bar_data = [
    {"genre": "Thriller", "viewers": 123456},
    {"genre": "Mystery", "viewers": 234567},
    {"genre": "Sci-Fi", "viewers": 987654},
    {"genre": "Fantasy", "viewers": 876543},
    {"genre": "Documentary", "viewers": 283105},
    {"genre": "Action", "viewers": 544099},
    {"genre": "Romantic Comedy", "viewers": 121212}
]

genres = []
viewers = []

for z in bar_data:
    genres.append(z["genre"])
    viewers.append(z["viewers"])

y_pos = np.arange(len(genres))
plt.barh(y_pos, viewers, align='center', alpha=0.5)
plt.yticks(y_pos, genres)
plt.xlabel('Viewers')
plt.title('Genre Popularity')
plt.show()

# print(bar_data) 

exit()
