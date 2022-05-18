import json

from assertpy import assert_that, soft_assertions


def assert_mapview_kpistatistics_widget(json_response, expectedDict):
    actual_unit = json_response["tabs"][0]["unit"]
    expected_unit = expectedDict['unit']
    actual_p10 = json_response["tabs"][0]["data"][0]["kpiValueColumn"]
    expected_p10 = expectedDict['p10']
    actual_p50 = json_response["tabs"][0]["data"][1]["kpiValueColumn"]
    expected_p50 = expectedDict['p50']
    actual_p90 = json_response["tabs"][0]["data"][2]["kpiValueColumn"]
    expected_p90 = expectedDict['p90']
    actual_KPIValue = json_response["tabs"][0]["data"][3]["kpiValueColumn"]
    expected_KPIValue = expectedDict['KPIValue']
    actual_AvgUserCount = json_response["tabs"][0]["data"][4]["kpiValueColumn"]
    expected_AvgUserCount = expectedDict['AvgUserCount']
    actual_SampleCount = json_response["tabs"][0]["data"][5]["kpiValueColumn"]
    expected_SampleCount = expectedDict['SampleCount']

    with soft_assertions():
        assert_that(actual_unit).described_as('Unit validation').is_equal_to(expected_unit)
        assert_that(actual_p10).described_as('P10 validation').is_equal_to(expected_p10)
        assert_that(actual_p50).described_as('P50 validation').is_equal_to(expected_p50)
        assert_that(actual_p90).described_as('P90 validation').is_equal_to(expected_p90)
        assert_that(actual_KPIValue).described_as('KPIValue validation').is_equal_to(expected_KPIValue)
        assert_that(actual_AvgUserCount).described_as('AvgUserCount validation').is_equal_to(expected_AvgUserCount)
        assert_that(actual_SampleCount).described_as('SampleCount validation').is_equal_to(expected_SampleCount)


def validate_status_code_200(status_code):
    with soft_assertions():
        assert_that(status_code).described_as('status_code').is_equal_to(200)


