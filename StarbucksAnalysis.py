import streamlit as st
import plotly.express as px
import pandas as pd
import pycountry as pc
import pycountry_convert as pcc

st.title("Starbucks Growth Strategy")

# data inputs
drink = pd.read_csv("starbucks_drink.csv")
food = pd.read_csv("starbucks_food.csv")
health = drink.merge(food, left_on='Calories', right_on='Protein (g)', how='left')
data = pd.read_csv('directory.csv')
consdata = pd.read_csv('CoffeeConsumption.csv')

# data clean
data['Brand'].value_counts().sort_values(ascending=False)
data = data.query('Brand == "Starbucks"')
data['Brand'].value_counts()
data.drop(axis=1, columns=['Store Number', 'Postcode', 'Phone Number', 'Timezone'], inplace=True)
data['Country'].value_counts().sort_values(ascending=False)
data['City'].value_counts().sort_values(ascending=False)
data['State/Province'].value_counts().sort_values(ascending=False)
data.query('Country == "US"')['State/Province'].value_counts().sort_values(ascending=False)
data.query('Country == "US"')['State/Province'].value_counts(normalize=True).apply(lambda x: x * 100).sort_values(
    ascending=False)
data['Country_ISO'] = data['Country']
data['Country'] = data['Country'].apply(lambda country: pc.countries.get(alpha_2=country).name)
data['Continent'] = data['Country_ISO'].apply(lambda country: pcc.country_alpha2_to_continent_code(country)).apply(
    lambda cont: pcc.convert_continent_code_to_continent_name(cont))
data['no.store'] = 1

# consdata clean
consdata.rename(columns={"country": "Country", "totCons2019": "Total", "perCapitaCons2016": "PerCapita"}, inplace=True)
x = pd.DataFrame(data['Country'].value_counts().rename('Stores_count'))
x.reset_index(inplace=True)
x.rename(columns={'index': 'Country'}, inplace=True)
consdata = consdata.merge(x, on='Country')


# Charts
st.header('Starbucks locations worldwide')
fig1 = px.scatter_geo(data, lat='Latitude', lon='Longitude', hover_name='Store Name', size_max=10 )
st.write(fig1)

st.header('Starbucks Address and Store Name')
st.write(data)

st.header('No. of stores per country')
st.subheader('Knowing the distritbution of the stores over the world is cool, but what is more interesting is to see the importance of stores in each country')

fig2_data = data['Country'].value_counts().rename('Counts')
fig2 = px.scatter_geo(fig2_data, locationmode='country names', locations=fig2_data.index, color='Counts',
                     hover_data=['Counts'], color_continuous_scale='RdBU')
st.write(fig2)


st.header('No. of stores per state in US')
st.subheader('As we saw in the previous chart, US as a pilot site for Starbucks strategic planning, we want to know how it develop')
fig3_data = data.query('Country_ISO == "US"')['State/Province'].value_counts().rename('Counts')
fig3 = px.scatter_geo(fig3_data, locationmode = 'USA-states' , locations=fig3_data.index , 
                     size='Counts' ,color='Counts' , hover_data=['Counts'] , color_continuous_scale='RdBu' , 
                     scope='usa'  , title = 'each state pointed out by size of total stores')
st.write(fig3)

st.header('No. of stores per continent & country')
st.subheader('We can see US, China and Japan play main role in development of Starbucks strategy')
fig4 = px.sunburst(data, path=['Continent', 'Country'], values='no.store', hover_data=['Country'], title = 'Total starbucks distribution through continent and country over sunburst Chart' )
st.write(fig4)

# st.header('No. of stores per continent')*
# st.subheader('We want to know the distribution of Starbucks in each continent')
# fig4 = px.histogram(data , x='Continent' , color='Country', labels={'count' : 'No. of Stores'},
#                     title='No. of stores per continent & country', color_discrete_sequence=px.colors.qualitative.Pastel,
#                     log_y=True).update_xaxes(categoryorder = 'total descending')
# st.write(fig4)


