from src.section import Figure, Table, Section


def show_government_household(scenario):
    description = """
                Changes in income show how scenarios affect how much **economic agents** earn. The change in income determines how economic agents can **spend or consume**. The government earns income through taxes and spends this money on services (like public services) or subsidies. Households earn income by providing production factors (like labor) to activities. In addition to labour income, households can receive transfers from the government, such as subsidies or social assistance. **Households also pay taxes** to the government, contributing to the government income. In different scenarios, changes in commodity and factor markets affect the demand for labor, which in turn impacts employment. If employment decreases, households earn less money and spend less. Less employment and consumption can also lead to lower tax income for the government. Overall, if household real income drops, it can **reduce consumption and have a negative effect** on the economy. On the other hand, if a scenario increases household income, it can lead to more consumption and help stimulate the economy."""
    notes = [
        "GOINvalu = total value of government income; GINKvalu = value of government income from capital; TPROvalu = value of government income from taxes on production; TCOMvalu = value of government income from taxes on commodities; TIMPvalu = value of government income from taxes on imports; GTRAvalu = value of government income from transfers; REU = Reunion Island.",
        "HHINvalu = total value of household income; HICAvalu = value of household income from capital; HILAvalu = value of household income from labour; HITRvalu = value of household income from transfers; HIDPvalu = value of household disposable income; HCOBvalu = value of household consumption budget; HSAVvalu = value of household savings.",
    ]

    section_data = {
        "figu_04_01": Figure(
            df=scenario.df,
            figure_id="figu_04_01",
            caption=f"Government Income in percentage change to the base in the scenario <i>{scenario.name}</i>",
            notes="GOINvalu = total value of government income; GINKvalu = value of government income from capital; TPROvalu = value of government income from taxes on production; TCOMvalu = value of government income from taxes on commodities; TIMPvalu = value of government income from taxes on imports; GTRAvalu = value of government income from transfers."
        ),
        "figu_04_02": Figure(
            df=scenario.df,
            figure_id="figu_04_02",
            caption=f"Household Income in percentage change to the base in the scenario <i>{scenario.name}</i>",
            notes="HHINvalu = total value of household income; HICAvalu = value of household income from capital; HILAvalu = value of household income from labour; HITRvalu = value of household income from transfers; HIDPvalu = value of household disposable income; HCOBvalu = value of household consumption budget; HSAVvalu = value of household savings."
        ),
        "tabl_04_01": Table(
            df=scenario.df,
            table_id="tabl_04_01",
            caption=f"Governement Income in percentage change to the base in the scenario <i>{scenario.name}</i>",
            notes="GOINvalu = total value of government income; GINKvalu = value of government income from capital; TPROvalu = value of government income from taxes on production; TCOMvalu = value of government income from taxes on commodities; TIMPvalu = value of government income from taxes on imports; GTRAvalu = value of government income from transfers; REU = Reunion Island."
        ),
        "tabl_04_02": Table(
            df=scenario.df,
            table_id="tabl_04_02",
            caption=f"Household Income in percentage change to the base in the scenario <i>{scenario.name}</i>",
            notes="HHINvalu = total value of household income; HICAvalu = value of household income from capital; HILAvalu = value of household income from labour; HITRvalu = value of household income from transfers; HIDPvalu = value of household disposable income; HCOBvalu = value of household consumption budget; HSAVvalu = value of household savings; REU = Reunion Island."
        )
    }

    section_columns = [
        (["figu_04_01"], [1]),
        (["figu_04_02"], [1]),
        (["tabl_04_01", "tabl_04_02"], [1, 1]),
    ]

    return Section(
        title="Government and Household income",
        anchor="government-and-households",
        description=description,
        data=section_data,
        columns=section_columns
    )
