from src.section import Section, Figure, Table


def show_macroeconomic(scenario):
    description = """
                Macroeconomic indicators show how a scenario affects the overall economy.
                Changes are shown as percentage differences from the base value.
                - The **Real Gross Domestic Product (GDPRvalu)** measures the total value of all goods and services produced in the economy, adjusted for inflation. A positive change indicates economic growth, while a negative change indicates contraction.
                - The **Value Added (VAADvalu)** represents the net output of a sector or the economy, calculated as the value of production minus the cost of intermediate goods. It helps track changes in production efficiency and productivity
                - The **Final Consumption (CONFvalu)** shows the total consumption expenditure by households, indicating if they consumer more or less.
                - The **Government Income (INCGvalu)** represents the government's revenue, mainly from taxes, which influences its ability to spend on public services and investments.
                - The **Import and Export Values (IMPOvalu & EXPOvalu)** show trade impacts with external partners.
                - The **Investment Budget (INVTvalu)** captures the level of investment in capital goods such as infrastructure, machinery, and equipment.
                - In the REWEFE-CGE model the  **Unemployment Rate (UNEMppts)** indicates the change in share of the labour force that is unemployed. A high posititive change signals that the share of labour not employed and available to be hired has increased.
                - The **Consumer Price Index (CPINinde)** represents overall price changes in the economy.

                The macroeconomic indicators should be analysed together for a complete picture. More detailed indicators, like those on production and trade, help interpret broader ones like GDP."
                """
    macroeconomic_section = Section(
        title="Macroeconomic indicators",
        anchor="macroeconomic-indicators",
        description=description,
        data={
            "figu_01_01": Figure(
                df=scenario.df,
                figure_id="figu_01_01",
                caption=f"Macroeconomic indicators in percentage change to the base in the scenario <i>{scenario.name}</i>",
                notes="GDPRvalu = value of real gross domestic product; PRODvalu = value of production (in value); VAADvalu = value added; CONFvalu = value of final consumption INCGvalu = value of government income; IMPOvalu = value of imports; EXPOvalu = value of exports; INVTvalu = value of total investments; UNEMppts = unemployment rate (change measured in percentage points, not in percentage); CPINinde = consumer price index."
            ),
            "tabl_01_01": Table(
                df=scenario.df,
                table_id="tabl_01_01",
                caption=f"Macroeconomic indicators in percentage change to the base in the scenario <i>{scenario.name}</i>",
                notes="GDPRvalu = value of real gross domestic product; PRODvalu = value of production (in value); VAADvalu = value added; CONFvalu = value of final consumption INCGvalu = value of government income; IMPOvalu = value of imports; EXPOvalu = value of exports; INVTvalu = value of total investments; UNEMppts = unemployment rate (change measured in percentage points, not in percentage); CPINinde = consumer price index."
            )
        },
        columns=[(["figu_01_01"], [1]), (["tabl_01_01"], [1])],
    )
    return macroeconomic_section
