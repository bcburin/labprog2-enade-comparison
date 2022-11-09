from typing import Iterable

from pandas import DataFrame
from numpy import mean, std, median, var


CONTINUOUS_RESULT_COL = 'Conceito Enade (Contínuo)'
INSTITUTION_SYMBOL_COL = 'Sigla da IES'
COURSE_COL = 'Área de Avaliação'
IS_IME_COL = 'IsIME'


def compare_institution_to_others(
        df_results: DataFrame,
        institution_symbol: str,
        result_col: str = CONTINUOUS_RESULT_COL,
        courses: Iterable[str] | None = None
) -> DataFrame:
    # Filter by course if courses are given
    if courses:
        if not isinstance(courses, set):
            # Optimize lookup
            courses = set(courses)
        df_results = df_results[df_results[COURSE_COL].apply(lambda course: course in courses)]
    # Create a column to partition institutions into the specified one and others
    df_results[IS_IME_COL] = df_results[INSTITUTION_SYMBOL_COL].apply(
        lambda symbol: symbol if symbol == institution_symbol else 'Other')
    # Calculate statistics for the groups of the specified institution and "Other"
    df_stats: DataFrame = (
        df_results[[COURSE_COL, IS_IME_COL, result_col]]
        .groupby(by=[COURSE_COL, IS_IME_COL])
        .agg(
            Mean=(result_col, mean),
            StdDev=(result_col, std),
            Median=(result_col, median),
            Var=(result_col, var)
        )
    )
    return df_stats


def compare_institution_course_yearly(
        df_results: DataFrame,
        institution_symbol: str,
        course: str,
        result_col: str = CONTINUOUS_RESULT_COL,
) -> DataFrame:
    df_results = df_results[df_results[INSTITUTION_SYMBOL_COL] == institution_symbol]
    df_results = df_results[df_results[COURSE_COL] == course]
    df_comparison = df_results[['Ano', result_col]].groupby(['Ano']).mean()
    return df_comparison


