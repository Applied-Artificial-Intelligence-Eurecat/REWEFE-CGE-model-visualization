from src.section import Figure, Table, Section


def get_commodity_prices(scenario):
    return Section(
        title="Commodity and Factor prices",
        anchor="commodity-and-factor-prices",
        description="""
                 Changes in prices show how markets are changing. Markets consist of **supply** (e.g., how much of a good is provided by producers) and **demand** (e.g., how much consumers want to buy). In a market, the supply is meant to meet the demand for a good at a price that works for both consumers and producers. This price is called the **equilibrium price**, where supply and demand are balanced. An economic shock - such as a sudden increase in costs or a drop in consumer demand - can disrupt the market equilibrium by affecting supply or demand, leading to price changes. Economic scenarios can also directly affect prices (e.g., through higher tariffs). These price changes then cause shifts in supply and/or demand. Price changes reflect changes in markets, and these changes can happen in different ways. When commodity prices change, it shows what is happening in the **commodity markets**.
                 When factor prices change, it shows what’s happening in the markets for production factors (like labor and capital). In **factor markets**, the **factor price** (e.g., wages for labor, rental rent for capital) is determined by **factor supply** and the **factor demand**. If demand for a factor goes up or supply decreases, the price for that factor increases (e.g., if the supply of the production factor water decreases due to water scarcity, the price for the factor water increases). On the other hand, if demand goes down or supply increases, the price for the factor decreases. Factor prices can also be directly affected by economic scenarios (e.g., wage changes from new tariffs on labor).
                 """,
        data={
            "figu_03_01": Figure(
                df=scenario.df,
                figure_id="figu_03_01",
                caption=f"Commodity prices in percentage change to the base in the scenario <i>{scenario.name}</i>",
                notes="cagri = agricultural commodities (including commodities from fishery and forestry); cfood = processed food and beverages; cpetr = petroleum and petroleum products; aoind = commodities from other activities (including coal); celec = electricity; cwadi = distribution of piped water; csaco = collective sanitary service; csanc = non-collective sanitary service; ccons = construction service; ctran = transport service; cadmi = public services and administration; csefi = financial services (e.g., insurance, banking); csenf = non-financial services (e.g., tourism, trade); CPINppts = consumer price index change measured in percentage points; REU = Reunion Island."
            ),
            "figu_03_02": Figure(
                df=scenario.df,
                figure_id="figu_03_02",
                caption=f"Capital Rental Rate and Wage Rate (% change from base) in the scenario <i>{scenario.name}</i>",
                notes="The capital rental rates for non-water capital (incl. land, machines, buildings) are sector specific for the industries; aagri = agricultural production (including fishery and forestry); afood = food processing industries (including beverages); aoind = other industries; aelhy = electricity production based on renewable energies (hydro power, wind and solar); aelbi = electricity production based on biomass energy; aelpe = electricity production based on fossil fuel energy (petrol and coal); awasa = water, sanitary and waste sector; acons = construction sector; atran = transport sector; aadmi = public services and administration; asefi = financial services; asenf = not financial services (e.g., tourism or trade); WRLApric = wage rate for labour."
            ),
            "figu_03_03": Figure(
                df=scenario.df,
                figure_id="figu_03_03",
                caption=f"Ground Water Rental Rate in percentage change to the base in the scenario <i>{scenario.name}</i>",
                notes="The ground water rental rates is sector specific for the industries, which use ground water as a production factor: aagri = agricultural production (including fishery and forestry) as irrigation water; afood = food processing industries (including beverages); aoind = other industries; awasa = water, sanitary and waste sector, as input for piped water production."
            ),
            "figu_03_04": Figure(
                df=scenario.df,
                figure_id="figu_03_04",
                caption=f"Surface Water Rental Rate in percentage change to the base in the scenario  <i>{scenario.name}</i>",
                notes="The ground water rental rates is sector specific for the industries, which use ground water as a production factor: aagri = agricultural production (including fishery and forestry) as irrigation water; aelpe = electricity production based on fossil fuel energy (petrol and coal) as cooling water; awasa = water, sanitary and waste sector, as input for piped water production."
            ),
            "tabl_03_01": Table(
                df=scenario.df,
                table_id="tabl_03_01",
                caption=f"Commodity prices in percentage change to the base in the scenario <i>{scenario.name}</i>",
                notes="cagri = agricultural commodities (including commodities from fishery and forestry); cfood = processed food and beverages; cpetr = petroleum and petroleum products; aoind = commodities from other activities (including coal); celec = electricity; cwadi = distribution of piped water; csaco = collective sanitary service; csanc = non-collective sanitary service; ccons = construction service; ctran = transport service; cadmi = public services and administration; csefi = financial services (e.g., insurance, banking); csenf = non-financial services (e.g., tourism, trade); CPINppts = consumer price index change measured in percentage points; REU = Reunion Island"
            ),
            "tabl_03_02": Table(
                df=scenario.df,
                table_id="tabl_03_02",
                caption=f"Commodity Prices in percentage change to the base in the scenario <i>{scenario.name}</i>",
                notes="The capital rental rates for non-water capital (incl. land, machines, buildings) are sector specific for the industries; aagri = agricultural production (including fishery and forestry); afood = food processing industries (including beverages); aoind = other industries; aelhy = electricity production based on renewable energies (hydro power, wind and solar); aelbi = electricity production based on biomass energy; aelpe = electricity production based on fossil fuel energy (petrol and coal); awasa = water, sanitary and waste sector; acons = construction sector; atran = transport sector; aadmi = public services and administration; asefi = financial services;  asenf = not financial services (e.g., tourism or trade); WRLApric = wage rate for labour; RRCApric = capital rental rate; RRGWpric = ground water rental rate (factor price for ground water); RRSWpric = surface water rental rate (factor price for surface water); REU = Reunion Island."
            )
        },
        columns=[
            (["figu_03_01"], [1]),
            (["figu_03_02"], [1]),
            (["figu_03_03", "figu_03_04"], [1, 1]),
            (["tabl_03_01", "tabl_03_02"], [1, 1]),
        ],
    )