"""
# Developer: Richard Raphael Banak
# Objective: Dashboard using streamlit to help Data Science table visualization
# Creation date: 2020-01-02

Run code: streamlit run main.py
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st


def cb_show_value(df):
    st.markdown("### Dataframe values")
    st.write(r"Number of columns: {}".format(df.shape[1]))
    st.write(r"number of rows: {}".format(df.shape[0]))

    if cb_flag_null:
        st.dataframe(df.style.highlight_null(null_color="red"))
    else:
        st.dataframe(df)


def main():
    global cb_value
    global cb_flag_null
    global cb_info
    global cb_plotar_grafico
    global cb_corr
    global cb_type_graph

    st.title("Data view Dashboard")

    st.sidebar.title("Menu")

    file_path = st.sidebar.file_uploader(
        label="Select dataframe file", type=["csv", "xlsx"]
    )

    cb_value = st.sidebar.checkbox("Show dataframe values")
    cb_flag_null = st.sidebar.checkbox("Flag null values")
    cb_info = st.sidebar.checkbox("Show dataframe info")
    cb_plotar_grafico = st.sidebar.checkbox("Plot Chart")
    cb_corr = st.sidebar.checkbox("Show correlation heatmap")

    cb_type_graph = st.sidebar.selectbox(
        "Select graph type",
        ["Scatter"],  # "Boxplot", "Histogram", "Scatterplot", "Line", "Bar", "Pie"],
    )

    if not file_path:
        st.write("Select file at menu sidebar")
        # st.markdown("Selecionar arquivo no menu lateral")

    else:

        df = pd.read_csv(filepath_or_buffer=file_path)
        numeric_columns = df.select_dtypes(include=["int64", "float64"]).columns

        column_x = st.sidebar.selectbox("Choose axis column X", numeric_columns)
        column_y = st.sidebar.selectbox("Choose axis column Y", numeric_columns)

        # show dataframe values
        if cb_value:
            cb_show_value(df)
        # show describe dataframe
        if cb_info:
            st.markdown("### Describe")
            st.write(df.describe())

        # plot chart
        if cb_plotar_grafico:
            if cb_type_graph == "Scatter":
                st.subheader("Scatter Chart")
                fig = plt.figure()
                plt.scatter(data=df, x=column_x, y=column_y)
                st.pyplot(fig)

        # show correlation heatmap
        if cb_corr:
            st.subheader("Heatmap of correlation between columns")
            fig = plt.figure()
            sns.heatmap(df.corr())
            st.pyplot(fig)

        # stream via matplotlib
        # fig = plt.figure()
        # plt.scatter(data=df, x=column_x, y=column_y)
        # st.pyplot(fig)

        # stream via plotly
        # st.plotly_chart(px.scatter(df, x="body_mass_g", y="culmen_depth_mm"))
        # st.sidebar.checkbox(label="Li e aceito")
        # st.sidebar.selectbox("Selecionar", ["Opção 1", "Opção 2", "Opção 3"])


if __name__ == "__main__":
    main()
