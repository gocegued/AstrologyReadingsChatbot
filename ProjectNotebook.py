#!/usr/bin/env python
# coding: utf-8

# # Astrology Readings Chatbot
# 
# Gina Ocegueda, COGS 18, Spring 2021, UC San Diego

# ### Want to learn what your zodiac sign is? Want to learn more information about your zodiac sign? Meet Athena! She will be giving you an astrology reading!
# 
# #### Recently, I have become very interested in astrology and love learning more about my sign. For my final project, I decided to work on a chatbot that can give an astrology reading. To do this, I made different functions. The first function would give you a greeting, another would tell you your zodiac sign and more information by you inputting your birthday, and the last function will close the conversation with a goodbye.
# 

# ## Meet Athena the Astrology Chatbot
# Run the cell below.

# In[ ]:


import random
from my_module import functions as f


# Down below, you will run the piece of code. You can start by typing in hi or hello. You can then type a space and enter. You then answer the question in the format given. After you receive your zodiac reading, you can say bye or goodbye.

# In[ ]:


while True:
   user_input = input(" ")
   if(user_input == " "): #blank
       choice = random.randint(1,2)
       if choice == 1:
           print(f.random_introduction())
       elif choice == 2:
           print(f.get_zodiac())
   elif(f.introductions(user_input)):
       print(f.random_introduction())
   elif(f.saying_bye(user_input)):
       print(f.random_goodbye())
       break
       


# In[ ]:


# test it out


# #### Extra Credit
# 
# The first time I ever coded python and coded in general was in this class so I would say I am definitely a beginner. My project went above and beyond the requirements as I did use more than three functions. I learned how to make and use a chatbot. It was very challenging for me to get what I wanted because my coding skills are not where I want them to be. It was really fun working on this project as I am very interested in astrology.

# In[ ]:




