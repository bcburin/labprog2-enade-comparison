from pandas import read_excel, DataFrame, concat


def read_enade_results(filepaths: [str]) -> DataFrame:
    results_df = DataFrame()
    for filepath in filepaths:
        df_yearly_results = read_excel(filepath)
        # Remove unwanted * symbols at the end of column names
        df_yearly_results = df_yearly_results.rename(
            axis=1, mapper=lambda col: col.split('*')[0])
        # Concatenate to total result
        results_df = concat([results_df,  df_yearly_results])
    return results_df
