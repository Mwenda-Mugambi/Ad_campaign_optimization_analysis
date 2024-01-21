import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Placeholder function for your predictive model
def predict_web_traffic(user_type, dates):
    # Replace with your own model logic
    # This function currently returns random data for demonstration purposes
    return np.random.randint(100, 500, size=len(dates))
# Image banner
# banner_image_path = 'Design_Assets/Header_image.jpg'  
# st.image(banner_image_path, use_column_width=True)
st.markdown("This product analyzes and predicts the dynamics of food commodity prices in Nairobi, Kenya."
                "Select a month and year that you would like to predict prices for.", unsafe_allow_html=True)

# Main app
def main():
    st.title("Web Traffic Prediction")

    # You can replace this with your actual animation
    st.markdown("## Plane Animation Placeholder")

    user_type = st.radio("Select User Type", ('New Users', 'Total Users'))

    # Date selection
    start_date = st.date_input("Start Date")
    end_date = st.date_input("End Date")

    if start_date and end_date:
        dates = pd.date_range(start_date, end_date)

        if st.button('Predict'):
            predictions = predict_web_traffic(user_type, dates)

            # Displaying the predictions
            if user_type == 'New Users':
                st.write(f"Predicted new users are {sum(predictions)}")
            else:
                st.write(f"Predicted total users are {sum(predictions)}")

            # Plotting
            plt.figure(figsize=(10, 4))
            plt.plot(dates, predictions, marker='o')
            plt.title(f'Predicted Web Traffic for {user_type}')
            plt.xlabel('Date')
            plt.ylabel('Number of Users')
            plt.xticks(rotation=45)
            st.pyplot(plt)

if __name__ == "__main__":
    main()