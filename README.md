# ☑️Temperature-control-using-Fuzzy-logic
This set of scripts uses Fuzzy logic and PID to maintain a temperature in an environment. Plans to add MPC in the future.

## ❇️Features
- **Fuzzy logic**: A fairly simple implementation of Fuzzy logic to get input on how much to heat at each given time.
- **PID**: Standard usage of PID, it uses the current, past and future to give an output of how much to heat to remain at the ideal temperature.
- **Graph**: Matplotlib is used to graph all temperatures giving you an idea of where the temperature stays at over time.

#### This project was made entirely in Python.

## 🤔The Process 

At first I made the entire project in one file and using very simple if logic, basically an "advanced" bang-bang control system.

I then understood properly how Fuzzy works and split it into a different file to allow for expansion later on.

The programming of the furnace taught me some nuances about max and minimum of a value amongst other things but the hardest thing was the logic.

I spent the majority of the time understanding how Fuzzy works instead of just incoorporating something I wouldn't understand.

I then sampled data from every step and graphed it with my previous experience in matplotlib.

After this I decided to work on PID, in my case the PID logic was pretty straightforward and after a bit of trial and error and small fine-tuning of the constants I got something I was relatively satisfied with.

It took a video or two on PID logic and how it works but it was just fine, I have asperations to add an AI to later find the ideal values for this very example.

## 📚My takeaways 

I got to use plotting now which was fun, I feel like I've gotten real understanding of a real control system concept, the Fuzzy control system which is incredibly motivating.

A big takeaway from this is that planning plays a huge role, rather spend a few minutes deciding how you're gonna program instead of just starting, it's often a big time saver.

## 🚀Running the project 

1. Install the main.py, fuzzy.py and PID.py
2. Using an editor and Python installed you open all three in the same folder and then run the fuzzy or PID file depending on which control logic you wanna use.

## 🍿Video

