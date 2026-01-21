import matplotlib.pyplot as plt
import seaborn as sns

def perform_data(df):

    sns.boxplot(x='status', y='interview_score', data=df)
    plt.title("Interview Score vs Job Acceptance")
    plt.show()


    plt.figure(figsize=(6,4))
    sns.boxplot(x='status', y='skills_match_percentage', data=df)
    plt.title("Skills match percentage impact on placement")
    plt.show()

    tier_acceptance = df.groupby("company_tier")["status"].mean().reset_index()
    plt.figure(figsize=(6,4))
    sns.barplot(x='company_tier', y = 'status', data=tier_acceptance)
    plt.title("Company tier vs acceptance rate")
    plt.show()

    plt.figure(figsize=(6,4))
    sns.countplot(x='years_of_experience', hue='status', data=df)
    plt.title("Experience vs placement probability")
    plt.show()

    plt.figure(figsize=(6,4))
    sns.barplot(x='competition_level', y='status' , data=df)
    plt.title("Competition level vs job acceptance")
    plt.show()

    plt.figure(figsize=(10,6))
    corr = df.corr(numeric_only=True)
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title("Correlation Heatmap")
    plt.show()



