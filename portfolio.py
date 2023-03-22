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
st.write("")

with st.expander("Analytics engineering example project (work)"):
    st.subheader("Analytics engineering example project")
    left_co, cent_co,last_co = st.columns([1,6,1])
    image = Image.open('ae.png')
    with cent_co:
        st.image(image
                , caption='Overview of tools used in the project')
    text_pe = '''
                In this project I built a small data warehouse in BigQuery\
                for a digital marketing agency.\
                The data warehouse includes daily batches of
                - ddb data (~100k rows nested data, flattened ~50 cols)
                - API data (~5k rows, ~20 cols)
                - GA data (~5k rows nested data, flattened ~30 cols)

                \\
                The data is moved using SQL and Python in the context of
                - AWS glue
                - Google Cloud Functions
                - BigQuery Scheduled Queries

                \\
                The data is used for analytics dashboards in Looker\
                , some of which I helped set up.
                '''
    st.markdown(text_pe)
    st.write("")
    text_live_app = "Due to a NDA, I'm limited in what I can showcase\
        for this project. Below is a link to a private github repo\
        where I can do a live demo of some of the relevant material"
    st.write(text_live_app)
    url_pt1 = "https://github.com/NilsSkoglund/"
    url_pt2 = "Analytics-engineering-portfolio-example"
    url_github=f"[Github]({url_pt1+url_pt2})"
    st.markdown(
        f'''
        - {url_github}
        '''
    )
    st.write("")

with st.expander("Pulmonary Embolism app (spare time)"):
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

with st.expander("Workout Schedule app (spare time)"):
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

with st.expander("Data analytics/science workshop (work)"):
    st.subheader("Data analytics/science workshop")
    image_url = ("https://github.com/NilsSkoglund/"
                 "ki_workshop/blob/main/"
                 "ki%20workshop.png?raw=true")
    st.image(f"{image_url}"
             , caption="Picture from one of the workshops")
    olink = "[OLINK](https://olink.com/)"
    umap = "[UMAP](https://umap-learn.readthedocs.io/en/latest/)"
    text_workshop = f"This workshop was aimed at coding beginners\
         with domain expertise in medicine.\
         In the codealong we started with basic Python code \
        and moved on to data manipulation, visualization\
         and statistical analysis. As the grande finale of the workshop we\
         applied unsupervised ML ({umap}) on protemoics data (from {olink})."
    
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



with st.expander("SQL Intro course (work)"):
    st.subheader("SQL Intro course")
    image = Image.open('nod_sql.png')
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

st.write("---")

center_button = '''
<style>
.row-widget.stDownloadButton {text-align: center;}
</style>
'''
st.markdown(center_button, unsafe_allow_html=True)

file_name_cv = "Nils Skoglund CV.pdf"
with open(file_name_cv, "rb") as file:
    cv = file.read()
st.download_button(label="Download CV",
                        data=cv,
                        file_name=file_name_cv)


file_name_records = "transcript of records UU.pdf"
with open(file_name_records, "rb") as file:
    records = file.read()
st.download_button(label="Download Transcript of Records",
                        data=records,
                        file_name=file_name_records)


st.markdown(
    """
    <a style='display: block; text-align: center; color: white;' href="https://www.credential.net/49eb1a90-490c-4ef8-85ff-45c2092dd6cc#gs.tc23rg">Nod Certificate</a>
    """,
    unsafe_allow_html=True,
)
