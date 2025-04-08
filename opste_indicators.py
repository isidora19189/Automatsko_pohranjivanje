indicators = ['NGDP_RPCH', 'NGDPD', 'NGDPDPC',
              'BCA', 'BCA_NGDPD',
              'PCPIPCH', 'PCPIEPCH',
              'GGXWDG_NGDP', 'LP', 'LUR',
              'GGR_G01_GDP_PT','G_X_G01_GDP_PT', 'GGXWDN_G01_GDP_PT'
              ]

"" 'DirectIn', 'rev', 'exp', 'd'

indicator_dict = {
    "NGDP_RPCH": {
      "label": "Real GDP growth",
      "description": "Gross domestic product is the most commonly used single measure of a country's overall economic activity. It represents the total value at constant prices of final goods and services produced within a country during a specified time period, such as one year.",
      "source": "World Economic Outlook (October 2024)",
      "unit": "Annual percent change",
      "dataset": "WEO"
    },
    "NGDPD": {
      "label": "GDP, current prices",
      "description": "Gross domestic product is the most commonly used single measure of a country's overall economic activity. It represents the total value at current prices of final goods and services produced within a country during a specified time period, such as one year.",
      "source": "World Economic Outlook (October 2024)",
      "unit": "Billions of U.S. dollars",
      "dataset": "WEO"
    },"BCA": {
      "label": "Current account balance",
      "description": "The current account is the record of all transactions in the balance of payments covering the exports and imports of goods and services, payments of income, and current transfers between residents of a country and nonresidents.",
      "source": "World Economic Outlook (October 2024)",
      "unit": "Billions of U.S. dollars",
      "dataset": "WEO"
    },
    "BCA_NGDPD": {
      "label": "Current account balance, percent of GDP",
      "description": "The current account is the record of all transactions in the balance of payments covering the exports and imports of goods and services, payments of income, and current transfers between residents of a country and nonresidents.",
      "source": "World Economic Outlook (October 2024)",
      "unit": "Percent of GDP",
      "dataset": "WEO"
    },"DirectIn": {
      "label": "Direct Investment In Country",
      "description": None,
      "source": "Capital Flows in Developing Economies",
      "unit": "Millions of US Dollars",
      "dataset": "CF"
    },"PCPIPCH": {
      "label": "Inflation rate, average consumer prices",
      "description": "The average consumer price index (CPI) is a measure of a country's average level of prices based on the cost of a typical basket of consumer goods and services in a given period. The rate of inflation is the percent change in the average CPI.\n \n",
      "source": "World Economic Outlook (October 2024)",
      "unit": "Annual percent change",
      "dataset": "WEO"
    },
    "PCPIEPCH": {
      "label": "Inflation rate, end of period consumer prices",
      "description": "The end of period consumer price index (CPI) is a measure of a country's general level of prices based on the cost of a typical basket of consumer goods and services at the end of a given period. The rate of inflation is the percent change in the end of period CPI.\n \n",
      "source": "World Economic Outlook (October 2024)",
      "unit": "Annual percent change",
      "dataset": "WEO"
    },"rev": {
      "label": "Government revenue, percent of GDP",
      "description": "Government revenue, percent of GDP",
      "source": "Public Finances in Modern History Database (Feb 2025)",
      "unit": "% of GDP",
      "dataset": "FPP"
    },
    "exp": {
      "label": "Government expenditure, percent of GDP",
      "description": "Government expenditure, percent of GDP",
      "source": "Public Finances in Modern History Database (Feb 2025)",
      "unit": "% of GDP",
      "dataset": "FPP"
    },"d": {
      "label": "Gross public debt, percent of GDP",
      "description": "Gross public debt, percent of GDP",
      "source": "Public Finances in Modern History Database (Feb 2025)",
      "unit": "% of GDP",
      "dataset": "FPP"
    },
    "LUR": {
      "label": "Unemployment rate",
      "description": "The number of unemployed persons as a percentage of the total labor force.",
      "source": "World Economic Outlook (October 2024)",
      "unit": "Percent",
      "dataset": "WEO"
    },
    "LP": {
      "label": "Population",
      "description": "Total population of a country, region, or group of countries.",
      "source": "World Economic Outlook (October 2024)",
      "unit": "Millions of people",
      "dataset": "WEO"
    },
    "GGXWDG_NGDP": {
      "label": "General government gross debt",
      "description": "Gross debt consists of all liabilities that require payment or payments of interest and/or principal by the debtor to the creditor at a date or dates in the future. This includes debt liabilities in the form of SDRs, currency and deposits, debt securities, loans, insurance, pensions and standardized guarantee schemes, and other accounts payable. Thus, all liabilities in the GFSM 2001 system are debt, except for equity and investment fund shares and financial derivatives and employee stock options. Debt can be valued at current market, nominal, or face values (GFSM 2001, paragraph 7.110).",
      "source": "World Economic Outlook (October 2024)",
      "unit": "Percent of GDP",
      "dataset": "WEO"
    },
    "GGR_G01_GDP_PT": {
      "label": "Revenue",
      "description": "Revenue",
      "source": "Fiscal Monitor (October 2024)",
      "unit": "% of GDP",
      "dataset": "FM"
    },
    "G_X_G01_GDP_PT": {
      "label": "Expenditure",
      "description": "Expenditure",
      "source": "Fiscal Monitor (October 2024)",
      "unit": "% of GDP",
      "dataset": "FM"
    },
    "GGXWDN_G01_GDP_PT": {
      "label": "Net debt",
      "description": "Gross debt minus financial assets corresponding to debt instruments. These financial assets are: monetary gold and SDRs, currency and deposits, debt securities, loans, insurance, pension, and standardized guarantee schemes, and other accounts receivable. In some countries the reported net debt can deviate from this definition on the basis of available information and national fiscal accounting practices.",
      "source": "Fiscal Monitor (October 2024)",
      "unit": "% of GDP",
      "dataset": "FM"
    },
    "NGDPDPC": {
      "label": "GDP per capita, current prices\n",
      "description": "Gross domestic product is the most commonly used single measure of a country's overall economic activity. It represents the total value at current prices of final goods and services produced within a country during a specified time period divided by the average population for the same one year.",
      "source": "World Economic Outlook (October 2024)",
      "unit": "U.S. dollars per capita",
      "dataset": "WEO"
    }
}