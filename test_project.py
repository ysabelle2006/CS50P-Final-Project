import pytest
from project import check_textin
from project import rankingpts
from project import handle_drawrank

def test_check_textin():
    assert check_textin("a",r"^([ABCDEFGH])$") == ("A",)
    assert check_textin("H",r"^([ABCDEFGH])$") == ("H",)
    assert check_textin("por-bel",r"^(\w{3}) ?- ?(\w{3})$") == ("POR","BEL")
    assert check_textin("por - bel",r"^(\w{3}) ?- ?(\w{3})$") == ("POR","BEL")
    assert check_textin("w-l",r"^([WDL]+) ?- ?([WDL]+)$") == ("W","L")
    assert check_textin("d - d",r"^([WDL]+) ?- ?([WDL]+)$") == ("D","D")
    with pytest.raises(ValueError):
        check_textin("p",r"^([ABCDEFGH])$")

    with pytest.raises(ValueError):
        check_textin("",r"^([ABCDEFGH])$")

    with pytest.raises(ValueError):
        check_textin("0-0",r"^(\w{3}) ?- ?(\w{3})$")

    with pytest.raises(ValueError):
        check_textin("o:o",r"^(\w{3}) ?- ?(\w{3})$")



def test_rankingpts():
    assert rankingpts({'QAT': {'pts': 0, 'gs': 0, 'gc': 0}, 'SEN': {'pts': 6, 'gs': 0, 'gc': 0}, 'ECU': {'pts': 4, 'gs': 0, 'gc': 0}, 'NED': {'pts': 7, 'gs': 0, 'gc': 0}}) == ([[1, 'NED'], [2, 'SEN'], [3, 'ECU'], [4, 'QAT']],[('NED', {'pts': 7, 'gs': 0, 'gc': 0}), ('SEN', {'pts': 6, 'gs': 0, 'gc': 0}), ('ECU', {'pts': 4, 'gs': 0, 'gc': 0}), ('QAT', {'pts': 0, 'gs': 0, 'gc': 0})])
    assert rankingpts({'WAL': {'pts': 1, 'gs': 0, 'gc': 0}, 'ENG': {'pts': 7, 'gs': 0, 'gc': 0}, 'USA': {'pts': 5, 'gs': 0, 'gc': 0}, 'IRN': {'pts': 3, 'gs': 0, 'gc': 0}}) == ([[1, 'ENG'], [2, 'USA'], [3, 'IRN'], [4, 'WAL']],[('ENG', {'pts': 7, 'gs': 0, 'gc': 0}), ('USA', {'pts': 5, 'gs': 0, 'gc': 0}), ('IRN', {'pts': 3, 'gs': 0, 'gc': 0}), ('WAL', {'pts': 1, 'gs': 0, 'gc': 0})])

    assert rankingpts({'KSA': {'pts': 3, 'gs': 0, 'gc': 0}, 'MEX': {'pts': 4, 'gs': 0, 'gc': 0}, 'ARG': {'pts': 6, 'gs': 0, 'gc': 0}, 'POL': {'pts': 4, 'gs': 0, 'gc': 0}}) == ([[1, 'ARG'], [2, 'MEX'], [3, 'POL'], [4, 'KSA']],[('ARG', {'pts': 6, 'gs': 0, 'gc': 0}), ('MEX', {'pts': 4, 'gs': 0, 'gc': 0}), ('POL', {'pts': 4, 'gs': 0, 'gc': 0}), ('KSA', {'pts': 3, 'gs': 0, 'gc': 0})])
    assert rankingpts({'QAT': {'pts': 3, 'gs': 0, 'gc': 0}, 'SEN': {'pts': 3, 'gs': 0, 'gc': 0}, 'ECU': {'pts': 3, 'gs': 0, 'gc': 0}, 'NED': {'pts': 3, 'gs': 0, 'gc': 0}}) == ([[1, 'QAT'], [2, 'SEN'], [3, 'ECU'], [4, 'NED']],[('QAT', {'pts': 3, 'gs': 0, 'gc': 0}), ('SEN', {'pts': 3, 'gs': 0, 'gc': 0}), ('ECU', {'pts': 3, 'gs': 0, 'gc': 0}), ('NED', {'pts': 3, 'gs': 0, 'gc': 0})])



def test_handle_drawrank():
    assert handle_drawrank([('ARG', {'pts': 6, 'gs': 0, 'gc': 0}), ('MEX', {'pts': 4, 'gs': 0, 'gc': 0}), ('POL', {'pts': 4, 'gs': 0, 'gc': 0}), ('KSA', {'pts': 3, 'gs': 0, 'gc': 0})],[[1, 'ARG'], [2, 'MEX'], [3, 'POL'], [4, 'KSA']]) == [[1, 'ARG'], [2, 'MEX'], [2, 'POL'], [4, 'KSA']]
    assert handle_drawrank([('NED', {'pts': 7, 'gs': 0, 'gc': 0}), ('SEN', {'pts': 6, 'gs': 0, 'gc': 0}), ('ECU', {'pts': 4, 'gs': 0, 'gc': 0}), ('QAT', {'pts': 0, 'gs': 0, 'gc': 0})],[[1, 'NED'], [2, 'SEN'], [3, 'ECU'], [4, 'QAT']]) == [[1, 'NED'], [2, 'SEN'], [3, 'ECU'], [4, 'QAT']]
    assert handle_drawrank([('FRA', {'pts': 3, 'gs': 0, 'gc': 0}), ('DEN', {'pts': 3, 'gs': 0, 'gc': 0}), ('AUS', {'pts': 3, 'gs': 0, 'gc': 0}), ('TUN', {'pts': 3, 'gs': 0, 'gc': 0})],[[1, 'FRA'], [2, 'DEN'], [3, 'AUS'], [4, 'TUN']]) == [[1, 'FRA'], [1, 'DEN'], [1, 'AUS'], [1, 'TUN']]
