# Test Module to test Mapview Dashboard - KPI Statistics Widget
import pytest
import requests
from testcases.helpers import *
from testcases.assertions.assertion import *


class TestMapview:
    # test suit for mapview - kpi statistics widget (data driven - parameterization concept used)
    @pytest.mark.parametrize("requestDict , expectedDict", input_request())
    @pytest.mark.Mapview_widget_kpiStatisticsc
    def test_mapview_widget_kpiStatistics(self, requestDict, expectedDict, session_auth, define_logger):
        try:
            url, headers = session_auth
            logger = define_logger
            logger.info("input_json: "+str(requestDict))
            resp = requests.post(url, json=requestDict, headers=headers, verify=False)
            json_response = resp.json()
            logger.info("response: "+resp.text)
            validate_status_code_200(resp.status_code)
            logger.info("status_code: "+str(resp.status_code))
            if assert_mapview_kpistatistics_widget(json_response, expectedDict):
                pass
            else:
                logger.info("All Validations : Passed")
        except AssertionError:
            logger.error("Error Occurred..", exc_info=True)
            raise
