def feature_engineering(df):

    def exp_category(x):
        if x == 0:
            return "Fresher"
        elif x <= 3:
            return "junior"
        else:
            return "senior"
        
    df['experience_category'] = df['experience'].apply(exp_category)

    def skill_level(x):
        if x < 50:
            return "low"
        elif x < 75:
            return "medium"
        else:
            return "high"
        
    df['skill_match_level'] = df['skills_match_percentage'].apply(skill_level)

    return df
  
