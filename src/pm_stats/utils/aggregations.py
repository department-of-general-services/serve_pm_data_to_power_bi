from typing import List
import pandas as pd


def aggregate_wos_to_assets(
    work_orders: pd.DataFrame,
    agg_mapping: dict,
    vehicle_attributes: List["str"],
) -> pd.DataFrame:
    """Given a dataframe with data at the work order level, with multiple work orders
    for each asset, this function follows instructions supplied in the agg_mapping dict
    to create a dataframe with aggregated asset-level information.

    Args:
        work_orders (pd.DataFrame): Input dataframe with information at the work order level
        agg_mapping (dict): Dictionary with instructions for how to perform aggregation
        vehicle_attributes (list): List of columns to include that are the same for each wo

    Returns:
        pd.DataFrame: Output dataframe with information at the asset level
    """
    work_orders = work_orders.copy()
    # ensure that vehicle attributes get added to agg_mapping
    for attribute in vehicle_attributes:
        agg_mapping[attribute] = ["first"]
    assets = work_orders.groupby(by="asset_number")[
        list(agg_mapping.keys())
    ].agg(agg_mapping)
    # get rid of multilevel index
    assets.columns = assets.columns.map("_".join)
    # get rid of "_first" suffix for vehicle attributes
    assets.columns = [col.replace("_first", "") for col in assets.columns]
    return assets
