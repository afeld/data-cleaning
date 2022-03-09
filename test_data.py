import pandas as pd
import pytest
from pytest import approx


@pytest.fixture
def df():
    return pd.read_csv("311_jan_2022.csv")


def test_num_columns(df):
    assert len(df.columns) == 41


def test_lat_lng(df):
    """Test that the points are in the NYC area"""
    # https://www.latlong.net/place/new-york-city-ny-usa-1848.html
    # https://docs.pytest.org/en/latest/reference/reference.html?highlight=within#pytest-approx
    assert df["Latitude"].median() == approx(40.730610, rel=1e-3)
    assert df["Longitude"].median() == approx(-73.935242, rel=1e-3)
