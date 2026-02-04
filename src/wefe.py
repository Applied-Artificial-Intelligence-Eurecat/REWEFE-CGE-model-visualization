from src.section import HeadersSection, Figure, Table


def show_wefe(scenario):
    description = """
        The WEFE nexus indicators show how scenarios affect the **four pillars of the WEFE nexus**. These indicators represent changes in economic factors like production, consumption, and prices. The changes are shown together in this section for all four WEFE nexus pillars, helping to understand how different sectors are linked (**sectoral interlinkages**). To understand these links, the results need to be looked at as a whole, **considering cause-and-effect relationships between sectors**. For example, if a scenario reduces raw water supply, it first affects water-related activities, and then all other activities that use water in production. Similarly, if energy prices increase, it first impacts the energy market, and then all activities that use energy.
        """
    return HeadersSection(
        title="WEFE Nexus Indicators",
        anchor="wefe-nexus",
        description=description,
        data={
            "figu_05_01": Figure(df=scenario.df, figure_id="figu_05_01",
                                 caption=f"W(ater) - pillar -- Production of the water and sanitary service activities in percentage change to the base in the scenario <i>{scenario.name}</i>",
                                 notes="cwadi = distribution of piped water; csaco = collective sanitary service; csanc = non-collective sanitary service"),
            "figu_05_02": Figure(df=scenario.df, figure_id="figu_05_02",
                                 caption=f"W(ater) - pillar -- Final consumption of the water and sanitary services and total intermediate demand of piped water in percentage change to the base in the scenario <i>{scenario.name}</i>",
                                 notes="WADIdito = total intermediate demand for piped water; WADIcons = final consumption of piped water; SACOcons = final consumption of collective water disposal services; SANCcons = final consumption of non-collective water disposal services."),
            "figu_05_03": Figure(df=scenario.df, figure_id="figu_05_03",
                                 caption=f"W(ater) - pillar -- Prices of the water and sanitary services in percentage change to the base in the scenario <i>{scenario.name}</i>",
                                 notes="cwadi = distribution of piped water; csaco = collective sanitary service; csanc = non-collective sanitary service"),
            "figu_05_04": Figure(df=scenario.df, figure_id="figu_05_04",
                                 caption=f"E(nergy) - pillar -- Production of the electricity producing activities in percentage change to the base in the scenario <i>{scenario.name}</i>",
                                 notes="aelhy = electricity production based on renewable energies (hydro power, wind and solar); aelbi = electricity production based on biomass energy; aelpe = electricity production based on fossil fuel energy (petrol and coal)."),
            "figu_05_05": Figure(df=scenario.df, figure_id="figu_05_05",
                                 caption=f"E(nergy) - pillar -- Intermediate demand and final consumption of electricity in percentage change to the base in the scenario <i>{scenario.name}</i>",
                                 notes="ELECdito = total intermediate demand for electricity; ELECcons = final consumption of electricity."),
            "figu_05_06": Figure(df=scenario.df, figure_id="figu_05_06",
                                 caption=f"E(nergy) - pillar -- Consumer price of electricity in percentage change to the base in the scenario <i>{scenario.name}</i>",
                                 notes="celec = electricity"),
            "figu_05_07": Figure(df=scenario.df, figure_id="figu_05_07",
                                 caption=f"F(ood) - pillar -- Production of the agriculture and food producing activities in percentage change to the base in the scenario <i>{scenario.name}</i>",
                                 notes="cagri = agricultural commodities (including commodities from fishery and forestry); cfood = processed food and beverages."),
            "figu_05_08": Figure(df=scenario.df, figure_id="figu_05_08",
                                 caption=f"F(ood) - pillar -- Intermediate demand of agricultural and food commodities in percentage change to the base in the scenario <i>{scenario.name}</i>",
                                 notes="cagri = agricultural commodities (including commodities from fishery and forestry); cfood = processed food and beverages."),
            "figu_05_09": Figure(df=scenario.df, figure_id="figu_05_09",
                                 caption=f"F(ood) - pillar -- Consumer price of agricultural and food commodities in percentage change to the base in the scenario <i>{scenario.name}</i>",
                                 notes="cagri = agricultural commodities (including commodities from fishery and forestry); cfood = processed food and beverages."),
            "figu_05_10": Figure(df=scenario.df, figure_id="figu_05_10",
                                 caption=f"F(ood) - pillar -- Prices of agricultural and food commodities in percentage change to the base in the scenario <i>{scenario.name}</i>",
                                 notes="cagri = agricultural commodities (including commodities from fishery and forestry); cfood = processed food and beverages."),
            "figu_05_11": Figure(df=scenario.df, figure_id="figu_05_11",
                                 caption=f"E(cosystems) - pillar -- Emissions of CO2 and water pollutants in percentage change to the base in the scenario <i>{scenario.name}</i>",
                                 notes="ECOSco2p = CO2 emissions from petrol usage (i.e., final and intermediate petrol consumption); ECOSco2e = CO2 emissions from electricity production;  ECOSnitr = nitrogen emissions to the water bodies resulting from industrial production and households; ECOSnagr = nitrogen emissions to the water bodies resulting from agricultural production; ECOSphos = phosphor emissions to the water from industrial production and households"),
            "tabl_05_01": Table(df=scenario.df, table_id="tabl_05_01",
                                caption=f"W(ater)-pillar indicators in percentage change to the base in the scenario <i>{scenario.name}</i>",
                                notes="WATEprod = production of water and sanitary services; WATEdito = total intermediate demand for piped water; WATEcons = final consumption of piped water; WATEpric = price of piped water; cwadi = distribution of piped water; csaco = collective sanitary service; csanc = non-collective sanitary service."),
            "tabl_05_02": Table(df=scenario.df, table_id="tabl_05_02",
                                caption=f"E(nergy)-pillar indicators in percentage change to the base   in the scenario <i>{scenario.name}</i>",
                                notes="ENERprod = production of energy as electricity; ENERdito = total intermediate demand for electricity; ENERcons = final consumption of electricity; ENERpric = price of electricity; aelhy = electricity production based on renewable energies (hydro power, wind and solar); aelbi = electricity production based on biomass energy; aelpe = electricity production based on fossil fuel energy (petrol and coal); celec = electricity;"),
            "tabl_05_03": Table(df=scenario.df, table_id="tabl_05_03",
                                caption="F(ood)-pillar indicators in percentage change to the base in the scenario <i>{scenario.name}</i>",
                                notes="FOODprod = production of agricultural and food commodities; FOODdito = total intermediate demand for agricultural and food commodities;FOODcons = final consumption of agricultural and food commodities; FOODpric = prices of agricultural and food commodities; cagri = agricultural commodities (including commodities from fishery and forestry); cfood = processed food and beverages"),
            "tabl_05_04": Table(df=scenario.df, table_id="tabl_05_04",
                                caption="E(cosystems)-pillar indicators in percentage change to the base in the scenario <i>{scenario.name}</i>",
                                notes="ECOSco2p = CO2 emissions from petrol usage (i.e., final and intermediate petrol consumption); ECOSco2e = CO2 emissions from electricity production;  ECOSnitr = nitrogen emissions to the water bodies resulting from industrial production and households; ECOSnagr = nitrogen emissions to the water bodies resulting from agricultural production; ECOSphos = phosphor emissions to the water from industrial production and households")
        },
        columns=[
            (["figu_05_01", "figu_05_02", "figu_05_03"], [1, 1, 1]),
            (["figu_05_04", "figu_05_05", "figu_05_06"], [1, 1, 1]),
            (["figu_05_07", "figu_05_08"], [1, 1]),
            (["figu_05_09", "figu_05_10"], [1, 1]),
            (["figu_05_11"], [1]),
            (["tabl_05_01", "tabl_05_02"], [1, 1]),
            (["tabl_05_03", "tabl_05_04"], [1, 1]),
        ],
        headers=["Water", "Energy", "Food", "", "Ecosystems", "Tables", ""]
    )
