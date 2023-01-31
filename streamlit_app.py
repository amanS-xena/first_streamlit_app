import streamlit;
import pandas as pd;
import requests;
import snowflake.connector;
from urllib.error import URLError


streamlit.title('My mom new healthy dinner');
streamlit.header('Breakfast Favourites');
streamlit.text('🥓Omega 3 & Bluebery oatmeal');
streamlit.text('🥗Kale, Spinach and Rocket Smoothie');
streamlit.text('🥚Hard-boiled free-range eggs');
streamlit.text('🥙Avocado toast');

streamlit.header('🍉🍋BUILD YOUR OWN FRUIT SMOOTHIES🍍🍌');


#import pandas as pd;

my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt');
my_fruit_list = my_fruit_list.set_index('Fruit');

# Let's put a pick list here so they can pick the fruit they want to include 
fruit_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index));

fruits_to_show = my_fruit_list.loc[fruit_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show);


#import requests


#header to display streamlit API
#streamlit.header("Fruityvice Fruit Advice!")

#fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
#streamlit.write('The user entered ', fruit_choice)

#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response)

#to display the text in json format
#streamlit.text(fruityvice_response.json())

# take the json version and normalise it - flatten the data to get key-value pair values
#fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# display the flattened data into a proper table
#streamlit.dataframe(fruityvice_normalized)

#Create the repeatable code block
def get_fruitvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
  fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

#New section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruitvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
    
except URLError as e:
  streamlit.error()
  

#don't run anything past here
# streamlit.stop();
# #import snowflake.connector

# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT * from fruit_load_list")
# my_data_row = my_cur.fetchall()
# streamlit.header("The fruit load list contains:")
# streamlit.dataframe(my_data_row)

#Allow the end user to add a fruit to the list
# add_my_fruit = streamlit.text_input('What fruit would you like to add ?', 'jackfruit')
# streamlit.write('Thanks for adding ', add_my_fruit)


# my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('from streamlit')")

#Move the Fruit Load List Query and Load into a Button Action
streamlit.header("View Our Fruit List - Add Your Favorites!")
#snowflake-related functions
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * from fruit_load_list")
    return my_cur.fetchall()
  
#add a button to load the fruit
if streamlit.button('Get Fruit List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  my_cnx.close()
  streamlit.dataframe(my_data_rows)

  
# Allow the end user to add a fruit to the list
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('" + new_fruit + "')")
    return "Thanks for adding " + new_fruit
  
add_my_fruit = streamlit.text_input('What fruit would you like to add ?')
if streamlit.button('Add a fruit to the list'):
  my_cnx =snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row_snowflake(add_my_fruit)
  streamlit.text(back_from_function)
  
  
#streamlit.write('Thanks for adding ', add_my_fruit)
