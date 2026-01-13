


def data_clean(df):


    # Handling missing values using mean, median, or mode
    df['ssc_percentage'].fillna(df['ssc_percentage'].median(), inplace=True)
    df['hsc_percentage'] = df['hsc_percentage'].fillna(df['hsc_percentage'].mean(), inplace=False)
    df['relocation_willingness'] = df['relocation_willingness'].fillna(df['relocation_willingness'].mode(), inplace=False)
    df['notice_period_days'] = df['notice_period_days'].fillna(df['notice_period_days'].median(), inplace=False)
    # df['relevant_experience'] = df['relevant_experience'].#df is your dataframe
    df['relevant_experience'] = df['relevant_experience'].fillna(df['relevant_experience'].mode(), inplace=False)
    df['career_switch_willingness'] = df['career_switch_willingness'].fillna(df['career_switch_willingness'].median().round(1), inplace=False)
    

    df['gender'] = df['gender'].str.lower().str.strip()
    df['relocation_willingness'] = df['relocation_willingness'].str.lower().str.strip()

    return df
