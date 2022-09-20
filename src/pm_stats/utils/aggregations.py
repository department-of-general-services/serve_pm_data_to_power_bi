import pandas as pd


def aggregate_wos_to_assets(
    work_orders: pd.DataFrame, agg_mapping: dict
) -> pd.DataFrame:
    """Given a dataframe with data at the work order level, with multiple work orders
    for each asset, this function follows instructions supplied in the agg_mapping dict
    to create a dataframe with aggregated asset-level information.

    Args:
        work_orders (pd.DataFrame): Input dataframe with information at the work order level
        agg_mapping (dict): Dictionary with instructions for how to perform aggregation

    Returns:
        pd.DataFrame: Output dataframe with information at the asset level
    """
    work_orders = work_orders.copy()
    assets = work_orders.groupby(by="asset_number")[
        list(agg_mapping.keys())
    ].agg(agg_mapping)
    # get rid of multilevel index
    assets.columns = assets.columns.map("_".join)
    return assets
