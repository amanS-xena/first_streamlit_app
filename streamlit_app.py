import streamlit;

streamlit.title('My mom new healthy dinner');
streamlit.header('Breakfast Favourites');
streamlit.text('🥓Omega 3 & Bluebery oatmeal');
streamlit.text('🥗Kale, Spinach and Rocket Smoothie');
streamlit.text('🥚Hard-boiled free-range eggs');
streamlit.text('🥙Avocado toast');

streamlit.header('🍉🍋BUILD YOUR OWN FRUIT SMOOTHIES🍍🍌');


import pandas as pd;

my_fruit_list = pf.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt');
streamlit.dataframe(my_fruit_list);
