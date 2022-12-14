
class ImeCourse:
    COMPUTER_ENGINEERING = 'ENGENHARIA DA COMPUTAÇÃO'
    ELECTRICAL_ENGINEERING = 'ENGENHARIA ELÉTRICA'
    MECHANICAL_ENGINEERING = 'ENGENHARIA MECÂNICA'
    CIVIL_ENGINEERING = 'ENGENHARIA CIVIL'
    CHEMICAL_ENGINEERING = 'ENGENHARIA QUÍMICA'

    @classmethod
    def get_courses(cls) -> set[str]:
        return {cls.COMPUTER_ENGINEERING, cls.ELECTRICAL_ENGINEERING, cls.MECHANICAL_ENGINEERING, cls.CIVIL_ENGINEERING,
                cls.CHEMICAL_ENGINEERING,}
