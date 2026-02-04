from src.section import Section, Figure, Table


def get_activities(scenario):
    description = """
                Changes in activities and commodities show how the scenario affects production, consumption, and trade
                The change in **production volume** shows whether activities are growing or shrinking, meaning whether sectors are positively or negatively affected. Scenarios can impact all activities in the same way or affect them differently, with some activities increasing, decreasing, or staying the same. Activities determine the supply of goods and services based on demand. The change in **final consumption** shows how households adjust their spending on goods and services in response to the economic shock—whether they buy more, less, or the same amount. Household consumption affects the demand for commodities produced by the activities. Changes in **export and import volumes** show the impact on international trade. If exports increase, more goods and services are needed to sell to other countries. If imports increase, more goods and services are needed to buy from other countries. These international trade partners are represented as an overall group called the **Rest of the World (RoW)**.
                """
    ActivityCommoditiesSection: Section = Section(
        title="Activity and Commodities",
        anchor="activity-and-commodity-indicators",
        description=description,
        data={
            "figu_02_01": Figure(
                df=scenario.df,
                figure_id="figu_02_01",
                caption=f"Production volume in percentage change to the base in the scenario  <i>{scenario.name}</i>",
                notes="aagri = agricultural production (including fishery and forestry); afood = food processing industries (including beverages); aoind = other industries; aelhy = electricity production based on renewable energies (hydro power, wind and solar); aelbi = electricity production based on biomass energy; aelpe = electricity production based on fossil fuel energy (petrol and coal); awasa = water, sanitary and waste sector; acons = construction sector; atran = transport sector; aadmi = public services and administration; asefi = financial services;  asenf = not financial services (e.g., tourism or trade)."
            ),
            "figu_02_02": Figure(
                df=scenario.df,
                figure_id="figu_02_02",
                caption=f"Final Consumption volume in percentage change to the base in the scenario <i>{scenario.name}</i>",
                notes="cagri = agricultural commodities (including commodities from fishery and forestry); cfood = processed food and beverages; cpetr = petroleum and petroleum products; aoind = commodities from other activities (including coal); celec = electricity; cwadi = distribution of piped water; csaco = collective sanitary service; csanc = non-collective sanitary service; ccons = construction service; ctran = transport service; cadmi = public services and administration; csefi = financial services (e.g., insurance, banking); csenf = non-financial services (e.g., tourism, trade)."
            ),
            "figu_02_03": Figure(
                df=scenario.df,
                figure_id="figu_02_03",
                caption=f"Import volume in percentage change to the base in the scenario <i>{scenario.name}</i>",
                notes="cagri = agricultural commodities (including commodities from fishery and forestry); cfood = processed food and beverages; cpetr = petroleum and petroleum products; aoind = commodities from other activities (including coal); celec = electricity; cwadi = distribution of piped water; csaco = collective sanitary service; csanc = non-collective sanitary service; ccons = construction service; ctran = transport service; cadmi = public services and administration; csefi = financial services (e.g., insurance, banking); csenf = non-financial services (e.g., tourism, trade)."
            ),
            "figu_02_04": Figure(
                df=scenario.df,
                figure_id="figu_02_04",
                caption=f"Export volume in percentage change to the base in the scenario <i>{scenario.name}</i>",
                notes="cagri = agricultural commodities (including commodities from fishery and forestry); cfood = processed food and beverages; cpetr = petroleum and petroleum products; aoind = commodities from other activities (including coal); celec = electricity; cwadi = distribution of piped water; csaco = collective sanitary service; csanc = non-collective sanitary service; ccons = construction service; ctran = transport service; cadmi = public services and administration; csefi = financial services (e.g., insurance, banking); csenf = non-financial services (e.g., tourism, trade)."
            ),
            "tabl_02_01": Table(
                df=scenario.df,
                table_id="tabl_02_01",
                caption=f"Production volume in percentage change to the base in the scenario <i>{scenario.name}</i>",
                notes="aagri = agricultural production (including fishery and forestry); afood = food processing industries (including beverages); aoind = other industries; aelhy = electricity production based on renewable energies (hydro power, wind and solar); aelbi = electricity production based on biomass energy; aelpe = electricity production based on fossil fuel energy (petrol and coal); awasa = water, sanitary and waste sector; acons = construction sector; atran = transport sector; aadmi = public services and administration; asefi = financial services;  asenf = not financial services (e.g., tourism or trade)."
            ),
            "tabl_02_02": Table(
                df=scenario.df,
                table_id="tabl_02_02",
                caption=f"Final Consumption and Trade in percentage change to the base in the scenario <i>{scenario.name}</i>",
                notes="cagri = agricultural commodities (including commodities from fishery and forestry); cfood = processed food and beverages; cpetr = petroleum and petroleum products; aoind = commodities from other activities (including coal); celec = electricity; cwadi = distribution of piped water; csaco = collective sanitary service; csanc = non-collective sanitary service; ccons = construction service; ctran = transport service; cadmi = public services and administration; csefi = financial services (e.g., insurance, banking); csenf = non-financial services (e.g., tourism, trade); CONFquan = final consumption quantity; IMPOquan = import quantity; EXPOquan = export quantity."
            ),
        },
        columns=[
            (["figu_02_01", "figu_02_02"], [1, 1]),
            (["figu_02_03", "figu_02_04"], [1, 1]),
            (["tabl_02_01", "tabl_02_02"], [3.5, 4]),
        ],
    )
    return ActivityCommoditiesSection
