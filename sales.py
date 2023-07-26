import matplotlib.pyplot as mat

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
monthSales = []

for month in months:
    sales = int(input(f"Please enter the sales for {month}: "))
    monthSales.append(sales)

mat.title("Prices over 10 years")
mat.scatter(months, monthSales, color='darkblue', marker='x', label="item 1")

mat.xlabel("Time (Months)")
mat.ylabel("total sales ($)")

mat.grid(True)
mat.legend()

mat.show()