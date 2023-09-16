# my_dash_app.py

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('https://raw.githubusercontent.com/AhmedJagirdar/ahmedasif/main/iris_data.csv')

# Histogram for sepal_length
fig1 = px.histogram(df, x='sepal_length', title='Distribution of Sepal Length', nbins=30)

# Bar Chart for average petal_width by species
avg_petal_width = df.groupby('species')['petal_width'].mean().reset_index()
fig2 = px.bar(avg_petal_width, x='species', y='petal_width', title='Average Petal Width by Species', color='species')

# Scatter Plot for sepal_length vs sepal_width
fig3 = px.scatter(df, x='sepal_length', y='sepal_width', color='species', title='Sepal Length vs Sepal Width')

# Create Dash app
app = dash.Dash(__name__)
server = app.server  # Expose the server variable for deployments

app.layout = html.Div([
    dcc.Graph(figure=fig1),
    dcc.Graph(figure=fig2),
    dcc.Graph(figure=fig3)
])

if __name__ == '__main__':
    app.run_server(debug=True)