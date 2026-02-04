import streamlit as st
import pandas as pd

from src.section import Section, Figure, Table


def get_msm(scenario):
    MSMSection: Section = Section(
        title="Indicators to the Microsimulation Model (MSM)",
        anchor="msm",
        description="""The microsimulation model indicators connect the CGE model with the **household water demand model (MSM)**. Changes in these indicators pass information about how the macroeconomic changes in the CGE model affect the microeconomic level in the microsimulation model. Indicators that can **transfer this information** include the consumption of piped water, non-water services, or changes in household disposable income. The price of electricity can also be transmitted, as it can affect the production costs of piped water, which relies on electricity.""",
        data={
            "figu_06_01": Figure(
                df=scenario.df,
                figure_id="figu_06_01",
                caption=f"Indicators to the Microsimulation Model (MSM) in <i>{scenario.name}</i>",
                notes="CONSothe = household final consumption of non-water commodities; CONSpwat = household final consumption of piped water; ENERpric = price for electricity;  INCOhous = household income; PRICothe = price of non-water commodities; PRICpwat = price of piped water."
            ),
            "tabl_06_01": Table(
                df=scenario.df,
                table_id="tabl_06_01",
                caption=f"Indicators to the Microsimulation Model (MSM) in <i>{scenario.name}</i>",
                notes="CONSothe = household final consumption of non-water commodities; CONSpwat = household final consumption of piped water; ENERpric = price for electricity;  INCOhous = household income; PRICothe = price of non-water commodities; PRICpwat = price of piped water; REU = Reunion Island."
            )
        },
        columns=[(["figu_06_01"], [1]), (["tabl_06_01"], [1])],
    )
    return MSMSection
