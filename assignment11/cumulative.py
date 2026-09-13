import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
conn = sqlite3.connect('./db/lesson.db')

query = """
SELECT 
    o.order_id, 
    SUM(p.price * l.quantity) AS total_price 
FROM orders o 
JOIN line_items l ON o.order_id = l.order_id 
JOIN products p ON l.product_id = p.product_id 
GROUP BY o.order_id 
ORDER BY o.order_id ASC;
"""

df = pd.read_sql_query(query, conn)
conn.close()

df['cumulative'] = df['total_price'].cumsum()
ax = df.plot(
    kind='line',
    x='order_id',
    y='cumulative',
    color='steelblue',
    linewidth=2,
    figsize=(9, 5),
    legend=False
)

plt.title('Cumulative Revenue Over Time', fontsize=14, fontweight='bold')
plt.xlabel('Order ID', fontsize=12)
plt.ylabel('Cumulative Revenue ($)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()












