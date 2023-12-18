import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show_explore_page():
    df = pd.read_csv("Fuel_Consumption.csv")
    st.title("Explorer la quantité de CO2 émis des vehicules.")

    st.write(
        """
    #### (A) Quantité CO2 émis en moyenne par rapport au nombre de cylindre
    """
    )

    data = df.groupby(["CYLINDERS"])["CO2EMISSIONS"].mean().sort_values(ascending=True)
    st.bar_chart(data, y="CO2EMISSIONS")

    st.write(
        """
    #### (B) Quantité CO2 émis en moyenne par rapport à la taille du moteur
    """
    )

    data = df.groupby(["ENGINESIZE"])["CO2EMISSIONS"].mean().sort_values(ascending=True)
    st.line_chart(data, y="CO2EMISSIONS")

    st.write(
        """
    #### (C) Quantité CO2 émis en moyenne par rapport à la consommation de carburant
    """
    )

    data = df.groupby(["FUELCONSUMPTION_COMB"])["CO2EMISSIONS"].mean().sort_values(ascending=True)
    st.line_chart(data, y="CO2EMISSIONS")

    with st.sidebar.expander("Cliquez pour en savoir plus sur ce tableau de bord"):
        st.markdown("""
        
        Ici, dans les graphiques suivants, nous suivront:

        (A) La quantité moyenne de C02 émis par rapport au nombre de cylindre. Et nous constatons,
        sans surprise, qu'elle est d'autant plus élevé que le nombre de cylindre est grand.

        (B) La quantité moyenne de C02 émis par rapport à la taille du moteur.

        """)