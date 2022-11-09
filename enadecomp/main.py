from os import getcwd, path, pardir, listdir

from enadecomp.readers import read_enade_results
from enadecomp.comparators import compare_institution_to_others, compare_institution_course_yearly
from enadecomp.enums import ImeCourse
from enadecomp.plots import plot_institution_comparison_to_others, plot_institution_comparison_yearly


if __name__ == '__main__':
    # Define working directories
    curr_dir = getcwd()
    data_dir = path.abspath(path.join(curr_dir, pardir, 'data'))
    input_dir = path.join(data_dir, 'enade')
    output_dir = path.join(data_dir, 'out')
    # Load input data
    filepaths = [path.join(input_dir, name) for name in listdir(input_dir)]
    df_results = read_enade_results(filepaths=filepaths)
    # Compare institutions to IME
    df_comparison = compare_institution_to_others(
        df_results=df_results,
        institution_symbol='IME',
        courses=ImeCourse.get_courses(),
    )
    plot_institution_comparison_to_others(
        df_comparison=df_comparison,
        path=path.join(output_dir, 'ime_to_others_comparison.png'),
    )
    # Compare IME courses yearly
    for course in ImeCourse.get_courses():
        df_comparison_yearly = compare_institution_course_yearly(
            df_results=df_results,
            institution_symbol='IME',
            course=course
        )
        plot_institution_comparison_yearly(
            df_comparison=df_comparison_yearly,
            path=path.join(output_dir, course + ' - Yearly.png')
        )




