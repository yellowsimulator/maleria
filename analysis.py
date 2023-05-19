import pandas as pd
import matplotlib.pyplot as plt



def get_data(county_code):
    """Reads the data from the csv file 
       and returns it as a pandas dataframe
    """
    #data = pd.read_csv('data/malaria.csv', sep=',', skiprows=2, header=0)
    data = pd.read_csv('data/malaria.csv', sep=',', skiprows=4, index_col=0)
    df  = data.loc[:, ~data.columns.str.contains('^Unnamed')]
    years = [str(x) for x in range(2000, 2022)]
    
    df = df[df['Country Code'] == county_code]
    incidence = df[years].values
    return years, incidence[0]


if __name__=='__main__':
    country_code = 'KEN'
    years, incidence = get_data(country_code)
    # add plot size
    plt.figure(figsize=(15, 5))
    plt.plot(years, incidence)
    plt.xlabel('Year')
    plt.ylabel('Incidence')
    plt.title('Malaria Incidence in Kenya. World Bank Data')
    plt.show()
   