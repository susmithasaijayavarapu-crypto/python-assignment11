import plotly.express as px
import plotly.data as pldata
import webbrowser

df = pldata.wind(return_type='pandas')

df['strength'] = (
    df['strength']
    .str.replace(r'^.*-', '', regex=True)  
    .str.replace(r'[^0-9.]', '', regex=True) 
    .astype(float)
)

print("--- First 10 Rows ---")
print(df.head(10))
print("\n--- Last 10 Rows ---")
print(df.tail(10))



fig = px.scatter(
    df,
    x='strength',
    y='frequency',
    color='direction',
    title='Wind Strength vs. Frequency by Direction',
    labels={'strength': 'Wind Strength', 'frequency': 'Frequency (%)'},
    template='plotly_white'
)


html_filename = 'wind.html'
fig.write_html(html_filename)
print(f"\nPlot saved successfully to {html_filename}")


webbrowser.open(html_filename)