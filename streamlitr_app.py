import streamlit
streamlit.title('My Mom''s New Healthy Dinner')

streamlit.header('Breakfast Favorites')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')
streamlit.text('Avocado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index("Fruit")
#Lets put a pick list here so thay pick a fruit they ant to include
fruit_selected=streamlit.multiselect("Pick Some Fruits",list(my_fruit_list.index),['Avocado','Strawberries'])
fruit_to_show=my_fruit_list.loc[fruit_selected]
#streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruit_to_show)


#New section to display fruityvice API
streamlit.header("Fruityvice Fruit Advice!")

fruit_choice=streamlit.text_input("What fruit would you like information about?",'kiwi')
streamlit.write("the user entered",fruit_choice)
import requests
fruityvice_response= requests.get("https://fruityvice.com/api/fruit/watermelon" + fruit_choice)
#streamlit.text(fruityvice_response.json())

#Takes the json version of the response and normalize it
fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
#output in the screen as a table
streamlit.dataframe(fruityvice_normalized)


import snowflake.connector
