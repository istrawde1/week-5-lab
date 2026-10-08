import streamlit as st

from apputil import visualize_demographic, visualize_families

st.write("# Titanic Visualization 1")
st.write(
    "How did survival rates differ across passenger classes and age groups?"
)
fig1 = visualize_demographic()
st.plotly_chart(fig1, use_container_width=True)

st.write("# Titanic Visualization 2")
st.write(
    "The counts are similar: 354 passengers have a listed relative aboard, "
    "and 357 share a last name with another passenger. They differ because "
    "relatives can have different last names, and unrelated passengers can "
    "share one."
)
st.write(
    "How does average ticket fare vary with family size across passenger "
    "classes?"
)
fig2 = visualize_families()
st.plotly_chart(fig2, use_container_width=True)