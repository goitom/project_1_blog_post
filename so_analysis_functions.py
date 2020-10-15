def collapse_cat_and_dummy(value_str, value_list):
    '''
    INPUT
        HomeRemoteStr - a string of one of the values from the column of interest

    OUTPUT
        return 1 if the string is in value_list
        return 0 otherwise
    '''
    if value_str in value_list:
        return 1
    else:
        return 0 
    
def get_description(column_name, schema):
    '''
    INPUT - schema - pandas dataframe with the schema of the developers survey
            column_name - string - the name of the column you would like to know about
    OUTPUT - 
            desc - string - the description of the column
    '''
    desc = schema['Question'][schema['Column']==column_name].values[0]
    return desc

def df_missingness_stats(df, year):
    df.name = year + ' data'
    print('Number of Rows in {}: {}'.format(df.name, df.shape[0]))
    print('Number of Columns in {}: {}'.format(df.name, df.shape[1]))
    print('Number of Columns in {} with no missing values: {}'.format(df.name, len(set(df.columns[~df.isnull().any()]))))
    print('Number of Columns in {} with > 75% missing values: {}'.format(df.name, 
                                                                         len(set(df.columns[df.isnull().sum()/len(df) > .75]))))
    print('Number of Columns in {} with all missing values: {}'.format(df.name, 
                                                                         len(set(df.columns[df.isnull().sum()/len(df) == 1]))))
    print('Columns in {} with no missing values: {}'.format(df.name, 
                                                            set(df.columns[~df.isnull().any()])))
    print('Columns in {} with > 75% missing values: {}'.format(df.name, 
                                                               set(df.columns[df.isnull().sum()/len(df) > .75])))
    
def recode_null_not_null_as_0_1(df, cols_not_to_recode):
    '''
    This function will split the data frame into columns that can easily be
    recoded as 0/1, and those that cannot. More specifically, if a column
    has a single non-NaN string value, and the relevant information is already contained
    in the column name, then it will convert that column to a 0/1 dummy
    '''
    
    # Split the dataframe into columns that will be operated on, and those that won't
    df_recode = df.drop(columns = cols_not_to_recode)
    df = df[cols_not_to_recode]
    df_recode = df_recode.notnull().astype('int')
    df = pd.concat([df, df_recode], axis=1)
    return df

def create_dummy_df(df, cols_to_dummy, dummy_na=True):
    '''
    INPUT:
    df - pandas dataframe with categorical variables you want to dummy
    cat_cols - list of strings that are associated with names of the categorical columns
    dummy_na - Bool holding whether you want to dummy NA vals of categorical columns or not
    
    OUTPUT:
    df - a new dataframe that has the following characteristics:
            1. contains all columns that were not specified as categorical
            2. removes all the original columns in cat_cols
            3. dummy columns for each of the categorical columns in cat_cols
            4. if dummy_na is True - it also contains dummy columns for the NaN values
            5. Use a prefix of the column name with an underscore (_) for separating 
    '''
    for col in cols_to_dummy:
        try:
            df = pd.concat([df.drop(col, axis=1), pd.get_dummies(df[col], 
                                                                 prefix=col, 
                                                                 prefix_sep='_', 
                                                                 drop_first=True,
                                                                 dummy_na=dummy_na
                                                                )], axis=1)
        except:
            continue

    return df

#creating labelEncoder
def process_y_var_split_data(df, yvar):
    df[yvar] = df[yvar].str.replace('<', 'less than ')
    df[yvar] = df[yvar].str.replace('>', 'greater than ')
    df[yvar] = df[yvar].astype('str')
    df = df[df[yvar]!='nan']
    
    print(df[yvar].value_counts())
    le = preprocessing.LabelEncoder()
    X = df.drop(columns=[yvar])
    y = le.fit_transform(df[yvar])
    
    return X, y 
