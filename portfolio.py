import streamlit as st
from PIL import Image

# vars
links_text = "**Find links below**"

# html hacks
hide_img_fs = '''
<style>
button[title="View fullscreen"]{
    visibility: hidden;}
</style>
'''
header_alignment="""
<style>
h2 {
  text-align: center
}
</style>
"""
subheader_alignment="""
<style>
h3 {
  text-align: center
}
</style>
"""
st.markdown(hide_img_fs, unsafe_allow_html=True)
st.markdown(header_alignment, unsafe_allow_html=True)
st.markdown(subheader_alignment, unsafe_allow_html=True)

# to display
st.header("Nils Skoglund Portfolio Projects")

with st.expander("Analytics engineering example project"):
    st.subheader("Analytics engineering example project")
    left_co, cent_co,last_co = st.columns([1,6,1])
    image = Image.open('ae.png')
    with cent_co:
        st.image(image
                , caption='Overview of tools used in the project')
    text_pe = '''
                In this project I built a small data warehouse in BigQuery\
                that is used for an analytics dashboard in Looker.\
                The data warehouse includes daily batches of
                - API data (~5k rows, ~20 cols)
                - ddb data (~100k rows nested data, flattened ~50 cols)
                - GA data (~5k rows nested data, flattened ~30 cols)
                
                
                The data is moved using SQL and Python in the context of
                - AWS glue
                - Google Cloud Functions
                - BigQuery Scheduled Queries

                '''
    st.markdown(text_pe)
    st.write(links_text)
    text_live_app = "*Below are links to the live version of the app.\
        The live version implements more questionnaires but lacks\
         user authentication and database interactions.*"
    st.write(text_live_app)
    live_url_app = "[App](https://metis-live.streamlit.app/)"
    url = "https://github.com/NilsSkoglund/lungemboli_multipage_master"
    live_url_github=f"[Github]({url})"
    st.markdown(
        f'''
        - {live_url_app}
        - {live_url_github}
        '''
    )
    st.write("")
    text_dev_app = "*Below are links to the development version of the app\
        which implements less questionnaires but has user authentication\
        and database interactions.*"
    st.write(text_dev_app)
    dev_url_app = "[App](https://metis-dev.streamlit.app/)"
    url = "https://github.com/NilsSkoglund/metis_development"
    dev_url_github=f"[Github]({url})"
    st.markdown(
        f'''
        - {dev_url_app}
        - {dev_url_github}
        '''
    )
    st.write("")

with st.expander("Pulmonary Embolism app"):
    st.subheader("Pulmonary Embolism app")
    left_co, cent_co,last_co = st.columns([1,6,1])
    image = Image.open('pe.png')
    with cent_co:
        st.image(image
                , caption='Patients are stratified in risk groups')
    text_pe = "A web application written in streamlit\
         meant to be used as a support tool for\
        diagnosing Pulmonary Embolism (PE). The application guides\
        the user (typically an ER doctor) through various questionnaires\
        helping them effectively adopt best practices when diagnosing\
         PE."
    st.write(text_pe)
    st.write(links_text)
    text_live_app = "*Below are links to the live version of the app.\
        The live version implements more questionnaires but lacks\
         user authentication and database interactions.*"
    st.write(text_live_app)
    live_url_app = "[App](https://metis-live.streamlit.app/)"
    url = "https://github.com/NilsSkoglund/lungemboli_multipage_master"
    live_url_github=f"[Github]({url})"
    st.markdown(
        f'''
        - {live_url_app}
        - {live_url_github}
        '''
    )
    st.write("")
    text_dev_app = "*Below are links to the development version of the app\
        which implements less questionnaires but has user authentication\
        and database interactions.*"
    st.write(text_dev_app)
    dev_url_app = "[App](https://metis-dev.streamlit.app/)"
    url = "https://github.com/NilsSkoglund/metis_development"
    dev_url_github=f"[Github]({url})"
    st.markdown(
        f'''
        - {dev_url_app}
        - {dev_url_github}
        '''
    )
    st.write("")

with st.expander("Workout Schedule app"):
    st.subheader("Workout Schedule app")
    # with cent_co:
    image = Image.open('workout.png')
    caption = 'Set quarterly goals and get at it with weekly workout schedules'
    st.image(image
            , caption=caption)
    text_schedule = "A web application written in streamlit and\
         meant to be used to plan & track fitness related actitvities."
    st.write(text_schedule)
    st.write(links_text)
    schedule_url_app = "[App](https://nils-schema.streamlit.app/)"
    url = "https://github.com/NilsSkoglund/nils_schedule"
    schedule_url_github=f"[Github]({url})"
    st.markdown(
        f'''
        - {schedule_url_app}
        - {schedule_url_github}
        '''
    )
    st.write("")

with st.expander("Data analytics/science workshop"):
    st.subheader("Data analytics/science workshop")
    image_url = ("https://github.com/NilsSkoglund/"
                 "ki_workshop/blob/main/"
                 "ki%20workshop.png?raw=true")
    st.image(f"{image_url}"
             , caption="Picture from one of the workshops")
    olink = "[OLINK](https://olink.com/)"
    text_workshop = f"This workshop was aimed at coding beginners\
         with domain expertise in medicine.\
         In the codealong we started with basic Python code \
        and moved on to conducting data manipulation, visualization\
         and statistical analysis. As the grande finale of the workshop we\
         applied unsupervised ML to cluster Covid\
         patients based on protemoics data ( from {olink} ) "
    
    st.write(text_workshop)
    st.write(links_text)
    url = "https://github.com/NilsSkoglund/ki_workshop"
    workshop_url_github=f"[Github]({url})"
    st.markdown(
        f'''
        - {workshop_url_github}
        '''
    )
    st.write("")



with st.expander("SQL Intro course"):
    st.subheader("SQL Intro course")
    image = Image.open('sql.png')
    st.image(image
             , caption='Overview of the 4 day schedule')
    text_sql = f"During my time at the coding bootcamp company Nod,\
          I developed an introductory course for SQL. I was also responsible\
             for selling and delivering the course. The project was\
             successful and added great value to Nod's offerings.\
             The course was built for Google Cloud Platform and involved\
             working with Google BigQuery and Google Data Studio."
    
    st.write(text_sql)
    st.write(links_text)
    url = "https://github.com/NilsSkoglund/sql_master"
    workshop_url_github=f"[Github]({url})"
    url = ("https://github.com/NilsSkoglund/"
           "sql_master/blob/main/SQL_material/"
           "04_window_case/window_master/ca_window_func.sql")
    sql_ca_github=f"[Query examples from final day]({url})"
    
    st.markdown(
        f'''
        - {workshop_url_github}
        - {sql_ca_github}
        '''
    )
    st.write("")