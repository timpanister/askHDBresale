import streamlit as st


st.title("Methods")

# Display the image using st.image
st.image('./data/flowchart.png', caption='Flow chart', use_column_width=True)

# Markdown content
markdown_content = """


### Github repository
<a href="https://github.com/timpanister/askHDBresale">Link to the Github repository</a>

### Contact
jenny_tan@np.edu.sg, Created in Oct 2024
"""

# Display the HTML content
st.markdown(markdown_content, unsafe_allow_html=True)