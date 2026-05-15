# -----------------------------
# IMT 561 Streamlit Starter
# -----------------------------
#
# This repo was produced by Dr. Shane McGarry for use in a lab assignment in IMT561 at the University of Washington
# This will be adapted to create the Your Library, Your Impact Dashboard.


import streamlit as st
import pandas as pd

from src.data import load_data
from src.filters import render_filters, apply_filters
from src.charts import plot_response_hist, plot_borough_bar
from src.layouts import header_metrics, body_layout_tabs

def main() -> None:
    st.set_page_config(
        page_title="Your Library, Your Impact",
        layout="wide",
    )

    # -------------------------
    ## Header (sidebar by default)
    # Header/Title
    st.title("Your Library, Your Impact")
    st.caption("Data Dashboard for Pacific Northwest University of Health Sciences Library.")

    # ✅ Data loading (cached)
    df = load_data("data/sample.csv")

    # -------------------------
    ## Filters (sidebar by default)
    # render_filters returns a dictionary of user selections
    selections = render_filters(df)

    # apply_filters returns a filtered dataframe based on selections
    df_f = apply_filters(df, selections)

    # -------------------------
    ## KPIS
    st.subheader("Key Insights", divider="grey")
    header_metrics(df_f)
    st.caption("*NOTE: Key Insight metrics update based on the selected Date of Symptom Onset range,"
               " all percent changes reflect how these set values shift over time.", text_alignment="left")

    # -------------------------
    # Main body
    # -------------------------
    st.subheader("Visualizations", divider="grey")
    body_layout_tabs(df_f)

    # -------------------------
    # Alt. Main body from Lab06; look at table with a specific visual
    # -------------------------
    # Tabs layout by default (3 tabs)
    # tab_choice = st.radio(
    # "Choose a layout for the body (lab demo uses tabs; assignment can remix):",
    # ["Tabs (3)", "Two Columns"],
    # horizontal=True,
    # )

    # if tab_choice == "Tabs (3)":
    # body_layout_tabs()
    # else:
    # -------------------------
    # - left column: a chart
    # - right column: a table
    # -------------------------
    # col1, col2 = st.columns(2)
    # with col1:
    # st.subheader("Response Time Distribution")
    # plot_response_hist(df_f)

    # with col2:
    # st.subheader("Filtered Rows")
    # st.dataframe(df_f, use_container_width=True, height=420)

if __name__ == "__main__":
    main()
