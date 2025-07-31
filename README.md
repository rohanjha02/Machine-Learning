**IMDb Movie Rating Predictor**

**Project Overview**

This project is a machine learning application that predicts movie ratings based on director and genre information. It scrapes data from IMDb's Top 250 Movies, processes this information, builds a prediction model, and deploys it through a user-friendly web interface.

**How It Works (In Simple Terms)**

Imagine you're wondering: "If Christopher Nolan made a comedy film, would it likely be highly rated?" This project answers exactly these kinds of questions by learning from historical movie data.

The system works in four main steps:

1. **Data Collection**: We automatically gather information about the top 250 movies from IMDb
2. **Data Processing**: We clean and organize this information to make it useful
3. **Model Training**: We teach our computer to recognize patterns between directors, genres, and ratings
4. **Prediction**: You can ask the system about any director and genre combination to get a rating prediction

**Components Explained**

**1\. Data Collection (scrape.py)**

The project starts by collecting data from IMDb's Top 250 Movies list using a web scraper built with Selenium. For each movie, we extract:

- Movie title
- Release year
- Duration
- Rating (PG, R, etc.)
- Genre
- Director
- IMDb rating score
- Stars/actors
- Streaming availability

This information is saved in an Excel file (IMDb_Top_250_Movies.xlsx) for further processing.

#  Example of how the scraper works:

#  1. Opens the IMDb Top 250 page

#  2. Clicks on each movie's info button

#  3. Extracts all the details from the popup

#  4. Saves everything to an Excel file

**2\. Data Processing and Model Building**

The collected data undergoes several transformations to prepare it for machine learning:

- Cleaning missing values
- Converting text data to numerical format
- Identifying patterns between directors, genres, and ratings
- Creating a machine learning pipeline that can:
  - Process new input data in the same way as our training data
  - Make accurate predictions based on historical patterns

The model categorizes potential movies into three rating categories:

- High rating (likely to be well-received)
- Low rating (might not perform well)
- "Director hasn't worked in this genre" (when there's no historical data)

**3\. Web Application**

The prediction model is integrated into a Django web application that provides:

- A simple interface where users can select a director and genre
- Instant predictions about the likely rating outcome
- An easy way to experiment with different combinations

**Technical Details (For Those Interested)**

- **Web Scraping**: Uses Selenium with Microsoft Edge WebDriver to automate data collection
- **Data Storage**: Initial data stored in Excel format
- **Machine Learning Pipeline**: Handles preprocessing, feature engineering, and model training
- **Model Deployment**: Django web framework serves the prediction model
- **User Interface**: Simple form-based interface for entering director and genre

**How To Use**

1. Select a movie director from the dropdown menu
2. Choose a genre you're curious about
3. Click the predict button
4. Get an instant prediction about whether this combination would likely result in a high-rated movie

**Project Value**

This tool can be useful for:

- Movie enthusiasts curious about "what if" scenarios
- Film students studying director-genre relationships
- Anyone interested in understanding what factors contribute to highly-rated movies

The project demonstrates how machine learning can identify patterns in creative industries and make predictions about subjective qualities like film ratings.

**Screenshots-**

!\[1\](<https://github.com/rohanjha02/Machine-Learning/assets/153548889/9f7c2b3b-8329-428d-b3d1-b31c6b277a2e>)

!\[2\](<https://github.com/rohanjha02/Machine-Learning/assets/153548889/ee344172-5b1d-42be-ab25-78fffa28edf4>)

!\[3\](<https://github.com/rohanjha02/Machine-Learning/assets/153548889/0ebdf69c-98c8-4451-a237-ca40972213f4>)
