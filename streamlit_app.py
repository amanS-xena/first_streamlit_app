import streamlit;

streamlit.title('My mom new healthy dinner');
streamlit.header('Breakfast Favourites');
streamlit.text('🥓Omega 3 & Bluebery oatmeal');
streamlit.text('🥗Kale, Spinach and Rocket Smoothie');
streamlit.text('🥚Hard-boiled free-range eggs');
streamlit.text('🥙Avocado toast');

streamlit.header('🍉🍋BUILD YOUR OWN FRUIT SMOOTHIES🍍🍌');


import pandas as pd;

my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt');
my_fruit_list = my_fruit_list.set_index('Fruit');

# Let's put a pick list here so they can pick the fruit they want to include 
fruit_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index));

fruits_to_show = my_fruit_list.loc[fruit_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show);


import requests


#header to display streamlit API
streamlit.header("Fruityvice Fruit Advice!")

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
#streamlit.text(fruityvice_response)

#to display the text in json format
streamlit.text(fruityvice_response.json())

# take the json version and normalise it - flatten the data to get key-value pair values
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# display the flattened data into a proper table
streamlit.dataframe(fruityvice_normalized)


