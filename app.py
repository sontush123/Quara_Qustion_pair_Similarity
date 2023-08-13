import streamlit as st
import helper
import pickle

model = pickle.load(open('model.pkl','rb'))


# Adjust the size of the first header using CSS styling
header1_style = "<style>h1.header1{font-size: 32px;}</style>"
st.markdown(header1_style, unsafe_allow_html=True)

# Display the first header with the adjusted size
st.markdown("<h1 class='header1'>Duplicate Question Pairs</h1>", unsafe_allow_html=True)
#st.header('Duplicate Question Pairs')


#st.header('Movie Recommender System')

import webbrowser

def open_github_repo():
    url = 'https://github.com/sontush123/Quara_Qustion_pair_Similarity.git'
    webbrowser.open_new_tab(url)


col1, col2 = st.columns([3, 1])  # Adjust the column widths as needed
# Adjust the size of the second header using CSS styling
header2_style = "<style>h1.header2{font-size: 24px;}</style>"
st.markdown(header2_style, unsafe_allow_html=True)

# Display the second header with the adjusted size
#st.markdown("<h1 class='header2'>Header 2</h1>", unsafe_allow_html=True)
# Add the header to the first column
#col1.header('Welcome to My App')
col1.markdown("<h1 class='header2'>Welcome to My App</h1>", unsafe_allow_html=True)
# Add the button to the second column
if col2.button('CODE OF THIS PROJECT'):
    #open_github_repo()
    st.markdown('<a href="https://github.com/sontush123/Quara_Qustion_pair_Similarity.git" target="_blank">Click here to visit code reposistory of this Website</a>', unsafe_allow_html=True)


q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')

if st.button('Find'):
    query = helper.query_point_creator(q1,q2)
    result = model.predict(query)[0]

    if result:
        st.header('Duplicate')
    else:
        st.header('Not Duplicate')


