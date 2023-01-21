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
