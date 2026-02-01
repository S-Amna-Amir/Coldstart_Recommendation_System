# Overview
This project implements a minimal recommendation system designed to cater for little to no user data, and minimal but structured product data. The system is displayed through a FLASK application running on localhost.
The system recommends items from a small catalog, and provides a short explanation for recommendation on each. 
# How the System works
1. Item Catalog: Each item has id, name, category, price, and gender fields. 
2. User/Session Input: The optional input of preferred category, and seen_items. These may be empty
3. Recommendation Heuristic Logic: Each item is scored using the following heuristics:
   Affordability bonus (items lesser than 50 receive extra points)
   Broad suitability bonus (gender neutral items receive additional points)
   Session based personalization (if the item is from preferred category, it has higher score)
   Light exploration (a small random value is added to encourage exploration, and avoid identical rankings)
4. The items are sorted by their final score (highest first).
5. The code can be run by running app.py, and then visiting  http://127.0.0.1:5000/
# Key Decisions and Tradeoffs
The system uses rule-based scoring instead of machine learning because of simplicity, minimal implementation requirement, and faster coding
The items are stored as static data in memory rather than a proper database. This was more convenient for a small demo
Only a very minimal session-level data is used, other metrics such as user clicks, or user time is not stored or processed. It would have resulted in ore accurate recommendations, but then the scope would have increased from static webpages to dynamic content
# Improvements over time and data
1. More user data (user clicks, views, purchases, cookies, user profiles etc could be stored)
2. Smarter ranking (the heuristics could be replaced with a machine learning model)
3. The catalog could be larger and more dynamic by loading items from a database, support real time updates, and add extensive item attributes such as ratings, popularity, descriptions etc
4. The UI/UX could definitely be improved by color themes, pagination, responsiveness etc.