st.header('Ownership type per country')
st.subheader('It is important to know the ownership distribution in each country')
fig5 = px.histogram(data, x='Country', color='Ownership Type', labels={'count': 'No. of Stores'},
                    title='Ownership type per country', color_discrete_sequence=px.colors.qualitative.Pastel,
                    log_y=True).update_xaxes(categoryorder='total descending')
st.write(fig5)

st.header('No. of stores per city')
st.subheader('This chart is a small representation of the distribution stores in each country')

country_option = st.selectbox(
     'Which country would you like to know?',
     (data['Country'].unique()))

graphdata = data.query(f'Country == "{country_option}"')
fig6 = px.histogram(graphdata , x='City', labels={'count' : 'No. of Stores'} , title='No. of stores per city & country').update_xaxes(categoryorder = 'total descending')    
st.write(fig6)

# Coffee Consumption
st.header('Coffee Consumption')

fig7 = px.scatter(consdata , x='PerCapita', y='Stores_count', labels={'Stores_count' : 'No. of Stores (log)', 
                                                                 'PerCapita' : 'Per capita coffee consumption'} , 
           title='No. of stores vs. Per capita coffee consumption', hover_data=['Country'] , log_y = True)
st.write(fig7)


st.subheader('We would like to know what is the trend of coffee consumption in each country')
fig8 = px.pie(consdata, values='Total', names='Country', title='consumption of amount of coffee for each country',
              hover_data=['Country'], labels={'Total':'Total Consumption'})
fig8.update_traces(textposition='inside', textinfo='percent+label')

st.write(fig8)

st.header('Food Analysis')
st.subheader('Calories Consumption')

fd_option1 = food['Food'].unique()
foodselect1 = st.multiselect('Select food you want to know?', fd_option1, default=["Plain Bagel"])
#st.write(foodselect)
food1 = food[food['Food'].isin(foodselect1)]
fig9 = px.bar(food1, x='Food', y='Calories', color='Food').update_xaxes(categoryorder = 'total descending')
st.write(fig9)

st.subheader('Carb. Consumption')
#st.write(health)
fd_option2= food['Food'].unique()
foodselect2 = st.multiselect('Select food you want to know?', fd_option2, default=["8-Grain Roll"])
food2 = food[food['Food'].isin(foodselect2)]
fig10 = px.bar(food2, x='Food', y='Carb. (g)', color='Food').update_xaxes(categoryorder = 'total descending')
st.write(fig10)



st.header('Drink Analysis')
st.subheader('Caffeine Consumption')

br_option = drink['Beverage'].unique().tolist()
Beverage = st.multiselect('Select Beverage?', br_option, default=["Coffee"])
drink = drink[(drink['Beverage'].isin(Beverage))]
fig11 = px.bar(drink, x='Beverage', y='Caffeine (mg)', color='Beverage_prep').update_xaxes(categoryorder = 'total descending')
st.write('My favorite Beverage is :kiss:', 'Starbucks')
st.write(fig11)



# Create new DataFrame for Size
st.subheader('Calories Consumption')
drinks = pd.read_csv('starbucks_drink.csv')

def remove_size(input = 'Short Latte'):
    for size in ['Short', 'Tall', 'Venti', 'Grande']:
        input = input.replace(size, '')
        input = input.strip()
    return input

drinks['Beverage_prep_without_size'] = drinks['Beverage_prep'].apply(remove_size)

rows = []
for idx, row in  drinks.groupby(['Beverage_category', 'Beverage', 'Beverage_prep_without_size']):
    if len(row) == 4:
        row = row.sort_values('Calories')
        row['Size'] = ['Short', 'Tall', 'Grande', 'Venti']
    rows.append(row)
# print(row[0])
df_size = pd.concat(rows, ignore_index=True)
df_size['Beverage_size'] = df_size['Beverage_prep_without_size'] + df_size['Size']


br_options = df_size['Beverage'].unique().tolist()
Beverage = st.multiselect('Select Beverage?', br_options, default=["Coffee"])
df_size = df_size[(df_size['Beverage'].isin(Beverage))]
fig12 = px.bar(df_size, x='Beverage', y='Calories', color='Beverage_size').update_xaxes(categoryorder = 'total descending')
st.write('My favorite Beverage is :kiss:', 'Starbucks')
st.write(fig12)




