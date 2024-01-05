import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Function to generate and display a word cloud
def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, random_state=21, max_font_size=110).generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis('off')
    st.pyplot()

# Main function to run the Streamlit app
def main():
    # Set the title of the web app
    st.title('Word Cloud Example')

    # Add a text input box for the user to enter text
    user_input = st.text_area("Enter some text:")

    # Check if the user has entered any text
    if user_input:
        # Call the function to generate and display the word cloud
        generate_wordcloud(user_input)

# Run the Streamlit app
if __name__ == '__main__':
    main()
