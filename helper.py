import pandas as pd


def transform_d(data, column_name, categories, is_ordinal = False, asserted = True):
    
    df = data.copy(deep = True)
    
    if asserted:
        assert df[column_name].apply(lambda x: x in categories).all(), df[column_name].iloc[0]
    
    column_series = df[column_name]
    df.drop(column_name, axis = 1, inplace = True)
    
    if is_ordinal:

        d = {x : i + 1 for i, x in enumerate(categories)}
        column_series.replace(d, inplace = True)
        
        df[column_name] = column_series
    
    else:
        
        columns = [f'{column_name}: {x}' for x in categories]
        temp_df = column_series.apply(lambda x: pd.Series([int(y == x) for y in categories]))
        temp_df.columns = columns
        
        df = df.join(temp_df)
        
    return df
        
        
def transform_c(data, column_name):
    
    df = data.copy(deep = True)
    
    column_series = df[column_name]
    df.drop(column_name, axis = 1, inplace = True)
    df[column_name] = column_series
    
    return df
    
    
def transform(data, column_name, categories = None, is_ordinal = False, asserted = True):

    if categories is None:
        
        return transform_c(data, column_name)
        
    return transform_d(data, column_name, categories, is_ordinal, asserted)
    

def transform_features(X):
    
        
    #Column: country
    
    categories = ['Albania', 'Antigua and Barbuda', 'Argentina', 'Armenia',
                  'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain',
                  'Barbados', 'Belarus', 'Belgium', 'Belize',
                  'Bosnia and Herzegovina', 'Brazil', 'Bulgaria', 'Cabo Verde',
                  'Canada', 'Chile', 'Colombia', 'Costa Rica', 'Croatia', 'Cuba',
                  'Cyprus', 'Czechia', 'Denmark', 'Ecuador', 'El Salvador',
                  'Estonia', 'Fiji', 'Finland', 'France', 'Georgia', 'Germany',
                  'Greece', 'Grenada', 'Guatemala', 'Guyana', 'Hungary', 'Iceland',
                  'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Kazakhstan',
                  'Kiribati', 'Kuwait', 'Kyrgyzstan', 'Latvia', 'Lithuania',
                  'Luxembourg', 'Maldives', 'Malta', 'Mauritius', 'Mexico',
                  'Mongolia', 'Montenegro', 'Netherlands', 'New Zealand',
                  'Nicaragua', 'Norway', 'Oman', 'Panama', 'Paraguay', 'Philippines',
                  'Poland', 'Portugal', 'Qatar', 'Korea', 'Romania',
                  'Russian Federation', 'Saint Lucia',
                  'Saint Vincent and the Grenadines', 'Serbia', 'Seychelles',
                  'Singapore', 'Slovakia', 'Slovenia', 'South Africa', 'Spain',
                  'Sri Lanka', 'Suriname', 'Sweden', 'Switzerland', 'Thailand',
                  'Trinidad and Tobago', 'Turkey', 'Turkmenistan', 'Ukraine',
                  'United Arab Emirates', 'United Kingdom', 'United States',
                  'Uruguay', 'Uzbekistan']
    
    df = transform(data = X,
                   column_name = 'country', 
                   categories = categories, 
                   is_ordinal = False,
                   asserted = True)
    
    ############################################
    
    #Column: year
    
    df = transform(data = df,
                   column_name = 'year')
    
    ############################################
    
    #Column: sex
    
    df = transform(data = df, 
                   column_name = 'sex', 
                   categories = ['male'], 
                   is_ordinal = False,
                   asserted = False)
    
    ############################################
    
    #Column: age
    
    categories = ['5-14', '15-24', '25-34',
                  '35-54', '55-74', '75+']
    
    df = transform(data = df, 
                   column_name = 'age', 
                   categories = categories, 
                   is_ordinal = False,
                   asserted = True)
    
    ############################################  
    #Column: population
    
    df = transform(data = df,
                   column_name = 'population')  
    
    ############################################
    
    #Column: HDI for year
    df = transform(data = df,
                   column_name = 'HDI')
    
    ############################################
    #Column: gdp_per_capita
    
    df = transform(data = df,
                   column_name = 'gdp_per_capita')

    return df