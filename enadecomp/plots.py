from pandas import DataFrame


def transform_comparison_multiindex_to_cols(df_comparison: DataFrame) -> DataFrame:
    institutions = set(df_comparison.index.get_level_values(1))
    df_transformed = DataFrame(
        data={
            institution: df_comparison['Mean'][df_comparison.index.map(lambda key: key[1] == institution)].droplevel(1)
            for institution in institutions
        },
    )
    return df_transformed


def plot_institution_comparison_to_others(df_comparison: DataFrame, path: str) -> None:
    df_transformed = transform_comparison_multiindex_to_cols(df_comparison=df_comparison)
    df_transformed.plot(kind='bar').figure.savefig(path, bbox_inches='tight')


def plot_institution_comparison_yearly(df_comparison: DataFrame, path: str) -> None:
    df_comparison.plot(kind='bar').figure.savefig(path, bbox_inches='tight')

